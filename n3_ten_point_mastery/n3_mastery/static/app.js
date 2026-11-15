/* Pure Vanilla JS SPA for JLPT N3 10/10 Mastery System */
"use strict";

const UI_PREFS_STORAGE_KEY = "n3_ui_preferences_v1";
const VALID_FONT_SCALES = ["sm", "md", "lg", "xl"];

function createDefaultUiState() {
  return {
    focusMode: false,
    revealedExamples: {},
    revealedVocab: {},
    fontScale: "md",
    dashboard: {
      quickGuide: true,
      scores: true,
      grammarCard: true,
      pace: true,
      topics: true,
      sectionTable: true,
    },
    grammar: {
      showOverview: true,
      libraryLayout: "split",
      showFilter: true,
      showListPane: true,
      maskExampleVi: false,
      lessonSections: {
        sec1Formula: true,
        sec2Meaning: true,
        sec3Confusable: true,
        sec4Examples: true,
        sec5LinkedQuestions: true,
      },
      drillShowFilter: true,
      drillFeedback: {
        showTranslation: true,
        showExplanation: true,
        showDiagnostics: true,
      },
      vocabLayout: "table",
      vocabDeckIndex: 0,
      vocabFields: {
        showFilter: true,
        showReading: true,
        showRadical: true,
        showMeaning: true,
        showSource: true,
      },
    },
    study: {
      layout: "standard",
      dokkaiLayout: "split",
      showToolbar: true,
      showStepHint: true,
      showGlossaryAid: true,
      showRubyAid: true,
      feedback: {
        showTranslation: true,
        showExplanation: true,
        showGrammarAnatomy: true,
        showCompanion: true,
      },
      bridge: {
        showExplanation: true,
        showExamples: true,
        showQuickCheck: true,
      },
    },
    exam: {
      layout: "all",
      currentIndex: 0,
      showTimer: true,
      showPalette: false,
    },
    notebook: {
      showErrors: true,
      showUploader: true,
      showWorkbooks: true,
    },
  };
}

const state = {
  activeView: "dashboard",
  theme: "light",
  hideQuickGuide: false,
  grammarModalDetail: null,
  ui: createDefaultUiState(),
  dashboard: null,
  study: {
    unitCode: "MU-01",
    mode: "mixed",
    showBridge: false,
    bridgeData: null,
    quickCheckAnswers: {},
    item: null,
    sessionSeed: "seed-" + Math.random().toString(36).slice(2, 8),
    selectedOption: null,
    starSlots: [null, null, null, null],
    evidenceIndices: [],
    usedHint: false,
    hintText: null,
    startedAt: 0,
    result: null,
  },
  exam: {
    active: false,
    examData: null,
    answers: {},
    startedAt: 0,
    timerId: null,
    elapsedSec: 0,
    result: null,
  },
  notebook: {
    errors: null,
    workbooks: null,
    importResult: null,
  },
  grammar: {
    subtab: "library",
    overview: null,
    overviewError: null,
    library: {
      scope: "all",
      level: "ALL",
      category: "",
      state: "",
      q: "",
      points: [],
      categories: [],
      total: 0,
      loaded: false,
      loading: false,
      error: null,
      selectedCode: null,
      detail: null,
      detailLoading: false,
      detailError: null,
    },
    drill: {
      drillType: "mixed",
      scope: "all",
      level: "ALL",
      grammarCode: null,
      sessionSeed: "gd-" + Math.random().toString(36).slice(2, 8),
      item: null,
      emptyReason: null,
      loading: false,
      error: null,
      selectedOption: null,
      startedAt: 0,
      result: null,
    },
    vocab: {
      scope: "all",
      level: "ALL",
      q: "",
      items: [],
      total: 0,
      loaded: false,
      loading: false,
      error: null,
    },
    importResult: null,
  },
};

function mergeBoolSection(target, source) {
  if (!source || typeof source !== "object") return;
  for (const key of Object.keys(target)) {
    if (typeof source[key] === "boolean") {
      target[key] = source[key];
    }
  }
}

function loadUiPreferences() {
  const ui = createDefaultUiState();
  try {
    const raw = localStorage.getItem(UI_PREFS_STORAGE_KEY);
    if (!raw) {
      state.ui = ui;
      return;
    }
    const parsed = JSON.parse(raw);
    if (!parsed || typeof parsed !== "object") {
      state.ui = ui;
      return;
    }
    if (VALID_FONT_SCALES.includes(parsed.fontScale)) {
      ui.fontScale = parsed.fontScale;
    }
    mergeBoolSection(ui.dashboard, parsed.dashboard);
    if (parsed.grammar && typeof parsed.grammar === "object") {
      const g = parsed.grammar;
      if (typeof g.showOverview === "boolean") ui.grammar.showOverview = g.showOverview;
      if (g.libraryLayout === "split" || g.libraryLayout === "reader") ui.grammar.libraryLayout = g.libraryLayout;
      if (typeof g.showFilter === "boolean") ui.grammar.showFilter = g.showFilter;
      if (typeof g.showListPane === "boolean") ui.grammar.showListPane = g.showListPane;
      if (typeof g.maskExampleVi === "boolean") ui.grammar.maskExampleVi = g.maskExampleVi;
      if (typeof g.drillShowFilter === "boolean") ui.grammar.drillShowFilter = g.drillShowFilter;
      if (g.vocabLayout === "table" || g.vocabLayout === "cards" || g.vocabLayout === "deck") {
        ui.grammar.vocabLayout = g.vocabLayout;
      }
      mergeBoolSection(ui.grammar.lessonSections, g.lessonSections);
      mergeBoolSection(ui.grammar.drillFeedback, g.drillFeedback);
      mergeBoolSection(ui.grammar.vocabFields, g.vocabFields);
    }
    if (parsed.study && typeof parsed.study === "object") {
      const s = parsed.study;
      if (s.layout === "standard" || s.layout === "focus") ui.study.layout = s.layout;
      if (s.dokkaiLayout === "split" || s.dokkaiLayout === "vertical") ui.study.dokkaiLayout = s.dokkaiLayout;
      if (typeof s.showToolbar === "boolean") ui.study.showToolbar = s.showToolbar;
      if (typeof s.showStepHint === "boolean") ui.study.showStepHint = s.showStepHint;
      if (typeof s.showGlossaryAid === "boolean") ui.study.showGlossaryAid = s.showGlossaryAid;
      if (typeof s.showRubyAid === "boolean") ui.study.showRubyAid = s.showRubyAid;
      mergeBoolSection(ui.study.feedback, s.feedback);
      mergeBoolSection(ui.study.bridge, s.bridge);
    }
    if (parsed.exam && typeof parsed.exam === "object") {
      const ex = parsed.exam;
      if (ex.layout === "all" || ex.layout === "single") ui.exam.layout = ex.layout;
      if (typeof ex.showTimer === "boolean") ui.exam.showTimer = ex.showTimer;
      if (typeof ex.showPalette === "boolean") ui.exam.showPalette = ex.showPalette;
    }
    mergeBoolSection(ui.notebook, parsed.notebook);
  } catch (e) {
    // ignore storage or JSON parse error and fall back to defaults
  }
  state.ui = ui;
}

function saveUiPreferences() {
  const ui = state.ui;
  const persisted = {
    fontScale: ui.fontScale,
    dashboard: { ...ui.dashboard },
    grammar: {
      showOverview: ui.grammar.showOverview,
      libraryLayout: ui.grammar.libraryLayout,
      showFilter: ui.grammar.showFilter,
      showListPane: ui.grammar.showListPane,
      maskExampleVi: ui.grammar.maskExampleVi,
      lessonSections: { ...ui.grammar.lessonSections },
      drillShowFilter: ui.grammar.drillShowFilter,
      drillFeedback: { ...ui.grammar.drillFeedback },
      vocabLayout: ui.grammar.vocabLayout,
      vocabFields: { ...ui.grammar.vocabFields },
    },
    study: {
      layout: ui.study.layout,
      dokkaiLayout: ui.study.dokkaiLayout,
      showToolbar: ui.study.showToolbar,
      showStepHint: ui.study.showStepHint,
      showGlossaryAid: ui.study.showGlossaryAid,
      showRubyAid: ui.study.showRubyAid,
      feedback: { ...ui.study.feedback },
      bridge: { ...ui.study.bridge },
    },
    exam: {
      layout: ui.exam.layout,
      showTimer: ui.exam.showTimer,
      showPalette: ui.exam.showPalette,
    },
    notebook: { ...ui.notebook },
  };
  try {
    localStorage.setItem(UI_PREFS_STORAGE_KEY, JSON.stringify(persisted));
  } catch (e) {
    // ignore storage restriction
  }
}

function getFocusContextLabel() {
  const ui = state.ui;
  if (state.activeView === "dashboard") return "Trang chủ · Xem gọn";
  if (state.activeView === "grammar") {
    const sub = state.grammar.subtab || "library";
    if (sub === "library") {
      return ui.grammar.libraryLayout === "reader" ? "Ngữ pháp · Đọc tập trung từng bài" : "Ngữ pháp · Tra cứu";
    }
    if (sub === "drill") return "Ngữ pháp · Tập trung làm bài";
    if (sub === "vocab") {
      if (ui.grammar.vocabLayout === "deck") return "Từ vựng · Tự dò từng từ";
      if (ui.grammar.vocabLayout === "cards") return "Từ vựng · Thẻ đọc tập trung";
      return "Từ vựng · Tra cứu";
    }
    return "Ngữ pháp · Lộ trình JLPT";
  }
  if (state.activeView === "study") {
    if (state.study.showBridge) return "Làm câu hỏi · Ôn nền N4";
    if (state.study.item && state.study.item.passage && ui.study.dokkaiLayout === "vertical") {
      return "Làm câu hỏi · Đọc hiểu 1 cột";
    }
    return ui.study.layout === "focus" ? "Làm câu hỏi · Tập trung" : "Làm câu hỏi · Luyện tập";
  }
  if (state.activeView === "exam") {
    if (!state.exam.active) return "Thi thử · Chuẩn bị";
    return ui.exam.layout === "single" ? "Thi thử · Tập trung từng câu" : "Thi thử · Phòng thi Thực chiến";
  }
  return "Câu sai & Nạp đề";
}

function applyUiStateToRoot() {
  const html = document.documentElement;
  const ui = state.ui;
  html.setAttribute("data-focus-mode", ui.focusMode ? "on" : "off");
  html.setAttribute("data-font-scale", ui.fontScale || "md");
  html.setAttribute("data-hide-ruby", ui.study.showRubyAid ? "0" : "1");

  const isWideStudy =
    state.activeView === "study" &&
    !state.study.showBridge &&
    Boolean(state.study.item && state.study.item.passage) &&
    ui.study.dokkaiLayout === "split";
  const isWideGrammar =
    state.activeView === "grammar" &&
    state.grammar.subtab === "library" &&
    ui.grammar.libraryLayout === "split" &&
    ui.grammar.showListPane;
  html.setAttribute("data-focus-wide", isWideStudy || isWideGrammar ? "1" : "0");

  const btnFocus = document.getElementById("btn-focus-mode");
  if (btnFocus) btnFocus.setAttribute("aria-pressed", ui.focusMode ? "true" : "false");
  const focusLabel = document.getElementById("focus-mode-label");
  if (focusLabel) focusLabel.textContent = ui.focusMode ? "Thoát Tập trung" : "Tập trung";

  const topbar = document.getElementById("focus-topbar");
  if (topbar) topbar.hidden = !ui.focusMode;

  const ctxLabel = document.getElementById("focus-context-label");
  if (ctxLabel) ctxLabel.textContent = getFocusContextLabel();

  document.querySelectorAll("[data-focus-view]").forEach((btn) => {
    const active = btn.dataset.focusView === state.activeView;
    btn.classList.toggle("active", active);
    if (active) btn.setAttribute("aria-current", "page");
    else btn.removeAttribute("aria-current");
  });

  document.querySelectorAll(".scale-btn[data-font-scale], .scale-btn[data-inline-scale]").forEach((btn) => {
    const val = btn.dataset.fontScale || btn.dataset.inlineScale;
    const isActive = val === ui.fontScale;
    btn.classList.toggle("active", isActive);
    btn.setAttribute("aria-pressed", isActive ? "true" : "false");
  });

  document.querySelectorAll("[data-enter-focus]").forEach((btn) => {
    btn.textContent = ui.focusMode ? "Thoát Tập trung (F)" : "Tập trung toàn màn hình (F)";
  });
}

function setFocusMode(enabled) {
  const next = Boolean(enabled);
  const wasFocusedInHeader = Boolean(document.activeElement && document.activeElement.closest(".app-header"));
  const wasFocusedInTopbar = Boolean(document.activeElement && document.activeElement.closest("#focus-topbar"));
  state.ui.focusMode = next;
  applyUiStateToRoot();
  if (next && wasFocusedInHeader) {
    const exitBtn = document.getElementById("btn-exit-focus");
    if (exitBtn) exitBtn.focus();
  } else if (!next && wasFocusedInTopbar) {
    const enterBtn = document.getElementById("btn-focus-mode");
    if (enterBtn) enterBtn.focus();
  }
}

function setFontScale(scale) {
  if (!VALID_FONT_SCALES.includes(scale)) return;
  state.ui.fontScale = scale;
  saveUiPreferences();
  applyUiStateToRoot();
}

function renderInlineFontScaleGroup() {
  const cur = state.ui.fontScale;
  return `
    <div class="font-scale-group" role="group" aria-label="Cỡ chữ đọc">
      <button type="button" class="scale-btn ${cur === "sm" ? "active" : ""}" data-inline-scale="sm" aria-pressed="${cur === "sm"}">A-</button>
      <button type="button" class="scale-btn ${cur === "md" ? "active" : ""}" data-inline-scale="md" aria-pressed="${cur === "md"}">A</button>
      <button type="button" class="scale-btn ${cur === "lg" ? "active" : ""}" data-inline-scale="lg" aria-pressed="${cur === "lg"}">A+</button>
      <button type="button" class="scale-btn ${cur === "xl" ? "active" : ""}" data-inline-scale="xl" aria-pressed="${cur === "xl"}">A++</button>
    </div>
  `;
}

function bindCommonControlEvents(container) {
  if (!container) return;
  container.querySelectorAll(".scale-btn[data-inline-scale]").forEach((btn) => {
    btn.addEventListener("click", () => setFontScale(btn.dataset.inlineScale));
  });
  container.querySelectorAll("[data-enter-focus]").forEach((btn) => {
    btn.addEventListener("click", () => setFocusMode(!state.ui.focusMode));
  });
}

function renderActiveViewSoft() {
  applyUiStateToRoot();
  if (state.activeView === "dashboard") {
    if (state.dashboard) renderDashboard();
  } else if (state.activeView === "grammar") {
    const strip = document.getElementById("grammar-overview-strip");
    if (strip) strip.hidden = !state.ui.grammar.showOverview;
    if (state.grammar.overview) renderGrammarShell();
  } else if (state.activeView === "study") {
    if (state.study.showBridge ? state.study.bridgeData : state.study.item !== undefined) {
      renderStudyView();
    }
  } else if (state.activeView === "exam") {
    renderExamShell();
  } else if (state.activeView === "notebook") {
    if (state.notebook.errors !== null) renderNotebookView();
  }
  const gramBd = document.getElementById("grammar-modal-backdrop");
  if (gramBd && !gramBd.hidden && state.grammarModalDetail) {
    const bodyEl = document.getElementById("grammar-modal-body");
    if (bodyEl) {
      const prevTop = bodyEl.scrollTop;
      bodyEl.innerHTML = renderGrammarLessonHtml(state.grammarModalDetail, { inModal: true });
      bindGrammarLessonActions(bodyEl, { inModal: true });
      bodyEl.scrollTop = prevTop;
    }
  }
}

function escapeHtml(str) {
  if (str === null || str === undefined) return "";
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

function showToast(message, isError) {
  const region = document.getElementById("toast-region");
  if (!region) return;
  const el = document.createElement("div");
  el.className = "toast-item" + (isError ? " error" : "");
  el.textContent = message;
  region.appendChild(el);
  setTimeout(() => {
    if (el.parentNode) el.parentNode.removeChild(el);
  }, 4200);
}

async function apiFetch(url, options) {
  const res = await fetch(url, options || {});
  const text = await res.text();
  let data = null;
  try {
    data = text ? JSON.parse(text) : {};
  } catch (e) {
    throw new Error("Phản hồi không hợp lệ từ máy chủ.");
  }
  if (!res.ok) {
    let msg = `Lỗi HTTP ${res.status}`;
    if (data && data.detail) {
      if (Array.isArray(data.detail)) {
        msg = data.detail.map((d) => (d && d.msg) ? d.msg : String(d)).join("; ");
      } else {
        msg = String(data.detail);
      }
    }
    throw new Error(msg);
  }
  return data;
}

function renderSkeleton(linesCount) {
  let lines = "";
  for (let i = 0; i < (linesCount || 4); i++) {
    const w = i === 0 ? "w-40 h-lg" : i % 2 === 1 ? "w-100" : "w-70";
    lines += `<div class="skeleton-line ${w}"></div>`;
  }
  return `<div class="skeleton-card" aria-busy="true" aria-label="Đang nạp dữ liệu">${lines}</div>`;
}

function renderEmptyState(title, message, ctaLabel, ctaId) {
  return `
    <div class="state-panel">
      <h2 class="card-title">${escapeHtml(title)}</h2>
      <p class="muted break-anywhere">${escapeHtml(message)}</p>
      ${ctaLabel ? `<button type="button" id="${escapeHtml(ctaId)}" class="btn-primary">${escapeHtml(ctaLabel)}</button>` : ""}
    </div>
  `;
}

function renderErrorState(message, retryId) {
  return `
    <div class="state-panel state-error" role="alert">
      <h2 class="card-title">Không thể nạp dữ liệu</h2>
      <p class="break-anywhere">${escapeHtml(message)}</p>
      <button type="button" id="${escapeHtml(retryId)}" class="btn-primary">Thử lại</button>
    </div>
  `;
}

/* Theme Handling */
function applyTheme(themeName) {
  const resolved = themeName === "dark" ? "dark" : "light";
  state.theme = resolved;
  document.documentElement.setAttribute("data-theme", resolved);
  try {
    localStorage.setItem("n3_mastery_theme", resolved);
  } catch (e) {
    // ignore storage restriction
  }
  const label = document.getElementById("theme-toggle-label");
  if (label) {
    label.textContent = resolved === "dark" ? "Giao diện Sáng" : "Giao diện Tối";
  }
  const prefsBd = document.getElementById("display-prefs-backdrop");
  if (prefsBd && !prefsBd.hidden) {
    renderDisplayPrefsModalBody();
  }
}

function toggleTheme() {
  applyTheme(state.theme === "light" ? "dark" : "light");
}

function setQuickGuidePreference(hidden) {
  state.hideQuickGuide = Boolean(hidden);
  try {
    localStorage.setItem("n3_hide_quick_guide", state.hideQuickGuide ? "1" : "0");
  } catch (e) {
    // ignore storage restriction
  }
}

function formatMasteryStateVi(fsrs) {
  if (!fsrs) return "Chưa học";
  if (fsrs.mastered) return "[OK] Đã thuộc vững";
  if (fsrs.state === "relearning") return "Hay sai · Cần ôn lại";
  if (fsrs.state === "review") return "Đang ôn định kỳ";
  if (fsrs.state === "learning") return "Đang học";
  return "Chưa học";
}

function formatExamTimer(totalSec) {
  const s = Math.max(0, Math.floor(Number(totalSec) || 0));
  const m = Math.floor(s / 60);
  const rem = s % 60;
  return `${String(m).padStart(2, "0")}:${String(rem).padStart(2, "0")}`;
}

function formatWorkbookLayoutVi(layoutType) {
  const map = {
    comprehensive_3_part: "Đề tổng hợp 3 phần",
    vocab_35: "Đề Từ vựng & Chữ Hán",
    grammar_cloze_3_passages: "Đề Ngữ pháp đoạn văn",
    dokkai_short: "Đề Đọc hiểu đoạn ngắn",
    dokkai_info: "Đề Đọc tìm thông tin",
  };
  return map[layoutType] || layoutType || "Khác";
}

/* Accessible Modals with Focus Trap */
let lastFocusedBeforeModal = null;
let lastFocusedBeforeGrammarModal = null;
let lastFocusedBeforePrefsModal = null;

function restoreFocusSafely(el, fallbackIds) {
  if (el && typeof el.focus === "function" && el.isConnected && el.offsetParent !== null) {
    el.focus();
    return;
  }
  for (const id of (fallbackIds || [])) {
    const fb = document.getElementById(id);
    if (fb && fb.offsetParent !== null) {
      fb.focus();
      return;
    }
  }
}

function isAnyModalOpen() {
  const helpBd = document.getElementById("help-modal-backdrop");
  const gramBd = document.getElementById("grammar-modal-backdrop");
  const prefsBd = document.getElementById("display-prefs-backdrop");
  return (helpBd && !helpBd.hidden) || (gramBd && !gramBd.hidden) || (prefsBd && !prefsBd.hidden);
}

function getActiveModalPair() {
  const prefsBd = document.getElementById("display-prefs-backdrop");
  const prefsModal = document.getElementById("display-prefs-modal");
  if (prefsBd && !prefsBd.hidden && prefsModal) {
    return { backdrop: prefsBd, modal: prefsModal, closeFn: closeDisplayPrefsModal };
  }
  const gramBd = document.getElementById("grammar-modal-backdrop");
  const gramModal = document.getElementById("grammar-modal");
  if (gramBd && !gramBd.hidden && gramModal) {
    return { backdrop: gramBd, modal: gramModal, closeFn: closeGrammarModal };
  }
  const helpBd = document.getElementById("help-modal-backdrop");
  const helpModal = document.getElementById("help-modal");
  if (helpBd && !helpBd.hidden && helpModal) {
    return { backdrop: helpBd, modal: helpModal, closeFn: closeHelpModal };
  }
  return null;
}

function openHelpModal() {
  const backdrop = document.getElementById("help-modal-backdrop");
  const modal = document.getElementById("help-modal");
  if (!backdrop || !modal) return;
  lastFocusedBeforeModal = document.activeElement;
  backdrop.hidden = false;
  const closeBtn = document.getElementById("btn-close-help");
  if (closeBtn) closeBtn.focus();
}

function closeHelpModal() {
  const backdrop = document.getElementById("help-modal-backdrop");
  if (!backdrop || backdrop.hidden) return;
  backdrop.hidden = true;
  restoreFocusSafely(lastFocusedBeforeModal, ["btn-help-modal", "btn-exit-focus"]);
}

function renderPrefSwitchRow(prefKey, title, desc, checked) {
  return `
    <div class="pref-row">
      <div class="pref-row-info">
        <strong>${escapeHtml(title)}</strong>
        ${desc ? `<span class="muted">${escapeHtml(desc)}</span>` : ""}
      </div>
      <button type="button" role="switch" class="pref-switch-btn" aria-checked="${checked ? "true" : "false"}" aria-label="${escapeHtml(title)}" data-pref-key="${escapeHtml(prefKey)}"></button>
    </div>
  `;
}

function togglePrefByKey(prefKey) {
  const ui = state.ui;
  if (prefKey === "__focusMode") {
    setFocusMode(!ui.focusMode);
    return;
  }
  if (prefKey === "__darkTheme") {
    toggleTheme();
    return;
  }
  if (prefKey === "__grammarReader") {
    ui.grammar.libraryLayout = ui.grammar.libraryLayout === "reader" ? "split" : "reader";
  } else if (prefKey === "__studyFocus") {
    ui.study.layout = ui.study.layout === "focus" ? "standard" : "focus";
  } else if (prefKey === "__dokkaiVertical") {
    ui.study.dokkaiLayout = ui.study.dokkaiLayout === "vertical" ? "split" : "vertical";
  } else if (prefKey === "__examSingle") {
    ui.exam.layout = ui.exam.layout === "single" ? "all" : "single";
  } else {
    const parts = prefKey.split(".");
    let cur = ui;
    for (let i = 0; i < parts.length - 1; i++) {
      if (!cur || typeof cur !== "object") return;
      cur = cur[parts[i]];
    }
    const last = parts[parts.length - 1];
    if (cur && typeof cur[last] === "boolean") {
      cur[last] = !cur[last];
    }
  }
  saveUiPreferences();
  renderActiveViewSoft();
}

function renderDisplayPrefsModalBody(preserveFocusKey) {
  const body = document.getElementById("display-prefs-body");
  if (!body) return;
  const ui = state.ui;
  const prevScroll = body.scrollTop;

  body.innerHTML = `
    <div class="pref-group">
      <h3 class="pref-group-title">Toàn cục &amp; Chế độ đọc</h3>
      ${renderPrefSwitchRow("__focusMode", "Chế độ Tập trung (Phím F)", "Ẩn thanh điều hướng lớn trên cùng, giữ lại thanh gọn để đọc và làm bài.", ui.focusMode)}
      <div class="pref-row">
        <div class="pref-row-info">
          <strong>Cỡ chữ tiếng Nhật</strong>
          <span class="muted">Phóng to hoặc thu nhỏ đề bài, đoạn văn đọc hiểu, ví dụ và Kanji.</span>
        </div>
        ${renderInlineFontScaleGroup()}
      </div>
      ${renderPrefSwitchRow("__darkTheme", "Giao diện Tối (Phím T)", "Chuyển nhanh giữa Nền Sáng ban ngày và Nền Tối dịu mắt.", state.theme === "dark")}
      ${renderPrefSwitchRow("study.showRubyAid", "Hiện phiên âm chữ Hán (Furigana)", "Bật hoặc tắt các chữ Hiragana nhỏ bên trên chữ Hán ở phần Làm câu hỏi (không áp dụng khi Thi thử).", ui.study.showRubyAid)}
    </div>

    <div class="pref-group">
      <h3 class="pref-group-title">Trang chủ</h3>
      ${renderPrefSwitchRow("dashboard.quickGuide", "Hướng dẫn nhanh 3 bước", "Khối giới thiệu trình tự ôn tập cho người mới.", ui.dashboard.quickGuide)}
      ${renderPrefSwitchRow("dashboard.scores", "Bảng điểm &amp; Nhận xét", "Điểm Làm Đề Gốc, Điểm Hiểu Thật và nhận xét trung thực.", ui.dashboard.scores)}
      ${renderPrefSwitchRow("dashboard.grammarCard", "Kho Ngữ pháp &amp; Từ vựng", "Thống kê tiến độ N5–N2 và nút mở nhanh Thư viện.", ui.dashboard.grammarCard)}
      ${renderPrefSwitchRow("dashboard.pace", "Lịch ôn tập theo thời gian", "Tính số phút và mục tiêu bài học mỗi ngày.", ui.dashboard.pace)}
      ${renderPrefSwitchRow("dashboard.topics", "12 Chủ đề Học tập", "Lưới 12 chủ đề từ MU-01 đến MU-12.", ui.dashboard.topics)}
      ${renderPrefSwitchRow("dashboard.sectionTable", "Bảng điểm chi tiết theo phần thi", "Bảng thu gọn cho Từ vựng, Ngữ pháp và Đọc hiểu.", ui.dashboard.sectionTable)}
    </div>

    <div class="pref-group">
      <h3 class="pref-group-title">Ngữ pháp &amp; Từ vựng</h3>
      ${renderPrefSwitchRow("grammar.showOverview", "Thống kê nhanh đầu trang", "4 ô số tổng mẫu, đề cuối kì, mở rộng JLPT và tiến độ.", ui.grammar.showOverview)}
      ${renderPrefSwitchRow("__grammarReader", "Đọc tập trung từng bài (Ngữ pháp)", "Ẩn danh sách bên trái, chỉ giữ khung đọc chính giữa như trang sách.", ui.grammar.libraryLayout === "reader")}
      ${renderPrefSwitchRow("grammar.showFilter", "Thanh bộ lọc Tra cứu Ngữ pháp", "Lọc theo nguồn, cấp độ JLPT, danh mục và từ khóa.", ui.grammar.showFilter)}
      ${renderPrefSwitchRow("grammar.showListPane", "Danh sách mẫu bên trái (khi chia 2 cột)", "Tạm ẩn danh sách trái để mở rộng bài học đang đọc.", ui.grammar.showListPane)}
      ${renderPrefSwitchRow("grammar.maskExampleVi", "Che nghĩa tiếng Việt ở Ví dụ để tự dò", "Ẩn nghĩa tiếng Việt và ghi chú, bấm để mở từng câu khi tự kiểm tra.", ui.grammar.maskExampleVi)}
      ${renderPrefSwitchRow("grammar.drillShowFilter", "Thanh bộ lọc Bài tập Ngữ pháp", "Chọn chế độ luyện, nguồn bài học và cấp độ JLPT.", ui.grammar.drillShowFilter)}
      ${renderPrefSwitchRow("grammar.vocabFields.showReading", "Hiện Phiên âm &amp; Hán-Việt (Từ vựng)", "Tắt ở chế độ Thẻ hoặc Từng từ 1 để tự nhớ cách đọc chữ Hán.", ui.grammar.vocabFields.showReading)}
      ${renderPrefSwitchRow("grammar.vocabFields.showRadical", "Hiện Bộ thủ / Ghi chú (Từ vựng)", "Hiển thị phân tích bộ thủ và mẹo nhớ mặt chữ.", ui.grammar.vocabFields.showRadical)}
      ${renderPrefSwitchRow("grammar.vocabFields.showMeaning", "Hiện Nghĩa &amp; Kết hợp từ (Từ vựng)", "Tắt ở chế độ Thẻ hoặc Từng từ 1 để tự kiểm tra nghĩa.", ui.grammar.vocabFields.showMeaning)}
      ${renderPrefSwitchRow("grammar.vocabFields.showSource", "Hiện Nguồn &amp; Câu đề (Từ vựng)", "Hiển thị tên giáo trình và nút nhảy tới câu hỏi.", ui.grammar.vocabFields.showSource)}
    </div>

    <div class="pref-group">
      <h3 class="pref-group-title">Làm câu hỏi</h3>
      ${renderPrefSwitchRow("__studyFocus", "Chế độ Tập trung câu hỏi", "Ẩn thanh chọn chủ đề, nhãn phân loại và khung nhắc để chỉ tập trung vào đề.", ui.study.layout === "focus")}
      ${renderPrefSwitchRow("__dokkaiVertical", "Đọc hiểu 1 cột dọc dễ đọc", "Xếp đoạn văn ở trên và câu hỏi ở dưới theo 1 cột trung tâm.", ui.study.dokkaiLayout === "vertical")}
      ${renderPrefSwitchRow("study.showToolbar", "Thanh chọn chủ đề &amp; cách luyện", "Hiển thị thanh chọn MU-01..MU-12 và nút Ôn nhanh nền N4.", ui.study.showToolbar)}
      ${renderPrefSwitchRow("study.showStepHint", "Hướng dẫn bước làm", "Dòng nhắc phím tắt 1–4, Space hoặc cách làm bài đọc.", ui.study.showStepHint)}
      ${renderPrefSwitchRow("study.showGlossaryAid", "Từ vựng gợi ý dưới đề bài", "Chỉ hiện ở chế độ hỗ trợ học, luôn khóa khi Thi thử.", ui.study.showGlossaryAid)}
      ${renderPrefSwitchRow("study.feedback.showTranslation", "Hiện Dịch nghĩa sau khi nộp", "Hiển thị câu dịch tiếng Việt và dịch mạch đoạn văn.", ui.study.feedback.showTranslation)}
      ${renderPrefSwitchRow("study.feedback.showExplanation", "Hiện Giải thích &amp; Phân tích bẫy sau khi nộp", "Hiển thị phân tích đúng/sai và bảng đối chiếu điều kiện.", ui.study.feedback.showExplanation)}
      ${renderPrefSwitchRow("study.feedback.showGrammarAnatomy", "Hiện Giải phẫu Ngữ pháp sau khi nộp", "Hiển thị các mẫu ngữ pháp xuất hiện trong câu.", ui.study.feedback.showGrammarAnatomy)}
      ${renderPrefSwitchRow("study.feedback.showCompanion", "Hiện Sổ tay Từ vựng / Ngữ pháp sau khi nộp", "Hiển thị ghi chú bổ trợ kèm theo câu.", ui.study.feedback.showCompanion)}
    </div>

    <div class="pref-group">
      <h3 class="pref-group-title">Thi thử</h3>
      ${renderPrefSwitchRow("__examSingle", "Thi tập trung từng câu một", "Chỉ hiện 1 câu hỏi mỗi lần để giảm áp lực nhìn toàn đề.", ui.exam.layout === "single")}
      ${renderPrefSwitchRow("exam.showTimer", "Hiện đồng hồ đếm giờ", "Ẩn đồng hồ khỏi mắt nếu gây căng thẳng, hệ thống vẫn bấm giờ ngầm.", ui.exam.showTimer)}
      ${renderPrefSwitchRow("exam.showPalette", "Hiện bảng chuyển câu nhanh", "Hiện dãy nút số 1..N để nhảy nhanh tới câu bất kỳ.", ui.exam.showPalette)}
    </div>

    <div class="pref-group">
      <h3 class="pref-group-title">Câu sai &amp; Nạp đề</h3>
      ${renderPrefSwitchRow("notebook.showErrors", "Danh sách câu cần làm lại", "Bảng tổng hợp các câu từng làm sai.", ui.notebook.showErrors)}
      ${renderPrefSwitchRow("notebook.showUploader", "Khung nạp thêm tệp Excel (.xlsx)", "Biểu mẫu tải lên bộ đề Excel mới.", ui.notebook.showUploader)}
      ${renderPrefSwitchRow("notebook.showWorkbooks", "Danh sách đề Excel đã nạp", "Bảng thống kê các tệp đã lưu trong cơ sở dữ liệu.", ui.notebook.showWorkbooks)}
    </div>
  `;

  body.scrollTop = prevScroll;
  body.querySelectorAll(".pref-switch-btn[data-pref-key]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const key = btn.dataset.prefKey;
      togglePrefByKey(key);
      renderDisplayPrefsModalBody(key);
    });
  });
  body.querySelectorAll(".scale-btn[data-inline-scale]").forEach((btn) => {
    btn.addEventListener("click", () => {
      setFontScale(btn.dataset.inlineScale);
      renderDisplayPrefsModalBody();
    });
  });

  if (preserveFocusKey) {
    const sameBtn = body.querySelector(`.pref-switch-btn[data-pref-key="${CSS.escape(preserveFocusKey)}"]`);
    if (sameBtn) sameBtn.focus();
  }
}

