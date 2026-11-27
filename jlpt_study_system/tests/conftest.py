"""Test configuration and fixtures."""

import sys
from pathlib import Path
import pytest

# Ensure jlpt_study_system is in python path
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from jlpt_study_system.database import init_db
from jlpt_study_system.importer import import_all


@pytest.fixture
def temp_db(tmp_path):
    """Provide an isolated temporary SQLite database for tests."""
    db_file = tmp_path / "test_jlpt.db"
    init_db(db_file)
    import_all(db_path=db_file)
    return db_file
