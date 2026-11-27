"""End-to-end real browser verification (Desktop 1440x900 & Mobile 390x844, Light & Dark, 0 console errors)."""

import os
import socket
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

from n3_mastery.config import BASE_DIR

def resolve_screenshot_dir(tmp_path: Path) -> Path:
    """Use N3_SCREENSHOT_DIR when provided, otherwise keep screenshots inside pytest's tmp_path."""
    env_dir = os.environ.get("N3_SCREENSHOT_DIR", "").strip()
    if env_dir:
        return Path(env_dir)
    return tmp_path / "screenshots"


def test_resolve_screenshot_dir_defaults_to_tmp_path(tmp_path, monkeypatch):
    monkeypatch.delenv("N3_SCREENSHOT_DIR", raising=False)
    assert resolve_screenshot_dir(tmp_path) == tmp_path / "screenshots"

    custom_dir = tmp_path / "custom_shots"
    monkeypatch.setenv("N3_SCREENSHOT_DIR", str(custom_dir))
    assert resolve_screenshot_dir(tmp_path) == custom_dir


def _find_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return int(s.getsockname()[1])


def _wait_for_server(url: str, timeout: float = 25.0) -> None:
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=2.0) as resp:
                if resp.status == 200:
                    return
        except Exception:
            time.sleep(0.3)
    raise RuntimeError(f"Server did not become ready at {url}")