function openDisplayPrefsModal(triggerEl) {
  const backdrop = document.getElementById("display-prefs-backdrop");
  const modal = document.getElementById("display-prefs-modal");
  if (!backdrop || !modal) return;
  lastFocusedBeforePrefsModal = triggerEl || document.activeElement;
  renderDisplayPrefsModalBody();
  backdrop.hidden = false;
  const closeBtn = document.getElementById("btn-close-display-prefs");
  if (closeBtn) closeBtn.focus();
}

function closeDisplayPrefsModal() {
  const backdrop = document.getElementById("display-prefs-backdrop");
  if (!backdrop || backdrop.hidden) return;
  backdrop.hidden = true;
  restoreFocusSafely(lastFocusedBeforePrefsModal, ["btn-focus-prefs", "btn-display-prefs", "btn-exit-focus"]);
}

function resetAllDisplayPrefs() {
  state.ui = createDefaultUiState();
  setQuickGuidePreference(false);
  saveUiPreferences();
  renderActiveViewSoft();
  renderDisplayPrefsModalBody();
  showToast("Đã khôi phục toàn bộ cài đặt hiển thị mặc định.");
}

async function openGrammarModal(code, triggerEl) {
  const backdrop = document.getElementById("grammar-modal-backdrop");
  const modal = document.getElementById("grammar-modal");
  const titleEl = document.getElementById("grammar-modal-title");
  const bodyEl = document.getElementById("grammar-modal-body");
  if (!backdrop || !modal || !bodyEl) return;

  lastFocusedBeforeGrammarModal = triggerEl || document.activeElement;
  state.grammarModalDetail = null;
  if (titleEl) titleEl.textContent = `Bài học Ngữ pháp: ${code}`;
  bodyEl.innerHTML = renderSkeleton(5);
  backdrop.hidden = false;
  const closeBtn = document.getElementById("btn-close-grammar-modal");
  if (closeBtn) closeBtn.focus();

  try {
    const detail = await apiFetch(`/api/grammar/points/${encodeURIComponent(code)}`);
    state.grammarModalDetail = detail;
    if (titleEl) {
      titleEl.textContent = `[${detail.jlpt_level}] ${detail.pattern} (${detail.code})`;
    }
    bodyEl.innerHTML = renderGrammarLessonHtml(detail, { inModal: true });
    bindGrammarLessonActions(bodyEl, { inModal: true });
  } catch (err) {
    state.grammarModalDetail = null;
    bodyEl.innerHTML = renderErrorState(err.message, "btn-retry-grammar-modal");
    const retryBtn = document.getElementById("btn-retry-grammar-modal");
    if (retryBtn) {
      retryBtn.addEventListener("click", () => openGrammarModal(code, triggerEl));
    }
  }
}

function closeGrammarModal(skipRestoreFocus) {
  const backdrop = document.getElementById("grammar-modal-backdrop");
  if (!backdrop || backdrop.hidden) return;
  backdrop.hidden = true;
  state.grammarModalDetail = null;
  if (!skipRestoreFocus) {
    restoreFocusSafely(lastFocusedBeforeGrammarModal, ["btn-focus-mode", "btn-exit-focus"]);
  }
}

function trapModalFocus(e) {
  const pair = getActiveModalPair();
  if (!pair || e.key !== "Tab") return;
  const focusables = pair.modal.querySelectorAll('button:not(:disabled), [href], input:not(:disabled), select:not(:disabled), textarea:not(:disabled), [tabindex]:not([tabindex="-1"])');
  if (!focusables.length) return;
  const first = focusables[0];
  const last = focusables[focusables.length - 1];
  if (e.shiftKey && document.activeElement === first) {
    e.preventDefault();
    last.focus();
  } else if (!e.shiftKey && document.activeElement === last) {
    e.preventDefault();
    first.focus();
  }
}

/* Navigation */
function switchView(viewName, skipAutoLoad) {
  state.activeView = viewName;
  document.querySelectorAll(".nav-btn").forEach((btn) => {
    const active = btn.dataset.view === viewName;
    btn.classList.toggle("active", active);
    if (active) btn.setAttribute("aria-current", "page");
    else btn.removeAttribute("aria-current");
  });
  document.querySelectorAll(".view-section").forEach((sec) => {
    const active = sec.id === "view-" + viewName;
    sec.hidden = !active;
    sec.classList.toggle("active", active);
  });
  applyUiStateToRoot();

  if (skipAutoLoad) return;
  if (viewName === "dashboard") loadDashboard();
  else if (viewName === "study") ensureStudyLoaded();
  else if (viewName === "exam") renderExamShell();
  else if (viewName === "notebook") loadNotebookView();
  else if (viewName === "grammar") loadGrammarView();
}

function updateNavErrorBadge(count) {
  const badge = document.getElementById("nav-error-badge");
  if (!badge) return;
  if (count > 0) {
    badge.hidden = false;
    badge.textContent = String(count);
  } else {
    badge.hidden = true;
  }
}

/* Dashboard View */
async function loadDashboard() {
  const root = document.getElementById("dashboard-root");
  if (!root) return;
  root.innerHTML = `<div class="stack-md">${renderSkeleton(4)}${renderSkeleton(5)}</div>`;
  try {
    const data = await apiFetch("/api/dashboard");
    state.dashboard = data;
    updateNavErrorBadge(data.error_count || 0);
    renderDashboard();
  } catch (err) {
    root.innerHTML = renderErrorState(err.message, "btn-retry-dash");
    const retryBtn = document.getElementById("btn-retry-dash");
    if (retryBtn) retryBtn.addEventListener("click", loadDashboard);
  }
}

function renderDashboard() {
  const root = document.getElementById("dashboard-root");
  const d = state.dashboard;
  if (!root || !d) return;

  const r = d.readiness;
  const p = d.pace;
  const s = d.settings;
  const uiDash = state.ui.dashboard;
  const hiddenDashCount = Object.values(uiDash).filter((v) => !v).length;

  const origPct = Math.min(100, (r.original_score_10 / 10) * 100);
  const mastPct = Math.min(100, (r.mastery_score_10 / 10) * 100);

  const verdictClass = r.rote_gap_10 >= 2.0 ? "callout-warn" : r.mastered_count === r.total_questions && r.total_questions > 0 ? "callout-success" : "callout-info";

  const secRowsHtml = (r.sections || []).map((sec) => `
    <tr>
      <td><strong>${escapeHtml(sec.label_vi)}</strong></td>
      <td class="tabular-nums">${sec.weight_10.toFixed(1)}</td>
      <td class="tabular-nums">${sec.correct_original}/${sec.total_questions}</td>
      <td class="tabular-nums">${sec.variant_passed_count}/${sec.total_questions}</td>
      <td class="tabular-nums"><strong>${sec.mastered_count}/${sec.total_questions}</strong></td>
      <td class="tabular-nums">${sec.original_score_10.toFixed(2)}</td>
      <td class="tabular-nums"><strong>${sec.mastery_score_10.toFixed(2)}</strong></td>
    </tr>
  `).join("");

  const topicCardsHtml = (d.units || []).map((u) => {
    const pct = u.total_questions > 0 ? Math.round((u.mastered_count / u.total_questions) * 100) : 0;
    const bridgeBadge = u.bridge_completed
      ? `<span class="badge success">[OK] Đã ôn nền N4</span>`
      : `<span class="badge warning">Chưa ôn nền N4</span>`;
    return `
      <div class="topic-card" data-unit-card="${escapeHtml(u.code)}">
        <div class="stack-sm" style="gap: 6px;">
          <div class="row-wrap" style="justify-content: space-between;">
            <span class="badge accent tabular-nums">${escapeHtml(u.code)}</span>
            ${bridgeBadge}
          </div>
          <div style="font-weight: 700; line-height: 1.35;">${escapeHtml(u.title)}</div>
          <div class="muted" style="font-size: 12.5px;">${escapeHtml(u.target_skill)}</div>
        </div>
        <div class="stack-sm" style="gap: 6px; margin-top: 4px;">
          <div class="row-wrap tabular-nums" style="justify-content: space-between; font-size: 12.5px;">
            <span><strong>${u.mastered_count}/${u.total_questions}</strong> câu thuộc vững</span>
            <span class="muted">${pct}%</span>
          </div>
          <div class="progress-track"><div class="progress-fill success" style="width:${pct}%"></div></div>
          <div class="muted tabular-nums" style="font-size: 12px;">
            Đề gốc: ${u.clean_original_count}/${u.total_questions} · Đổi dạng: ${u.variant_passed_count}/${u.total_questions}
          </div>
          <div class="row-wrap" style="margin-top: 2px;">
            <button type="button" class="btn-secondary btn-sm btn-open-bridge" data-unit="${escapeHtml(u.code)}">Ôn nền N4</button>
            <button type="button" class="btn-primary btn-sm btn-open-study" data-unit="${escapeHtml(u.code)}">Làm bài</button>
          </div>
        </div>
      </div>
    `;
  }).join("");

  const quickGuideHiddenAttr = uiDash.quickGuide ? "" : "hidden";
  const quickGuideHtml = state.hideQuickGuide
    ? `
      <div id="quick-guide-card" class="card quick-guide-card row-wrap" style="justify-content: space-between;" ${quickGuideHiddenAttr}>
        <div>
          <strong>Bắt đầu nhanh trong 3 bước:</strong>
          <span class="muted">1. Học Ngữ pháp &amp; Từ vựng -> 2. Làm câu hỏi theo chủ đề -> 3. Sửa câu sai &amp; Thi thử.</span>
        </div>
        <div class="row-wrap">
          <button type="button" id="btn-toggle-quick-guide" class="btn-secondary btn-sm">Mở hướng dẫn</button>
          <button type="button" class="section-collapse-btn" data-dash-hide="quickGuide">Ẩn mục này</button>
        </div>
      </div>
    `
    : `
      <div id="quick-guide-card" class="card quick-guide-card stack-sm" ${quickGuideHiddenAttr}>
        <div class="row-wrap" style="justify-content: space-between;">
          <div>
            <h3 class="card-title" style="margin-bottom: 2px;">Bắt đầu nhanh trong 3 bước</h3>
            <p class="muted" style="margin: 0;">Đi theo thứ tự này để nắm chắc kiến thức trước khi bấm giờ thi thử.</p>
          </div>
          <div class="row-wrap">
            <button type="button" id="btn-toggle-quick-guide" class="btn-secondary btn-sm">Thu gọn</button>
            <button type="button" class="section-collapse-btn" data-dash-hide="quickGuide">Ẩn mục này</button>
          </div>
        </div>
        <div class="guide-steps-grid">
          <div class="guide-step-item">
            <div class="stack-sm" style="gap: 6px;">
              <span class="step-num-badge">Bước 1 · Hiểu bài trước</span>
              <strong>Học Ngữ pháp &amp; Từ vựng</strong>
              <p class="muted" style="margin: 0;">Xem công thức chia thể, nghĩa cốt lõi, cặp dễ nhầm và từ vựng của bộ đề.</p>
            </div>
            <div><button type="button" id="btn-guide-open-grammar" class="btn-secondary btn-sm">Mở Ngữ pháp</button></div>
          </div>
          <div class="guide-step-item">
            <div class="stack-sm" style="gap: 6px;">
              <span class="step-num-badge">Bước 2 · Luyện phản xạ</span>
              <strong>Làm câu hỏi theo Chủ đề</strong>
              <p class="muted" style="margin: 0;">Luyện câu gốc và câu đổi dạng, đọc giải thích chi tiết ngay sau khi nộp.</p>
            </div>
            <div><button type="button" id="btn-guide-open-study" class="btn-primary btn-sm">Vào Làm câu hỏi</button></div>
          </div>
          <div class="guide-step-item">
            <div class="stack-sm" style="gap: 6px;">
              <span class="step-num-badge">Bước 3 · Chốt điểm thật</span>
              <strong>Sửa câu sai &amp; Thi thử</strong>
              <p class="muted" style="margin: 0;">Ôn lại câu hay nhầm và làm bài thi bấm giờ (tắt hết gợi ý như thi thật).</p>
            </div>
            <div class="row-wrap">
              <button type="button" id="btn-guide-open-exam" class="btn-secondary btn-sm">Vào Thi thử</button>
              ${d.error_count > 0 ? `<button type="button" id="btn-guide-open-errors" class="btn-secondary btn-sm">Làm lại ${d.error_count} câu sai</button>` : ""}
            </div>
          </div>
        </div>
      </div>
    `;

  const dashControlBarHtml = `
    <div class="view-control-bar" role="region" aria-label="Tùy chỉnh hiển thị Trang chủ">
      <div class="view-control-group">
        <span class="view-control-label">Hiển thị trên Trang chủ:</span>
        <button type="button" class="vis-chip ${uiDash.quickGuide ? "is-on" : ""}" data-dash-toggle="quickGuide" aria-pressed="${uiDash.quickGuide}">Hướng dẫn nhanh</button>
        <button type="button" class="vis-chip ${uiDash.scores ? "is-on" : ""}" data-dash-toggle="scores" aria-pressed="${uiDash.scores}">Bảng điểm</button>
        <button type="button" class="vis-chip ${uiDash.grammarCard ? "is-on" : ""}" data-dash-toggle="grammarCard" aria-pressed="${uiDash.grammarCard}">Kho Ngữ pháp</button>
        <button type="button" class="vis-chip ${uiDash.pace ? "is-on" : ""}" data-dash-toggle="pace" aria-pressed="${uiDash.pace}">Lịch ôn tập</button>
        <button type="button" class="vis-chip ${uiDash.topics ? "is-on" : ""}" data-dash-toggle="topics" aria-pressed="${uiDash.topics}">12 Chủ đề</button>
        <button type="button" class="vis-chip ${uiDash.sectionTable ? "is-on" : ""}" data-dash-toggle="sectionTable" aria-pressed="${uiDash.sectionTable}">Bảng điểm chi tiết</button>
      </div>
      <div class="view-control-group">
        <button type="button" id="btn-dash-open-prefs" class="btn-secondary btn-sm">Tùy chỉnh nâng cao</button>
      </div>
    </div>
  `;

  const restoreBarHtml = hiddenDashCount > 0
    ? `<div class="hidden-restore-bar" role="status">
         <span>Đang ẩn <strong>${hiddenDashCount}</strong> mục trên Trang chủ.</span>
         <button type="button" id="btn-dash-restore-all" class="btn-secondary btn-sm">Hiện lại tất cả</button>
       </div>`
    : "";

  root.innerHTML = `
    <div class="stack-md">
      <div class="section-header">
        <div>
          <h2 id="dash-heading" class="section-title">Trang chủ Ôn tập &amp; Tiến độ Học tập</h2>
          <p class="muted">Đã sẵn sàng ${r.total_questions} câu hỏi từ ${d.workbooks_count || 7} bộ đề Excel.</p>
        </div>
        <div class="row-wrap">
          <button type="button" id="btn-dash-start-study" class="btn-primary">Làm câu hỏi ngay</button>
        </div>
      </div>

      ${dashControlBarHtml}
      ${quickGuideHtml}

      <div id="dash-scores-section" class="stack-md" ${uiDash.scores ? "" : "hidden"}>
        <div class="grid-2">
          <div class="card">
            <div class="row-wrap" style="justify-content: space-between;">
              <h3 class="card-title">Điểm Làm Đề Gốc</h3>
              <span class="badge accent tabular-nums">${r.attempted_count}/${r.total_questions} câu đã làm</span>
            </div>
            <div class="score-display tabular-nums">
              <span class="score-big">${r.original_score_10.toFixed(2)}</span>
              <span class="score-den">/ 10.00</span>
            </div>
            <div class="progress-track"><div class="progress-fill" style="width:${origPct}%"></div></div>
            <p class="muted" style="margin-top:8px;">Tính trên kết quả làm câu hỏi nguyên bản trong đề Excel (đáp án tự trộn thứ tự mỗi lần làm).</p>
          </div>

          <div class="card">
            <div class="row-wrap" style="justify-content: space-between;">
              <h3 class="card-title">Điểm Hiểu Thật (Không học vẹt)</h3>
              <div class="row-wrap">
                <span class="badge ${r.mastered_count === r.total_questions && r.total_questions > 0 ? "success" : "warning"} tabular-nums">Thuộc vững: ${r.mastered_count}/${r.total_questions}</span>
                <button type="button" class="section-collapse-btn" data-dash-hide="scores">Ẩn mục này</button>
              </div>
            </div>
            <div class="score-display tabular-nums">
              <span class="score-big">${r.mastery_score_10.toFixed(2)}</span>
              <span class="score-den">/ 10.00</span>
            </div>
            <div class="progress-track"><div class="progress-fill success" style="width:${mastPct}%"></div></div>
            <p class="muted" style="margin-top:8px;">Cần làm đúng câu gốc (không xem gợi ý), đúng câu đổi dạng và đúng qua ít nhất 2 lần ôn.</p>
          </div>
        </div>

        <div class="${verdictClass}">${escapeHtml(r.honest_verdict)}</div>
      </div>

      ${renderDashboardGrammarCard(d.grammar_summary, !uiDash.grammarCard)}

      <div id="dash-pace-section" class="card" ${uiDash.pace ? "" : "hidden"}>
        <div class="section-header" style="margin-bottom: 12px;">
          <div>
            <h3 class="card-title">Lịch ôn tập theo thời gian của bạn</h3>
            <p class="muted">Nhập số ngày còn lại và thời gian học mỗi ngày để hệ thống chia khối lượng bài hợp lý.</p>
          </div>
          <div class="row-wrap">
            <span class="badge ${p.is_feasible ? "success" : "danger"}">${escapeHtml(p.status_tag)}</span>
            <button type="button" class="section-collapse-btn" data-dash-hide="pace">Ẩn mục này</button>
          </div>
        </div>

        <form id="pace-form" class="form-row">
          <div class="field">
            <label for="inp-days">Số ngày đến kỳ thi</label>
            <input id="inp-days" type="number" class="input tabular-nums" min="1" max="365" value="${s.days_remaining}">
          </div>
          <div class="field">
            <label for="inp-minutes">Phút học mỗi ngày</label>
            <input id="inp-minutes" type="number" class="input tabular-nums" min="5" max="720" value="${s.daily_minutes}">
          </div>
          <div class="field">
            <label for="sel-scoring">Cách tính điểm /10</label>
            <select id="sel-scoring" class="select">
              <option value="jlpt_weighted" ${s.scoring_mode === "jlpt_weighted" ? "selected" : ""}>Chuẩn thi thật JLPT (3 : 4 : 3)</option>
              <option value="equal_weighted" ${s.scoring_mode === "equal_weighted" ? "selected" : ""}>Tính đều theo ${r.total_questions} câu</option>
            </select>
          </div>
          <button type="submit" class="btn-primary">Lưu lịch học</button>
        </form>

        <div class="row-wrap" style="margin-top: 12px;">
          <span class="badge tabular-nums">Thời gian cần thêm: ${p.remaining_workload_minutes.toFixed(0)} phút</span>
          <span class="badge tabular-nums">Nên học tối thiểu: ${p.required_minutes_per_day.toFixed(1)} phút/ngày</span>
          <span class="badge tabular-nums">Mục tiêu/ngày: ${p.new_units_per_day} bài nền N4 · ${p.questions_per_day} câu gốc · ${p.variants_per_day} câu đổi dạng</span>
        </div>

        ${p.warning_message ? `<div class="callout-danger" style="margin-top: 12px;">${escapeHtml(p.warning_message)}</div>` : ""}
      </div>

      <div id="dash-topics-section" class="card" ${uiDash.topics ? "" : "hidden"}>
        <div class="section-header" style="margin-bottom: 12px;">
          <div>
            <h3 class="card-title" style="margin-bottom: 4px;">12 Chủ đề Học tập (Từ nền N4 lên vững N3)</h3>
            <p class="muted" style="margin: 0;">Nên bấm <strong>Ôn nền N4</strong> trước ở mỗi chủ đề để nắm ngữ pháp cơ bản, sau đó bấm <strong>Làm bài</strong>.</p>
          </div>
          <button type="button" class="section-collapse-btn" data-dash-hide="topics">Ẩn mục này</button>
        </div>
        <div class="topic-grid">${topicCardsHtml}</div>
      </div>

      <details id="dash-sections-details" class="card details-card" ${uiDash.sectionTable ? "" : "hidden"}>
        <summary class="details-summary">Xem bảng điểm chi tiết theo từng phần thi (Từ vựng · Ngữ pháp · Đọc hiểu)</summary>
        <div class="table-scroll-wrap" style="margin-top: 12px;">
          <table class="data-table">
            <thead>
              <tr>
                <th>Phần thi</th>
                <th>Trọng số</th>
                <th>Đề gốc đúng</th>
                <th>Qua Đổi dạng</th>
                <th>Thuộc vững</th>
                <th>Điểm Gốc</th>
                <th>Điểm Hiểu Thật</th>
              </tr>
            </thead>
            <tbody>${secRowsHtml}</tbody>
          </table>
        </div>
      </details>

      ${restoreBarHtml}
    </div>
  `;

  root.querySelectorAll("[data-dash-toggle]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const key = btn.dataset.dashToggle;
      if (key in state.ui.dashboard) {
        state.ui.dashboard[key] = !state.ui.dashboard[key];
        saveUiPreferences();
        renderDashboard();
      }
    });
  });

  root.querySelectorAll("[data-dash-hide]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const key = btn.dataset.dashHide;
      if (key in state.ui.dashboard) {
        state.ui.dashboard[key] = false;
        saveUiPreferences();
        renderDashboard();
      }
    });
  });

  const openPrefsBtn = document.getElementById("btn-dash-open-prefs");
  if (openPrefsBtn) {
    openPrefsBtn.addEventListener("click", () => openDisplayPrefsModal(openPrefsBtn));
  }

  const restoreAllBtn = document.getElementById("btn-dash-restore-all");
  if (restoreAllBtn) {
    restoreAllBtn.addEventListener("click", () => {
      for (const key of Object.keys(state.ui.dashboard)) {
        state.ui.dashboard[key] = true;
      }
      saveUiPreferences();
      renderDashboard();
    });
  }

  document.getElementById("btn-dash-start-study").addEventListener("click", () => {
    state.study.showBridge = false;
    switchView("study");
    loadNextStudyItem();
  });

  const toggleGuideBtn = document.getElementById("btn-toggle-quick-guide");
  if (toggleGuideBtn) {
    toggleGuideBtn.addEventListener("click", () => {
      setQuickGuidePreference(!state.hideQuickGuide);
      renderDashboard();
    });
  }
  const guideGramBtn = document.getElementById("btn-guide-open-grammar");
  if (guideGramBtn) {
    guideGramBtn.addEventListener("click", () => {
      state.grammar.subtab = "library";
      switchView("grammar");
    });
  }
  const guideStudyBtn = document.getElementById("btn-guide-open-study");
  if (guideStudyBtn) {
    guideStudyBtn.addEventListener("click", () => {
      state.study.showBridge = false;
      switchView("study");
      loadNextStudyItem();
    });
  }
  const guideExamBtn = document.getElementById("btn-guide-open-exam");
  if (guideExamBtn) {
    guideExamBtn.addEventListener("click", () => switchView("exam"));
  }
  const guideErrBtn = document.getElementById("btn-guide-open-errors");
  if (guideErrBtn) {
    guideErrBtn.addEventListener("click", () => switchView("notebook"));
  }

  document.getElementById("pace-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const days = parseInt(document.getElementById("inp-days").value, 10);
    const minutes = parseInt(document.getElementById("inp-minutes").value, 10);
    const scoring_mode = document.getElementById("sel-scoring").value;
    if (!Number.isFinite(days) || days < 1 || !Number.isFinite(minutes) || minutes < 5) {
      showToast("Vui lòng nhập số ngày (>= 1) và số phút mỗi ngày (>= 5) hợp lệ.", true);
      return;
    }
    try {
      const updated = await apiFetch("/api/settings", {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ days_remaining: days, daily_minutes: minutes, scoring_mode }),
      });
      state.dashboard.settings = updated.settings;
      state.dashboard.pace = updated.pace;
      state.dashboard.readiness = updated.readiness;
      renderDashboard();
      showToast("Đã lưu lịch học và tính lại khối lượng ôn mỗi ngày.");
    } catch (err) {
      showToast(err.message, true);
    }
  });

  root.querySelectorAll(".btn-open-bridge").forEach((btn) => {
    btn.addEventListener("click", () => {
      state.study.unitCode = btn.dataset.unit;
      state.study.showBridge = true;
      switchView("study");
      loadBridgeUnit(btn.dataset.unit);
    });
  });

  root.querySelectorAll(".btn-open-study").forEach((btn) => {
    btn.addEventListener("click", () => {
      state.study.unitCode = btn.dataset.unit;
      state.study.showBridge = false;
      switchView("study");
      loadNextStudyItem();
    });
  });

  const btnGramLib = document.getElementById("btn-dash-open-grammar-lib");
  if (btnGramLib) {
    btnGramLib.addEventListener("click", () => {
      state.grammar.subtab = "library";
      switchView("grammar");
    });
  }
  const btnGramDrill = document.getElementById("btn-dash-open-grammar-drill");
  if (btnGramDrill) {
    btnGramDrill.addEventListener("click", () => {
      state.grammar.subtab = "drill";
      state.grammar.drill.drillType = "mixed";
      switchView("grammar");
    });
  }
}

