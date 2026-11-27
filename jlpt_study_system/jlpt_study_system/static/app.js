/**
 * JLPT N3 STUDY SYSTEM - Executive Minimalist Frontend Client
 * Pure Vanilla JS, zero external build dependencies.
 */

// Application State
const state = {
    activeTab: 'dashboard',
    activeDay: 1,
    activeCardCategory: 'all',
    dueCards: [],
    currentCardIndex: 0,
    isCardFlipped: false,
    activeDrillMode: 'choukai',
    drillItems: [],
    currentDrillIndex: 0,
    drillStartTime: 0,
    drillTimerInterval: null,
    errorFilter: 'unresolved',
    pomodoro: {
        totalSeconds: 50 * 60,
        remainingSeconds: 50 * 60,
        isRunning: false,
        intervalId: null,
        dayNumber: 1,
        blockIndex: 1,
    }
};

// DOM Content Loaded Handler
document.addEventListener('DOMContentLoaded', () => {
    initNavigation();
    initClock();
    initDashboard();
    initCurriculum();
    initPomodoro();
    initFlashcards();
    initDrills();
    initErrorNotebook();
    initSeedButton();
    setupKeybindings();
});

// 1. Navigation Controller
function initNavigation() {
    const navItems = document.querySelectorAll('.nav-item');
    navItems.forEach(item => {
        item.addEventListener('click', () => {
            const tabId = item.getAttribute('data-tab');
            switchTab(tabId);
        });
    });
}

function switchTab(tabId) {
    state.activeTab = tabId;

    // Update active nav item
    document.querySelectorAll('.nav-item').forEach(el => {
        el.classList.toggle('active', el.getAttribute('data-tab') === tabId);
    });

    // Update active pane
    document.querySelectorAll('.tab-pane').forEach(el => {
        el.classList.toggle('active', el.id === `pane-${tabId}`);
    });

    // Update topbar breadcrumb
    const titles = {
        dashboard: 'READINESS DASHBOARD',
        curriculum: '7-DAY SPRINT & POMODORO',
        flashcards: 'FSRS FLASHCARDS',
        drills: 'INTERACTIVE DRILLS',
        errors: 'ERROR NOTEBOOK'
    };
    document.getElementById('current-module-title').innerText = titles[tabId] || 'STUDY SYSTEM';

    // Refresh view data
    if (tabId === 'dashboard') loadDashboardData();
    if (tabId === 'curriculum') loadCurriculumDay(state.activeDay);
    if (tabId === 'flashcards') loadDueCards();
    if (tabId === 'drills') loadDrillSet(state.activeDrillMode);
    if (tabId === 'errors') loadErrorNotebook();
}

// 2. UTC Time Ticker
function initClock() {
    const el = document.getElementById('system-time');
    const updateTime = () => {
        const now = new Date();
        el.innerText = now.toISOString().slice(11, 19) + ' UTC';
    };
    updateTime();
    setInterval(updateTime, 1000);
}

// 3. Readiness Dashboard
function initDashboard() {
    loadDashboardData();
}

