"""Comprehensive tests for JLPT N5-N2 Grammar Corpus, 163/163 Question Anatomy, Non-destructive Migration, Zero-Leakage API, and Rich CLI."""

import hashlib
import io
import json
import re
import shutil
import sqlite3
from pathlib import Path

import openpyxl
import pytest
from fastapi.testclient import TestClient

from n3_mastery import cli
from n3_mastery.api import app
from n3_mastery.config import BASE_DIR
from n3_mastery.database import get_connection
from n3_mastery.importer import compute_question_hash, import_all_excel

FORBIDDEN_EMOJI_RE = re.compile(r"[\U0001F300-\U0001FAFF\u2600-\u2604\u2606-\u26FF\u2700-\u27BF]")


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def test_zero_decorative_emojis_in_grammar_files_and_seeded_db(isolated_db):
    """Ensure 0 decorative emojis across grammar Python modules, UI assets, and seeded DB tables."""
    checked_files = [
        BASE_DIR / "n3_mastery" / "grammar_corpus.py",
        BASE_DIR / "n3_mastery" / "question_grammar_map.py",
        BASE_DIR / "n3_mastery" / "grammar_engine.py",
        BASE_DIR / "n3_mastery" / "database.py",
        BASE_DIR / "n3_mastery" / "api.py",
        BASE_DIR / "n3_mastery" / "cli.py",
        BASE_DIR / "n3_mastery" / "templates" / "index.html",
        BASE_DIR / "n3_mastery" / "static" / "app.css",
        BASE_DIR / "n3_mastery" / "static" / "app.js",
        BASE_DIR / "DESIGN.md",
    ]
    for path in checked_files:
        assert path.exists(), f"Missing expected file: {path}"
        content = path.read_text(encoding="utf-8")
        found = FORBIDDEN_EMOJI_RE.findall(content)
        assert found == [], f"Found forbidden emoji {found} in {path.name}"

    import_all_excel(generate_variants=False)
    conn = get_connection()
    try:
        tables = [
            "GRAMMAR_POINTS",
            "QUESTION_GRAMMAR_LINKS",
            "QUESTION_GRAMMAR_ANALYSES",
            "GRAMMAR_DRILLS",
            "VOCAB_FOUNDATION",
        ]
        for tbl in tables:
            rows = conn.execute(f"SELECT * FROM {tbl}").fetchall()
            for r in rows:
                for col in r.keys():
                    val = r[col]
                    if isinstance(val, str):
                        found = FORBIDDEN_EMOJI_RE.findall(val)
                        assert found == [], f"Found forbidden emoji {found} in DB {tbl}.{col}: {val[:80]}"
    finally:
        conn.close()


def test_grammar_points_corpus_completeness_and_pedagogical_fields():
    """Verify >= 135 grammar points spanning N5/N4/N3/N2 with complete 3D Form-Meaning-Use fields."""
    from n3_mastery.grammar_corpus import GRAMMAR_POINTS_DATA

    assert len(GRAMMAR_POINTS_DATA) >= 135
    codes = [p["code"] for p in GRAMMAR_POINTS_DATA]
    assert len(codes) == len(set(codes)), "Duplicate grammar point codes detected"

    levels = {p["jlpt_level"] for p in GRAMMAR_POINTS_DATA}
    assert {"N5", "N4", "N3", "N2"}.issubset(levels)
    n2_points = [p for p in GRAMMAR_POINTS_DATA if p["jlpt_level"] == "N2"]
    assert len(n2_points) >= 12, f"Expected >= 12 N2 extension points, got {len(n2_points)}"

    for pt in GRAMMAR_POINTS_DATA:
        assert isinstance(pt["code"], str) and pt["code"].strip()
        assert isinstance(pt["pattern"], str) and pt["pattern"].strip()
        assert pt["jlpt_level"] in {"N5", "N4", "N3", "N2", "N1"}
        assert isinstance(pt["category"], str) and pt["category"].strip()
        assert isinstance(pt["category_label_vi"], str) and pt["category_label_vi"].strip()
        assert isinstance(pt["in_exam_corpus"], bool)
        assert isinstance(pt["formation_formula"], str) and len(pt["formation_formula"].strip()) >= 3
        assert isinstance(pt["core_meaning_vi"], str) and len(pt["core_meaning_vi"].strip()) >= 4
        assert isinstance(pt["deep_explanation_vi"], str) and len(pt["deep_explanation_vi"].strip()) >= 20
        assert isinstance(pt["register_tag"], str) and pt["register_tag"].strip()
        assert isinstance(pt["source_ref"], str) and pt["source_ref"].strip()
        assert isinstance(pt["search_keywords"], str) and pt["search_keywords"].strip()

        ft = pt["formation_table"]
        assert isinstance(ft, list) and len(ft) >= 1, f"{pt['code']} missing formation_table"
        for row in ft:
            assert isinstance(row.get("pos"), str) and row["pos"].strip()
            assert isinstance(row.get("rule"), str) and row["rule"].strip()

        examples = pt["examples"]
        assert isinstance(examples, list) and len(examples) >= 2, f"{pt['code']} must have >= 2 examples"
        for ex in examples:
            assert isinstance(ex.get("jp"), str) and ex["jp"].strip()
            assert isinstance(ex.get("vi"), str) and ex["vi"].strip()
            assert isinstance(ex.get("reading_note"), str)
            assert isinstance(ex.get("grammar_note"), str)

        cp = pt.get("confusable_pairs", [])
        assert isinstance(cp, list)
        for pair in cp:
            assert isinstance(pair.get("rival_pattern"), str) and pair["rival_pattern"].strip()
            assert isinstance(pair.get("difference_vi"), str) and pair["difference_vi"].strip()
            assert isinstance(pair.get("quick_test_vi"), str) and pair["quick_test_vi"].strip()

        mp = pt.get("match_patterns", [])
        assert isinstance(mp, list) and len(mp) >= 1, f"{pt['code']} missing match_patterns"


