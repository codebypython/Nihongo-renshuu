"""SQLite WAL database management and schema initialization."""

import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator, Optional

from n3_mastery.config import (
    DEFAULT_DAILY_MINUTES,
    DEFAULT_DAYS_REMAINING,
    DEFAULT_DIFFICULTY,
    DEFAULT_SCORING_MODE,
    DEFAULT_STABILITY,
    get_db_path,
)

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS SOURCE_WORKBOOKS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT NOT NULL,
    file_hash TEXT NOT NULL UNIQUE,
    layout_type TEXT NOT NULL,
    raw_count INTEGER NOT NULL DEFAULT 0,
    imported_count INTEGER NOT NULL DEFAULT 0,
    imported_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS MICRO_UNITS (
    code TEXT PRIMARY KEY,
    order_index INTEGER NOT NULL UNIQUE,
    title TEXT NOT NULL,
    section TEXT NOT NULL CHECK(section IN ('vocab', 'grammar', 'reading')),
    target_skill TEXT NOT NULL,
    estimated_minutes INTEGER NOT NULL DEFAULT 30
);

CREATE TABLE IF NOT EXISTS N4_BRIDGE_CAPSULES (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    unit_code TEXT NOT NULL UNIQUE REFERENCES MICRO_UNITS(code) ON DELETE CASCADE,
    grammar_focus TEXT NOT NULL,
    explanation_vi TEXT NOT NULL,
    examples_json TEXT NOT NULL DEFAULT '[]',
    quick_check_json TEXT NOT NULL DEFAULT '[]',
    completed INTEGER NOT NULL DEFAULT 0 CHECK(completed IN (0, 1))
);

CREATE TABLE IF NOT EXISTS PASSAGES (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content_hash TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL,
    genre TEXT NOT NULL,
    section TEXT NOT NULL DEFAULT 'reading' CHECK(section IN ('grammar', 'reading')),
    japanese_text TEXT NOT NULL,
    vietnamese_text TEXT NOT NULL DEFAULT '',
    evidence_sentences_json TEXT NOT NULL DEFAULT '[]',
    condition_matrix_json TEXT NOT NULL DEFAULT '[]'
);

CREATE TABLE IF NOT EXISTS QUESTIONS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content_hash TEXT NOT NULL UNIQUE,
    workbook_id INTEGER NOT NULL REFERENCES SOURCE_WORKBOOKS(id) ON DELETE CASCADE,
    unit_code TEXT NOT NULL REFERENCES MICRO_UNITS(code) ON DELETE RESTRICT,
    passage_id INTEGER REFERENCES PASSAGES(id) ON DELETE SET NULL,
    section TEXT NOT NULL CHECK(section IN ('vocab', 'grammar', 'reading')),
    mondai_type TEXT NOT NULL,
    source_label TEXT NOT NULL,
    focus_keyword TEXT NOT NULL DEFAULT '',
    prompt_jp TEXT NOT NULL,
    options_json TEXT NOT NULL,
    correct_index INTEGER NOT NULL CHECK(correct_index BETWEEN 0 AND 3),
    translation_vi TEXT NOT NULL DEFAULT '',
    explanation_vi TEXT NOT NULL DEFAULT '',
    notebook_meta_json TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE IF NOT EXISTS QUESTION_SOURCES (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id INTEGER NOT NULL REFERENCES QUESTIONS(id) ON DELETE CASCADE,
    workbook_id INTEGER NOT NULL REFERENCES SOURCE_WORKBOOKS(id) ON DELETE CASCADE,
    source_label TEXT NOT NULL,
    UNIQUE(question_id, workbook_id, source_label)
);

CREATE TABLE IF NOT EXISTS VARIANT_DRILLS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id INTEGER NOT NULL REFERENCES QUESTIONS(id) ON DELETE CASCADE,
    variant_mode TEXT NOT NULL,
    prompt_jp TEXT NOT NULL,
    options_json TEXT NOT NULL,
    correct_index INTEGER NOT NULL CHECK(correct_index BETWEEN 0 AND 3),
    metadata_json TEXT NOT NULL DEFAULT '{}',
    explanation_vi TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS FSRS_STATES (
    question_id INTEGER PRIMARY KEY REFERENCES QUESTIONS(id) ON DELETE CASCADE,
    stability REAL NOT NULL DEFAULT 0.5,
    difficulty REAL NOT NULL DEFAULT 5.0,
    reps INTEGER NOT NULL DEFAULT 0,
    lapses INTEGER NOT NULL DEFAULT 0,
    state TEXT NOT NULL DEFAULT 'new' CHECK(state IN ('new', 'learning', 'review', 'relearning')),
    scaffold_tier INTEGER NOT NULL DEFAULT 1 CHECK(scaffold_tier IN (1, 2, 3)),
    variant_passed INTEGER NOT NULL DEFAULT 0,
    clean_original_passed INTEGER NOT NULL DEFAULT 0 CHECK(clean_original_passed IN (0, 1)),
    spaced_clean_sessions INTEGER NOT NULL DEFAULT 0,
    last_clean_session_at TEXT,
    last_review TEXT,
    due_date TEXT
);