async function loadDashboardData() {
    try {
        const [readinessRes, deckStatsRes, errorStatsRes] = await Promise.all([
            fetch('/api/readiness').then(r => r.json()),
            fetch('/api/cards/stats').then(r => r.json()),
            fetch('/api/error-notebook/stats').then(r => r.json())
        ]);

        // Render Hero Score
        document.getElementById('hero-total-score').innerText = readinessRes.total_score.toFixed(1);
        const passStatusEl = document.getElementById('hero-pass-status');
        if (readinessRes.pass_status === 'PASS') {
            passStatusEl.innerText = '[STATUS: PASS - READY FOR EXAM]';
            passStatusEl.className = 'hero-title text-success';
        } else if (readinessRes.pass_status === 'AT_RISK') {
            passStatusEl.innerText = '[STATUS: AT RISK - SECTION CUTOFF THREAT]';
            passStatusEl.className = 'hero-title text-warn';
        } else {
            passStatusEl.innerText = '[STATUS: FAIL - CRITICAL TRIAGE NEEDED]';
            passStatusEl.className = 'hero-title text-danger';
        }

        // Render 3 Gauges
        renderGauge('gengo', readinessRes.gengo);
        renderGauge('reading', readinessRes.reading);
        renderGauge('listening', readinessRes.listening);

        // Render Strategic Recommendations
        const recContainer = document.getElementById('recommendations-container');
        recContainer.innerHTML = readinessRes.critical_recommendations.map(rec =>
            `<div class="stat-row"><span class="stat-label text-primary">${escapeHtml(rec)}</span></div>`
        ).join('');

        // Render Deck Stats
        document.getElementById('stat-total-cards').innerText = deckStatsRes.total_cards;
        const reviewedCount = (deckStatsRes.states.Review || 0) + (deckStatsRes.states.Learning || 0) + (deckStatsRes.states.Relearning || 0);
        document.getElementById('stat-reviewed-cards').innerText = `${reviewedCount} / ${deckStatsRes.total_cards}`;
        document.getElementById('stat-retention-rate').innerText = `${deckStatsRes.retention_rate_pct}%`;
        document.getElementById('stat-total-reviews').innerText = deckStatsRes.total_reviews;

        // Render Error Stats
        document.getElementById('stat-unresolved-errors').innerText = errorStatsRes.unresolved_errors;
        document.getElementById('stat-remediated-errors').innerText = errorStatsRes.remediated_errors;
        document.getElementById('stat-remediation-rate').innerText = `${errorStatsRes.remediation_rate_pct}%`;

    } catch (err) {
        console.error('Failed to load dashboard data:', err);
    }
}

function renderGauge(sectionKey, sectionData) {
    document.getElementById(`score-${sectionKey}`).innerText = sectionData.score.toFixed(1);
    const pct = Math.min(100, Math.max(0, (sectionData.score / 60.0) * 100));
    const fillEl = document.getElementById(`bar-${sectionKey}`);
    fillEl.style.width = `${pct}%`;

    const statusEl = document.getElementById(`status-${sectionKey}`);
    if (sectionData.pass_cutoff) {
        fillEl.style.backgroundColor = 'var(--accent-ice)';
        statusEl.innerText = `[PASS] VƯỢT SÀN (${sectionData.score}/60 >= 19)`;
        statusEl.className = 'gauge-status text-success';
    } else {
        fillEl.style.backgroundColor = 'var(--state-danger)';
        statusEl.innerText = `[DANGER] NGUY CƠ LIỆT (${sectionData.score}/60 < 19)`;
        statusEl.className = 'gauge-status text-danger';
    }
}

// 4. Curriculum & Pomodoro
function initCurriculum() {
    const dayPills = document.querySelectorAll('.btn-day');
    dayPills.forEach(btn => {
        btn.addEventListener('click', () => {
            dayPills.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            const dayNum = parseInt(btn.getAttribute('data-day'), 10);
            state.activeDay = dayNum;
            state.pomodoro.dayNumber = dayNum;
            loadCurriculumDay(dayNum);
        });
    });
}

async function loadCurriculumDay(dayNum) {
    try {
        const [dayData, adviceData] = await Promise.all([
            fetch(`/api/curriculum/day/${dayNum}`).then(r => r.json()),
            fetch(`/api/curriculum/advice/${dayNum}`).then(r => r.json())
        ]);

        document.getElementById('curriculum-day-tag').innerText = `[DAY ${dayNum}]`;
        document.getElementById('curriculum-day-pct').innerText = `${dayData.completion_rate_pct}% Complete`;

        const listContainer = document.getElementById('curriculum-blocks-list');
        listContainer.innerHTML = dayData.blocks.map(block => `
            <div class="curriculum-block-item ${block.is_completed ? 'completed' : ''}" id="block-item-${block.id}">
                <div class="block-header">
                    <span class="block-time">[${block.block_name.toUpperCase()}] • ${block.planned_minutes} MIN</span>
                    <label class="label-xs flex-between" style="cursor: pointer;">
                        <input type="checkbox" ${block.is_completed ? 'checked' : ''} onchange="toggleBlockComplete(${block.id}, this.checked)">
                        <span style="margin-left: 6px;">${block.is_completed ? 'COMPLETED' : 'MARK DONE'}</span>
                    </label>
                </div>
                <div class="block-title">${escapeHtml(block.title)}</div>
                <div class="block-notes">${escapeHtml(block.notes)}</div>
            </div>
        `).join('');

        const adviceContainer = document.getElementById('curriculum-adaptive-advice');
        adviceContainer.innerHTML = adviceData.recommendations.map(adv =>
            `<div class="stat-row"><span class="stat-label text-primary">${escapeHtml(adv)}</span></div>`
        ).join('');

    } catch (err) {
        console.error('Failed to load curriculum day:', err);
    }
}

