"""Unit tests for curriculum tracker, Pomodoro block manager, and adaptive engine."""

from jlpt_study_system.curriculum import (
    get_curriculum_day,
    complete_curriculum_block,
    log_pomodoro_session,
    get_pomodoro_summary,
    get_sprint_overview,
    get_adaptive_schedule_advice,
)
from jlpt_study_system.error_notebook import log_mistake


def test_get_curriculum_day(temp_db):
    day1 = get_curriculum_day(1, db_path=temp_db)
    assert day1["day_number"] == 1
    assert len(day1["blocks"]) == 3  # morning, afternoon, evening
    assert day1["completion_rate_pct"] == 0.0


def test_complete_curriculum_block(temp_db):
    day1 = get_curriculum_day(1, db_path=temp_db)
    first_block = day1["blocks"][0]

    updated = complete_curriculum_block(
        block_id=first_block["id"],
        completed_minutes=240,
        notes="All morning drills completed ahead of time",
        is_completed=True,
        db_path=temp_db,
    )

    assert updated.is_completed is True
    assert updated.completed_minutes == 240
    assert updated.completed_at is not None

    refreshed_day1 = get_curriculum_day(1, db_path=temp_db)
    assert refreshed_day1["completed_blocks_count"] == 1
    assert refreshed_day1["completion_rate_pct"] > 30.0


def test_pomodoro_logging_and_summary(temp_db):
    session = log_pomodoro_session(
        day_number=1,
        block_index=1,
        task_label="Grammar Tier 1 deep dive",
        duration_minutes=50,
        status="completed",
        db_path=temp_db,
    )

    assert session.id is not None
    assert session.duration_minutes == 50

    summary = get_pomodoro_summary(day_number=1, db_path=temp_db)
    assert summary["completed_sessions"] == 1
    assert summary["total_study_minutes"] == 50


def test_sprint_overview(temp_db):
    overview = get_sprint_overview(db_path=temp_db)
    assert len(overview["days"]) == 7
    assert overview["total_blocks"] == 21


def test_adaptive_advice_triggers_on_unresolved_traps(temp_db):
    # Log 3 grammar errors
    for i in range(3):
        log_mistake(
            item_type="grammar",
            prompt=f"Test Grammar Trap {i}",
            user_answer="wrong",
            correct_answer="correct",
            trap_analysis=f"Trap explanation {i}",
            db_path=temp_db,
        )

    advice = get_adaptive_schedule_advice(current_day=2, db_path=temp_db)
    assert any("Ngữ pháp" in a for a in advice)
