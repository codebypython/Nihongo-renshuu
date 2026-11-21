"""Tests for Rich CLI commands and interactive study workflows."""

import sqlite3

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


def test_cli_default_help_doctor_backup_and_quickstart(isolated_db, tmp_path, monkeypatch, capsys):
    # Calling with no args displays friendly Vietnamese quick-start banner
    assert cli.main([]) == 0
    help_out = capsys.readouterr().out
    assert "quickstart" in help_out
    assert "CHAY_NHANH_WEB.bat" in help_out

    # doctor checks SQLite integrity & seeds automatically
    assert cli.main(["doctor"]) == 0
    doc_out = capsys.readouterr().out
    assert "163" in doc_out
    assert "[OK]" in doc_out

    # backup writes an openable SQLite snapshot to --dir
    bk_dir = tmp_path / "backups_out"
    assert cli.main(["backup", "--dir", str(bk_dir)]) == 0
    bk_files = list(bk_dir.glob("*.db"))
    assert len(bk_files) == 1
    bconn = sqlite3.connect(str(bk_files[0]))
    try:
        assert bconn.execute("SELECT COUNT(*) FROM QUESTIONS").fetchone()[0] == 163
        assert bconn.execute("SELECT COUNT(*) FROM GRAMMAR_POINTS").fetchone()[0] >= 135
    finally:
        bconn.close()

    # quickstart reuses existing running server cleanly and opens browser
    opened_urls = []
    uvicorn_calls = []
    monkeypatch.setattr(cli.webbrowser, "open", lambda url: opened_urls.append(url) or True)
    monkeypatch.setattr(cli.uvicorn, "run", lambda *a, **kw: uvicorn_calls.append((a, kw)))
    monkeypatch.setattr(cli, "_is_mastery_server_running", lambda h, p: True)
    assert cli.main(["quickstart", "--port", "8999"]) == 0
    assert opened_urls == ["http://127.0.0.1:8999"]
    assert uvicorn_calls == []

    # quickstart launches uvicorn when no server is already running
    monkeypatch.setattr(cli, "_is_mastery_server_running", lambda h, p: False)
    monkeypatch.setattr(cli, "_pick_available_port", lambda h, p: 8999)
    assert cli.main(["quickstart", "--port", "8999", "--no-browser"]) == 0
    assert len(uvicorn_calls) == 1
    assert uvicorn_calls[0][1]["port"] == 8999
