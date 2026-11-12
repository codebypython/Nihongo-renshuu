"""Data importer module: Seeds cards, drill items, and curriculum from CSV/Markdown."""

import csv
from datetime import datetime, timezone
import json
from pathlib import Path
import re
from typing import Dict, List, Optional, Tuple

from jlpt_study_system.config import SPRINT_REFERENCE_DIR
from jlpt_study_system.database import get_db, init_db
from jlpt_study_system.models import CardCategory, DrillType


# Built-in structured items for Choukai Mondai 5 reflex drills
BUILTIN_CHOUKAI_DRILLS = [
    {
        "prompt": "A: すみません、この資料のコピー、手伝っていただけないでしょうか。",
        "context": "Nhóm 1: Lời yêu cầu & nhờ vả",
        "options": [
            "ええ、喜んで。すぐやりますね。",
            "いいえ、手伝ってください。",
            "どういたしまして、どうぞ。",
        ],
        "correct_index": 0,
        "trap_analysis": "ĐÁP ÁN ĐỒNG Ý CHUẨN: 'ええ、喜んで' hoặc 'いいですよ'. BẪY: Lựa chọn 2 dùng '手伝ってください' (bắt người khác giúp) là ngược hướng hành động.",
    },
    {
        "prompt": "A: 今日の会議の資料、まだ準備できてないなら、手伝おうか。",
        "context": "Nhóm 1: Đề nghị giúp đỡ",
        "options": [
            "えっ、手伝ってあげるんですか。",
            "すみません、助かります。お願いできますか。",
            "はい、手伝ってもいいですよ。",
        ],
        "correct_index": 1,
        "trap_analysis": "KHI ĐƯỢC ĐỀ NGHỊ GIÚP ĐỠ: Đáp lại bằng sự biết ơn '助かります / お願いできますか'. Lựa chọn 1 và 3 dùng ngữ điệu ban ơn là sai vị thế.",
    },
    {
        "prompt": "A: 部長、体調がすぐれないので、本日早退させていただけないでしょうか。",
        "context": "Nhóm 2: Xin phép bản thân được làm gì",
        "options": [
            "ええ、早く帰って休んでください。",
            "はい、早退させますよ。",
            "いえ、早退してはいけませんでした。",
        ],
        "correct_index": 0,
        "trap_analysis": "BẪY XIN PHÉP: '〜させていただけないでしょうか' là 'Tôi xin phép làm'. Người nghe (Sếp) đồng ý cho về: 'ええ、早く帰って休んでください'.",
    },
    {
        "prompt": "A: このペン、ちょっと使わせてもらってもいいですか。",
        "context": "Nhóm 2: Xin phép mượn đồ",
        "options": [
            "ええ、どうぞ使ってください。",
            "いいえ、使わせてください。",
            "はい、使ってもかまいませんでした。",
        ],
        "correct_index": 0,
        "trap_analysis": "XIN PHÉP BẢN THÂN DÙNG: Đáp án chuẩn 'ええ、どうぞ'. Tránh nhầm với cấu trúc bắt đối phương làm.",
    },
    {
        "prompt": "A: 日本語の発音、ずいぶん自然でお上手ですね。",
        "context": "Nhóm 3: Khen ngợi & đáp lại lời khen",
        "options": [
            "はい、私の発音は完璧ですよ。",
            "いいえ、まだまだです。もっと練習しないと。",
            "ええ、上手になりましたね。",
        ],
        "correct_index": 1,
        "trap_analysis": "VĂN HÓA KHIÊM TỐN: Khi người Nhật khen, đáp lại bằng 'いいえ、まだまだです / そんなことありません'. Tuyệt đối không tự nhận 'はい、上手です'.",
    },
    {
        "prompt": "A: 今回のプレゼンテーション、論理的で素晴らしかったですよ。",
        "context": "Nhóm 3: Khen ngợi thuyết trình",
        "options": [
            "そう言っていただけると励みになります。ありがとうございます。",
            "当然ですよ、一生懸命準備しましたから。",
            "いいえ、素晴らしかったです。",
        ],
        "correct_index": 0,
        "trap_analysis": "KHIÊM TỐN TIẾP NHẬN: 'そう言っていただけると励みになります' (Được khen vậy tôi rất có động lực). Không được tỏ thái độ tự phụ.",
    },
    {
        "prompt": "A: 仕事が終わったら、駅前の新しい居酒屋に行ってみない？",
        "context": "Nhóm 4: Lời mời & rủ rê",
        "options": [
            "いいですね、ぜひ行きましょう！",
            "ええ、行かせていただきます。",
            "いいえ、行かないでください。",
        ],
        "correct_index": 0,
        "trap_analysis": "ĐỒNG Ý LỜI MỜI THÂN MẬT: 'いいですね、ぜひ行きましょう'. Lựa chọn 2 quá khách khí (dùng cho sếp mời trang trọng).",
    },
    {
        "prompt": "A: 今度の土曜日、みんなでバーベキューするんだけど、来られない？",
        "context": "Nhóm 4: Lời mời & Từ chối khéo",
        "options": [
            "あいにく先約がありまして、今回は遠慮しておきます。",
            "行きたくないので、行きません。",
            "ええ、来られませんよ。",
        ],
        "correct_index": 0,
        "trap_analysis": "TỪ CHỐI KHÉO ĐÚNG CHUẨN: 'あいにく先約がありまして...' (Tiếc quá tôi lại có hẹn trước...). Không bao giờ từ chối thẳng thừng sỗ sàng.",
    },
    {
        "prompt": "A: 昨日、急な仕様変更のせいで、夜遅くまで残業させられちゃったよ。",
        "context": "Nhóm 5: Thể sai khiến bị động & Than phiền",
        "options": [
            "それは大変でしたね。お疲れ様でした。",
            "残業させてあげてよかったですね。",
            "ええ、残業させられましたよ。",
        ],
        "correct_index": 0,
        "trap_analysis": "ĐỒNG CẢM VỚI THỂ SAI KHIẾN BỊ ĐỘNG (させられた - bị bắt làm): Đáp lại sự chia sẻ 'それは大変でしたね / お疲れ様でした'.",
    },
    {
        "prompt": "A: 雨で靴も服もびしょ濡れになっちゃったよ...",
        "context": "Nhóm 5: Tình huống gặp nạn",
        "options": [
            "風邪を引かないように、早く着替えたほうがいいよ。",
            "よかったですね、涼しくなりましたね。",
            "雨に降らせてあげましたね。",
        ],
        "correct_index": 0,
        "trap_analysis": "ĐỒNG CẢM & KHUYÊN NHỦ: Đưa ra lời khuyên chăm sóc sức khỏe '風邪を引かないように...'.",
    },
]

