# JLPT N3 10/10 MASTERY — HƯỚNG DẪN SỬ DỤNG CHƯƠNG TRÌNH

Chương trình ôn thi tiếng Nhật Cuối kì & JLPT (Ngữ pháp N5–N2, Từ vựng/Kanji, Đọc hiểu và bộ đề `.xlsx`).

---

## 1. Khởi chạy nhanh

- **Cách 1 (Nhanh nhất):** Nhấp đúp `start_web.bat` (hoặc `..\CHAY_NHANH_WEB.bat`) để kiểm tra dữ liệu, bật máy chủ Web tại `http://127.0.0.1:8000` và tự động mở trình duyệt.
- **Cách 2 (Mở Menu chọn tác vụ):** Nhấp đúp `run_all.bat` để mở menu số `0–8` bằng tiếng Việt.
- **Cách 3 (Chạy trực tiếp qua PowerShell):**
  - `.\run_all.ps1 -Action web`
  - `.\run_all.ps1 -Action doctor`
  - `.\run_all.ps1 -Action status`
  - `.\run_all.ps1 -Action backup`
  - `.\run_all.ps1 -Action import`
  - `.\run_all.ps1 -Action test`

---

## 2. Hướng dẫn sử dụng 5 mục trên giao diện Web

1. **Trang chủ:**
   - Khối **Bắt đầu nhanh trong 3 bước** giúp bạn đi thẳng tới từng phần học (có nút `Thu gọn` khi đã quen).
   - Theo dõi 2 điểm số trên thang 10: **Điểm Làm Đề Gốc** và **Điểm Hiểu Thật (Không học vẹt)** — chỉ tính thuộc vững khi bạn vượt qua cả câu hỏi đổi dạng và ôn lại ít nhất 2 lần.
   - Nhập **Số ngày đến kỳ thi** và **Phút học mỗi ngày** để biết mỗi ngày cần làm bao nhiêu bài.
   - Chọn trực tiếp từng chủ đề trong lưới **12 Chủ đề Học tập** (`Ôn nền N4` hoặc `Làm bài`).
   - Thanh công cụ đầu trang cho phép ẩn/bật từng khối (`Hướng dẫn`, `Điểm số`, `Ngữ pháp`, `Lịch học`, `12 Chủ đề`, `Bảng chi tiết`) và bấm `Hiện lại tất cả` bất cứ lúc nào.
2. **Ngữ pháp & Từ vựng:**
   - `Tra cứu Ngữ pháp`: Lọc theo Đề cuối kì (`[THI CUỐI KÌ]`), Mở rộng JLPT (`N5`–`N2`), xem công thức, cặp dễ nhầm, ví dụ và bấm nhảy thẳng sang câu hỏi đề thi liên kết. Hỗ trợ chuyển từ `Chia 2 cột` sang `Đọc tập trung từng bài`, bật `Che nghĩa tiếng Việt` ở phần ví dụ và ẩn/bật từng mục `[1]`–`[5]`.
   - `Bài tập Ngữ pháp`: Luyện 3 dạng (`Chia thể`, `Cặp dễ nhầm`, `Dùng trong câu`), xem giải thích chi tiết lý do đúng/sai cho từng phương án 1–4.
   - `Từ vựng & Chữ Hán`: Tra cứu Kanji, Hiragana, Hán-Việt, bộ thủ và cách kết hợp từ dưới 3 chế độ hiển thị: `Bảng tra cứu`, `Thẻ đọc tập trung` và `Từng từ 1 · Tự dò Kanji` (cho phép che phiên âm hoặc nghĩa để tự kiểm tra).
   - `Lộ trình & Mở rộng JLPT`: Xem tiến độ từng cấp độ và nạp thêm gói `.json` hoặc `.xlsx`.
3. **Làm câu hỏi:**
   - Luyện đề gốc hoặc câu hỏi đổi dạng (ghép đủ 4 ô dấu `★`, chọn câu bằng chứng trong bài đọc trước khi trả lời).
   - Có nút `Tập trung câu hỏi` (ẩn thanh chọn và nhãn phụ), chuyển bài Đọc hiểu (Dokkai) giữa `2 cột song song` và `1 cột dọc dễ đọc`, và nút bật/tắt Furigana cho chữ Hán xung quanh.
   - Sau khi nộp bài, đọc phần **Giải phẫu Ngữ pháp & Bài học liên quan** và bấm trực tiếp vào thẻ mẫu để xem bài học (có thể ẩn/hiện từng phần dịch nghĩa, giải thích, giải phẫu).
