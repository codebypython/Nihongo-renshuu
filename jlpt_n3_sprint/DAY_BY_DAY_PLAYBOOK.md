# SỔ TAY TÁC CHIẾN 7 NGÀY (DAY-BY-DAY PLAYBOOK)
<!-- Lộ trình 12 giờ/ngày: Thực thi từ nền N5 đến mốc an toàn JLPT N3 -->

---

## 1. HƯỚNG DẪN IMPORT VÀ CẤU HÌNH ANKI NGAY LẬP TỨC (10 PHÚT)

1. Mở phần mềm **Anki** trên máy tính (hoặc điện thoại).
2. Vào **File -> Import**:
   - Chọn tệp: `d:\Development\jlpt_n3_sprint\anki_grammar_tier1.csv`
     - Field 1: Front (Pattern)
     - Field 2: Back (Meaning & Formation)
     - Field 3: Back (Trap & Bẫy trắc nghiệm)
     - Field 4: Back (Example)
   - Chọn tệp: `d:\Development\jlpt_n3_sprint\anki_vocab_discourse.csv`
     - Field 1: Front (Word / Kanji)
     - Field 2: Back (Type / Furigana)
     - Field 3: Back (Meaning & Core Signal)
     - Field 4: Back (Context & Test Signal)
3. Cấu hình Deck Options (Bắt buộc cho Sprint 7 ngày):
   - **New cards/day**: Đặt là `50` (hoặc `Unlimited`).
   - **Maximum reviews/day**: Đặt là `9999`.
   - **FSRS Settings**: Bật FSRS, đặt `Desired Retention` = `0.75` - `0.80` để giảm số lượt lặp lại thẻ cũ, dồn sức nạp thẻ mới.

---

## 2. LỊCH TRÌNH CHI TIẾT TỪ NGÀY 1 ĐẾN NGÀY 7

```text
[TỔNG QUAN 7 NGÀY TÁC CHIẾN]
Ngày 1: Thiết lập hạ tầng + Bẻ khóa 20 Ngữ pháp Tier 1 + Làm quen nhịp đọc quét.
Ngày 2: Hoàn tất 20 Ngữ pháp Tier 1 còn lại + Cày nát 120 Từ nối lập luận.
Ngày 3: Thực chiến Đọc hiểu Dokkai (Đoản văn + Tìm kiếm thông tin).
Ngày 4: Xây dựng thành trì Nghe hiểu (Mondai 5 Phản xạ nhanh + Mondai 1).
Ngày 5: Đọc hiểu Trung văn + Động từ phức N3 + Nghe Mondai 2.
Ngày 6: Thi thử Mock Test 1 (Bấm giờ chuẩn 100%) + Sửa lỗi sai lập tức (Error Logging).
Ngày 7: Thi thử Mock Test 2 + Ôn lướt toàn bộ Flashcard + Thiết lập tâm lý phòng thi.
```

---

### NGÀY 1: CÔNG PHÁ NGỮ PHÁP HẠT NHÂN (PHẦN 1)
- **Sáng (07:30 - 11:30)**:
  - Import 2 file CSV vào Anki.
  - Học sâu 20 mẫu ngữ pháp đầu tiên trong `anki_grammar_tier1.csv` (Cụm trợ từ phức: `に対して`, `にとって`, `に関して`, `によって`...).
  - Làm 40 câu trắc nghiệm ngữ pháp ngắn liên quan đến các trợ từ phức này.
- **Chiều (13:00 - 16:30)**:
  - Đọc kỹ tài liệu `DOKKAI_READING_DECODER.md`.
  - Thực hành ngay 3 bài Tìm kiếm thông tin (Mondai cuối của Đọc hiểu) theo thuật toán quét chú thích hoa thị (*).
- **Tối (17:30 - 22:30)**:
  - Chạy 150 lượt thẻ Anki Từ vựng/Từ nối trong `anki_vocab_discourse.csv`.
  - Luyện 20 câu Mondai 5 Nghe hiểu (Choukai) theo bộ mẫu trong `CHOUKAI_LISTENING_SURVIVAL.md`.

---

### NGÀY 2: HOÀN TẤT NGỮ PHÁP TIER 1 & BỘ TỪ NỐI LẬP LUẬN
- **Sáng (07:30 - 11:30)**:
  - Học nốt 20 mẫu ngữ pháp còn lại trong `anki_grammar_tier1.csv` (Họ わけ, Họ こと, Họ もの, Thể sai khiến bị động `させられる`).
  - Dùng LLM kiểm tra lại các cặp hay nhầm: `わけではない` vs `わけがない`.
- **Chiều (13:00 - 16:30)**:
  - Nạp toàn bộ 120 từ nối lập luận trong `anki_vocab_discourse.csv`.
  - In ra giấy 4 bài Đoản văn N3, thực hành kỹ thuật "Đọc câu hỏi trước - Khoanh vùng từ nối".
- **Tối (17:30 - 22:30)**:
  - Review 250 thẻ Anki tích lũy.
  - Nghe 30 câu Mondai 5 phản xạ tức thì (Nghe 1 lần, chọn ngay đáp án trong 2 giây).

---