def test_grammar_drills_completeness_diagnostics_and_no_answer_leaks():
    """Verify >= 270 grammar drills, all 3 drill types, 4 distinct options, 4 diagnostics, and 0 answer leaks."""
    from n3_mastery.grammar_corpus import GRAMMAR_DRILLS_DATA, GRAMMAR_POINTS_DATA

    assert len(GRAMMAR_DRILLS_DATA) >= 270
    valid_codes = {p["code"] for p in GRAMMAR_POINTS_DATA}

    drill_keys = [d["drill_key"] for d in GRAMMAR_DRILLS_DATA]
    assert len(drill_keys) == len(set(drill_keys)), "Duplicate drill_key values detected"

    drill_types = {d["drill_type"] for d in GRAMMAR_DRILLS_DATA}
    assert drill_types == {"formation", "contrast", "application"}

    drills_per_code = {c: 0 for c in valid_codes}
    for d in GRAMMAR_DRILLS_DATA:
        gc = d["grammar_code"]
        assert gc in valid_codes, f"Drill {d['drill_key']} references unknown grammar_code {gc}"
        drills_per_code[gc] += 1

        prompt = str(d["prompt_jp"])
        assert prompt.strip()
        assert isinstance(d["translation_vi"], str) and d["translation_vi"].strip()
        assert isinstance(d["explanation_vi"], str) and d["explanation_vi"].strip()

        opts = d["options"]
        assert isinstance(opts, list) and len(opts) == 4
        clean_opts = [str(o).strip() for o in opts]
        assert all(clean_opts), f"Empty option in {d['drill_key']}"
        assert len(set(clean_opts)) == 4, f"Duplicate options in {d['drill_key']}: {opts}"

        c_idx = d["correct_index"]
        assert isinstance(c_idx, int) and 0 <= c_idx <= 3

        diags = d["option_diagnostics"]
        assert isinstance(diags, list) and len(diags) == 4
        assert all(isinstance(x, str) and len(x.strip()) >= 8 for x in diags), (
            f"Incomplete option_diagnostics in {d['drill_key']}"
        )

        # Anti-leak check: never reveal the exact answer in brackets or verbatim inside blank-fill stems
        ans = clean_opts[c_idx]
        assert f"【{ans}】" not in prompt, f"Bracketed answer leak in {d['drill_key']}"
        assert f"（{ans}）" not in prompt, f"Parenthesized answer leak in {d['drill_key']}"
        assert f"({ans})" not in prompt, f"Parenthesized answer leak in {d['drill_key']}"
        if re.search(r"[（(]\s*[）)]|＿+|\[[\s_]*\]", prompt):
            prompt_without_quoted = re.sub(r"「[^」]*」", "", prompt)
            if len(ans) >= 3:
                assert ans not in prompt_without_quoted, (
                    f"Answer '{ans}' leaked in blank-fill prompt of {d['drill_key']}: {prompt}"
                )

    under_drilled = [c for c, cnt in drills_per_code.items() if cnt < 2]
    assert under_drilled == [], f"Grammar points with < 2 drills: {under_drilled}"


