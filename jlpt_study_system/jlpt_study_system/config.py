"""Configuration module for JLPT N3 Study System."""

import os
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_DB_PATH = os.environ.get("JLPT_DB_PATH")
DEFAULT_DB_PATH = Path(ENV_DB_PATH) if ENV_DB_PATH else (BASE_DIR / "data" / "jlpt_study.db")
SPRINT_REFERENCE_DIR = Path(os.environ.get("JLPT_SPRINT_DIR", BASE_DIR.parent / "jlpt_n3_sprint"))

# JLPT N3 Scoring Constants
PASS_TOTAL_THRESHOLD = 95
MAX_TOTAL_SCORE = 180

SECTION_CUTOFF = 19
SECTION_MAX_SCORE = 60

# Sprint Operational Parameters
SPRINT_TOTAL_DAYS = 7
POMODORO_WORK_MINUTES = 50
POMODORO_REST_MINUTES = 10
TARGET_DAILY_POMODORO = 12  # 12 blocks per day * 50 min ~ 10-12 hours sprint

# FSRS / Spaced Repetition Parameters (Tuned for 7-day intensive sprint)
DESIRED_RETENTION_SPRINT = 0.80  # 80% retention to avoid card backlog explosion
DEFAULT_DIFFICULTY = 5.0
DEFAULT_STABILITY = 2.0
MIN_DIFFICULTY = 1.0
MAX_DIFFICULTY = 10.0

# Initial stability in days for ratings [Again=1, Hard=2, Good=3, Easy=4]
INITIAL_STABILITY = {
    1: 0.4,  # ~10 hours (due today)
    2: 1.0,  # 1 day
    3: 2.2,  # ~2 days
    4: 4.5,  # ~4-5 days
}
