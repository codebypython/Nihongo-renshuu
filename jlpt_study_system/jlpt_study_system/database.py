"""Database layer for JLPT N3 Study System."""

import os
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Generator, Optional
from jlpt_study_system.config import DEFAULT_DB_PATH


SCHEMA_SQL = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    front TEXT NOT NULL,
    back TEXT NOT NULL,
    trap TEXT DEFAULT '',
    example TEXT DEFAULT '',
    tags TEXT DEFAULT '',
    created_at TEXT NOT NULL,
    UNIQUE(category, front)
);

CREATE TABLE IF NOT EXISTS fsrs_states (
    card_id INTEGER PRIMARY KEY REFERENCES cards(id) ON DELETE CASCADE,
    stability REAL NOT NULL DEFAULT 2.0,
    difficulty REAL NOT NULL DEFAULT 5.0,
    reps INTEGER NOT NULL DEFAULT 0,
    lapses INTEGER NOT NULL DEFAULT 0,
    state TEXT NOT NULL DEFAULT 'New',
    last_review TEXT,
    due_date TEXT,
    scheduled_days INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS review_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    card_id INTEGER NOT NULL REFERENCES cards(id) ON DELETE CASCADE,
    rating INTEGER NOT NULL,
    review_time TEXT NOT NULL,
    elapsed_seconds REAL NOT NULL DEFAULT 0.0,
    scheduled_days INTEGER NOT NULL DEFAULT 0,
    stability_after REAL NOT NULL DEFAULT 2.0,
    difficulty_after REAL NOT NULL DEFAULT 5.0
);

CREATE TABLE IF NOT EXISTS drill_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    drill_type TEXT NOT NULL,
    section TEXT NOT NULL,
    prompt TEXT NOT NULL,
    context TEXT DEFAULT '',
    options_json TEXT NOT NULL,
    correct_index INTEGER NOT NULL,
    trap_analysis TEXT DEFAULT '',
    UNIQUE(drill_type, prompt)
);

CREATE TABLE IF NOT EXISTS drill_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    drill_item_id INTEGER NOT NULL REFERENCES drill_items(id) ON DELETE CASCADE,
    selected_index INTEGER NOT NULL,
    is_correct INTEGER NOT NULL,
    response_time_sec REAL NOT NULL DEFAULT 0.0,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS error_notebook (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_type TEXT NOT NULL,
    item_id INTEGER,
    prompt TEXT NOT NULL,
    user_answer TEXT NOT NULL,
    correct_answer TEXT NOT NULL,
    trap_analysis TEXT NOT NULL,
    remediated INTEGER NOT NULL DEFAULT 0,
    attempt_count INTEGER NOT NULL DEFAULT 1,
    created_at TEXT NOT NULL,
    remediated_at TEXT
);

CREATE TABLE IF NOT EXISTS curriculum_blocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    day_number INTEGER NOT NULL,
    block_name TEXT NOT NULL,
    title TEXT NOT NULL,
    planned_minutes INTEGER NOT NULL DEFAULT 50,
    completed_minutes INTEGER NOT NULL DEFAULT 0,
    is_completed INTEGER NOT NULL DEFAULT 0,
    notes TEXT DEFAULT '',
    completed_at TEXT,
    UNIQUE(day_number, block_name, title)
);

CREATE TABLE IF NOT EXISTS pomodoro_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    day_number INTEGER NOT NULL,
    block_index INTEGER NOT NULL DEFAULT 1,
    task_label TEXT NOT NULL,
    duration_minutes INTEGER NOT NULL DEFAULT 50,
    status TEXT NOT NULL DEFAULT 'completed',
    created_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_cards_category ON cards(category);
CREATE INDEX IF NOT EXISTS idx_fsrs_due_date ON fsrs_states(due_date);
CREATE INDEX IF NOT EXISTS idx_error_notebook_remediated ON error_notebook(remediated);
CREATE INDEX IF NOT EXISTS idx_curriculum_day ON curriculum_blocks(day_number);
"""


def get_db_path(db_path: Optional[Path] = None) -> Path:
    """Resolve database path and ensure parent directories exist."""
    if db_path:
        resolved = Path(db_path)
    else:
        env_path = os.environ.get("JLPT_DB_PATH")
        resolved = Path(env_path) if env_path else DEFAULT_DB_PATH
    if str(resolved) != ":memory:":
        resolved.parent.mkdir(parents=True, exist_ok=True)
    return resolved


def create_connection(db_path: Optional[Path] = None) -> sqlite3.Connection:
    """Create a configured SQLite connection."""
    target_path = get_db_path(db_path)
    conn = sqlite3.connect(str(target_path), timeout=30.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    # Try enabling WAL mode; in-memory (:memory:) doesn't support WAL so ignore if fails
    if str(target_path) != ":memory:":
        try:
            conn.execute("PRAGMA journal_mode = WAL;")
        except sqlite3.OperationalError:
            pass
    return conn


@contextmanager
def get_db(db_path: Optional[Path] = None) -> Generator[sqlite3.Connection, None, None]:
    """Context manager for SQLite database connection with automatic commit/rollback."""
    conn = create_connection(db_path)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_db(db_path: Optional[Path] = None) -> None:
    """Initialize database schema idempotently."""
    with get_db(db_path) as conn:
        conn.executescript(SCHEMA_SQL)