CREATE TABLE IF NOT EXISTS MOCK_EXAMS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    exam_mode TEXT NOT NULL,
    original_score_10 REAL NOT NULL DEFAULT 0.0,
    mastery_score_10 REAL NOT NULL DEFAULT 0.0,
    total_questions INTEGER NOT NULL DEFAULT 0,
    correct_count INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS ATTEMPT_LOGS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id INTEGER NOT NULL REFERENCES QUESTIONS(id) ON DELETE CASCADE,
    variant_id INTEGER REFERENCES VARIANT_DRILLS(id) ON DELETE SET NULL,
    mock_exam_id INTEGER REFERENCES MOCK_EXAMS(id) ON DELETE SET NULL,
    mode TEXT NOT NULL,
    is_correct INTEGER NOT NULL CHECK(is_correct IN (0, 1)),
    used_hint INTEGER NOT NULL DEFAULT 0 CHECK(used_hint IN (0, 1)),
    response_sec REAL NOT NULL DEFAULT 0.0,
    user_payload_json TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS USER_SETTINGS (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS GRAMMAR_POINTS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    pattern TEXT NOT NULL,
    jlpt_level TEXT NOT NULL CHECK(jlpt_level IN ('N5', 'N4', 'N3', 'N2', 'N1')),
    category TEXT NOT NULL,
    category_label_vi TEXT NOT NULL,
    in_exam_corpus INTEGER NOT NULL DEFAULT 0 CHECK(in_exam_corpus IN (0, 1)),
    formation_formula TEXT NOT NULL,
    formation_table_json TEXT NOT NULL DEFAULT '[]',
    core_meaning_vi TEXT NOT NULL,
    deep_explanation_vi TEXT NOT NULL,
    register_tag TEXT NOT NULL DEFAULT '',
    confusable_pairs_json TEXT NOT NULL DEFAULT '[]',
    examples_json TEXT NOT NULL DEFAULT '[]',
    source_ref TEXT NOT NULL DEFAULT '',
    search_keywords TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS QUESTION_GRAMMAR_LINKS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id INTEGER NOT NULL REFERENCES QUESTIONS(id) ON DELETE CASCADE,
    grammar_id INTEGER NOT NULL REFERENCES GRAMMAR_POINTS(id) ON DELETE CASCADE,
    role TEXT NOT NULL CHECK(role IN ('primary_target', 'distractor_trap', 'sentence_structure', 'discourse_marker')),
    note_vi TEXT NOT NULL DEFAULT '',
    UNIQUE(question_id, grammar_id, role)
);

CREATE TABLE IF NOT EXISTS QUESTION_GRAMMAR_ANALYSES (
    question_id INTEGER PRIMARY KEY REFERENCES QUESTIONS(id) ON DELETE CASCADE,
    structure_parse_vi TEXT NOT NULL DEFAULT '',
    pedagogical_takeaway_vi TEXT NOT NULL DEFAULT '',
    option_grammar_notes_json TEXT NOT NULL DEFAULT '[]'
);

CREATE TABLE IF NOT EXISTS GRAMMAR_DRILLS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    drill_key TEXT NOT NULL UNIQUE,
    grammar_id INTEGER NOT NULL REFERENCES GRAMMAR_POINTS(id) ON DELETE CASCADE,
    drill_type TEXT NOT NULL CHECK(drill_type IN ('formation', 'contrast', 'application')),
    prompt_jp TEXT NOT NULL,
    options_json TEXT NOT NULL,
    correct_index INTEGER NOT NULL CHECK(correct_index BETWEEN 0 AND 3),
    translation_vi TEXT NOT NULL DEFAULT '',
    explanation_vi TEXT NOT NULL DEFAULT '',
    option_diagnostics_json TEXT NOT NULL DEFAULT '[]'
);

CREATE TABLE IF NOT EXISTS GRAMMAR_FSRS_STATES (
    grammar_id INTEGER PRIMARY KEY REFERENCES GRAMMAR_POINTS(id) ON DELETE CASCADE,
    stability REAL NOT NULL DEFAULT 0.5,
    difficulty REAL NOT NULL DEFAULT 5.0,
    reps INTEGER NOT NULL DEFAULT 0,
    lapses INTEGER NOT NULL DEFAULT 0,
    state TEXT NOT NULL DEFAULT 'new' CHECK(state IN ('new', 'learning', 'review', 'relearning')),
    formation_passed INTEGER NOT NULL DEFAULT 0 CHECK(formation_passed IN (0, 1)),
    contrast_passed INTEGER NOT NULL DEFAULT 0 CHECK(contrast_passed IN (0, 1)),
    application_passed INTEGER NOT NULL DEFAULT 0 CHECK(application_passed IN (0, 1)),
    last_review TEXT,
    due_date TEXT
);