/* Study Workspace View */
async function ensureStudyLoaded() {
  if (state.study.showBridge) {
    if (!state.study.bridgeData || state.study.bridgeData.unit.code !== state.study.unitCode) {
      await loadBridgeUnit(state.study.unitCode);
    } else {
      renderStudyView();
    }
    return;
  }
  if (!state.study.item) {
    await loadNextStudyItem();
  } else {
    renderStudyView();
  }
}

async function loadBridgeUnit(unitCode) {
  const root = document.getElementById("study-root");
  state.study.showBridge = true;
  state.study.unitCode = unitCode || "MU-01";
  state.study.quickCheckAnswers = {};
  if (root) root.innerHTML = renderSkeleton(6);
  try {
    const data = await apiFetch(`/api/units/${encodeURIComponent(state.study.unitCode)}`);
    state.study.bridgeData = data;
    renderStudyView();
  } catch (err) {
    if (root) {
      root.innerHTML = renderErrorState(err.message, "btn-retry-bridge");
      document.getElementById("btn-retry-bridge").addEventListener("click", () => loadBridgeUnit(unitCode));
    }
  }
}

async function loadNextStudyItem(customParams) {
  const root = document.getElementById("study-root");
  state.study.showBridge = false;
  state.study.selectedOption = null;
  state.study.starSlots = [null, null, null, null];
  state.study.evidenceIndices = [];
  state.study.usedHint = false;
  state.study.hintText = null;
  state.study.result = null;
  state.study.sessionSeed = "s-" + Math.random().toString(36).slice(2, 9);
  if (root) root.innerHTML = renderSkeleton(6);

  const params = new URLSearchParams();
  if (state.study.unitCode && state.study.unitCode !== "ALL") {
    params.set("unit_code", state.study.unitCode);
  }
  params.set("mode", state.study.mode);
  params.set("session_seed", state.study.sessionSeed);
  if (customParams && customParams.question_id) {
    params.set("question_id", String(customParams.question_id));
  }
  if (customParams && customParams.variant_id) {
    params.set("variant_id", String(customParams.variant_id));
  }

  try {
    const res = await apiFetch("/api/session/next?" + params.toString());
    state.study.item = res.item;
    if (customParams && customParams.question_id && res.item && res.item.unit_code) {
      state.study.unitCode = res.item.unit_code;
    }
    state.study.startedAt = Date.now();
    renderStudyView();
  } catch (err) {
    if (root) {
      root.innerHTML = renderErrorState(err.message, "btn-retry-study");
      document.getElementById("btn-retry-study").addEventListener("click", () => loadNextStudyItem());
    }
  }
}

function renderStudyToolbar() {
  const units = (state.dashboard && state.dashboard.units) || [];
  let unitOptions = `<option value="ALL" ${state.study.unitCode === "ALL" ? "selected" : ""}>Tất cả 12 chủ đề</option>`;
  for (let i = 1; i <= 12; i++) {
    const code = `MU-${String(i).padStart(2, "0")}`;
    const uObj = units.find((u) => u.code === code);
    const label = uObj ? `${code}: ${uObj.title}` : code;
    unitOptions += `<option value="${code}" ${state.study.unitCode === code ? "selected" : ""}>${escapeHtml(label)}</option>`;
  }

  return `
    <div class="card" style="margin-bottom: 16px;">
      <div class="form-row" style="justify-content: space-between;">
        <div class="form-row">
          <div class="field">
            <label for="study-unit-sel">Chọn chủ đề</label>
            <select id="study-unit-sel" class="select">${unitOptions}</select>
          </div>
          <div class="field">
            <label for="study-mode-sel">Cách luyện tập</label>
            <select id="study-mode-sel" class="select">
              <option value="mixed" ${state.study.mode === "mixed" ? "selected" : ""}>Tự động kết hợp (Khuyên dùng)</option>
              <option value="original" ${state.study.mode === "original" ? "selected" : ""}>Câu hỏi gốc trong đề Excel</option>
              <option value="variant" ${state.study.mode === "variant" ? "selected" : ""}>Câu hỏi đổi dạng (Kiểm tra hiểu thật)</option>
              <option value="remediation" ${state.study.mode === "remediation" ? "selected" : ""}>Làm lại câu từng sai</option>
            </select>
          </div>
        </div>
        <div class="row-wrap">
          <button type="button" id="btn-view-bridge" class="btn-secondary">${state.study.showBridge ? "Quay lại câu hỏi" : "Ôn nhanh nền N4"}</button>
          <button type="button" id="btn-reshuffle-item" class="btn-secondary">Trộn lại đáp án</button>
        </div>
      </div>
    </div>
  `;
}

function bindStudyToolbarEvents() {
  const uSel = document.getElementById("study-unit-sel");
  const mSel = document.getElementById("study-mode-sel");
  const bBtn = document.getElementById("btn-view-bridge");
  const rBtn = document.getElementById("btn-reshuffle-item");

  if (uSel) {
    uSel.addEventListener("change", () => {
      state.study.unitCode = uSel.value;
      if (state.study.showBridge && uSel.value !== "ALL") loadBridgeUnit(uSel.value);
      else loadNextStudyItem();
    });
  }
  if (mSel) {
    mSel.addEventListener("change", () => {
      state.study.mode = mSel.value;
      loadNextStudyItem();
    });
  }
  if (bBtn) {
    bBtn.addEventListener("click", () => {
      if (state.study.showBridge) {
        loadNextStudyItem();
      } else {
        const target = state.study.unitCode === "ALL" ? "MU-01" : state.study.unitCode;
        loadBridgeUnit(target);
      }
    });
  }
  if (rBtn) {
    rBtn.addEventListener("click", () => {
      if (state.study.item) {
        loadNextStudyItem({
          question_id: state.study.item.question_id,
          variant_id: state.study.item.variant_id,
        });
      } else {
        loadNextStudyItem();
      }
    });
  }
}

function renderBridgePanel() {
  const bd = state.study.bridgeData;
  if (!bd || !bd.bridge_capsule) {
    return renderEmptyState("Chưa chọn chủ đề", "Chọn một chủ đề từ MU-01 đến MU-12 để xem bài ôn nền N4.", "Mở MU-01", "btn-open-mu01");
  }
  const u = bd.unit;
  const cap = bd.bridge_capsule;
  const brUi = state.ui.study.bridge;
  const examplesHtml = (cap.examples || []).map((ex) => `
    <div class="card" style="padding: 12px;">
      <div class="example-jp">${escapeHtml(ex.jp)}</div>
      <div class="muted">${escapeHtml(ex.vi)}</div>
    </div>
  `).join("");

  const qcHtml = (cap.quick_check || []).map((qc, idx) => {
    const chosen = state.study.quickCheckAnswers[idx];
    const opts = (qc.options || []).map((opt, oi) => `
      <button type="button" class="option-btn ${chosen === oi ? "selected" : ""}" data-qc="${idx}" data-oi="${oi}">
        <span class="opt-num">${oi + 1}</span>
        <span>${escapeHtml(opt)}</span>
      </button>
    `).join("");
    return `
      <div class="card" style="padding: 14px;">
        <p style="margin:0 0 8px;"><strong>Kiểm tra nhanh nền N4 (Câu ${idx + 1}):</strong> ${escapeHtml(qc.prompt)}</p>
        <div class="options-list">${opts}</div>
      </div>
    `;
  }).join("");

  return `
    <div class="card-editorial stack-md">
      <div class="section-header" style="margin-bottom:0;">
        <div>
          <span class="badge accent">Bước 1 · Ôn nền N4 trước khi làm N3</span>
          <h2 id="study-heading" class="section-title" style="margin-top:6px;">${escapeHtml(u.code)}: ${escapeHtml(u.title)}</h2>
          <p class="muted">${escapeHtml(cap.grammar_focus)}</p>
        </div>
        <span class="badge ${cap.completed ? "success" : "warning"}">${cap.completed ? "[OK] Đã hoàn thành nền N4" : "Chưa làm bài kiểm tra nhanh"}</span>
      </div>

      ${brUi.showExplanation ? `<div class="callout-info break-anywhere" style="white-space: pre-wrap;">${escapeHtml(cap.explanation_vi)}</div>` : ""}

      ${brUi.showExamples ? `
        <div class="stack-sm">
          <h3 class="card-title">Ví dụ so sánh N4 &#8594; N3</h3>
          ${examplesHtml}
        </div>
      ` : ""}

      ${brUi.showQuickCheck ? `
        <div class="stack-sm">
          <h3 class="card-title">Làm nhanh để chốt kiến thức nền N4</h3>
          ${qcHtml}
        </div>
      ` : ""}

      <div class="row-wrap">
        <button type="button" id="btn-complete-bridge" class="btn-primary">Hoàn thành ôn nền N4 &amp; Vào làm câu N3</button>
        <button type="button" id="btn-skip-to-questions" class="btn-secondary">Bỏ qua, vào thẳng câu hỏi ${escapeHtml(u.code)}</button>
      </div>
    </div>
  `;
}

function renderStudyView() {
  const root = document.getElementById("study-root");
  if (!root) return;

  const sUi = state.ui.study;
  const isFocusLayout = sUi.layout === "focus";
  const hasPassage = Boolean(!state.study.showBridge && state.study.item && state.study.item.passage);
  const isExamModeItem = Boolean(!state.study.showBridge && state.study.item && state.study.item.exam_mode);

  const studyControlBarHtml = `
    <div class="view-control-bar" role="region" aria-label="Tùy chỉnh hiển thị Làm câu hỏi">
      <div class="view-control-group">
        <div class="mode-seg-group" role="group" aria-label="Chế độ hiển thị câu hỏi">
          <button type="button" class="mode-seg-btn ${sUi.layout === "standard" ? "active" : ""}" data-study-layout="standard" aria-pressed="${sUi.layout === "standard"}">Đầy đủ</button>
          <button type="button" class="mode-seg-btn ${sUi.layout === "focus" ? "active" : ""}" data-study-layout="focus" aria-pressed="${sUi.layout === "focus"}">Tập trung câu hỏi</button>
        </div>
        ${hasPassage ? `
          <div class="mode-seg-group" role="group" aria-label="Bố cục bài đọc hiểu">
            <button type="button" class="mode-seg-btn ${sUi.dokkaiLayout === "split" ? "active" : ""}" data-dokkai-layout="split" aria-pressed="${sUi.dokkaiLayout === "split"}">2 cột song song</button>
            <button type="button" class="mode-seg-btn ${sUi.dokkaiLayout === "vertical" ? "active" : ""}" data-dokkai-layout="vertical" aria-pressed="${sUi.dokkaiLayout === "vertical"}">1 cột dọc dễ đọc</button>
          </div>
        ` : ""}
      </div>
      <div class="view-control-group">
        ${state.study.showBridge ? `
          <button type="button" class="vis-chip ${sUi.bridge.showExplanation ? "is-on" : ""}" data-bridge-vis="showExplanation" aria-pressed="${sUi.bridge.showExplanation}">Giải thích nền</button>
          <button type="button" class="vis-chip ${sUi.bridge.showExamples ? "is-on" : ""}" data-bridge-vis="showExamples" aria-pressed="${sUi.bridge.showExamples}">Ví dụ</button>
          <button type="button" class="vis-chip ${sUi.bridge.showQuickCheck ? "is-on" : ""}" data-bridge-vis="showQuickCheck" aria-pressed="${sUi.bridge.showQuickCheck}">Kiểm tra nhanh</button>
        ` : `
          <button type="button" class="vis-chip ${sUi.showToolbar ? "is-on" : ""}" data-study-vis="showToolbar" aria-pressed="${sUi.showToolbar}" ${isFocusLayout ? "disabled" : ""}>Thanh chủ đề</button>
          <button type="button" class="vis-chip ${sUi.showStepHint ? "is-on" : ""}" data-study-vis="showStepHint" aria-pressed="${sUi.showStepHint}" ${isFocusLayout ? "disabled" : ""}>Hướng dẫn bước</button>
          <button type="button" class="vis-chip ${sUi.showGlossaryAid ? "is-on" : ""}" data-study-vis="showGlossaryAid" aria-pressed="${sUi.showGlossaryAid}" ${isExamModeItem ? "disabled" : ""}>Từ vựng gợi ý</button>
          <button type="button" class="vis-chip ${sUi.showRubyAid ? "is-on" : ""}" data-study-vis="showRubyAid" aria-pressed="${sUi.showRubyAid}" ${isExamModeItem ? "disabled" : ""}>Phiên âm chữ Hán</button>
        `}
        <button type="button" class="btn-secondary btn-sm" data-enter-focus="study">${state.ui.focusMode ? "Thoát Tập trung (F)" : "Tập trung toàn màn hình (F)"}</button>
      </div>
    </div>
  `;

  let bodyHtml = "";
  if (state.study.showBridge) {
    bodyHtml = renderBridgePanel();
  } else if (!state.study.item) {
    bodyHtml = renderEmptyState(
      "Hiện chưa có câu hỏi trong chế độ này",
      "Bạn đã làm hết hàng đợi hiện tại. Hãy chuyển sang Câu hỏi đổi dạng hoặc chọn chủ đề khác.",
      "Chuyển sang Câu hỏi đổi dạng",
      "btn-switch-variant-empty"
    );
  } else {
    bodyHtml = renderActiveStudyItem();
  }

  const showToolbar = !isFocusLayout && sUi.showToolbar;
  const toolbarHtml = showToolbar ? renderStudyToolbar() : "";
  root.innerHTML = `<div class="stack-md">${studyControlBarHtml}${toolbarHtml}${bodyHtml}</div>`;
  applyUiStateToRoot();
  bindCommonControlEvents(root);
  if (showToolbar) bindStudyToolbarEvents();

  root.querySelectorAll("[data-study-layout]").forEach((btn) => {
    btn.addEventListener("click", () => {
      state.ui.study.layout = btn.dataset.studyLayout === "focus" ? "focus" : "standard";
      saveUiPreferences();
      renderStudyView();
    });
  });

  root.querySelectorAll("[data-dokkai-layout]").forEach((btn) => {
    btn.addEventListener("click", () => {
      state.ui.study.dokkaiLayout = btn.dataset.dokkaiLayout === "vertical" ? "vertical" : "split";
      saveUiPreferences();
      renderStudyView();
    });
  });

  root.querySelectorAll("[data-study-vis]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const key = btn.dataset.studyVis;
      if (key in state.ui.study) {
        state.ui.study[key] = !state.ui.study[key];
        saveUiPreferences();
        renderStudyView();
      }
    });
  });

  root.querySelectorAll("[data-bridge-vis]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const key = btn.dataset.bridgeVis;
      if (key in state.ui.study.bridge) {
        state.ui.study.bridge[key] = !state.ui.study.bridge[key];
        saveUiPreferences();
        renderStudyView();
      }
    });
  });

  if (state.study.showBridge) {
    const mu01Btn = document.getElementById("btn-open-mu01");
    if (mu01Btn) mu01Btn.addEventListener("click", () => loadBridgeUnit("MU-01"));
    root.querySelectorAll("[data-qc]").forEach((btn) => {
      btn.addEventListener("click", () => {
        const qci = parseInt(btn.dataset.qc, 10);
        const oi = parseInt(btn.dataset.oi, 10);
        state.study.quickCheckAnswers[qci] = oi;
        renderStudyView();
      });
    });
    const compBtn = document.getElementById("btn-complete-bridge");
    if (compBtn) {
      compBtn.addEventListener("click", async () => {
        const cap = state.study.bridgeData.bridge_capsule;
        const totalQc = (cap.quick_check || []).length;
        const answers = [];
        for (let i = 0; i < totalQc; i++) {
          if (state.study.quickCheckAnswers[i] === undefined) {
            showToast("Hãy trả lời đủ các câu Kiểm tra nhanh N4 trước khi thông trạm.", true);
            return;
          }
          answers.push(state.study.quickCheckAnswers[i]);
        }
        try {
          const res = await apiFetch(`/api/units/${encodeURIComponent(state.study.unitCode)}/bridge/complete`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ quick_check_answers: answers }),
          });
          if (!res.completed) {
            const firstErr = (res.quick_check_results || []).find((x) => !x.is_correct);
            showToast("Có câu nền N4 chưa đúng: " + (firstErr ? firstErr.note : ""), true);
            return;
          }
          showToast("[OK] Đã hoàn thành bài ôn nền N4! Giờ hãy làm câu hỏi N3.");
          loadNextStudyItem();
        } catch (err) {
          showToast(err.message, true);
        }
      });
    }
    const skipBtn = document.getElementById("btn-skip-to-questions");
    if (skipBtn) skipBtn.addEventListener("click", () => loadNextStudyItem());
  } else if (!state.study.item) {
    const swBtn = document.getElementById("btn-switch-variant-empty");
    if (swBtn) {
      swBtn.addEventListener("click", () => {
        state.study.mode = "variant";
        loadNextStudyItem();
      });
    }
  } else {
    bindActiveStudyEvents();
  }
}

