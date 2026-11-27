"""Verification tests for Frontend SPA assets, tokens.json, DESIGN.md, and Anti-Slop compliance."""

import json
import re
from pathlib import Path

from fastapi.testclient import TestClient

from n3_mastery.api import app
from n3_mastery.config import BASE_DIR


FORBIDDEN_EMOJI_RE = re.compile(r"[\U0001F300-\U0001FAFF\u2600-\u2604\u2606-\u26FF\u2700-\u27BF]")


def test_design_and_tokens_single_source_of_truth():
    design_path = BASE_DIR / "DESIGN.md"
    tokens_path = BASE_DIR / "tokens.json"
    assert design_path.exists()
    assert tokens_path.exists()

    tokens = json.loads(tokens_path.read_text(encoding="utf-8"))
    assert tokens["meta"]["defaultTheme"] == "light"
    assert tokens["themes"]["light"]["bgBase"] == "#FAFAF9"
    assert tokens["themes"]["light"]["accentPrimary"] == "#1D4ED8"
    assert tokens["themes"]["dark"]["bgBase"] == "#1E1E24"
    assert tokens["themes"]["dark"]["accentPrimary"] == "#38BDF8"


def test_spa_routes_and_zero_decorative_emojis(isolated_db):
    with TestClient(app) as client:
        r_html = client.get("/")
        assert r_html.status_code == 200
        html = r_html.text
        assert "JLPT N3 10/10 Mastery" in html
        assert 'aria-label="Điều hướng chính"' in html
        assert 'role="dialog"' in html
        assert 'aria-modal="true"' in html

        r_css = client.get("/static/app.css")
        assert r_css.status_code == 200
        css = r_css.text
        assert '[data-theme="dark"]' in css
        assert "overflow-wrap: anywhere" in css
        assert "skeleton-line" in css

        r_js = client.get("/static/app.js")
        assert r_js.status_code == 200
        js = r_js.text

        # Ensure zero decorative emojis in HTML, CSS, JS, and DESIGN.md (★ U+2605 is explicitly allowed JLPT marker)
        for label, content in (
            ("index.html", html),
            ("app.css", css),
            ("app.js", js),
            ("DESIGN.md", (BASE_DIR / "DESIGN.md").read_text(encoding="utf-8")),
        ):
            found = FORBIDDEN_EMOJI_RE.findall(content)
            assert found == [], f"Phát hiện ký tự emoji cấm trong {label}: {found}"