window.toggleBlockComplete = async function(blockId, isCompleted) {
    try {
        await fetch(`/api/curriculum/block/${blockId}/complete`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ is_completed: isCompleted })
        });
        loadCurriculumDay(state.activeDay);
    } catch (err) {
        console.error('Failed to toggle block completion:', err);
    }
};

// Pomodoro Timer Controller
function initPomodoro() {
    const btnToggle = document.getElementById('btn-pomo-toggle');
    const btnReset = document.getElementById('btn-pomo-reset');

    btnToggle.addEventListener('click', togglePomodoro);
    btnReset.addEventListener('click', resetPomodoro);
    updatePomodoroDisplay();
    refreshPomodoroSummary();
}

function togglePomodoro() {
    const btn = document.getElementById('btn-pomo-toggle');
    if (state.pomodoro.isRunning) {
        clearInterval(state.pomodoro.intervalId);
        state.pomodoro.isRunning = false;
        btn.innerText = 'RESUME SPRINT BLOCK';
        btn.className = 'btn btn-primary btn-block';
    } else {
        state.pomodoro.isRunning = true;
        btn.innerText = 'PAUSE SPRINT BLOCK';
        btn.className = 'btn btn-secondary btn-block';
        state.pomodoro.intervalId = setInterval(tickPomodoro, 1000);
    }
}

function tickPomodoro() {
    if (state.pomodoro.remainingSeconds > 0) {
        state.pomodoro.remainingSeconds--;
        updatePomodoroDisplay();
    } else {
        // Complete block!
        clearInterval(state.pomodoro.intervalId);
        state.pomodoro.isRunning = false;
        document.getElementById('btn-pomo-toggle').innerText = 'START SPRINT BLOCK';
        completePomodoroSession();
    }
}

function resetPomodoro() {
    clearInterval(state.pomodoro.intervalId);
    state.pomodoro.isRunning = false;
    state.pomodoro.remainingSeconds = state.pomodoro.totalSeconds;
    document.getElementById('btn-pomo-toggle').innerText = 'START SPRINT BLOCK';
    document.getElementById('btn-pomo-toggle').className = 'btn btn-primary btn-block';
    updatePomodoroDisplay();
}

function updatePomodoroDisplay() {
    const mins = Math.floor(state.pomodoro.remainingSeconds / 60);
    const secs = state.pomodoro.remainingSeconds % 60;
    const pad = (n) => (n < 10 ? '0' + n : n);
    document.getElementById('pomo-timer').innerText = `${pad(mins)}:${pad(secs)}`;
}

async function completePomodoroSession() {
    const taskInput = document.getElementById('pomo-task-input');
    const taskLabel = taskInput.value || 'General Sprint Review';
    try {
        await fetch('/api/pomodoro/session', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                day_number: state.activeDay,
                block_index: state.pomodoro.blockIndex++,
                task_label: taskLabel,
                duration_minutes: 50,
                status: 'completed'
            })
        });
        alert('[POMODORO COMPLETE] Hoàn thành xuất sắc 1 block 50 phút! Nghỉ ngơi 10 phút trước khi bắt đầu block tiếp theo.');
        resetPomodoro();
        refreshPomodoroSummary();
    } catch (err) {
        console.error('Failed to log pomodoro session:', err);
    }
}

