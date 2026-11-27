# JLPT N3 SPRINT STUDY SYSTEM (BỘ CÔNG CỤ TÁC CHIẾN 7 NGÀY)

Hệ thống công cụ quản trị học tập chuyên sâu hỗ trợ lộ trình sinh tồn JLPT N3 trong 7 ngày (từ nền tảng N5), vận hành theo nguyên lý Pareto 80/20 nhằm vượt ngưỡng đỗ an toàn (tổng điểm >= 95/180, điểm thành phần >= 19/60 ở cả 3 phân môn: Kiến thức ngôn ngữ, Đọc hiểu, Nghe hiểu).

---

## 1. TỔNG QUAN KIẾN TRÚC & TÍNH NĂNG CỐT LÕI

Dự án được xây dựng theo kiến trúc mô-đun hóa cao, kế thừa kỷ luật thiết kế Executive Minimalist (Nordic Frost) và Kỷ luật Thợ máy Karpathy Guardrails.

```text
jlpt_study_system/
├── jlpt_study_system\
│   ├── __init__.py           # Package meta
│   ├── config.py             # Tham số cắt ngưỡng (19/60, 95/180), FSRS retention, Pomodoro
│   ├── database.py           # SQLite persistence với WAL mode & Foreign Keys
│   ├── models.py             # Pydantic & Enums schemas
│   ├── importer.py           # Bộ nạp dữ liệu tự động từ CSV & Markdown (idempotent)
│   ├── fsrs_scheduler.py     # Thuật toán Spaced Repetition FSRS (Sprint 7 ngày)
│   ├── curriculum.py         # Quản trị lộ trình 7 ngày & Bộ đếm Pomodoro 50/10 & Adaptive
│   ├── readiness.py          # Bộ tính điểm năng lực thực tế & Báo động sàn liệt
│   ├── quiz_engine.py        # Động cơ trắc nghiệm phản xạ tức thì Mondai 5 & Đọc quét Dokkai
│   ├── error_notebook.py     # Sổ tay bẫy trắc nghiệm & Quy trình vá lỗ hổng
│   ├── api.py                # FastAPI REST API & Lifespan handler
│   ├── cli.py                # Rich Terminal Interface
│   ├── templates\
│   │   └── index.html        # Single-Page Application (SPA) UI
│   └── static\
│       ├── app.css           # Bảng màu Nordic Frost Minimal (#16161A, #38BDF8, #E2E8F0)
│       └── app.js            # Pure Vanilla JS (Zero external build tool)
├── tests\                    # 39 kiểm thử tự động pytest
├── data\                     # Lưu trữ SQLite (jlpt_study.db)
├── jlpt_cli.py               # Trình khởi chạy dòng lệnh tiện lợi
└── README.md
```

### Các Tính Năng Trọng Tâm:
1. **Bộ Lập Lịch Khoa Học (FSRS Spaced Repetition)**:
   - 4 mức đánh giá phản xạ: Again (1), Hard (2), Good (3), Easy (4).
   - Tối ưu hóa chu kỳ ôn tập co cụm trong khung 7 ngày (Desired Retention: 0.80).
   - Thẻ đánh giá "Again" tự động chuyển trạng thái học lại trong ngày (10 phút) và tự động ghi nhận bẫy vào Sổ tay bẫy trắc nghiệm.
2. **Quản Lý Phiên Học 50-10 Pomodoro & Lộ Trình 7 Ngày**:
   - Khung giờ 50 phút tập trung sâu, 10 phút nghỉ ngơi (chỉ tiêu 12 block/ngày ~ 10-12 giờ tác chiến).
   - Đánh dấu hoàn thành từng block: Sáng (240 phút), Chiều (210 phút), Tối (300 phút).
   - Thuật toán thích ứng (Adaptive Rebalancing): Tự động phát hiện điểm yếu (ví dụ: bẫy Ngữ pháp họ わけ còn tồn đọng) để đưa ra chỉ dẫn điều chỉnh ngày học kế tiếp.
