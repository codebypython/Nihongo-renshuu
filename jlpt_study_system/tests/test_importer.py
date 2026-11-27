"""Unit tests for CSV and Markdown data importer."""

from pathlib import Path
from jlpt_study_system.database import get_db, init_db
from jlpt_study_system.importer import (
    import_grammar_csv,
    import_vocab_csv,
    seed_drill_items,
    seed_curriculum_playbook,
    import_all,
    parse_playbook_markdown,
)
from jlpt_study_system.config import SPRINT_REFERENCE_DIR


def test_import_all_idempotency(tmp_path):
    db_file = tmp_path / "idempotent_test.db"

    # First import
    res1 = import_all(db_path=db_file)
    assert res1["grammar_cards"] == 40
    assert res1["vocab_cards"] == 40
    assert res1["choukai_drills"] >= 10
    assert res1["dokkai_drills"] >= 5
    assert res1["curriculum_blocks"] == 21  # 7 days * 3 blocks

    # Second import (must be idempotent and not duplicate rows)
    res2 = import_all(db_path=db_file)
    assert res2["grammar_cards"] == 40
    assert res2["vocab_cards"] == 40

    with get_db(db_file) as conn:
        total_cards = conn.execute("SELECT COUNT(*) AS c FROM cards").fetchone()["c"]
        assert total_cards == 80

        total_blocks = conn.execute("SELECT COUNT(*) AS c FROM curriculum_blocks").fetchone()["c"]
        assert total_blocks == 21


def test_grammar_card_contents(temp_db):
    with get_db(temp_db) as conn:
        row = conn.execute(
            "SELECT * FROM cards WHERE category = 'grammar' LIMIT 1"
        ).fetchone()

        assert row is not None
        assert row["front"] != ""
        assert row["back"] != ""
        # Verify FSRS state was initialized
        fsrs = conn.execute(
            "SELECT * FROM fsrs_states WHERE card_id = ?", (row["id"],)
        ).fetchone()
        assert fsrs is not None
        assert fsrs["state"] == "New"
        assert fsrs["reps"] == 0


def test_vocab_card_contents(temp_db):
    with get_db(temp_db) as conn:
        row = conn.execute(
            "SELECT * FROM cards WHERE category = 'vocab' LIMIT 1"
        ).fetchone()

        assert row is not None
        assert row["front"] != ""
        assert row["back"] != ""


def test_parse_playbook_markdown_real_file():
    md_file = SPRINT_REFERENCE_DIR / "DAY_BY_DAY_PLAYBOOK.md"
    if md_file.exists():
        blocks = parse_playbook_markdown(md_file)
        assert len(blocks) >= 21
        days = {b[0] for b in blocks}
        assert days == {1, 2, 3, 4, 5, 6, 7}