function renderActiveStudyItem() {
  const item = state.study.item;
  const res = state.study.result;
  const scaf = item.scaffolding;
  const sUi = state.ui.study;
  const isFocusLayout = sUi.layout === "focus";
  const isExamModeItem = Boolean(item.exam_mode);

  const variantLabel = item.variant_mode === "original"
    ? "Câu gốc trong đề (Trộn A/B/C/D)"
    : item.variant_mode === "star_4slot_shift"
    ? "Đổi dạng: Xếp đủ 4 ô dấu ★"
    : item.variant_mode === "dokkai_evidence"
    ? "Đổi dạng: Chọn câu bằng chứng trước khi trả lời"
    : item.variant_mode === "condition_shift"
    ? "Đổi dạng: Đảo điều kiện tìm thông tin"
    : item.variant_mode === "error_diagnosis"
    ? "Đổi dạng: Phân biệt bẫy ngữ cảnh"
    : "Đổi dạng: Thử thách phương án dễ nhầm";

  const badgesRowHtml = isFocusLayout
    ? ""
    : `<div class="row-wrap" style="justify-content: space-between; margin-bottom: 8px;">
         <div class="row-wrap">
           <span class="badge accent">${escapeHtml(item.unit_code)}</span>
           <span class="badge">${escapeHtml(item.mondai_type)}</span>
           <span class="badge">${escapeHtml(variantLabel)}</span>
         </div>
         <span class="badge ${scaf.tier === 3 ? "warning" : ""}">${escapeHtml(scaf.tier_label)}</span>
       </div>`;

  const bridgeAlert = !isFocusLayout && item.bridge_status && !item.bridge_status.completed
    ? `<div class="callout-warn" style="margin-bottom: 12px;">
         Bạn chưa ôn bài <strong>Nền tảng N4 (${escapeHtml(item.unit_code)})</strong>: ${escapeHtml(item.bridge_status.grammar_focus)}.
         <button type="button" id="btn-inline-bridge" class="btn-secondary btn-sm" style="margin-left:8px;">Ôn nhanh nền N4 (~5 phút)</button>
       </div>`
    : "";

  const glossaryHtml = !res && !isExamModeItem && sUi.showGlossaryAid && scaf.background_glossary && scaf.background_glossary.length
    ? `<div class="glossary-grid">${scaf.background_glossary.map((g) =>
        `<span class="glossary-chip"><strong>${escapeHtml(g.word)}</strong> (${escapeHtml(g.reading)} · ${escapeHtml(g.han_viet)}): ${escapeHtml(g.meaning_vi)}</span>`
      ).join("")}</div>`
    : "";

  const hintBox = !isExamModeItem && state.study.hintText
    ? `<div class="callout-info" style="margin-top:8px;"><strong>Gợi ý (Phím H):</strong> ${escapeHtml(state.study.hintText)}</div>`
    : "";

  const stepHintBar = !res && !isFocusLayout && sUi.showStepHint
    ? `<div class="step-hint-bar">${
        item.interaction_type === "star_4slot"
          ? "Cách làm: Bấm lần lượt từng mảnh ghép bên dưới để xếp đúng trật tự câu đủ 4 ô (chú ý vị trí dấu ★)."
          : item.interaction_type === "dokkai_evidence"
          ? "Cách làm: Bước 1 bấm chọn câu chứa bằng chứng ở đoạn văn bên trái, Bước 2 chọn đáp án 1–4 rồi nộp."
          : "Cách làm: Chọn 1 đáp án đúng (hoặc bấm phím 1–4), sau đó bấm Kiểm tra đáp án (hoặc phím Space)."
      }</div>`
    : "";

  let interactiveHtml = "";
  if (item.interaction_type === "star_4slot") {
    const sa = item.star_assembly;
    const starSlot = sa.star_slot_index;
    const slotsHtml = [0, 1, 2, 3].map((slotIdx) => {
      const assignedChunkIdx = state.study.starSlots[slotIdx];
      const chunkObj = assignedChunkIdx !== null ? sa.chunks.find((c) => c.chunk_index === assignedChunkIdx) : null;
      const isStar = slotIdx === starSlot;
      return `
        <button type="button" class="star-slot-btn ${isStar ? "is-star-slot" : ""} ${chunkObj ? "filled" : ""}" data-slot-idx="${slotIdx}" ${res ? "disabled" : ""}>
          <span class="slot-label">${isStar ? `Ô ${slotIdx + 1} (★)` : `Ô ${slotIdx + 1}`}</span>
          <span>${chunkObj ? escapeHtml(chunkObj.text) : "Trống"}</span>
        </button>
      `;
    }).join("");

    const usedChunks = new Set(state.study.starSlots.filter((x) => x !== null));
    const chipsHtml = sa.chunks.map((c) => `
      <button type="button" class="chunk-chip ${usedChunks.has(c.chunk_index) ? "used" : ""}" data-chunk-idx="${c.chunk_index}" ${res || usedChunks.has(c.chunk_index) ? "disabled" : ""}>
        ${escapeHtml(c.text)}
      </button>
    `).join("");

    const allFilled = state.study.starSlots.every((x) => x !== null);
    interactiveHtml = `
      <div class="stack-sm">
        <p class="muted"><strong>Quy tắc Ghép đủ 4 ô ★:</strong> Bấm từng mảnh ghép bên dưới để xếp đủ cả 4 ô [1][2][3][4] (ô ★ đang ở <strong>Ô ${starSlot + 1}</strong>). Bấm vào ô đã điền để gỡ ra.</p>
        <div class="star-slots-grid">${slotsHtml}</div>
        <div class="chunks-pool">${chipsHtml}</div>
        <div class="row-wrap">
          <button type="button" id="btn-clear-star" class="btn-secondary btn-sm" ${res ? "disabled" : ""}>Xóa xếp lại</button>
          ${!res ? `<button type="button" id="btn-submit-study" class="btn-primary" ${allFilled ? "" : "disabled"}>Kiểm tra đủ 4 ô (${state.study.starSlots.filter((x) => x !== null).length}/4)</button>` : ""}
        </div>
      </div>
    `;
  } else {
    const optsHtml = item.options_html.map((optHtml, idx) => {
      let cls = "option-btn";
      if (!res && state.study.selectedOption === idx) cls += " selected";
      if (res) {
        const correctTxt = res.correct_option_text;
        const rawTxt = item.options[idx];
        if (rawTxt === correctTxt) cls += " correct";
        else if (state.study.selectedOption === idx && !res.answer_correct) cls += " wrong";
      }
      return `
        <button type="button" class="${cls}" data-opt-idx="${idx}" ${res ? "disabled" : ""}>
          <span class="opt-num tabular-nums">${idx + 1}</span>
          <span class="min-w-0 break-anywhere">${optHtml}</span>
        </button>
      `;
    }).join("");

    const evNote = item.interaction_type === "dokkai_evidence" && !res
      ? `<div class="callout-info" style="margin-bottom:8px;">
           <strong>Bước 1:</strong> Bấm chọn câu chốt / dòng điều kiện (<code>注意・休診</code>) ở khung văn bản (${state.study.evidenceIndices.length} câu đã chọn).
           <strong>Bước 2:</strong> Chọn đáp án 1–4 rồi nộp bài.
         </div>`
      : "";

    const canSubmit = item.interaction_type === "dokkai_evidence"
      ? state.study.selectedOption !== null && state.study.evidenceIndices.length > 0
      : state.study.selectedOption !== null;

    interactiveHtml = `
      ${evNote}
      <div class="options-list">${optsHtml}</div>
      <div class="row-wrap" style="margin-top: 12px;">
        ${!res ? `<button type="button" id="btn-submit-study" class="btn-primary" ${canSubmit ? "" : "disabled"}>Kiểm tra đáp án (Space)</button>` : ""}
        ${!res && !isExamModeItem && scaf.hint_allowed ? `<button type="button" id="btn-hint-study" class="btn-secondary">Xem 1 gợi ý (Phím H)</button>` : ""}
      </div>
    `;
  }

  let feedbackHtml = "";
  if (res) {
    const fbUi = sUi.feedback;
    const statusCls = res.is_correct ? "callout-success" : "callout-danger";
    const statusTitle = res.is_correct
      ? (res.remediated ? "[OK] CHÍNH XÁC — Bạn đã sửa xong câu từng sai!" : "[OK] CHÍNH XÁC")
      : (item.interaction_type === "dokkai_evidence" && res.answer_correct && !res.evidence_correct
          ? "[FAIL] CHỌN ĐÚNG ĐÁP ÁN NHƯNG SAI CÂU BẰNG CHỨNG TRONG BÀI ĐỌC"
          : "[FAIL] CHƯA CHÍNH XÁC — Đã lưu vào mục Câu hay sai để ôn lại");

    const soTay = res.notebook_meta && res.notebook_meta.so_tay;
    const gNb = res.notebook_meta && res.notebook_meta.grammar_notebook;
    const trapDec = res.notebook_meta && res.notebook_meta.trap_decoder;

    const companionHtml = soTay
      ? `<div class="callout-info"><strong>Sổ tay Từ vựng:</strong> ${escapeHtml(soTay.word)} (${escapeHtml(soTay.hiragana)} | Hán-Việt: ${escapeHtml(soTay.han_viet)}) — ${escapeHtml(soTay.meaning_vi)}<br>${escapeHtml(soTay.collocation_tip)}</div>`
      : gNb
      ? `<div class="callout-info"><strong>Sổ tay Ngữ pháp:</strong> ${escapeHtml(gNb.pattern)} (${escapeHtml(gNb.structure)}) — ${escapeHtml(gNb.meaning_vi)}<br><em>Phân biệt:</em> ${escapeHtml(gNb.distinction)}</div>`
      : trapDec
      ? `<div class="callout-info"><strong>Giải mã Bẫy Dokkai:</strong><br>Câu chốt: ${escapeHtml(trapDec.key_evidence_sentence)}<br>Paraphrase: ${escapeHtml(trapDec.paraphrase)}<br>Bẫy: ${escapeHtml(trapDec.classic_traps)}</div>`
      : "";

    const matrixRows = (res.condition_matrix || []).map((m) => `
      <tr>
        <td><strong>${escapeHtml(m.source_label)}</strong><br>${escapeHtml(m.character)}</td>
        <td>${escapeHtml(m.condition_1)}</td>
        <td>${escapeHtml(m.condition_2)}</td>
        <td>${escapeHtml(m.hidden_condition)}</td>
        <td><strong>${escapeHtml(m.matched_answer)}</strong></td>
      </tr>
    `).join("");

    const matrixHtml = matrixRows
      ? `<div class="table-scroll-wrap" style="margin-top:8px;">
           <table class="data-table">
             <thead><tr><th>Câu/Nhân vật</th><th>ĐK 1</th><th>ĐK 2</th><th>Điều kiện ẩn (注意/休診)</th><th>Khớp chuẩn</th></tr></thead>
             <tbody>${matrixRows}</tbody>
           </table>
         </div>`
      : "";

    const fbControlsHtml = `
      <div class="view-control-bar" role="region" aria-label="Ẩn hiện phần giải thích sau nộp">
        <div class="view-control-group">
          <span class="view-control-label">Giải thích sau nộp:</span>
          <button type="button" class="vis-chip ${fbUi.showTranslation ? "is-on" : ""}" data-study-fb="showTranslation" aria-pressed="${fbUi.showTranslation}">Dịch nghĩa</button>
          <button type="button" class="vis-chip ${fbUi.showExplanation ? "is-on" : ""}" data-study-fb="showExplanation" aria-pressed="${fbUi.showExplanation}">Giải thích</button>
          <button type="button" class="vis-chip ${fbUi.showGrammarAnatomy ? "is-on" : ""}" data-study-fb="showGrammarAnatomy" aria-pressed="${fbUi.showGrammarAnatomy}">Giải phẫu Ngữ pháp</button>
          <button type="button" class="vis-chip ${fbUi.showCompanion ? "is-on" : ""}" data-study-fb="showCompanion" aria-pressed="${fbUi.showCompanion}">Sổ tay</button>
        </div>
      </div>
    `;

    feedbackHtml = `
      <div class="stack-sm" style="margin-top: 16px;">
        <div class="${statusCls}">
          <strong>${statusTitle}</strong><br>
          <span>Đáp án chuẩn: <strong>${escapeHtml(res.correct_option_text)}</strong></span>
          ${res.assembled_sentence ? `<div style="margin-top:4px;">Câu ghép hoàn chỉnh: <strong>${escapeHtml(res.assembled_sentence)}</strong></div>` : ""}
        </div>
        ${fbControlsHtml}
        ${fbUi.showTranslation && res.translation_vi ? `<div class="card" data-study-fb-box="translation" style="padding:12px;"><strong>Dịch nghĩa:</strong> ${escapeHtml(res.translation_vi)}</div>` : ""}
        ${fbUi.showExplanation ? `<div class="card" data-study-fb-box="explanation" style="padding:12px; white-space: pre-wrap;"><strong>Giải thích &amp; Phân tích bẫy:</strong>\n${escapeHtml(res.explanation_vi)}</div>` : ""}
        ${fbUi.showGrammarAnatomy ? renderGrammarBreakdownHtml(res.grammar_breakdown) : ""}
        ${fbUi.showCompanion ? companionHtml : ""}
        ${fbUi.showTranslation && res.passage_translation_vi ? `<div class="card" data-study-fb-box="passage-translation" style="padding:12px; white-space: pre-wrap;"><strong>Dịch &amp; Mạch logic văn bản:</strong>\n${escapeHtml(res.passage_translation_vi)}</div>` : ""}
        ${fbUi.showExplanation ? matrixHtml : ""}
        <div class="row-wrap" style="justify-content: space-between; margin-top: 6px;">
          <span class="muted tabular-nums">Hẹn ôn lại sau ${res.fsrs.effective_interval_days} ngày · Đã làm đúng liên tiếp ${res.fsrs.spaced_clean_sessions}/2 lần</span>
          <button type="button" id="btn-next-study" class="btn-primary">Câu tiếp theo (Space)</button>
        </div>
      </div>
    `;
  }

  const questionCardHtml = `
    <div class="card-editorial min-w-0">
      ${badgesRowHtml}
      ${bridgeAlert}
      ${stepHintBar}
      <div class="jp-prompt">${item.prompt_html}</div>
      ${glossaryHtml}
      ${hintBox}
      ${interactiveHtml}
      ${feedbackHtml}
    </div>
  `;

  if (item.passage) {
    const p = item.passage;
    const isSelectable = item.interaction_type === "dokkai_evidence" && !res;
    const goldSet = new Set((res && res.gold_evidence_indices) || []);
    const selectedSet = new Set(state.study.evidenceIndices);

    const sentsHtml = (p.sentences || []).map((s) => {
      let sCls = "passage-sentence";
      if (isSelectable) sCls += " selectable";
      if (goldSet.has(s.index)) sCls += " gold-evidence";
      else if (selectedSet.has(s.index)) sCls += " selected-evidence";
      return `
        <button type="button" class="${sCls}" data-sent-idx="${s.index}" ${isSelectable ? "" : "disabled"}>
          <span class="sent-num">S${s.index + 1}</span>
          <span>${s.html}</span>
        </button>
      `;
    }).join("");

    const dokkaiCls = sUi.dokkaiLayout === "vertical" ? "dokkai-split dokkai-vertical" : "dokkai-split";
    const splitHtml = `
      <div class="${dokkaiCls}">
        <div class="passage-card">
          <div class="row-wrap" style="justify-content: space-between; margin-bottom: 8px;">
            <strong class="break-anywhere">${escapeHtml(p.title)}</strong>
            <span class="badge">${escapeHtml(p.genre)}</span>
          </div>
          <div>${sentsHtml}</div>
        </div>
        <div class="min-w-0">${questionCardHtml}</div>
      </div>
    `;
    if (isFocusLayout && sUi.dokkaiLayout === "vertical") {
      return `<div class="study-focus-stage">${splitHtml}</div>`;
    }
    return splitHtml;
  }

  return isFocusLayout ? `<div class="study-focus-stage">${questionCardHtml}</div>` : questionCardHtml;
}

function bindActiveStudyEvents() {
  const root = document.getElementById("study-root");
  if (!root || !state.study.item) return;

  const inlineBridge = document.getElementById("btn-inline-bridge");
  if (inlineBridge) {
    inlineBridge.addEventListener("click", () => loadBridgeUnit(state.study.item.unit_code));
  }

  root.querySelectorAll("[data-study-fb]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const key = btn.dataset.studyFb;
      if (key in state.ui.study.feedback) {
        state.ui.study.feedback[key] = !state.ui.study.feedback[key];
        saveUiPreferences();
        renderStudyView();
      }
    });
  });

  root.querySelectorAll("[data-opt-idx]").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      if (state.study.result) return;
      state.study.selectedOption = parseInt(btn.dataset.optIdx, 10);
      if (e.detail > 0 && document.activeElement) document.activeElement.blur();
      renderStudyView();
    });
  });

  root.querySelectorAll("[data-sent-idx]").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      if (state.study.result || state.study.item.interaction_type !== "dokkai_evidence") return;
      const idx = parseInt(btn.dataset.sentIdx, 10);
      const pos = state.study.evidenceIndices.indexOf(idx);
      if (pos >= 0) state.study.evidenceIndices.splice(pos, 1);
      else state.study.evidenceIndices.push(idx);
      if (e.detail > 0 && document.activeElement) document.activeElement.blur();
      renderStudyView();
    });
  });

  root.querySelectorAll("[data-chunk-idx]").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      if (state.study.result) return;
      const chunkIdx = parseInt(btn.dataset.chunkIdx, 10);
      const emptyPos = state.study.starSlots.indexOf(null);
      if (emptyPos >= 0) {
        state.study.starSlots[emptyPos] = chunkIdx;
        if (e.detail > 0 && document.activeElement) document.activeElement.blur();
        renderStudyView();
      }
    });
  });

  root.querySelectorAll("[data-slot-idx]").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      if (state.study.result) return;
      const slotIdx = parseInt(btn.dataset.slotIdx, 10);
      if (state.study.starSlots[slotIdx] !== null) {
        state.study.starSlots[slotIdx] = null;
        if (e.detail > 0 && document.activeElement) document.activeElement.blur();
        renderStudyView();
      }
    });
  });

  const clearStarBtn = document.getElementById("btn-clear-star");
  if (clearStarBtn) {
    clearStarBtn.addEventListener("click", () => {
      state.study.starSlots = [null, null, null, null];
      renderStudyView();
    });
  }

  const hintBtn = document.getElementById("btn-hint-study");
  if (hintBtn) hintBtn.addEventListener("click", triggerStudyHint);

  const subBtn = document.getElementById("btn-submit-study");
  if (subBtn) subBtn.addEventListener("click", submitActiveStudy);

  const nextBtn = document.getElementById("btn-next-study");
  if (nextBtn) nextBtn.addEventListener("click", () => loadNextStudyItem());

  bindGrammarChipButtons(root);
}

async function triggerStudyHint() {
  const item = state.study.item;
  if (!item || state.study.result) return;
  try {
    const res = await apiFetch("/api/session/hint", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        question_id: item.question_id,
        variant_id: item.variant_id,
        exam_mode: item.exam_mode,
      }),
    });
    if (!res.allowed) {
      showToast(res.reason, true);
      return;
    }
    state.study.usedHint = true;
    state.study.hintText = res.hint_text;
    renderStudyView();
  } catch (err) {
    showToast(err.message, true);
  }
}

async function submitActiveStudy() {
  const item = state.study.item;
  if (!item || state.study.result) return;
  const elapsed = Math.max(0.5, (Date.now() - state.study.startedAt) / 1000);
  const payload = {
    question_id: item.question_id,
    variant_id: item.variant_id,
    mode: item.mode,
    used_hint: state.study.usedHint,
    response_sec: elapsed,
    session_seed: item.session_seed,
    exam_mode: item.exam_mode,
  };
  if (item.interaction_type === "star_4slot") {
    if (state.study.starSlots.some((x) => x === null)) {
      showToast("Bắt buộc ghép đủ cả 4 ô [1][2][3][4] trước khi nộp.", true);
      return;
    }
    payload.slot_order = state.study.starSlots;
  } else {
    if (state.study.selectedOption === null) {
      showToast("Hãy chọn 1 đáp án (1–4).", true);
      return;
    }
    payload.selected_index = state.study.selectedOption;
    if (item.interaction_type === "dokkai_evidence") {
      if (!state.study.evidenceIndices.length) {
        showToast("Hãy bấm chọn câu chốt bằng chứng trong văn bản trước.", true);
        return;
      }
      payload.evidence_indices = state.study.evidenceIndices;
    }
  }

  try {
    const res = await apiFetch("/api/session/submit", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    state.study.result = res.result;
    if (typeof res.error_count === "number") {
      updateNavErrorBadge(res.error_count);
    }
    if (state.dashboard) {
      state.dashboard.readiness = res.readiness;
      state.dashboard.pace = res.pace;
      if (typeof res.error_count === "number") {
        state.dashboard.error_count = res.error_count;
      }
    }
    renderStudyView();
  } catch (err) {
    showToast(err.message, true);
  }
}

/* Exam Mode View */
function isExamItemAnswered(it) {
  const a = state.exam.answers[it.question_id];
  if (!a) return false;
  if (it.interaction_type === "star_4slot") {
    return Array.isArray(a.slot_order) && a.slot_order.every((x) => x !== null);
  }
  return a.selected_index !== undefined && a.selected_index !== null;
}

function navigateExamSingle(delta) {
  const ex = state.exam.examData;
  if (!state.exam.active || !ex || !ex.items || !ex.items.length) return;
  const next = state.ui.exam.currentIndex + delta;
  if (next < 0 || next >= ex.items.length) return;
  state.ui.exam.currentIndex = next;
  renderExamShell();
}

function renderExamShell() {
  const root = document.getElementById("exam-root");
  if (!root) return;

  if (state.exam.result) {
    const er = state.exam.result;
    const rows = er.details.map((d, idx) => `
      <tr>
        <td class="tabular-nums">${idx + 1}</td>
        <td>${d.is_correct ? '<span class="badge success">[OK]</span>' : '<span class="badge danger">[FAIL]</span>'}</td>
        <td class="break-anywhere">
          <strong>${escapeHtml(d.correct_option_text)}</strong>
          ${d.assembled_sentence ? `<div class="muted" style="margin-top:2px;">${escapeHtml(d.assembled_sentence)}</div>` : ""}
        </td>
        <td class="break-anywhere">
          <div>${escapeHtml((d.explanation_vi || "").split("\n")[0])}</div>
          ${renderGrammarBreakdownHtml(d.grammar_breakdown, { compact: true })}
        </td>
      </tr>
    `).join("");

    root.innerHTML = `
      <div class="stack-md">
        <div class="section-header">
          <div>
            <h2 id="exam-heading" class="section-title">Kết quả Phòng thi Thực chiến (Bài thi thử)</h2>
            <p class="muted">Kết quả đã được lưu tự động vào tiến độ học tập trên Trang chủ.</p>
          </div>
          <button type="button" id="btn-exam-reset" class="btn-primary">Làm đề thi khác</button>
        </div>
        <div class="grid-3">
          <div class="card">
            <h3 class="card-title">Điểm bài thi này</h3>
            <div class="score-big tabular-nums">${er.exam_accuracy_10.toFixed(2)} <span class="score-den">/ 10</span></div>
            <p class="muted tabular-nums">${er.correct_count}/${er.total_questions} câu đúng</p>
          </div>
          <div class="card">
            <h3 class="card-title">Điểm Làm Đề Gốc toàn bộ</h3>
            <div class="score-big tabular-nums">${er.readiness.original_score_10.toFixed(2)} <span class="score-den">/ 10</span></div>
          </div>
          <div class="card">
            <h3 class="card-title">Điểm Hiểu Thật toàn bộ</h3>
            <div class="score-big tabular-nums">${er.readiness.mastery_score_10.toFixed(2)} <span class="score-den">/ 10</span></div>
          </div>
        </div>
        <div class="table-scroll-wrap">
          <table class="data-table">
            <thead><tr><th>#</th><th>Kết quả</th><th>Đáp án đúng</th><th>Giải thích cốt lõi</th></tr></thead>
            <tbody>${rows}</tbody>
          </table>
        </div>
      </div>
    `;
    document.getElementById("btn-exam-reset").addEventListener("click", () => {
      state.exam.result = null;
      state.exam.examData = null;
      renderExamShell();
    });
    bindGrammarChipButtons(root);
    applyUiStateToRoot();
    return;
  }

  if (!state.exam.active || !state.exam.examData) {
    root.innerHTML = `
      <div class="card-editorial stack-md" style="max-width: 680px; margin: 0 auto;">
        <h2 id="exam-heading" class="section-title">Thi thử như Phòng thi Thật (Tắt hết gợi ý)</h2>
        <ul class="stack-sm" style="margin: 0; padding-left: 20px;">
          <li>Không hiển thị phiên âm phụ và khóa hoàn toàn nút xem gợi ý.</li>
          <li>Thứ tự đáp án A/B/C/D tự động trộn mới mỗi lần thi để kiểm tra năng lực thực tế.</li>
          <li>Với câu sắp xếp sao ★, cần điền đủ cả 4 ô trước khi nộp bài.</li>
        </ul>
        <div class="form-row">
          <div class="field">
            <label for="exam-count-sel">Độ dài đề thi thử</label>
            <select id="exam-count-sel" class="select">
              <option value="2">Đề ngắn — 6 câu (~5 phút)</option>
              <option value="3" selected>Đề vừa — 9 câu (~10 phút)</option>
              <option value="5">Đề đầy đủ — 15 câu (~18 phút)</option>
            </select>
          </div>
          <button type="button" id="btn-start-exam" class="btn-primary">Bắt đầu Thi thử</button>
        </div>
      </div>
    `;
    document.getElementById("btn-start-exam").addEventListener("click", startMockExam);
    applyUiStateToRoot();
    return;
  }

  const ex = state.exam.examData;
  const exUi = state.ui.exam;
  if (exUi.currentIndex >= ex.items.length) {
    exUi.currentIndex = Math.max(0, ex.items.length - 1);
  }
  if (exUi.currentIndex < 0) exUi.currentIndex = 0;

  const isSingle = exUi.layout === "single";
  const curIdx = exUi.currentIndex;
  const answeredCount = ex.items.filter(isExamItemAnswered).length;

  const examControlStripHtml = `
    <div class="exam-control-strip" role="region" aria-label="Tùy chỉnh phòng thi">
      <div class="view-control-group">
        <div class="mode-seg-group" role="group" aria-label="Bố cục đề thi">
          <button type="button" class="mode-seg-btn ${!isSingle ? "active" : ""}" data-exam-layout="all" aria-pressed="${!isSingle}">Xem toàn bộ đề</button>
          <button type="button" class="mode-seg-btn ${isSingle ? "active" : ""}" data-exam-layout="single" aria-pressed="${isSingle}">Tập trung từng câu</button>
        </div>
      </div>
      <div class="view-control-group">
        <button type="button" class="vis-chip ${exUi.showTimer ? "is-on" : ""}" data-exam-vis="showTimer" aria-pressed="${exUi.showTimer}">Hiện đồng hồ</button>
        <button type="button" class="vis-chip ${exUi.showPalette ? "is-on" : ""}" data-exam-vis="showPalette" aria-pressed="${exUi.showPalette}">Bảng chuyển câu</button>
        <button type="button" class="btn-secondary btn-sm" data-enter-focus="exam">${state.ui.focusMode ? "Thoát Tập trung (F)" : "Tập trung phòng thi (F)"}</button>
      </div>
    </div>
  `;

  const examPaletteHtml = exUi.showPalette
    ? `<div class="exam-palette" role="navigation" aria-label="Bảng chuyển câu thi">
         ${ex.items.map((it, idx) => {
           const answered = isExamItemAnswered(it);
           const isCur = idx === curIdx;
           return `<button type="button" class="exam-palette-btn ${answered ? "is-answered" : ""} ${isCur ? "is-current" : ""}" data-exam-idx="${idx}" aria-label="Chuyển tới câu ${idx + 1}">${idx + 1}</button>`;
         }).join("")}
       </div>`
    : "";

  const itemsHtml = ex.items.map((it, idx) => {
    const ans = state.exam.answers[it.question_id] || {};
    let inputHtml = "";
    if (it.interaction_type === "star_4slot") {
      const slots = ans.slot_order || [null, null, null, null];
      const sa = it.star_assembly;
      const used = new Set(slots.filter((x) => x !== null));
      inputHtml = `
        <div class="star-slots-grid">
          ${[0, 1, 2, 3].map((si) => {
            const cIdx = slots[si];
            const cObj = cIdx !== null ? sa.chunks.find((c) => c.chunk_index === cIdx) : null;
            return `<button type="button" class="star-slot-btn ${si === sa.star_slot_index ? "is-star-slot" : ""} ${cObj ? "filled" : ""}" data-ex-q="${it.question_id}" data-ex-slot="${si}">
              <span class="slot-label">${si === sa.star_slot_index ? `Ô ${si + 1} (★)` : `Ô ${si + 1}`}</span>
              <span>${cObj ? escapeHtml(cObj.text) : "Trống"}</span>
            </button>`;
          }).join("")}
        </div>
        <div class="chunks-pool">
          ${sa.chunks.map((c) => `<button type="button" class="chunk-chip ${used.has(c.chunk_index) ? "used" : ""}" data-ex-q="${it.question_id}" data-ex-chunk="${c.chunk_index}" ${used.has(c.chunk_index) ? "disabled" : ""}>${escapeHtml(c.text)}</button>`).join("")}
        </div>
      `;
    } else {
      inputHtml = `
        <div class="options-list">
          ${it.options_html.map((oh, oi) => `
            <button type="button" class="option-btn ${ans.selected_index === oi ? "selected" : ""}" data-ex-q="${it.question_id}" data-ex-opt="${oi}">
              <span class="opt-num tabular-nums">${oi + 1}</span>
              <span>${oh}</span>
            </button>
          `).join("")}
        </div>
      `;
    }

    const pHtml = it.passage ? `<div class="passage-card" style="margin-bottom:8px;"><strong>${escapeHtml(it.passage.title)}</strong><div>${it.passage.full_html}</div></div>` : "";
    const hiddenAttr = isSingle && idx !== curIdx ? "hidden" : "";
    return `
      <div class="card" data-exam-card-idx="${idx}" ${hiddenAttr}>
        <div class="row-wrap" style="justify-content: space-between; margin-bottom: 6px;">
          <span class="badge accent tabular-nums">Câu ${idx + 1}/${ex.total_questions} · ${escapeHtml(it.unit_code)}</span>
          <span class="badge warning">Không gợi ý</span>
        </div>
        ${pHtml}
        <div class="jp-prompt">${it.prompt_html}</div>
        ${inputHtml}
      </div>
    `;
  }).join("");

  const examSingleNavHtml = isSingle
    ? `<div class="exam-single-nav">
         <button type="button" id="btn-exam-prev" class="btn-secondary" ${curIdx <= 0 ? "disabled" : ""}>Câu trước ([)</button>
         <span class="muted tabular-nums">Câu <strong>${curIdx + 1}</strong> / ${ex.items.length}</span>
         <button type="button" id="btn-exam-next" class="btn-primary" ${curIdx >= ex.items.length - 1 ? "disabled" : ""}>Câu tiếp (])</button>
       </div>`
    : "";

  root.innerHTML = `
    <div class="stack-md">
      <div class="section-header">
        <div>
          <h2 id="exam-heading" class="section-title">Đang thi thử (${ex.total_questions} câu)</h2>
          <p class="muted">Đã trả lời: <strong class="tabular-nums">${answeredCount}/${ex.total_questions} câu</strong> · Thời gian: <strong id="exam-timer" class="tabular-nums" ${exUi.showTimer ? "" : "hidden"}>${formatExamTimer(state.exam.elapsedSec)}</strong>${exUi.showTimer ? "" : ' <span class="muted">[Đã ẩn đồng hồ]</span>'}</p>
        </div>
        <button type="button" id="btn-submit-exam" class="btn-primary">Nộp bài thi ngay</button>
      </div>
      ${examControlStripHtml}
      ${examPaletteHtml}
      ${itemsHtml}
      ${examSingleNavHtml}
    </div>
  `;

  applyUiStateToRoot();
  bindCommonControlEvents(root);

  root.querySelectorAll("[data-exam-layout]").forEach((btn) => {
    btn.addEventListener("click", () => {
      state.ui.exam.layout = btn.dataset.examLayout === "single" ? "single" : "all";
      saveUiPreferences();
      renderExamShell();
    });
  });

  root.querySelectorAll("[data-exam-vis]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const key = btn.dataset.examVis;
      if (key in state.ui.exam) {
        state.ui.exam[key] = !state.ui.exam[key];
        saveUiPreferences();
        renderExamShell();
      }
    });
  });

  root.querySelectorAll("[data-exam-idx]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const idx = parseInt(btn.dataset.examIdx, 10);
      if (!Number.isFinite(idx)) return;
      state.ui.exam.currentIndex = idx;
      renderExamShell();
      if (state.ui.exam.layout === "all") {
        const card = root.querySelector(`[data-exam-card-idx="${idx}"]`);
        if (card) card.scrollIntoView({ behavior: "smooth", block: "nearest" });
      }
    });
  });

  const prevBtn = document.getElementById("btn-exam-prev");
  if (prevBtn) prevBtn.addEventListener("click", () => navigateExamSingle(-1));
  const nextBtn = document.getElementById("btn-exam-next");
  if (nextBtn) nextBtn.addEventListener("click", () => navigateExamSingle(1));

  root.querySelectorAll("[data-ex-opt]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const qid = parseInt(btn.dataset.exQ, 10);
      const oi = parseInt(btn.dataset.exOpt, 10);
      state.exam.answers[qid] = { selected_index: oi };
      renderExamShell();
    });
  });

  root.querySelectorAll("[data-ex-chunk]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const qid = parseInt(btn.dataset.exQ, 10);
      const ci = parseInt(btn.dataset.exChunk, 10);
      const cur = (state.exam.answers[qid] && state.exam.answers[qid].slot_order) || [null, null, null, null];
      const emp = cur.indexOf(null);
      if (emp >= 0) {
        cur[emp] = ci;
        state.exam.answers[qid] = { slot_order: cur };
        renderExamShell();
      }
    });
  });

  root.querySelectorAll("[data-ex-slot]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const qid = parseInt(btn.dataset.exQ, 10);
      const si = parseInt(btn.dataset.exSlot, 10);
      const cur = (state.exam.answers[qid] && state.exam.answers[qid].slot_order) || [null, null, null, null];
      if (cur[si] !== null) {
        cur[si] = null;
        state.exam.answers[qid] = { slot_order: cur };
        renderExamShell();
      }
    });
  });

  document.getElementById("btn-submit-exam").addEventListener("click", submitMockExam);
}

