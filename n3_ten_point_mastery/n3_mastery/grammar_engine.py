"""Grammar Curriculum, Question Anatomy Links, Independent Grammar FSRS & Vocab Foundation Engine."""

import hashlib
import importlib
import json
import re
import sqlite3
import tempfile
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

from n3_mastery.config import (
    INITIAL_STABILITY_DAYS,
    MAX_DIFFICULTY,
    MIN_DIFFICULTY,
)
from n3_mastery.database import get_connection, init_db, transaction
from n3_mastery.drill_engine import permute_options
from n3_mastery.fsrs_adaptive import (
    compute_horizon_interval,
    compute_retrievability,
    format_iso,
    get_pace_settings,
    parse_iso,
    utc_now,
)
from n3_mastery.models import Rating

LEVEL_ORDER = ("N5", "N4", "N3", "N2", "N1")
VALID_LEVELS = set(LEVEL_ORDER)
VALID_ROLES = {"primary_target", "distractor_trap", "sentence_structure", "discourse_marker"}
VALID_DRILL_TYPES = {"formation", "contrast", "application"}

LEVEL_LABELS_VI = {
    "N5": "N5 — Nền tảng Cốt lõi (Trợ từ & Chia thể)",
    "N4": "N4 — Bắc cầu (Khả năng, Sai khiến, Bị động)",
    "N3": "N3 — Trọng tâm Đề thi Cuối kì & JLPT",
    "N2": "N2 — Mở rộng Trung-Cao cấp",
    "N1": "N1 — Mở rộng Cao cấp",
}

DRILL_TYPE_LABELS_VI = {
    "formation": "Chia thể & Kết hợp",
    "contrast": "Phân biệt cặp dễ nhầm",
    "application": "Ứng dụng ngữ cảnh",
}


def _load_grammar_corpus():
    try:
        importlib.invalidate_caches()
        return importlib.import_module("n3_mastery.grammar_corpus")
    except ImportError:
        return None


def _load_question_grammar_map():
    try:
        importlib.invalidate_caches()
        return importlib.import_module("n3_mastery.question_grammar_map")
    except ImportError:
        return None


def _safe_json_loads(raw: Any, default: Any) -> Any:
    if raw is None or raw == "":
        return default
    if isinstance(raw, (list, dict)):
        return raw
    try:
        return json.loads(raw)
    except (TypeError, ValueError):
        return default


def _normalize_word_key(word: str) -> str:
    return re.sub(r"[\s\u3000・]+", "", str(word or "")).lower()


def _make_exam_vocab_key(word: str) -> str:
    digest = hashlib.sha256(str(word).encode("utf-8")).hexdigest()[:12]
    return f"exam-{digest}"


def is_grammar_mastered(fsrs_row: Dict[str, Any], available_drill_types: Optional[set] = None) -> bool:
    """True iff grammar point is in active review, reps >= 2, stability >= 2.0, and available drill types passed."""
    if str(fsrs_row.get("state", "new")) != "review":
        return False
    if int(fsrs_row.get("reps", 0)) < 2 or float(fsrs_row.get("stability", 0.0)) < 2.0:
        return False
    if available_drill_types:
        flag_map = {
            "formation": bool(fsrs_row.get("formation_passed", 0)),
            "contrast": bool(fsrs_row.get("contrast_passed", 0)),
            "application": bool(fsrs_row.get("application_passed", 0)),
        }
        return all(flag_map.get(dt, False) for dt in available_drill_types)
    return (
        bool(fsrs_row.get("formation_passed", 0))
        or bool(fsrs_row.get("contrast_passed", 0))
        or bool(fsrs_row.get("application_passed", 0))
    )


def _format_grammar_fsrs(row: Any, available_drill_types: Optional[set] = None) -> Dict[str, Any]:
    d = dict(row)
    state = str(d.get("state") or "new")
    reps = int(d.get("reps") or 0)
    lapses = int(d.get("lapses") or 0)
    stability = float(d.get("stability") if d.get("stability") is not None else 0.5)
    difficulty = float(d.get("difficulty") if d.get("difficulty") is not None else 5.0)
    f_pass = bool(d.get("formation_passed"))
    c_pass = bool(d.get("contrast_passed"))
    a_pass = bool(d.get("application_passed"))
    mastered = is_grammar_mastered(
        {
            "state": state,
            "reps": reps,
            "stability": stability,
            "formation_passed": f_pass,
            "contrast_passed": c_pass,
            "application_passed": a_pass,
        },
        available_drill_types=available_drill_types,
    )
    return {
        "stability": stability,
        "difficulty": difficulty,
        "reps": reps,
        "lapses": lapses,
        "state": state,
        "formation_passed": f_pass,
        "contrast_passed": c_pass,
        "application_passed": a_pass,
        "mastered": mastered,
        "last_review": d.get("last_review"),
        "due_date": d.get("due_date"),
    }


def _upsert_grammar_point(conn: sqlite3.Connection, gp: Dict[str, Any]) -> int:
    code = str(gp.get("code", "")).strip()
    pattern = str(gp.get("pattern", "")).strip()
    if not code or not pattern:
        raise ValueError("Điểm ngữ pháp bắt buộc phải có 'code' và 'pattern'.")

    level = str(gp.get("jlpt_level", "N3")).strip().upper()
    if level not in VALID_LEVELS:
        raise ValueError(f"Cấp độ JLPT không hợp lệ cho '{code}': {level}")

    category = str(gp.get("category", "general")).strip() or "general"
    category_label_vi = str(gp.get("category_label_vi", category)).strip() or category
    in_exam = 1 if gp.get("in_exam_corpus") else 0
    formation_formula = str(gp.get("formation_formula", "")).strip() or pattern
    formation_table = gp.get("formation_table", [])
    core_meaning_vi = str(gp.get("core_meaning_vi", "")).strip()
    deep_explanation_vi = str(gp.get("deep_explanation_vi", "")).strip() or core_meaning_vi
    register_tag = str(gp.get("register_tag", "")).strip()
    confusable_pairs = gp.get("confusable_pairs", [])
    examples = gp.get("examples", [])
    source_ref = str(gp.get("source_ref", "")).strip()
    search_keywords = str(gp.get("search_keywords", "")).strip()

    conn.execute(
        """
        INSERT INTO GRAMMAR_POINTS (
            code, pattern, jlpt_level, category, category_label_vi, in_exam_corpus,
            formation_formula, formation_table_json, core_meaning_vi, deep_explanation_vi,
            register_tag, confusable_pairs_json, examples_json, source_ref, search_keywords
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(code) DO UPDATE SET
            pattern=excluded.pattern,
            jlpt_level=excluded.jlpt_level,
            category=excluded.category,
            category_label_vi=excluded.category_label_vi,
            in_exam_corpus=excluded.in_exam_corpus,
            formation_formula=excluded.formation_formula,
            formation_table_json=excluded.formation_table_json,
            core_meaning_vi=excluded.core_meaning_vi,
            deep_explanation_vi=excluded.deep_explanation_vi,
            register_tag=excluded.register_tag,
            confusable_pairs_json=excluded.confusable_pairs_json,
            examples_json=excluded.examples_json,
            source_ref=excluded.source_ref,
            search_keywords=excluded.search_keywords
        """,
        (
            code,
            pattern,
            level,
            category,
            category_label_vi,
            in_exam,
            formation_formula,
            json.dumps(formation_table, ensure_ascii=False),
            core_meaning_vi,
            deep_explanation_vi,
            register_tag,
            json.dumps(confusable_pairs, ensure_ascii=False),
            json.dumps(examples, ensure_ascii=False),
            source_ref,
            search_keywords,
        ),
    )
    gp_id = int(conn.execute("SELECT id FROM GRAMMAR_POINTS WHERE code=?", (code,)).fetchone()[0])
    conn.execute("INSERT OR IGNORE INTO GRAMMAR_FSRS_STATES (grammar_id) VALUES (?)", (gp_id,))
    return gp_id