async function refreshPomodoroSummary() {
    try {
        const summary = await fetch(`/api/pomodoro/summary?day_number=${state.activeDay}`).then(r => r.json());
        document.getElementById('pomo-target').innerText = `Today: ${summary.completed_sessions} / 12 Blocks Completed (${summary.total_study_minutes} min)`;
    } catch (err) {
        console.error('Failed to fetch pomodoro summary:', err);
    }
}

// 5. FSRS Flashcard Engine
function initFlashcards() {
    const filterBtns = document.querySelectorAll('.btn-filter');
    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            state.activeCardCategory = btn.getAttribute('data-cat');
            loadDueCards();
        });
    });

    // Card flip interaction
    const cardBox = document.getElementById('flashcard-box');
    cardBox.addEventListener('click', flipCard);

    // Rating buttons
    document.querySelectorAll('.btn-rating').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            const rating = parseInt(btn.getAttribute('data-rating'), 10);
            submitCardRating(rating);
        });
    });
}

async function loadDueCards() {
    try {
        let url = '/api/cards/due?limit=100';
        if (state.activeCardCategory !== 'all') {
            url += `&category=${state.activeCardCategory}`;
        }
        const cards = await fetch(url).then(r => r.json());
        state.dueCards = cards;
        state.currentCardIndex = 0;
        state.isCardFlipped = false;
        document.getElementById('cards-due-count').innerText = `Due: ${cards.length} cards`;
        renderCurrentCard();
    } catch (err) {
        console.error('Failed to load due cards:', err);
    }
}

function renderCurrentCard() {
    const box = document.getElementById('flashcard-box');
    const backWrapper = document.getElementById('card-back-wrapper');
    const catBadge = document.getElementById('card-cat-badge');
    const frontText = document.getElementById('card-front-text');
    const backText = document.getElementById('card-back-text');
    const trapText = document.getElementById('card-trap-text');
    const exampleText = document.getElementById('card-example-text');
    const trapBox = document.getElementById('card-trap-box');
    const exampleBox = document.getElementById('card-example-box');

    state.isCardFlipped = false;
    backWrapper.classList.add('hidden');

    if (!state.dueCards || state.dueCards.length === 0 || state.currentCardIndex >= state.dueCards.length) {
        catBadge.innerText = '[DECK COMPLETED]';
        frontText.innerText = 'All scheduled reviews completed for this session!';
        backText.innerText = '';
        trapBox.classList.add('hidden');
        exampleBox.classList.add('hidden');
        return;
    }

    const item = state.dueCards[state.currentCardIndex];
    catBadge.innerText = `[${item.card.category.toUpperCase()}] • State: ${item.fsrs.state}`;
    frontText.innerText = item.card.front;
    backText.innerText = item.card.back;

    if (item.card.trap) {
        trapBox.classList.remove('hidden');
        trapText.innerText = item.card.trap;
    } else {
        trapBox.classList.add('hidden');
    }

    if (item.card.example) {
        exampleBox.classList.remove('hidden');
        exampleText.innerText = item.card.example;
    } else {
        exampleBox.classList.add('hidden');
    }
}

function flipCard() {
    if (state.dueCards.length === 0 || state.currentCardIndex >= state.dueCards.length) return;
    state.isCardFlipped = !state.isCardFlipped;
    const backWrapper = document.getElementById('card-back-wrapper');
    backWrapper.classList.toggle('hidden', !state.isCardFlipped);
}

async function submitCardRating(rating) {
    if (!state.dueCards || state.currentCardIndex >= state.dueCards.length) return;
    const currentItem = state.dueCards[state.currentCardIndex];

    try {
        await fetch('/api/cards/review', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                card_id: currentItem.card.id,
                rating: rating,
                elapsed_seconds: 3.0
            })
        });

        state.currentCardIndex++;
        renderCurrentCard();
        document.getElementById('cards-due-count').innerText = `Due: ${state.dueCards.length - state.currentCardIndex} cards`;
    } catch (err) {
        console.error('Failed to submit card review:', err);
    }
}

