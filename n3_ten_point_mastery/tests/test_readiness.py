"""Tests for Dual 10-Point Calibration and Zero-Sycophancy Mastery Gate."""

import json
from datetime import timedelta

from n3_mastery.database import get_connection
from n3_mastery.drill_engine import get_study_item, submit_answer
from n3_mastery.fsrs_adaptive import utc_now
from n3_mastery.importer import import_all_excel
from n3_mastery.models import ScoringMode
from n3_mastery.readiness import calculate_dual_readiness


def _answer_item_correctly(q_id: int, variant_id=None, seed="rseed", used_hint=False, now=None):
    mode = "variant" if variant_id is not None else "original"
    item = get_study_item(q_id, mode=mode, variant_id=variant_id, session_seed=seed)
    conn = get_connection()
    try:
        if variant_id is not None:
            row = conn.execute("SELECT options_json, correct_index, metadata_json FROM VARIANT_DRILLS WHERE id=?", (variant_id,)).fetchone()
            meta = json.loads(row["metadata_json"] or "{}")
        else:
            row = conn.execute("SELECT options_json, correct_index, notebook_meta_json FROM QUESTIONS WHERE id=?", (q_id,)).fetchone()
            meta = json.loads(row["notebook_meta_json"] or "{}")
    finally:
        conn.close()

    if item["interaction_type"] == "star_4slot":
        sa = meta if variant_id is not None else meta["star_assembly"]
        return submit_answer(
            q_id,
            mode=mode,
            variant_id=variant_id,
            slot_order=sa["slots_order"],
            used_hint=used_hint,
            session_seed=seed,
            now=now,
        )

    orig_opts = json.loads(row["options_json"])
    correct_text = orig_opts[int(row["correct_index"])]
    disp_idx = item["options"].index(correct_text)
    ev = meta.get("evidence_indices", [0]) if item["interaction_type"] == "dokkai_evidence" else None
    return submit_answer(
        q_id,
        mode=mode,
        variant_id=variant_id,
        selected_index=disp_idx,
        evidence_indices=ev,
        used_hint=used_hint,
        session_seed=seed,
        now=now,
    )


def test_initial_scores_strictly_zero(isolated_db):
    import_all_excel(generate_variants=True)
    rep = calculate_dual_readiness()
    assert rep.original_score_10 == 0.0
    assert rep.mastery_score_10 == 0.0
    assert rep.mastered_count == 0
    assert rep.attempted_count == 0
    assert "0.00/10.00" in rep.honest_verdict


def test_passing_only_original_exposes_rote_gap(isolated_db):
    import_all_excel(generate_variants=True)
    conn = get_connection()
    q_ids = [r[0] for r in conn.execute("SELECT id FROM QUESTIONS ORDER BY id").fetchall()]
    conn.close()

    t0 = utc_now()
    for q_id in q_ids:
        _answer_item_correctly(q_id, variant_id=None, seed="rote_test", used_hint=False, now=t0)

    rep = calculate_dual_readiness(now=t0)
    assert rep.original_score_10 == 10.0
    # Capped strictly at 4.50/10.00 because NO anti-rote variants and NO 2 spaced sessions were passed!
    assert rep.mastery_score_10 == 4.5
    assert rep.mastered_count == 0
    assert rep.rote_gap_10 == 5.5
    assert "[WARN]" in rep.honest_verdict