def test_all_163_exam_questions_grammar_mapped_and_analyzed(isolated_db):
    """Verify 163/163 exam questions have QUESTION_GRAMMAR_ANALYSES and >= 1 link; 42/42 grammar have primary_target + 4 notes."""
    from n3_mastery.grammar_engine import seed_grammar_and_foundation
    from n3_mastery.question_grammar_map import QUESTION_GRAMMAR_MAP

    summary = import_all_excel(generate_variants=False)
    assert summary["unique_questions"] == 163

    # Verify idempotent re-seeding never duplicates rows
    seed_grammar_and_foundation()

    conn = get_connection()
    try:
        q_rows = conn.execute(
            "SELECT id, content_hash, section, mondai_type, prompt_jp, options_json FROM QUESTIONS ORDER BY id"
        ).fetchall()
        assert len(q_rows) == 163

        for qr in q_rows:
            recomputed = compute_question_hash(qr["prompt_jp"], json.loads(qr["options_json"]))
            assert qr["content_hash"] in QUESTION_GRAMMAR_MAP or recomputed in QUESTION_GRAMMAR_MAP, (
                f"Question id={qr['id']} missing from QUESTION_GRAMMAR_MAP"
            )

        analyses_cnt = conn.execute("SELECT COUNT(*) FROM QUESTION_GRAMMAR_ANALYSES").fetchone()[0]
        assert analyses_cnt == 163

        missing_analyses = conn.execute(
            """
            SELECT q.id FROM QUESTIONS q
            LEFT JOIN QUESTION_GRAMMAR_ANALYSES a ON a.question_id = q.id
            WHERE a.question_id IS NULL
               OR trim(a.structure_parse_vi) = ''
               OR trim(a.pedagogical_takeaway_vi) = ''
            """
        ).fetchall()
        assert missing_analyses == []

        linked_q_cnt = conn.execute("SELECT COUNT(DISTINCT question_id) FROM QUESTION_GRAMMAR_LINKS").fetchone()[0]
        assert linked_q_cnt == 163

        grammar_qs = conn.execute(
            "SELECT id, mondai_type FROM QUESTIONS WHERE section='grammar' ORDER BY id"
        ).fetchall()
        assert len(grammar_qs) == 42
        for gq in grammar_qs:
            primary = conn.execute(
                "SELECT COUNT(*) FROM QUESTION_GRAMMAR_LINKS WHERE question_id=? AND role='primary_target'",
                (gq["id"],),
            ).fetchone()[0]
            assert primary >= 1, f"Grammar question id={gq['id']} missing primary_target link"

            ana = conn.execute(
                "SELECT option_grammar_notes_json FROM QUESTION_GRAMMAR_ANALYSES WHERE question_id=?",
                (gq["id"],),
            ).fetchone()
            notes = json.loads(ana["option_grammar_notes_json"] or "[]")
            assert len(notes) == 4 and all(isinstance(n, str) and n.strip() for n in notes), (
                f"Grammar question id={gq['id']} must have 4 option_grammar_notes"
            )
    finally:
        conn.close()


def test_vocab_foundation_seeded_from_exam_and_curriculum(isolated_db):
    """Verify VOCAB_FOUNDATION >= 150 combining both exam corpus vocab and curated textbook vocab."""
    from n3_mastery.grammar_corpus import VOCAB_FOUNDATION_CURATED

    assert len(VOCAB_FOUNDATION_CURATED) >= 120
    import_all_excel(generate_variants=False)
    conn = get_connection()
    try:
        total = conn.execute("SELECT COUNT(*) FROM VOCAB_FOUNDATION").fetchone()[0]
        exam_cnt = conn.execute("SELECT COUNT(*) FROM VOCAB_FOUNDATION WHERE in_exam_corpus=1").fetchone()[0]
        curated_cnt = conn.execute("SELECT COUNT(*) FROM VOCAB_FOUNDATION WHERE in_exam_corpus=0").fetchone()[0]
        assert total >= 150
        assert exam_cnt >= 30
        assert curated_cnt >= 100
    finally:
        conn.close()


