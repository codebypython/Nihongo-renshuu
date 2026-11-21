"""Playwright E2E tests for Focus Mode, Display Preferences, and Per-Component Visibility Controls."""

import os
import socket
import subprocess
import sys
import time
import urllib.request

from playwright.sync_api import sync_playwright

from n3_mastery.config import BASE_DIR


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


def _assert_no_horizontal_overflow(page, label: str) -> None:
    overflow = page.evaluate("document.documentElement.scrollWidth > window.innerWidth")
    assert overflow is False, f"Horizontal overflow detected at {label}"


def _verify_desktop_header_and_focus_mode(page) -> None:
    header_height = page.locator(".app-header").evaluate("el => el.getBoundingClientRect().height")
    assert header_height <= 76, f"Desktop header height {header_height}px exceeded 76px single-row limit"
    _assert_no_horizontal_overflow(page, "desktop_initial")

    assert page.get_attribute("html", "data-focus-mode") == "off"
    assert page.get_attribute("html", "data-font-scale") == "md"
    assert page.get_attribute("html", "data-hide-ruby") == "0"
    assert page.is_hidden("#focus-topbar")

    # Toggle Focus Mode on via header button
    page.click("#btn-focus-mode")
    assert page.get_attribute("html", "data-focus-mode") == "on"
    assert page.is_hidden(".app-header")
    assert page.is_visible("#focus-topbar")

    # Switch views via #focus-topbar quick nav
    page.click('#focus-topbar [data-focus-view="grammar"]')
    page.wait_for_selector("#grammar-heading")
    assert page.is_visible("#view-grammar")
    assert page.get_attribute("html", "data-focus-mode") == "on"

    page.click('#focus-topbar [data-focus-view="dashboard"]')
    page.wait_for_selector("#dash-heading")

    # Open #display-prefs-modal from focus topbar, close with Esc -> Focus Mode stays intact
    page.click("#btn-focus-prefs")
    page.wait_for_selector("#display-prefs-modal")
    assert page.is_visible("#display-prefs-modal")
    page.keyboard.press("Escape")
    assert page.is_hidden("#display-prefs-backdrop")
    assert page.get_attribute("html", "data-focus-mode") == "on"
    assert page.is_visible("#focus-topbar")

    # Next Esc exits Focus Mode cleanly
    page.keyboard.press("Escape")
    assert page.get_attribute("html", "data-focus-mode") == "off"
    assert page.is_hidden("#focus-topbar")
    assert page.is_visible(".app-header")

    # Keyboard shortcut F enters and exits Focus Mode
    page.keyboard.press("f")
    assert page.get_attribute("html", "data-focus-mode") == "on"
    page.keyboard.press("f")
    assert page.get_attribute("html", "data-focus-mode") == "off"


def _verify_font_scale_and_display_prefs_modal(page) -> None:
    page.click('.nav-btn[data-view="study"]')
    page.wait_for_selector("#study-root .jp-prompt")

    # Enter Focus Mode so #focus-topbar font-scale group is visible
    page.click("#btn-focus-mode")
    page.wait_for_selector('#focus-topbar .scale-btn[data-font-scale="md"]')

    size_md = float(
        page.locator("#study-root .jp-prompt").first.evaluate(
            "el => parseFloat(getComputedStyle(el).fontSize)"
        )
    )
    page.click('#focus-topbar .scale-btn[data-font-scale="lg"]')
    assert page.get_attribute("html", "data-font-scale") == "lg"
    size_lg = float(
        page.locator("#study-root .jp-prompt").first.evaluate(
            "el => parseFloat(getComputedStyle(el).fontSize)"
        )
    )
    assert size_lg > size_md

    page.click('#focus-topbar .scale-btn[data-font-scale="xl"]')
    assert page.get_attribute("html", "data-font-scale") == "xl"
    size_xl = float(
        page.locator("#study-root .jp-prompt").first.evaluate(
            "el => parseFloat(getComputedStyle(el).fontSize)"
        )
    )
    assert size_xl > size_lg

    page.click('#focus-topbar .scale-btn[data-font-scale="sm"]')
    assert page.get_attribute("html", "data-font-scale") == "sm"
    size_sm = float(
        page.locator("#study-root .jp-prompt").first.evaluate(
            "el => parseFloat(getComputedStyle(el).fontSize)"
        )
    )
    assert size_sm < size_md

    page.click("#btn-exit-focus")
    assert page.get_attribute("html", "data-focus-mode") == "off"

    # Open #display-prefs-modal via header button, toggle switch, reset defaults, Esc returns focus
    page.click('.nav-btn[data-view="dashboard"]')
    page.wait_for_selector("#dash-heading")

    page.click("#btn-display-prefs")
    page.wait_for_selector("#display-prefs-modal")
    assert page.get_attribute("#display-prefs-modal", "role") == "dialog"
    assert page.get_attribute("#display-prefs-modal", "aria-modal") == "true"

    target_switch = page.locator('#display-prefs-modal button.pref-switch-btn[data-pref-key="dashboard.scores"]')
    assert target_switch.get_attribute("aria-checked") == "true"
    assert page.is_visible("#dash-scores-section")
    target_switch.click()
    assert target_switch.get_attribute("aria-checked") == "false"
    assert page.is_hidden("#dash-scores-section")

    page.click("#btn-reset-display-prefs")
    assert page.is_visible("#dash-scores-section")
    assert page.get_attribute("html", "data-font-scale") == "md"
    assert page.get_attribute("html", "data-hide-ruby") == "0"

    page.keyboard.press("Escape")
    assert page.is_hidden("#display-prefs-backdrop")
    active_id = page.evaluate("document.activeElement ? document.activeElement.id : ''")
    assert active_id == "btn-display-prefs"

    # Keyboard shortcut V opens #display-prefs-modal
    page.keyboard.press("v")
    assert page.is_visible("#display-prefs-modal")
    page.keyboard.press("Escape")
    assert page.is_hidden("#display-prefs-backdrop")