def _upsert_grammar_drill(
    conn: sqlite3.Connection,
    drill: Dict[str, Any],
    code_to_id: Dict[str, int],
    fallback_idx: int = 0,
) -> Optional[int]:
    g_code = str(drill.get("grammar_code", "")).strip()
    grammar_id = code_to_id.get(g_code)
    if grammar_id is None:
        return None

    drill_type = str(drill.get("drill_type", "application")).strip().lower()
    if drill_type not in VALID_DRILL_TYPES:
        raise ValueError(f"drill_type không hợp lệ: {drill_type}")

    options = [str(o) for o in drill.get("options", [])]
    if len(options) != 4:
        raise ValueError(f"Drill '{drill.get('drill_key', fallback_idx)}' phải có đúng 4 lựa chọn.")

    correct_idx = int(drill.get("correct_index", -1))
    if not (0 <= correct_idx <= 3):
        raise ValueError(f"Drill '{drill.get('drill_key', fallback_idx)}' có correct_index không hợp lệ: {correct_idx}")

    drill_key = str(drill.get("drill_key", "")).strip() or f"{g_code}-{drill_type}-{fallback_idx}"
    prompt_jp = str(drill.get("prompt_jp", "")).strip()
    if not prompt_jp:
        raise ValueError(f"Drill '{drill_key}' bị thiếu prompt_jp.")

    translation_vi = str(drill.get("translation_vi", "")).strip()
    explanation_vi = str(drill.get("explanation_vi", "")).strip()
    diagnostics = [str(x) for x in drill.get("option_diagnostics", [])]
    if len(diagnostics) < 4:
        diagnostics = diagnostics + [""] * (4 - len(diagnostics))
    elif len(diagnostics) > 4:
        diagnostics = diagnostics[:4]

    conn.execute(
        """
        INSERT INTO GRAMMAR_DRILLS (
            drill_key, grammar_id, drill_type, prompt_jp, options_json,
            correct_index, translation_vi, explanation_vi, option_diagnostics_json
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(drill_key) DO UPDATE SET
            grammar_id=excluded.grammar_id,
            drill_type=excluded.drill_type,
            prompt_jp=excluded.prompt_jp,
            options_json=excluded.options_json,
            correct_index=excluded.correct_index,
            translation_vi=excluded.translation_vi,
            explanation_vi=excluded.explanation_vi,
            option_diagnostics_json=excluded.option_diagnostics_json
        """,
        (
            drill_key,
            grammar_id,
            drill_type,
            prompt_jp,
            json.dumps(options, ensure_ascii=False),
            correct_idx,
            translation_vi,
            explanation_vi,
            json.dumps(diagnostics, ensure_ascii=False),
        ),
    )
    row = conn.execute("SELECT id FROM GRAMMAR_DRILLS WHERE drill_key=?", (drill_key,)).fetchone()
    return int(row[0]) if row else None