async function startMockExam() {
  const count = parseInt(document.getElementById("exam-count-sel").value, 10) || 3;
  const root = document.getElementById("exam-root");
  root.innerHTML = renderSkeleton(6);
  try {
    const data = await apiFetch(`/api/exam/generate?count_per_section=${count}`);
    state.exam.active = true;
    state.exam.examData = data;
    state.exam.answers = {};
    state.exam.elapsedSec = 0;
    state.exam.result = null;
    state.ui.exam.currentIndex = 0;
    if (state.exam.timerId) clearInterval(state.exam.timerId);
    state.exam.timerId = setInterval(() => {
      state.exam.elapsedSec += 1;
      const el = document.getElementById("exam-timer");
      if (el) el.textContent = formatExamTimer(state.exam.elapsedSec);
    }, 1000);
    renderExamShell();
  } catch (err) {
    root.innerHTML = renderErrorState(err.message, "btn-retry-exam");
    document.getElementById("btn-retry-exam").addEventListener("click", renderExamShell);
  }
}

async function submitMockExam() {
  const ex = state.exam.examData;
  if (!ex) return;
  const payloadItems = [];
  for (let i = 0; i < ex.items.length; i++) {
    const it = ex.items[i];
    const ans = state.exam.answers[it.question_id];
    if (it.interaction_type === "star_4slot") {
      if (!ans || !ans.slot_order || ans.slot_order.some((x) => x === null)) {
        if (state.ui.exam.layout === "single") {
          state.ui.exam.currentIndex = i;
          renderExamShell();
        }
        showToast(`Câu ${it.unit_code} (★) bắt buộc ghép đủ cả 4 ô trước khi nộp bài thi.`, true);
        return;
      }
      payloadItems.push({ question_id: it.question_id, slot_order: ans.slot_order, session_seed: ex.session_seed });
    } else {
      if (!ans || ans.selected_index === undefined) {
        if (state.ui.exam.layout === "single") {
          state.ui.exam.currentIndex = i;
          renderExamShell();
        }
        showToast("Hãy chọn đáp án cho tất cả các câu trước khi nộp bài thi.", true);
        return;
      }
      payloadItems.push({ question_id: it.question_id, selected_index: ans.selected_index, session_seed: ex.session_seed });
    }
  }

  try {
    const res = await apiFetch("/api/exam/submit", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ exam_mode: ex.exam_mode, answers: payloadItems, duration_sec: state.exam.elapsedSec }),
    });
    if (state.exam.timerId) clearInterval(state.exam.timerId);
    state.exam.active = false;
    state.exam.result = res;
    if (typeof res.error_count === "number") {
      updateNavErrorBadge(res.error_count);
    }
    renderExamShell();
  } catch (err) {
    showToast(err.message, true);
  }
}

/* Error Notebook & Excel Importer View */
async function loadNotebookView() {
  const root = document.getElementById("notebook-root");
  if (!root) return;
  root.innerHTML = `<div class="stack-md">${renderSkeleton(4)}${renderSkeleton(4)}</div>`;
  try {
    const [errData, wbData] = await Promise.all([apiFetch("/api/errors"), apiFetch("/api/workbooks")]);
    state.notebook.errors = errData.errors || [];
    state.notebook.workbooks = wbData.workbooks || [];
    updateNavErrorBadge(state.notebook.errors.length);
    renderNotebookView();
  } catch (err) {
    root.innerHTML = renderErrorState(err.message, "btn-retry-nb");
    document.getElementById("btn-retry-nb").addEventListener("click", loadNotebookView);
  }
}

function renderNotebookView() {
  const root = document.getElementById("notebook-root");
  if (!root) return;
  const errs = state.notebook.errors || [];
  const wbs = state.notebook.workbooks || [];
  const nbUi = state.ui.notebook;
  const hiddenNbCount = Object.values(nbUi).filter((v) => !v).length;

  const errContent = errs.length === 0
    ? renderEmptyState(
        "Tuyệt vời — Bạn chưa có câu nào cần làm lại (0 lỗi)",
        "Khi bạn trả lời sai ở mục Làm câu hỏi hoặc Thi thử, câu đó sẽ tự động hiện ở đây để bạn ôn lại cho tới khi đúng vững.",
        "Luyện câu hỏi đổi dạng",
        "btn-nb-to-study"
      )
    : `<div class="table-scroll-wrap">
         <table class="data-table">
           <thead><tr><th>Chủ đề</th><th>Dạng bài</th><th>Số lần sai</th><th>Từ khóa &amp; Đề bài</th><th>Thao tác</th></tr></thead>
           <tbody>
             ${errs.map((e) => `
               <tr>
                 <td><strong>${escapeHtml(e.unit_code)}</strong></td>
                 <td>${escapeHtml(e.mondai_type)}</td>
                 <td class="tabular-nums"><span class="badge danger">${e.lapses}</span></td>
                 <td class="min-w-0 break-anywhere">
                   <strong>${escapeHtml(e.focus_keyword)}</strong><br>
                   <span class="muted">${escapeHtml(e.prompt_jp)}</span>
                   ${renderGrammarBreakdownHtml(e.grammar_breakdown, { compact: true })}
                 </td>
                 <td><button type="button" class="btn-primary btn-sm btn-fix-err" data-qid="${e.question_id}" data-unit="${escapeHtml(e.unit_code)}">Làm lại ngay</button></td>
               </tr>
             `).join("")}
           </tbody>
         </table>
       </div>`;

  const wbRows = wbs.map((w) => `
    <tr>
      <td class="min-w-0 break-anywhere"><strong>${escapeHtml(w.filename)}</strong></td>
      <td><span class="badge">${escapeHtml(formatWorkbookLayoutVi(w.layout_type))}</span></td>
      <td class="tabular-nums">${w.raw_count}</td>
      <td class="tabular-nums"><strong>${w.imported_count}</strong></td>
      <td class="tabular-nums muted">${escapeHtml(w.imported_at)}</td>
    </tr>
  `).join("");

  const impBox = state.notebook.importResult
    ? `<div class="callout-success" style="margin-top:12px;">
         [OK] Đã nạp tệp <strong>${escapeHtml(state.notebook.importResult.filename)}</strong> (Mẫu đề: ${escapeHtml(formatWorkbookLayoutVi(state.notebook.importResult.layout_type))}) —
         Số câu trong file: ${state.notebook.importResult.raw_count} · Mới thêm: ${state.notebook.importResult.newly_imported_count} · Câu đổi dạng tạo thêm: ${state.notebook.importResult.variants_generated}
       </div>`
    : "";

  const restoreNbHtml = hiddenNbCount > 0
    ? `<div class="hidden-restore-bar" role="status">
         <span>Đang ẩn <strong>${hiddenNbCount}</strong> mục ở Câu sai &amp; Nạp đề.</span>
         <button type="button" id="btn-nb-restore-all" class="btn-secondary btn-sm">Hiện lại tất cả</button>
       </div>`
    : "";

  root.innerHTML = `
    <div class="stack-md">
      <div class="section-header">
        <h2 id="notebook-heading" class="section-title">Sổ tay Câu hay sai &amp; Nạp thêm Đề Excel</h2>
      </div>

      <div class="view-control-bar" role="region" aria-label="Tùy chỉnh hiển thị Sổ tay và Nạp đề">
        <div class="view-control-group">
          <span class="view-control-label">Hiển thị:</span>
          <button type="button" class="vis-chip ${nbUi.showErrors ? "is-on" : ""}" data-nb-vis="showErrors" aria-pressed="${nbUi.showErrors}">Câu hay sai</button>
          <button type="button" class="vis-chip ${nbUi.showUploader ? "is-on" : ""}" data-nb-vis="showUploader" aria-pressed="${nbUi.showUploader}">Nạp tệp Excel</button>
          <button type="button" class="vis-chip ${nbUi.showWorkbooks ? "is-on" : ""}" data-nb-vis="showWorkbooks" aria-pressed="${nbUi.showWorkbooks}">Danh sách đề đã nạp</button>
        </div>
      </div>

      <div id="nb-errors-card" class="card" ${nbUi.showErrors ? "" : "hidden"}>
        <h3 class="card-title">Danh sách câu cần làm lại</h3>
        ${errContent}
      </div>

      <div id="nb-uploader-card" class="card" ${nbUi.showUploader ? "" : "hidden"}>
        <h3 class="card-title">Nạp thêm tệp Đề thi Excel (.xlsx)</h3>
        <p class="muted">Bước 1: Chọn tệp <code>.xlsx</code> trên máy. Bước 2: Bấm nút <strong>Nạp tệp Excel</strong>. Hệ thống tự lọc câu trùng lặp và tạo câu đổi dạng để luyện thêm.</p>
        <form id="excel-upload-form" class="form-row">
          <div class="field">
            <label for="inp-xlsx-file">Chọn tệp .xlsx</label>
            <input id="inp-xlsx-file" type="file" accept=".xlsx" class="input">
          </div>
          <button type="submit" class="btn-primary">Nạp tệp Excel</button>
        </form>
        ${impBox}
      </div>

      <div id="nb-workbooks-card" class="card" ${nbUi.showWorkbooks ? "" : "hidden"}>
        <h3 class="card-title">Danh sách đề Excel đã nạp (${wbs.length} tệp)</h3>
        <div class="table-scroll-wrap">
          <table class="data-table">
            <thead><tr><th>Tên tệp</th><th>Dạng đề nhận diện</th><th>Số câu trong file</th><th>Số câu duy nhất đã nạp</th><th>Thời điểm</th></tr></thead>
            <tbody>${wbRows}</tbody>
          </table>
        </div>
      </div>

      ${restoreNbHtml}
    </div>
  `;

  root.querySelectorAll("[data-nb-vis]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const key = btn.dataset.nbVis;
      if (key in state.ui.notebook) {
        state.ui.notebook[key] = !state.ui.notebook[key];
        saveUiPreferences();
        renderNotebookView();
      }
    });
  });

  const nbRestoreBtn = document.getElementById("btn-nb-restore-all");
  if (nbRestoreBtn) {
    nbRestoreBtn.addEventListener("click", () => {
      for (const key of Object.keys(state.ui.notebook)) {
        state.ui.notebook[key] = true;
      }
      saveUiPreferences();
      renderNotebookView();
    });
  }

  const toStudyBtn = document.getElementById("btn-nb-to-study");
  if (toStudyBtn) {
    toStudyBtn.addEventListener("click", () => {
      state.study.mode = "variant";
      switchView("study");
      loadNextStudyItem();
    });
  }

  root.querySelectorAll(".btn-fix-err").forEach((btn) => {
    btn.addEventListener("click", () => {
      state.study.unitCode = btn.dataset.unit;
      state.study.mode = "remediation";
      switchView("study");
      loadNextStudyItem({ question_id: parseInt(btn.dataset.qid, 10) });
    });
  });

  document.getElementById("excel-upload-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const inp = document.getElementById("inp-xlsx-file");
    if (!inp.files || !inp.files.length) {
      showToast("Vui lòng chọn một tệp .xlsx để nạp.", true);
      return;
    }
    const fd = new FormData();
    fd.append("file", inp.files[0]);
    try {
      const res = await apiFetch("/api/import/excel", { method: "POST", body: fd });
      state.notebook.importResult = res.import_report;
      showToast("Đã nạp thành công tệp Excel mới!");
      await loadNotebookView();
    } catch (err) {
      showToast(err.message, true);
    }
  });

  bindGrammarChipButtons(root);
}

/* Dashboard Grammar Card & Post-Submit Grammar Breakdown */
function renderDashboardGrammarCard(gs, isHidden) {
  if (!gs) return "";
  const levelsHtml = (gs.levels || []).map((lv) => `
    <span class="badge ${lv.mastered > 0 && lv.mastered === lv.total ? "success" : "accent"} tabular-nums">
      [${escapeHtml(lv.level)}] ${lv.mastered}/${lv.total} (${Number(lv.coverage_pct || 0).toFixed(0)}%)
    </span>
  `).join("");

  return `
    <div id="dash-grammar-card" class="card" ${isHidden ? "hidden" : ""}>
      <div class="section-header" style="margin-bottom: 12px;">
        <div>
          <h3 class="card-title" style="margin-bottom: 4px;">Kho Ngữ pháp &amp; Từ vựng nền tảng (N5 &#8594; N2)</h3>
          <p class="muted">Tra cứu công thức ngữ pháp, từ vựng kèm bài tập liên kết trực tiếp với toàn bộ bộ đề .xlsx Cuối kì.</p>
        </div>
        <div class="row-wrap">
          <span class="badge accent tabular-nums">Liên kết đề .xlsx: ${gs.total_linked_questions || 0} câu</span>
          <button type="button" class="section-collapse-btn" data-dash-hide="grammarCard">Ẩn mục này</button>
        </div>
      </div>

      <div class="grammar-stats-row">
        <div class="grammar-stat-box">
          <div class="muted">Tổng mẫu Ngữ pháp</div>
          <div class="grammar-stat-num tabular-nums">${gs.total_points || 0}</div>
        </div>
        <div class="grammar-stat-box">
          <div class="muted">Có trong Đề cuối kì</div>
          <div class="grammar-stat-num tabular-nums">${gs.exam_corpus_count || 0}</div>
        </div>
        <div class="grammar-stat-box">
          <div class="muted">Mở rộng JLPT</div>
          <div class="grammar-stat-num tabular-nums">${gs.jlpt_extension_count || 0}</div>
        </div>
        <div class="grammar-stat-box">
          <div class="muted">Bài tập / Từ vựng</div>
          <div class="grammar-stat-num tabular-nums">${gs.total_drills || 0} / ${gs.vocab_foundation_count || 0}</div>
        </div>
      </div>

      <div class="row-wrap" style="margin-top: 12px;">${levelsHtml}</div>

      <div class="row-wrap" style="margin-top: 12px;">
        <button type="button" id="btn-dash-open-grammar-lib" class="btn-primary btn-sm">Tra cứu Ngữ pháp</button>
        <button type="button" id="btn-dash-open-grammar-drill" class="btn-secondary btn-sm">Làm bài tập Ngữ pháp</button>
      </div>
    </div>
  `;
}

function formatGrammarRoleLabel(role) {
  if (role === "primary_target") return "Trọng tâm câu";
  if (role === "distractor_trap") return "Bẫy nhiễu";
  if (role === "sentence_structure") return "Cấu trúc câu";
  if (role === "discourse_marker") return "Mạch văn bản";
  return role || "Liên kết";
}

function renderGrammarBreakdownHtml(gb, opts) {
  if (!gb) return "";
  const compact = Boolean(opts && opts.compact);
  const points = Array.isArray(gb.grammar_points) ? gb.grammar_points : [];
  const notes = Array.isArray(gb.option_grammar_notes) ? gb.option_grammar_notes : [];
  if (!gb.structure_parse_vi && !gb.pedagogical_takeaway_vi && !points.length && !notes.length) {
    return "";
  }

  const chipsHtml = points.map((gp) => `
    <button type="button" class="grammar-chip-btn" data-grammar-code="${escapeHtml(gp.code)}" title="${escapeHtml(gp.note_vi || gp.core_meaning_vi || "")}">
      <span>[${escapeHtml(gp.jlpt_level)}] ${escapeHtml(gp.pattern)}</span>
      <span class="muted">(${escapeHtml(formatGrammarRoleLabel(gp.role))})</span>
    </button>
  `).join("");

  const notesHtml = notes.length
    ? compact
      ? `<details style="margin-top:4px;"><summary class="muted" style="cursor:pointer;">Ghi chú ngữ pháp 4 phương án (${notes.length})</summary><ul class="stack-sm" style="margin:6px 0 0; padding-left:18px;">${notes.map((n) => `<li class="break-anywhere">${escapeHtml(n)}</li>`).join("")}</ul></details>`
      : `<div><strong>Phân tích ngữ pháp các phương án:</strong><ul class="stack-sm" style="margin:4px 0 0; padding-left:18px;">${notes.map((n) => `<li class="break-anywhere">${escapeHtml(n)}</li>`).join("")}</ul></div>`
    : "";

  return `
    <div class="grammar-breakdown-box" data-grammar-breakdown="1">
      <div class="row-wrap" style="justify-content: space-between;">
        <strong>Giải phẫu Ngữ pháp &amp; Bài học liên quan</strong>
        <span class="muted" style="font-size:12px;">Bấm vào thẻ mẫu để xem bài học chi tiết</span>
      </div>
      ${chipsHtml ? `<div class="row-wrap">${chipsHtml}</div>` : ""}
      ${gb.structure_parse_vi ? `<div class="break-anywhere" style="white-space: pre-wrap;"><strong>Cấu trúc câu:</strong> ${escapeHtml(gb.structure_parse_vi)}</div>` : ""}
      ${gb.pedagogical_takeaway_vi ? `<div class="break-anywhere"><strong>Mẹo tránh nhầm:</strong> ${escapeHtml(gb.pedagogical_takeaway_vi)}</div>` : ""}
      ${notesHtml}
    </div>
  `;
}

function bindGrammarChipButtons(container) {
  if (!container) return;
  container.querySelectorAll(".grammar-chip-btn[data-grammar-code]").forEach((btn) => {
    btn.addEventListener("click", () => {
      openGrammarModal(btn.dataset.grammarCode, btn);
    });
  });
}

/* Grammar & JLPT Hub View */
let grammarListReqSeq = 0;
let grammarDrillReqSeq = 0;
let vocabReqSeq = 0;
let grammarSearchTimer = null;
let vocabSearchTimer = null;

function jumpToStudyQuestion(questionId) {
  const qid = parseInt(questionId, 10);
  if (!Number.isFinite(qid)) return;
  closeGrammarModal(true);
  state.study.showBridge = false;
  state.study.mode = "original";
  switchView("study", true);
  loadNextStudyItem({ question_id: qid });
}

function jumpToGrammarDrill(grammarCode) {
  closeGrammarModal(true);
  state.grammar.subtab = "drill";
  state.grammar.drill.grammarCode = grammarCode || null;
  state.grammar.drill.drillType = "mixed";
  state.grammar.drill.scope = "all";
  state.grammar.drill.level = "ALL";
  state.grammar.drill.item = null;
  state.grammar.drill.emptyReason = null;
  state.grammar.drill.selectedOption = null;
  state.grammar.drill.result = null;
  state.grammar.drill.loading = false;
  switchView("grammar");
}

async function loadGrammarView() {
  const root = document.getElementById("grammar-root");
  if (!root) return;
  const hadOverview = Boolean(state.grammar.overview);
  if (!hadOverview) {
    root.innerHTML = `<div class="stack-md">${renderSkeleton(3)}${renderSkeleton(5)}</div>`;
  } else {
    renderGrammarShell();
  }

  try {
    const ov = await apiFetch("/api/grammar/overview");
    state.grammar.overview = ov;
    state.grammar.overviewError = null;
    if (state.dashboard) state.dashboard.grammar_summary = ov;
    if (!hadOverview) {
      renderGrammarShell();
    } else {
      const strip = document.getElementById("grammar-overview-strip");
      if (strip) {
        strip.innerHTML = renderGrammarOverviewStrip(ov);
        strip.hidden = !state.ui.grammar.showOverview;
      }
      if (state.grammar.subtab === "jlpt") renderJlptExpansionSubtab();
    }
  } catch (err) {
    state.grammar.overviewError = err.message;
    if (!hadOverview) {
      root.innerHTML = renderErrorState(err.message, "btn-retry-grammar-overview");
      const retryBtn = document.getElementById("btn-retry-grammar-overview");
      if (retryBtn) retryBtn.addEventListener("click", loadGrammarView);
    }
  }
}

function renderGrammarOverviewStrip(ov) {
  if (!ov) return "";
  return `
    <div class="grammar-stats-row">
      <div class="grammar-stat-box">
        <div class="muted">Tổng mẫu ngữ pháp</div>
        <div class="grammar-stat-num tabular-nums">${ov.total_points || 0}</div>
      </div>
      <div class="grammar-stat-box">
        <div class="muted">Bộ đề .xlsx Cuối kì</div>
        <div class="grammar-stat-num tabular-nums">${ov.exam_corpus_count || 0}</div>
      </div>
      <div class="grammar-stat-box">
        <div class="muted">Mở rộng JLPT</div>
        <div class="grammar-stat-num tabular-nums">${ov.jlpt_extension_count || 0}</div>
      </div>
      <div class="grammar-stat-box">
        <div class="muted">Mẫu đã vững / Câu đề có giải thích</div>
        <div class="grammar-stat-num tabular-nums">${ov.mastered_count || 0} / ${ov.total_linked_questions || 0}</div>
      </div>
    </div>
  `;
}