def _verify_dashboard_visibility_and_reload(page) -> None:
    page.click('.nav-btn[data-view="dashboard"]')
    page.wait_for_selector("#dash-scores-section")
    assert page.is_visible("#dash-scores-section")
    assert page.is_visible("#dash-topics-section")

    page.click('[data-dash-toggle="scores"]')
    assert page.locator("#dash-scores-section").count() == 0 or page.is_hidden("#dash-scores-section")
    page.click('[data-dash-toggle="topics"]')
    assert page.locator("#dash-topics-section").count() == 0 or page.is_hidden("#dash-topics-section")
    assert page.is_visible("#btn-dash-restore-all")

    page.reload(wait_until="networkidle")
    page.wait_for_selector("#dash-heading")
    assert page.locator("#dash-scores-section").count() == 0 or page.is_hidden("#dash-scores-section")
    assert page.locator("#dash-topics-section").count() == 0 or page.is_hidden("#dash-topics-section")

    page.click("#btn-dash-restore-all")
    page.wait_for_selector("#dash-scores-section")
    assert page.is_visible("#dash-scores-section")
    assert page.is_visible("#dash-topics-section")
    assert page.locator(".topic-grid .topic-card").count() == 12


def _verify_grammar_book_reader(page) -> None:
    page.click('.nav-btn[data-view="grammar"]')
    page.wait_for_selector("#grammar-heading")
    page.wait_for_selector("#grammar-library-results .grammar-point-card")

    page.click('[data-grammar-layout="reader"]')
    page.wait_for_selector(".grammar-reader-stage .grammar-lesson-block")
    assert page.locator("#grammar-library-results:visible").count() == 0
    assert page.is_visible("#btn-reader-next")
    assert page.is_visible("#reader-point-sel")

    code_1 = page.locator("#reader-point-sel").input_value()
    page.click("#btn-reader-next")
    page.wait_for_function(
        f"() => {{ const s = document.querySelector('#reader-point-sel'); return s && s.value !== {code_1!r}; }}"
    )
    code_2 = page.locator("#reader-point-sel").input_value()
    assert code_2 != code_1

    # Blur select before pressing keyboard navigation '[' / ']'
    page.evaluate("if (document.activeElement) document.activeElement.blur();")
    page.keyboard.press("]")
    page.wait_for_function(
        f"() => {{ const s = document.querySelector('#reader-point-sel'); return s && s.value !== {code_2!r}; }}"
    )
    code_3 = page.locator("#reader-point-sel").input_value()
    assert code_3 != code_2

    # Self-masking Vietnamese translations in examples
    page.click('[data-grammar-vis="maskExampleVi"]')
    page.wait_for_selector(".grammar-reader-stage .self-mask-btn[data-reveal-ex]")
    masked_before = page.locator(".grammar-reader-stage .self-mask-btn[data-reveal-ex]").count()
    assert masked_before >= 1
    page.locator(".grammar-reader-stage .self-mask-btn[data-reveal-ex]").first.click()
    masked_after = page.locator(".grammar-reader-stage .self-mask-btn[data-reveal-ex]").count()
    assert masked_after == masked_before - 1

    # Toggle lesson section [3] Confusable Pairs off and on
    assert page.is_visible('[data-lesson-box="sec3Confusable"]')
    page.click('[data-lesson-sec="sec3Confusable"]')
    assert page.is_hidden('[data-lesson-box="sec3Confusable"]')
    page.click('[data-lesson-sec="sec3Confusable"]')
    assert page.is_visible('[data-lesson-box="sec3Confusable"]')