### NGÀY 3: ĐỘT PHÁ ĐỌC HIỂU ĐOẢN VĂN & TÌM KIẾM THÔNG TIN
- **Sáng (07:30 - 11:30)**:
  - Ôn tập Anki buổi sáng (30 phút).
  - Bấm giờ làm 8 bài Đoản văn N3 (Mỗi bài chuẩn 3 phút).
  - Phân tích đáp án sai: Tại sao sai? Dính bẫy tuyệt đối hóa (`すべて`, `必ず`) hay bẫy thông tin ngoài bài?
- **Chiều (13:00 - 16:30)**:
  - Luyện 4 bài Tìm kiếm thông tin. Mục tiêu: Đạt tỷ lệ đúng 100% (Ăn trọn 2/2 câu mỗi bài).
  - Nhận diện 50 Kanji N3 thường gặp trong các biển báo, thông báo văn phòng.
- **Tối (17:30 - 22:30)**:
  - Nghe luyện Mondai 1 (Hiểu nhiệm vụ - 10 bài). Áp dụng quy tắc bắt từ khóa `まず` và từ bẫy `その前に`.

---

### NGÀY 4: THÀNH TRÌ NGHE HIỂU (BẢO VỆ SÀN 30 ĐIỂM)
- **Sáng (07:30 - 11:30)**:
  - Chạy Anki toàn bộ ngữ pháp Tier 1 và từ nối.
  - Nghe liên tục 40 câu Mondai 5 ở tốc độ 1.1x. Buộc tai phải phản xạ tức thời với các mẫu kính ngữ và từ chối khéo.
- **Chiều (13:00 - 16:30)**:
  - Giải mã Mondai 2 (Hiểu điểm cốt lõi). Rèn luyện kỹ năng đọc trước 4 đáp án trên giấy trong 20 giây mở đầu.
  - Lập bảng danh sách các từ vựng gây nhiễu thường gặp trong bài nghe.
- **Tối (17:30 - 22:30)**:
  - Ghép bài thi: Làm 1 set Nghe hiểu trọn vẹn 40 phút. Bấm giờ thật.
  - Chấm điểm ngay: Nếu đạt >= 25 điểm, bạn đã an toàn vượt qua vùng liệt.

---

### NGÀY 5: ĐỌC TRUNG VĂN & ĐỘNG TỪ PHỨC N3
- **Sáng (07:30 - 11:30)**:
  - Nạp 30 Động từ phức cốt lõi (`引き受ける`, `思いつく`, `見直す`...).
  - Thực hành làm 2 bài Đọc hiểu Trung văn (Mỗi bài có 3 câu hỏi). Áp dụng quy tắc "1 câu hỏi ứng với 1-2 đoạn văn".
- **Chiều (13:00 - 16:30)**:
  - Bấm giờ làm bài thi tổng hợp Phần 2 (Ngữ pháp + Đọc hiểu): Ép thời gian đúng 70 phút (20 phút Ngữ pháp, 50 phút Đọc hiểu).
  - Ghi nhận xem có bị cháy giờ hay không.
- **Tối (17:30 - 22:30)**:
  - Chữa chi tiết đề vừa làm. Cập nhật các câu sai vào tệp Error Log.
  - Ôn lướt 300 thẻ Anki.

---

### NGÀY 6: TỔNG DUYỆT ĐỀ MOCK TEST 1 (MÔ PHỎNG PHÒNG THI 100%)
- **08:30 - 09:00**: Khởi động não, duyệt Anki.
- **09:00 - 09:30**: Bấm giờ thi PHẦN 1: Từ vựng (Gengo Chishiki - Moji/Goi, 30 phút).
- **09:45 - 10:55**: Bấm giờ thi PHẦN 2: Ngữ pháp + Đọc hiểu (70 phút). Cắt đúng 20 phút cho Ngữ pháp!
- **11:15 - 11:55**: Bấm giờ thi PHẦN 3: Nghe hiểu (40 phút).
- **Chiều & Tối**:
  - Dành trọn 6 giờ để GIẢI PHẪU TOÀN BỘ ĐỀ THI.
  - Không quan tâm điểm số được bao nhiêu. Chỉ tập trung vào câu hỏi: "Tại sao câu này sai? Có phải do không nhớ nghĩa ngữ pháp Tier 1, hay do đọc nhầm câu hỏi?".

---

### NGÀY 7: TINH CHỈNH PHẢN XẠ & CỦNG CỐ TÂM LÝ PHÒNG THI
- **Sáng (07:30 - 11:30)**:
  - Làm 1 đề rút gọn (Mini-Mock Test) gồm 20 câu ngữ pháp trọng điểm và 2 bài đọc ngắn.
  - Rà soát lại 40 cấu trúc trong `anki_grammar_tier1.csv`.
- **Chiều (13:00 - 16:30)**:
  - Nghe lại toàn bộ các câu Mondai 5 đã làm sai trong 6 ngày qua.
  - Đọc lại toàn bộ quy tắc bẫy trong `DOKKAI_READING_DECODER.md`.
- **Tối (17:30 - 21:00)**:
  - DỪNG TOÀN BỘ VIỆC HỌC MỚI từ 21:00.
  - Chuẩn bị dụng cụ: Bút chì 2B (2-3 chiếc gọt sẵn), tẩy mềm, đồng hồ đeo tay kim (không dùng smartwatch), giấy báo dự thi và CMND/CCCD.
  - Đi ngủ trước 22:30 để bảo đảm não bộ đạt trạng thái tỉnh táo tối đa.