def test_non_destructive_migration_on_backup_db_copy(tmp_path, monkeypatch):
    """Verify upgrading a copy of backup_pre_grammar.db preserves all 41 ATTEMPT_LOGS and 163 QUESTIONS intact."""
    backup_src = BASE_DIR / "data" / "n3_mastery.backup_pre_grammar.db"
    assert backup_src.exists(), f"Missing backup DB at {backup_src}"
    src_hash_before = _sha256_file(backup_src)

    copy_db = tmp_path / "migrated_backup_copy.db"
    shutil.copy2(backup_src, copy_db)

    # Snapshot original ATTEMPT_LOGS & QUESTIONS from temp copy before migration
    pre_conn = sqlite3.connect(str(copy_db))
    pre_conn.row_factory = sqlite3.Row
    pre_attempts = [
        tuple(r)
        for r in pre_conn.execute(
            "SELECT id, question_id, variant_id, mock_exam_id, mode, is_correct, used_hint, response_sec, user_payload_json, created_at FROM ATTEMPT_LOGS ORDER BY id"
        ).fetchall()
    ]
    pre_questions = [
        tuple(r)
        for r in pre_conn.execute("SELECT id, content_hash, unit_code, section FROM QUESTIONS ORDER BY id").fetchall()
    ]
    pre_fsrs = [
        tuple(r)
        for r in pre_conn.execute(
            "SELECT question_id, stability, difficulty, reps, lapses, state FROM FSRS_STATES ORDER BY question_id"
        ).fetchall()
    ]
    pre_conn.close()
    assert len(pre_attempts) == 41
    assert len(pre_questions) == 163
    assert len(pre_fsrs) == 163

    monkeypatch.setenv("N3_MASTERY_DB_PATH", str(copy_db))
    with TestClient(app) as client:
        h = client.get("/api/health")
        assert h.status_code == 200
        hd = h.json()
        assert hd["total_questions"] == 163
        assert hd["grammar_points"] >= 135
        assert hd["grammar_drills"] >= 270
        assert hd["question_grammar_analyses"] == 163
        assert hd["vocab_foundation"] >= 150

    post_conn = get_connection(copy_db)
    try:
        post_attempts = [
            tuple(r)
            for r in post_conn.execute(
                "SELECT id, question_id, variant_id, mock_exam_id, mode, is_correct, used_hint, response_sec, user_payload_json, created_at FROM ATTEMPT_LOGS ORDER BY id"
            ).fetchall()
        ]
        post_questions = [
            tuple(r)
            for r in post_conn.execute("SELECT id, content_hash, unit_code, section FROM QUESTIONS ORDER BY id").fetchall()
        ]
        post_fsrs = [
            tuple(r)
            for r in post_conn.execute(
                "SELECT question_id, stability, difficulty, reps, lapses, state FROM FSRS_STATES ORDER BY question_id"
            ).fetchall()
        ]
        assert post_attempts == pre_attempts
        assert post_questions == pre_questions
        assert post_fsrs == pre_fsrs
        assert post_conn.execute("SELECT COUNT(*) FROM GRAMMAR_FSRS_STATES").fetchone()[0] >= 135
    finally:
        post_conn.close()

    assert _sha256_file(backup_src) == src_hash_before, "Original backup file must remain untouched"


