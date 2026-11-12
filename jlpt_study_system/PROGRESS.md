# TIẾN ĐỘ DỰ ÁN & CHUYỂN GIAO TRẠNG THÁI (PROJECT PROGRESS)

## Handoff Anchor
- **Active Task:** TASK-09 (Hardening, Zero-Sycophancy Readiness Calibration & Full Test Isolation)
- **Current State:** VERIFIED_PASS
- **Active Environment:** Python 3.11 (`py -3.11` / `C:\Users\kien1\AppData\Local\Programs\Python\Python311\python.exe`)
- **Target Files:** `jlpt_study_system/`, `tests/`, `jlpt_cli.py`, `README.md`
- **Last Verification:** `py -3.11 -m pytest tests/` (exit code: 0, 48 passed in 3.14s)
- **Next Immediate Action:** Ready for user study sprint via `py -3.11 jlpt_cli.py serve` or CLI workflows
- **Blockers / Risks:** None

---

## Bảng Theo Dõi Nhiệm Vụ (Default-FAIL Contract)

| Task ID | Nhiệm Vụ | Trạng Thái | Lệnh Kiểm Thử Thực Tế | Exit Code | Bằng Chứng / Output Digest | Thời Điểm |
| :--- | :--- | :---: | :--- | :---: | :--- | :--- |
| **TASK-01** | Khởi tạo cấu trúc & mô hình dữ liệu (SQLite & Pydantic) | [x] PASS | `py -3.11 -m pytest tests/test_database.py` | `0` | 3 passed (schema, foreign keys, rollback) | 2026-11-22 21:22 |
| **TASK-02** | Xây dựng bộ lập lịch FSRS Spaced Repetition | [x] PASS | `py -3.11 -m pytest tests/test_fsrs.py` | `0` | 8 passed (ratings 1..4, intervals, auto-remediation) | 2026-11-22 21:57 |
| **TASK-03** | Triển khai Data Importer nạp CSV & Markdown | [x] PASS | `py -3.11 -m pytest tests/test_importer.py` | `0` | 4 passed (CSV + Markdown parser real file) | 2026-11-22 21:57 |
| **TASK-04** | Xây dựng Curriculum Tracker, Pomodoro & Adaptive Engine | [x] PASS | `py -3.11 -m pytest tests/test_curriculum.py` | `0` | 5 passed (blocks, 7-day targets, adaptive advice) | 2026-11-22 21:57 |
| **TASK-05** | Bộ tính điểm Sectional Readiness & Error Notebook | [x] PASS | `py -3.11 -m pytest tests/test_readiness.py` | `0` | 3 passed (honest cutoff triggers, sample volume weighting) | 2026-11-22 21:57 |
| **TASK-06** | Engine thi thử & phản xạ tức thì (Drill & Quiz Engine) | [x] PASS | `py -3.11 -m pytest tests/test_quiz_engine.py` | `0` | 6 passed (reflex drills, dokkai decoder, auto-remediation) | 2026-11-22 21:57 |
| **TASK-07** | FastAPI REST Backend & Nordic Frost SPA Web UI | [x] PASS | `py -3.11 -m pytest tests/test_api.py` | `0` | 10 passed (isolated client, REST endpoints & HTML 200 OK) | 2026-11-22 21:57 |
| **TASK-08** | Rich CLI Interface & E2E Verification | [x] PASS | `py -3.11 -m pytest tests/test_cli.py` | `0` | 9 passed (interactive mock study, drills, pomodoro, routing) | 2026-11-22 21:57 |
| **TASK-09** | Thẩm định phản biện, khử tô hồng điểm số & cô lập môi trường test | [x] PASS | `py -3.11 -m pytest tests/` | `0` | 48/48 passed cleanly without touching production DB | 2026-11-22 21:57 |

---

## Nhật Ký Chi Tiết Từng Lượt Chuyển Giao (Handoff Log)
- **2026-11-22 21:10 [Worker Subagent]**: Khởi tạo cấu trúc dự án `d:\Development\jlpt_study_system`, bắt đầu lập trình lõi hệ thống theo kỷ luật Karpathy Guardrails.
- **2026-11-22 21:24 [Worker Subagent]**: Hoàn thiện toàn bộ hệ thống gồm FSRS Spaced Repetition, Pomodoro 50-10, Curriculum 7 ngày, Sectional Readiness, Interactive Drills, Error Notebook, FastAPI REST API, Nordic Frost SPA Web UI, và Rich CLI. Xác thực 39/39 bài kiểm thử đạt kết quả 100% pass sạch với exit code 0.
- **2026-11-22 21:57 [Antigravity Reviewer]**: 
  - Khắc phục lỗi tô hồng điểm số (Zero-Sycophancy): điểm dự phóng unstudied ban đầu trả về đúng điểm sàn liệt N5 (13-14 điểm < sàn 19), kích hoạt đúng Báo động đỏ; khắc phục lỗi chỉ trả lời 5 câu nghe đã cho 60/60 điểm bằng trọng số mẫu kiểm thử.
  - Khắc phục rò rỉ cơ sở dữ liệu test: bổ sung biến môi trường `JLPT_DB_PATH`, bảo đảm toàn bộ test suite chạy trên database tạm thời cô lập, không ghi đè vào `data/jlpt_study.db`.
  - Bổ sung parser đọc động Markdown từ `DAY_BY_DAY_PLAYBOOK.md`.
  - Khắc phục lỗi bỏ qua tham số category trong CLI study và xử lý an toàn kiểu chuỗi.
  - Bổ sung cơ chế tự động giải trừ bẫy (auto-remediation) khi học viên ôn tập đạt Good/Easy hoặc trả lời đúng câu hỏi trắc nghiệm.
  - Mở rộng bộ test từ 39 lên 48 bài kiểm thử, kiểm thử toàn diện các tương tác dòng lệnh (CLI study, drill, pomodoro).
