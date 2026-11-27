"""Tests for database initialization, WAL mode, FK constraints, and DB isolation."""

import sqlite3
import pytest

from n3_mastery.config import get_db_path
from n3_mastery.database import get_connection, init_db, transaction


def test_db_path_isolation(isolated_db):
    assert get_db_path() == isolated_db
    assert isolated_db.exists()


def test_wal_mode_and_foreign_keys_enabled(isolated_db):
    conn = get_connection()
    try:
        journal = conn.execute("PRAGMA journal_mode;").fetchone()[0]
        fk = conn.execute("PRAGMA foreign_keys;").fetchone()[0]
        assert str(journal).lower() == "wal"
        assert fk == 1
    finally:
        conn.close()


def test_schema_tables_created(isolated_db):
    expected_tables = {
        "SOURCE_WORKBOOKS",
        "MICRO_UNITS",
        "N4_BRIDGE_CAPSULES",
        "PASSAGES",
        "QUESTIONS",
        "QUESTION_SOURCES",
        "VARIANT_DRILLS",
        "FSRS_STATES",
        "MOCK_EXAMS",
        "ATTEMPT_LOGS",
        "USER_SETTINGS",
    }
    conn = get_connection()
    try:
        rows = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';"
        ).fetchall()
        found = {r[0] for r in rows}
        assert expected_tables.issubset(found)
    finally:
        conn.close()


def test_foreign_key_enforcement_and_cascade(isolated_db):
    with transaction() as conn:
        with pytest.raises(sqlite3.IntegrityError):
            conn.execute(
                """
                INSERT INTO QUESTIONS
                (content_hash, workbook_id, unit_code, section, mondai_type, source_label, prompt_jp, options_json, correct_index)
                VALUES ('h1', 999, 'MU-01', 'vocab', '問題1', 'Q1', 'P', '["a","b","c","d"]', 0)
                """
            )

    with transaction() as conn:
        conn.execute(
            "INSERT INTO MICRO_UNITS (code, order_index, title, section, target_skill) VALUES ('MU-01', 1, 'Unit 1', 'vocab', 'Reading')"
        )
        conn.execute(
            "INSERT INTO SOURCE_WORKBOOKS (filename, file_hash, layout_type, raw_count, imported_count) VALUES ('f.xlsx', 'fh1', 'vocab_35', 1, 1)"
        )
        wb_id = conn.execute("SELECT id FROM SOURCE_WORKBOOKS WHERE file_hash='fh1'").fetchone()[0]
        conn.execute(
            """
            INSERT INTO QUESTIONS
            (content_hash, workbook_id, unit_code, section, mondai_type, source_label, prompt_jp, options_json, correct_index)
            VALUES ('qh1', ?, 'MU-01', 'vocab', '問題1', 'Q1', 'テスト', '["a","b","c","d"]', 1)
            """,
            (wb_id,),
        )
        q_id = conn.execute("SELECT id FROM QUESTIONS WHERE content_hash='qh1'").fetchone()[0]
        conn.execute("INSERT INTO FSRS_STATES (question_id) VALUES (?)", (q_id,))
        conn.execute("DELETE FROM QUESTIONS WHERE id=?", (q_id,))
        left = conn.execute("SELECT COUNT(*) FROM FSRS_STATES WHERE question_id=?", (q_id,)).fetchone()[0]
        assert left == 0


def test_init_db_idempotent(isolated_db):
    init_db()
    conn = get_connection()
    try:
        val = conn.execute("SELECT value FROM USER_SETTINGS WHERE key='days_remaining'").fetchone()[0]
        assert val == "14"
    finally:
        conn.close()