def test_real_browser_desktop_and_mobile_light_dark_zero_errors(isolated_db, tmp_path):
    port = _find_free_port()
    env = os.environ.copy()
    env["N3_MASTERY_DB_PATH"] = str(isolated_db)
    env["PYTHONPATH"] = str(BASE_DIR)

    proc = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "uvicorn",
            "n3_mastery.api:app",
            "--host",
            "127.0.0.1",
            "--port",
            str(port),
            "--log-level",
            "warning",
        ],
        cwd=str(BASE_DIR),
        env=env,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    screenshot_dir = resolve_screenshot_dir(tmp_path)
    screenshot_dir.mkdir(parents=True, exist_ok=True)
    base_url = f"http://127.0.0.1:{port}"

    try:
        _wait_for_server(f"{base_url}/api/health")

        console_errors = []
        page_errors = []

        with sync_playwright() as p:
            browser = p.chromium.launch(channel="chrome", headless=True)
            context = browser.new_context(viewport={"width": 1440, "height": 900})
            page = context.new_page()

            page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
            page.on("pageerror", lambda err: page_errors.append(str(err)))

            # 1. Desktop Light Mode (1440x900)
            page.goto(base_url, wait_until="networkidle")
            page.wait_for_selector("#dash-heading")
            assert page.get_attribute("html", "data-theme") == "light"
            assert "0.00" in page.locator(".score-big").first.text_content()
            assert page.is_visible("#dash-grammar-card")
            assert page.is_visible("#quick-guide-card")
            assert page.locator(".topic-grid .topic-card").count() == 12
            # Toggle quick-start guide collapse/expand cleanly
            page.click("#btn-toggle-quick-guide")
            assert page.locator("#quick-guide-card .guide-steps-grid").count() == 0
            page.click("#btn-toggle-quick-guide")
            assert page.is_visible("#btn-guide-open-grammar")
            overflow_desktop = page.evaluate("document.documentElement.scrollWidth > window.innerWidth")
            assert overflow_desktop is False
            page.screenshot(path=str(screenshot_dir / "desktop_light.png"), full_page=False)

            # 2. Adaptive Pace check -> honest capacity warning
            page.fill("#inp-days", "4")
            page.fill("#inp-minutes", "25")
            page.click("#pace-form button[type='submit']")
            page.wait_for_selector(".callout-danger")
            assert "[WARN]" in page.locator(".callout-danger").first.text_content()

            # 3. Toggle Dark Mode via keyboard shortcut 'T'
            page.keyboard.press("t")
            assert page.get_attribute("html", "data-theme") == "dark"
            page.screenshot(path=str(screenshot_dir / "desktop_dark.png"), full_page=False)
            page.keyboard.press("t")
            assert page.get_attribute("html", "data-theme") == "light"

            # 4. Accessible Modal open & close via Esc
            page.click("#btn-help-modal")
            assert page.is_visible("#help-modal")
            page.keyboard.press("Escape")
            assert page.is_hidden("#help-modal-backdrop")

            # 5. Open N4 Bridge Capsule for MU-01 and inspect
            page.click('.btn-open-bridge[data-unit="MU-01"]')
            page.wait_for_selector("#btn-complete-bridge")
            assert "MU-01" in page.locator("#study-heading").text_content()

            # 6. Interactive 4-Slot Star Assembly (MU-10)
            page.select_option("#study-unit-sel", "MU-10")
            page.select_option("#study-mode-sel", "original")
            page.wait_for_selector(".star-slots-grid")
            # Submit button MUST be disabled until all 4 slots are filled
            assert page.is_disabled("#btn-submit-study")
            chips = page.locator(".chunks-pool .chunk-chip")
            assert chips.count() == 4
            for i in range(4):
                chips.nth(i).click()
            assert not page.is_disabled("#btn-submit-study")
            page.click("#btn-submit-study")
            page.wait_for_selector("#btn-next-study")
            # Post-submit Grammar Anatomy & Modal inspection (preserves current study progress)
            page.wait_for_selector(".grammar-breakdown-box")
            assert "Giải phẫu Ngữ pháp" in page.locator(".grammar-breakdown-box").text_content()
            page.locator(".grammar-breakdown-box .grammar-chip-btn").first.click()
            page.wait_for_selector("#grammar-modal .grammar-lesson-block")
            assert page.is_visible("#grammar-modal")
            page.keyboard.press("Escape")
            assert page.is_hidden("#grammar-modal-backdrop")
            assert page.is_visible("#btn-next-study")
            page.screenshot(path=str(screenshot_dir / "study_star_4slot.png"), full_page=False)

            # 7. Interactive Dokkai Evidence-First (MU-11) & Space shortcut after mouse click
            page.select_option("#study-unit-sel", "MU-11")
            page.select_option("#study-mode-sel", "variant")
            page.wait_for_selector(".dokkai-split")
            # Zero-leakage: no grammar breakdown before submitting
            assert page.locator(".grammar-breakdown-box").count() == 0
            page.locator(".passage-sentence.selectable").first.click()
            page.locator(".options-list .option-btn").first.click()
            assert not page.is_disabled("#btn-submit-study")
            page.keyboard.press("Space")
            page.wait_for_selector("#btn-next-study")
            page.screenshot(path=str(screenshot_dir / "study_dokkai_evidence.png"), full_page=False)

            # Jump directly from Study Grammar Modal -> Grammar Drill BEFORE opening Ngữ pháp tab
            page.locator(".grammar-breakdown-box .grammar-chip-btn").first.click()
            page.wait_for_selector("#grammar-modal .btn-practice-grammar")
            page.locator("#grammar-modal .btn-practice-grammar").click()
            page.wait_for_selector("#grammar-overview-strip .grammar-stat-box")
            assert page.locator("#grammar-overview-strip .grammar-stat-box").count() == 4
            page.wait_for_selector("#grammar-drill-stage .grammar-drill-opt-btn")
            page.click("#btn-clear-grammar-filter")
            page.wait_for_selector("#grammar-drill-stage .grammar-drill-opt-btn")

            # 8. Exam Mode (Phòng thi Thực chiến) full UI walkthrough including any 4-slot ★ item
            page.click('.nav-btn[data-view="exam"]')
            page.wait_for_selector("#btn-start-exam")
            page.select_option("#exam-count-sel", "2")
            page.click("#btn-start-exam")
            page.wait_for_selector("#btn-submit-exam")
            # Confirm zero artificial scaffolding inside Exam Mode view
            assert page.locator("#exam-root .scaffold-ruby").count() == 0
            # Answer all questions in the exam grid (both MCQ and any 4-slot ★)
            exam_q_cards = page.locator("#exam-root > .stack-md > .card")
            for idx in range(exam_q_cards.count()):
                card = exam_q_cards.nth(idx)
                chips = card.locator(".chunk-chip")
                if chips.count() == 4:
                    for ci in range(4):
                        chips.nth(ci).click()
                else:
                    card.locator(".option-btn").first.click()
            page.click("#btn-submit-exam")
            page.wait_for_selector("#btn-exam-reset")
            assert "Kết quả Phòng thi Thực chiến" in page.locator("#exam-root").text_content()
            page.screenshot(path=str(screenshot_dir / "exam_result.png"), full_page=False)

            # 9. Notebook & Live Chrome .xlsx file upload
            page.click('.nav-btn[data-view="notebook"]')
            page.wait_for_selector("#excel-upload-form")
            assert "7 tệp" in page.locator("#notebook-root").text_content()

            import openpyxl
            upload_path = tmp_path / "browser_upload_extra.xlsx"
            wb_up = openpyxl.Workbook()
            ws_up = wb_up.active
            ws_up.title = "Tong_Hop_On_Thi"
            ws_up.append(["ĐỀ UPLOAD TRÌNH DUYỆT"])
            ws_up.append(["Hướng dẫn"])
            ws_up.append([])
            ws_up.append([
                "Mondai", "Câu", "Từ khóa", "Đề bài", "Đ1", "Đ2", "Đ3", "Đ4",
                "Tự chọn", "KQ", "Đáp án đúng", "Nội dung", "Dịch", "Giải thích"
            ])
            ws_up.append([
                "問題1: Cách đọc Kanji", 1, "技術 → ぎじゅつ", "新しい【技術】を学ぶ。",
                "きじゅつ", "ぎじゅつ", "ぎしゅつ", "きしゅつ", None, None, 2, "2. ぎじゅつ",
                "Học kỹ thuật mới.",
                "• Đáp án đúng: 2. ぎじゅつ.\n• Bẫy:\n  - 1. きじゅつ (記述: ghi chép)."
            ])
            ws_nb = wb_up.create_sheet("So_Tay_Tu_Vung")
            ws_nb.append(["SỔ TAY"])
            ws_nb.append([])
            ws_nb.append(["STT", "Nguồn câu", "Từ vựng", "Hiragana", "Hán Việt", "Nghĩa", "Mẹo"])
            ws_nb.append([1, "Câu 1", "技術", "ぎじゅつ", "KỸ THUẬT", "Kỹ thuật", "新しい技術"])
            wb_up.save(upload_path)

            page.set_input_files("#inp-xlsx-file", str(upload_path))
            page.click('#excel-upload-form button[type="submit"]')
            page.wait_for_selector("#notebook-root .callout-success")
            assert "8 tệp" in page.locator("#notebook-root").text_content()

            # Also upload a partial Layout B (Phan_II_Ngu_Phap only, no Dashboard_Tong_Quan) via live Chrome UI
            upload_b_path = tmp_path / "browser_upload_partial_b.xlsx"
            wb_b = openpyxl.Workbook()
            ws_b = wb_b.active
            ws_b.title = "Phan_II_Ngu_Phap"
            ws_b.append(["Gói", "Câu", "Mẫu", "Đề bài", "Đ1", "Đ2", "Đ3", "Đ4", "T", "K", "ĐA", "ND", "Câu hoàn chỉnh", "GT"])
            ws_b.append([
                "II-2. 問題2: Sắp xếp câu sao ★", "1)", "Định ngữ",
                "駅の前で ＿＿＿ ＿＿＿ ★ ＿＿＿ 買った。",
                "花を", "きれいな", "友だちに", "渡す", None, None, 2, "2. きれいな",
                "Câu hoàn chỉnh: 駅の前で [3. 友だちに] [4. 渡す] [★ 2. きれいな] [1. 花を] 買った。",
                "Giải thích.",
            ])
            wb_b.save(upload_b_path)
            page.set_input_files("#inp-xlsx-file", str(upload_b_path))
            page.click('#excel-upload-form button[type="submit"]')
            page.wait_for_function("document.querySelector('#notebook-root')?.textContent?.includes('9 tệp')")
            assert "9 tệp" in page.locator("#notebook-root").text_content()

            # 10. Error + Retry UI banner check via simulated API abort on Dashboard
            assert console_errors == [], f"Unexpected console errors before simulated abort: {console_errors}"

            def _abort_dash(route):
                route.abort()

            page.route("**/api/dashboard", _abort_dash)
            page.click('.nav-btn[data-view="dashboard"]')
            page.wait_for_selector("#btn-retry-dash")
            assert page.is_visible(".state-error")
            page.unroute("**/api/dashboard", _abort_dash)
            # Clear the intentional simulated network-abort console entry before testing Retry + Mobile
            console_errors.clear()
            page.click("#btn-retry-dash")
            page.wait_for_selector("#dash-heading")
            assert "165" in page.locator("#dash-heading").locator("..").text_content()

            # 11. Ngữ pháp & JLPT tab: Library filters, 3D lesson, Grammar Drill, Foundation Vocab, JLPT Expansion
            page.click('.nav-btn[data-view="grammar"]')
            page.wait_for_selector("#grammar-heading")
            page.click('.subnav-btn[data-grammar-tab="library"]')
            page.wait_for_selector("#grammar-library-results .grammar-point-card")

            page.select_option("#grammar-scope-sel", "exam")
            page.wait_for_function(
                "() => { const c = document.querySelectorAll('#grammar-library-results .grammar-point-card'); return c.length > 0 && Array.from(c).every(el => el.textContent.includes('[THI CUỐI KÌ]')); }"
            )
            page.select_option("#grammar-scope-sel", "jlpt")
            page.wait_for_function(
                "() => { const c = document.querySelectorAll('#grammar-library-results .grammar-point-card'); return c.length > 0 && Array.from(c).every(el => el.textContent.includes('[MỞ RỘNG JLPT]')); }"
            )
            page.select_option("#grammar-scope-sel", "all")

            for lvl in ("N5", "N4", "N3", "N2"):
                page.select_option("#grammar-level-sel", lvl)
                page.wait_for_function(
                    f"() => {{ const c = document.querySelectorAll('#grammar-library-results .grammar-point-card'); return c.length > 0 && Array.from(c).every(el => el.textContent.includes('[{lvl}]')); }}"
                )
            page.select_option("#grammar-level-sel", "ALL")
            page.wait_for_function(
                "() => document.querySelectorAll('#grammar-library-results .grammar-point-card').length >= 100"
            )

            # Open 3D grammar lesson detail
            page.locator("#grammar-library-results .grammar-point-card").first.click()
            page.wait_for_selector("#grammar-detail-panel .grammar-lesson-block")
            detail_txt = page.locator("#grammar-detail-panel").text_content()
            assert "Công thức chia thể" in detail_txt
            assert "Bản chất ngữ nghĩa" in detail_txt
            page.screenshot(path=str(screenshot_dir / "grammar_library.png"), full_page=False)

            # Grammar Drill subtab: zero diagnostic leak before submit, keyboard 1 + Space, 4 diagnostics after submit
            page.click('.subnav-btn[data-grammar-tab="drill"]')
            page.wait_for_selector("#grammar-drill-stage .grammar-drill-opt-btn")
            assert page.locator("#grammar-drill-stage .diagnostic-list").count() == 0
            page.keyboard.press("1")
            assert not page.is_disabled("#btn-submit-grammar-drill")
            page.keyboard.press("Space")
            page.wait_for_selector("#btn-next-grammar-drill")
            assert page.locator("#grammar-drill-stage .diagnostic-item").count() == 4
            page.screenshot(path=str(screenshot_dir / "grammar_drill.png"), full_page=False)

            # Foundation Vocab subtab
            page.click('.subnav-btn[data-grammar-tab="vocab"]')
            page.wait_for_selector("#vocab-results-container table.data-table tbody tr")
            assert page.locator("#vocab-results-container table.data-table tbody tr").count() >= 10

            # JLPT Expansion subtab
            page.click('.subnav-btn[data-grammar-tab="jlpt"]')
            page.wait_for_selector("#jlpt-levels-table tbody tr")
            assert page.locator("#jlpt-levels-table tbody tr").count() >= 4

            # 12. Mobile Viewport (390x844) Light & Dark zero horizontal overflow (Dashboard + Grammar tabs)
            page.set_viewport_size({"width": 390, "height": 844})
            assert page.evaluate("document.documentElement.scrollWidth > window.innerWidth") is False
            page.click('.subnav-btn[data-grammar-tab="library"]')
            page.wait_for_selector("#grammar-library-results .grammar-point-card")
            assert page.evaluate("document.documentElement.scrollWidth > window.innerWidth") is False
            page.click('.subnav-btn[data-grammar-tab="vocab"]')
            page.wait_for_selector("#vocab-results-container table.data-table tbody tr")
            assert page.evaluate("document.documentElement.scrollWidth > window.innerWidth") is False

            page.click('.nav-btn[data-view="dashboard"]')
            page.wait_for_selector("#dash-heading")
            overflow_mobile_light = page.evaluate("document.documentElement.scrollWidth > window.innerWidth")
            assert overflow_mobile_light is False
            page.screenshot(path=str(screenshot_dir / "mobile_light.png"), full_page=False)

            page.click("#btn-theme-toggle")
            assert page.get_attribute("html", "data-theme") == "dark"
            overflow_mobile_dark = page.evaluate("document.documentElement.scrollWidth > window.innerWidth")
            assert overflow_mobile_dark is False
            page.screenshot(path=str(screenshot_dir / "mobile_dark.png"), full_page=False)

            page.click('.nav-btn[data-view="grammar"]')
            page.wait_for_selector("#grammar-heading")
            assert page.evaluate("document.documentElement.scrollWidth > window.innerWidth") is False

            browser.close()

        assert console_errors == [], f"Console errors: {console_errors}"
        assert page_errors == [], f"Page errors: {page_errors}"
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()