function renderGrammarShell() {
  const root = document.getElementById("grammar-root");
  if (!root) return;
  const ov = state.grammar.overview;
  const tab = state.grammar.subtab || "library";
  const gUi = state.ui.grammar;

  root.innerHTML = `
    <div class="stack-md">
      <div class="section-header">
        <div>
          <h2 id="grammar-heading" class="section-title">Ngữ pháp N5&#8594;N2, Từ vựng Nền tảng &amp; Lộ trình JLPT</h2>
          <p class="muted">Tra cứu công thức chia thể, nghĩa, cặp dễ nhầm và luyện tập gắn liền với bộ đề thi .xlsx.</p>
        </div>
      </div>

      <div class="view-control-bar" role="region" aria-label="Tùy chỉnh hiển thị khu Ngữ pháp">
        <div class="view-control-group">
          <button type="button" class="vis-chip ${gUi.showOverview ? "is-on" : ""}" data-grammar-vis="overview" aria-pressed="${gUi.showOverview}">Thống kê nhanh</button>
        </div>
        <div class="view-control-group">
          <span class="view-control-label">Cỡ chữ:</span>
          ${renderInlineFontScaleGroup()}
          <button type="button" class="btn-secondary btn-sm" data-enter-focus="grammar">${state.ui.focusMode ? "Thoát Tập trung (F)" : "Tập trung toàn màn hình (F)"}</button>
        </div>
      </div>

      <div id="grammar-overview-strip" ${gUi.showOverview ? "" : "hidden"}>${renderGrammarOverviewStrip(ov)}</div>

      <div class="subnav-tabs" role="tablist" aria-label="Phân khu Ngữ pháp và Từ vựng">
        <button type="button" class="subnav-btn ${tab === "library" ? "active" : ""}" data-grammar-tab="library" role="tab" aria-selected="${tab === "library"}">Tra cứu Ngữ pháp</button>
        <button type="button" class="subnav-btn ${tab === "drill" ? "active" : ""}" data-grammar-tab="drill" role="tab" aria-selected="${tab === "drill"}">Bài tập Ngữ pháp</button>
        <button type="button" class="subnav-btn ${tab === "vocab" ? "active" : ""}" data-grammar-tab="vocab" role="tab" aria-selected="${tab === "vocab"}">Từ vựng &amp; Chữ Hán</button>
        <button type="button" class="subnav-btn ${tab === "jlpt" ? "active" : ""}" data-grammar-tab="jlpt" role="tab" aria-selected="${tab === "jlpt"}">Lộ trình &amp; Mở rộng JLPT</button>
      </div>

      <div id="grammar-subtab-container"></div>
    </div>
  `;

  applyUiStateToRoot();
  bindCommonControlEvents(root);

  root.querySelectorAll("[data-grammar-vis=\"overview\"]").forEach((btn) => {
    btn.addEventListener("click", () => {
      state.ui.grammar.showOverview = !state.ui.grammar.showOverview;
      saveUiPreferences();
      const strip = document.getElementById("grammar-overview-strip");
      if (strip) strip.hidden = !state.ui.grammar.showOverview;
      btn.classList.toggle("is-on", state.ui.grammar.showOverview);
      btn.setAttribute("aria-pressed", state.ui.grammar.showOverview ? "true" : "false");
    });
  });

  root.querySelectorAll(".subnav-btn[data-grammar-tab]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const nextTab = btn.dataset.grammarTab;
      if (nextTab === state.grammar.subtab) return;
      state.grammar.subtab = nextTab;
      renderGrammarShell();
    });
  });

  if (tab === "library") renderGrammarLibrarySubtab();
  else if (tab === "drill") renderGrammarDrillSubtab();
  else if (tab === "vocab") renderVocabSubtab();
  else if (tab === "jlpt") renderJlptExpansionSubtab();
}

function navigateGrammarReader(delta) {
  const lib = state.grammar.library;
  if (!lib.points || !lib.points.length) return;
  let idx = lib.points.findIndex((p) => p.code === lib.selectedCode);
  if (idx < 0) idx = 0;
  const nextIdx = idx + delta;
  if (nextIdx < 0 || nextIdx >= lib.points.length) return;
  loadGrammarPointDetail(lib.points[nextIdx].code, false);
}

function renderGrammarReaderNav() {
  const sel = document.getElementById("reader-point-sel");
  const counter = document.getElementById("reader-pos-counter");
  const prevBtn = document.getElementById("btn-reader-prev");
  const nextBtn = document.getElementById("btn-reader-next");
  if (!sel && !counter && !prevBtn && !nextBtn) return;

  const lib = state.grammar.library;
  const pts = lib.points || [];
  let idx = pts.findIndex((p) => p.code === lib.selectedCode);
  if (idx < 0 && pts.length) idx = 0;

  if (sel) {
    sel.innerHTML = pts.length
      ? pts.map((pt) => `<option value="${escapeHtml(pt.code)}" ${pt.code === lib.selectedCode ? "selected" : ""}>[${escapeHtml(pt.jlpt_level)}] ${escapeHtml(pt.pattern)} — ${escapeHtml(pt.core_meaning_vi)}</option>`).join("")
      : `<option value="">Không có mẫu ngữ pháp</option>`;
    sel.disabled = !pts.length;
  }
  if (counter) {
    counter.textContent = pts.length ? `${idx + 1} / ${pts.length}` : "0 / 0";
  }
  if (prevBtn) prevBtn.disabled = !pts.length || idx <= 0;
  if (nextBtn) nextBtn.disabled = !pts.length || idx >= pts.length - 1;
}

/* Subtab 1: Thư viện Ngữ pháp */
function renderGrammarLibrarySubtab() {
  const container = document.getElementById("grammar-subtab-container");
  if (!container) return;
  const lib = state.grammar.library;
  const gUi = state.ui.grammar;
  const isReader = gUi.libraryLayout === "reader";
  const ovCats = (state.grammar.overview && state.grammar.overview.categories) || lib.categories || [];
  const catOptions = [
    `<option value="" ${lib.category === "" ? "selected" : ""}>Tất cả danh mục</option>`,
    ...ovCats.map((c) => `<option value="${escapeHtml(c.category)}" ${lib.category === c.category ? "selected" : ""}>${escapeHtml(c.category_label_vi || c.category)}</option>`),
  ].join("");

  const stageHtml = isReader
    ? `<div id="grammar-reader-shell" class="stack-md">
         <div class="reader-nav-bar">
           <button type="button" id="btn-reader-prev" class="btn-secondary btn-sm">Bài trước ([)</button>
           <select id="reader-point-sel" class="select" aria-label="Chọn mẫu ngữ pháp để đọc"></select>
           <span id="reader-pos-counter" class="muted tabular-nums">0 / 0</span>
           <button type="button" id="btn-reader-next" class="btn-primary btn-sm">Bài tiếp (])</button>
         </div>
         <div id="grammar-detail-panel" class="grammar-reader-stage min-w-0"></div>
       </div>`
    : `<div class="grammar-split ${gUi.showListPane ? "" : "list-hidden"}">
         <div id="grammar-library-results" class="grammar-list-pane" ${gUi.showListPane ? "" : "hidden"}></div>
         <div id="grammar-detail-panel" class="card min-w-0"></div>
       </div>`;

  container.innerHTML = `
    <div class="stack-md">
      <div class="view-control-bar" role="region" aria-label="Tùy chỉnh hiển thị Tra cứu Ngữ pháp">
        <div class="view-control-group">
          <div class="mode-seg-group" role="group" aria-label="Bố cục đọc Ngữ pháp">
            <button type="button" class="mode-seg-btn ${!isReader ? "active" : ""}" data-grammar-layout="split" aria-pressed="${!isReader}">Chia 2 cột</button>
            <button type="button" class="mode-seg-btn ${isReader ? "active" : ""}" data-grammar-layout="reader" aria-pressed="${isReader}">Đọc tập trung từng bài</button>
          </div>
        </div>
        <div class="view-control-group">
          <button type="button" class="vis-chip ${gUi.showFilter ? "is-on" : ""}" data-grammar-vis="filter" aria-pressed="${gUi.showFilter}">Bộ lọc</button>
          <button type="button" class="vis-chip ${gUi.showListPane ? "is-on" : ""}" data-grammar-vis="listPane" aria-pressed="${gUi.showListPane}" ${isReader ? "disabled title=\"Đang ở chế độ đọc từng bài\"" : ""}>Danh sách trái</button>
          <button type="button" class="vis-chip ${gUi.maskExampleVi ? "is-on" : ""}" data-grammar-vis="maskExampleVi" aria-pressed="${gUi.maskExampleVi}">Che nghĩa tiếng Việt ở Ví dụ</button>
        </div>
      </div>

      <div id="grammar-lib-filter-card" class="card" ${gUi.showFilter ? "" : "hidden"}>
        <div class="grammar-filter-bar">
          <div class="field">
            <label for="grammar-scope-sel">Nguồn bài học</label>
            <select id="grammar-scope-sel" class="select">
              <option value="all" ${lib.scope === "all" ? "selected" : ""}>Tất cả (Đề thi + Giáo trình)</option>
              <option value="exam" ${lib.scope === "exam" ? "selected" : ""}>[THI CUỐI KÌ] Bộ đề .xlsx</option>
              <option value="jlpt" ${lib.scope === "jlpt" ? "selected" : ""}>[MỞ RỘNG JLPT] Giáo trình</option>
            </select>
          </div>
          <div class="field">
            <label for="grammar-level-sel">Cấp độ JLPT</label>
            <select id="grammar-level-sel" class="select">
              <option value="ALL" ${lib.level === "ALL" ? "selected" : ""}>Tất cả (N5–N2)</option>
              <option value="N5" ${lib.level === "N5" ? "selected" : ""}>N5</option>
              <option value="N4" ${lib.level === "N4" ? "selected" : ""}>N4</option>
              <option value="N3" ${lib.level === "N3" ? "selected" : ""}>N3</option>
              <option value="N2" ${lib.level === "N2" ? "selected" : ""}>N2</option>
            </select>
          </div>
          <div class="field">
            <label for="grammar-category-sel">Danh mục</label>
            <select id="grammar-category-sel" class="select">${catOptions}</select>
          </div>
          <div class="field">
            <label for="grammar-state-sel">Mức độ thuộc</label>
            <select id="grammar-state-sel" class="select">
              <option value="" ${lib.state === "" ? "selected" : ""}>Tất cả mức độ</option>
              <option value="new" ${lib.state === "new" ? "selected" : ""}>Chưa học</option>
              <option value="learning" ${lib.state === "learning" ? "selected" : ""}>Đang học</option>
              <option value="review" ${lib.state === "review" ? "selected" : ""}>Đang ôn định kỳ</option>
              <option value="relearning" ${lib.state === "relearning" ? "selected" : ""}>Hay sai · Cần ôn lại</option>
            </select>
          </div>
          <div class="field" style="flex: 1.5 1 200px;">
            <label for="grammar-search-inp">Tìm kiếm mẫu / nghĩa</label>
            <input id="grammar-search-inp" type="search" class="input" placeholder="VD: ために, わけ, giả định..." value="${escapeHtml(lib.q)}">
          </div>
          <button type="button" id="btn-grammar-search" class="btn-primary">Lọc</button>
        </div>
      </div>

      ${stageHtml}
    </div>
  `;

  applyUiStateToRoot();

  container.querySelectorAll("[data-grammar-layout]").forEach((btn) => {
    btn.addEventListener("click", () => {
      state.ui.grammar.libraryLayout = btn.dataset.grammarLayout === "reader" ? "reader" : "split";
      saveUiPreferences();
      renderGrammarLibrarySubtab();
    });
  });

  container.querySelectorAll("[data-grammar-vis]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const kind = btn.dataset.grammarVis;
      if (kind === "filter") state.ui.grammar.showFilter = !state.ui.grammar.showFilter;
      else if (kind === "listPane") state.ui.grammar.showListPane = !state.ui.grammar.showListPane;
      else if (kind === "maskExampleVi") state.ui.grammar.maskExampleVi = !state.ui.grammar.maskExampleVi;
      saveUiPreferences();
      renderGrammarLibrarySubtab();
    });
  });

  const readerPrev = document.getElementById("btn-reader-prev");
  if (readerPrev) readerPrev.addEventListener("click", () => navigateGrammarReader(-1));
  const readerNext = document.getElementById("btn-reader-next");
  if (readerNext) readerNext.addEventListener("click", () => navigateGrammarReader(1));
  const readerSel = document.getElementById("reader-point-sel");
  if (readerSel) {
    readerSel.addEventListener("change", (e) => {
      if (e.target.value) loadGrammarPointDetail(e.target.value, false);
    });
  }

  document.getElementById("grammar-scope-sel").addEventListener("change", (e) => {
    lib.scope = e.target.value;
    loadGrammarLibrary();
  });
  document.getElementById("grammar-level-sel").addEventListener("change", (e) => {
    lib.level = e.target.value;
    loadGrammarLibrary();
  });
  document.getElementById("grammar-category-sel").addEventListener("change", (e) => {
    lib.category = e.target.value;
    loadGrammarLibrary();
  });
  document.getElementById("grammar-state-sel").addEventListener("change", (e) => {
    lib.state = e.target.value;
    loadGrammarLibrary();
  });
  const searchInp = document.getElementById("grammar-search-inp");
  searchInp.addEventListener("input", () => {
    lib.q = searchInp.value;
    if (grammarSearchTimer) clearTimeout(grammarSearchTimer);
    grammarSearchTimer = setTimeout(() => loadGrammarLibrary(), 250);
  });
  searchInp.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      if (grammarSearchTimer) clearTimeout(grammarSearchTimer);
      lib.q = searchInp.value;
      loadGrammarLibrary();
    }
  });
  document.getElementById("btn-grammar-search").addEventListener("click", () => {
    lib.q = searchInp.value;
    loadGrammarLibrary();
  });

  if (lib.loaded && !lib.loading && !lib.error) {
    if (isReader && lib.points.length) {
      const stillValid = lib.selectedCode && lib.points.some((p) => p.code === lib.selectedCode);
      if (!stillValid) {
        loadGrammarPointDetail(lib.points[0].code, false);
        return;
      }
      if (!lib.detail && !lib.detailLoading) {
        loadGrammarPointDetail(lib.selectedCode, false);
        return;
      }
    }
    renderGrammarLibraryList();
    renderGrammarReaderNav();
    renderGrammarDetailPanel();
  } else {
    loadGrammarLibrary();
    renderGrammarReaderNav();
    renderGrammarDetailPanel();
  }
}

async function loadGrammarLibrary() {
  const lib = state.grammar.library;
  const reqSeq = ++grammarListReqSeq;
  lib.loading = true;
  lib.error = null;
  renderGrammarLibraryList();

  const params = new URLSearchParams();
  params.set("scope", lib.scope || "all");
  if (lib.level && lib.level !== "ALL") params.set("level", lib.level);
  if (lib.category) params.set("category", lib.category);
  if (lib.state) params.set("state", lib.state);
  if (lib.q && lib.q.trim()) params.set("q", lib.q.trim());

  try {
    const res = await apiFetch("/api/grammar/points?" + params.toString());
    if (reqSeq !== grammarListReqSeq) return;
    lib.points = res.points || [];
    lib.total = res.total || lib.points.length;
    if (Array.isArray(res.categories) && res.categories.length) {
      lib.categories = res.categories;
    }
    lib.loaded = true;
    lib.loading = false;
    renderGrammarLibraryList();
    if (state.ui.grammar.libraryLayout === "reader" && lib.points.length) {
      const hasSelected = lib.selectedCode && lib.points.some((p) => p.code === lib.selectedCode);
      if (!hasSelected) {
        loadGrammarPointDetail(lib.points[0].code, false);
        return;
      }
    }
    renderGrammarReaderNav();
  } catch (err) {
    if (reqSeq !== grammarListReqSeq) return;
    lib.loading = false;
    lib.error = err.message;
    renderGrammarLibraryList();
    renderGrammarReaderNav();
  }
}

function renderGrammarLibraryList() {
  const box = document.getElementById("grammar-library-results");
  if (!box) return;
  const lib = state.grammar.library;

  if (lib.loading) {
    box.innerHTML = `<div class="stack-sm">${renderSkeleton(4)}${renderSkeleton(4)}</div>`;
    return;
  }
  if (lib.error) {
    box.innerHTML = renderErrorState(lib.error, "btn-retry-grammar-list");
    const retry = document.getElementById("btn-retry-grammar-list");
    if (retry) retry.addEventListener("click", loadGrammarLibrary);
    return;
  }
  if (!lib.points.length) {
    box.innerHTML = renderEmptyState(
      "Không tìm thấy mẫu ngữ pháp phù hợp",
      "Thử nới lỏng bộ lọc cấp độ, phạm vi hoặc từ khóa tìm kiếm.",
      "Đặt lại bộ lọc",
      "btn-reset-grammar-lib"
    );
    const resetBtn = document.getElementById("btn-reset-grammar-lib");
    if (resetBtn) {
      resetBtn.addEventListener("click", () => {
        lib.scope = "all";
        lib.level = "ALL";
        lib.category = "";
        lib.state = "";
        lib.q = "";
        lib.loaded = false;
        renderGrammarLibrarySubtab();
      });
    }
    return;
  }

  const cardsHtml = lib.points.map((pt) => {
    const f = pt.fsrs || {};
    const sourceBadge = pt.in_exam_corpus
      ? `<span class="badge success">[THI CUỐI KÌ]</span>`
      : `<span class="badge">[MỞ RỘNG JLPT]</span>`;
    const stateBadge = f.mastered
      ? `<span class="badge success">${formatMasteryStateVi(f)}</span>`
      : f.state === "relearning"
      ? `<span class="badge danger">${formatMasteryStateVi(f)}</span>`
      : `<span class="badge">${escapeHtml(formatMasteryStateVi(f))}</span>`;
    return `
      <button type="button" class="grammar-point-card ${lib.selectedCode === pt.code ? "active" : ""}" data-grammar-code="${escapeHtml(pt.code)}">
        <div class="row-wrap" style="justify-content: space-between;">
          <div class="row-wrap">
            <span class="badge accent">[${escapeHtml(pt.jlpt_level)}]</span>
            ${sourceBadge}
          </div>
          ${stateBadge}
        </div>
        <div class="grammar-pattern-title">${escapeHtml(pt.pattern)}</div>
        <div class="grammar-formula-box">${escapeHtml(pt.formation_formula)}</div>
        <div class="muted break-anywhere">${escapeHtml(pt.core_meaning_vi)}</div>
        <div class="row-wrap muted tabular-nums" style="font-size:12px;">
          <span>${escapeHtml(pt.code)}</span>
          <span>· ${pt.linked_question_count || 0} câu đề</span>
          <span>· ${pt.drill_count || 0} bài luyện</span>
        </div>
      </button>
    `;
  }).join("");

  box.innerHTML = `
    <div class="stack-sm">
      <div class="muted tabular-nums">Hiển thị <strong>${lib.points.length}</strong> mẫu ngữ pháp</div>
      <div class="stack-sm">${cardsHtml}</div>
    </div>
  `;

  box.querySelectorAll(".grammar-point-card[data-grammar-code]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const code = btn.dataset.grammarCode;
      loadGrammarPointDetail(code, true);
    });
  });
}

async function loadGrammarPointDetail(code, scrollOnMobile) {
  const lib = state.grammar.library;
  lib.selectedCode = code;
  lib.detail = null;
  lib.detailLoading = true;
  lib.detailError = null;
  renderGrammarLibraryList();
  renderGrammarReaderNav();
  renderGrammarDetailPanel();

  if (scrollOnMobile && window.innerWidth <= 960) {
    const panel = document.getElementById("grammar-detail-panel");
    if (panel) panel.scrollIntoView({ behavior: "smooth", block: "nearest" });
  }

  try {
    const detail = await apiFetch(`/api/grammar/points/${encodeURIComponent(code)}`);
    if (lib.selectedCode !== code) return;
    lib.detail = detail;
    lib.detailLoading = false;
    renderGrammarReaderNav();
    renderGrammarDetailPanel();
  } catch (err) {
    if (lib.selectedCode !== code) return;
    lib.detailLoading = false;
    lib.detailError = err.message;
    renderGrammarDetailPanel();
  }
}

function renderGrammarDetailPanel() {
  const panel = document.getElementById("grammar-detail-panel");
  if (!panel) return;
  const lib = state.grammar.library;

  if (lib.detailLoading) {
    panel.innerHTML = renderSkeleton(6);
    return;
  }
  if (lib.detailError) {
    panel.innerHTML = renderErrorState(lib.detailError, "btn-retry-grammar-detail");
    const retry = document.getElementById("btn-retry-grammar-detail");
    if (retry) retry.addEventListener("click", () => loadGrammarPointDetail(lib.selectedCode));
    return;
  }
  if (!lib.detail) {
    if (state.ui.grammar.libraryLayout === "reader" && !lib.loading && !lib.points.length) {
      panel.innerHTML = renderEmptyState(
        "Chưa có mẫu ngữ pháp phù hợp bộ lọc",
        "Hãy mở Bộ lọc hoặc đặt lại điều kiện lọc để xem bài học.",
        "",
        ""
      );
      return;
    }
    panel.innerHTML = renderEmptyState(
      "Chọn một mẫu ngữ pháp bên cạnh để xem bài học",
      "Mỗi bài học gồm công thức chia thể, bản chất ý nghĩa, mẹo tránh nhầm, ví dụ tiếng Nhật và các câu hỏi liên quan trong đề .xlsx.",
      "",
      ""
    );
    return;
  }

  panel.innerHTML = renderGrammarLessonHtml(lib.detail, { inModal: false });
  bindGrammarLessonActions(panel, { inModal: false });
}

function renderGrammarLessonHtml(detail, opts) {
  const f = detail.fsrs || {};
  const secUi = state.ui.grammar.lessonSections;
  const hiddenSecCount = Object.values(secUi).filter((v) => !v).length;
  const inModal = Boolean(opts && opts.inModal);

  const formRows = (detail.formation_table || []).map((row) => `
    <tr>
      <td><strong>${escapeHtml(row.pos)}</strong></td>
      <td class="break-anywhere">${escapeHtml(row.rule)}</td>
    </tr>
  `).join("");

  const formTableHtml = formRows
    ? `<div class="table-scroll-wrap" style="margin-top:8px;">
         <table class="data-table">
           <thead><tr><th>Từ loại</th><th>Quy tắc kết hợp</th></tr></thead>
           <tbody>${formRows}</tbody>
         </table>
       </div>`
    : "";

  const pairsHtml = (detail.confusable_pairs || []).length
    ? detail.confusable_pairs.map((cp) => `
        <div class="confusable-card stack-sm">
          <div><strong>Dễ nhầm với: ${escapeHtml(cp.rival_pattern)}</strong></div>
          <div class="break-anywhere">${escapeHtml(cp.difference_vi)}</div>
          ${cp.quick_test_vi ? `<div class="muted break-anywhere"><strong>Mẹo kiểm tra nhanh:</strong> ${escapeHtml(cp.quick_test_vi)}</div>` : ""}
        </div>
      `).join("")
    : `<p class="muted">Chưa ghi nhận cặp dễ nhầm riêng cho mẫu này.</p>`;

  const examplesHtml = (detail.examples || []).map((ex, idx) => {
    const exKey = `${detail.code}::${idx}`;
    const isMasked = state.ui.grammar.maskExampleVi && !state.ui.revealedExamples[exKey];
    const viContent = isMasked
      ? `<div><button type="button" class="self-mask-btn" data-reveal-ex="${escapeHtml(exKey)}">Xem nghĩa tiếng Việt</button></div>`
      : `<div class="break-anywhere">${escapeHtml(ex.vi)}</div>
         ${ex.grammar_note ? `<div class="muted break-anywhere"><strong>Ghi chú:</strong> ${escapeHtml(ex.grammar_note)}</div>` : ""}`;
    return `
      <div class="example-item stack-sm">
        <div class="example-jp">${escapeHtml(ex.jp)}</div>
        ${ex.reading_note ? `<div class="muted">${escapeHtml(ex.reading_note)}</div>` : ""}
        ${viContent}
      </div>
    `;
  }).join("");

  const linkedHtml = (detail.linked_questions || []).length
    ? detail.linked_questions.map((lq) => `
        <div class="example-item stack-sm">
          <div class="row-wrap" style="justify-content: space-between;">
            <div class="row-wrap">
              <span class="badge accent">${escapeHtml(lq.unit_code)}</span>
              <span class="badge">${escapeHtml(lq.mondai_type)}</span>
              <span class="badge">${escapeHtml(formatGrammarRoleLabel(lq.role))}</span>
            </div>
            <button type="button" class="btn-secondary btn-sm btn-jump-question" data-qid="${lq.question_id}">Giải câu hỏi này</button>
          </div>
          <div class="break-anywhere" style="font-weight: 600;">${escapeHtml(lq.prompt_jp)}</div>
          ${lq.note_vi ? `<div class="muted break-anywhere">${escapeHtml(lq.note_vi)}</div>` : ""}
        </div>
      `).join("")
    : `<p class="muted">Chưa có câu hỏi thuộc mẫu này trong bộ đề .xlsx đã nạp. Bạn có thể bấm "Luyện Phản xạ Mẫu này" để luyện ngay.</p>`;

  const drillsInfo = detail.drills_summary || { total: 0, by_type: {} };

  const secControlBar = `
    <div class="view-control-bar" role="region" aria-label="Ẩn hiện từng mục trong bài học ngữ pháp">
      <div class="view-control-group">
        <span class="view-control-label">Mục bài học:</span>
        <button type="button" class="vis-chip ${secUi.sec1Formula ? "is-on" : ""}" data-lesson-sec="sec1Formula" aria-pressed="${secUi.sec1Formula}">[1] Công thức</button>
        <button type="button" class="vis-chip ${secUi.sec2Meaning ? "is-on" : ""}" data-lesson-sec="sec2Meaning" aria-pressed="${secUi.sec2Meaning}">[2] Nghĩa</button>
        <button type="button" class="vis-chip ${secUi.sec3Confusable ? "is-on" : ""}" data-lesson-sec="sec3Confusable" aria-pressed="${secUi.sec3Confusable}">[3] Dễ nhầm</button>
        <button type="button" class="vis-chip ${secUi.sec4Examples ? "is-on" : ""}" data-lesson-sec="sec4Examples" aria-pressed="${secUi.sec4Examples}">[4] Ví dụ</button>
        <button type="button" class="vis-chip ${secUi.sec5LinkedQuestions ? "is-on" : ""}" data-lesson-sec="sec5LinkedQuestions" aria-pressed="${secUi.sec5LinkedQuestions}">[5] Câu đề</button>
      </div>
      <div class="view-control-group">
        <button type="button" ${inModal ? "" : 'id="btn-lesson-expand-all"'} class="btn-ghost btn-sm" data-lesson-action="expand">Mở hết</button>
        <button type="button" ${inModal ? "" : 'id="btn-lesson-collapse-all"'} class="btn-ghost btn-sm" data-lesson-action="collapse">Thu gọn hết</button>
      </div>
    </div>
  `;

  const allHiddenRestore = hiddenSecCount === 5
    ? `<div class="hidden-restore-bar" role="status">
         <span>Đang thu gọn toàn bộ 5 mục bài học.</span>
         <button type="button" class="btn-secondary btn-sm" data-lesson-action="expand">Hiện lại cả 5 mục</button>
       </div>`
    : "";

  return `
    <div class="grammar-lesson-block">
      <div class="section-header" style="margin-bottom: 0;">
        <div class="min-w-0">
          <div class="row-wrap" style="margin-bottom: 6px;">
            <span class="badge accent">[${escapeHtml(detail.jlpt_level)}]</span>
            <span class="badge ${detail.in_exam_corpus ? "success" : ""}">${detail.in_exam_corpus ? "[THI CUỐI KÌ]" : "[MỞ RỘNG JLPT]"}</span>
            <span class="badge">${escapeHtml(detail.category_label_vi || detail.category)}</span>
            ${detail.register_tag ? `<span class="badge">${escapeHtml(detail.register_tag)}</span>` : ""}
          </div>
          ${inModal ? "" : `<h3 class="section-title break-anywhere">${escapeHtml(detail.pattern)} <span class="muted" style="font-size:13px;">(${escapeHtml(detail.code)})</span></h3>`}
          <div class="muted break-anywhere">${escapeHtml(detail.core_meaning_vi)}</div>
        </div>
        <button type="button" class="btn-primary btn-sm btn-practice-grammar" data-grammar-code="${escapeHtml(detail.code)}">
          Luyện Phản xạ Mẫu này (${drillsInfo.total || 0})
        </button>
      </div>

      <div class="row-wrap">
        <span class="badge ${f.formation_passed ? "success" : ""}">Chia thể: ${f.formation_passed ? "[OK] Đạt" : "Chưa làm"}</span>
        <span class="badge ${f.contrast_passed ? "success" : ""}">Phân biệt cặp dễ nhầm: ${f.contrast_passed ? "[OK] Đạt" : "Chưa làm"}</span>
        <span class="badge ${f.application_passed ? "success" : ""}">Dùng trong câu: ${f.application_passed ? "[OK] Đạt" : "Chưa làm"}</span>
        <span class="muted tabular-nums" style="font-size:12px;">Mức độ: ${escapeHtml(formatMasteryStateVi(f))} · Số lần nhầm: ${f.lapses || 0}</span>
      </div>

      ${secControlBar}
      ${allHiddenRestore}

      <div class="grammar-dim-box" data-lesson-box="sec1Formula" ${secUi.sec1Formula ? "" : "hidden"}>
        <h4 class="grammar-dim-title">[1] Công thức chia thể &amp; Bảng kết hợp</h4>
        <div class="grammar-formula-box">${escapeHtml(detail.formation_formula)}</div>
        ${formTableHtml}
      </div>

      <div class="grammar-dim-box" data-lesson-box="sec2Meaning" ${secUi.sec2Meaning ? "" : "hidden"}>
        <h4 class="grammar-dim-title">[2] Bản chất ngữ nghĩa &amp; Ngữ dụng</h4>
        <div class="break-anywhere" style="white-space: pre-wrap;">${escapeHtml(detail.deep_explanation_vi)}</div>
        ${detail.source_ref ? `<div class="muted" style="margin-top:8px;"><strong>Nguồn giáo trình:</strong> ${escapeHtml(detail.source_ref)}</div>` : ""}
      </div>

      <div class="grammar-dim-box stack-sm" data-lesson-box="sec3Confusable" ${secUi.sec3Confusable ? "" : "hidden"}>
        <h4 class="grammar-dim-title" style="margin-bottom:0;">[3] Cặp dễ nhầm cho người Việt</h4>
        ${pairsHtml}
      </div>

      <div class="grammar-dim-box stack-sm" data-lesson-box="sec4Examples" ${secUi.sec4Examples ? "" : "hidden"}>
        <h4 class="grammar-dim-title" style="margin-bottom:0;">[4] Ví dụ giáo trình</h4>
        ${examplesHtml}
      </div>

      <div class="grammar-dim-box stack-sm" data-lesson-box="sec5LinkedQuestions" ${secUi.sec5LinkedQuestions ? "" : "hidden"}>
        <h4 class="grammar-dim-title" style="margin-bottom:0;">[5] Câu hỏi bộ đề .xlsx liên kết (${(detail.linked_questions || []).length})</h4>
        ${linkedHtml}
      </div>
    </div>
  `;
}