def _verify_vocab_focused_views(page) -> None:
    page.click('.subnav-btn[data-grammar-tab="vocab"]')
    page.wait_for_selector("#vocab-results-container table.data-table tbody tr")

    page.click('[data-vocab-layout="cards"]')
    page.wait_for_selector(".vocab-cards-grid .vocab-focus-card")
    assert page.locator(".vocab-cards-grid .vocab-focus-card").count() >= 10

    page.click('[data-vocab-layout="deck"]')
    page.wait_for_selector(".vocab-deck-stage .vocab-focus-word")
    first_word = page.locator(".vocab-deck-stage .vocab-focus-word").text_content()

    # Mask reading and test click-to-reveal
    page.click('[data-vocab-vis="showReading"]')
    page.wait_for_selector(".vocab-deck-stage .self-mask-btn")
    mask_count_before = page.locator(".vocab-deck-stage .self-mask-btn").count()
    page.locator(".vocab-deck-stage .self-mask-btn").first.click()
    mask_count_after = page.locator(".vocab-deck-stage .self-mask-btn").count()
    assert mask_count_after == mask_count_before - 1

    page.click("#btn-vocab-next")
    second_word = page.locator(".vocab-deck-stage .vocab-focus-word").text_content()
    assert second_word != first_word

    # Restore showReading for cleanliness
    page.click('[data-vocab-vis="showReading"]')


def _verify_study_focus_and_dokkai_vertical(page) -> None:
    page.click('.nav-btn[data-view="study"]')
    page.wait_for_selector("#study-unit-sel")
    page.select_option("#study-unit-sel", "MU-11")
    page.select_option("#study-mode-sel", "variant")
    page.wait_for_selector(".dokkai-split .passage-sentence.selectable")

    # Zero-Leakage before submit
    assert page.locator(".grammar-breakdown-box").count() == 0
    assert page.locator("[data-grammar-breakdown]").count() == 0

    # Pick evidence sentence and option before layout switch to confirm state preservation
    page.locator(".passage-sentence.selectable").first.click()
    page.locator(".options-list .option-btn").first.click()
    assert page.locator(".passage-sentence.selected-evidence").count() == 1
    assert page.locator(".options-list .option-btn.selected").count() == 1

    # Switch Dokkai to vertical 1-column reading layout
    page.click('[data-dokkai-layout="vertical"]')
    page.wait_for_selector(".dokkai-split.dokkai-vertical")
    assert page.locator(".passage-sentence.selected-evidence").count() == 1
    assert page.locator(".options-list .option-btn.selected").count() == 1

    # Switch Study to Focus layout (hides toolbar cleanly)
    page.click('[data-study-layout="focus"]')
    page.wait_for_selector(".study-focus-stage")
    assert page.locator("#study-unit-sel:visible").count() == 0
    assert page.locator(".passage-sentence.selected-evidence").count() == 1
    assert page.locator(".options-list .option-btn.selected").count() == 1
    assert page.locator(".grammar-breakdown-box").count() == 0

    # Toggle Furigana / Ruby aid off and back on
    assert page.locator("#study-root ruby rt").count() > 0
    page.click('[data-study-vis="showRubyAid"]')
    assert page.get_attribute("html", "data-hide-ruby") == "1"
    rt_displays = page.evaluate(
        "Array.from(document.querySelectorAll('#study-root ruby rt')).map(el => getComputedStyle(el).display)"
    )
    assert rt_displays and all(d == "none" for d in rt_displays)

    page.click('[data-study-vis="showRubyAid"]')
    assert page.get_attribute("html", "data-hide-ruby") == "0"

    # Submit and test post-submit translation toggle
    page.click("#btn-submit-study")
    page.wait_for_selector("#btn-next-study")
    assert page.locator(".grammar-breakdown-box").count() >= 1

    trans_btn = page.locator('[data-study-fb="showTranslation"]')
    trans_boxes = page.locator('[data-study-fb-box="translation"], [data-study-fb-box="passage-translation"]')
    if trans_btn.count() > 0:
        assert trans_boxes.count() >= 1
        trans_btn.click()
        assert trans_boxes.count() == 0
        trans_btn.click()
        assert trans_boxes.count() >= 1

    # Restore standard study layout
    page.click('[data-study-layout="standard"]')
    page.wait_for_selector("#study-unit-sel")