def test_zero_leakage_study_and_exam_vs_submit_and_errors(isolated_db):
    """Ensure grammar_breakdown and answers NEVER leak before submission, and DO appear after submit & in errors."""
    with TestClient(app) as client:
        # 1. GET /api/session/next on grammar unit (MU-08) and star unit (MU-10)
        for unit in ("MU-08", "MU-10", "MU-01"):
            res = client.get(f"/api/session/next?unit_code={unit}&mode=original&session_seed=zleak")
            assert res.status_code == 200
            item = res.json()["item"]
            assert "grammar_breakdown" not in item
            assert "correct_index" not in item
            assert "explanation_vi" not in item
            assert "correct_option_text" not in item

        # 2. GET /api/exam/generate must also have zero leakage
        ex_gen = client.get("/api/exam/generate?count_per_section=1&session_seed=zexam").json()
        for ex_item in ex_gen["items"]:
            assert "grammar_breakdown" not in ex_item
            assert "correct_index" not in ex_item
            assert "explanation_vi" not in ex_item

        # 3. Submit a guaranteed WRONG answer on MU-08 grammar MCQ to inspect grammar_breakdown & Error Notebook
        s_item = client.get("/api/session/next?unit_code=MU-08&mode=original&session_seed=wrongseed").json()["item"]
        conn = get_connection()
        try:
            q_row = conn.execute(
                "SELECT options_json, correct_index FROM QUESTIONS WHERE id=?",
                (s_item["question_id"],),
            ).fetchone()
        finally:
            conn.close()
        correct_txt = json.loads(q_row["options_json"])[int(q_row["correct_index"])]
        wrong_disp_idx = next(i for i, opt in enumerate(s_item["options"]) if opt != correct_txt)

        sub = client.post(
            "/api/session/submit",
            json={
                "question_id": s_item["question_id"],
                "mode": "original",
                "selected_index": wrong_disp_idx,
                "session_seed": "wrongseed",
            },
        )
        assert sub.status_code == 200
        sub_res = sub.json()["result"]
        assert sub_res["is_correct"] is False
        gb = sub_res.get("grammar_breakdown")
        assert isinstance(gb, dict)
        assert gb["structure_parse_vi"].strip()
        assert gb["pedagogical_takeaway_vi"].strip()
        assert len(gb["option_grammar_notes"]) == 4
        assert len(gb["grammar_points"]) >= 1
        assert gb["grammar_points"][0]["code"]

        # 4. Error notebook includes grammar_breakdown
        errs = client.get("/api/errors").json()["errors"]
        matched = [e for e in errs if e["question_id"] == s_item["question_id"]]
        assert len(matched) == 1
        assert isinstance(matched[0].get("grammar_breakdown"), dict)
        assert matched[0]["grammar_breakdown"]["structure_parse_vi"].strip()

        # 5. Exam submit details include grammar_breakdown
        exam_answers = []
        for it in ex_gen["items"]:
            if it["interaction_type"] == "star_4slot":
                exam_answers.append({"question_id": it["question_id"], "slot_order": [0, 1, 2, 3], "session_seed": "zexam"})
            else:
                exam_answers.append({"question_id": it["question_id"], "selected_index": 0, "session_seed": "zexam"})
        ex_sub = client.post("/api/exam/submit", json={"exam_mode": "mini_mock", "answers": exam_answers, "duration_sec": 30.0})
        assert ex_sub.status_code == 200
        for det in ex_sub.json()["details"]:
            assert isinstance(det.get("grammar_breakdown"), dict)
            assert det["grammar_breakdown"]["structure_parse_vi"].strip()


def test_readiness_scores_start_at_zero_and_independent_of_grammar_drills(isolated_db):
    """Original Bank Score and Mastery Score start at 0.00 and are unaffected by Grammar Drills."""
    with TestClient(app) as client:
        dash = client.get("/api/dashboard").json()
        assert dash["readiness"]["original_score_10"] == 0.0
        assert dash["readiness"]["mastery_score_10"] == 0.0
        assert dash["grammar_summary"]["total_points"] >= 135

        # Complete one grammar drill
        nxt = client.get("/api/grammar/drill/next?drill_type=formation&session_seed=indep").json()
        assert nxt["empty"] is False
        drill_id = nxt["drill"]["drill_id"]
        sub = client.post(
            "/api/grammar/drill/submit",
            json={"drill_id": drill_id, "selected_index": 0, "response_sec": 4.0, "session_seed": "indep"},
        )
        assert sub.status_code == 200

        dash_after = client.get("/api/dashboard").json()
        assert dash_after["readiness"]["original_score_10"] == 0.0
        assert dash_after["readiness"]["mastery_score_10"] == 0.0


