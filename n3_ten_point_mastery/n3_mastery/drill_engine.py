"""Anti-Rote Drill Engine: OptionPermuter, DistractorInverter, 4-Slot Star Assembly, Evidence-First Dokkai."""

import hashlib
import json
import random
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from n3_mastery.database import get_connection, transaction
from n3_mastery.fsrs_adaptive import (
    apply_fsrs_update,
    format_iso,
    get_due_question_ids,
    utc_now,
)
from n3_mastery.models import Rating
from n3_mastery.scaffolding import apply_passage_scaffolding, apply_scaffolding


def permute_options(
    options: List[str],
    correct_index: int,
    session_seed: str,
    item_key: str,
) -> Tuple[List[str], int, List[int]]:
    """Deterministically permute 4 options using session_seed + item_key.

    Returns (permuted_options, new_correct_index, display_to_orig_map).
    """
    n = len(options)
    indices = list(range(n))
    seed_int = int.from_bytes(
        hashlib.sha256(f"{session_seed}:{item_key}".encode("utf-8")).digest()[:8], "big"
    )
    rng = random.Random(seed_int)
    rng.shuffle(indices)
    permuted = [options[i] for i in indices]
    new_correct = indices.index(correct_index)
    return permuted, new_correct, indices


def _validate_4slot_order(slot_order: Optional[List[int]]) -> List[int]:
    if slot_order is None or len(slot_order) != 4:
        raise ValueError(
            "Bắt buộc ghép đầy đủ cả 4 mảnh vào 4 ô [1][2][3][4] trước khi nộp bài (không được chỉ chọn dấu ★)."
        )
    if any(not isinstance(i, int) or i < 0 or i > 3 for i in slot_order):
        raise ValueError("Chỉ số mảnh ghép không hợp lệ (chỉ chấp nhận 0..3).")
    if len(set(slot_order)) != 4:
        raise ValueError("Mỗi mảnh ghép chỉ được đặt vào đúng 1 ô (không được lặp mảnh).")
    return list(slot_order)