// 6. Interactive Drills (Choukai Speed Reflex & Dokkai Decoder)
function initDrills() {
    document.querySelectorAll('.btn-drill-mode').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.btn-drill-mode').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            state.activeDrillMode = btn.getAttribute('data-drill');
            loadDrillSet(state.activeDrillMode);
        });
    });

    document.getElementById('btn-reload-drill').addEventListener('click', () => {
        loadDrillSet(state.activeDrillMode);
    });

    document.getElementById('btn-next-drill-question').addEventListener('click', () => {
        state.currentDrillIndex++;
        renderCurrentDrill();
    });
}

async function loadDrillSet(mode) {
    clearInterval(state.drillTimerInterval);
    const endpoint = mode === 'choukai' ? '/api/drills/choukai?count=10' : '/api/drills/dokkai?count=10';
    try {
        const items = await fetch(endpoint).then(r => r.json());
        state.drillItems = items;
        state.currentDrillIndex = 0;
        renderCurrentDrill();
    } catch (err) {
        console.error('Failed to load drill items:', err);
    }
}

function renderCurrentDrill() {
    clearInterval(state.drillTimerInterval);
    const feedbackBox = document.getElementById('drill-feedback-box');
    feedbackBox.classList.add('hidden');

    if (!state.drillItems || state.currentDrillIndex >= state.drillItems.length) {
        document.getElementById('drill-prompt-text').innerText = 'Drill session completed! Excellent focus.';
        document.getElementById('drill-options-container').innerHTML = '';
        return;
    }

    const item = state.drillItems[state.currentDrillIndex];
    document.getElementById('drill-section-tag').innerText = `[${item.section.toUpperCase()}]`;
    document.getElementById('drill-prompt-context').innerText = item.context || 'Interactive Prompt';
    document.getElementById('drill-prompt-text').innerText = item.prompt;

    const optContainer = document.getElementById('drill-options-container');
    optContainer.innerHTML = item.options.map((opt, idx) => `
        <button class="drill-option-btn" id="drill-opt-${idx}" onclick="selectDrillOption(${item.id}, ${idx})">
            <span class="label-xs" style="margin-right: 8px;">[${idx + 1}]</span>
            ${escapeHtml(opt)}
        </button>
    `).join('');

    // Start 3-second reflex stopwatch
    state.drillStartTime = performance.now();
    const timerEl = document.getElementById('drill-stopwatch');
    timerEl.innerText = '0.0s';
    timerEl.style.color = 'var(--accent-ice)';

    state.drillTimerInterval = setInterval(() => {
        const elapsed = (performance.now() - state.drillStartTime) / 1000;
        timerEl.innerText = elapsed.toFixed(1) + 's';
        if (elapsed > 3.0 && state.activeDrillMode === 'choukai') {
            timerEl.style.color = 'var(--state-danger)';
        }
    }, 100);
}

window.selectDrillOption = async function(itemId, selectedIdx) {
    clearInterval(state.drillTimerInterval);
    const elapsedSec = (performance.now() - state.drillStartTime) / 1000;

    // Disable all options
    document.querySelectorAll('.drill-option-btn').forEach(btn => btn.disabled = true);

    try {
        const res = await fetch('/api/drills/submit', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                item_id: itemId,
                selected_index: selectedIdx,
                response_time_sec: elapsedSec
            })
        }).then(r => r.json());

        // Highlight options
        const selBtn = document.getElementById(`drill-opt-${selectedIdx}`);
        const correctBtn = document.getElementById(`drill-opt-${res.correct_index}`);

        if (res.is_correct) {
            selBtn.classList.add('correct');
        } else {
            selBtn.classList.add('wrong');
            if (correctBtn) correctBtn.classList.add('correct');
        }

        // Show feedback
        const feedbackBox = document.getElementById('drill-feedback-box');
        const feedbackTitle = document.getElementById('drill-feedback-title');
        const feedbackTrap = document.getElementById('drill-feedback-trap');

        feedbackBox.classList.remove('hidden');
        if (res.is_correct) {
            feedbackTitle.innerText = `[CHÍNH XÁC] Phản xạ hoàn thành trong ${elapsedSec.toFixed(1)} giây.`;
            feedbackTitle.className = 'feedback-status text-success';
        } else {
            feedbackTitle.innerText = `[BẪY TRẮC NGHIỆM] Đã ghi nhận vào Sổ tay bẫy!`;
            feedbackTitle.className = 'feedback-status text-danger';
        }
        feedbackTrap.innerText = res.trap_analysis;

    } catch (err) {
        console.error('Failed to submit drill answer:', err);
    }
};

