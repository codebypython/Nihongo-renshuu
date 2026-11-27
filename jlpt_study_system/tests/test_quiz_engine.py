"""Unit tests for interactive quiz engine and error notebook."""

from jlpt_study_system.models import DrillType
from jlpt_study_system.quiz_engine import (
    get_drill_items_by_type,
    submit_drill_answer,
    generate_mini_mock_quiz,
    get_drill_performance_summary,
)
from jlpt_study_system.error_notebook import (
    log_mistake,
    get_error_items,
    remediate_error_item,
    get_error_notebook_stats,
)


def test_drill_items_retrieval(temp_db):
    choukai = get_drill_items_by_type(DrillType.CHOUKAI_REFLEX, count=5, db_path=temp_db)
    assert len(choukai) == 5
    for itm in choukai:
        assert itm.drill_type == DrillType.CHOUKAI_REFLEX
        assert len(itm.options) >= 3
        assert 0 <= itm.correct_index < len(itm.options)

    dokkai = get_drill_items_by_type(DrillType.DOKKAI_DECODER, count=3, db_path=temp_db)
    assert len(dokkai) == 3
    for itm in dokkai:
        assert itm.drill_type == DrillType.DOKKAI_DECODER


def test_submit_correct_drill_answer(temp_db):
    items = get_drill_items_by_type(DrillType.CHOUKAI_REFLEX, count=1, db_path=temp_db)
    item = items[0]

    result = submit_drill_answer(
        drill_item_id=item.id,
        selected_index=item.correct_index,
        response_time_sec=1.8,
        db_path=temp_db,
    )

    assert result.is_correct is True
    assert result.logged_to_error_notebook is False


def test_submit_incorrect_drill_answer_logs_to_error_notebook(temp_db):
    items = get_drill_items_by_type(DrillType.CHOUKAI_REFLEX, count=1, db_path=temp_db)
    item = items[0]
    wrong_index = (item.correct_index + 1) % len(item.options)

    result = submit_drill_answer(
        drill_item_id=item.id,
        selected_index=wrong_index,
        response_time_sec=4.5,
        db_path=temp_db,
    )

    assert result.is_correct is False
    assert result.logged_to_error_notebook is True
    assert result.trap_analysis != ""

    errors = get_error_items(db_path=temp_db)
    assert any(e.item_id == item.id for e in errors)


def test_submit_correct_drill_answer_auto_remediates(temp_db):
    items = get_drill_items_by_type(DrillType.CHOUKAI_REFLEX, count=1, db_path=temp_db)
    item = items[0]
    wrong_index = (item.correct_index + 1) % len(item.options)

    # 1. Answer incorrectly
    submit_drill_answer(
        drill_item_id=item.id,
        selected_index=wrong_index,
        response_time_sec=4.0,
        db_path=temp_db,
    )
    active = get_error_items(db_path=temp_db, remediated=False)
    assert any(e.item_id == item.id for e in active)

    # 2. Answer correctly
    res_correct = submit_drill_answer(
        drill_item_id=item.id,
        selected_index=item.correct_index,
        response_time_sec=1.5,
        db_path=temp_db,
    )
    assert res_correct.is_correct is True

    # Error must now be remediated
    active_after = get_error_items(db_path=temp_db, remediated=False)
    assert not any(e.item_id == item.id for e in active_after)


def test_mini_mock_quiz_generation(temp_db):
    mock = generate_mini_mock_quiz(count_per_section=2, db_path=temp_db)
    assert mock["total_items"] == 4
    assert len(mock["items"]) == 4


def test_error_notebook_remediation(temp_db):
    mistake = log_mistake(
        item_type="grammar",
        prompt="わけではない vs わけがない",
        user_answer="わけがない",
        correct_answer="わけではない",
        trap_analysis="Tuyệt đối không thể vs Không hẳn là",
        db_path=temp_db,
    )

    assert mistake.id is not None
    assert mistake.remediated is False

    # Attempt remediation
    remediated = remediate_error_item(error_id=mistake.id, success=True, db_path=temp_db)
    assert remediated.remediated is True
    assert remediated.remediated_at is not None

    stats = get_error_notebook_stats(db_path=temp_db)
    assert stats["remediated_errors"] >= 1