# Built-in structured items for Dokkai Decoder drills
BUILTIN_DOKKAI_DRILLS = [
    {
        "prompt": "Đoạn văn có câu: '科学技術の進歩は生活を豊かにしたと言われている。しかし、それによって人間本来のコミュニケーションが希薄になったのではないだろう cả.' -> Luận điểm cốt lõi của tác giả là gì?",
        "context": "Bước 3: Bộ lọc từ nối lập luận (しかし / だが)",
        "options": [
            "Khoa học kỹ thuật làm cho đời sống con người trở nên giàu có, tiện nghi hoàn hảo.",
            "Tác giả lo ngại tiến bộ khoa học kỹ thuật làm xói mòn, suy giảm giao tiếp nguyên bản giữa con người.",
            "Giao tiếp giữa con người từ xưa đến nay chưa bao giờ bị ảnh hưởng bởi công nghệ.",
            "Con người cần từ bỏ hoàn toàn các thiết bị công nghệ hiện đại.",
        ],
        "correct_index": 1,
        "trap_analysis": "QUY TẮC VÀNG TỪ NỐI 'しかし': Ý trước 'しかし' chỉ là định kiến số đông/nền tảng. Luận điểm thực sự của tác giả nằm NGAY SAU 'しかし' kèm đuôi khẳng định '〜のではないだろうか'.",
    },
    {
        "prompt": "Trong bài đọc xuất hiện 4 phương án. Phương án nào vi phạm bẫy 'Tuyệt đối hóa' (Extreme Words Trap) cần LOẠI TRỪ NGAY LẬP TỨC?",
        "context": "Bước 4: Kỹ thuật loại trừ bẫy trắc nghiệm",
        "options": [
            "環境問題を解決するためには、個人の意識改革も重要な要素の一つである。",
            "この方法を実践すれば、どのような初心者であっても絶対に失敗することはない。",
            "若者の読書離れには、スマートフォンの普及が少なからず関係していると思われる。",
            "地域住民の協力が得られなければ、計画の遂行は困難になる可能性がある。",
        ],
        "correct_index": 1,
        "trap_analysis": "BẪY TUYỆT ĐỐI HÓA (Extreme Words Trap): Lựa chọn chứa '絶対に〜ない' (tuyệt đối không bao giờ) trong 95% trường hợp là ĐÁP ÁN SAI. Văn phong nghị luận Nhật luôn chừng mực, dè dặt.",
    },
    {
        "prompt": "Câu hỏi yêu cầu: '筆者が最も言いたいことは何ですか'. Khi quét bài đọc, vị trí và từ nối nào báo hiệu đáp án chính xác nhất?",
        "context": "Bước 2 & 3: Quét từ nối chốt luận điểm",
        "options": [
            "Câu đầu tiên của bài đọc, trước các ví dụ cụ thể.",
            "Các câu liệt kê dữ liệu thống kê ở đoạn 2.",
            "Đoạn văn cuối cùng, đặc biệt là sau từ nối 'つまり' hoặc '要するに'.",
            "Đoạn giải thích chi tiết lý do lịch sử.",
        ],
        "correct_index": 2,
        "trap_analysis": "TÍN HIỆU TỔNG KẾT: 'つまり / 要するに' (Tóm lại, nói cách khác) là tín hiệu đóng đinh kết luận của tác giả, thường tập trung ở đoạn cuối cùng của văn bản.",
    },
    {
        "prompt": "Quy tắc vàng khi làm bài Tìm kiếm thông tin (情報検索 - Mondai cuối cùng 2 câu hỏi) để không bị bẫy ngoại lệ là gì?",
        "context": "Chiến thuật ăn trọn điểm Tìm kiếm thông tin",
        "options": [
            "Đọc kỹ toàn bộ các điều khoản dài dòng từ dòng 1 đến dòng cuối.",
            "Lập checklist điều kiện đối tượng, sau đó nhìn ngay vào các dòng chú thích nhỏ có dấu hoa thị (* hoặc ※) ở chân trang.",
            "Chọn đáp án có chi phí đắt nhất vì dịch vụ tốt nhất.",
            "Không cần đọc câu hỏi, chỉ cần so sánh độ dài 4 phương án.",
        ],
        "correct_index": 1,
        "trap_analysis": "BẪY DẤU HOA THỊ (* hoặc ※): Trong bài thông tin biểu mẫu, đáp án và bẫy ngoại lệ (miễn phí, giảm giá, hạn đăng ký, đối tượng loại trừ) LUÔN nằm ở các dòng chú thích hoa thị nhỏ dưới chân bảng.",
    },
    {
        "prompt": "Đề bài có câu gạch chân: '<u>その計画には慎重な検討が求められている</u>'. Hỏi: 'なぜですか (Tại sao lại như vậy?)'. Đâu là vùng định vị đáp án tối ưu?",
        "context": "Bước 2: Định vị vùng chứa đáp án (Zone Localization)",
        "options": [
            "Đọc lại từ dòng đầu tiên của bài đọc.",
            "Tìm kiếm trong phạm vi đúng 1 câu ngay trước hoặc 1 câu ngay sau đường gạch chân, tập trung từ khóa 'から / ので / ため'.",
            "Đáp án chắc chắn nằm ở trang kế tiếp.",
            "Bỏ qua câu gạch chân và đọc phần kết bài.",
        ],
        "correct_index": 1,
        "trap_analysis": "NGUYÊN TẮC CÂU GẠCH CHÂN: Đối với câu hỏi 'Tại sao / Ý là gì' của câu gạch chân, đáp án nằm ngay trong bán kính 1 câu trước hoặc sau nó, nhận diện qua từ chỉ nguyên nhân 'から / ので / ため'.",
    },
]