// 7. Error Notebook Controller
function initErrorNotebook() {
    const filterBtns = document.querySelectorAll('.btn-error-filter');
    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            state.errorFilter = btn.getAttribute('data-filter');
            loadErrorNotebook();
        });
    });
}

async function loadErrorNotebook() {
    try {
        let url = '/api/error-notebook?limit=200';
        if (state.errorFilter === 'unresolved') {
            url += '&remediated=false';
        }
        const errors = await fetch(url).then(r => r.json());
        const tbody = document.getElementById('error-notebook-tbody');

        if (!errors || errors.length === 0) {
            tbody.innerHTML = `<tr><td colspan="6" class="text-center text-muted">Không có bẫy trắc nghiệm tồn đọng. Toàn bộ lỗ hổng đã được vá sạch!</td></tr>`;
            return;
        }

        tbody.innerHTML = errors.map(err => `
            <tr>
                <td><span class="tag tag-accent">[${err.item_type.toUpperCase()}]</span></td>
                <td style="max-width: 260px;"><strong>${escapeHtml(err.prompt)}</strong></td>
                <td class="text-success" style="max-width: 200px;">${escapeHtml(err.correct_answer)}</td>
                <td style="max-width: 320px; font-size: 12px;">${escapeHtml(err.trap_analysis)}</td>
                <td class="text-center font-mono">${err.attempt_count}</td>
                <td>
                    ${err.remediated ?
                        '<span class="text-success">[REMEDIATED]</span>' :
                        `<button class="btn btn-secondary btn-sm" onclick="remediateTrap(${err.id})">ĐÃ KHẮC PHỤC</button>`
                    }
                </td>
            </tr>
        `).join('');

    } catch (err) {
        console.error('Failed to load error notebook:', err);
    }
}

window.remediateTrap = async function(errId) {
    try {
        await fetch(`/api/error-notebook/${errId}/remediate`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ success: true })
        });
        loadErrorNotebook();
    } catch (err) {
        console.error('Failed to remediate error item:', err);
    }
};

// 8. Re-index Button Controller
function initSeedButton() {
    const btn = document.getElementById('btn-seed-data');
    btn.addEventListener('click', async () => {
        if (!confirm('Re-index and reload all grammar, vocab CSVs, and markdown drills into database?')) return;
        btn.disabled = true;
        btn.innerText = 'RE-INDEXING...';
        try {
            await fetch('/api/seed', { method: 'POST' });
            alert('[INDEX COMPLETE] Đã nạp thành công toàn bộ dữ liệu thẻ và đề luyện.');
            loadDashboardData();
            loadCurriculumDay(state.activeDay);
            loadDueCards();
        } catch (err) {
            console.error('Seed failed:', err);
        } finally {
            btn.disabled = false;
            btn.innerText = 'RE-INDEX ASSETS';
        }
    });
}

// 9. Keyboard Shortcuts (1, 2, 3, 4, Space)
function setupKeybindings() {
    window.addEventListener('keydown', (e) => {
        if (state.activeTab === 'flashcards') {
            if (e.code === 'Space') {
                e.preventDefault();
                flipCard();
            } else if (e.key === '1') {
                submitCardRating(1);
            } else if (e.key === '2') {
                submitCardRating(2);
            } else if (e.key === '3') {
                submitCardRating(3);
            } else if (e.key === '4') {
                submitCardRating(4);
            }
        }
    });
}

function escapeHtml(str) {
    if (!str) return '';
    return str
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
}