4. **Thi thử:**
   - Khóa toàn bộ phiên âm phụ và gợi ý, trộn thứ tự đáp án và bấm giờ như phòng thi thật.
   - Hỗ trợ chuyển giữa `Xem toàn bộ đề` và `Tập trung từng câu`, bật/tắt `Hiện đồng hồ` để giảm áp lực thời gian và bật `Bảng chuyển câu` khi cần rà soát nhanh.
5. **Câu sai & Nạp đề:**
   - Tập hợp mọi câu từng trả lời sai để làm lại cho tới khi đúng vững; cho phép tải lên tệp đề `.xlsx` mới và ẩn/bật riêng từng khối trên màn hình.

---

## 3. Chế độ Tập trung & Bảng Ẩn/Hiện Thành phần

- **Nút `Ẩn/Hiện` (phím `V`):** Mở bảng tùy chỉnh để bật/tắt từng khối nội dung trên mỗi màn hình, điều chỉnh cỡ chữ đọc tiếng Nhật (`A-` / `A` / `A+` / `A++`), chuyển Sáng/Tối và nhấn `Khôi phục mặc định` khi muốn đặt lại toàn bộ về chuẩn ban đầu.
- **Nút `Tập trung` (phím `F`):** Ẩn thanh điều hướng lớn phía trên, hiện thanh điều khiển gọn để chuyển nhanh giữa `Ngữ pháp`, `Làm câu hỏi`, `Thi thử`, `Trang chủ`, chỉnh cỡ chữ `A-`..`A++` và giữ màn hình sạch sẽ cho việc đọc/làm bài. Nhấn `Esc` (khi không mở hộp thoại) hoặc `F` để thoát về giao diện đầy đủ.

---

## 4. Phím tắt khi học trên Web

- `1` – `4`: Chọn nhanh đáp án trắc nghiệm 1–4.
- `Space`: Nộp đáp án hoặc chuyển sang câu tiếp theo.
- `H`: Xem 1 gợi ý ngữ cảnh (khi câu hỏi đang ở Hỗ trợ Mức 2).
- `V`: Mở bảng `Ẩn/Hiện` thành phần và chỉnh cỡ chữ đọc (`A-` / `A` / `A+` / `A++`).
- `F`: Bật / Tắt Chế độ `Tập trung` toàn màn hình.
- `[` / `]`: Chuyển về bài trước hoặc bài/câu tiếp theo khi đang ở `Đọc tập trung từng bài` (Ngữ pháp), `Từng từ 1 · Tự dò Kanji` (Từ vựng) hoặc `Tập trung từng câu` (Thi thử).
- `T`: Đổi nhanh Giao diện Sáng / Giao diện Tối.
- `Esc`: Đóng hộp thoại đang mở; nếu không có hộp thoại, thoát Chế độ `Tập trung`.

---

## 5. Các lệnh CLI qua Python (`py -3.11 n3_cli.py`)

| Lệnh | Tác dụng |
| :--- | :--- |
| `py -3.11 n3_cli.py` | Hiện bảng hướng dẫn sử dụng nhanh |
| `py -3.11 n3_cli.py quickstart` | Kiểm tra DB, bật Web server và tự mở trình duyệt |
| `py -3.11 n3_cli.py doctor` | Kiểm tra toàn vẹn cơ sở dữ liệu và thư mục đề Excel |
| `py -3.11 n3_cli.py backup` | Tạo bản sao lưu `.db` an toàn trong `data/backups/` |
| `py -3.11 n3_cli.py status` | In điểm số hiện tại và bảng tiến độ 12 chủ đề |
| `py -3.11 n3_cli.py grammar --exam-only` | Xem toàn bộ ngữ pháp xuất hiện trong đề `.xlsx` |
| `py -3.11 n3_cli.py grammar-inspect GP-N3-005` | Xem chi tiết một mẫu ngữ pháp bất kỳ |
| `py -3.11 n3_cli.py import` | Quét và nạp dữ liệu từ `..\exam_downloads` |
