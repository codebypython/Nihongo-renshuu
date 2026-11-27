"""Integration tests for FastAPI REST API endpoints."""

import os
import pytest
from fastapi.testclient import TestClient

from jlpt_study_system.api import app
from jlpt_study_system.database import init_db
from jlpt_study_system.importer import import_all


@pytest.fixture(scope="module")
def client(tmp_path_factory):
    """Create test client for API using an isolated test database."""
    test_dir = tmp_path_factory.mktemp("api_test")
    test_db = test_dir / "test_api.db"
    old_env = os.environ.get("JLPT_DB_PATH")
    os.environ["JLPT_DB_PATH"] = str(test_db)
    init_db(test_db)
    import_all(test_db)
    with TestClient(app) as c:
        yield c
    if old_env is not None:
        os.environ["JLPT_DB_PATH"] = old_env
    else:
        os.environ.pop("JLPT_DB_PATH", None)


def test_api_health(client):
    res = client.get("/api/health")
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "online"
    assert data["total_cards"] >= 80


def test_api_seed(client):
    res = client.post("/api/seed")
    assert res.status_code == 200
    data = res.json()
    assert "counts" in data
    assert data["counts"]["grammar_cards"] == 40


def test_api_cards_due_and_review(client):
    res = client.get("/api/cards/due?limit=10")
    assert res.status_code == 200
    cards = res.json()
    assert len(cards) > 0

    target_card = cards[0]
    review_res = client.post(
        "/api/cards/review",
        json={
            "card_id": target_card["card"]["id"],
            "rating": 3,
            "elapsed_seconds": 2.5,
        },
    )
    assert review_res.status_code == 200
    review_data = review_res.json()
    assert "card_with_state" in review_data
    assert review_data["card_with_state"]["fsrs"]["reps"] >= 1


def test_api_curriculum_day(client):
    res = client.get("/api/curriculum/day/1")
    assert res.status_code == 200
    data = res.json()
    assert data["day_number"] == 1
    assert len(data["blocks"]) == 3

    # Complete a block
    block_id = data["blocks"][0]["id"]
    complete_res = client.post(
        f"/api/curriculum/block/{block_id}/complete",
        json={"completed_minutes": 200, "is_completed": True},
    )
    assert complete_res.status_code == 200
    assert complete_res.json()["is_completed"] is True


def test_api_pomodoro(client):
    pomo_res = client.post(
        "/api/pomodoro/session",
        json={
            "day_number": 1,
            "block_index": 1,
            "task_label": "Grammar Tier 1 deep dive",
            "duration_minutes": 50,
            "status": "completed",
        },
    )
    assert pomo_res.status_code == 200
    assert pomo_res.json()["id"] is not None

    summary_res = client.get("/api/pomodoro/summary?day_number=1")
    assert summary_res.status_code == 200
    assert summary_res.json()["completed_sessions"] >= 1


def test_api_drills_choukai_and_submit(client):
    drills_res = client.get("/api/drills/choukai?count=5")
    assert drills_res.status_code == 200
    items = drills_res.json()
    assert len(items) == 5

    item = items[0]
    submit_res = client.post(
        "/api/drills/submit",
        json={
            "item_id": item["id"],
            "selected_index": item["correct_index"],
            "response_time_sec": 1.4,
        },
    )
    assert submit_res.status_code == 200
    assert submit_res.json()["is_correct"] is True


def test_api_drills_dokkai_and_mock(client):
    dokkai_res = client.get("/api/drills/dokkai?count=3")
    assert dokkai_res.status_code == 200
    assert len(dokkai_res.json()) == 3

    mock_res = client.get("/api/drills/mock?count_per_section=2")
    assert mock_res.status_code == 200
    assert mock_res.json()["total_items"] == 4


def test_api_error_notebook(client):
    errors_res = client.get("/api/error-notebook")
    assert errors_res.status_code == 200

    stats_res = client.get("/api/error-notebook/stats")
    assert stats_res.status_code == 200
    assert "total_errors_logged" in stats_res.json()


def test_api_readiness(client):
    readiness_res = client.get("/api/readiness")
    assert readiness_res.status_code == 200
    data = readiness_res.json()
    assert data["total_score"] >= 0.0
    assert data["gengo"]["max_score"] == 60.0
    assert data["reading"]["max_score"] == 60.0
    assert data["listening"]["max_score"] == 60.0
    assert data["pass_status"] in ("PASS", "AT_RISK", "FAIL")


def test_api_ui_page(client):
    ui_res = client.get("/")
    assert ui_res.status_code == 200
    assert "JLPT N3 SPRINT" in ui_res.text
