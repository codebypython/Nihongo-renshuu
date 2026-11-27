"""Tests for Rich CLI commands and interactive study workflows."""

from n3_mastery import cli


def test_cli_import_status_pace_bridge_errors(isolated_db, tmp_path, capsys):
    assert cli.main(["import"]) == 0
    assert cli.main(["import", str(tmp_path / "does_not_exist.xlsx")]) == 1
    assert cli.main(["status"]) == 0
    assert cli.main(["pace", "--days", "5", "--minutes", "30", "--scoring", "jlpt_weighted"]) == 0
    assert cli.main(["bridge", "MU-01", "--complete"]) == 0
    assert cli.main(["errors"]) == 0


def test_cli_study_interactive_quit(isolated_db, monkeypatch):
    cli.main(["import"])
    # Simulate pressing 'q' immediately to exit interactive study loop cleanly
    monkeypatch.setattr("rich.console.Console.input", lambda self, prompt="": "q")
    rc = cli.main(["study", "--unit", "MU-01", "--mode", "original", "--limit", "1"])
    assert rc == 0


def test_cli_study_interactive_mcq_hint_star_and_dokkai(isolated_db, monkeypatch, capsys):
    cli.main(["import"])

    # 1. MU-01 MCQ: press 'h' for hint, then '1' to answer
    inputs_mcq = iter(["h", "1"])
    monkeypatch.setattr("rich.console.Console.input", lambda self, prompt="": next(inputs_mcq))
    assert cli.main(["study", "--unit", "MU-01", "--mode", "original", "--limit", "1"]) == 0

    # 2. MU-10 4-slot star: bad 2-slot input first, then valid 4-slot order '0 1 2 3'
    inputs_star = iter(["0 1", "0 1 2 3"])
    monkeypatch.setattr("rich.console.Console.input", lambda self, prompt="": next(inputs_star))
    assert cli.main(["study", "--unit", "MU-10", "--mode", "original", "--limit", "1"]) == 0
    out_star = capsys.readouterr().out
    assert "4 mảnh" in out_star or "CHÍNH XÁC" in out_star or "SAI" in out_star

    # 3. MU-11 Dokkai Evidence-First: pick option '1' then evidence sentence '0 1'
    inputs_dokkai = iter(["1", "0 1"])
    monkeypatch.setattr("rich.console.Console.input", lambda self, prompt="": next(inputs_dokkai))
    assert cli.main(["study", "--unit", "MU-11", "--mode", "variant", "--limit", "1"]) == 0