function rerenderLessonContainer(container, opts) {
  const inModal = Boolean(opts && opts.inModal);
  if (inModal) {
    if (!state.grammarModalDetail) return;
    const prevTop = container.scrollTop;
    container.innerHTML = renderGrammarLessonHtml(state.grammarModalDetail, { inModal: true });
    bindGrammarLessonActions(container, { inModal: true });
    container.scrollTop = prevTop;
  } else {
    const prevWinY = window.scrollY;
    renderGrammarDetailPanel();
    if (Math.abs(window.scrollY - prevWinY) > 4) {
      window.scrollTo({ top: prevWinY });
    }
  }
}

function bindGrammarLessonActions(container, opts) {
  if (!container) return;
  container.querySelectorAll(".btn-jump-question[data-qid]").forEach((btn) => {
    btn.addEventListener("click", () => {
      jumpToStudyQuestion(btn.dataset.qid);
    });
  });
  container.querySelectorAll(".btn-practice-grammar[data-grammar-code]").forEach((btn) => {
    btn.addEventListener("click", () => {
      jumpToGrammarDrill(btn.dataset.grammarCode);
    });
  });
  container.querySelectorAll("[data-lesson-sec]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const key = btn.dataset.lessonSec;
      if (key in state.ui.grammar.lessonSections) {
        state.ui.grammar.lessonSections[key] = !state.ui.grammar.lessonSections[key];
        saveUiPreferences();
        rerenderLessonContainer(container, opts);
      }
    });
  });
  container.querySelectorAll("[data-lesson-action]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const expand = btn.dataset.lessonAction === "expand";
      for (const key of Object.keys(state.ui.grammar.lessonSections)) {
        state.ui.grammar.lessonSections[key] = expand;
      }
      saveUiPreferences();
      rerenderLessonContainer(container, opts);
    });
  });
  container.querySelectorAll("[data-reveal-ex]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const key = btn.dataset.revealEx;
      state.ui.revealedExamples[key] = true;
      rerenderLessonContainer(container, opts);
    });
  });
}

/* Subtab 2: Luyện Ngữ pháp Sư phạm */
function renderGrammarDrillSubtab() {
  const container = document.getElementById("grammar-subtab-container");
  if (!container) return;
  const dr = state.grammar.drill;
  const gUi = state.ui.grammar;
  const dfb = gUi.drillFeedback;

  container.innerHTML = `
    <div class="stack-md">
      <div class="view-control-bar" role="region" aria-label="Tùy chỉnh hiển thị Bài tập Ngữ pháp">
        <div class="view-control-group">
          <button type="button" class="vis-chip ${gUi.drillShowFilter ? "is-on" : ""}" data-drill-vis="filter" aria-pressed="${gUi.drillShowFilter}">Bộ lọc</button>
          <span class="view-control-label">Sau khi nộp:</span>
          <button type="button" class="vis-chip ${dfb.showTranslation ? "is-on" : ""}" data-drill-fb="showTranslation" aria-pressed="${dfb.showTranslation}">Dịch nghĩa</button>
          <button type="button" class="vis-chip ${dfb.showExplanation ? "is-on" : ""}" data-drill-fb="showExplanation" aria-pressed="${dfb.showExplanation}">Giải thích</button>
          <button type="button" class="vis-chip ${dfb.showDiagnostics ? "is-on" : ""}" data-drill-fb="showDiagnostics" aria-pressed="${dfb.showDiagnostics}">Chẩn đoán 4 đáp án</button>
        </div>
        <div class="view-control-group">
          ${renderInlineFontScaleGroup()}
          <button type="button" class="btn-secondary btn-sm" data-enter-focus="drill">${state.ui.focusMode ? "Thoát Tập trung (F)" : "Tập trung làm bài (F)"}</button>
        </div>
      </div>

      <div id="grammar-drill-filter-card" class="card" ${gUi.drillShowFilter ? "" : "hidden"}>
        <div class="grammar-filter-bar" style="justify-content: space-between;">
          <div class="grammar-filter-bar" style="flex: 1 1 auto;">
            <div class="field">
              <label for="drill-type-sel">Chế độ luyện</label>
              <select id="drill-type-sel" class="select">
                <option value="mixed" ${dr.drillType === "mixed" ? "selected" : ""}>Tổng hợp 3 bước</option>
                <option value="formation" ${dr.drillType === "formation" ? "selected" : ""}>Chia thể &amp; Kết hợp</option>
                <option value="contrast" ${dr.drillType === "contrast" ? "selected" : ""}>Phân biệt cặp dễ nhầm</option>
                <option value="application" ${dr.drillType === "application" ? "selected" : ""}>Ứng dụng ngữ cảnh</option>
              </select>
            </div>
            <div class="field">
              <label for="drill-scope-sel">Nguồn bài học</label>
              <select id="drill-scope-sel" class="select">
                <option value="all" ${dr.scope === "all" ? "selected" : ""}>Tất cả (Đề thi + Giáo trình)</option>
                <option value="exam" ${dr.scope === "exam" ? "selected" : ""}>Bộ đề .xlsx Cuối kì</option>
                <option value="jlpt" ${dr.scope === "jlpt" ? "selected" : ""}>Mở rộng JLPT</option>
              </select>
            </div>
            <div class="field">
              <label for="drill-level-sel">Cấp độ JLPT</label>
              <select id="drill-level-sel" class="select">
                <option value="ALL" ${dr.level === "ALL" ? "selected" : ""}>Tất cả (N5–N2)</option>
                <option value="N5" ${dr.level === "N5" ? "selected" : ""}>N5</option>
                <option value="N4" ${dr.level === "N4" ? "selected" : ""}>N4</option>
                <option value="N3" ${dr.level === "N3" ? "selected" : ""}>N3</option>
                <option value="N2" ${dr.level === "N2" ? "selected" : ""}>N2</option>
              </select>
            </div>
          </div>
          <div class="row-wrap">
            ${dr.grammarCode ? `<span class="badge accent">Đang lọc mẫu: ${escapeHtml(dr.grammarCode)}</span><button type="button" id="btn-clear-grammar-filter" class="btn-secondary btn-sm">Luyện toàn bộ</button>` : ""}
            <button type="button" id="btn-reload-grammar-drill" class="btn-secondary btn-sm">Đổi câu khác</button>
          </div>
        </div>
      </div>

      <div id="grammar-drill-stage"></div>
    </div>
  `;

  applyUiStateToRoot();
  bindCommonControlEvents(container);

  container.querySelectorAll("[data-drill-vis=\"filter\"]").forEach((btn) => {
    btn.addEventListener("click", () => {
      state.ui.grammar.drillShowFilter = !state.ui.grammar.drillShowFilter;
      saveUiPreferences();
      const fc = document.getElementById("grammar-drill-filter-card");
      if (fc) fc.hidden = !state.ui.grammar.drillShowFilter;
      btn.classList.toggle("is-on", state.ui.grammar.drillShowFilter);
      btn.setAttribute("aria-pressed", state.ui.grammar.drillShowFilter ? "true" : "false");
    });
  });

  container.querySelectorAll("[data-drill-fb]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const key = btn.dataset.drillFb;
      if (key in state.ui.grammar.drillFeedback) {
        state.ui.grammar.drillFeedback[key] = !state.ui.grammar.drillFeedback[key];
        saveUiPreferences();
        btn.classList.toggle("is-on", state.ui.grammar.drillFeedback[key]);
        btn.setAttribute("aria-pressed", state.ui.grammar.drillFeedback[key] ? "true" : "false");
        renderGrammarDrillStage();
      }
    });
  });

  document.getElementById("drill-type-sel").addEventListener("change", (e) => {
    dr.drillType = e.target.value;
    loadNextGrammarDrill();
  });
  document.getElementById("drill-scope-sel").addEventListener("change", (e) => {
    dr.scope = e.target.value;
    loadNextGrammarDrill();
  });
  document.getElementById("drill-level-sel").addEventListener("change", (e) => {
    dr.level = e.target.value;
    loadNextGrammarDrill();
  });
  const clrBtn = document.getElementById("btn-clear-grammar-filter");
  if (clrBtn) {
    clrBtn.addEventListener("click", () => {
      dr.grammarCode = null;
      dr.item = null;
      dr.emptyReason = null;
      dr.selectedOption = null;
      dr.result = null;
      renderGrammarDrillSubtab();
    });
  }
  document.getElementById("btn-reload-grammar-drill").addEventListener("click", (e) => {
    if (e.detail > 0 && document.activeElement) document.activeElement.blur();
    loadNextGrammarDrill();
  });

  if (!dr.item && !dr.loading && !dr.error && !dr.emptyReason) {
    loadNextGrammarDrill();
  } else {
    renderGrammarDrillStage();
  }
}

async function loadNextGrammarDrill() {
  const dr = state.grammar.drill;
  const reqSeq = ++grammarDrillReqSeq;
  dr.loading = true;
  dr.error = null;
  dr.emptyReason = null;
  dr.selectedOption = null;
  dr.result = null;
  dr.sessionSeed = "gd-" + Math.random().toString(36).slice(2, 9);
  renderGrammarDrillStage();

  const params = new URLSearchParams();
  params.set("drill_type", dr.drillType || "mixed");
  params.set("scope", dr.scope || "all");
  if (dr.level && dr.level !== "ALL") params.set("level", dr.level);
  if (dr.grammarCode) params.set("grammar_code", dr.grammarCode);
  params.set("session_seed", dr.sessionSeed);

  try {
    const res = await apiFetch("/api/grammar/drill/next?" + params.toString());
    if (reqSeq !== grammarDrillReqSeq) return;
    dr.loading = false;
    if (res.empty || !res.drill) {
      dr.item = null;
      dr.emptyReason = res.reason || "Không còn bài tập ngữ pháp phù hợp bộ lọc này.";
    } else {
      dr.item = res.drill;
      dr.startedAt = Date.now();
    }
    renderGrammarDrillStage();
  } catch (err) {
    if (reqSeq !== grammarDrillReqSeq) return;
    dr.loading = false;
    dr.error = err.message;
    renderGrammarDrillStage();
  }
}

function renderGrammarDrillStage() {
  const stage = document.getElementById("grammar-drill-stage");
  if (!stage) return;
  const dr = state.grammar.drill;
  const dfb = state.ui.grammar.drillFeedback;

  if (dr.loading) {
    stage.innerHTML = renderSkeleton(5);
    return;
  }
  if (dr.error) {
    stage.innerHTML = renderErrorState(dr.error, "btn-retry-grammar-drill");
    const retry = document.getElementById("btn-retry-grammar-drill");
    if (retry) retry.addEventListener("click", loadNextGrammarDrill);
    return;
  }
  if (!dr.item) {
    stage.innerHTML = renderEmptyState(
      "Chưa có bài luyện phù hợp bộ lọc",
      dr.emptyReason || "Không tìm thấy bài tập ngữ pháp cho tổ hợp lọc hiện tại.",
      "Đặt lại bộ lọc về Tất cả",
      "btn-reset-grammar-drill-filter"
    );
    const resetBtn = document.getElementById("btn-reset-grammar-drill-filter");
    if (resetBtn) {
      resetBtn.addEventListener("click", () => {
        dr.drillType = "mixed";
        dr.scope = "all";
        dr.level = "ALL";
        dr.grammarCode = null;
        dr.item = null;
        dr.emptyReason = null;
        dr.selectedOption = null;
        dr.result = null;
        renderGrammarDrillSubtab();
      });
    }
    return;
  }

  const it = dr.item;
  const res = dr.result;
  const optsHtml = (it.options || []).map((optText, idx) => {
    let cls = "option-btn grammar-drill-opt-btn";
    if (!res && dr.selectedOption === idx) cls += " selected";
    if (res) {
      if (idx === res.correct_display_index) cls += " correct";
      else if (idx === res.selected_display_index && !res.is_correct) cls += " wrong";
    }
    return `
      <button type="button" class="${cls}" data-opt-idx="${idx}" ${res ? "disabled" : ""}>
        <span class="opt-num tabular-nums">${idx + 1}</span>
        <span class="min-w-0 break-anywhere">${escapeHtml(optText)}</span>
      </button>
    `;
  }).join("");

  let feedbackHtml = "";
  if (res) {
    const statusCls = res.is_correct ? "callout-success" : "callout-danger";
    const statusTitle = res.is_correct
      ? "[OK] CHÍNH XÁC — Nắm đúng hình thái & ngữ dụng!"
      : "[FAIL] CHƯA CHÍNH XÁC — Xem chẩn đoán bẫy bên dưới";

    const diagItems = (res.option_diagnostics_detailed && res.option_diagnostics_detailed.length)
      ? res.option_diagnostics_detailed
      : (res.option_diagnostics || []).map((diag, idx) => ({
          display_index: idx,
          option_text: (it.options || [])[idx] || "",
          is_correct: idx === res.correct_display_index,
          is_selected: idx === res.selected_display_index,
          diagnostic: diag,
        }));

    const diagHtml = diagItems.map((d) => {
      const cls = d.is_correct ? "is-correct-opt" : (d.is_selected ? "is-selected-wrong" : "");
      const tag = d.is_correct ? "[ĐÚNG]" : (d.is_selected ? "[BẠN CHỌN]" : "[NHIỄU]");
      return `
        <div class="diagnostic-item ${cls}">
          <strong>${d.display_index + 1}. ${escapeHtml(d.option_text)}</strong> <span class="badge">${tag}</span><br>
          <span>${escapeHtml(d.diagnostic)}</span>
        </div>
      `;
    }).join("");

    const gp = res.grammar_point || {};
    const fAfter = res.fsrs || {};

    feedbackHtml = `
      <div class="stack-sm" style="margin-top: 16px;">
        <div class="${statusCls}">
          <strong>${statusTitle}</strong><br>
          <span>Đáp án chuẩn: <strong>${escapeHtml(res.correct_option_text)}</strong></span>
          ${res.selected_diagnostic ? `<div style="margin-top:4px;"><strong>Chẩn đoán lựa chọn của bạn:</strong> ${escapeHtml(res.selected_diagnostic)}</div>` : ""}
        </div>

        ${dfb.showTranslation && res.translation_vi ? `<div class="card" style="padding:12px;"><strong>Dịch nghĩa:</strong> ${escapeHtml(res.translation_vi)}</div>` : ""}
        ${dfb.showExplanation && res.explanation_vi ? `<div class="card" style="padding:12px; white-space: pre-wrap;"><strong>Giải thích cốt lõi:</strong> ${escapeHtml(res.explanation_vi)}</div>` : ""}

        ${dfb.showDiagnostics ? `
          <div class="stack-sm">
            <strong>Chẩn đoán từng phương án (1–4):</strong>
            <div class="diagnostic-list">${diagHtml}</div>
          </div>
        ` : ""}

        ${gp.code ? `
          <div class="callout-info row-wrap" style="justify-content: space-between;">
            <div class="min-w-0 break-anywhere">
              <strong>Mẫu liên quan:</strong> [${escapeHtml(gp.jlpt_level)}] ${escapeHtml(gp.pattern)} (${escapeHtml(gp.formation_formula || "")})
            </div>
            <button type="button" class="btn-secondary btn-sm btn-open-grammar-from-drill" data-grammar-code="${escapeHtml(gp.code)}">Xem Bài học Mẫu này</button>
          </div>
        ` : ""}

        <div class="row-wrap" style="justify-content: space-between; margin-top: 6px;">
          <span class="muted tabular-nums">Trạng thái: ${escapeHtml(formatMasteryStateVi(fAfter))} · Số lần nhầm: ${fAfter.lapses || 0}</span>
          <button type="button" id="btn-next-grammar-drill" class="btn-primary">Câu Luyện Ngữ pháp Tiếp theo (Space)</button>
        </div>
      </div>
    `;
  }

  stage.innerHTML = `
    <div class="card-editorial min-w-0">
      <div class="row-wrap" style="justify-content: space-between; margin-bottom: 8px;">
        <div class="row-wrap">
          <span class="badge accent">[${escapeHtml(it.jlpt_level)}]</span>
          <span class="badge">${escapeHtml(it.drill_type_label_vi || it.drill_type)}</span>
          <span class="badge">${escapeHtml(it.category_label_vi || it.category)}</span>
          <span class="badge ${it.in_exam_corpus ? "success" : ""}">${it.in_exam_corpus ? "[THI CUỐI KÌ]" : "[MỞ RỘNG JLPT]"}</span>
        </div>
        <span class="muted tabular-nums" style="font-size:12px;">${escapeHtml(it.drill_key)}</span>
      </div>

      ${!res ? `<div class="step-hint-bar">Cách làm: Chọn 1 đáp án đúng (hoặc bấm phím 1–4) rồi bấm Kiểm tra Đáp án (hoặc phím Space).</div>` : ""}
      <div class="jp-prompt">${escapeHtml(it.prompt_jp)}</div>
      <div class="options-list">${optsHtml}</div>
      ${!res ? `
        <div class="row-wrap" style="margin-top: 12px;">
          <button type="button" id="btn-submit-grammar-drill" class="btn-primary" ${dr.selectedOption !== null ? "" : "disabled"}>Kiểm tra Đáp án (Space)</button>
        </div>
      ` : ""}
      ${feedbackHtml}
    </div>
  `;

  stage.querySelectorAll(".grammar-drill-opt-btn[data-opt-idx]").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      if (dr.result) return;
      dr.selectedOption = parseInt(btn.dataset.optIdx, 10);
      if (e.detail > 0 && document.activeElement) document.activeElement.blur();
      renderGrammarDrillStage();
    });
  });

  const subBtn = document.getElementById("btn-submit-grammar-drill");
  if (subBtn) subBtn.addEventListener("click", submitGrammarDrill);

  const nextBtn = document.getElementById("btn-next-grammar-drill");
  if (nextBtn) nextBtn.addEventListener("click", loadNextGrammarDrill);

  stage.querySelectorAll(".btn-open-grammar-from-drill[data-grammar-code]").forEach((btn) => {
    btn.addEventListener("click", () => {
      openGrammarModal(btn.dataset.grammarCode, btn);
    });
  });
}

async function submitGrammarDrill() {
  const dr = state.grammar.drill;
  if (!dr.item || dr.result) return;
  if (dr.selectedOption === null) {
    showToast("Hãy chọn 1 đáp án (1–4).", true);
    return;
  }
  const elapsed = Math.max(0.5, (Date.now() - dr.startedAt) / 1000);
  try {
    const res = await apiFetch("/api/grammar/drill/submit", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        drill_id: dr.item.drill_id,
        selected_index: dr.selectedOption,
        response_sec: elapsed,
        session_seed: dr.item.session_seed,
      }),
    });
    dr.result = res;
    if (res.overview) {
      state.grammar.overview = res.overview;
      const strip = document.getElementById("grammar-overview-strip");
      if (strip) {
        strip.innerHTML = renderGrammarOverviewStrip(res.overview);
        strip.hidden = !state.ui.grammar.showOverview;
      }
      if (state.dashboard) state.dashboard.grammar_summary = res.overview;
    }
    renderGrammarDrillStage();
  } catch (err) {
    showToast(err.message, true);
  }
}

/* Subtab 3: Nền tảng Từ vựng & Chữ Hán */
function navigateVocabDeck(delta) {
  const vb = state.grammar.vocab;
  if (!vb.items || !vb.items.length) return;
  const maxIdx = vb.items.length - 1;
  const next = Math.max(0, Math.min(maxIdx, state.ui.grammar.vocabDeckIndex + delta));
  if (next === state.ui.grammar.vocabDeckIndex) return;
  state.ui.grammar.vocabDeckIndex = next;
  renderVocabResults();
}

function renderVocabSubtab() {
  const container = document.getElementById("grammar-subtab-container");
  if (!container) return;
  const vb = state.grammar.vocab;
  const gUi = state.ui.grammar;
  const vf = gUi.vocabFields;
  const vl = gUi.vocabLayout;

  container.innerHTML = `
    <div class="stack-md">
      <div class="view-control-bar" role="region" aria-label="Tùy chỉnh hiển thị Từ vựng và Chữ Hán">
        <div class="view-control-group">
          <div class="mode-seg-group" role="group" aria-label="Bố cục Từ vựng">
            <button type="button" class="mode-seg-btn ${vl === "table" ? "active" : ""}" data-vocab-layout="table" aria-pressed="${vl === "table"}">Bảng tra cứu</button>
            <button type="button" class="mode-seg-btn ${vl === "cards" ? "active" : ""}" data-vocab-layout="cards" aria-pressed="${vl === "cards"}">Thẻ đọc tập trung</button>
            <button type="button" class="mode-seg-btn ${vl === "deck" ? "active" : ""}" data-vocab-layout="deck" aria-pressed="${vl === "deck"}">Từng từ 1 · Tự dò Kanji</button>
          </div>
        </div>
        <div class="view-control-group">
          <button type="button" class="vis-chip ${vf.showFilter ? "is-on" : ""}" data-vocab-vis="filter" aria-pressed="${vf.showFilter}">Bộ lọc</button>
          <button type="button" class="vis-chip ${vf.showReading ? "is-on" : ""}" data-vocab-vis="showReading" aria-pressed="${vf.showReading}">Phiên âm &amp; Hán-Việt</button>
          <button type="button" class="vis-chip ${vf.showRadical ? "is-on" : ""}" data-vocab-vis="showRadical" aria-pressed="${vf.showRadical}">Bộ thủ</button>
          <button type="button" class="vis-chip ${vf.showMeaning ? "is-on" : ""}" data-vocab-vis="showMeaning" aria-pressed="${vf.showMeaning}">Nghĩa &amp; Kết hợp</button>
          <button type="button" class="vis-chip ${vf.showSource ? "is-on" : ""}" data-vocab-vis="showSource" aria-pressed="${vf.showSource}">Nguồn &amp; Câu đề</button>
        </div>
      </div>

      <div id="vocab-filter-card" class="card" ${vf.showFilter ? "" : "hidden"}>
        <div class="grammar-filter-bar">
          <div class="field">
            <label for="vocab-scope-sel">Nguồn từ vựng</label>
            <select id="vocab-scope-sel" class="select">
              <option value="all" ${vb.scope === "all" ? "selected" : ""}>Tất cả nguồn</option>
              <option value="exam" ${vb.scope === "exam" ? "selected" : ""}>Từ Sổ tay Bộ đề .xlsx</option>
              <option value="curated" ${vb.scope === "curated" ? "selected" : ""}>Giáo trình Mimikara / Somatome / Bộ thủ</option>
            </select>
          </div>
          <div class="field">
            <label for="vocab-level-sel">Cấp độ JLPT</label>
            <select id="vocab-level-sel" class="select">
              <option value="ALL" ${vb.level === "ALL" ? "selected" : ""}>Tất cả (N5–N2)</option>
              <option value="N5" ${vb.level === "N5" ? "selected" : ""}>N5</option>
              <option value="N4" ${vb.level === "N4" ? "selected" : ""}>N4</option>
              <option value="N3" ${vb.level === "N3" ? "selected" : ""}>N3</option>
              <option value="N2" ${vb.level === "N2" ? "selected" : ""}>N2</option>
            </select>
          </div>
          <div class="field" style="flex: 1.5 1 200px;">
            <label for="vocab-search-inp">Tra cứu Kanji / Hiragana / Hán-Việt / Nghĩa</label>
            <input id="vocab-search-inp" type="search" class="input" placeholder="VD: 技術, ぎじゅつ, KỸ THUẬT, bộ thủ..." value="${escapeHtml(vb.q)}">
          </div>
          <button type="button" id="btn-vocab-search" class="btn-primary">Tra cứu</button>
        </div>
      </div>

      <div id="vocab-results-container"></div>
    </div>
  `;

  applyUiStateToRoot();

  container.querySelectorAll("[data-vocab-layout]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const val = btn.dataset.vocabLayout;
      if (val === "table" || val === "cards" || val === "deck") {
        state.ui.grammar.vocabLayout = val;
        saveUiPreferences();
        renderVocabSubtab();
      }
    });
  });

  container.querySelectorAll("[data-vocab-vis]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const key = btn.dataset.vocabVis === "filter" ? "showFilter" : btn.dataset.vocabVis;
      if (key in state.ui.grammar.vocabFields) {
        state.ui.grammar.vocabFields[key] = !state.ui.grammar.vocabFields[key];
        saveUiPreferences();
        renderVocabSubtab();
      }
    });
  });

  document.getElementById("vocab-scope-sel").addEventListener("change", (e) => {
    vb.scope = e.target.value;
    state.ui.grammar.vocabDeckIndex = 0;
    loadVocabFoundation();
  });
  document.getElementById("vocab-level-sel").addEventListener("change", (e) => {
    vb.level = e.target.value;
    state.ui.grammar.vocabDeckIndex = 0;
    loadVocabFoundation();
  });
  const searchInp = document.getElementById("vocab-search-inp");
  searchInp.addEventListener("input", () => {
    vb.q = searchInp.value;
    if (vocabSearchTimer) clearTimeout(vocabSearchTimer);
    vocabSearchTimer = setTimeout(() => {
      state.ui.grammar.vocabDeckIndex = 0;
      loadVocabFoundation();
    }, 250);
  });
  searchInp.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      if (vocabSearchTimer) clearTimeout(vocabSearchTimer);
      vb.q = searchInp.value;
      state.ui.grammar.vocabDeckIndex = 0;
      loadVocabFoundation();
    }
  });
  document.getElementById("btn-vocab-search").addEventListener("click", () => {
    vb.q = searchInp.value;
    state.ui.grammar.vocabDeckIndex = 0;
    loadVocabFoundation();
  });

  if (vb.loaded && !vb.loading && !vb.error) {
    renderVocabResults();
  } else {
    loadVocabFoundation();
  }
}

