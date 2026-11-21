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


def test_quick_run_scripts_readme_and_friendly_ui_zero_emojis():
    required_files = [
        BASE_DIR / "README.md",
        BASE_DIR / "run_all.ps1",
        BASE_DIR / "start_web.bat",
        BASE_DIR / "run_all.bat",
        BASE_DIR.parent / "README.md",
        BASE_DIR.parent / "CHAY_NHANH_WEB.bat",
        BASE_DIR.parent / "MENU_CHAY_NHANH.bat",
    ]
    for path in required_files:
        assert path.exists(), f"Thiếu tệp khởi chạy / hướng dẫn: {path}"
        text = path.read_text(encoding="utf-8")
        found = FORBIDDEN_EMOJI_RE.findall(text)
        assert found == [], f"Phát hiện ký tự emoji cấm trong {path.name}: {found}"
        if path.suffix.lower() == ".bat":
            assert text.isascii(), f"Tệp .bat phải thuần ASCII để tránh lỗi codepage Windows: {path.name}"

    html = (BASE_DIR / "n3_mastery" / "templates" / "index.html").read_text(encoding="utf-8")
    js = (BASE_DIR / "n3_mastery" / "static" / "app.js").read_text(encoding="utf-8")
    assert 'id="btn-help-modal"' in html and "Hướng dẫn" in html
    assert 'id="quick-guide-card"' in js
    assert 'class="topic-grid"' in js


_CSS_HEX_COLOR_RE = re.compile(
    r"(?:^|[\s:,(])(#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8}))(?![0-9a-zA-Z_-])"
)


def _find_hex_colors_outside_theme_blocks(css_text: str) -> list[str]:
    """Return hardcoded hex color values in declaration blocks outside :root and [data-theme="dark"]."""
    cleaned = re.sub(r"/\*.*?\*/", "", css_text, flags=re.S)
    stack: list[bool] = []
    has_child_block: list[bool] = []
    header_buf: list[str] = []
    body_buf: list[str] = []
    violations: list[str] = []

    for ch in cleaned:
        if ch == "{":
            if stack:
                has_child_block[-1] = True
            header = "".join(header_buf).strip()
            header_buf.clear()
            is_theme_block = (
                ":root" in header
                or '[data-theme="dark"]' in header
                or "[data-theme='dark']" in header
            )
            parent_allowed = stack[-1] if stack else False
            stack.append(is_theme_block or parent_allowed)
            has_child_block.append(False)
            body_buf.clear()
        elif ch == "}":
            body = "".join(body_buf)
            body_buf.clear()
            header_buf.clear()
            if stack:
                is_allowed_theme = stack.pop()
                nested = has_child_block.pop()
                if not is_allowed_theme and not nested:
                    for match in _CSS_HEX_COLOR_RE.finditer(body):
                        violations.append(match.group(1))
        else:
            if stack:
                body_buf.append(ch)
            header_buf.append(ch)
    return violations


def test_focus_mode_display_prefs_and_anti_slop_assets():
    html = (BASE_DIR / "n3_mastery" / "templates" / "index.html").read_text(encoding="utf-8")
    css = (BASE_DIR / "n3_mastery" / "static" / "app.css").read_text(encoding="utf-8")
    js = (BASE_DIR / "n3_mastery" / "static" / "app.js").read_text(encoding="utf-8")

    for req_id in ("btn-focus-mode", "btn-display-prefs", "focus-topbar", "display-prefs-modal"):
        assert req_id in html, f"Thiếu thành phần bắt buộc '{req_id}' trong index.html"

    for req_css in ("data-focus-mode", "data-font-scale", "data-hide-ruby", "--jp-prompt-size"):
        assert req_css in css, f"Thiếu quy tắc CSS bắt buộc '{req_css}' trong app.css"

    css_no_comments = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    assert "backdrop-filter" not in css_no_comments.lower(), "Cấm dùng backdrop-filter trong app.css"
    assert not re.search(r"filter\s*:\s*[^;]*blur\s*\(", css_no_comments, flags=re.I), (
        "Cấm dùng filter: blur(...) trong app.css"
    )
    hex_outside = _find_hex_colors_outside_theme_blocks(css)
    assert hex_outside == [], (
        f"Phát hiện mã màu #hex hardcode bên ngoài khối :root / [data-theme=\"dark\"]: {hex_outside}"
    )

    assert "n3_ui_preferences_v1" in js, "Thiếu khóa lưu trữ tùy chỉnh hiển thị n3_ui_preferences_v1 trong app.js"

    for readme_path in (BASE_DIR / "README.md", BASE_DIR.parent / "README.md"):
        readme_text = readme_path.read_text(encoding="utf-8")
        assert FORBIDDEN_EMOJI_RE.findall(readme_text) == []
        for keyword in ("Ẩn/Hiện", "Tập trung", "Đọc tập trung từng bài", "1 cột dọc dễ đọc", "Tập trung từng câu"):
            assert keyword in readme_text, f"Thiếu hướng dẫn '{keyword}' trong {readme_path}"
