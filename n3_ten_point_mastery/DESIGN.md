# DESIGN SYSTEM — N3 10/10 MASTERY WORKSPACE

Tài liệu này và [tokens.json](tokens.json) là **Nguồn chân lý duy nhất (Single Source of Truth)** cho toàn bộ giao diện Web SPA của hệ thống `n3_ten_point_mastery`.

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
   - Phím tắt thao tác nhanh: `1`–`4` (chọn đáp án), `Space` (nộp/kiểm tra hoặc câu tiếp theo khi không gõ trong input), `H` (gợi ý Giàn giáo Cấp 2), `T` (đổi Light/Dark), `Esc` (đóng hộp thoại).