def _verify_exam_single_question_mode(page) -> None:
    page.click('.nav-btn[data-view="exam"]')
    page.wait_for_selector("#btn-start-exam")
    page.select_option("#exam-count-sel", "2")
    page.click("#btn-start-exam")
    page.wait_for_selector("#btn-submit-exam")

    total_cards = page.locator("#exam-root > .stack-md > .card").count()
    assert total_cards >= 2

    page.click('[data-exam-layout="single"]')
    page.wait_for_selector(".exam-single-nav")
    assert page.locator("#exam-root > .stack-md > .card").count() == total_cards
    assert page.locator("#exam-root > .stack-md > .card:visible").count() == 1

    page.click('[data-exam-vis="showPalette"]')
    page.wait_for_selector(".exam-palette .exam-palette-btn")
    assert page.locator(".exam-palette .exam-palette-btn").count() == total_cards

    assert page.is_visible("#exam-timer")
    page.click('[data-exam-vis="showTimer"]')
    assert page.is_hidden("#exam-timer")

    # Answer all questions sequentially in single-question mode and submit
    for idx in range(total_cards):
        visible_card = page.locator("#exam-root > .stack-md > .card:visible")
        assert visible_card.count() == 1
        chips = visible_card.locator(".chunk-chip")
        if chips.count() == 4:
            for ci in range(4):
                chips.nth(ci).click()
        else:
            visible_card.locator(".option-btn").first.click()
        if idx < total_cards - 1:
            page.click("#btn-exam-next")

    page.click("#btn-submit-exam")
    page.wait_for_selector("#btn-exam-reset")
    assert "Kết quả Phòng thi Thực chiến" in page.locator("#exam-root").text_content()


def _verify_notebook_toggles(page) -> None:
    page.click('.nav-btn[data-view="notebook"]')
    page.wait_for_selector("#excel-upload-form")
    assert page.is_visible("#nb-workbooks-card")

    page.click('[data-nb-vis="showWorkbooks"]')
    assert page.is_hidden("#nb-workbooks-card")
    assert page.is_visible("#btn-nb-restore-all")

    page.click("#btn-nb-restore-all")
    assert page.is_visible("#nb-workbooks-card")


def _verify_mobile_focus_views(page) -> None:
    page.set_viewport_size({"width": 390, "height": 844})
    _assert_no_horizontal_overflow(page, "mobile_header_before_focus")
    page.click("#btn-focus-mode")
    assert page.get_attribute("html", "data-focus-mode") == "on"
    assert page.is_visible("#focus-topbar")
    _assert_no_horizontal_overflow(page, "mobile_focus_topbar_initial")

    for theme in ("light", "dark"):
        if theme == "dark":
            page.click("#btn-focus-theme")
            assert page.get_attribute("html", "data-theme") == "dark"

        # Grammar Reader
        page.click('#focus-topbar [data-focus-view="grammar"]')
        page.wait_for_selector("#grammar-heading")
        page.click('.subnav-btn[data-grammar-tab="library"]')
        page.click('[data-grammar-layout="reader"]')
        page.wait_for_selector(".grammar-reader-stage .grammar-lesson-block")
        _assert_no_horizontal_overflow(page, f"mobile_{theme}_grammar_reader")

        # Vocab Deck
        page.click('.subnav-btn[data-grammar-tab="vocab"]')
        page.click('[data-vocab-layout="deck"]')
        page.wait_for_selector(".vocab-deck-stage .vocab-focus-word")
        _assert_no_horizontal_overflow(page, f"mobile_{theme}_vocab_deck")

        # Study Focus
        page.click('#focus-topbar [data-focus-view="study"]')
        page.wait_for_selector("#study-root")
        page.click('[data-study-layout="focus"]')
        page.wait_for_selector(".study-focus-stage")
        _assert_no_horizontal_overflow(page, f"mobile_{theme}_study_focus")


def test_focus_views_desktop_and_mobile_e2e(isolated_db):
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

            page.goto(base_url, wait_until="networkidle")
            page.wait_for_selector("#dash-heading")

            _verify_desktop_header_and_focus_mode(page)
            _verify_font_scale_and_display_prefs_modal(page)
            _verify_dashboard_visibility_and_reload(page)
            _verify_grammar_book_reader(page)
            _verify_vocab_focused_views(page)
            _verify_study_focus_and_dokkai_vertical(page)
            _verify_exam_single_question_mode(page)
            _verify_notebook_toggles(page)
            _verify_mobile_focus_views(page)

            browser.close()

        assert console_errors == [], f"Console errors: {console_errors}"
        assert page_errors == [], f"Page errors: {page_errors}"
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()