def get_study_item(
    question_id: int,
    mode: str = "original",
    variant_id: Optional[int] = None,
    session_seed: str = "default",
    exam_mode: bool = False,
    db_path: Optional[Path] = None,
) -> Dict[str, Any]:
    """Build a renderable, scaffolded study payload for original or anti-rote variant drills."""
    conn = get_connection(db_path)
    try:
        q = conn.execute("SELECT * FROM QUESTIONS WHERE id=?", (question_id,)).fetchone()
        if not q:
            raise ValueError(f"Không tìm thấy câu hỏi id={question_id}")
        fsrs = conn.execute("SELECT * FROM FSRS_STATES WHERE question_id=?", (question_id,)).fetchone()
        stability = float(fsrs["stability"]) if fsrs else 0.5
        meta = json.loads(q["notebook_meta_json"] or "{}")

        variant_row = None
        if variant_id is not None:
            variant_row = conn.execute(
                "SELECT * FROM VARIANT_DRILLS WHERE id=? AND question_id=?",
                (variant_id, question_id),
            ).fetchone()
            if not variant_row:
                raise ValueError(f"Không tìm thấy biến thể id={variant_id} cho câu hỏi id={question_id}")
        elif mode == "variant":
            variant_row = conn.execute(
                "SELECT * FROM VARIANT_DRILLS WHERE question_id=? ORDER BY id LIMIT 1",
                (question_id,),
            ).fetchone()

        is_variant = variant_row is not None
        active_prompt = str(variant_row["prompt_jp"]) if is_variant else str(q["prompt_jp"])
        raw_options = json.loads(variant_row["options_json"] if is_variant else q["options_json"])
        orig_correct_idx = int(variant_row["correct_index"] if is_variant else q["correct_index"])
        v_meta = json.loads(variant_row["metadata_json"] or "{}") if is_variant else {}
        variant_mode = str(variant_row["variant_mode"]) if is_variant else "original"

        # Determine interaction widget type
        if (q["section"] == "grammar" and q["mondai_type"] == "問題2" and meta.get("star_assembly")) or variant_mode == "star_4slot_shift":
            interaction_type = "star_4slot"
            star_info = v_meta if is_variant else meta.get("star_assembly", {})
            # Permute display chunks only (keeping canonical chunk index 0..3 as value!)
            chunk_indices = [0, 1, 2, 3]
            rng = random.Random(f"{session_seed}:star:{q['id']}:{variant_row['id'] if is_variant else 0}")
            rng.shuffle(chunk_indices)
            display_chunks = [{"chunk_index": ci, "text": raw_options[ci]} for ci in chunk_indices]
            scaf = apply_scaffolding(
                active_prompt,
                [c["text"] for c in display_chunks],
                stability=stability,
                exam_mode=exam_mode,
                focus_keyword=q["focus_keyword"],
            )
            star_payload = {
                "star_slot_index": int(star_info.get("star_slot_index", 2)),
                "prefix": star_info.get("prefix", ""),
                "suffix": star_info.get("suffix", ""),
                "chunks": display_chunks,
            }
            display_options = [c["text"] for c in display_chunks]
            index_map = chunk_indices
        else:
            if variant_mode == "dokkai_evidence" and q["passage_id"] is not None:
                interaction_type = "dokkai_evidence"
            else:
                interaction_type = "mcq"
            item_key = f"v{variant_row['id']}" if is_variant else f"q{q['id']}"
            display_options, _, index_map = permute_options(
                raw_options, orig_correct_idx, session_seed=session_seed, item_key=item_key
            )
            scaf = apply_scaffolding(
                active_prompt,
                display_options,
                stability=stability,
                exam_mode=exam_mode,
                focus_keyword=q["focus_keyword"],
            )
            star_payload = None

        passage_payload = None
        if q["passage_id"] is not None:
            p = conn.execute("SELECT * FROM PASSAGES WHERE id=?", (q["passage_id"],)).fetchone()
            if p:
                sentences = json.loads(p["evidence_sentences_json"] or "[]")
                p_scaf = apply_passage_scaffolding(
                    p["japanese_text"],
                    stability=stability,
                    exam_mode=exam_mode,
                    sentences=sentences,
                )
                passage_payload = {
                    "id": p["id"],
                    "title": p["title"],
                    "genre": p["genre"],
                    "section": p["section"],
                    "full_html": p_scaf["full_html"],
                    "sentences": [
                        {"index": i, "text": sentences[i], "html": p_scaf["sentence_htmls"][i]}
                        for i in range(len(sentences))
                    ],
                }

        bridge = conn.execute(
            "SELECT unit_code, grammar_focus, completed FROM N4_BRIDGE_CAPSULES WHERE unit_code=?",
            (q["unit_code"],),
        ).fetchone()

        available_variants = conn.execute(
            "SELECT id, variant_mode FROM VARIANT_DRILLS WHERE question_id=? ORDER BY id",
            (q["id"],),
        ).fetchall()

        return {
            "question_id": int(q["id"]),
            "variant_id": int(variant_row["id"]) if is_variant else None,
            "mode": "variant" if is_variant else "original",
            "variant_mode": variant_mode,
            "interaction_type": interaction_type,
            "unit_code": q["unit_code"],
            "section": q["section"],
            "mondai_type": q["mondai_type"],
            "source_label": q["source_label"],
            "session_seed": session_seed,
            "exam_mode": exam_mode,
            "prompt_jp": active_prompt,
            "prompt_html": scaf["prompt_html"],
            "options": display_options,
            "options_html": scaf["options_html"],
            "star_assembly": star_payload,
            "passage": passage_payload,
            "scaffolding": {
                "tier": scaf["tier"],
                "tier_label": scaf["tier_label"],
                "hint_allowed": scaf["hint_allowed"],
                "background_glossary": scaf["background_glossary"],
            },
            "fsrs": {
                "stability": stability,
                "reps": int(fsrs["reps"]) if fsrs else 0,
                "lapses": int(fsrs["lapses"]) if fsrs else 0,
                "state": str(fsrs["state"]) if fsrs else "new",
                "clean_original_passed": bool(fsrs["clean_original_passed"]) if fsrs else False,
                "variant_passed": bool(fsrs["variant_passed"]) if fsrs else False,
                "spaced_clean_sessions": int(fsrs["spaced_clean_sessions"]) if fsrs else 0,
            },
            "bridge_status": {
                "unit_code": bridge["unit_code"],
                "grammar_focus": bridge["grammar_focus"],
                "completed": bool(bridge["completed"]),
            }
            if bridge
            else None,
            "available_variants": [{"id": r["id"], "variant_mode": r["variant_mode"]} for r in available_variants],
        }
    finally:
        conn.close()


