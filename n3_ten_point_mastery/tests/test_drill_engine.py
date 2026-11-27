"""Tests for 4 anti-rote modes: OptionPermuter, DistractorInverter, 4-Slot Star Assembly, Evidence-First Dokkai."""

import json
import pytest

from n3_mastery.database import get_connection
from n3_mastery.drill_engine import (
    get_error_notebook,
    get_study_item,
    permute_options,
    submit_answer,
)
from n3_mastery.importer import import_all_excel


def test_option_permuter_shuffles_and_updates_correct_index():
    opts = ["optA", "optB", "optC", "optD"]
    seen_correct_positions = set()
    for i in range(1, 20):
        p_opts, new_idx, idx_map = permute_options(opts, 1, session_seed=f"session-{i}", item_key="q10")
        assert sorted(p_opts) == sorted(opts)
        assert p_opts[new_idx] == "optB"
        assert idx_map[new_idx] == 1
        seen_correct_positions.add(new_idx)
    assert len(seen_correct_positions) == 4


def test_full_4slot_star_assembly_rejects_incomplete_and_verifies_shifted_star(isolated_db):
    import_all_excel(generate_variants=True)
    conn = get_connection()
    q = conn.execute(
        "SELECT id, notebook_meta_json FROM QUESTIONS WHERE section='grammar' AND mondai_type='問題2' LIMIT 1"
    ).fetchone()
    v = conn.execute(
        "SELECT id, metadata_json FROM VARIANT_DRILLS WHERE question_id=? AND variant_mode='star_4slot_shift' LIMIT 1",
        (q["id"],),
    ).fetchone()
    conn.close()

    sa = json.loads(q["notebook_meta_json"])["star_assembly"]
    expected_slots = sa["slots_order"]

    # Incomplete 1-slot or 3-slot guess MUST raise ValueError
    with pytest.raises(ValueError, match="4 mảnh"):
        submit_answer(q["id"], mode="original", slot_order=[expected_slots[2]])
    with pytest.raises(ValueError, match="4 mảnh"):
        submit_answer(q["id"], mode="original", slot_order=expected_slots[:3])
    # Duplicate chunk in slots MUST raise ValueError
    with pytest.raises(ValueError, match="lặp mảnh"):
        submit_answer(q["id"], mode="original", slot_order=[0, 0, 1, 2])

    # Wrong permutation with ★ coincidentally right MUST still fail
    wrong_slots = expected_slots.copy()
    wrong_slots[0], wrong_slots[1] = wrong_slots[1], wrong_slots[0]
    res_wrong = submit_answer(q["id"], mode="original", slot_order=wrong_slots)
    assert res_wrong["is_correct"] is False

    # Correct full 4-slot assembly passes
    res_ok = submit_answer(q["id"], mode="original", slot_order=expected_slots)
    assert res_ok["is_correct"] is True
    assert res_ok["remediated"] is True

    # Shifted ★ variant tests new star_slot_index != 2
    item_v = get_study_item(q["id"], mode="variant", variant_id=v["id"], session_seed="seedX")
    assert item_v["interaction_type"] == "star_4slot"
    assert item_v["star_assembly"]["star_slot_index"] != 2
    v_meta = json.loads(v["metadata_json"])
    res_v = submit_answer(q["id"], mode="variant", variant_id=v["id"], slot_order=v_meta["slots_order"])
    assert res_v["is_correct"] is True


