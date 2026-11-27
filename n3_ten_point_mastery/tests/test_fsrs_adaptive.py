"""Tests for Adaptive Pace FSRS scheduler, Horizon Scaling, Hint cap, and capacity warning."""

from datetime import timedelta

from n3_mastery.database import get_connection
from n3_mastery.fsrs_adaptive import (
    apply_fsrs_update,
    compute_horizon_interval,
    compute_pace_feasibility,
    update_pace_settings,
    utc_now,
)
from n3_mastery.importer import import_all_excel


def test_horizon_scaling_formula():
    # With 4 days remaining, horizon cap = max(0.25, 0.45 * 4) = 1.80 days
    assert compute_horizon_interval(10.0, days_remaining=4) == 1.8
    # With 1 day remaining, horizon cap = max(0.25, 0.45) = 0.45 days
    assert compute_horizon_interval(5.0, days_remaining=1) == 0.45


def test_capacity_warning_when_daily_minutes_insufficient(isolated_db):
    import_all_excel(generate_variants=True)
    # 5 days * 30 min = 150 min budget << ~680 min workload -> MUST emit warning
    feas = compute_pace_feasibility(days_remaining=5, daily_minutes=30)
    assert feas.is_feasible is False
    assert feas.warning_message is not None
    assert "[WARN]" in feas.warning_message
    assert feas.shortfall_minutes_per_day > 0

    # 30 days * 60 min = 1800 min budget >> ~680 min workload -> feasible
    ok_feas = compute_pace_feasibility(days_remaining=30, daily_minutes=60)
    assert ok_feas.is_feasible is True
    assert ok_feas.warning_message is None


def test_hint_downgrades_easy_to_hard_and_again_triggers_relearning(isolated_db):
    import_all_excel(generate_variants=False)
    conn = get_connection()
    q_id = conn.execute("SELECT id FROM QUESTIONS LIMIT 1").fetchone()[0]
    conn.close()

    t0 = utc_now()
    # Passing EASY with hint MUST cap effective rating to HARD (2) and NOT advance spaced_clean_sessions
    res_hint = apply_fsrs_update(q_id, rating=4, used_hint=True, now=t0, days_remaining=14, daily_minutes=60)
    assert res_hint["effective_rating"] == 2
    assert res_hint["downgraded_by_hint"] is True
    assert res_hint["spaced_clean_sessions"] == 0

    # Clean pass 2 hours later advances spaced_clean_sessions -> 1
    t1 = t0 + timedelta(hours=2)
    res_clean1 = apply_fsrs_update(q_id, rating=3, used_hint=False, now=t1, days_remaining=14, daily_minutes=60)
    assert res_clean1["spaced_clean_sessions"] == 1
    assert res_clean1["effective_interval_days"] <= 0.45 * 14

    # Clean pass 2 days later advances spaced_clean_sessions -> 2
    t2 = t1 + timedelta(days=2)
    res_clean2 = apply_fsrs_update(q_id, rating=4, used_hint=False, now=t2, days_remaining=4, daily_minutes=60)
    assert res_clean2["spaced_clean_sessions"] == 2
    # Horizon compression with 4 days remaining caps interval at 1.8 days
    assert res_clean2["effective_interval_days"] <= 1.8

    # Rating AGAIN pushes card to same-day relearning and resets clean streak
    t3 = t2 + timedelta(hours=3)
    res_again = apply_fsrs_update(q_id, rating=1, used_hint=False, now=t3, days_remaining=4, daily_minutes=60)
    assert res_again["state"] == "relearning"
    assert res_again["lapses"] == 1
    assert res_again["spaced_clean_sessions"] == 0
    assert res_again["effective_interval_days"] < 0.05


def test_pace_settings_persistence(isolated_db):
    updated = update_pace_settings(days_remaining=10, daily_minutes=75, scoring_mode="equal_weighted")
    assert updated.days_remaining == 10
    assert updated.daily_minutes == 75
    assert updated.scoring_mode.value == "equal_weighted"