def submit_answer(
    question_id: int,
    mode: str = "original",
    variant_id: Optional[int] = None,
    selected_index: Optional[int] = None,
    slot_order: Optional[List[int]] = None,
    evidence_indices: Optional[List[int]] = None,
    used_hint: bool = False,
    response_sec: float = 0.0,
    session_seed: str = "default",
    exam_mode: bool = False,
    mock_exam_id: Optional[int] = None,
    now: Optional[datetime] = None,
    db_path: Optional[Path] = None,
) -> Dict[str, Any]:
    """Validate and grade original / anti-rote variant / 4-slot star / Evidence-First Dokkai submissions."""
    ts_now = now or utc_now()
    if exam_mode:
        used_hint = False

    conn = get_connection(db_path)
    try:
        q = conn.execute("SELECT * FROM QUESTIONS WHERE id=?", (question_id,)).fetchone()
        if not q:
            raise ValueError(f"Không tìm thấy câu hỏi id={question_id}")
        q_meta = json.loads(q["notebook_meta_json"] or "{}")
        fsrs_before = conn.execute("SELECT * FROM FSRS_STATES WHERE question_id=?", (question_id,)).fetchone()
        prev_state = str(fsrs_before["state"]) if fsrs_before else "new"

        variant_row = None
        if variant_id is not None:
            variant_row = conn.execute(
                "SELECT * FROM VARIANT_DRILLS WHERE id=? AND question_id=?",
                (variant_id, question_id),
            ).fetchone()
            if not variant_row:
                raise ValueError(f"Không tìm thấy biến thể id={variant_id}")

        is_variant = variant_row is not None
        raw_options = json.loads(variant_row["options_json"] if is_variant else q["options_json"])
        orig_correct_idx = int(variant_row["correct_index"] if is_variant else q["correct_index"])
        v_meta = json.loads(variant_row["metadata_json"] or "{}") if is_variant else {}
        variant_mode = str(variant_row["variant_mode"]) if is_variant else "original"
        explanation_vi = str(variant_row["explanation_vi"] or q["explanation_vi"]) if is_variant else str(q["explanation_vi"])

        passage_row = None
        if q["passage_id"] is not None:
            passage_row = conn.execute("SELECT * FROM PASSAGES WHERE id=?", (q["passage_id"],)).fetchone()

        from n3_mastery.grammar_engine import get_question_grammar_payload

        grammar_breakdown = get_question_grammar_payload(question_id, conn)
    finally:
        conn.close()

    evidence_correct: Optional[bool] = None
    answer_correct: bool = False
    gold_evidence_indices: List[int] = []
    assembled_sentence: Optional[str] = None
    expected_slots_order: Optional[List[int]] = None
    user_payload: Dict[str, Any] = {"session_seed": session_seed}

    # Case 1: Full 4-Slot Star Assembly (問題2)
    if (q["section"] == "grammar" and q["mondai_type"] == "問題2" and q_meta.get("star_assembly")) or variant_mode == "star_4slot_shift":
        valid_slots = _validate_4slot_order(slot_order)
        sa = v_meta if is_variant else q_meta.get("star_assembly", {})
        expected_slots_order = list(sa["slots_order"])
        star_slot_idx = int(sa.get("star_slot_index", 2))
        assembled_sentence = sa.get("full_sentence", "")
        is_correct = valid_slots == expected_slots_order
        answer_correct = is_correct
        user_payload["slot_order"] = valid_slots
        user_payload["star_slot_index"] = star_slot_idx
        correct_display_text = raw_options[expected_slots_order[star_slot_idx]]
    else:
        # Permute using the exact same session_seed + item_key to resolve display index back to canonical index
        item_key = f"v{variant_row['id']}" if is_variant else f"q{q['id']}"
        permuted_opts, display_correct_idx, index_map = permute_options(
            raw_options, orig_correct_idx, session_seed=session_seed, item_key=item_key
        )
        if selected_index is None or not (0 <= int(selected_index) <= 3):
            raise ValueError("Vui lòng chọn 1 đáp án hợp lệ từ 1 đến 4 (0..3).")
        sel_idx = int(selected_index)
        orig_selected_idx = index_map[sel_idx]
        answer_correct = orig_selected_idx == orig_correct_idx
        correct_display_text = raw_options[orig_correct_idx]
        user_payload["selected_display_index"] = sel_idx
        user_payload["selected_orig_index"] = orig_selected_idx
        user_payload["expected_display_index"] = display_correct_idx

        # Case 2: Evidence-First Dokkai
        if variant_mode == "dokkai_evidence" and passage_row is not None:
            if not evidence_indices or len(evidence_indices) == 0:
                raise ValueError(
                    "Chế độ Evidence-First yêu cầu bấm chọn ít nhất 1 câu chốt / điều kiện bằng chứng trong đoạn văn trước khi nộp!"
                )
            gold_evidence_indices = list(v_meta.get("evidence_indices") or q_meta.get("evidence_indices") or [0])
            clean_ev = [int(i) for i in evidence_indices]
            evidence_correct = bool(set(clean_ev) & set(gold_evidence_indices))
            is_correct = evidence_correct and answer_correct
            user_payload["evidence_indices"] = clean_ev
            user_payload["gold_evidence_indices"] = gold_evidence_indices
        else:
            is_correct = answer_correct

    # Determine FSRS rating
    if not is_correct:
        rating = Rating.AGAIN.value
    elif used_hint:
        rating = Rating.HARD.value
    elif response_sec > 0 and response_sec <= 12.0:
        rating = Rating.EASY.value
    else:
        rating = Rating.GOOD.value

    # Persist attempt log and update flags
    with transaction(db_path) as conn:
        conn.execute(
            """
            INSERT INTO ATTEMPT_LOGS
                (question_id, variant_id, mock_exam_id, mode, is_correct, used_hint, response_sec, user_payload_json, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                question_id,
                variant_id,
                mock_exam_id,
                mode,
                1 if is_correct else 0,
                1 if used_hint else 0,
                float(response_sec),
                json.dumps(user_payload, ensure_ascii=False),
                format_iso(ts_now),
            ),
        )
        if is_correct:
            if not is_variant and not used_hint:
                conn.execute(
                    "UPDATE FSRS_STATES SET clean_original_passed=1 WHERE question_id=?",
                    (question_id,),
                )
            elif is_variant and not used_hint:
                conn.execute(
                    "UPDATE FSRS_STATES SET variant_passed=1 WHERE question_id=?",
                    (question_id,),
                )
        else:
            if not is_variant:
                conn.execute(
                    "UPDATE FSRS_STATES SET clean_original_passed=0 WHERE question_id=?",
                    (question_id,),
                )
            else:
                conn.execute(
                    "UPDATE FSRS_STATES SET variant_passed=0 WHERE question_id=?",
                    (question_id,),
                )

    fsrs_res = apply_fsrs_update(
        question_id=question_id,
        rating=rating,
        used_hint=used_hint,
        now=ts_now,
        is_clean_pass_override=(is_correct and not used_hint),
        db_path=db_path,
    )

    remediated = prev_state == "relearning" and is_correct
    sentences = json.loads(passage_row["evidence_sentences_json"] or "[]") if passage_row else []
    gold_evidence_texts = [sentences[i] for i in gold_evidence_indices if 0 <= i < len(sentences)]

    return {
        "question_id": question_id,
        "variant_id": variant_id,
        "variant_mode": variant_mode,
        "is_correct": is_correct,
        "answer_correct": answer_correct,
        "evidence_correct": evidence_correct,
        "gold_evidence_indices": gold_evidence_indices,
        "gold_evidence_texts": gold_evidence_texts,
        "correct_option_text": correct_display_text,
        "expected_slots_order": expected_slots_order,
        "expected_chunks": [raw_options[i] for i in expected_slots_order] if expected_slots_order else None,
        "assembled_sentence": assembled_sentence,
        "translation_vi": q["translation_vi"],
        "explanation_vi": explanation_vi,
        "passage_translation_vi": passage_row["vietnamese_text"] if passage_row else None,
        "condition_matrix": json.loads(passage_row["condition_matrix_json"] or "[]") if passage_row else [],
        "notebook_meta": q_meta,
        "grammar_breakdown": grammar_breakdown,
        "remediated": remediated,
        "fsrs": fsrs_res,
    }


def get_error_notebook(limit: int = 100, db_path: Optional[Path] = None) -> List[Dict[str, Any]]:
    """Return questions currently in Relearning or with a failed latest attempt."""
    conn = get_connection(db_path)
    try:
        rows = conn.execute(
            """
            SELECT q.id, q.unit_code, q.section, q.mondai_type, q.source_label,
                   q.focus_keyword, q.prompt_jp, q.explanation_vi, q.notebook_meta_json,
                   f.state, f.lapses, f.stability,
                   (SELECT mode FROM ATTEMPT_LOGS a WHERE a.question_id=q.id ORDER BY a.id DESC LIMIT 1) AS last_mode,
                   (SELECT is_correct FROM ATTEMPT_LOGS a WHERE a.question_id=q.id ORDER BY a.id DESC LIMIT 1) AS last_correct,
                   (SELECT created_at FROM ATTEMPT_LOGS a WHERE a.question_id=q.id ORDER BY a.id DESC LIMIT 1) AS last_attempt_at
            FROM QUESTIONS q
            JOIN FSRS_STATES f ON f.question_id = q.id
            WHERE f.state = 'relearning'
               OR EXISTS (
                    SELECT 1 FROM ATTEMPT_LOGS a
                    WHERE a.id = (SELECT MAX(id) FROM ATTEMPT_LOGS a2 WHERE a2.question_id = q.id)
                      AND a.is_correct = 0
               )
            ORDER BY f.lapses DESC, last_attempt_at DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
        from n3_mastery.grammar_engine import get_question_grammar_payload

        items: List[Dict[str, Any]] = []
        for r in rows:
            q_id = int(r["id"])
            items.append(
                {
                    "question_id": q_id,
                    "unit_code": r["unit_code"],
                    "section": r["section"],
                    "mondai_type": r["mondai_type"],
                    "source_label": r["source_label"],
                    "focus_keyword": r["focus_keyword"],
                    "prompt_jp": r["prompt_jp"],
                    "explanation_vi": r["explanation_vi"],
                    "state": r["state"],
                    "lapses": int(r["lapses"]),
                    "stability": float(r["stability"]),
                    "last_mode": r["last_mode"],
                    "last_attempt_at": r["last_attempt_at"],
                    "grammar_breakdown": get_question_grammar_payload(q_id, conn),
                }
            )
        return items
    finally:
        conn.close()


def get_next_study_candidate(
    unit_code: Optional[str] = None,
    mode: str = "mixed",
    session_seed: str = "default",
    exam_mode: bool = False,
    now: Optional[datetime] = None,
    db_path: Optional[Path] = None,
) -> Optional[Dict[str, Any]]:
    """Select the highest-priority next study item (Remediation -> Original/Variant -> Due Review)."""
    conn = get_connection(db_path)
    try:
        where_unit = "AND q.unit_code=?" if unit_code else ""
        params = (unit_code,) if unit_code else ()

        if mode == "remediation":
            row = conn.execute(
                f"""
                SELECT q.id FROM QUESTIONS q
                JOIN FSRS_STATES f ON f.question_id=q.id
                WHERE f.state='relearning' {where_unit}
                ORDER BY f.lapses DESC, q.id ASC LIMIT 1
                """,
                params,
            ).fetchone()
            if not row:
                return None
            return get_study_item(int(row["id"]), mode="original", session_seed=session_seed, exam_mode=exam_mode, db_path=db_path)

        if mode == "variant":
            # Prioritize questions/variants not yet passed, rotating across multiple variants per question
            row = conn.execute(
                f"""
                SELECT q.id, v.id AS vid FROM QUESTIONS q
                JOIN FSRS_STATES f ON f.question_id=q.id
                JOIN VARIANT_DRILLS v ON v.question_id=q.id
                WHERE 1=1 {where_unit}
                ORDER BY
                    f.variant_passed ASC,
                    (SELECT COUNT(*) FROM ATTEMPT_LOGS a WHERE a.variant_id=v.id AND a.is_correct=1) ASC,
                    COALESCE(f.due_date, '') ASC,
                    q.id ASC,
                    v.id ASC
                LIMIT 1
                """,
                params,
            ).fetchone()
            if not row:
                return None
            return get_study_item(int(row["id"]), mode="variant", variant_id=int(row["vid"]), session_seed=session_seed, exam_mode=exam_mode, db_path=db_path)

        if mode == "original":
            due_ids = get_due_question_ids(unit_code=unit_code, limit=1, now=now, db_path=db_path)
            q_id = due_ids[0] if due_ids else None
            if q_id is None:
                row = conn.execute(
                    f"SELECT q.id FROM QUESTIONS q JOIN FSRS_STATES f ON f.question_id=q.id WHERE 1=1 {where_unit} ORDER BY f.clean_original_passed ASC, q.id ASC LIMIT 1",
                    params,
                ).fetchone()
                q_id = int(row["id"]) if row else None
            if q_id is None:
                return None
            return get_study_item(q_id, mode="original", session_seed=session_seed, exam_mode=exam_mode, db_path=db_path)

        # Mixed mode (Just-in-Time anti-rote loop):
        # 1. Relearning card first
        rem = conn.execute(
            f"""
            SELECT q.id FROM QUESTIONS q JOIN FSRS_STATES f ON f.question_id=q.id
            WHERE f.state='relearning' {where_unit} ORDER BY f.lapses DESC, q.id ASC LIMIT 1
            """,
            params,
        ).fetchone()
        if rem:
            return get_study_item(int(rem["id"]), mode="original", session_seed=session_seed, exam_mode=exam_mode, db_path=db_path)

        # 2. Questions that passed original cleanly but haven't passed anti-rote variant yet!
        need_var = conn.execute(
            f"""
            SELECT q.id, v.id AS vid FROM QUESTIONS q
            JOIN FSRS_STATES f ON f.question_id=q.id
            JOIN VARIANT_DRILLS v ON v.question_id=q.id
            WHERE f.clean_original_passed=1 AND f.variant_passed=0 {where_unit}
            ORDER BY q.id ASC, v.id ASC LIMIT 1
            """,
            params,
        ).fetchone()
        if need_var:
            return get_study_item(int(need_var["id"]), mode="variant", variant_id=int(need_var["vid"]), session_seed=session_seed, exam_mode=exam_mode, db_path=db_path)

        # 3. Unattempted original question
        unattempted = conn.execute(
            f"""
            SELECT q.id FROM QUESTIONS q JOIN FSRS_STATES f ON f.question_id=q.id
            WHERE f.clean_original_passed=0 {where_unit}
            ORDER BY q.id ASC LIMIT 1
            """,
            params,
        ).fetchone()
        if unattempted:
            return get_study_item(int(unattempted["id"]), mode="original", session_seed=session_seed, exam_mode=exam_mode, db_path=db_path)

        # 4. Due FSRS review (alternating to least-practiced variant if already clean)
        due_ids = get_due_question_ids(unit_code=unit_code, limit=1, now=now, db_path=db_path)
        if due_ids:
            q_id = due_ids[0]
            v_row = conn.execute(
                """
                SELECT v.id FROM VARIANT_DRILLS v
                WHERE v.question_id=?
                ORDER BY (SELECT COUNT(*) FROM ATTEMPT_LOGS a WHERE a.variant_id=v.id AND a.is_correct=1) ASC, v.id ASC
                LIMIT 1
                """,
                (q_id,),
            ).fetchone()
            return get_study_item(q_id, mode="variant" if v_row else "original", variant_id=int(v_row["id"]) if v_row else None, session_seed=session_seed, exam_mode=exam_mode, db_path=db_path)
        return None
    finally:
        conn.close()
