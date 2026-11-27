"""Unit tests for FSRS spaced repetition scheduler."""

from datetime import datetime, timezone
import pytest

from jlpt_study_system.models import FSRSState, Rating, CardState, CardCategory
from jlpt_study_system.fsrs_scheduler import (
    calculate_next_fsrs_state,
    get_due_cards,
    process_card_review,
    get_card_stats,
)
from jlpt_study_system.error_notebook import get_error_items


def test_initial_review_good_rating():
    initial = FSRSState(
        card_id=1,
        stability=2.0,
        difficulty=5.0,
        reps=0,
        lapses=0,
        state=CardState.NEW,
    )

    next_state = calculate_next_fsrs_state(initial, Rating.GOOD)

    assert next_state.reps == 1
    assert next_state.lapses == 0
    assert next_state.state == CardState.REVIEW
    assert next_state.stability > 2.0
    assert next_state.scheduled_days >= 2
    assert next_state.due_date is not None


def test_initial_review_again_rating():
    initial = FSRSState(
        card_id=1,
        stability=2.0,
        difficulty=5.0,
        reps=0,
        lapses=0,
        state=CardState.NEW,
    )

    next_state = calculate_next_fsrs_state(initial, Rating.AGAIN)

    assert next_state.reps == 0
    assert next_state.lapses == 1
    assert next_state.state == CardState.LEARNING
    assert next_state.scheduled_days == 0
    assert next_state.due_date is not None


def test_subsequent_review_lapse():
    active = FSRSState(
        card_id=1,
        stability=4.0,
        difficulty=5.0,
        reps=3,
        lapses=0,
        state=CardState.REVIEW,
    )

    lapsed = calculate_next_fsrs_state(active, Rating.AGAIN)

    assert lapsed.state == CardState.RELEARNING
    assert lapsed.lapses == 1
    assert lapsed.stability < 4.0
    assert lapsed.difficulty > 5.0
    assert lapsed.scheduled_days == 0


def test_subsequent_review_easy_growth():
    active = FSRSState(
        card_id=1,
        stability=2.5,
        difficulty=4.5,
        reps=2,
        lapses=0,
        state=CardState.REVIEW,
    )

    easy_state = calculate_next_fsrs_state(active, Rating.EASY)

    assert easy_state.state == CardState.REVIEW
    assert easy_state.reps == 3
    assert easy_state.stability > 5.0
    assert easy_state.scheduled_days <= 7  # sprint boundary cap


def test_process_card_review_records_error_for_again(temp_db):
    due = get_due_cards(db_path=temp_db, limit=5)
    assert len(due) > 0
    test_card = due[0]

    updated, logged_error = process_card_review(
        card_id=test_card.card.id,
        rating=Rating.AGAIN,
        elapsed_seconds=4.2,
        db_path=temp_db,
    )

    assert updated.fsrs.state in (CardState.LEARNING, CardState.RELEARNING)
    assert updated.fsrs.lapses >= 1
    assert logged_error is True

    errors = get_error_items(db_path=temp_db, remediated=False)
    assert any(e.item_id == test_card.card.id for e in errors)


def test_process_card_review_auto_remediates_on_good(temp_db):
    due = get_due_cards(db_path=temp_db, limit=1)
    test_card = due[0]

    # 1. Fail review -> creates error
    process_card_review(
        card_id=test_card.card.id,
        rating=Rating.AGAIN,
        elapsed_seconds=3.0,
        db_path=temp_db,
    )
    active_errors = get_error_items(db_path=temp_db, remediated=False)
    assert any(e.item_id == test_card.card.id for e in active_errors)

    # 2. Pass review with GOOD -> auto remediates error
    process_card_review(
        card_id=test_card.card.id,
        rating=Rating.GOOD,
        elapsed_seconds=2.0,
        db_path=temp_db,
    )
    active_errors_after = get_error_items(db_path=temp_db, remediated=False)
    assert not any(e.item_id == test_card.card.id for e in active_errors_after)

    remediated_errors = get_error_items(db_path=temp_db, remediated=True)
    assert any(e.item_id == test_card.card.id for e in remediated_errors)


def test_category_string_filter_in_get_due_cards(temp_db):
    # Verify string parameter works safely without crashing
    grammar_due = get_due_cards(db_path=temp_db, category="grammar")
    assert len(grammar_due) > 0
    assert all(c.card.category == CardCategory.GRAMMAR for c in grammar_due)

    vocab_due = get_due_cards(db_path=temp_db, category="vocab")
    assert len(vocab_due) > 0
    assert all(c.card.category == CardCategory.VOCAB for c in vocab_due)


def test_deck_stats_aggregation(temp_db):
    stats = get_card_stats(db_path=temp_db)
    assert stats["total_cards"] >= 80  # 40 grammar + 40 vocab
    assert stats["states"]["New"] >= 0
    assert "categories" in stats
    assert "retention_rate_pct" in stats