def test_mastery_gate_requires_clean_original_plus_variant_plus_two_spaced_sessions(isolated_db):
    import_all_excel(generate_variants=True)
    conn = get_connection()
    q_rows = conn.execute(
        """
        SELECT q.id, (SELECT v.id FROM VARIANT_DRILLS v WHERE v.question_id=q.id ORDER BY v.id LIMIT 1) AS vid
        FROM QUESTIONS q ORDER BY q.id
        """
    ).fetchall()
    conn.close()

    t0 = utc_now()
    # Pass BOTH original and variant at t0 (same minute = only 1 spaced session!)
    for r in q_rows[:10]:
        _answer_item_correctly(r["id"], variant_id=None, seed="s1", now=t0)
        _answer_item_correctly(r["id"], variant_id=r["vid"], seed="s1", now=t0)

    rep_same_session = calculate_dual_readiness(now=t0)
    assert rep_same_session.mastered_count == 0  # Still 0 because only 1 session so far!

    # Now review again 2 hours later (2nd spaced session)
    t1 = t0 + timedelta(hours=2)
    for r in q_rows[:10]:
        _answer_item_correctly(r["id"], variant_id=r["vid"], seed="s2", now=t1)

    rep_spaced = calculate_dual_readiness(now=t1)
    assert rep_spaced.mastered_count == 10
    assert rep_spaced.mastery_score_10 > 0.0

    # Check retrievability decay after 30 days without review lowers scores honestly
    t_late = t1 + timedelta(days=30)
    rep_decayed = calculate_dual_readiness(now=t_late)
    assert rep_decayed.original_score_10 < rep_spaced.original_score_10
    assert rep_decayed.mastery_score_10 < rep_spaced.mastery_score_10


def test_equal_weighted_vs_jlpt_weighted_scoring_modes(isolated_db):
    import_all_excel(generate_variants=True)
    conn = get_connection()
    grammar_q = conn.execute("SELECT id FROM QUESTIONS WHERE section='grammar' ORDER BY id").fetchall()
    conn.close()

    t0 = utc_now()
    for r in grammar_q:
        _answer_item_correctly(r["id"], variant_id=None, seed="g", now=t0)

    rep_jlpt = calculate_dual_readiness(scoring_mode=ScoringMode.JLPT_WEIGHTED, now=t0)
    rep_equal = calculate_dual_readiness(scoring_mode=ScoringMode.EQUAL_WEIGHTED, now=t0)
    # In JLPT weighted mode, grammar is 4.0/10.0; in equal weighted, 42/163 * 10 = 2.58/10.0
    assert rep_jlpt.original_score_10 == 4.0
    assert rep_equal.original_score_10 == round(42 / 163 * 10.0, 2)


def test_relearning_card_gets_zero_partial_mastery_credit(isolated_db):
    import_all_excel(generate_variants=True)
    conn = get_connection()
    row = conn.execute(
        """
        SELECT q.id, (SELECT v.id FROM VARIANT_DRILLS v WHERE v.question_id=q.id ORDER BY v.id LIMIT 1) AS vid
        FROM QUESTIONS q WHERE q.section='grammar' LIMIT 1
        """
    ).fetchone()
    conn.close()

    t0 = utc_now()
    # Pass variant cleanly
    _answer_item_correctly(row["id"], variant_id=row["vid"], seed="r1", now=t0)
    rep_before = calculate_dual_readiness(now=t0)
    assert rep_before.mastery_score_10 > 0.0

    # Now fail original -> card enters relearning; Zero-Sycophancy must revoke partial mastery credit
    item = get_study_item(row["id"], mode="original", session_seed="failseed")
    conn2 = get_connection()
    q_row = conn2.execute("SELECT options_json, correct_index, notebook_meta_json FROM QUESTIONS WHERE id=?", (row["id"],)).fetchone()
    conn2.close()
    if item["interaction_type"] == "star_4slot":
        sa = json.loads(q_row["notebook_meta_json"])["star_assembly"]
        wrong_slots = sa["slots_order"].copy()
        wrong_slots[0], wrong_slots[1] = wrong_slots[1], wrong_slots[0]
        submit_answer(row["id"], mode="original", slot_order=wrong_slots, session_seed="failseed", now=t0)
    else:
        corr_txt = json.loads(q_row["options_json"])[int(q_row["correct_index"])]
        wrong_idx = (item["options"].index(corr_txt) + 1) % 4
        submit_answer(row["id"], mode="original", selected_index=wrong_idx, session_seed="failseed", now=t0)

    rep_after = calculate_dual_readiness(now=t0)
    assert rep_after.original_score_10 == 0.0
    assert rep_after.mastery_score_10 == 0.0
