"""Shared pytest fixtures ensuring 100% isolated temporary SQLite databases."""

import pytest


@pytest.fixture
def isolated_db(tmp_path, monkeypatch):
    """Point N3_MASTERY_DB_PATH to a unique temporary SQLite file per test."""
    db_file = tmp_path / "test_n3_mastery.db"
    monkeypatch.setenv("N3_MASTERY_DB_PATH", str(db_file))
    from n3_mastery.database import init_db

    init_db()
    return db_file