async function loadVocabFoundation() {
  const vb = state.grammar.vocab;
  const reqSeq = ++vocabReqSeq;
  vb.loading = true;
  vb.error = null;
  renderVocabResults();

  const params = new URLSearchParams();
  params.set("scope", vb.scope || "all");
  if (vb.level && vb.level !== "ALL") params.set("level", vb.level);
  if (vb.q && vb.q.trim()) params.set("q", vb.q.trim());
  params.set("limit", "120");

  try {
    const res = await apiFetch("/api/foundation/vocab?" + params.toString());
    if (reqSeq !== vocabReqSeq) return;
    vb.items = res.items || [];
    vb.total = res.total || vb.items.length;
    vb.loaded = true;
    vb.loading = false;
    renderVocabResults();
  } catch (err) {
    if (reqSeq !== vocabReqSeq) return;
    vb.loading = false;
    vb.error = err.message;
    renderVocabResults();
  }
}

function renderVocabCardInner(item, idx, isDeck) {
  const vf = state.ui.grammar.vocabFields;
  const vKey = item.vocab_key || `${item.word || "v"}::${idx}`;
  const readingKey = `${vKey}::reading`;
  const meaningKey = `${vKey}::meaning`;
  const readingRevealed = Boolean(state.ui.revealedVocab[readingKey]);
  const meaningRevealed = Boolean(state.ui.revealedVocab[meaningKey]);

  const linkedBtns = (item.linked_question_ids || []).map((qid) => `
    <button type="button" class="btn-secondary btn-sm btn-vocab-jump-q" data-qid="${qid}">Câu #${qid}</button>
  `).join("");

  const readingBlock = vf.showReading || readingRevealed
    ? `<div>
         <div style="font-size: ${isDeck ? "18px" : "15px"}; font-weight: 600;">${escapeHtml(item.reading)}</div>
         <div class="muted"><strong>${escapeHtml(item.han_viet)}</strong></div>
       </div>`
    : `<div><button type="button" class="self-mask-btn" data-reveal-vocab="${escapeHtml(readingKey)}">Xem phiên âm &amp; Hán-Việt</button></div>`;

  const radicalBlock = vf.showRadical
    ? `<div class="muted break-anywhere"><strong>Bộ thủ:</strong> ${escapeHtml(item.radical_note || "—")}</div>`
    : "";

  const meaningBlock = vf.showMeaning || meaningRevealed
    ? `<div class="break-anywhere">
         <div><strong>${escapeHtml(item.meaning_vi)}</strong></div>
         ${item.collocation_tip ? `<div class="muted" style="margin-top:2px;">${escapeHtml(item.collocation_tip)}</div>` : ""}
       </div>`
    : `<div><button type="button" class="self-mask-btn" data-reveal-vocab="${escapeHtml(meaningKey)}">Xem nghĩa &amp; kết hợp từ</button></div>`;

  const sourceBlock = vf.showSource
    ? `<div class="stack-sm" style="gap:4px;">
         <div class="muted break-anywhere" style="font-size:12px;">${escapeHtml(item.source_ref || "")}</div>
         ${linkedBtns ? `<div class="row-wrap">${linkedBtns}</div>` : ""}
       </div>`
    : "";

  return `
    <div class="stack-sm">
      <div class="row-wrap" style="justify-content: space-between;">
        <div class="row-wrap">
          <span class="badge accent">[${escapeHtml(item.jlpt_level || "N3")}]</span>
          <span class="badge ${item.in_exam_corpus ? "success" : ""}">${item.in_exam_corpus ? "[THI CUỐI KÌ]" : "[GIÁO TRÌNH]"}</span>
        </div>
      </div>
      <div class="vocab-focus-word">${escapeHtml(item.word)}</div>
      ${readingBlock}
      ${radicalBlock}
      ${meaningBlock}
      ${sourceBlock}
    </div>
  `;
}

function renderVocabResults() {
  const box = document.getElementById("vocab-results-container");
  if (!box) return;
  const vb = state.grammar.vocab;
  const gUi = state.ui.grammar;
  const vf = gUi.vocabFields;
  const vl = gUi.vocabLayout;

  if (vb.loading) {
    box.innerHTML = renderSkeleton(5);
    return;
  }
  if (vb.error) {
    box.innerHTML = renderErrorState(vb.error, "btn-retry-vocab-list");
    const retry = document.getElementById("btn-retry-vocab-list");
    if (retry) retry.addEventListener("click", loadVocabFoundation);
    return;
  }
  if (!vb.items.length) {
    box.innerHTML = renderEmptyState(
      "Không tìm thấy mục từ vựng / Kanji phù hợp",
      "Thử đổi nguồn, cấp độ hoặc xóa từ khóa tìm kiếm.",
      "Đặt lại bộ lọc Từ vựng",
      "btn-reset-vocab-filter"
    );
    const resetBtn = document.getElementById("btn-reset-vocab-filter");
    if (resetBtn) {
      resetBtn.addEventListener("click", () => {
        vb.scope = "all";
        vb.level = "ALL";
        vb.q = "";
        vb.loaded = false;
        gUi.vocabDeckIndex = 0;
        renderVocabSubtab();
      });
    }
    return;
  }

  if (vl === "deck") {
    const maxIdx = vb.items.length - 1;
    if (gUi.vocabDeckIndex > maxIdx) gUi.vocabDeckIndex = maxIdx;
    if (gUi.vocabDeckIndex < 0) gUi.vocabDeckIndex = 0;
    const idx = gUi.vocabDeckIndex;
    const item = vb.items[idx];

    box.innerHTML = `
      <div class="stack-md">
        <div class="reader-nav-bar">
          <button type="button" id="btn-vocab-prev" class="btn-secondary btn-sm" ${idx <= 0 ? "disabled" : ""}>Từ trước ([)</button>
          <span class="muted tabular-nums">Từ <strong>${idx + 1}</strong> / ${vb.items.length}</span>
          <button type="button" id="btn-vocab-next" class="btn-primary btn-sm" ${idx >= maxIdx ? "disabled" : ""}>Từ tiếp (])</button>
        </div>
        <div class="vocab-deck-stage">
          ${renderVocabCardInner(item, idx, true)}
        </div>
      </div>
    `;

    const prevBtn = document.getElementById("btn-vocab-prev");
    if (prevBtn) prevBtn.addEventListener("click", () => navigateVocabDeck(-1));
    const nextBtn = document.getElementById("btn-vocab-next");
    if (nextBtn) nextBtn.addEventListener("click", () => navigateVocabDeck(1));
  } else if (vl === "cards") {
    const cardsHtml = vb.items.map((item, idx) => `
      <div class="vocab-focus-card">
        ${renderVocabCardInner(item, idx, false)}
      </div>
    `).join("");

    box.innerHTML = `
      <div class="stack-sm">
        <div class="muted tabular-nums">Hiển thị <strong>${vb.items.length}</strong> / ${vb.total} thẻ từ vựng &amp; Kanji nền tảng</div>
        <div class="vocab-cards-grid">${cardsHtml}</div>
      </div>
    `;
  } else {
    const rowsHtml = vb.items.map((item) => {
      const linkedBtns = (item.linked_question_ids || []).map((qid) => `
        <button type="button" class="btn-secondary btn-sm btn-vocab-jump-q" data-qid="${qid}">Câu #${qid}</button>
      `).join("");

      return `
        <tr>
          <td class="min-w-0 break-anywhere">
            <strong style="font-size: 16px;">${escapeHtml(item.word)}</strong>
            <div class="row-wrap" style="margin-top:4px;">
              <span class="badge accent">[${escapeHtml(item.jlpt_level || "N3")}]</span>
              <span class="badge ${item.in_exam_corpus ? "success" : ""}">${item.in_exam_corpus ? "[THI CUỐI KÌ]" : "[GIÁO TRÌNH]"}</span>
            </div>
          </td>
          ${vf.showReading ? `
            <td class="min-w-0 break-anywhere">
              <div>${escapeHtml(item.reading)}</div>
              <div class="muted"><strong>${escapeHtml(item.han_viet)}</strong></div>
            </td>
          ` : ""}
          ${vf.showRadical ? `<td class="min-w-0 break-anywhere">${escapeHtml(item.radical_note || "—")}</td>` : ""}
          ${vf.showMeaning ? `
            <td class="min-w-0 break-anywhere">
              <div><strong>${escapeHtml(item.meaning_vi)}</strong></div>
              ${item.collocation_tip ? `<div class="muted" style="margin-top:2px;">${escapeHtml(item.collocation_tip)}</div>` : ""}
            </td>
          ` : ""}
          ${vf.showSource ? `
            <td class="min-w-0 break-anywhere">
              <div class="muted" style="margin-bottom:4px;">${escapeHtml(item.source_ref || "")}</div>
              ${linkedBtns ? `<div class="row-wrap">${linkedBtns}</div>` : ""}
            </td>
          ` : ""}
        </tr>
      `;
    }).join("");

    box.innerHTML = `
      <div class="card stack-sm">
        <div class="muted tabular-nums">Hiển thị <strong>${vb.items.length}</strong> / ${vb.total} mục từ vựng &amp; Kanji nền tảng</div>
        <div class="table-scroll-wrap">
          <table class="data-table">
            <thead>
              <tr>
                <th>Chữ viết</th>
                ${vf.showReading ? "<th>Hiragana &amp; Hán-Việt</th>" : ""}
                ${vf.showRadical ? "<th>Bộ thủ / Ghi chú</th>" : ""}
                ${vf.showMeaning ? "<th>Nghĩa &amp; Collocation</th>" : ""}
                ${vf.showSource ? "<th>Nguồn &amp; Liên kết Đề</th>" : ""}
              </tr>
            </thead>
            <tbody>${rowsHtml}</tbody>
          </table>
        </div>
      </div>
    `;
  }

  box.querySelectorAll("[data-reveal-vocab]").forEach((btn) => {
    btn.addEventListener("click", () => {
      state.ui.revealedVocab[btn.dataset.revealVocab] = true;
      renderVocabResults();
    });
  });

  box.querySelectorAll(".btn-vocab-jump-q[data-qid]").forEach((btn) => {
    btn.addEventListener("click", () => {
      jumpToStudyQuestion(btn.dataset.qid);
    });
  });
}

/* Subtab 4: Mở rộng Kỳ thi JLPT */
const SAMPLE_JLPT_JSON_PACK = `{
  "grammar_points": [
    {
      "code": "GP-N2-EXT-01",
      "pattern": "～ざるを得ない",
      "jlpt_level": "N2",
      "category": "modality",
      "category_label_vi": "Tình thái & Bắt buộc",
      "formation_formula": "Vない (bỏ ない) + ざるを得ない (する -> せざるを得ない)",
      "formation_table": [
        {"pos": "Động từ thể ない", "rule": "Vない (bỏ ない) + ざるを得ない"},
        {"pos": "Động từ nhóm 3 (する)", "rule": "する -> せざるを得ない"}
      ],
      "core_meaning_vi": "Đành phải / Không thể không làm",
      "deep_explanation_vi": "Diễn tả tình huống bất đắc dĩ phải làm vì hoàn cảnh khách quan ép buộc.",
      "register_tag": "Văn viết / Trang trọng",
      "confusable_pairs": [
        {
          "rival_pattern": "～ないわけにはいかない",
          "difference_vi": "ざるを得ない trang trọng hơn và nhấn mạnh không còn lựa chọn nào khác.",
          "quick_test_vi": "Thường gặp trong văn bản trang trọng hoặc thông báo."
        }
      ],
      "examples": [
        {
          "jp": "台風が近づいているので、旅行を中止せざるを得ない。",
          "reading_note": "たいふう・ちゅうし",
          "vi": "Vì bão đang đến gần nên đành phải hủy chuyến du lịch.",
          "grammar_note": "する chuyển thành せざるを得ない"
        }
      ]
    }
  ],
  "drills": [
    {
      "drill_key": "DR-N2-EXT-01-F",
      "grammar_code": "GP-N2-EXT-01",
      "drill_type": "formation",
      "prompt_jp": "急な仕事が入り、今日の会議には欠席（　　　）。",
      "options": ["せざるを得ない", "するざるを得ない", "しざるを得ない", "したざるを得ない"],
      "correct_index": 0,
      "translation_vi": "Có việc gấp nên đành phải vắng mặt cuộc họp hôm nay.",
      "explanation_vi": "Động từ する chia đặc biệt thành せざるを得ない.",
      "option_diagnostics": [
        "ĐÚNG: する chuyển thành せ + ざるを得ない.",
        "SAI HÌNH THÁI: Không gắn ざるを得ない sau Vる.",
        "SAI HÌNH THÁI: Dạng し là Vます, không dùng cho mẫu này.",
        "SAI HÌNH THÁI: Không gắn sau Vた."
      ]
    }
  ]
}`;

function renderJlptExpansionSubtab() {
  const container = document.getElementById("grammar-subtab-container");
  if (!container) return;
  const ov = state.grammar.overview;
  const levels = (ov && ov.levels) || [];

  const levelRows = levels.length
    ? levels.map((lv) => {
        const pct = Math.min(100, Number(lv.coverage_pct || 0));
        return `
          <tr>
            <td><strong>[${escapeHtml(lv.level)}]</strong><br><span class="muted">${escapeHtml(lv.label_vi || "")}</span></td>
            <td class="tabular-nums"><strong>${lv.total}</strong></td>
            <td class="tabular-nums">${lv.exam_corpus_count || 0}</td>
            <td class="tabular-nums">${lv.in_progress || 0} / ${lv.relearning || 0}</td>
            <td class="tabular-nums">${lv.due || 0}</td>
            <td class="tabular-nums" style="min-width: 140px;">
              <div><strong>${lv.mastered || 0}/${lv.total}</strong> (${pct.toFixed(1)}%)</div>
              <div class="progress-track" style="margin-top:4px;"><div class="progress-fill success" style="width:${pct}%"></div></div>
            </td>
            <td>
              <button type="button" class="btn-secondary btn-sm btn-practice-level" data-level="${escapeHtml(lv.level)}">Luyện ${escapeHtml(lv.level)}</button>
            </td>
          </tr>
        `;
      }).join("")
    : "";

  const imp = state.grammar.importResult;
  const impBanner = imp
    ? `<div class="callout-success" style="margin-top:12px;">
         [OK] Đã nạp gói mở rộng <strong>${escapeHtml(imp.filename)}</strong> (${escapeHtml(imp.import_type)}) —
         Mẫu ngữ pháp: +${imp.imported_grammar_points || 0} · Bài luyện: +${imp.imported_drills || 0} · Từ vựng: +${imp.imported_vocab || 0}
       </div>`
    : "";

  container.innerHTML = `
    <div class="stack-md">
      <div class="card">
        <h3 class="card-title">Tiến độ Phủ Ngữ pháp theo Cấp độ JLPT (N5 &#8594; N2)</h3>
        ${levels.length ? `
          <div class="table-scroll-wrap">
            <table id="jlpt-levels-table" class="data-table">
              <thead>
                <tr>
                  <th>Cấp độ</th>
                  <th>Tổng mẫu</th>
                  <th>Trong đề .xlsx</th>
                  <th>Đang học / Cần vá</th>
                  <th>Cần ôn</th>
                  <th>Đã vững (%)</th>
                  <th>Thao tác</th>
                </tr>
              </thead>
              <tbody>${levelRows}</tbody>
            </table>
          </div>
        ` : renderEmptyState("Chưa có dữ liệu cấp độ JLPT", "Hãy kiểm tra kết nối backend hoặc nạp gói ngữ pháp.", "", "")}
      </div>

      <div class="card stack-sm">
        <h3 class="card-title">Nạp Gói Ngữ pháp Mở rộng (.json hoặc .xlsx) cho N2 / N1</h3>
        <p class="muted">Chọn tệp <code>.json</code> theo chuẩn bên dưới để mở rộng thêm kho mẫu N2/N1, hoặc tải lên tệp đề thi <code>.xlsx</code> để tự động liên kết ngữ pháp.</p>
        <form id="grammar-import-form" class="form-row">
          <div class="field">
            <label for="inp-grammar-import-file">Chọn tệp .json hoặc .xlsx</label>
            <input id="inp-grammar-import-file" type="file" accept=".json,.xlsx" class="input">
          </div>
          <button type="submit" class="btn-primary">Nạp gói Mở rộng</button>
        </form>
        ${impBanner}
      </div>

      <details class="card details-card">
        <summary class="details-summary">Xem mẫu cấu trúc tệp .json (dành cho người muốn tự soạn thêm gói N2 / N1)</summary>
        <div style="margin-top: 12px;">
          <pre class="code-block">${escapeHtml(SAMPLE_JLPT_JSON_PACK)}</pre>
        </div>
      </details>
    </div>
  `;

  container.querySelectorAll(".btn-practice-level[data-level]").forEach((btn) => {
    btn.addEventListener("click", () => {
      state.grammar.subtab = "drill";
      state.grammar.drill.level = btn.dataset.level;
      state.grammar.drill.scope = "all";
      state.grammar.drill.grammarCode = null;
      state.grammar.drill.drillType = "mixed";
      state.grammar.drill.item = null;
      state.grammar.drill.emptyReason = null;
      state.grammar.drill.selectedOption = null;
      state.grammar.drill.result = null;
      state.grammar.drill.loading = false;
      renderGrammarShell();
    });
  });

  document.getElementById("grammar-import-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const inp = document.getElementById("inp-grammar-import-file");
    if (!inp.files || !inp.files.length) {
      showToast("Vui lòng chọn một tệp .json hoặc .xlsx để nạp.", true);
      return;
    }
    const fd = new FormData();
    fd.append("file", inp.files[0]);
    try {
      const res = await apiFetch("/api/grammar/import", { method: "POST", body: fd });
      state.grammar.importResult = res;
      if (res.overview) {
        state.grammar.overview = res.overview;
        if (state.dashboard) state.dashboard.grammar_summary = res.overview;
      }
      state.grammar.library.points = [];
      state.grammar.library.loaded = false;
      state.grammar.vocab.items = [];
      state.grammar.vocab.loaded = false;
      showToast(`[OK] Đã nạp gói mở rộng ${res.filename || ""}!`);
      renderGrammarShell();
    } catch (err) {
      showToast(err.message, true);
    }
  });
}

/* Global Keyboard Shortcuts (WCAG 2.1 AA) */
function handleGlobalKeydown(e) {
  trapModalFocus(e);
  if (e.key === "Escape") {
    const pair = getActiveModalPair();
    if (pair) {
      pair.closeFn();
      return;
    }
    if (state.ui.focusMode) {
      setFocusMode(false);
    }
    return;
  }

  const tag = document.activeElement ? document.activeElement.tagName.toLowerCase() : "";
  if (tag === "input" || tag === "textarea" || tag === "select") return;
  if (e.ctrlKey || e.metaKey || e.altKey) return;
  if (isAnyModalOpen()) return;

  if (e.key === "t" || e.key === "T") {
    toggleTheme();
    return;
  }
  if (e.key === "f" || e.key === "F") {
    e.preventDefault();
    setFocusMode(!state.ui.focusMode);
    return;
  }
  if (e.key === "v" || e.key === "V") {
    e.preventDefault();
    openDisplayPrefsModal(document.activeElement);
    return;
  }
  if (e.key === "[" || e.key === "]") {
    const delta = e.key === "[" ? -1 : 1;
    if (state.activeView === "grammar" && state.grammar.subtab === "library" && state.ui.grammar.libraryLayout === "reader") {
      e.preventDefault();
      navigateGrammarReader(delta);
      return;
    }
    if (state.activeView === "grammar" && state.grammar.subtab === "vocab" && state.ui.grammar.vocabLayout === "deck") {
      e.preventDefault();
      navigateVocabDeck(delta);
      return;
    }
    if (state.activeView === "exam" && state.exam.active && state.ui.exam.layout === "single") {
      e.preventDefault();
      navigateExamSingle(delta);
      return;
    }
  }

  if (state.activeView === "study" && !state.study.showBridge && state.study.item) {
    if (["1", "2", "3", "4"].includes(e.key) && !state.study.result && state.study.item.interaction_type !== "star_4slot") {
      state.study.selectedOption = parseInt(e.key, 10) - 1;
      renderStudyView();
      return;
    }
    if ((e.key === "h" || e.key === "H") && !state.study.result && state.study.item.scaffolding.hint_allowed) {
      triggerStudyHint();
      return;
    }
    if (e.code === "Space" && tag !== "button") {
      e.preventDefault();
      if (state.study.result) loadNextStudyItem();
      else submitActiveStudy();
    }
    return;
  }

  if (state.activeView === "grammar" && state.grammar.subtab === "drill" && state.grammar.drill.item) {
    if (["1", "2", "3", "4"].includes(e.key) && !state.grammar.drill.result) {
      state.grammar.drill.selectedOption = parseInt(e.key, 10) - 1;
      renderGrammarDrillStage();
      return;
    }
    if (e.code === "Space" && tag !== "button") {
      e.preventDefault();
      if (state.grammar.drill.result) loadNextGrammarDrill();
      else if (state.grammar.drill.selectedOption !== null) submitGrammarDrill();
    }
  }
}

function bootstrapApp() {
  let savedTheme = "light";
  try {
    savedTheme = localStorage.getItem("n3_mastery_theme") || "light";
    state.hideQuickGuide = localStorage.getItem("n3_hide_quick_guide") === "1";
  } catch (e) {
    savedTheme = "light";
    state.hideQuickGuide = false;
  }
  loadUiPreferences();
  applyTheme(savedTheme);
  applyUiStateToRoot();

  document.querySelectorAll(".nav-btn").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      if (e.detail > 0 && document.activeElement) document.activeElement.blur();
      switchView(btn.dataset.view);
    });
  });

  const bindClick = (id, fn) => {
    const el = document.getElementById(id);
    if (el) el.addEventListener("click", fn);
  };

  bindClick("btn-theme-toggle", toggleTheme);
  bindClick("btn-focus-mode", () => setFocusMode(!state.ui.focusMode));
  bindClick("btn-display-prefs", (e) => openDisplayPrefsModal(e.currentTarget));
  bindClick("btn-help-modal", openHelpModal);
  bindClick("btn-close-help", closeHelpModal);
  bindClick("btn-ok-help", closeHelpModal);
  bindClick("help-modal-backdrop", (e) => {
    if (e.target.id === "help-modal-backdrop") closeHelpModal();
  });
  bindClick("btn-close-grammar-modal", () => closeGrammarModal(false));
  bindClick("btn-ok-grammar-modal", () => closeGrammarModal(false));
  bindClick("grammar-modal-backdrop", (e) => {
    if (e.target.id === "grammar-modal-backdrop") closeGrammarModal(false);
  });
  bindClick("btn-close-display-prefs", closeDisplayPrefsModal);
  bindClick("btn-ok-display-prefs", closeDisplayPrefsModal);
  bindClick("btn-reset-display-prefs", resetAllDisplayPrefs);
  bindClick("display-prefs-backdrop", (e) => {
    if (e.target.id === "display-prefs-backdrop") closeDisplayPrefsModal();
  });

  bindClick("btn-exit-focus", () => setFocusMode(false));
  bindClick("btn-focus-prefs", (e) => openDisplayPrefsModal(e.currentTarget));
  bindClick("btn-focus-theme", toggleTheme);

  document.querySelectorAll("#focus-topbar .scale-btn[data-font-scale]").forEach((btn) => {
    btn.addEventListener("click", () => setFontScale(btn.dataset.fontScale));
  });
  document.querySelectorAll("#focus-topbar [data-focus-view]").forEach((btn) => {
    btn.addEventListener("click", () => switchView(btn.dataset.focusView));
  });

  document.addEventListener("keydown", handleGlobalKeydown);

  loadDashboard();
}

document.addEventListener("DOMContentLoaded", bootstrapApp);
