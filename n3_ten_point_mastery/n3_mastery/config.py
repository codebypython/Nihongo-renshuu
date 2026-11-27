"""Configuration and constants for JLPT N3 10/10 Mastery System."""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def get_db_path() -> Path:
    """Resolve database path dynamically from N3_MASTERY_DB_PATH for test isolation."""
    env_path = os.environ.get("N3_MASTERY_DB_PATH")
    if env_path and env_path.strip():
        return Path(env_path.strip())
    return BASE_DIR / "data" / "n3_mastery.db"


def get_excel_dir() -> Path:
    """Resolve source Excel folder path."""
    env_dir = os.environ.get("N3_MASTERY_EXCEL_DIR")
    if env_dir and env_dir.strip():
        return Path(env_dir.strip())
    return BASE_DIR.parent / "exam_downloads"


# Scoring constants (Dual 10-point calibration)
TOTAL_SCORE_10 = 10.0
SECTION_WEIGHTS_JLPT = {
    "vocab": 3.0,
    "grammar": 4.0,
    "reading": 3.0,
}

# Anti-Rote Mastery Gate constants
MASTERY_PARTIAL_CREDIT_CLEAN = 0.45
MASTERY_PARTIAL_CREDIT_HINTED = 0.30
MASTERY_REQUIRED_SPACED_REPS = 2
MIN_SPACED_SESSION_HOURS = 1.0  # minimum spacing between two review sessions to count as spaced

# FSRS & Adaptive Pace defaults
DEFAULT_DAYS_REMAINING = 14
DEFAULT_DAILY_MINUTES = 60
DEFAULT_SCORING_MODE = "jlpt_weighted"
DEFAULT_DIFFICULTY = 5.0
DEFAULT_STABILITY = 0.5
MIN_DIFFICULTY = 1.0
MAX_DIFFICULTY = 10.0

# Initial stability in days by rating: 1=Again, 2=Hard, 3=Good, 4=Easy
INITIAL_STABILITY_DAYS = {
    1: 0.25,
    2: 1.0,
    3: 2.5,
    4: 4.5,
}

# Scaffolding stability thresholds (days)
SCAFFOLD_TIER2_STABILITY = 3.0
SCAFFOLD_TIER3_STABILITY = 7.0

# Workload estimate constants (minutes)
WORKLOAD_BRIDGE_MIN = 7.0
WORKLOAD_ORIGINAL_MIN = 1.5
WORKLOAD_VARIANT_MIN = 2.15
WORKLOAD_REMEDIATION_MIN = 2.0

# Server defaults
DEFAULT_API_HOST = "127.0.0.1"
DEFAULT_API_PORT = 8010