def test_grammar_api_workflow_shuffle_fsrs_vocab_import_and_xlsx_autolink(isolated_db):
    """End-to-end test of /api/grammar/*, /api/foundation/vocab, JSON N2 import, and .xlsx auto-linking."""
    with TestClient(app) as client:
        # 1. Overview
        ov = client.get("/api/grammar/overview")
        assert ov.status_code == 200
        ov_data = ov.json()
        assert ov_data["total_points"] >= 135
        assert ov_data["exam_corpus_count"] >= 20
        assert ov_data["jlpt_extension_count"] >= 40
        level_map = {lv["level"]: lv for lv in ov_data["levels"]}
        for lv in ("N5", "N4", "N3", "N2"):
            assert lv in level_map
            assert level_map[lv]["total"] > 0

        # 2. List & Filter points
        pts_exam = client.get("/api/grammar/points?scope=exam").json()
        assert pts_exam["total"] > 0
        assert all(p["in_exam_corpus"] is True for p in pts_exam["points"])

        pts_n2 = client.get("/api/grammar/points?level=N2").json()
        assert pts_n2["total"] >= 12
        assert all(p["jlpt_level"] == "N2" for p in pts_n2["points"])

        # 3. Point detail (pick an exam-linked point)
        sample_code = pts_exam["points"][0]["code"]
        detail = client.get(f"/api/grammar/points/{sample_code}")
        assert detail.status_code == 200
        det = detail.json()
        assert det["code"] == sample_code
        assert len(det["formation_table"]) >= 1
        assert len(det["examples"]) >= 2
        assert len(det["linked_questions"]) >= 1
        assert det["drills_summary"]["total"] >= 2
        assert "fsrs" in det

        assert client.get("/api/grammar/points/GP-NOT-FOUND-999").status_code == 404

        # 4. Drill next deterministic option permutation + zero leakage
        seen_orders = set()
        first_drill = None
        for idx in range(12):
            r = client.get(f"/api/grammar/drill/next?grammar_code={sample_code}&session_seed=gseed-{idx}")
            assert r.status_code == 200
            payload = r.json()
            assert payload["empty"] is False
            dr = payload["drill"]
            assert "correct_index" not in dr
            assert "explanation_vi" not in dr
            assert "option_diagnostics" not in dr
            assert "pattern" not in dr
            assert len(dr["options"]) == 4
            if first_drill is None:
                first_drill = dr
            if dr["drill_id"] == first_drill["drill_id"]:
                seen_orders.add(tuple(dr["options"]))
        assert len(seen_orders) >= 2, "Option permutation must vary across session_seed values"

        # 5. Drill submit: wrong -> relearning & lapses++, then right -> review & passed flag
        seed_use = "gseed-0"
        dr_check = client.get(f"/api/grammar/drill/next?grammar_code={sample_code}&session_seed={seed_use}").json()["drill"]
        conn = get_connection()
        try:
            d_row = conn.execute(
                "SELECT grammar_id, options_json, correct_index FROM GRAMMAR_DRILLS WHERE id=?",
                (dr_check["drill_id"],),
            ).fetchone()
        finally:
            conn.close()
        orig_correct_txt = json.loads(d_row["options_json"])[int(d_row["correct_index"])]
        wrong_idx = next(i for i, o in enumerate(dr_check["options"]) if o != orig_correct_txt)
        right_idx = dr_check["options"].index(orig_correct_txt)

        sub_wrong = client.post(
            "/api/grammar/drill/submit",
            json={"drill_id": dr_check["drill_id"], "selected_index": wrong_idx, "response_sec": 5.0, "session_seed": seed_use},
        )
        assert sub_wrong.status_code == 200
        sw = sub_wrong.json()
        assert sw["is_correct"] is False
        assert sw["fsrs"]["state"] == "relearning"
        assert sw["fsrs"]["lapses"] >= 1
        assert len(sw["option_diagnostics"]) == 4
        assert sw["selected_diagnostic"] == sw["option_diagnostics"][wrong_idx]

        sub_right = client.post(
            "/api/grammar/drill/submit",
            json={"drill_id": dr_check["drill_id"], "selected_index": right_idx, "response_sec": 4.2, "session_seed": seed_use},
        )
        assert sub_right.status_code == 200
        sr = sub_right.json()
        assert sr["is_correct"] is True
        assert sr["correct_option_text"] == orig_correct_txt
        assert sr["fsrs"]["state"] != "relearning"
        assert sr["fsrs"]["reps"] >= 2

        conn = get_connection()
        try:
            log_cnt = conn.execute(
                "SELECT COUNT(*) FROM GRAMMAR_ATTEMPT_LOGS WHERE drill_id=?",
                (dr_check["drill_id"],),
            ).fetchone()[0]
            assert log_cnt == 2
        finally:
            conn.close()

        # 6. Foundation vocab endpoint
        vocab_all = client.get("/api/foundation/vocab?limit=200").json()
        assert vocab_all["total"] >= 150
        vocab_exam = client.get("/api/foundation/vocab?scope=exam").json()
        assert vocab_exam["total"] >= 30
        assert all(v["in_exam_corpus"] is True for v in vocab_exam["items"])

        # 7. Import N2 JSON expansion pack via POST /api/grammar/import
        n2_pack = {
            "grammar_points": [
                {
                    "code": "GP-N2-EXT-99",
                    "pattern": "～にもかかわらず",
                    "jlpt_level": "N2",
                    "category": "contrast_concession",
                    "category_label_vi": "Nhượng bộ & Tương phản",
                    "in_exam_corpus": False,
                    "formation_formula": "V(thường) / A-い / A-な・N(bỏ だ) + にかかわらず・にもかかわらず",
                    "formation_table": [
                        {"pos": "Động từ / A-い", "rule": "Thể thông thường + にもかかわらず"},
                        {"pos": "Danh từ / A-な", "rule": "Bỏ だ (hoặc である) + にもかかわらず"},
                    ],
                    "core_meaning_vi": "Mặc dù ... nhưng vẫn ... (tương phản ngoài mong đợi)",
                    "deep_explanation_vi": "Diễn tả kết quả xảy ra trái ngược hoàn toàn với điều kiện hoặc dự đoán ở vế trước, văn phong trang trọng hơn のに.",
                    "register_tag": "Văn viết / Trang trọng",
                    "confusable_pairs": [
                        {
                            "rival_pattern": "～のに",
                            "difference_vi": "のに mang sắc thái trách móc/tiếc nuối cá nhân trong khẩu ngữ; にもかかわらず khách quan và trang trọng hơn.",
                            "quick_test_vi": "Gặp văn bản báo chí hoặc thông báo hành chính -> ưu tiên にもかかわらず.",
                        }
                    ],
                    "examples": [
                        {
                            "jp": "激しい雨にもかかわらず、試合は予定通り行われた。",
                            "reading_note": "はげしいあめにもかかわらず",
                            "vi": "Mặc dù mưa rất to, trận đấu vẫn được tổ chức đúng kế hoạch.",
                            "grammar_note": "N (激しい雨) + にもかかわらず",
                        },
                        {
                            "jp": "忙しいにもかかわらず、わざわざ来てくださってありがとうございます。",
                            "reading_note": "いそがしいにもかかわらず",
                            "vi": "Mặc dù bận rộn nhưng cảm ơn anh đã cất công tới.",
                            "grammar_note": "A-い (忙しい) + にもかかわらず",
                        },
                    ],
                    "source_ref": "JSON N2 Expansion Test",
                    "search_keywords": "にもかかわらず mặc dù nhượng bộ N2",
                    "match_patterns": ["にもかかわらず"],
                }
            ],
            "drills": [
                {
                    "drill_key": "DR-N2-EXT-99-F1",
                    "grammar_code": "GP-N2-EXT-99",
                    "drill_type": "formation",
                    "prompt_jp": "大雨（　　　）、多くの人が会場に集まった。",
                    "options": ["にもかかわらず", "だにもかかわらず", "なのにもかかわらず", "てにもかかわらず"],
                    "correct_index": 0,
                    "translation_vi": "Mặc dù mưa lớn, rất nhiều người vẫn tập trung tại hội trường.",
                    "explanation_vi": "Danh từ đứng trực tiếp trước にもかかわらず, không thêm だ hay なの.",
                    "option_diagnostics": [
                        "[OK] Danh từ 大雨 kết hợp trực tiếp với にもかかわらず.",
                        "[FAIL] Sai hình thái: không dùng だ trước にもかかわらず.",
                        "[FAIL] Sai hình thái: không chèn なの trước にもかかわらず.",
                        "[FAIL] Sai hình thái: て không đi với danh từ 大雨.",
                    ],
                }
            ],
        }
        imp_json = client.post(
            "/api/grammar/import",
            files={"file": ("n2_pack.json", json.dumps(n2_pack, ensure_ascii=False).encode("utf-8"), "application/json")},
        )
        assert imp_json.status_code == 200
        imp_data = imp_json.json()
        assert imp_data["import_type"] == "json"
        assert imp_data["imported_grammar_points"] >= 1
        assert imp_data["imported_drills"] >= 1

        assert client.get("/api/grammar/points/GP-N2-EXT-99").status_code == 200
        ext_drill = client.get("/api/grammar/drill/next?grammar_code=GP-N2-EXT-99").json()
        assert ext_drill["empty"] is False
        assert ext_drill["drill"]["drill_key"] == "DR-N2-EXT-99-F1"

        # 8. Upload new .xlsx -> auto-links new question into QUESTION_GRAMMAR_ANALYSES & LINKS
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Phan_II_Ngu_Phap"
        ws.append(["Gói", "Câu", "Mẫu", "Đề bài", "Đ1", "Đ2", "Đ3", "Đ4", "T", "K", "ĐA", "ND", "Câu hoàn chỉnh", "GT"])
        ws.append([
            "II-1. 問題1: Ngữ pháp câu đơn",
            "1)",
            "～ように",
            "日本語が上手になる（　　　）、毎日練習している。",
            "ように",
            "ために",
            "ことに",
            "はずで",
            None,
            None,
            1,
            "1. ように",
            "日本語が上手になるように、毎日練習している。",
            "• Đáp án đúng: 1. ように (đạt trạng thái không chủ ý).",
        ])
        buf = io.BytesIO()
        wb.save(buf)
        up_xl = client.post(
            "/api/import/excel",
            files={"file": ("grammar_auto_link.xlsx", buf.getvalue(), "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")},
        )
        assert up_xl.status_code == 200
        assert up_xl.json()["health"]["total_questions"] == 164
        assert up_xl.json()["health"]["question_grammar_analyses"] == 164

        conn = get_connection()
        try:
            new_qid = conn.execute(
                "SELECT id FROM QUESTIONS WHERE prompt_jp LIKE '%日本語が上手になる%'"
            ).fetchone()[0]
            link_cnt = conn.execute(
                "SELECT COUNT(*) FROM QUESTION_GRAMMAR_LINKS WHERE question_id=?", (new_qid,)
            ).fetchone()[0]
            assert link_cnt >= 1
        finally:
            conn.close()


