# THUẬT TOÁN GIẢI MÃ ĐỌC HIỂU JLPT N3 (DOKKAI DECODER)
<!-- Phác đồ sinh tồn: Vượt qua bài thi Đọc hiểu trong 50 phút với nền tảng N5 -->

---

## 1. PHÂN BỔ THỜI GIAN CỨNG (HARD TIMEBOXING)
Kỳ thi N3 gom chung Ngữ pháp và Đọc hiểu trong đúng **70 phút**.
- **Phút 00 - 20 (20 phút)**: Hoàn tất toàn bộ phần Ngữ pháp (Mondai 1, 2, 3 của Ngữ pháp). Đúng 20 phút phải lật sang Đọc hiểu ngay lập tức!
- **Phút 20 - 70 (50 phút)**: Dành trọn cho Đọc hiểu theo thứ tự chiến thuật ngược:

```text
[THỨ TỰ LÀM BÀI ĐỌC HIỂU TỐI ƯU HÓA ĐIỂM SỐ]
1. Bài Tìm kiếm thông tin (情報検索 - Mondai cuối, 1 bài, 2 câu hỏi): 8 phút -> DỄ ĂN ĐIỂM NHẤT.
2. Bài Đoản văn (短文 - Mondai 4, 4 bài ngắn, mỗi bài 1 câu hỏi): 12 phút (3 phút/bài).
3. Bài Trung văn (中文 - Mondai 5, 2 bài vừa, mỗi bài 3 câu hỏi): 18 phút (9 phút/bài).
4. Bài Trường văn (長文 - Mondai 6, 1 bài dài, 4 câu hỏi): 12 phút.
```

---

## 2. THUẬT TOÁN 4 BƯỚC ĐỌC QUÉT (SCANNING ALGORITHM)

Tuyệt đối KHÔNG đọc toàn bài từ đầu đến cuối như đọc tiểu thuyết. Người có nền N5 sẽ hết giờ ngay ở bài thứ hai.

### BƯỚC 1: Đọc Câu Hỏi & Từ Khóa Trọng Tâm (Question Priming)
- Đọc lướt câu hỏi trước khi nhìn vào bài đọc.
- Gạch chân 2 loại từ khóa trong câu hỏi:
  - **Từ khóa danh từ thực thể**: Tên người, thời gian, sự kiện, địa điểm.
  - **Từ khóa chỉ loại câu hỏi**:
    - `なぜですか` (Hỏi nguyên nhân -> Đi tìm `から`, `ので`, `ため`).
    - `どういうことですか` (Hỏi bản chất -> Đi tìm câu định nghĩa ngay trước hoặc sau gạch chân).
    - `筆者が最も言いたいことは何ですか` (Hỏi ý tác giả -> Quét cuối bài và từ nối).

### BƯỚC 2: Định Vị Đoạn Văn Chứa Đáp Án (Zone Localization)
- Nguyên tắc cơ bản của đề JLPT: **Thứ tự câu hỏi bám sát thứ tự các đoạn văn trong bài**.
  - Câu hỏi 1 thường nằm ở Đoạn 1 hoặc Đoạn 2.
  - Câu hỏi 2 nằm ở Đoạn 3 hoặc Đoạn 4.
  - Câu hỏi cuối cùng hỏi ý tác giả nằm ở Đoạn cuối cùng.
- Nếu câu hỏi có từ gạch chân `_________`: Đáp án nằm trong phạm vi **1 câu ngay phía trước** hoặc **1 câu ngay phía sau** đường gạch chân đó.

### BƯỚC 3: Kích Hoạt Bộ Lọc Từ Nối Lập Luận (Discourse Marker Scanning)
- Mắt quét nhanh các từ nối mang tính chất bước ngoặt:
  - `しかし`, `だが`, `ところが`, `それに反して`, `実は`: **90% đáp án nằm ở câu sau các từ này**.
  - `つまり`, `要するに`: Tác giả tóm tắt toàn bộ ý nghĩa bài văn tại đây.
  - `〜のではないだろうか`, `〜と思う`, `〜に違いない`: Khẳng định quan điểm tác giả.

### BƯỚC 4: Kỹ Thuật Loại Trừ 3 Bẫy Trắc Nghiệm Kinh Điển
1. **Bẫy Tuyệt Đối Hóa (Extreme Words Trap)**:
   - Các đáp án chứa: `すべて` (tất cả), `絶対に` (tuyệt đối), `必ず` (chắc chắn 100%), `全く〜ない` (hoàn toàn không). Trong 95% trường hợp, đây là **ĐÁP ÁN SAI**. Tác giả văn học/nghị luận Nhật Bản luôn dùng cách nói dè dặt, khách quan.
2. **Bẫy Thông Tin Ngoài Bài (Out-of-Context Trap)**:
   - Một đáp án nghe rất hợp lý và đúng với kiến thức đời sống thực tế, nhưng trong bài KHÔNG HỀ ĐỀ CẬP -> **ĐÁP ÁN SAI**.
3. **Bẫy Đảo Ngược Chủ - Khách (Subject-Object Inversion)**:
   - Đổi chủ ngữ của hành động (A làm cho B bị biến thành B làm cho A). Kiểm tra kỹ trợ từ `が`, `を`, `に`.

---

## 3. CHIẾN THUẬT ĂN TRỌN ĐIỂM BÀI TÌM KIẾM THÔNG TIN (MONDAI CUỐI)
- Đây là phần dễ nhất để lấy trọn 100% điểm vì không yêu cầu đọc hiểu triết lý.
- **Quy trình xử lý**:
  1. Đọc kỹ **Điều kiện của đối tượng** trong câu hỏi (Ví dụ: "Sinh viên đại học, muốn tham gia vào ngày thứ Bảy, có thẻ hội viên, muốn chi phí dưới 3,000 yên").
  2. Lập checklist các điều kiện: [Sinh viên] + [Thứ 7] + [Có thẻ] + [< 3,000 yên].
  3. Nhìn vào bảng biểu quảng cáo: Đọc kỹ phần **chú thích nhỏ có dấu hoa thị (* hoặc ※)** ở góc dưới cùng. **Đáp án luôn nằm ở phần ghi chú ngoại lệ này**.
