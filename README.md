# Nihongo Renshuu

Hai công cụ học JLPT N3 bằng tiếng Việt chạy cục bộ trong trình duyệt.

| Công cụ | Nội dung | Địa chỉ mặc định |
| --- | --- | --- |
| **JLPT N3 Sprint** | Thẻ FSRS, lộ trình 7 ngày, Pomodoro, luyện đọc và nghe | http://127.0.0.1:8000 |
| **N3 Mastery 10/10** | 163 câu gốc từ 7 bộ đề, bài luyện biến thể, 12 trạm bắc cầu và thi thử | http://127.0.0.1:8010 |

## Chạy từ mã nguồn

Yêu cầu Python 3.11 trở lên. Ví dụ dưới đây dùng PowerShell tại thư mục gốc.

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe jlpt_study_system/jlpt_cli.py serve
```

Để mở Mastery, chạy lệnh sau trong cửa sổ PowerShell khác.

```powershell
.\.venv\Scripts\python.exe n3_ten_point_mastery/n3_cli.py serve
```

Mỗi ứng dụng tự tạo cơ sở dữ liệu SQLite và nạp học liệu trong lần mở đầu tiên.
Tiến độ và cài đặt được lưu trong thư mục `data` tương ứng của từng ứng dụng.

## Tạo bản ZIP chạy ngoại tuyến

Từ bản clone trên Windows 64-bit có Git và Python 3.11 trở lên, chạy lệnh sau.

```powershell
py -3.11 packaging/windows/build.py
```

Công cụ lấy mã nguồn và học liệu từ commit hiện tại, rồi thêm Python nhúng,
thư viện và cơ sở dữ liệu khởi tạo. Tệp kết quả nằm trong `dist/`.
Người nhận chỉ cần giải nén và mở một trong hai tệp `Mo … .cmd`.

## Kiểm thử

Kiểm thử trình duyệt của Mastery dùng Google Chrome. Chạy hai bộ kiểm thử
trong thư mục của từng ứng dụng để Pytest nạp đúng các module cùng tên.

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
$python = (Resolve-Path .\.venv\Scripts\python.exe).Path
Push-Location jlpt_study_system
& $python -m pytest tests -q
Pop-Location
Push-Location n3_ten_point_mastery
& $python -m pytest tests -q
Pop-Location
```

- [Hướng dẫn Sprint](jlpt_study_system/README.md)
- [Thiết kế Mastery](docs/mastery-blueprint.md)
- [Lộ trình 7 ngày và thẻ Anki](jlpt_n3_sprint/)
- [Bộ đề Excel](exam_downloads/)