3. **Đo Lường Năng Lực Thành Phần (Sectional Readiness & Cutoff Safeguards)**:
   - Dự phóng điểm số thực tế trên thang 60 điểm cho từng phân môn:
     - Kiến thức ngôn ngữ (Gengo Chishiki): Đánh giá qua độ bao phủ và tỷ lệ nhớ flashcard.
     - Đọc hiểu (Dokkai): Đánh giá qua độ thành thạo từ nối và độ chính xác câu hỏi đọc quét.
     - Nghe hiểu (Choukai): Đánh giá qua độ chính xác và tốc độ phản xạ (< 3 giây) câu hỏi Mondai 5.
   - Báo động đỏ tức thời nếu bất kỳ phân môn nào có nguy cơ rớt xuống dưới sàn liệt (< 19 điểm).
4. **Động Cơ Trắc Nghiệm Phản Xạ & Giải Mã Đọc Hiểu**:
   - Mondai 5 Instant Reflex: Bấm giờ phản xạ thực tế (Stopwatch), đo lường ngưỡng quyết định trong 3 giây.
   - 4-Step Reading Decoder: Luyện tập kỹ thuật loại trừ bẫy tuyệt đối hóa (`すべて`, `絶対に`), bẫy thông tin ngoài bài và kỹ thuật quét dấu hoa thị (*).
5. **Sổ Tay Bẫy Trắc Nghiệm (Error Notebook)**:
   - Tự động bắt lỗi mọi câu làm sai hoặc thẻ nhớ bị khựng (Again/Hard).
   - Giải mã chi tiết lý do bẫy (Distinction analysis) và hỗ trợ quy trình vá lỗi (Remediation).

---

## 2. HƯỚNG DẪN CÀI ĐẶT & KHỞI CHẠY

Cài các thư viện từ `requirements.txt` ở thư mục gốc và chạy các lệnh sau trong `jlpt_study_system`.

### Khởi tạo Cơ sở dữ liệu:
```powershell
py -3.11 jlpt_cli.py init
```
Lệnh trên sẽ tự động nạp toàn bộ 40 mẫu ngữ pháp hạt nhân, 40 từ nối lập luận, 10 mẫu phản xạ nghe hiểu Mondai 5, 5 bài đọc quét và lộ trình 7 ngày vào `data/jlpt_study.db`.

### Xem Bảng Điểm Dự Phóng & Trạng Thái Sẵn Sàng (CLI Status):
```powershell
py -3.11 jlpt_cli.py status
```

### Học Thẻ Spaced Repetition trong Terminal:
```powershell
py -3.11 jlpt_cli.py study --limit 20
```
- Phím `Enter`: Lật mặt sau thẻ để xem nghĩa, bẫy trắc nghiệm và ví dụ.
- Phím `1` (Again), `2` (Hard), `3` (Good), `4` (Easy): Ghi nhận phản xạ.

### Luyện Phản Xạ Nghe Hiểu / Đọc Hiểu (CLI Drill):
```powershell
py -3.11 jlpt_cli.py drill choukai
# hoặc
py -3.11 jlpt_cli.py drill dokkai
```

### Khởi Chạy Giao Diện Web Single-Page Application (FastAPI UI):
```powershell
py -3.11 jlpt_cli.py serve --port 8000
```
Sau đó mở trình duyệt tại: `http://127.0.0.1:8000`

---

## 3. PHÍM TẮT & TƯƠNG TÁC GIAO DIỆN WEB

Giao diện tuân thủ chuẩn mực **Nordic Frost Minimal**:
- Nền Matte Dark Slate (`#16161A`, `#1E1E24`), chữ Silver (`#F4F4F6`), màu nhấn Xanh băng (`#38BDF8`).
- Hoàn toàn không sử dụng emoji trang trí.
- **Phím tắt trên tab Flashcards**:
  - `Phím Cách (Space)`: Lật mặt sau thẻ.
  - `1`: Đánh giá AGAIN (10 phút / Lỗi nhớ).
  - `2`: Đánh giá HARD (1 ngày).
  - `3`: Đánh giá GOOD (2-3 ngày).
  - `4`: Đánh giá EASY (4-5 ngày).
