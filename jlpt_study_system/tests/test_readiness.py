"""Unit tests for sectional readiness and score projection engine."""

from jlpt_study_system.readiness import calculate_sectional_readiness
from jlpt_study_system.fsrs_scheduler import get_due_cards, process_card_review
from jlpt_study_system.models import Rating
from jlpt_study_system.quiz_engine import get_drill_items_by_type, submit_drill_answer, DrillType


def test_initial_readiness_report_structure(temp_db):
    report = calculate_sectional_readiness(db_path=temp_db)

    assert report.total_score >= 0.0
    assert report.total_score <= 180.0
    assert report.gengo.max_score == 60.0
    assert report.reading.max_score == 60.0
    assert report.listening.max_score == 60.0
    assert report.pass_status in ("PASS", "AT_RISK", "FAIL")
    assert len(report.critical_recommendations) > 0


def test_readiness_score_increases_with_practice(temp_db):
    report_before = calculate_sectional_readiness(db_path=temp_db)

    # 1. Review several cards with GOOD/EASY
    due = get_due_cards(db_path=temp_db, limit=10)
    for c in due:
        process_card_review(c.card.id, rating=Rating.GOOD, elapsed_seconds=2.0, db_path=temp_db)

    # 2. Answer Choukai drills with high speed
    choukai_items = get_drill_items_by_type(DrillType.CHOUKAI_REFLEX, count=5, db_path=temp_db)
    for itm in choukai_items:
        submit_drill_answer(itm.id, selected_index=itm.correct_index, response_time_sec=1.5, db_path=temp_db)

    # 3. Answer Dokkai drills
    dokkai_items = get_drill_items_by_type(DrillType.DOKKAI_DECODER, count=3, db_path=temp_db)
    for itm in dokkai_items:
        submit_drill_answer(itm.id, selected_index=itm.correct_index, response_time_sec=2.0, db_path=temp_db)

    report_after = calculate_sectional_readiness(db_path=temp_db)

    assert report_after.total_score > report_before.total_score
    assert report_after.listening.score > report_before.listening.score
    assert report_after.gengo.score > report_before.gengo.score


def test_cutoff_safeguards_detect_risk(temp_db):
    report = calculate_sectional_readiness(db_path=temp_db)
    # At baseline (zero reviews/zero drills), all 3 sections must accurately trigger cutoff alerts
    assert report.gengo.cutoff == 19.0
    assert report.reading.cutoff == 19.0
    assert report.listening.cutoff == 19.0
    assert report.gengo.pass_cutoff is False
    assert report.reading.pass_cutoff is False
    assert report.listening.pass_cutoff is False
    assert report.pass_status == "FAIL"
    assert len(report.at_risk_sections) == 3
    assert any("Language Knowledge" in r for r in report.at_risk_sections)
