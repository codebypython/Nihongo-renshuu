"""Tests for 12 Micro-Units N4->N3 Bridge Capsules and 100% anti-rote variant coverage."""

import json
import re

from n3_mastery.database import get_connection
from n3_mastery.importer import import_all_excel


def test_12_bridge_capsules_complete(isolated_db):
    import_all_excel(generate_variants=True)
    conn = get_connection()
    try:
        units = conn.execute("SELECT * FROM MICRO_UNITS ORDER BY order_index").fetchall()
        assert len(units) == 12
        assert [u["code"] for u in units] == [f"MU-{i:02d}" for i in range(1, 13)]

        capsules = conn.execute("SELECT * FROM N4_BRIDGE_CAPSULES").fetchall()
        assert len(capsules) == 12
        for cap in capsules:
            assert len(cap["grammar_focus"].strip()) >= 10
            assert len(cap["explanation_vi"].strip()) >= 40
            examples = json.loads(cap["examples_json"])
            qc = json.loads(cap["quick_check_json"])
            assert len(examples) >= 3
            assert len(qc) >= 2
            for item in qc:
                assert len(item["options"]) == 4
                assert 0 <= item["correct_index"] <= 3
    finally:
        conn.close()


def test_100_percent_variant_coverage_and_no_answer_leaks(isolated_db):
    summary = import_all_excel(generate_variants=True)
    assert summary["unique_questions"] == 163
    assert summary["total_variants_in_db"] >= 163

    conn = get_connection()
    try:
        # Every single one of the 163 unique questions must have >= 1 variant
        missing = conn.execute(
            """
            SELECT q.id, q.unit_code, q.mondai_type, q.focus_keyword
            FROM QUESTIONS q
            LEFT JOIN VARIANT_DRILLS v ON v.question_id = q.id
            WHERE v.id IS NULL
            """
        ).fetchall()
        assert missing == []

        # Verify all 10 問題2 ★ questions have star_4slot_shift variants with shifted ★
        star_q = conn.execute(
            "SELECT id FROM QUESTIONS WHERE section='grammar' AND mondai_type='問題2'"
        ).fetchall()
        assert len(star_q) == 10
        for row in star_q:
            vs = conn.execute(
                "SELECT * FROM VARIANT_DRILLS WHERE question_id=? AND variant_mode='star_4slot_shift'",
                (row["id"],),
            ).fetchall()
            assert len(vs) >= 1
            for v in vs:
                meta = json.loads(v["metadata_json"])
                assert meta["star_slot_index"] != 2
                assert sorted(meta["slots_order"]) == [0, 1, 2, 3]
                assert meta["slots_order"][meta["star_slot_index"]] == v["correct_index"]

        # Verify all 23 reading questions have dokkai_evidence and all 6 MU-12 have condition_shift
        read_q = conn.execute("SELECT id, unit_code FROM QUESTIONS WHERE section='reading'").fetchall()
        assert len(read_q) == 23
        for row in read_q:
            ev_v = conn.execute(
                "SELECT * FROM VARIANT_DRILLS WHERE question_id=? AND variant_mode='dokkai_evidence'",
                (row["id"],),
            ).fetchall()
            assert len(ev_v) == 1
            meta = json.loads(ev_v[0]["metadata_json"])
            assert len(meta["evidence_indices"]) >= 1
            if row["unit_code"] == "MU-12":
                cs_v = conn.execute(
                    "SELECT * FROM VARIANT_DRILLS WHERE question_id=? AND variant_mode='condition_shift'",
                    (row["id"],),
                ).fetchall()
                assert len(cs_v) >= 1

        # Verify all 14 問題5 questions have error_diagnosis variants
        u_q = conn.execute("SELECT id FROM QUESTIONS WHERE section='vocab' AND mondai_type='問題5'").fetchall()
        assert len(u_q) == 14
        for row in u_q:
            uv = conn.execute(
                "SELECT * FROM VARIANT_DRILLS WHERE question_id=? AND variant_mode='error_diagnosis'",
                (row["id"],),
            ).fetchall()
            assert len(uv) >= 1

        # ANTI-LEAK check on 問題1, 問題2, 問題4, and Tier-1 scaffolding of distractor_invert variants
        from n3_mastery.scaffolding import apply_scaffolding

        leaks = []
        v_rows = conn.execute(
            """
            SELECT v.id, v.prompt_jp, v.options_json, v.correct_index, q.section, q.mondai_type, q.focus_keyword
            FROM VARIANT_DRILLS v
            JOIN QUESTIONS q ON q.id = v.question_id
            WHERE v.variant_mode = 'distractor_invert'
            """
        ).fetchall()
        for vr in v_rows:
            opts = json.loads(vr["options_json"])
            ans = opts[vr["correct_index"]]
            clean_ans = re.sub(r"（[^）]{1,12}）", "", ans).strip()
            if vr["section"] == "vocab" and vr["mondai_type"] == "問題1":
                if ans in vr["prompt_jp"]:
                    leaks.append((vr["id"], "M1_hiragana_leak", ans, vr["prompt_jp"]))
                scaf = apply_scaffolding(vr["prompt_jp"], opts, stability=0.5, exam_mode=False, focus_keyword=vr["focus_keyword"])
                rts = re.findall(r'<ruby class="scaffold-ruby"[^>]*>([^<]+)<rt>([^<]+)</rt></ruby>', scaf["prompt_html"])
                for word, rt in rts:
                    if rt == ans or word in ans or ans in rt:
                        leaks.append((vr["id"], "M1_tier1_ruby_leak", ans, word, rt))
            elif vr["section"] == "vocab" and vr["mondai_type"] == "問題2":
                kanjis = re.findall(r"[\u4e00-\u9faf]+", ans)
                for k in kanjis:
                    if k in vr["prompt_jp"]:
                        leaks.append((vr["id"], "M2_kanji_leak", ans, vr["prompt_jp"]))
            elif vr["section"] == "vocab" and vr["mondai_type"] == "問題4":
                if clean_ans and clean_ans in vr["prompt_jp"]:
                    leaks.append((vr["id"], "M4_text_leak", ans, vr["prompt_jp"]))
        assert leaks == []

        # Verify 問題5 error_diagnosis choices never leak furigana only on the answer
        m5_rows = conn.execute(
            "SELECT options_json FROM VARIANT_DRILLS WHERE variant_mode='error_diagnosis'"
        ).fetchall()
        for m5r in m5_rows:
            opts = json.loads(m5r["options_json"])
            assert all("（" not in o for o in opts), f"Furigana giveaway in 問題5 options: {opts}"

        # Verify Q46 antonym variant correctly points to 始まったら
        q46_row = conn.execute(
            """
            SELECT v.options_json, v.correct_index
            FROM VARIANT_DRILLS v
            JOIN QUESTIONS q ON q.id = v.question_id
            WHERE q.focus_keyword LIKE '%済んだら%' AND v.prompt_jp LIKE '%TRÁI NGHĨA%'
            """
        ).fetchone()
        assert q46_row is not None
        assert json.loads(q46_row["options_json"])[q46_row["correct_index"]] == "始まったら"

        # Verify MU-12 fee question evidence includes 注意 discount sentence
        fee_q = conn.execute(
            """
            SELECT q.notebook_meta_json, p.evidence_sentences_json
            FROM QUESTIONS q JOIN PASSAGES p ON p.id=q.passage_id
            WHERE q.prompt_jp LIKE '%いくら払う%'
            """
        ).fetchone()
        fee_evs = json.loads(fee_q["notebook_meta_json"])["evidence_indices"]
        fee_sents = json.loads(fee_q["evidence_sentences_json"])
        assert any("4,500円" in fee_sents[i] or "注意" in fee_sents[i] for i in fee_evs)
    finally:
        conn.close()
