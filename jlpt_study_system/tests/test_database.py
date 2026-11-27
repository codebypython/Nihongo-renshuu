"""Unit tests for SQLite database schema and connection lifecycle."""

import sqlite3
from pathlib import Path
from jlpt_study_system.database import init_db, get_db, create_connection


def test_init_db_creates_all_tables(tmp_path):
    db_file = tmp_path / "schema_test.db"
    init_db(db_file)

    conn = create_connection(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = {row[0] for row in cursor.fetchall()}
    conn.close()

    expected_tables = {
        "cards",
        "fsrs_states",
        "review_logs",
        "drill_items",
        "drill_history",
        "error_notebook",
        "curriculum_blocks",
        "pomodoro_sessions",
    }
    assert expected_tables.issubset(tables)


def test_foreign_key_enforcement(tmp_path):
    db_file = tmp_path / "fk_test.db"
    init_db(db_file)

    with get_db(db_file) as conn:
        # Inserting fsrs_state with non-existent card_id should raise IntegrityError
        try:
            conn.execute(
                """
                INSERT INTO fsrs_states (card_id, stability, difficulty, reps, lapses, state)
                VALUES (99999, 2.0, 5.0, 0, 0, 'New')
                """
            )
            assert False, "Should have failed due to foreign key violation"
        except sqlite3.IntegrityError:
            pass


def test_transaction_rollback_on_exception(tmp_path):
    db_file = tmp_path / "rollback_test.db"
    init_db(db_file)

    try:
        with get_db(db_file) as conn:
            conn.execute(
                "INSERT INTO cards (category, front, back, created_at) VALUES ('grammar', 'test_f', 'test_b', '2026-11-22T00:00:00')"
            )
            raise RuntimeError("Simulated crash")
    except RuntimeError:
        pass

    with get_db(db_file) as conn:
        count = conn.execute("SELECT COUNT(*) AS c FROM cards WHERE front = 'test_f'").fetchone()["c"]
        assert count == 0
