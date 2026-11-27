# DESIGN SYSTEM — N3 10/10 MASTERY WORKSPACE

Tài liệu này và [tokens.json](file:///d:/NEXUS/01_Life_Ops/Language_Lab/n3_ten_point_mastery/tokens.json) là **Nguồn chân lý duy nhất (Single Source of Truth)** cho toàn bộ giao diện Web SPA của hệ thống `n3_ten_point_mastery`.

---

## 1. Hệ thống Chủ đề (Dual-Theme Editorial System)

1. **Chế độ mặc định — `Academic Editorial Light`** (Tối ưu đọc chữ Hán & Dokkai dài hạn không mỏi mắt):
   - Nền chính (`--bg-base`): `#FAFAF9` (Warm Off-White)
   - Bề mặt thẻ (`--bg-surface`): `#FFFFFF`
   - Nền phụ (`--bg-canvas`): `#F4F4F5`
   - Chữ chính (`--text-primary`): `#18181B`, phụ `#3F3F46`, chú thích `#52525B`
   - Viền mảnh 1px (`--border-subtle`): `#E4E4E7`
   - Màu nhấn (`--accent-primary`): `#1D4ED8`
   - Ngữ nghĩa: Đúng `#15803D`, Cảnh báo `#B45309`, Sai/Lỗ hổng `#B91C1C` (tất cả đạt tương phản WCAG 2.1 AA >= 4.5:1).
2. **Chế độ chuyển đổi — `Nordic Frost Matte Dark`** (Toggle bằng nút trên thanh đầu trang hoặc phím `T`, lưu `localStorage`):
   - Nền ứng dụng (`--bg-canvas`): `#121214`, nền chính (`--bg-base`): `#1E1E24`, thẻ (`--bg-surface`): `#16161A`
   - Chữ chính (`--text-primary`): `#F4F4F6`, phụ `#E2E8F0`, mờ `#94A3B8`
   - Viền mảnh 1px (`--border-subtle`): `#2E2E38`
   - Màu nhấn (`--accent-primary`): `#38BDF8`

---

## 2. Quy chuẩn Typography & Tiếng Nhật

- **Font chữ:** `'Noto Sans JP', 'Hiragino Sans', 'Yu Gothic UI', Inter, 'Segoe UI', Roboto, sans-serif`.
- **Con số:** Mọi điểm số (`/10.00`), bộ đếm câu, thời gian và FSRS stability sử dụng `font-variant-numeric: tabular-nums`.
- **Văn bản Đọc hiểu (Dokkai):**
  - Chiều rộng cột đọc giới hạn `65ch` – `75ch` (`max-width: 72ch`).
  - Giãn dòng `line-height: 1.95` để chứa `<ruby><rt>` Furigana phía trên chữ Hán không dính dòng.
- **Vùng từ khóa đang kiểm tra (`【...】`):** Hiển thị khung viền nhấn `--mask-border` trên nền `--mask-bg`, tuyệt đối không chèn Furigana hay Hán-Việt trước khi người học nộp đáp án.

---

## 3. Hàng rào Chống AI UI Slop (Bắt buộc)

- **Cấm 100% Emoji trang trí** (tên lửa, ngọn lửa, bóng đèn, vương miện, sticker 3D) trong giao diện, thông báo, nhật ký và code. Chỉ dùng thẻ cấu trúc (`[OK]`, `[WARN]`, `[FAIL]`, `[INFO]`, `[MASTERED 10/10]`) hoặc SVG nét mảnh `1.5px` (`16px–20px`) đơn sắc theo biến `currentColor`.
- **Cấm Gradient cầu vồng / neon**, cấm viền phát sáng (`glow`), cấm Glassmorphism (`backdrop-blur`) trên nội dung đọc chính, cấm thẻ KPI trang trí vô nghĩa.
- **Thang khoảng cách chuẩn:** `4px`, `8px`, `12px`, `16px`, `24px`, `32px`.

---

## 4. 4 Trạng thái Biên & Tiếp cận (WCAG 2.1 AA)

1. **Loading Skeleton:** Mọi khu vực nạp dữ liệu bất đồng bộ hiển thị khung xương tỷ lệ thật (`skeleton-box`), không để chữ `"Loading..."` trơ trọi.
2. **Empty State + CTA:** Khi Sổ tay Lỗ hổng trống, hàng đợi ôn tập trống, hoặc chưa có dữ liệu đề, hiển thị bảng trạng thái trung thực kèm nút hành động chính (CTA).
3. **Error State + Retry:** Khi gọi API lỗi, hiển thị thông báo lỗi cụ thể kèm nút `Thử lại` kích hoạt lại request.
4. **Overflow Handling:** Mọi khối văn bản dài, tên file `.xlsx`, câu hỏi Nhật/Việt dùng `min-w-0` và `overflow-wrap: anywhere`; bảng dữ liệu dùng `.table-scroll-wrap` (`overflow-x: auto`) để đảm bảo `scrollWidth <= innerWidth` trên Mobile `390x844`.
5. **Tiếp cận bàn phím & Modal:**
   - Thanh điều hướng dùng `<nav aria-label="...">`.
   - Mọi nút chỉ có icon có `aria-label`.
   - Modal dùng `<dialog>` / `role="dialog"` + `aria-modal="true"` + focus-trap + đóng bằng `Esc`.
   - Phím tắt thao tác nhanh: `1`–`4` (chọn đáp án trong Luyện tập & Luyện Ngữ pháp), `Space` (nộp/kiểm tra hoặc câu tiếp theo khi không gõ trong input), `H` (gợi ý Giàn giáo Cấp 2), `T` (đổi Light/Dark), `Esc` (đóng hộp thoại).

---

## 5. Thành phần Học Ngữ pháp, Từ vựng Nền tảng & Mở rộng JLPT (`view-grammar`)

Không gian `Ngữ pháp & JLPT` (`#view-grammar`) dùng hoàn toàn CSS variables từ `tokens.json` (hỗ trợ cả `Academic Editorial Light` và `Nordic Frost Matte Dark`) và tuân thủ đủ 4 trạng thái biên (`Skeleton`, `Empty + CTA`, `Error + Retry`, `Overflow` an toàn trên Mobile `390x844`).

1. **Điều hướng phụ 4 phân khu (`.subnav-tabs`):**
   - `Thư viện Ngữ pháp`: Bộ lọc Phạm vi (`Tất cả` | `Bộ đề .xlsx Cuối kì` `[THI CUỐI KÌ]` | `Mở rộng JLPT` `[MỞ RỘNG JLPT]`), Cấp độ (`ALL`, `N5`, `N4`, `N3`, `N2`), Danh mục, Trạng thái FSRS và ô tìm kiếm.
   - `Luyện Ngữ pháp Sư phạm`: Chọn chế độ (`mixed` Tổng hợp 3 bước | `formation` Chia thể & Kết hợp | `contrast` Phân biệt cặp dễ nhầm | `application` Ứng dụng ngữ cảnh), Phạm vi và Cấp độ. Trước khi nộp bài chỉ hiển thị `prompt_jp` và 4 phương án xáo seed (Zero-Answer-Leakage); sau khi nộp bài hiển thị phản hồi chẩn đoán lỗi chi tiết cho từng phương án (`option_diagnostics`, `selected_diagnostic`), giải thích bản chất và nút chuyển về bài học hoặc câu tiếp theo. Hỗ trợ phím tắt `1`–`4` và `Space`.
   - `Nền tảng Từ vựng & Chữ Hán`: Bảng/thẻ tra cứu có `.table-scroll-wrap` hiển thị Chữ viết, Hiragana, Âm Hán-Việt, Bộ thủ/Ghi chú, Nghĩa & Collocation, Nguồn & Câu hỏi liên quan (bấm nhảy thẳng sang `study`).
   - `Mở rộng Kỳ thi JLPT`: Bảng tiến độ theo từng cấp độ `N5`, `N4`, `N3`, `N2` từ `overview.levels` và biểu mẫu nạp gói mở rộng `.json` / `.xlsx` (`POST /api/grammar/import`) kèm khối cấu trúc JSON mẫu có `overflow-wrap: anywhere`.

2. **Thẻ & Bài học Ngữ pháp 3 Chiều (Form – Meaning – Use):**
   - Thẻ tóm tắt hiển thị `pattern`, nhãn cấp độ (`[N5]`..`[N2]`), nhãn nguồn (`[THI CUỐI KÌ]` hoặc `[MỞ RỘNG JLPT]`), trạng thái FSRS, `formation_formula` và `core_meaning_vi`.
   - Chi tiết Bài học 3 chiều trình bày tuần tự:
     - `[1] Công thức chia thể & Bảng kết hợp` (`formation_formula`, `formation_table`)
     - `[2] Bản chất ngữ nghĩa & Ngữ dụng` (`deep_explanation_vi`, `register_tag`)
     - `[3] Cặp dễ nhầm cho người Việt` (`confusable_pairs`: mẫu đối chiếu, ranh giới khác biệt, mẹo kiểm tra nhanh)
     - `[4] Ví dụ giáo trình` (`examples`)
     - `[5] Câu hỏi đề thi liên kết` (`linked_questions`) kèm nút `Giải câu hỏi này` (mở đúng `question_id` trong `study`) và `Luyện Phản xạ Mẫu này` (chuyển sang phân khu Luyện Ngữ pháp cho `grammar_code`).

---

## 6. Tích hợp Giải phẫu Ngữ pháp & Modal Chi tiết (`#grammar-modal`)

1. **Hiển thị hậu kiểm (Zero-Leakage):**
   - Trên `dashboard`: Card `Nền tảng Ngữ pháp & Lộ trình JLPT` dùng dữ liệu `grammar_summary` (số mẫu ngữ pháp bộ đề `.xlsx`, phân bố `N5`–`N2`, 2 CTA chuyển nhanh sang Thư viện hoặc Luyện Ngữ pháp). Không dùng `.score-big` để bảo toàn ngữ nghĩa 2 thẻ điểm `/10.00`.
   - Trong `study`: Khối `Giải phẫu Ngữ pháp & Liên kết Bài học` (`structure_parse_vi`, `pedagogical_takeaway_vi`, `option_grammar_notes` và các chip `grammar_points`) CHỈ được render bên trong `feedbackHtml` sau khi nộp bài.
   - Trong `exam`: Chỉ hiển thị giải phẫu ngữ pháp trong bảng kết quả sau khi đã nộp toàn bộ bài thi; phòng thi đang làm khóa 100% gợi ý và không thêm thẻ `.card` vào lưới câu hỏi `#exam-root > .stack-md`.
   - Trong `notebook`: Hiển thị tóm tắt `grammar_breakdown` và các chip mở bài học ngay trong hàng đợi lỗ hổng.
2. **Modal Bài học Ngữ pháp Chi tiết (`#grammar-modal`):**
   - Dùng `role="dialog"`, `aria-modal="true"`, `aria-labelledby="grammar-modal-title"`, focus-trap vòng lặp `Tab`/`Shift+Tab`, đóng bằng phím `Esc` hoặc click nền ngoài, và trả lại focus về nút chip đã mở.
   - Việc mở và đóng `#grammar-modal` không làm reset câu hỏi hay tiến độ đang mở bên dưới ở `study`, `exam` (sau nộp), hoặc `notebook`.
   - Mọi phần tử trong modal tuân thủ `min-w-0`, `overflow-wrap: anywhere` và cuộn dọc an toàn (`max-height: 85vh`) trên Mobile `390x844`.

---

## 7. Tinh gọn UX & Ngôn ngữ Người học Thân thiện (Progressive Disclosure)

1. **Điều hướng chính 5 mục theo lộ trình học tự nhiên:**
   - `Trang chủ` (`#view-dashboard`) -> `Ngữ pháp & Từ vựng` (`#view-grammar`) -> `Làm câu hỏi` (`#view-study`) -> `Thi thử` (`#view-exam`) -> `Câu sai & Nạp đề` (`#view-notebook`), kèm nút `Hướng dẫn` (`#btn-help-modal`) và `Giao diện Sáng / Giao diện Tối` (`#btn-theme-toggle`).
2. **Khối Bắt đầu nhanh & Lưới 12 Chủ đề Học tập:**
   - Đầu `Trang chủ` có khối `#quick-guide-card` (3 bước ngắn gọn + nút thu gọn/mở lại lưu qua `localStorage`) để người mới biết ngay phải bấm đâu.
   - Chuyển danh sách 12 chủ đề từ bảng 7 cột sang **Lưới 12 Chủ đề (`.topic-grid`: 3 cột Desktop, 2 cột Tablet, 1 cột Mobile `390x844`)**, mỗi thẻ giữ sẵn thanh tiến độ và 2 thao tác `Ôn nền N4` / `Làm bài`.
   - Các bảng chi tiết ít dùng (bảng điểm theo từng phần thi và mẫu JSON mở rộng N2/N1) thu gọn trong `<details class="card details-card">`.
3. **Ngôn ngữ Giao diện Thuần Việt Trực quan:**
   - Không hiển thị thuật ngữ kỹ thuật nội bộ trên bề mặt giao diện học (`Zero-Sycophancy`, `Adaptive Pace`, `Horizon cap`, `FSRS R(t)`, `Relearning Queue`, `Lapses`, `Seed`). Thay bằng diễn giải tiếng Việt tự nhiên kèm `.step-hint-bar` hướng dẫn 1 dòng ngay đầu từng dạng câu hỏi và nhãn trạng thái Việt hóa (`Chưa học`, `Đang học`, `Đang ôn định kỳ`, `Hay sai · Cần ôn lại`, `[OK] Đã thuộc vững`).

---

## 8. Hệ thống Ẩn/Hiện Thành phần & Chế độ Tập trung (Focus & Reader Views)

1. **Điều khiển Ẩn/Hiện Từng Thành phần (`#btn-display-prefs` / Phím `V` & `.view-control-bar`):**
   - Mỗi màn hình (`Trang chủ`, `Ngữ pháp & Từ vựng`, `Làm câu hỏi`, `Thi thử`, `Câu sai & Nạp đề`) cung cấp thanh điều khiển gọn `.view-control-bar` (dùng các chip `.vis-chip` / `.mode-seg-btn`) và nút thu gọn từng khối `.section-collapse-btn`, kèm `.hidden-restore-bar` để bật lại nhanh khi có mục đang ẩn.
   - Modal `#display-prefs-modal` (`role="dialog"`, `aria-modal="true"`, switch `role="switch"` `.pref-switch-btn`, nút `#btn-reset-display-prefs`) đồng bộ hai chiều với `localStorage` (`n3_ui_preferences_v1`). Toàn bộ các khối mặc định ở trạng thái hiển thị đầy đủ khi chưa tùy chỉnh; đóng/mở bảng không làm mất tiến độ câu hỏi hoặc bài thi đang làm.
2. **Chế độ Tập trung Toàn màn hình (`#btn-focus-mode` / Phím `F` & `#focus-topbar`):**
   - Khi kích hoạt `html[data-focus-mode="on"]`, thanh đầu trang chính `.app-header` được ẩn và thay bằng thanh điều khiển gọn `#focus-topbar` (nền đặc `--bg-surface`, viền `1px` `--border-subtle`, không dùng hiệu ứng kính mờ) gồm nhãn ngữ cảnh `#focus-context-label`, 4 nút chuyển màn hình nhanh, bộ chỉnh cỡ chữ, nút mở bảng Ẩn/Hiện, nút đổi Sáng/Tối và nút thoát (`F` hoặc `Esc`).
   - Khung nội dung `.app-main` căn giữa ở `max-width: 940px` (mở rộng `1180px` khi `data-focus-wide="1"` cho bố cục đọc hiểu / ngữ pháp 2 cột).
3. **Thang Cỡ chữ Đọc Tiếng Nhật (`data-font-scale`) & Tắt Furigana (`data-hide-ruby`):**
   - Hỗ trợ 4 mức (`sm`, `md`, `lg`, `xl` tương ứng `A-`, `A`, `A+`, `A++`) qua biến CSS `--jp-prompt-size` (`17px`–`25px`), `--jp-passage-size` (`14.5px`–`19.5px`), `--jp-example-size` (`14.5px`–`21px`) và `--jp-vocab-kanji-size` (`18px`–`32px`).
   - Bật `html[data-hide-ruby="1"]` ẩn thẻ `<rt>` phiên âm phụ trợ khi tự kiểm tra đọc chữ Hán ở phần học; tuyệt đối không mở khóa vùng từ khóa kiểm tra `【...】` và không mở gợi ý trong `Thi thử`.
4. **Chế độ Đọc Tập trung & Tự dò Chữ Hán / Nghĩa (Active Recall):**
   - **Ngữ pháp (`Đọc tập trung từng bài`):** Khung đọc sách căn giữa `.grammar-reader-stage` (`78ch`), thanh điều hướng `.reader-nav-bar` (phím `[` / `]`), cho phép bật/tắt 5 chiều bài học và dùng `.self-mask-btn` (nền `--bg-canvas`, viền nét đứt `--border-strong`, không `blur`) để tự che nghĩa tiếng Việt ở ví dụ trước khi bấm xem.
   - **Từ vựng (`Thẻ đọc tập trung` & `Từng từ 1 · Tự dò Kanji`):** Bố cục `.vocab-cards-grid` và `.vocab-deck-stage` (`68ch`) kết hợp che Phiên âm / Nghĩa để luyện nhớ chủ động.
   - **Làm câu hỏi & Đọc hiểu Dokkai:** `.study-focus-stage` (`76ch`) tinh gọn thanh công cụ và nhãn phụ; `.dokkai-split.dokkai-vertical` chuyển bài đọc hiểu sang 1 cột dọc `78ch` dễ theo dõi trên màn hình hẹp; phản hồi sau nộp cho phép ẩn/hiện từng khối mà vẫn bảo đảm Zero-Leakage trước khi nộp.
   - **Thi thử (`Tập trung từng câu`):** Thanh `.exam-control-strip`, bảng chọn câu `.exam-palette` và điều hướng `.exam-single-nav` (tách biệt khỏi `.card` câu hỏi) hiển thị mỗi lần 1 câu thi kèm tùy chọn ẩn `#exam-timer` để giảm áp lực thời gian.