def _fallback_analyze_question(
    question_dict: Dict[str, Any],
    passage_dict: Optional[Dict[str, Any]],
    grammar_points: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """Minimal safe structural analysis when question_grammar_map is unavailable or misses an uploaded item."""
    section = question_dict.get("section", "")
    mondai = question_dict.get("mondai_type", "")
    prompt_jp = str(question_dict.get("prompt_jp", "") or "")
    options = question_dict.get("options", [])
    focus_kw = str(question_dict.get("focus_keyword", "") or "")
    expl = str(question_dict.get("explanation_vi", "") or "")

    haystack = " ".join([prompt_jp, focus_kw, " ".join(options), expl])
    if passage_dict:
        haystack += " " + str(passage_dict.get("japanese_text", ""))

    links: List[Dict[str, str]] = []
    seen_codes: set[str] = set()
    for gp in grammar_points:
        code = str(gp.get("code", ""))
        patterns = gp.get("match_patterns") or []
        if not patterns:
            pat_clean = re.sub(r"[～~\s]+", "", str(gp.get("pattern", "")))
            if len(pat_clean) >= 2:
                patterns = [pat_clean]
        matched = False
        for pat in patterns:
            if not pat:
                continue
            try:
                if re.search(pat, haystack):
                    matched = True
                    break
            except re.error:
                if pat in haystack:
                    matched = True
                    break
        if matched and code not in seen_codes:
            seen_codes.add(code)
            if section == "grammar" and len(links) == 0:
                role = "primary_target"
            elif section == "grammar":
                role = "distractor_trap"
            elif section == "reading":
                role = "discourse_marker"
            else:
                role = "sentence_structure"
            links.append(
                {
                    "grammar_code": code,
                    "role": role,
                    "note_vi": f"Nhận diện tự động trong {mondai or section}: {gp.get('pattern', '')}.",
                }
            )
            if len(links) >= 3:
                break

    if section == "grammar" and mondai == "問題2":
        sa = (question_dict.get("notebook_meta") or {}).get("star_assembly") or {}
        assembled = sa.get("full_sentence") or prompt_jp
        parse_vi = f"Cấu trúc lắp ghép 問題2 ★: {assembled}"
    else:
        parse_vi = f"Phân tích câu {mondai or section}: Trọng tâm '{focus_kw or prompt_jp[:40]}'."

    takeaway = expl.splitlines()[0].strip() if expl else "Xác định chức năng trợ từ, chia thể và sắc thái ngữ cảnh."
    notes = [f"Phương án {idx + 1}: {opt}" for idx, opt in enumerate(options)] if section == "grammar" else []
    return {
        "links": links,
        "structure_parse_vi": parse_vi,
        "pedagogical_takeaway_vi": takeaway,
        "option_grammar_notes": notes,
    }


def _extract_exam_vocab_entries(conn: sqlite3.Connection) -> Dict[str, Dict[str, Any]]:
    rows = conn.execute(
        """
        SELECT id, section, mondai_type, source_label, focus_keyword, prompt_jp,
               options_json, correct_index, translation_vi, explanation_vi, notebook_meta_json
        FROM QUESTIONS
        ORDER BY id
        """
    ).fetchall()

    exam_vocab: Dict[str, Dict[str, Any]] = {}
    for r in rows:
        meta = _safe_json_loads(r["notebook_meta_json"], {})
        so_tay = meta.get("so_tay")
        if not so_tay and r["section"] != "vocab":
            continue

        q_id = int(r["id"])
        options = _safe_json_loads(r["options_json"], [])
        c_idx = int(r["correct_index"])
        correct_opt = str(options[c_idx]) if 0 <= c_idx < len(options) else ""
        focus_kw = str(r["focus_keyword"] or "").strip()
        expl = str(r["explanation_vi"] or "").strip()
        trans = str(r["translation_vi"] or "").strip()

        if so_tay:
            word = str(so_tay.get("word") or focus_kw or correct_opt).strip()
            reading = str(so_tay.get("hiragana") or "").strip()
            han_viet = str(so_tay.get("han_viet") or "").strip()
            meaning_vi = str(so_tay.get("meaning_vi") or "").strip()
            collocation_tip = str(so_tay.get("collocation_tip") or "").strip()
            src_ref = f"Đề .xlsx ({r['mondai_type']} · {r['source_label']})"
        else:
            reading = ""
            han_viet = ""
            meaning_vi = ""
            collocation_tip = ""
            if "→" in focus_kw:
                left, right = [p.strip() for p in focus_kw.split("→", 1)]
                if re.search(r"[\u4e00-\u9faf]", left):
                    word, reading = left, right
                elif re.search(r"[\u4e00-\u9faf]", right):
                    word, reading = right, left
                else:
                    word, reading = left, right
            elif "＝" in focus_kw:
                left, right = [p.strip() for p in focus_kw.split("＝", 1)]
                word = left
                collocation_tip = f"Từ đồng nghĩa trong đề: {left} ＝ {right}"
            else:
                word = focus_kw or correct_opt
                if word and not re.search(r"[\u4e00-\u9faf]", word):
                    reading = word

            if not meaning_vi:
                first_line = expl.splitlines()[0].strip() if expl else ""
                cleaned_line = re.sub(r"^[•\-\s]*Đáp án đúng:\s*\d+(?:\(\d+\))?\.\s*", "", first_line).strip()
                meaning_vi = cleaned_line or trans or focus_kw
            if not collocation_tip:
                collocation_tip = trans or str(r["prompt_jp"] or "").strip()
            src_ref = f"Đề .xlsx ({r['mondai_type']} · {r['source_label']})"

        if not word:
            continue
        norm_key = _normalize_word_key(word)
        if norm_key not in exam_vocab:
            exam_vocab[norm_key] = {
                "vocab_key": _make_exam_vocab_key(word),
                "word": word,
                "reading": reading,
                "han_viet": han_viet,
                "radical_note": "",
                "meaning_vi": meaning_vi,
                "collocation_tip": collocation_tip,
                "jlpt_level": "N3",
                "in_exam_corpus": 1,
                "source_ref": src_ref,
                "linked_question_ids": [q_id],
            }
        else:
            cur = exam_vocab[norm_key]
            if q_id not in cur["linked_question_ids"]:
                cur["linked_question_ids"].append(q_id)
            if not cur["reading"] and reading:
                cur["reading"] = reading
            if not cur["han_viet"] and han_viet:
                cur["han_viet"] = han_viet
            if len(meaning_vi) > len(cur["meaning_vi"]):
                cur["meaning_vi"] = meaning_vi
            if len(collocation_tip) > len(cur["collocation_tip"]):
                cur["collocation_tip"] = collocation_tip
    return exam_vocab


def _upsert_vocab_foundation_item(conn: sqlite3.Connection, item: Dict[str, Any]) -> None:
    vocab_key = str(item.get("vocab_key", "")).strip()
    word = str(item.get("word", "")).strip()
    if not vocab_key or not word:
        return
    level = str(item.get("jlpt_level", "N3")).strip().upper()
    if level not in VALID_LEVELS:
        level = "N3"
    in_exam = 1 if item.get("in_exam_corpus") else 0
    linked_qids = sorted({int(x) for x in item.get("linked_question_ids", [])})

    conn.execute(
        """
        INSERT INTO VOCAB_FOUNDATION (
            vocab_key, word, reading, han_viet, radical_note, meaning_vi,
            collocation_tip, jlpt_level, in_exam_corpus, source_ref, linked_question_ids_json
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(vocab_key) DO UPDATE SET
            word=excluded.word,
            reading=CASE WHEN excluded.reading != '' THEN excluded.reading ELSE VOCAB_FOUNDATION.reading END,
            han_viet=CASE WHEN excluded.han_viet != '' THEN excluded.han_viet ELSE VOCAB_FOUNDATION.han_viet END,
            radical_note=CASE WHEN excluded.radical_note != '' THEN excluded.radical_note ELSE VOCAB_FOUNDATION.radical_note END,
            meaning_vi=CASE WHEN excluded.meaning_vi != '' THEN excluded.meaning_vi ELSE VOCAB_FOUNDATION.meaning_vi END,
            collocation_tip=CASE WHEN excluded.collocation_tip != '' THEN excluded.collocation_tip ELSE VOCAB_FOUNDATION.collocation_tip END,
            jlpt_level=excluded.jlpt_level,
            in_exam_corpus=MAX(VOCAB_FOUNDATION.in_exam_corpus, excluded.in_exam_corpus),
            source_ref=CASE WHEN excluded.source_ref != '' THEN excluded.source_ref ELSE VOCAB_FOUNDATION.source_ref END,
            linked_question_ids_json=excluded.linked_question_ids_json
        """,
        (
            vocab_key,
            word,
            str(item.get("reading", "") or "").strip(),
            str(item.get("han_viet", "") or "").strip(),
            str(item.get("radical_note", "") or "").strip(),
            str(item.get("meaning_vi", "") or "").strip(),
            str(item.get("collocation_tip", "") or "").strip(),
            level,
            in_exam,
            str(item.get("source_ref", "") or "").strip(),
            json.dumps(linked_qids, ensure_ascii=False),
        ),
    )


def seed_grammar_and_foundation(db_path: Optional[Path] = None) -> Dict[str, Any]:
    """Idempotently seed grammar points, drills, FSRS states, 100% question grammar links, and vocab foundation."""
    init_db(db_path)
    corpus_mod = _load_grammar_corpus()
    qmap_mod = _load_question_grammar_map()

    grammar_points_data: List[Dict[str, Any]] = list(getattr(corpus_mod, "GRAMMAR_POINTS_DATA", []) or []) if corpus_mod else []
    grammar_drills_data: List[Dict[str, Any]] = list(getattr(corpus_mod, "GRAMMAR_DRILLS_DATA", []) or []) if corpus_mod else []
    vocab_curated_data: List[Dict[str, Any]] = list(getattr(corpus_mod, "VOCAB_FOUNDATION_CURATED", []) or []) if corpus_mod else []
    q_grammar_map: Dict[str, Dict[str, Any]] = dict(getattr(qmap_mod, "QUESTION_GRAMMAR_MAP", {}) or {}) if qmap_mod else {}
    analyze_fn = getattr(qmap_mod, "analyze_question_grammar", None) if qmap_mod else None

    with transaction(db_path) as conn:
        for gp in grammar_points_data:
            _upsert_grammar_point(conn, gp)

        code_to_id: Dict[str, int] = {
            str(r["code"]): int(r["id"])
            for r in conn.execute("SELECT id, code FROM GRAMMAR_POINTS").fetchall()
        }

        seeded_drills = 0
        for idx, drill in enumerate(grammar_drills_data, 1):
            if _upsert_grammar_drill(conn, drill, code_to_id, fallback_idx=idx) is not None:
                seeded_drills += 1

        # Build passage lookup map
        passage_map: Dict[int, Dict[str, Any]] = {}
        for p_row in conn.execute("SELECT * FROM PASSAGES").fetchall():
            passage_map[int(p_row["id"])] = dict(p_row)

        # Link 100% of QUESTIONS into QUESTION_GRAMMAR_ANALYSES + QUESTION_GRAMMAR_LINKS
        q_rows = conn.execute("SELECT * FROM QUESTIONS ORDER BY id").fetchall()
        analyses_synced = 0
        links_synced = 0
        for q_row in q_rows:
            q_id = int(q_row["id"])
            q_hash = str(q_row["content_hash"])
            options = _safe_json_loads(q_row["options_json"], [])
            meta = _safe_json_loads(q_row["notebook_meta_json"], {})
            q_dict = {
                **dict(q_row),
                "options": options,
                "notebook_meta": meta,
            }
            p_dict = passage_map.get(int(q_row["passage_id"])) if q_row["passage_id"] is not None else None

            analysis = q_grammar_map.get(q_hash)
            if analysis is None and callable(analyze_fn):
                analysis = analyze_fn(q_dict, p_dict)
            if analysis is None:
                analysis = _fallback_analyze_question(q_dict, p_dict, grammar_points_data)

            structure_parse_vi = str(analysis.get("structure_parse_vi", "") or "").strip()
            takeaway_vi = str(analysis.get("pedagogical_takeaway_vi", "") or "").strip()
            option_notes = list(analysis.get("option_grammar_notes", []) or [])

            conn.execute(
                """
                INSERT INTO QUESTION_GRAMMAR_ANALYSES
                    (question_id, structure_parse_vi, pedagogical_takeaway_vi, option_grammar_notes_json)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(question_id) DO UPDATE SET
                    structure_parse_vi=excluded.structure_parse_vi,
                    pedagogical_takeaway_vi=excluded.pedagogical_takeaway_vi,
                    option_grammar_notes_json=excluded.option_grammar_notes_json
                """,
                (
                    q_id,
                    structure_parse_vi,
                    takeaway_vi,
                    json.dumps(option_notes, ensure_ascii=False),
                ),
            )
            analyses_synced += 1

            resolved_links: List[Tuple[int, str, str]] = []
            for lnk in analysis.get("links", []):
                g_code = str(lnk.get("grammar_code", "")).strip()
                g_id = code_to_id.get(g_code)
                role = str(lnk.get("role", "sentence_structure")).strip()
                if g_id is None or role not in VALID_ROLES:
                    continue
                note_vi = str(lnk.get("note_vi", "") or "").strip()
                resolved_links.append((g_id, role, note_vi))

            if resolved_links:
                conn.execute("DELETE FROM QUESTION_GRAMMAR_LINKS WHERE question_id=?", (q_id,))
                for g_id, role, note_vi in resolved_links:
                    conn.execute(
                        """
                        INSERT INTO QUESTION_GRAMMAR_LINKS (question_id, grammar_id, role, note_vi)
                        VALUES (?, ?, ?, ?)
                        ON CONFLICT(question_id, grammar_id, role) DO UPDATE SET note_vi=excluded.note_vi
                        """,
                        (q_id, g_id, role, note_vi),
                    )
                    links_synced += 1

        # Automatically mark in_exam_corpus = 1 for all grammar points linked to QUESTIONS
        conn.execute(
            """
            UPDATE GRAMMAR_POINTS
            SET in_exam_corpus = 1
            WHERE id IN (SELECT DISTINCT grammar_id FROM QUESTION_GRAMMAR_LINKS)
            """
        )

        # Merge VOCAB_FOUNDATION from QUESTIONS + VOCAB_FOUNDATION_CURATED
        exam_vocab = _extract_exam_vocab_entries(conn)
        matched_exam_keys: set[str] = set()

        for curated in vocab_curated_data:
            c_item = dict(curated)
            c_word = str(c_item.get("word", "")).strip()
            c_norm = _normalize_word_key(c_word)
            # Check exact normalized word or slash-separated sub-words
            sub_norms = [c_norm] + [_normalize_word_key(p) for p in re.split(r"[/・、]", c_word) if p.strip()]
            matched_entry = None
            for sn in sub_norms:
                if sn in exam_vocab:
                    matched_entry = exam_vocab[sn]
                    matched_exam_keys.add(sn)
                    break
            if matched_entry is not None:
                c_item["in_exam_corpus"] = 1
                c_item["linked_question_ids"] = matched_entry["linked_question_ids"]
                if not c_item.get("reading") and matched_entry.get("reading"):
                    c_item["reading"] = matched_entry["reading"]
                if not c_item.get("han_viet") and matched_entry.get("han_viet"):
                    c_item["han_viet"] = matched_entry["han_viet"]
                if not c_item.get("collocation_tip") and matched_entry.get("collocation_tip"):
                    c_item["collocation_tip"] = matched_entry["collocation_tip"]
            else:
                c_item["in_exam_corpus"] = 1 if c_item.get("in_exam_corpus") else 0
                c_item.setdefault("linked_question_ids", [])
            _upsert_vocab_foundation_item(conn, c_item)

        for norm_key, e_item in exam_vocab.items():
            if norm_key in matched_exam_keys:
                continue
            _upsert_vocab_foundation_item(conn, e_item)

        gp_total = int(conn.execute("SELECT COUNT(*) FROM GRAMMAR_POINTS").fetchone()[0])
        dr_total = int(conn.execute("SELECT COUNT(*) FROM GRAMMAR_DRILLS").fetchone()[0])
        vf_total = int(conn.execute("SELECT COUNT(*) FROM VOCAB_FOUNDATION").fetchone()[0])

    return {
        "grammar_points": gp_total,
        "grammar_drills": dr_total,
        "analyses_synced": analyses_synced,
        "links_synced": links_synced,
        "vocab_foundation": vf_total,
        "corpus_loaded": corpus_mod is not None,
        "question_map_loaded": qmap_mod is not None,
    }


def get_question_grammar_payload(question_id: int, conn: sqlite3.Connection) -> Dict[str, Any]:
    """Return full post-submission grammar anatomy payload for a question."""
    ana = conn.execute(
        """
        SELECT structure_parse_vi, pedagogical_takeaway_vi, option_grammar_notes_json
        FROM QUESTION_GRAMMAR_ANALYSES
        WHERE question_id=?
        """,
        (question_id,),
    ).fetchone()
    link_rows = conn.execute(
        """
        SELECT gp.code, gp.pattern, gp.jlpt_level, qgl.role,
               gp.formation_formula, gp.core_meaning_vi, qgl.note_vi
        FROM QUESTION_GRAMMAR_LINKS qgl
        JOIN GRAMMAR_POINTS gp ON gp.id = qgl.grammar_id
        WHERE qgl.question_id=?
        ORDER BY CASE qgl.role
            WHEN 'primary_target' THEN 0
            WHEN 'distractor_trap' THEN 1
            WHEN 'sentence_structure' THEN 2
            ELSE 3
        END ASC, gp.code ASC
        """,
        (question_id,),
    ).fetchall()

    return {
        "structure_parse_vi": str(ana["structure_parse_vi"]) if ana else "",
        "pedagogical_takeaway_vi": str(ana["pedagogical_takeaway_vi"]) if ana else "",
        "option_grammar_notes": _safe_json_loads(ana["option_grammar_notes_json"], []) if ana else [],
        "grammar_points": [
            {
                "code": r["code"],
                "pattern": r["pattern"],
                "jlpt_level": r["jlpt_level"],
                "role": r["role"],
                "formation_formula": r["formation_formula"],
                "core_meaning_vi": r["core_meaning_vi"],
                "note_vi": r["note_vi"],
            }
            for r in link_rows
        ],
    }


def _load_drill_types_map(conn: sqlite3.Connection) -> Dict[int, set]:
    dt_map: Dict[int, set] = {}
    for r in conn.execute("SELECT DISTINCT grammar_id, drill_type FROM GRAMMAR_DRILLS").fetchall():
        dt_map.setdefault(int(r["grammar_id"]), set()).add(str(r["drill_type"]))
    return dt_map


def get_grammar_overview(db_path: Optional[Path] = None, now: Optional[datetime] = None) -> Dict[str, Any]:
    """Return aggregate grammar counts, exam coverage, and per-JLPT-level mastery statistics."""
    now_iso = format_iso(now or utc_now())
    conn = get_connection(db_path)
    try:
        rows = conn.execute(
            """
            SELECT gp.id, gp.code, gp.jlpt_level, gp.category, gp.category_label_vi, gp.in_exam_corpus,
                   f.stability, f.difficulty, f.reps, f.lapses, f.state,
                   f.formation_passed, f.contrast_passed, f.application_passed,
                   f.last_review, f.due_date
            FROM GRAMMAR_POINTS gp
            LEFT JOIN GRAMMAR_FSRS_STATES f ON f.grammar_id = gp.id
            ORDER BY gp.id
            """
        ).fetchall()
        drill_types_map = _load_drill_types_map(conn)
        total_drills = int(conn.execute("SELECT COUNT(*) FROM GRAMMAR_DRILLS").fetchone()[0])
        linked_questions = int(
            conn.execute("SELECT COUNT(DISTINCT question_id) FROM QUESTION_GRAMMAR_LINKS").fetchone()[0]
        )
        total_analyses = int(conn.execute("SELECT COUNT(*) FROM QUESTION_GRAMMAR_ANALYSES").fetchone()[0])
        vocab_count = int(conn.execute("SELECT COUNT(*) FROM VOCAB_FOUNDATION").fetchone()[0])
    finally:
        conn.close()

    total_points = len(rows)
    exam_corpus_count = 0
    mastered_count = 0
    practiced_count = 0
    due_count = 0

    by_level: Dict[str, Dict[str, Any]] = {
        lvl: {
            "level": lvl,
            "label_vi": LEVEL_LABELS_VI[lvl],
            "total": 0,
            "exam_corpus_count": 0,
            "mastered": 0,
            "in_progress": 0,
            "relearning": 0,
            "due": 0,
            "coverage_pct": 0.0,
        }
        for lvl in LEVEL_ORDER
    }
    by_category: Dict[str, Dict[str, Any]] = {}

    for r in rows:
        gp_id = int(r["id"])
        lvl = str(r["jlpt_level"])
        cat = str(r["category"])
        cat_lbl = str(r["category_label_vi"])
        in_exam = bool(r["in_exam_corpus"])
        fsrs = _format_grammar_fsrs(r, drill_types_map.get(gp_id))
        is_due = fsrs["state"] == "relearning" or fsrs["due_date"] is None or str(fsrs["due_date"]) <= now_iso

        if in_exam:
            exam_corpus_count += 1
        if fsrs["mastered"]:
            mastered_count += 1
        if fsrs["reps"] > 0:
            practiced_count += 1
        if is_due:
            due_count += 1

        if lvl in by_level:
            lb = by_level[lvl]
            lb["total"] += 1
            if in_exam:
                lb["exam_corpus_count"] += 1
            if fsrs["mastered"]:
                lb["mastered"] += 1
            elif fsrs["state"] == "relearning":
                lb["relearning"] += 1
            elif fsrs["reps"] > 0:
                lb["in_progress"] += 1
            if is_due:
                lb["due"] += 1

        if cat not in by_category:
            by_category[cat] = {
                "category": cat,
                "category_label_vi": cat_lbl,
                "total": 0,
                "mastered": 0,
            }
        by_category[cat]["total"] += 1
        if fsrs["mastered"]:
            by_category[cat]["mastered"] += 1

    levels_list: List[Dict[str, Any]] = []
    for lvl in LEVEL_ORDER:
        lb = by_level[lvl]
        if lvl == "N1" and lb["total"] == 0:
            continue
        lb["coverage_pct"] = round((lb["mastered"] / lb["total"]) * 100.0, 1) if lb["total"] > 0 else 0.0
        levels_list.append(lb)

    categories_list = sorted(by_category.values(), key=lambda x: (-x["total"], x["category"]))
    coverage_pct = round((mastered_count / total_points) * 100.0, 1) if total_points > 0 else 0.0

    return {
        "total_points": total_points,
        "exam_corpus_count": exam_corpus_count,
        "jlpt_extension_count": total_points - exam_corpus_count,
        "mastered_count": mastered_count,
        "practiced_count": practiced_count,
        "due_count": due_count,
        "total_drills": total_drills,
        "total_linked_questions": linked_questions,
        "total_analyses": total_analyses,
        "vocab_foundation_count": vocab_count,
        "coverage_pct": coverage_pct,
        "levels": levels_list,
        "categories": categories_list,
    }


def get_grammar_categories(db_path: Optional[Path] = None) -> List[Dict[str, str]]:
    conn = get_connection(db_path)
    try:
        rows = conn.execute(
            """
            SELECT category, MIN(category_label_vi) AS category_label_vi
            FROM GRAMMAR_POINTS
            GROUP BY category
            ORDER BY COUNT(*) DESC, category ASC
            """
        ).fetchall()
        return [{"category": r["category"], "category_label_vi": r["category_label_vi"]} for r in rows]
    finally:
        conn.close()


def list_grammar_points(
    scope: str = "all",
    level: Optional[str] = None,
    category: Optional[str] = None,
    state: Optional[str] = None,
    q: Optional[str] = None,
    db_path: Optional[Path] = None,
    now: Optional[datetime] = None,
) -> List[Dict[str, Any]]:
    """Filter and return grammar points with nested FSRS mastery metadata."""
    now_iso = format_iso(now or utc_now())
    conn = get_connection(db_path)
    try:
        where = ["1=1"]
        params: List[Any] = []

        norm_scope = (scope or "all").strip().lower()
        if norm_scope == "exam":
            where.append("gp.in_exam_corpus = 1")
        elif norm_scope == "jlpt":
            where.append("gp.in_exam_corpus = 0")

        if level and level.strip().upper() != "ALL":
            where.append("gp.jlpt_level = ?")
            params.append(level.strip().upper())

        if category and category.strip().upper() != "ALL":
            where.append("gp.category = ?")
            params.append(category.strip())

        where_sql = " AND ".join(where)
        rows = conn.execute(
            f"""
            SELECT gp.*,
                   f.stability, f.difficulty, f.reps, f.lapses, f.state,
                   f.formation_passed, f.contrast_passed, f.application_passed,
                   f.last_review, f.due_date,
                   (SELECT COUNT(DISTINCT qgl.question_id) FROM QUESTION_GRAMMAR_LINKS qgl WHERE qgl.grammar_id = gp.id) AS linked_question_count,
                   (SELECT COUNT(*) FROM GRAMMAR_DRILLS gd WHERE gd.grammar_id = gp.id) AS drill_count
            FROM GRAMMAR_POINTS gp
            LEFT JOIN GRAMMAR_FSRS_STATES f ON f.grammar_id = gp.id
            WHERE {where_sql}
            ORDER BY
                CASE gp.jlpt_level WHEN 'N5' THEN 1 WHEN 'N4' THEN 2 WHEN 'N3' THEN 3 WHEN 'N2' THEN 4 ELSE 5 END ASC,
                gp.in_exam_corpus DESC,
                gp.code ASC
            """,
            tuple(params),
        ).fetchall()
        drill_types_map = _load_drill_types_map(conn)
    finally:
        conn.close()

    q_lower = q.strip().lower() if q else ""
    state_filter = state.strip().lower() if state else ""

    results: List[Dict[str, Any]] = []
    for r in rows:
        gp_id = int(r["id"])
        fsrs = _format_grammar_fsrs(r, drill_types_map.get(gp_id))
        is_due = fsrs["state"] == "relearning" or fsrs["due_date"] is None or str(fsrs["due_date"]) <= now_iso

        if state_filter and state_filter != "all":
            if state_filter == "mastered" and not fsrs["mastered"]:
                continue
            elif state_filter == "due" and not is_due:
                continue
            elif state_filter not in ("mastered", "due") and fsrs["state"] != state_filter:
                continue

        if q_lower:
            search_blob = " ".join(
                [
                    str(r["code"] or ""),
                    str(r["pattern"] or ""),
                    str(r["core_meaning_vi"] or ""),
                    str(r["search_keywords"] or ""),
                    str(r["deep_explanation_vi"] or ""),
                    str(r["category_label_vi"] or ""),
                ]
            ).lower()
            if q_lower not in search_blob:
                continue

        results.append(
            {
                "id": gp_id,
                "code": r["code"],
                "pattern": r["pattern"],
                "jlpt_level": r["jlpt_level"],
                "category": r["category"],
                "category_label_vi": r["category_label_vi"],
                "in_exam_corpus": bool(r["in_exam_corpus"]),
                "formation_formula": r["formation_formula"],
                "core_meaning_vi": r["core_meaning_vi"],
                "register_tag": r["register_tag"],
                "source_ref": r["source_ref"],
                "search_keywords": r["search_keywords"],
                "linked_question_count": int(r["linked_question_count"] or 0),
                "drill_count": int(r["drill_count"] or 0),
                "fsrs": fsrs,
            }
        )
    return results


def get_grammar_point_detail(code: str, db_path: Optional[Path] = None) -> Optional[Dict[str, Any]]:
    """Return 3D pedagogical lesson detail, linked exam questions, drill summary, and FSRS state."""
    conn = get_connection(db_path)
    try:
        gp = conn.execute(
            """
            SELECT gp.*,
                   f.stability, f.difficulty, f.reps, f.lapses, f.state,
                   f.formation_passed, f.contrast_passed, f.application_passed,
                   f.last_review, f.due_date
            FROM GRAMMAR_POINTS gp
            LEFT JOIN GRAMMAR_FSRS_STATES f ON f.grammar_id = gp.id
            WHERE gp.code = ?
            """,
            (code,),
        ).fetchone()
        if not gp:
            gp = conn.execute(
                """
                SELECT gp.*,
                       f.stability, f.difficulty, f.reps, f.lapses, f.state,
                       f.formation_passed, f.contrast_passed, f.application_passed,
                       f.last_review, f.due_date
                FROM GRAMMAR_POINTS gp
                LEFT JOIN GRAMMAR_FSRS_STATES f ON f.grammar_id = gp.id
                WHERE UPPER(gp.code) = UPPER(?)
                """,
                (code,),
            ).fetchone()
        if not gp:
            return None

        gp_id = int(gp["id"])
        linked_rows = conn.execute(
            """
            SELECT q.id AS question_id, q.unit_code, q.section, q.mondai_type,
                   q.source_label, q.prompt_jp, qgl.role, qgl.note_vi
            FROM QUESTION_GRAMMAR_LINKS qgl
            JOIN QUESTIONS q ON q.id = qgl.question_id
            WHERE qgl.grammar_id = ?
            ORDER BY CASE qgl.role
                WHEN 'primary_target' THEN 0
                WHEN 'distractor_trap' THEN 1
                WHEN 'sentence_structure' THEN 2
                ELSE 3
            END ASC, q.id ASC
            """,
            (gp_id,),
        ).fetchall()

        drill_rows = conn.execute(
            "SELECT drill_type, COUNT(*) AS cnt FROM GRAMMAR_DRILLS WHERE grammar_id=? GROUP BY drill_type",
            (gp_id,),
        ).fetchall()
    finally:
        conn.close()

    by_type = {"formation": 0, "contrast": 0, "application": 0}
    avail_types: set[str] = set()
    for dr in drill_rows:
        dt = str(dr["drill_type"])
        by_type[dt] = int(dr["cnt"])
        if int(dr["cnt"]) > 0:
            avail_types.add(dt)

    return {
        "id": gp_id,
        "code": gp["code"],
        "pattern": gp["pattern"],
        "jlpt_level": gp["jlpt_level"],
        "category": gp["category"],
        "category_label_vi": gp["category_label_vi"],
        "in_exam_corpus": bool(gp["in_exam_corpus"]),
        "formation_formula": gp["formation_formula"],
        "formation_table": _safe_json_loads(gp["formation_table_json"], []),
        "core_meaning_vi": gp["core_meaning_vi"],
        "deep_explanation_vi": gp["deep_explanation_vi"],
        "register_tag": gp["register_tag"],
        "confusable_pairs": _safe_json_loads(gp["confusable_pairs_json"], []),
        "examples": _safe_json_loads(gp["examples_json"], []),
        "source_ref": gp["source_ref"],
        "search_keywords": gp["search_keywords"],
        "linked_questions": [
            {
                "question_id": int(lr["question_id"]),
                "unit_code": lr["unit_code"],
                "section": lr["section"],
                "mondai_type": lr["mondai_type"],
                "source_label": lr["source_label"],
                "prompt_jp": lr["prompt_jp"],
                "role": lr["role"],
                "note_vi": lr["note_vi"],
            }
            for lr in linked_rows
        ],
        "drills_summary": {
            "total": sum(by_type.values()),
            "by_type": by_type,
        },
        "fsrs": _format_grammar_fsrs(gp, avail_types),
    }


def get_next_grammar_drill(
    drill_type: str = "mixed",
    scope: str = "all",
    level: Optional[str] = None,
    grammar_code: Optional[str] = None,
    session_seed: str = "default",
    now: Optional[datetime] = None,
    db_path: Optional[Path] = None,
) -> Optional[Dict[str, Any]]:
    """Select next grammar drill by FSRS priority and permute options with zero answer leakage."""
    now_iso = format_iso(now or utc_now())
    norm_type = (drill_type or "mixed").strip().lower()
    if norm_type != "mixed" and norm_type not in VALID_DRILL_TYPES:
        raise ValueError(f"drill_type không hợp lệ: {drill_type}")

    conn = get_connection(db_path)
    try:
        where = ["1=1"]
        params: List[Any] = []

        if norm_type != "mixed":
            where.append("d.drill_type = ?")
            params.append(norm_type)

        norm_scope = (scope or "all").strip().lower()
        if norm_scope == "exam":
            where.append("gp.in_exam_corpus = 1")
        elif norm_scope == "jlpt":
            where.append("gp.in_exam_corpus = 0")

        if level and level.strip().upper() != "ALL":
            where.append("gp.jlpt_level = ?")
            params.append(level.strip().upper())

        if grammar_code and grammar_code.strip():
            where.append("UPPER(gp.code) = UPPER(?)")
            params.append(grammar_code.strip())

        where_sql = " AND ".join(where)
        params.append(now_iso)
        row = conn.execute(
            f"""
            SELECT d.id AS drill_id, d.drill_key, d.grammar_id, d.drill_type,
                   d.prompt_jp, d.options_json, d.correct_index,
                   gp.code, gp.jlpt_level, gp.category, gp.category_label_vi, gp.in_exam_corpus,
                   f.stability, f.difficulty, f.reps, f.lapses, f.state,
                   f.formation_passed, f.contrast_passed, f.application_passed,
                   f.last_review, f.due_date
            FROM GRAMMAR_DRILLS d
            JOIN GRAMMAR_POINTS gp ON gp.id = d.grammar_id
            LEFT JOIN GRAMMAR_FSRS_STATES f ON f.grammar_id = gp.id
            WHERE {where_sql}
            ORDER BY
                CASE
                    WHEN f.state = 'relearning' THEN 0
                    WHEN f.state IN ('review', 'learning') AND (f.due_date IS NULL OR f.due_date <= ?) THEN 1
                    WHEN COALESCE(f.state, 'new') = 'new' THEN 2
                    ELSE 3
                END ASC,
                CASE d.drill_type
                    WHEN 'formation' THEN COALESCE(f.formation_passed, 0)
                    WHEN 'contrast' THEN COALESCE(f.contrast_passed, 0)
                    ELSE COALESCE(f.application_passed, 0)
                END ASC,
                (SELECT COUNT(*) FROM GRAMMAR_ATTEMPT_LOGS a WHERE a.drill_id = d.id AND a.is_correct = 1) ASC,
                COALESCE((SELECT MAX(a.id) FROM GRAMMAR_ATTEMPT_LOGS a WHERE a.drill_id = d.id), 0) ASC,
                gp.in_exam_corpus DESC,
                gp.id ASC,
                d.id ASC
            LIMIT 1
            """,
            tuple(params),
        ).fetchone()
        if not row:
            return None

        avail_rows = conn.execute(
            "SELECT DISTINCT drill_type FROM GRAMMAR_DRILLS WHERE grammar_id=?",
            (row["grammar_id"],),
        ).fetchall()
        avail_types = {str(r["drill_type"]) for r in avail_rows}
    finally:
        conn.close()

    raw_options = _safe_json_loads(row["options_json"], [])
    orig_correct = int(row["correct_index"])
    display_options, _, _ = permute_options(
        raw_options,
        orig_correct,
        session_seed=session_seed,
        item_key=f"gd{row['drill_id']}",
    )

    return {
        "drill_id": int(row["drill_id"]),
        "drill_key": row["drill_key"],
        "drill_type": row["drill_type"],
        "drill_type_label_vi": DRILL_TYPE_LABELS_VI.get(row["drill_type"], row["drill_type"]),
        "jlpt_level": row["jlpt_level"],
        "category": row["category"],
        "category_label_vi": row["category_label_vi"],
        "in_exam_corpus": bool(row["in_exam_corpus"]),
        "prompt_jp": row["prompt_jp"],
        "options": display_options,
        "session_seed": session_seed,
        "fsrs": _format_grammar_fsrs(row, avail_types),
    }


def submit_grammar_drill(
    drill_id: int,
    selected_index: int,
    response_sec: float = 0.0,
    session_seed: str = "default",
    now: Optional[datetime] = None,
    db_path: Optional[Path] = None,
) -> Dict[str, Any]:
    """Grade grammar drill submission, log attempt, and update independent GRAMMAR_FSRS_STATES."""
    if selected_index is None or not (0 <= int(selected_index) <= 3):
        raise ValueError("Vui lòng chọn 1 đáp án hợp lệ từ 1 đến 4 (0..3).")
    sel_idx = int(selected_index)

    ts_now = now or utc_now()
    settings = get_pace_settings(db_path=db_path)
    d_rem = max(1, settings.days_remaining)
    d_min = max(5, settings.daily_minutes)

    with transaction(db_path) as conn:
        row = conn.execute(
            """
            SELECT d.*, gp.code, gp.pattern, gp.jlpt_level, gp.category, gp.category_label_vi,
                   gp.in_exam_corpus, gp.formation_formula, gp.core_meaning_vi
            FROM GRAMMAR_DRILLS d
            JOIN GRAMMAR_POINTS gp ON gp.id = d.grammar_id
            WHERE d.id = ?
            """,
            (drill_id,),
        ).fetchone()
        if not row:
            raise ValueError(f"Không tìm thấy bài luyện ngữ pháp id={drill_id}")

        grammar_id = int(row["grammar_id"])
        conn.execute("INSERT OR IGNORE INTO GRAMMAR_FSRS_STATES (grammar_id) VALUES (?)", (grammar_id,))
        fsrs_row = conn.execute(
            "SELECT * FROM GRAMMAR_FSRS_STATES WHERE grammar_id=?",
            (grammar_id,),
        ).fetchone()
        avail_types = {
            str(r["drill_type"])
            for r in conn.execute(
                "SELECT DISTINCT drill_type FROM GRAMMAR_DRILLS WHERE grammar_id=?",
                (grammar_id,),
            ).fetchall()
        }

        raw_options = _safe_json_loads(row["options_json"], [])
        orig_correct_idx = int(row["correct_index"])
        permuted_opts, display_correct_idx, index_map = permute_options(
            raw_options,
            orig_correct_idx,
            session_seed=session_seed,
            item_key=f"gd{drill_id}",
        )
        orig_selected_idx = index_map[sel_idx]
        is_correct = orig_selected_idx == orig_correct_idx

        raw_diagnostics = _safe_json_loads(row["option_diagnostics_json"], [])
        display_diagnostics = [
            str(raw_diagnostics[orig_i]) if orig_i < len(raw_diagnostics) else ""
            for orig_i in index_map
        ]
        selected_diagnostic = display_diagnostics[sel_idx]
        option_diagnostics_detailed = [
            {
                "display_index": i,
                "orig_index": orig_i,
                "option_text": permuted_opts[i],
                "is_correct": orig_i == orig_correct_idx,
                "is_selected": i == sel_idx,
                "diagnostic": display_diagnostics[i],
            }
            for i, orig_i in enumerate(index_map)
        ]

        # FSRS update (compatible with fsrs_adaptive.py)
        old_stab = float(fsrs_row["stability"])
        old_diff = float(fsrs_row["difficulty"])
        old_reps = int(fsrs_row["reps"])
        old_lapses = int(fsrs_row["lapses"])
        old_state = str(fsrs_row["state"])
        last_rev_dt = parse_iso(fsrs_row["last_review"])
        elapsed_days = max(0.0, (ts_now - last_rev_dt).total_seconds() / 86400.0) if last_rev_dt else 0.0

        pass_flags = {
            "formation": int(fsrs_row["formation_passed"]),
            "contrast": int(fsrs_row["contrast_passed"]),
            "application": int(fsrs_row["application_passed"]),
        }
        pass_flags[str(row["drill_type"])] = 1 if is_correct else 0
        f_pass = pass_flags["formation"]
        c_pass = pass_flags["contrast"]
        a_pass = pass_flags["application"]

        if not is_correct:
            rating = Rating.AGAIN.value
            new_state = "relearning"
            new_lapses = old_lapses + 1
            new_reps = old_reps + 1
            new_stab = round(max(0.25, old_stab * 0.4), 4)
            new_diff = round(min(MAX_DIFFICULTY, old_diff + 0.85), 3)
            delay_min = 10 if d_min >= 45 else 120
            due_dt = ts_now + timedelta(minutes=delay_min)
            raw_interval_days = delay_min / 1440.0
            effective_interval_days = raw_interval_days
        else:
            rating = Rating.EASY.value if (response_sec > 0 and response_sec <= 12.0) else Rating.GOOD.value
            r_now = compute_retrievability(old_stab, elapsed_days)
            if old_state in ("new", "relearning") or old_reps == 0:
                new_stab = INITIAL_STABILITY_DAYS[rating]
            else:
                mult = (
                    1.0 + 0.85 * ((11.0 - old_diff) / 5.0) * (1.0 + (1.0 - r_now))
                    if rating == Rating.EASY.value
                    else 1.0 + 0.45 * ((11.0 - old_diff) / 5.0) * (1.0 + (1.0 - r_now))
                )
                new_stab = round(min(180.0, max(old_stab + 0.2, old_stab * mult)), 4)

            diff_delta = -0.45 if rating == Rating.EASY.value else -0.10
            new_diff = round(min(MAX_DIFFICULTY, max(MIN_DIFFICULTY, old_diff + diff_delta)), 3)
            new_reps = old_reps + 1
            new_lapses = old_lapses
            new_state = "review"
            raw_interval_days = new_stab
            effective_interval_days = compute_horizon_interval(raw_interval_days, d_rem)
            due_dt = ts_now + timedelta(days=effective_interval_days)

        now_iso = format_iso(ts_now)
        due_iso = format_iso(due_dt)

        conn.execute(
            """
            UPDATE GRAMMAR_FSRS_STATES
            SET stability=?, difficulty=?, reps=?, lapses=?, state=?,
                formation_passed=?, contrast_passed=?, application_passed=?,
                last_review=?, due_date=?
            WHERE grammar_id=?
            """,
            (
                new_stab,
                new_diff,
                new_reps,
                new_lapses,
                new_state,
                f_pass,
                c_pass,
                a_pass,
                now_iso,
                due_iso,
                grammar_id,
            ),
        )
        conn.execute(
            """
            INSERT INTO GRAMMAR_ATTEMPT_LOGS
                (grammar_id, drill_id, drill_type, is_correct, response_sec, selected_orig_index, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                grammar_id,
                drill_id,
                row["drill_type"],
                1 if is_correct else 0,
                float(response_sec),
                orig_selected_idx,
                now_iso,
            ),
        )

    mastered = is_grammar_mastered(
        {
            "state": new_state,
            "reps": new_reps,
            "stability": new_stab,
            "formation_passed": f_pass,
            "contrast_passed": c_pass,
            "application_passed": a_pass,
        },
        available_drill_types=avail_types,
    )

    return {
        "drill_id": int(drill_id),
        "drill_key": row["drill_key"],
        "drill_type": row["drill_type"],
        "is_correct": is_correct,
        "selected_display_index": sel_idx,
        "selected_orig_index": orig_selected_idx,
        "selected_option_text": permuted_opts[sel_idx],
        "correct_display_index": display_correct_idx,
        "correct_option_text": raw_options[orig_correct_idx],
        "selected_diagnostic": selected_diagnostic,
        "option_diagnostics": display_diagnostics,
        "option_diagnostics_detailed": option_diagnostics_detailed,
        "explanation_vi": row["explanation_vi"],
        "translation_vi": row["translation_vi"],
        "grammar_point": {
            "id": grammar_id,
            "code": row["code"],
            "pattern": row["pattern"],
            "jlpt_level": row["jlpt_level"],
            "category": row["category"],
            "category_label_vi": row["category_label_vi"],
            "in_exam_corpus": bool(row["in_exam_corpus"]),
            "formation_formula": row["formation_formula"],
            "core_meaning_vi": row["core_meaning_vi"],
        },
        "fsrs": {
            "grammar_id": grammar_id,
            "code": row["code"],
            "stability": new_stab,
            "difficulty": new_diff,
            "reps": new_reps,
            "lapses": new_lapses,
            "state": new_state,
            "formation_passed": bool(f_pass),
            "contrast_passed": bool(c_pass),
            "application_passed": bool(a_pass),
            "mastered": mastered,
            "raw_interval_days": round(raw_interval_days, 4),
            "effective_interval_days": round(effective_interval_days, 4),
            "last_review": now_iso,
            "due_date": due_iso,
        },
    }


def import_jlpt_grammar_pack(
    payload_or_bytes: Union[bytes, bytearray, str, Dict[str, Any], List[Dict[str, Any]]],
    filename: str = "grammar_pack.json",
    db_path: Optional[Path] = None,
) -> Dict[str, Any]:
    """Import an extension JLPT grammar pack (.json) or delegate .xlsx to Smart Excel Importer."""
    init_db(db_path)
    lower_name = str(filename or "").lower()
    if lower_name.endswith(".xlsx"):
        from n3_mastery.importer import import_excel_file

        if isinstance(payload_or_bytes, (bytes, bytearray)):
            if not payload_or_bytes:
                raise ValueError("Tệp Excel tải lên rỗng.")
            with tempfile.TemporaryDirectory() as tmp_dir:
                tmp_path = Path(tmp_dir) / Path(filename).name
                tmp_path.write_bytes(bytes(payload_or_bytes))
                report = import_excel_file(tmp_path, db_path=db_path, generate_variants=True)
        elif isinstance(payload_or_bytes, (str, Path)):
            report = import_excel_file(Path(payload_or_bytes), db_path=db_path, generate_variants=True)
        else:
            raise ValueError("Định dạng dữ liệu Excel không hợp lệ.")
        return {
            "import_type": "xlsx",
            "filename": Path(filename).name,
            "imported_grammar_points": 0,
            "imported_drills": 0,
            "imported_vocab": 0,
            "import_report": report,
        }

    if not lower_name.endswith(".json") and isinstance(payload_or_bytes, (bytes, bytearray)):
        raise ValueError("Chỉ hỗ trợ tệp định dạng .json hoặc .xlsx.")

    if isinstance(payload_or_bytes, (bytes, bytearray)):
        if not payload_or_bytes:
            raise ValueError("Tệp JSON tải lên rỗng.")
        try:
            parsed = json.loads(bytes(payload_or_bytes).decode("utf-8"))
        except Exception as exc:
            raise ValueError(f"Không đọc được cấu trúc JSON: {exc}") from exc
    elif isinstance(payload_or_bytes, str):
        try:
            parsed = json.loads(payload_or_bytes)
        except Exception as exc:
            raise ValueError(f"Không đọc được chuỗi JSON: {exc}") from exc
    else:
        parsed = payload_or_bytes

    if isinstance(parsed, list):
        gp_list = parsed
        drill_list: List[Dict[str, Any]] = []
        vocab_list: List[Dict[str, Any]] = []
    elif isinstance(parsed, dict):
        gp_list = list(parsed.get("grammar_points", []) or [])
        drill_list = list(parsed.get("drills", []) or [])
        vocab_list = list(parsed.get("vocab_foundation", []) or [])
    else:
        raise ValueError("Gói JSON phải là Object chứa 'grammar_points' hoặc Array danh sách mẫu ngữ pháp.")

    if not gp_list and not drill_list and not vocab_list:
        raise ValueError("Gói JSON không có dữ liệu grammar_points, drills hoặc vocab_foundation.")

    with transaction(db_path) as conn:
        imported_gp = 0
        for gp in gp_list:
            gp_copy = dict(gp)
            if not gp_copy.get("source_ref"):
                gp_copy["source_ref"] = Path(filename).name
            _upsert_grammar_point(conn, gp_copy)
            imported_gp += 1

        code_to_id = {
            str(r["code"]): int(r["id"])
            for r in conn.execute("SELECT id, code FROM GRAMMAR_POINTS").fetchall()
        }

        imported_drills = 0
        for idx, dr in enumerate(drill_list, 1):
            if _upsert_grammar_drill(conn, dr, code_to_id, fallback_idx=idx) is None:
                raise ValueError(
                    f"Drill '{dr.get('drill_key', idx)}' tham chiếu mã ngữ pháp không tồn tại: {dr.get('grammar_code')}"
                )
            imported_drills += 1

        imported_vocab = 0
        for vf in vocab_list:
            _upsert_vocab_foundation_item(conn, vf)
            imported_vocab += 1

    return {
        "import_type": "json",
        "filename": Path(filename).name,
        "imported_grammar_points": imported_gp,
        "imported_drills": imported_drills,
        "imported_vocab": imported_vocab,
    }


def list_vocab_foundation(
    scope: str = "all",
    level: Optional[str] = None,
    q: Optional[str] = None,
    limit: int = 200,
    db_path: Optional[Path] = None,
) -> List[Dict[str, Any]]:
    """Query VOCAB_FOUNDATION filtered by scope (all|exam|curated), JLPT level, and search text."""
    conn = get_connection(db_path)
    try:
        where = ["1=1"]
        params: List[Any] = []

        norm_scope = (scope or "all").strip().lower()
        if norm_scope == "exam":
            where.append("in_exam_corpus = 1")
        elif norm_scope in ("curated", "jlpt"):
            where.append("in_exam_corpus = 0")

        if level and level.strip().upper() != "ALL":
            where.append("jlpt_level = ?")
            params.append(level.strip().upper())

        q_lower = q.strip().lower() if q else ""
        if q_lower:
            like = f"%{q_lower}%"
            where.append(
                "(LOWER(word) LIKE ? OR LOWER(reading) LIKE ? OR LOWER(han_viet) LIKE ? "
                "OR LOWER(radical_note) LIKE ? OR LOWER(meaning_vi) LIKE ? OR LOWER(collocation_tip) LIKE ?)"
            )
            params.extend([like, like, like, like, like, like])

        params.append(max(1, min(1000, int(limit))))
        where_sql = " AND ".join(where)
        rows = conn.execute(
            f"""
            SELECT * FROM VOCAB_FOUNDATION
            WHERE {where_sql}
            ORDER BY in_exam_corpus DESC,
                     CASE jlpt_level WHEN 'N5' THEN 1 WHEN 'N4' THEN 2 WHEN 'N3' THEN 3 WHEN 'N2' THEN 4 ELSE 5 END ASC,
                     id ASC
            LIMIT ?
            """,
            tuple(params),
        ).fetchall()
    finally:
        conn.close()

    return [
        {
            "id": int(r["id"]),
            "vocab_key": r["vocab_key"],
            "word": r["word"],
            "reading": r["reading"],
            "han_viet": r["han_viet"],
            "radical_note": r["radical_note"],
            "meaning_vi": r["meaning_vi"],
            "collocation_tip": r["collocation_tip"],
            "jlpt_level": r["jlpt_level"],
            "in_exam_corpus": bool(r["in_exam_corpus"]),
            "source_ref": r["source_ref"],
            "linked_question_ids": _safe_json_loads(r["linked_question_ids_json"], []),
        }
        for r in rows
    ]
