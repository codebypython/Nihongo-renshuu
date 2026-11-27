/* Pure Vanilla JS SPA for JLPT N3 10/10 Mastery System */
"use strict";

const state = {
  activeView: "dashboard",
  theme: "light",
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
};

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
    label.textContent = resolved === "dark" ? "Editorial Light" : "Nordic Dark";
  }
}

function toggleTheme() {
  applyTheme(state.theme === "light" ? "dark" : "light");
}

/* Accessible Modal with Focus Trap */
let lastFocusedBeforeModal = null;

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
  if (lastFocusedBeforeModal && typeof lastFocusedBeforeModal.focus === "function") {
    lastFocusedBeforeModal.focus();
  }
}

function trapModalFocus(e) {
  const backdrop = document.getElementById("help-modal-backdrop");
  const modal = document.getElementById("help-modal");
  if (!backdrop || backdrop.hidden || !modal || e.key !== "Tab") return;
  const focusables = modal.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
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
function switchView(viewName) {
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

  if (viewName === "dashboard") loadDashboard();
  else if (viewName === "study") ensureStudyLoaded();
  else if (viewName === "exam") renderExamShell();
  else if (viewName === "notebook") loadNotebookView();
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

  const unitsRowsHtml = (d.units || []).map((u) => {
    const pct = u.total_questions > 0 ? Math.round((u.mastered_count / u.total_questions) * 100) : 0;
    const bridgeBadge = u.bridge_completed
      ? `<span class="badge success">[OK] Đã qua N4</span>`
      : `<span class="badge warning">[CHƯA] Cần Bắc cầu N4</span>`;
    return `
      <tr>
        <td class="tabular-nums"><strong>${escapeHtml(u.code)}</strong></td>
        <td class="min-w-0 break-anywhere">
          <div><strong>${escapeHtml(u.title)}</strong></div>
          <div class="muted">${escapeHtml(u.target_skill)}</div>
        </td>
        <td>${bridgeBadge}</td>
        <td class="tabular-nums">${u.clean_original_count}/${u.total_questions}</td>
        <td class="tabular-nums">${u.variant_passed_count}/${u.total_questions}</td>
        <td class="tabular-nums"><strong>${u.mastered_count}/${u.total_questions}</strong> (${pct}%)</td>
        <td>
          <div class="row-wrap">
            <button type="button" class="btn-secondary btn-sm btn-open-bridge" data-unit="${escapeHtml(u.code)}">Trạm N4</button>
            <button type="button" class="btn-primary btn-sm btn-open-study" data-unit="${escapeHtml(u.code)}">Luyện Unit</button>
          </div>
        </td>
      </tr>
    `;
  }).join("");

  root.innerHTML = `
    <div class="stack-md">
      <div class="section-header">
        <div>
          <h2 id="dash-heading" class="section-title">Bảng Hiệu chuẩn Điểm Kép &amp; Lộ trình 10/10</h2>
          <p class="muted">Đánh giá thực chất Zero-Sycophancy trên ${r.total_questions} câu hỏi duy nhất từ ${d.workbooks_count || 7} bộ đề Excel.</p>
        </div>
        <div class="row-wrap">
          <button type="button" id="btn-dash-start-study" class="btn-primary">Bắt đầu học theo FSRS</button>
        </div>
      </div>

      <div class="grid-2">
        <div class="card">
          <div class="row-wrap" style="justify-content: space-between;">
            <h3 class="card-title">Điểm Đề Gốc (Original Bank)</h3>
            <span class="badge accent tabular-nums">${r.attempted_count}/${r.total_questions} đã làm</span>
          </div>
          <div class="score-display tabular-nums">
            <span class="score-big">${r.original_score_10.toFixed(2)}</span>
            <span class="score-den">/ 10.00</span>
          </div>
          <div class="progress-track"><div class="progress-fill" style="width:${origPct}%"></div></div>
          <p class="muted" style="margin-top:8px;">Xáo thứ tự 4 đáp án theo phiên + suy giảm trí nhớ FSRS R(t).</p>
        </div>

        <div class="card">
          <div class="row-wrap" style="justify-content: space-between;">
            <h3 class="card-title">Điểm Chống Biến Thể (Anti-Rote Mastery)</h3>
            <span class="badge ${r.mastered_count === r.total_questions && r.total_questions > 0 ? "success" : "warning"} tabular-nums">[MASTERED 10/10]: ${r.mastered_count}/${r.total_questions}</span>
          </div>
          <div class="score-display tabular-nums">
            <span class="score-big">${r.mastery_score_10.toFixed(2)}</span>
            <span class="score-den">/ 10.00</span>
          </div>
          <div class="progress-track"><div class="progress-fill success" style="width:${mastPct}%"></div></div>
          <p class="muted" style="margin-top:8px;">Yêu cầu: Đúng gốc không Hint + Đúng biến thể + &ge; 2 phiên cách quãng (lapses=0).</p>
        </div>
      </div>

      <div class="${verdictClass}">${escapeHtml(r.honest_verdict)}</div>

      <div class="card">
        <div class="section-header" style="margin-bottom: 12px;">
          <div>
            <h3 class="card-title">Bộ lập lịch Adaptive Pace &amp; Nén FSRS</h3>
            <p class="muted">Điều chỉnh quỹ thời gian thực tế trước ngày thi (Horizon cap hiện tại: <strong class="tabular-nums">${p.horizon_cap_days} ngày</strong>).</p>
          </div>
          <span class="badge ${p.is_feasible ? "success" : "danger"}">${escapeHtml(p.status_tag)}</span>
        </div>

        <form id="pace-form" class="form-row">
          <div class="field">
            <label for="inp-days">Số ngày còn lại</label>
            <input id="inp-days" type="number" class="input tabular-nums" min="1" max="365" value="${s.days_remaining}">
          </div>
          <div class="field">
            <label for="inp-minutes">Phút học / ngày</label>
            <input id="inp-minutes" type="number" class="input tabular-nums" min="5" max="720" value="${s.daily_minutes}">
          </div>
          <div class="field">
            <label for="sel-scoring">Chế độ trọng số /10</label>
            <select id="sel-scoring" class="select">
              <option value="jlpt_weighted" ${s.scoring_mode === "jlpt_weighted" ? "selected" : ""}>Chuẩn JLPT (3 : 4 : 3)</option>
              <option value="equal_weighted" ${s.scoring_mode === "equal_weighted" ? "selected" : ""}>Đồng trọng số (${r.total_questions} câu)</option>
            </select>
          </div>
          <button type="submit" class="btn-primary">Cập nhật Kế hoạch</button>
        </form>

        <div class="row-wrap" style="margin-top: 12px;">
          <span class="badge tabular-nums">Khối lượng còn lại: ${p.remaining_workload_minutes.toFixed(0)} phút</span>
          <span class="badge tabular-nums">Yêu cầu tối thiểu: ${p.required_minutes_per_day.toFixed(1)} phút/ngày</span>
          <span class="badge tabular-nums">Mục tiêu/ngày: ${p.new_units_per_day} Trạm N4 · ${p.questions_per_day} câu gốc · ${p.variants_per_day} biến thể</span>
        </div>

        ${p.warning_message ? `<div class="callout-danger" style="margin-top: 12px;">${escapeHtml(p.warning_message)}</div>` : ""}
      </div>

      <div class="card">
        <h3 class="card-title">Chi tiết 3 Phân môn (Phòng thi Viết)</h3>
        <div class="table-scroll-wrap">
          <table class="data-table">
            <thead>
              <tr>
                <th>Phân môn</th>
                <th>Trọng số</th>
                <th>Đề gốc đúng</th>
                <th>Qua Biến thể</th>
                <th>[MASTERED 10/10]</th>
                <th>Điểm Gốc</th>
                <th>Điểm Thực chất</th>
              </tr>
            </thead>
            <tbody>${secRowsHtml}</tbody>
          </table>
        </div>
      </div>

      <div class="card">
        <h3 class="card-title">Đồ thị 12 Micro-Units (Bắc cầu N4 &#8594; Chinh phục N3 10/10)</h3>
        <div class="table-scroll-wrap">
          <table class="data-table">
            <thead>
              <tr>
                <th>Unit</th>
                <th>Chuyên đề &amp; Kỹ năng mục tiêu</th>
                <th>Trạm N4</th>
                <th>Gốc</th>
                <th>Biến thể</th>
                <th>10/10</th>
                <th>Thao tác</th>
              </tr>
            </thead>
            <tbody>${unitsRowsHtml}</tbody>
          </table>
        </div>
      </div>
    </div>
  `;

  document.getElementById("btn-dash-start-study").addEventListener("click", () => {
    state.study.showBridge = false;
    switchView("study");
    loadNextStudyItem();
  });

  document.getElementById("pace-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const days = parseInt(document.getElementById("inp-days").value, 10);
    const minutes = parseInt(document.getElementById("inp-minutes").value, 10);
    const scoring_mode = document.getElementById("sel-scoring").value;
    if (!Number.isFinite(days) || days < 1 || !Number.isFinite(minutes) || minutes < 5) {
      showToast("Vui lòng nhập số ngày (>= 1) và số phút/ngày (>= 5) hợp lệ.", true);
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
      showToast("Đã cập nhật Adaptive Pace và hiệu chuẩn lại lịch FSRS.");
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
  let unitOptions = `<option value="ALL" ${state.study.unitCode === "ALL" ? "selected" : ""}>Tất cả 12 Units</option>`;
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
            <label for="study-unit-sel">Micro-Unit</label>
            <select id="study-unit-sel" class="select">${unitOptions}</select>
          </div>
          <div class="field">
            <label for="study-mode-sel">Chế độ chống học vẹt</label>
            <select id="study-mode-sel" class="select">
              <option value="mixed" ${state.study.mode === "mixed" ? "selected" : ""}>Chu trình 5 bước (Gốc + Biến thể)</option>
              <option value="original" ${state.study.mode === "original" ? "selected" : ""}>Đề gốc (Xáo đáp án)</option>
              <option value="variant" ${state.study.mode === "variant" ? "selected" : ""}>Biến thể Chống học vẹt</option>
              <option value="remediation" ${state.study.mode === "remediation" ? "selected" : ""}>Vá lỗ hổng (Relearning)</option>
            </select>
          </div>
        </div>
        <div class="row-wrap">
          <button type="button" id="btn-view-bridge" class="btn-secondary">${state.study.showBridge ? "Quay lại Câu hỏi" : "Xem Trạm Bắc cầu N4"}</button>
          <button type="button" id="btn-reshuffle-item" class="btn-secondary">Đổi Seed Xáo đáp án</button>
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
    return renderEmptyState("Chưa chọn Micro-Unit", "Chọn một unit từ MU-01 đến MU-12 để học Trạm Bắc cầu N4.", "Mở MU-01", "btn-open-mu01");
  }
  const u = bd.unit;
  const cap = bd.bridge_capsule;
  const examplesHtml = (cap.examples || []).map((ex) => `
    <div class="card" style="padding: 12px;">
      <div style="font-size: 16px; font-weight: 600;">${escapeHtml(ex.jp)}</div>
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
        <p style="margin:0 0 8px;"><strong>Kiểm tra nhanh N4 (${idx + 1}):</strong> ${escapeHtml(qc.prompt)}</p>
        <div class="options-list">${opts}</div>
      </div>
    `;
  }).join("");

  return `
    <div class="card-editorial stack-md">
      <div class="section-header" style="margin-bottom:0;">
        <div>
          <span class="badge accent">Bước 1 · Trạm Bắc cầu N4&#8594;N3</span>
          <h2 id="study-heading" class="section-title" style="margin-top:6px;">${escapeHtml(u.code)}: ${escapeHtml(u.title)}</h2>
          <p class="muted">${escapeHtml(cap.grammar_focus)}</p>
        </div>
        <span class="badge ${cap.completed ? "success" : "warning"}">${cap.completed ? "[OK] Đã thông trạm" : "[CHƯA] Chưa hoàn thành"}</span>
      </div>

      <div class="callout-info break-anywhere" style="white-space: pre-wrap;">${escapeHtml(cap.explanation_vi)}</div>

      <div class="stack-sm">
        <h3 class="card-title">Ví dụ đối chiếu N4 &#8594; N3</h3>
        ${examplesHtml}
      </div>

      <div class="stack-sm">
        <h3 class="card-title">Chốt nền N4 trước khi vào đề N3</h3>
        ${qcHtml}
      </div>

      <div class="row-wrap">
        <button type="button" id="btn-complete-bridge" class="btn-primary">Hoàn thành Trạm N4 &amp; Vào Luyện N3</button>
        <button type="button" id="btn-skip-to-questions" class="btn-secondary">Vào thẳng câu hỏi ${escapeHtml(u.code)}</button>
      </div>
    </div>
  `;
}

function renderStudyView() {
  const root = document.getElementById("study-root");
  if (!root) return;

  let bodyHtml = "";
  if (state.study.showBridge) {
    bodyHtml = renderBridgePanel();
  } else if (!state.study.item) {
    bodyHtml = renderEmptyState(
      "Hàng đợi hiện tại đã trống",
      "Không có câu hỏi nào ở chế độ này. Bạn có thể chuyển sang Biến thể Chống học vẹt hoặc chọn Unit khác.",
      "Chuyển sang Biến thể Chống học vẹt",
      "btn-switch-variant-empty"
    );
  } else {
    bodyHtml = renderActiveStudyItem();
  }

  root.innerHTML = renderStudyToolbar() + bodyHtml;
  bindStudyToolbarEvents();

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
            showToast("Có câu N4 chưa đúng: " + (firstErr ? firstErr.note : ""), true);
            return;
          }
          showToast("[OK] Đã thông Trạm Bắc cầu N4! Bắt đầu câu N3.");
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
  const fsrs = item.fsrs;

  const variantLabel = item.variant_mode === "original"
    ? "Đề gốc (Xáo A/B/C/D)"
    : item.variant_mode === "star_4slot_shift"
    ? "Biến thể Dời dấu ★ (Ghép đủ 4 ô)"
    : item.variant_mode === "dokkai_evidence"
    ? "Evidence-First Dokkai (Chọn câu chốt)"
    : item.variant_mode === "condition_shift"
    ? "Biến thể Đảo điều kiện 情報検索"
    : item.variant_mode === "error_diagnosis"
    ? "Biến thể Chẩn đoán Lỗi sai Ngữ cảnh"
    : "Đảo chiều 3 Phương án Nhiễu";

  const bridgeAlert = item.bridge_status && !item.bridge_status.completed
    ? `<div class="callout-warn" style="margin-bottom: 12px;">
         Bạn chưa thông <strong>Trạm Bắc cầu N4 (${escapeHtml(item.unit_code)})</strong>: ${escapeHtml(item.bridge_status.grammar_focus)}.
         <button type="button" id="btn-inline-bridge" class="btn-secondary btn-sm" style="margin-left:8px;">Học Trạm N4 (5 phút)</button>
       </div>`
    : "";

  const glossaryHtml = !res && scaf.background_glossary && scaf.background_glossary.length
    ? `<div class="glossary-grid">${scaf.background_glossary.map((g) =>
        `<span class="glossary-chip"><strong>${escapeHtml(g.word)}</strong> (${escapeHtml(g.reading)} · ${escapeHtml(g.han_viet)}): ${escapeHtml(g.meaning_vi)}</span>`
      ).join("")}</div>`
    : "";

  const hintBox = state.study.hintText
    ? `<div class="callout-info" style="margin-top:8px;"><strong>Gợi ý Giàn giáo (H):</strong> ${escapeHtml(state.study.hintText)}</div>`
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
           <strong>Bước 1:</strong> Bấm chọn câu chốt / dòng điều kiện (<code>注意・休診</code>) ở khung văn bản bên trái (${state.study.evidenceIndices.length} câu đã chọn).
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
        ${!res && scaf.hint_allowed ? `<button type="button" id="btn-hint-study" class="btn-secondary">Gợi ý Giàn giáo (H)</button>` : ""}
      </div>
    `;
  }

  let feedbackHtml = "";
  if (res) {
    const statusCls = res.is_correct ? "callout-success" : "callout-danger";
    const statusTitle = res.is_correct
      ? (res.remediated ? "[OK] CHÍNH XÁC — Đã vá xong lỗ hổng!" : "[OK] CHÍNH XÁC")
      : (item.interaction_type === "dokkai_evidence" && res.answer_correct && !res.evidence_correct
          ? "[FAIL] CHỌN ĐÚNG ĐÁP ÁN NHƯNG SAI CÂU BẰNG CHỨNG (Chống đoán mò)"
          : "[FAIL] CHƯA CHÍNH XÁC — Đã đưa vào Sổ tay Lỗ hổng");

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

    feedbackHtml = `
      <div class="stack-sm" style="margin-top: 16px;">
        <div class="${statusCls}">
          <strong>${statusTitle}</strong><br>
          <span>Đáp án chuẩn: <strong>${escapeHtml(res.correct_option_text)}</strong></span>
          ${res.assembled_sentence ? `<div style="margin-top:4px;">Câu ghép hoàn chỉnh: <strong>${escapeHtml(res.assembled_sentence)}</strong></div>` : ""}
        </div>
        ${res.translation_vi ? `<div class="card" style="padding:12px;"><strong>Dịch nghĩa:</strong> ${escapeHtml(res.translation_vi)}</div>` : ""}
        <div class="card" style="padding:12px; white-space: pre-wrap;"><strong>Giải thích &amp; Phân tích bẫy:</strong>\n${escapeHtml(res.explanation_vi)}</div>
        ${companionHtml}
        ${res.passage_translation_vi ? `<div class="card" style="padding:12px; white-space: pre-wrap;"><strong>Dịch &amp; Mạch logic văn bản:</strong>\n${escapeHtml(res.passage_translation_vi)}</div>` : ""}
        ${matrixHtml}
        <div class="row-wrap" style="justify-content: space-between; margin-top: 6px;">
          <span class="muted tabular-nums">FSRS: Stability ${res.fsrs.stability.toFixed(2)} ngày · Khoảng ôn nén ${res.fsrs.effective_interval_days} ngày · Chuỗi sạch ${res.fsrs.spaced_clean_sessions}/2</span>
          <button type="button" id="btn-next-study" class="btn-primary">Câu tiếp theo (Space)</button>
        </div>
      </div>
    `;
  }

  const questionCardHtml = `
    <div class="card-editorial min-w-0">
      <div class="row-wrap" style="justify-content: space-between; margin-bottom: 8px;">
        <div class="row-wrap">
          <span class="badge accent">${escapeHtml(item.unit_code)}</span>
          <span class="badge">${escapeHtml(item.mondai_type)}</span>
          <span class="badge">${escapeHtml(variantLabel)}</span>
        </div>
        <span class="badge ${scaf.tier === 3 ? "warning" : ""}">${escapeHtml(scaf.tier_label)}</span>
      </div>

      ${bridgeAlert}
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

    return `
      <div class="dokkai-split">
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
  }

  return questionCardHtml;
}

function bindActiveStudyEvents() {
  const root = document.getElementById("study-root");
  if (!root || !state.study.item) return;

  const inlineBridge = document.getElementById("btn-inline-bridge");
  if (inlineBridge) {
    inlineBridge.addEventListener("click", () => loadBridgeUnit(state.study.item.unit_code));
  }

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
        <td class="break-anywhere">${escapeHtml((d.explanation_vi || "").split("\n")[0])}</td>
      </tr>
    `).join("");

    root.innerHTML = `
      <div class="stack-md">
        <div class="section-header">
          <div>
            <h2 id="exam-heading" class="section-title">Kết quả Phòng thi Thực chiến (Cấp 3)</h2>
            <p class="muted">Đã cập nhật trực tiếp vào Bảng điểm Kép và hàng đợi FSRS.</p>
          </div>
          <button type="button" id="btn-exam-reset" class="btn-primary">Làm đề mới</button>
        </div>
        <div class="grid-3">
          <div class="card">
            <h3 class="card-title">Điểm bài thi thử</h3>
            <div class="score-big tabular-nums">${er.exam_accuracy_10.toFixed(2)} <span class="score-den">/ 10</span></div>
            <p class="muted tabular-nums">${er.correct_count}/${er.total_questions} câu đúng</p>
          </div>
          <div class="card">
            <h3 class="card-title">Điểm Đề Gốc toàn ngân hàng</h3>
            <div class="score-big tabular-nums">${er.readiness.original_score_10.toFixed(2)} <span class="score-den">/ 10</span></div>
          </div>
          <div class="card">
            <h3 class="card-title">Điểm Chống Biến Thể</h3>
            <div class="score-big tabular-nums">${er.readiness.mastery_score_10.toFixed(2)} <span class="score-den">/ 10</span></div>
          </div>
        </div>
        <div class="table-scroll-wrap">
          <table class="data-table">
            <thead><tr><th>#</th><th>KQ</th><th>Đáp án đúng</th><th>Giải thích cốt lõi</th></tr></thead>
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
    return;
  }

  if (!state.exam.active || !state.exam.examData) {
    root.innerHTML = `
      <div class="card-editorial stack-md" style="max-width: 680px; margin: 0 auto;">
        <h2 id="exam-heading" class="section-title">Phòng thi Thực chiến (Khóa 100% Giàn giáo Cấp 3)</h2>
        <p class="muted">Không hiển thị Furigana nhân tạo, không nút gợi ý, xáo trộn đáp án động và bắt buộc ghép đủ 4 ô ★.</p>
        <div class="form-row">
          <div class="field">
            <label for="exam-count-sel">Số câu mỗi phân môn</label>
            <select id="exam-count-sel" class="select">
              <option value="2">Mini Mock (6 câu: 2+2+2)</option>
              <option value="3" selected>Chuẩn nhanh (9 câu: 3+3+3)</option>
              <option value="5">Tổng lực (15 câu: 5+5+5)</option>
            </select>
          </div>
          <button type="button" id="btn-start-exam" class="btn-primary">Bắt đầu làm bài thi</button>
        </div>
      </div>
    `;
    document.getElementById("btn-start-exam").addEventListener("click", startMockExam);
    return;
  }

  const ex = state.exam.examData;
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
    return `
      <div class="card">
        <div class="row-wrap" style="justify-content: space-between; margin-bottom: 6px;">
          <span class="badge accent tabular-nums">Câu ${idx + 1}/${ex.total_questions} · ${escapeHtml(it.unit_code)}</span>
          <span class="badge warning">Cấp 3 · Không gợi ý</span>
        </div>
        ${pHtml}
        <div class="jp-prompt">${it.prompt_html}</div>
        ${inputHtml}
      </div>
    `;
  }).join("");

  root.innerHTML = `
    <div class="stack-md">
      <div class="section-header">
        <div>
          <h2 id="exam-heading" class="section-title">Đang thi Thực chiến (${ex.total_questions} câu)</h2>
          <p class="muted">Thời gian đã làm: <strong id="exam-timer" class="tabular-nums">${state.exam.elapsedSec}s</strong></p>
        </div>
        <button type="button" id="btn-submit-exam" class="btn-primary">Nộp toàn bộ bài thi</button>
      </div>
      ${itemsHtml}
    </div>
  `;

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
    if (state.exam.timerId) clearInterval(state.exam.timerId);
    state.exam.timerId = setInterval(() => {
      state.exam.elapsedSec += 1;
      const el = document.getElementById("exam-timer");
      if (el) el.textContent = `${state.exam.elapsedSec}s`;
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
  for (const it of ex.items) {
    const ans = state.exam.answers[it.question_id];
    if (it.interaction_type === "star_4slot") {
      if (!ans || !ans.slot_order || ans.slot_order.some((x) => x === null)) {
        showToast(`Câu ${it.unit_code} (★) bắt buộc ghép đủ cả 4 ô trước khi nộp bài thi.`, true);
        return;
      }
      payloadItems.push({ question_id: it.question_id, slot_order: ans.slot_order, session_seed: ex.session_seed });
    } else {
      if (!ans || ans.selected_index === undefined) {
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

  const errContent = errs.length === 0
    ? renderEmptyState(
        "Sổ tay Lỗ hổng đang sạch (0 lỗi)",
        "Chưa có câu hỏi nào ở trạng thái Relearning. Hãy luyện thêm biến thể chống học vẹt để kiểm tra độ vững thực chất.",
        "Chuyển tới Luyện tập Biến thể",
        "btn-nb-to-study"
      )
    : `<div class="table-scroll-wrap">
         <table class="data-table">
           <thead><tr><th>Unit</th><th>Mondai</th><th>Lapses</th><th>Từ khóa &amp; Đề bài</th><th>Thao tác</th></tr></thead>
           <tbody>
             ${errs.map((e) => `
               <tr>
                 <td><strong>${escapeHtml(e.unit_code)}</strong></td>
                 <td>${escapeHtml(e.mondai_type)}</td>
                 <td class="tabular-nums"><span class="badge danger">${e.lapses}</span></td>
                 <td class="min-w-0 break-anywhere"><strong>${escapeHtml(e.focus_keyword)}</strong><br><span class="muted">${escapeHtml(e.prompt_jp)}</span></td>
                 <td><button type="button" class="btn-primary btn-sm btn-fix-err" data-qid="${e.question_id}" data-unit="${escapeHtml(e.unit_code)}">Vá lỗ hổng</button></td>
               </tr>
             `).join("")}
           </tbody>
         </table>
       </div>`;

  const wbRows = wbs.map((w) => `
    <tr>
      <td class="min-w-0 break-anywhere"><strong>${escapeHtml(w.filename)}</strong></td>
      <td><span class="badge">${escapeHtml(w.layout_type)}</span></td>
      <td class="tabular-nums">${w.raw_count}</td>
      <td class="tabular-nums"><strong>${w.imported_count}</strong></td>
      <td class="tabular-nums muted">${escapeHtml(w.imported_at)}</td>
    </tr>
  `).join("");

  const impBox = state.notebook.importResult
    ? `<div class="callout-success" style="margin-top:12px;">
         [OK] Đã nạp tệp <strong>${escapeHtml(state.notebook.importResult.filename)}</strong> (Layout: ${escapeHtml(state.notebook.importResult.layout_type)}) —
         Dòng gốc: ${state.notebook.importResult.raw_count} · Mới thêm: ${state.notebook.importResult.newly_imported_count} · Biến thể tự sinh: ${state.notebook.importResult.variants_generated}
       </div>`
    : "";

  root.innerHTML = `
    <div class="stack-md">
      <div class="section-header">
        <h2 id="notebook-heading" class="section-title">Sổ tay Lỗ hổng &amp; Smart Excel Importer</h2>
      </div>

      <div class="card">
        <h3 class="card-title">Hàng đợi Vá lỗ hổng (Relearning Queue)</h3>
        ${errContent}
      </div>

      <div class="card">
        <h3 class="card-title">Nạp thêm Đề thi Excel (.xlsx chuẩn Gemini)</h3>
        <p class="muted">Hệ thống tự nhận diện cả 4 mẫu sheet, khử trùng theo nội dung và tự sinh biến thể chống học vẹt.</p>
        <form id="excel-upload-form" class="form-row">
          <div class="field">
            <label for="inp-xlsx-file">Chọn tệp .xlsx</label>
            <input id="inp-xlsx-file" type="file" accept=".xlsx" class="input">
          </div>
          <button type="submit" class="btn-primary">Import Excel</button>
        </form>
        ${impBox}
      </div>

      <div class="card">
        <h3 class="card-title">Nguồn Đề Excel đã nạp (${wbs.length} tệp)</h3>
        <div class="table-scroll-wrap">
          <table class="data-table">
            <thead><tr><th>Tên tệp</th><th>Layout nhận diện</th><th>Số câu gốc</th><th>Câu duy nhất nạp</th><th>Thời điểm</th></tr></thead>
            <tbody>${wbRows}</tbody>
          </table>
        </div>
      </div>
    </div>
  `;

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
}

/* Global Keyboard Shortcuts (WCAG 2.1 AA) */
function handleGlobalKeydown(e) {
  trapModalFocus(e);
  if (e.key === "Escape") {
    closeHelpModal();
    return;
  }

  const tag = document.activeElement ? document.activeElement.tagName.toLowerCase() : "";
  if (tag === "input" || tag === "textarea" || tag === "select") return;
  const backdrop = document.getElementById("help-modal-backdrop");
  if (backdrop && !backdrop.hidden) return;

  if (e.key === "t" || e.key === "T") {
    toggleTheme();
    return;
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
  }
}

function bootstrapApp() {
  let savedTheme = "light";
  try {
    savedTheme = localStorage.getItem("n3_mastery_theme") || "light";
  } catch (e) {
    savedTheme = "light";
  }
  applyTheme(savedTheme);

  document.querySelectorAll(".nav-btn").forEach((btn) => {
    btn.addEventListener("click", () => switchView(btn.dataset.view));
  });
  document.getElementById("btn-theme-toggle").addEventListener("click", toggleTheme);
  document.getElementById("btn-help-modal").addEventListener("click", openHelpModal);
  document.getElementById("btn-close-help").addEventListener("click", closeHelpModal);
  document.getElementById("btn-ok-help").addEventListener("click", closeHelpModal);
  document.getElementById("help-modal-backdrop").addEventListener("click", (e) => {
    if (e.target.id === "help-modal-backdrop") closeHelpModal();
  });
  document.addEventListener("keydown", handleGlobalKeydown);

  loadDashboard();
}

document.addEventListener("DOMContentLoaded", bootstrapApp);
