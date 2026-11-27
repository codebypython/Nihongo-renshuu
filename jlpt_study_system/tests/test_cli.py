"""Unit tests for CLI command functions with full isolation and interactive coverage."""

import pytest
from rich.prompt import Prompt
from jlpt_study_system.cli import (
    cmd_init,
    cmd_status,
    cmd_study,
    cmd_drill,
    cmd_errors,
    cmd_pomodoro,
    main,
)


@pytest.fixture(autouse=True)
def isolated_cli_db(tmp_path, monkeypatch):
    """Ensure every CLI test operates on an isolated temporary database."""
    test_db = tmp_path / "cli_test.db"
    monkeypatch.setenv("JLPT_DB_PATH", str(test_db))
    cmd_init()
    return test_db


def test_cli_init_execution():
    # Calling init again should be idempotent
    cmd_init()


def test_cli_status_execution():
    cmd_status()


def test_cli_errors_execution():
    cmd_errors()


def test_cli_study_interactive(monkeypatch):
    # Mock user input: Enter to flip, '3' for Good grade
    monkeypatch.setattr("builtins.input", lambda _: "")
    monkeypatch.setattr(Prompt, "ask", lambda *args, **kwargs: "3")
    cmd_study(limit=2, category="grammar")


def test_cli_study_quit(monkeypatch):
    # Mock user pressing 'q' to quit early
    monkeypatch.setattr("builtins.input", lambda _: "")
    monkeypatch.setattr(Prompt, "ask", lambda *args, **kwargs: "q")
    cmd_study(limit=5)


def test_cli_drill_choukai_interactive(monkeypatch):
    # Mock user selecting option '1'
    monkeypatch.setattr(Prompt, "ask", lambda *args, **kwargs: "1")
    cmd_drill("choukai")


def test_cli_drill_dokkai_interactive(monkeypatch):
    # Mock user selecting option '2'
    monkeypatch.setattr(Prompt, "ask", lambda *args, **kwargs: "2")
    cmd_drill("dokkai")


def test_cli_pomodoro_execution(monkeypatch):
    # Mock task label prompt and sleep to avoid waiting real seconds
    monkeypatch.setattr(Prompt, "ask", lambda *args, **kwargs: "Grammar Deep Dive")
    monkeypatch.setattr("time.sleep", lambda _: None)
    cmd_pomodoro(minutes=1, day=1)


def test_cli_main_subcommands(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "")
    monkeypatch.setattr(Prompt, "ask", lambda *args, **kwargs: "q")
    monkeypatch.setattr("time.sleep", lambda _: None)

    for cmd_args in [
        ["jlpt_cli", "status"],
        ["jlpt_cli", "errors"],
        ["jlpt_cli", "drill", "choukai"],
        ["jlpt_cli", "study", "--limit", "1"],
        ["jlpt_cli", "pomodoro", "--minutes", "1"],
    ]:
        monkeypatch.setattr("sys.argv", cmd_args)
        main()