# Built-in 7-day playbook schedule
BUILTIN_PLAYBOOK_SCHEDULE = [
    # Day 1
    (1, "morning", "Công phá Ngữ pháp hạt nhân (Phần 1 - Trợ từ phức)", 240, "Import dữ liệu, học 20 mẫu đầu tiên: に対して, にとって, に関して, によって..."),
    (1, "afternoon", "Đột phá Đọc quét Dokkai & Tìm kiếm thông tin", 210, "Áp dụng thuật toán quét chú thích hoa thị (*), làm 3 bài Tìm kiếm thông tin."),
    (1, "evening", "Anki Từ nối lập luận & Choukai Mondai 5 phản xạ", 300, "150 lượt thẻ Từ nối, luyện 20 mẫu phản xạ đối đáp ngắn Mondai 5."),
    
    # Day 2
    (2, "morning", "Hoàn tất Ngữ pháp Tier 1 (Họ わけ, こと, もの, Thể sai khiến bị động)", 240, "20 mẫu còn lại, bẻ khóa bẫy わけではない vs わけがない."),
    (2, "afternoon", "Nạp 120 Từ nối lập luận & Đoản văn N3", 210, "Thực hành kỹ thuật đọc câu hỏi trước - khoanh vùng từ nối trên 4 bài đoản văn."),
    (2, "evening", "Review 250 Flashcard tích lũy & Choukai tốc độ cao", 300, "Nghe 30 câu Mondai 5 tức thì (chọn đáp án trong 2 giây)."),
    
    # Day 3
    (3, "morning", "Đột phá Đoản văn N3 (Timebox 3 phút/bài)", 240, "Bấm giờ làm 8 bài Đoản văn, giải phẫu bẫy tuyệt đối hóa và ngoài bài."),
    (3, "afternoon", "Luyện 4 bài Tìm kiếm thông tin & 50 Kanji biển báo", 210, "Mục tiêu đúng 100% phần Thông tin quảng cáo biểu mẫu."),
    (3, "evening", "Nghe Mondai 1 (Bắt từ khóa 'まず' & từ bẫy 'その前に')", 300, "Luyện 10 bài Mondai 1 Hiểu nhiệm vụ, triệt tiêu bẫy đổi ý."),
    
    # Day 4
    (4, "morning", "Thành trì Nghe hiểu Mondai 5 (Tốc độ 1.1x)", 240, "Nghe 40 câu Mondai 5 liên tục, phản xạ tự động với kính ngữ & từ chối khéo."),
    (4, "afternoon", "Giải mã Mondai 2 (Đọc trước 4 đáp án trong 20s)", 210, "Kỹ thuật nhìn lướt 4 động từ cuối của từng phương án trên giấy."),
    (4, "evening", "Full Test Nghe hiểu 40 phút mô phỏng phòng thi", 300, "Chấm điểm bám sàn 30/60 điểm, triệt tiêu nguy cơ liệt."),
    
    # Day 5
    (5, "morning", "Đọc Trung văn & 30 Động từ phức cốt lõi N3", 240, "Nạp động từ phức: 引き受ける, 思いつく... Áp dụng 1 câu hỏi/1-2 đoạn văn."),
    (5, "afternoon", "Bấm giờ thi trọn gói Phần 2 (Ngữ pháp + Đọc hiểu 70 phút)", 210, "Cắt đúng 20 phút Ngữ pháp, 50 phút Đọc hiểu. Đo lường rủi ro cháy giờ."),
    (5, "evening", "Giải phẫu chi tiết đề thi & Cập nhật Sổ tay bẫy trắc nghiệm", 300, "Phân tích nguyên nhân sai lầm, ôn lướt 300 thẻ Anki."),
    
    # Day 6
    (6, "morning", "Mock Test 1: Mô phỏng phòng thi 100% (3 phần thi chuẩn giờ)", 240, "Phần 1 (30p), Phần 2 (70p), Phần 3 (40p) đúng kỷ luật phòng thi."),
    (6, "afternoon", "Giải phẫu toàn bộ Mock Test 1 (Chẩn đoán điểm yếu)", 210, "Xác định rõ lỗ hổng: Ngữ pháp hay nhầm, hay bẫy đọc hiểu ngoài bài."),
    (6, "evening", "Vá lỗ hổng khẩn cấp & Luyện tập có chủ đích các điểm liệt", 300, "Tái kiểm tra các mục trong Sổ tay bẫy trắc nghiệm."),
    
    # Day 7
    (7, "morning", "Mini-Mock Test tinh gọn & Duyệt toàn bộ 40 Ngữ pháp Tier 1", 240, "20 câu ngữ pháp trọng điểm, 2 bài đọc ngắn củng cố tự tin."),
    (7, "afternoon", "Nghe lại toàn bộ câu Mondai 5 từng sai & Rà soát quy tắc Dokkai", 210, "Bảo đảm phản xạ 100% trong 2 giây."),
    (7, "evening", "Thiết lập tâm lý phòng thi & Nghỉ ngơi toàn diện", 180, "DỪNG HỌC LÚC 21:00. Chuẩn bị bút chì 2B, CCCD, ngủ trước 22:30."),
]