CREATE TABLE IF NOT EXISTS GRAMMAR_ATTEMPT_LOGS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    grammar_id INTEGER NOT NULL REFERENCES GRAMMAR_POINTS(id) ON DELETE CASCADE,
    drill_id INTEGER REFERENCES GRAMMAR_DRILLS(id) ON DELETE SET NULL,
    drill_type TEXT NOT NULL,
    is_correct INTEGER NOT NULL CHECK(is_correct IN (0, 1)),
    response_sec REAL NOT NULL DEFAULT 0.0,
    selected_orig_index INTEGER,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS VOCAB_FOUNDATION (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vocab_key TEXT NOT NULL UNIQUE,
    word TEXT NOT NULL,
    reading TEXT NOT NULL DEFAULT '',
    han_viet TEXT NOT NULL DEFAULT '',
    radical_note TEXT NOT NULL DEFAULT '',
    meaning_vi TEXT NOT NULL DEFAULT '',
    collocation_tip TEXT NOT NULL DEFAULT '',
    jlpt_level TEXT NOT NULL DEFAULT 'N3' CHECK(jlpt_level IN ('N5', 'N4', 'N3', 'N2', 'N1')),
    in_exam_corpus INTEGER NOT NULL DEFAULT 0 CHECK(in_exam_corpus IN (0, 1)),
    source_ref TEXT NOT NULL DEFAULT '',
    linked_question_ids_json TEXT NOT NULL DEFAULT '[]'
);

CREATE INDEX IF NOT EXISTS idx_questions_unit ON QUESTIONS(unit_code);
CREATE INDEX IF NOT EXISTS idx_questions_section ON QUESTIONS(section);
CREATE INDEX IF NOT EXISTS idx_questions_passage ON QUESTIONS(passage_id);
CREATE INDEX IF NOT EXISTS idx_variants_question ON VARIANT_DRILLS(question_id);
CREATE INDEX IF NOT EXISTS idx_fsrs_due ON FSRS_STATES(due_date);
CREATE INDEX IF NOT EXISTS idx_attempts_question_created ON ATTEMPT_LOGS(question_id, created_at DESC);
CREATE INDEX IF NOT EXISTS idx_grammar_points_level_cat ON GRAMMAR_POINTS(jlpt_level, category);
CREATE INDEX IF NOT EXISTS idx_grammar_points_exam ON GRAMMAR_POINTS(in_exam_corpus);
CREATE INDEX IF NOT EXISTS idx_qgl_question ON QUESTION_GRAMMAR_LINKS(question_id);
CREATE INDEX IF NOT EXISTS idx_qgl_grammar ON QUESTION_GRAMMAR_LINKS(grammar_id);
CREATE INDEX IF NOT EXISTS idx_grammar_drills_grammar_type ON GRAMMAR_DRILLS(grammar_id, drill_type);
CREATE INDEX IF NOT EXISTS idx_grammar_fsrs_due ON GRAMMAR_FSRS_STATES(state, due_date);
CREATE INDEX IF NOT EXISTS idx_grammar_attempts_grammar_created ON GRAMMAR_ATTEMPT_LOGS(grammar_id, created_at DESC);
CREATE INDEX IF NOT EXISTS idx_vocab_foundation_level_exam ON VOCAB_FOUNDATION(jlpt_level, in_exam_corpus);
"""


def get_connection(db_path: Optional[Path] = None) -> sqlite3.Connection:
    """Open a SQLite connection configured with WAL mode and foreign keys."""
    resolved_path = Path(db_path) if db_path is not None else get_db_path()
    resolved_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(resolved_path), timeout=30.0, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA foreign_keys=ON;")
    conn.execute("PRAGMA busy_timeout=5000;")
    return conn


@contextmanager
def transaction(db_path: Optional[Path] = None) -> Iterator[sqlite3.Connection]:
    """Context manager yielding an isolated SQLite transaction."""
    conn = get_connection(db_path=db_path)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_db(db_path: Optional[Path] = None) -> Path:
    """Initialize SQLite schema and default settings."""
    resolved_path = Path(db_path) if db_path is not None else get_db_path()
    with transaction(resolved_path) as conn:
        conn.executescript(SCHEMA_SQL)
        defaults = {
            "days_remaining": str(DEFAULT_DAYS_REMAINING),
            "daily_minutes": str(DEFAULT_DAILY_MINUTES),
            "scoring_mode": DEFAULT_SCORING_MODE,
            "default_stability": str(DEFAULT_STABILITY),
            "default_difficulty": str(DEFAULT_DIFFICULTY),
        }
        for key, val in defaults.items():
            conn.execute(
                "INSERT OR IGNORE INTO USER_SETTINGS (key, value) VALUES (?, ?)",
                (key, val),
            )
    return resolved_path