def test_dokkai_evidence_first_requires_both_evidence_and_answer(isolated_db):
    import_all_excel(generate_variants=True)
    conn = get_connection()
    q = conn.execute(
        "SELECT id, correct_index, notebook_meta_json FROM QUESTIONS WHERE section='reading' LIMIT 1"
    ).fetchone()
    v = conn.execute(
        "SELECT id, metadata_json, correct_index FROM VARIANT_DRILLS WHERE question_id=? AND variant_mode='dokkai_evidence'",
        (q["id"],),
    ).fetchone()
    conn.close()

    item = get_study_item(q["id"], mode="variant", variant_id=v["id"], session_seed="dokkai_seed")
    assert item["interaction_type"] == "dokkai_evidence"
    assert item["passage"] is not None
    assert len(item["passage"]["sentences"]) >= 2

    # Compute display index of correct answer
    v_opts = item["options"]
    conn2 = get_connection()
    try:
        orig_opts = json.loads(
            conn2.execute("SELECT options_json FROM VARIANT_DRILLS WHERE id=?", (v["id"],)).fetchone()[0]
        )
    finally:
        conn2.close()
    correct_text = orig_opts[int(v["correct_index"])]
    display_correct_idx = v_opts.index(correct_text)

    gold_ev = json.loads(v["metadata_json"])["evidence_indices"]
    wrong_ev = [i for i in range(len(item["passage"]["sentences"])) if i not in gold_ev]

    # Missing evidence_indices MUST raise ValueError
    with pytest.raises(ValueError, match="Evidence-First"):
        submit_answer(q["id"], mode="variant", variant_id=v["id"], selected_index=display_correct_idx, evidence_indices=[])

    # Correct option BUT wrong evidence sentence MUST fail dual check!
    if wrong_ev:
        res_bad_ev = submit_answer(
            q["id"],
            mode="variant",
            variant_id=v["id"],
            selected_index=display_correct_idx,
            evidence_indices=[wrong_ev[0]],
            session_seed="dokkai_seed",
        )
        assert res_bad_ev["answer_correct"] is True
        assert res_bad_ev["evidence_correct"] is False
        assert res_bad_ev["is_correct"] is False

    # Both evidence and option correct -> PASS!
    res_good = submit_answer(
        q["id"],
        mode="variant",
        variant_id=v["id"],
        selected_index=display_correct_idx,
        evidence_indices=[gold_ev[0]],
        session_seed="dokkai_seed",
    )
    assert res_good["evidence_correct"] is True
    assert res_good["answer_correct"] is True
    assert res_good["is_correct"] is True


def test_distractor_invert_and_error_notebook_remediation(isolated_db):
    import_all_excel(generate_variants=True)
    conn = get_connection()
    q = conn.execute(
        "SELECT id, options_json, correct_index FROM QUESTIONS WHERE section='vocab' AND mondai_type='問題1' LIMIT 1"
    ).fetchone()
    v = conn.execute(
        "SELECT id, options_json, correct_index FROM VARIANT_DRILLS WHERE question_id=? AND variant_mode='distractor_invert' LIMIT 1",
        (q["id"],),
    ).fetchone()
    conn.close()

    item = get_study_item(q["id"], mode="variant", variant_id=v["id"], session_seed="inv_seed")
    v_opts = json.loads(v["options_json"])
    correct_text = v_opts[int(v["correct_index"])]
    disp_correct = item["options"].index(correct_text)
    disp_wrong = (disp_correct + 1) % 4

    # Wrong answer logs into Error Notebook
    res_err = submit_answer(
        q["id"], mode="variant", variant_id=v["id"], selected_index=disp_wrong, session_seed="inv_seed"
    )
    assert res_err["is_correct"] is False
    errors = get_error_notebook()
    assert any(e["question_id"] == q["id"] for e in errors)

    # Remediate with correct answer clears Error Notebook
    res_fix = submit_answer(
        q["id"], mode="variant", variant_id=v["id"], selected_index=disp_correct, session_seed="inv_seed"
    )
    assert res_fix["is_correct"] is True
    assert res_fix["remediated"] is True
    errors_after = get_error_notebook()
    assert not any(e["question_id"] == q["id"] for e in errors_after)


def test_variant_mode_rotates_through_multiple_variants_in_mu12(isolated_db):
    from n3_mastery.drill_engine import get_next_study_candidate

    import_all_excel(generate_variants=True)
    seen_modes = set()
    for step in range(12):
        item = get_next_study_candidate(unit_code="MU-12", mode="variant", session_seed=f"rot-{step}")
        assert item is not None
        seen_modes.add(item["variant_mode"])
        conn = get_connection()
        vrow = conn.execute(
            "SELECT options_json, correct_index, metadata_json FROM VARIANT_DRILLS WHERE id=?",
            (item["variant_id"],),
        ).fetchone()
        conn.close()
        corr_txt = json.loads(vrow["options_json"])[int(vrow["correct_index"])]
        disp_idx = item["options"].index(corr_txt)
        ev = json.loads(vrow["metadata_json"]).get("evidence_indices") if item["interaction_type"] == "dokkai_evidence" else None
        submit_answer(
            item["question_id"],
            mode="variant",
            variant_id=item["variant_id"],
            selected_index=disp_idx,
            evidence_indices=ev,
            session_seed=f"rot-{step}",
        )
    assert seen_modes == {"dokkai_evidence", "condition_shift"}