def test_cli_grammar_and_grammar_inspect(isolated_db, capsys):
    """Verify Rich CLI subcommands `grammar` and `grammar-inspect`."""
    assert cli.main(["import"]) == 0
    assert cli.main(["grammar"]) == 0
    assert cli.main(["grammar", "--level", "N3"]) == 0
    assert cli.main(["grammar", "--exam-only"]) == 0
    assert cli.main(["grammar", "--search", "ため"]) == 0

    conn = get_connection()
    try:
        sample_code = conn.execute("SELECT code FROM GRAMMAR_POINTS ORDER BY id LIMIT 1").fetchone()[0]
    finally:
        conn.close()

    assert cli.main(["grammar-inspect", sample_code]) == 0
    out = capsys.readouterr().out
    assert sample_code in out

    assert cli.main(["grammar-inspect", "GP-UNKNOWN-999"]) == 1


def test_grammar_drill_failure_resets_failed_type_flag_and_blocks_false_mastery(isolated_db):
    """Failing a grammar drill resets that specific drill_type passed flag until remediated."""
    with TestClient(app) as client:
        conn = get_connection()
        try:
            row = conn.execute(
                """
                SELECT gp.code, gp.id
                FROM GRAMMAR_POINTS gp
                JOIN GRAMMAR_DRILLS d ON d.grammar_id = gp.id
                GROUP BY gp.id
                HAVING COUNT(DISTINCT d.drill_type) = 3
                ORDER BY gp.id
                LIMIT 1
                """
            ).fetchone()
            assert row is not None
            code = row["code"]
            gp_id = row["id"]
            drills = {
                dt: conn.execute(
                    "SELECT id, options_json, correct_index FROM GRAMMAR_DRILLS WHERE grammar_id=? AND drill_type=? LIMIT 1",
                    (gp_id, dt),
                ).fetchone()
                for dt in ("formation", "contrast", "application")
            }
        finally:
            conn.close()

        def _submit_drill(drill_row, want_correct: bool, seed: str):
            did = int(drill_row["id"])
            opts = json.loads(drill_row["options_json"])
            corr_txt = opts[int(drill_row["correct_index"])]
            from n3_mastery.drill_engine import permute_options

            disp_opts, disp_corr, _ = permute_options(opts, int(drill_row["correct_index"]), seed, f"gd{did}")
            sel = disp_corr if want_correct else next(i for i in range(4) if disp_opts[i] != corr_txt)
            resp = client.post(
                "/api/grammar/drill/submit",
                json={"drill_id": did, "selected_index": sel, "response_sec": 3.0, "session_seed": seed},
            )
            assert resp.status_code == 200
            return resp.json()

        # Pass all 3 drill types cleanly -> mastered becomes True
        _submit_drill(drills["formation"], True, "m1")
        _submit_drill(drills["contrast"], True, "m2")
        r3 = _submit_drill(drills["application"], True, "m3")
        assert r3["fsrs"]["formation_passed"] is True
        assert r3["fsrs"]["contrast_passed"] is True
        assert r3["fsrs"]["application_passed"] is True
        assert r3["fsrs"]["mastered"] is True

        # Fail contrast -> contrast_passed resets to False and mastered becomes False
        r_fail = _submit_drill(drills["contrast"], False, "m4")
        assert r_fail["is_correct"] is False
        assert r_fail["fsrs"]["state"] == "relearning"
        assert r_fail["fsrs"]["contrast_passed"] is False
        assert r_fail["fsrs"]["mastered"] is False

        # Re-passing formation does NOT falsely restore mastered while contrast_passed is False
        r_form = _submit_drill(drills["formation"], True, "m5")
        assert r_form["fsrs"]["contrast_passed"] is False
        assert r_form["fsrs"]["mastered"] is False

        # Remediating contrast restores contrast_passed and mastered
        r_fix = _submit_drill(drills["contrast"], True, "m6")
        assert r_fix["fsrs"]["contrast_passed"] is True
        assert r_fix["fsrs"]["mastered"] is True