def import_grammar_csv(db_path=None, csv_path: Optional[Path] = None) -> int:
    """Import grammar cards from anki_grammar_tier1.csv."""
    target_csv = csv_path or (SPRINT_REFERENCE_DIR / "anki_grammar_tier1.csv")
    if not Path(target_csv).exists():
        return 0

    imported_count = 0
    now_iso = datetime.now(timezone.utc).isoformat()

    with open(target_csv, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            return 0

        with get_db(db_path) as conn:
            for row in reader:
                if len(row) < 2:
                    continue
                front = row[0].strip()
                back = row[1].strip()
                trap = row[2].strip() if len(row) > 2 else ""
                example = row[3].strip() if len(row) > 3 else ""

                if not front:
                    continue

                cursor = conn.execute(
                    """
                    INSERT INTO cards (category, front, back, trap, example, tags, created_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(category, front) DO UPDATE SET
                        back = excluded.back,
                        trap = excluded.trap,
                        example = excluded.example
                    RETURNING id
                    """,
                    (CardCategory.GRAMMAR.value, front, back, trap, example, "grammar,tier1,n3_sprint", now_iso),
                )
                row_res = cursor.fetchone()
                if row_res:
                    card_id = row_res["id"]
                    # Ensure FSRS state exists
                    conn.execute(
                        """
                        INSERT OR IGNORE INTO fsrs_states (card_id, stability, difficulty, reps, lapses, state, due_date, scheduled_days)
                        VALUES (?, 2.0, 5.0, 0, 0, 'New', ?, 0)
                        """,
                        (card_id, now_iso),
                    )
                    imported_count += 1

    return imported_count


def import_vocab_csv(db_path=None, csv_path: Optional[Path] = None) -> int:
    """Import vocabulary & discourse marker cards from anki_vocab_discourse.csv."""
    target_csv = csv_path or (SPRINT_REFERENCE_DIR / "anki_vocab_discourse.csv")
    if not Path(target_csv).exists():
        return 0

    imported_count = 0
    now_iso = datetime.now(timezone.utc).isoformat()

    with open(target_csv, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            return 0

        with get_db(db_path) as conn:
            for row in reader:
                if len(row) < 3:
                    continue
                front = row[0].strip()
                furigana_type = row[1].strip()
                meaning_signal = row[2].strip()
                context_signal = row[3].strip() if len(row) > 3 else ""

                if not front:
                    continue

                back = f"{meaning_signal}\n[{furigana_type}]"
                trap = context_signal

                cursor = conn.execute(
                    """
                    INSERT INTO cards (category, front, back, trap, example, tags, created_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(category, front) DO UPDATE SET
                        back = excluded.back,
                        trap = excluded.trap
                    RETURNING id
                    """,
                    (CardCategory.VOCAB.value, front, back, trap, "", "vocab,discourse,n3_sprint", now_iso),
                )
                row_res = cursor.fetchone()
                if row_res:
                    card_id = row_res["id"]
                    conn.execute(
                        """
                        INSERT OR IGNORE INTO fsrs_states (card_id, stability, difficulty, reps, lapses, state, due_date, scheduled_days)
                        VALUES (?, 2.0, 5.0, 0, 0, 'New', ?, 0)
                        """,
                        (card_id, now_iso),
                    )
                    imported_count += 1

    return imported_count


def parse_playbook_markdown(md_path: Path) -> List[Tuple[int, str, str, int, str]]:
    """Parse 7-day schedule blocks dynamically from DAY_BY_DAY_PLAYBOOK.md."""
    if not md_path.exists():
        return BUILTIN_PLAYBOOK_SCHEDULE

    try:
        content = md_path.read_text(encoding="utf-8")
        day_sections = re.split(r"###\s+NGÀY\s+(\d+)[:\s]+([^\n\r]+)", content)
        if len(day_sections) < 3:
            return BUILTIN_PLAYBOOK_SCHEDULE

        blocks = []
        for i in range(1, len(day_sections), 3):
            day_num = int(day_sections[i])
            day_title = day_sections[i + 1].strip()
            day_body = day_sections[i + 2]

            if day_num == 6:
                # Day 6 is a full simulated mock test day; aggregate into canonical 3 blocks
                blocks.append((
                    6,
                    "morning",
                    "Mock Test 1: Mô phỏng phòng thi 100% (3 phần thi chuẩn giờ)",
                    240,
                    "Phần 1 Từ vựng (30p), Phần 2 Ngữ pháp + Đọc hiểu (70p), Phần 3 Nghe hiểu (40p) đúng kỷ luật phòng thi.",
                ))
                blocks.append((
                    6,
                    "afternoon",
                    "Giải phẫu toàn bộ Mock Test 1 (Chẩn đoán điểm yếu)",
                    210,
                    "Xác định rõ lỗ hổng: Ngữ pháp hay nhầm, hay bẫy đọc hiểu ngoài bài.",
                ))
                blocks.append((
                    6,
                    "evening",
                    "Vá lỗ hổng khẩn cấp & Luyện tập có chủ đích các điểm liệt",
                    300,
                    "Tái kiểm tra các mục trong Sổ tay bẫy trắc nghiệm, ôn lướt 300 thẻ Anki.",
                ))
                continue

            block_matches = list(re.finditer(
                r"-\s+\*\*([^\*]+)\*\*:?\s*([^\n\r]*)((?:\n\s+-\s+[^\n\r]+)*)",
                day_body
            ))

            for bm in block_matches:
                b_hdr = bm.group(1).strip()
                b_inline = bm.group(2).strip()
                b_bullets = [b.strip("- \t") for b in bm.group(3).splitlines() if b.strip()]
                b_notes = " ".join(b_bullets) if b_bullets else b_inline

                if "Sáng" in b_hdr or "08:30" in b_hdr or "09:00" in b_hdr:
                    b_name = "morning"
                    minutes = 240
                    title = b_inline or f"{day_title} (Sáng)"
                elif "Chiều" in b_hdr or "13:00" in b_hdr:
                    b_name = "afternoon"
                    minutes = 210
                    title = b_inline or f"{day_title} (Chiều)"
                elif "Tối" in b_hdr or "17:30" in b_hdr or "Chiều & Tối" in b_hdr:
                    b_name = "evening"
                    minutes = 180 if day_num == 7 else 300
                    title = b_inline or f"{day_title} (Tối)"
                else:
                    b_name = "focus_block"
                    minutes = 50
                    title = b_inline or b_hdr

                blocks.append((day_num, b_name, title, minutes, b_notes))

        if len(blocks) < 14:
            return BUILTIN_PLAYBOOK_SCHEDULE

        return blocks
    except Exception:
        return BUILTIN_PLAYBOOK_SCHEDULE


def seed_drill_items(db_path=None, sprint_dir: Optional[Path] = None) -> Tuple[int, int]:
    """Seed structured Choukai and Dokkai drill items into database."""
    choukai_count = 0
    dokkai_count = 0

    with get_db(db_path) as conn:
        # Choukai drills
        for item in BUILTIN_CHOUKAI_DRILLS:
            cursor = conn.execute(
                """
                INSERT INTO drill_items (drill_type, section, prompt, context, options_json, correct_index, trap_analysis)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(drill_type, prompt) DO UPDATE SET
                    options_json = excluded.options_json,
                    correct_index = excluded.correct_index,
                    trap_analysis = excluded.trap_analysis
                """,
                (
                    DrillType.CHOUKAI_REFLEX.value,
                    "Listening",
                    item["prompt"],
                    item["context"],
                    json.dumps(item["options"], ensure_ascii=False),
                    item["correct_index"],
                    item["trap_analysis"],
                ),
            )
            choukai_count += 1

        # Dokkai drills
        for item in BUILTIN_DOKKAI_DRILLS:
            cursor = conn.execute(
                """
                INSERT INTO drill_items (drill_type, section, prompt, context, options_json, correct_index, trap_analysis)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(drill_type, prompt) DO UPDATE SET
                    options_json = excluded.options_json,
                    correct_index = excluded.correct_index,
                    trap_analysis = excluded.trap_analysis
                """,
                (
                    DrillType.DOKKAI_DECODER.value,
                    "Reading",
                    item["prompt"],
                    item["context"],
                    json.dumps(item["options"], ensure_ascii=False),
                    item["correct_index"],
                    item["trap_analysis"],
                ),
            )
            dokkai_count += 1

    return choukai_count, dokkai_count


def seed_curriculum_playbook(db_path=None, sprint_dir: Optional[Path] = None) -> int:
    """Seed 7-day playbook curriculum blocks, loading from markdown if available."""
    s_dir = Path(sprint_dir) if sprint_dir else SPRINT_REFERENCE_DIR
    md_file = s_dir / "DAY_BY_DAY_PLAYBOOK.md"
    schedule_data = parse_playbook_markdown(md_file) if md_file.exists() else BUILTIN_PLAYBOOK_SCHEDULE

    seeded = 0
    with get_db(db_path) as conn:
        for day, block, title, minutes, notes in schedule_data:
            conn.execute(
                """
                INSERT INTO curriculum_blocks (day_number, block_name, title, planned_minutes, notes)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(day_number, block_name, title) DO UPDATE SET
                    planned_minutes = excluded.planned_minutes,
                    notes = excluded.notes
                """,
                (day, block, title, minutes, notes),
            )
            seeded += 1
    return seeded


def import_all(db_path=None, sprint_dir: Optional[Path] = None) -> Dict[str, int]:
    """Execute complete initial database setup and data seeding."""
    init_db(db_path)
    s_dir = Path(sprint_dir) if sprint_dir else SPRINT_REFERENCE_DIR

    grammar_count = import_grammar_csv(db_path, s_dir / "anki_grammar_tier1.csv")
    vocab_count = import_vocab_csv(db_path, s_dir / "anki_vocab_discourse.csv")
    choukai_drills, dokkai_drills = seed_drill_items(db_path, s_dir)
    curriculum_blocks = seed_curriculum_playbook(db_path, s_dir)

    return {
        "grammar_cards": grammar_count,
        "vocab_cards": vocab_count,
        "choukai_drills": choukai_drills,
        "dokkai_drills": dokkai_drills,
        "curriculum_blocks": curriculum_blocks,
    }
