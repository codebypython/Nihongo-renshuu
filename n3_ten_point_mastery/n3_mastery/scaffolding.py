"""3-Tier Adaptive Furigana & Hán-Việt Scaffolding Engine with strict 【...】 target masking."""

import html
import re
from typing import Any, Dict, List, Optional, Set, Tuple

from n3_mastery.config import SCAFFOLD_TIER2_STABILITY, SCAFFOLD_TIER3_STABILITY

# Offline N4->N3 background lexicon: word -> (hiragana, han_viet, meaning_vi)
# Used ONLY for surrounding background words outside 【...】 at Tier 1 (or Tier 2 single hint).
BACKGROUND_LEXICON: Dict[str, Tuple[str, str, str]] = {
    "日本": ("にほん", "NHẬT BẢN", "Nhật Bản"),
    "東京": ("とうきょう", "ĐÔNG KINH", "Tokyo"),
    "気温": ("きおん", "KHÍ ÔN", "nhiệt độ không khí"),
    "生活": ("せいかつ", "SINH HOẠT", "cuộc sống, sinh hoạt"),
    "仕事": ("しごと", "SĨ SỰ", "công việc"),
    "会社": ("かいしゃ", "HỘI XÃ", "công ty"),
    "病院": ("びょういん", "BỆNH VIỆN", "bệnh viện"),
    "電話": ("でんわ", "ĐIỆN THOẠI", "điện thoại"),
    "予約": ("よやく", "DỰ ƯỚC", "đặt trước"),
    "先生": ("せんせい", "TIÊN SINH", "thầy/cô giáo"),
    "学生": ("がくせい", "HỌC SINH", "học sinh, sinh viên"),
    "授業": ("じゅぎょう", "THỤ NGHIỆP", "giờ học"),
    "家族": ("かぞく", "GIA TỘC", "gia đình"),
    "両親": ("りょうしん", "LƯỠNG THÂN", "bố mẹ"),
    "友だち": ("ともだち", "HỮU", "bạn bè"),
    "友達": ("ともだち", "HỮU ĐẠT", "bạn bè"),
    "子ども": ("こども", "TỬ", "trẻ em, con"),
    "大人": ("おとな", "ĐẠI NHÂN", "người lớn"),
    "写真": ("しゃしん", "TẢ CHÂN", "ảnh"),
    "旅行": ("りょこう", "LỮ HÀNH", "du lịch"),
    "問題": ("もんだい", "VẤN ĐỀ", "vấn đề, câu hỏi"),
    "試験": ("しけん", "THÍ NGHIỆM", "kỳ thi"),
    "空港": ("くうこう", "KHÔNG CẢNG", "sân bay"),
    "天気": ("てんき", "THIÊN KHÍ", "thời tiết"),
    "地震": ("じしん", "ĐỊA CHẤN", "động đất"),
    "野菜": ("やさい", "DÃ THÁI", "rau củ"),
    "言葉": ("ことば", "NGÔN DIỆP", "từ ngữ, ngôn ngữ"),
    "音楽": ("おんがく", "ÂM LẠC", "âm nhạc"),
    "新聞": ("しんぶん", "TÂN VĂN", "báo chí"),
    "電車": ("でんしゃ", "ĐIỆN XA", "tàu điện"),
    "世界": ("せかい", "THẾ GIỚI", "thế giới"),
    "地球": ("ちきゅう", "ĐỊA CẦU", "Trái Đất"),
    "環境": ("かんきょう", "HOÀN CẢNH", "môi trường"),
    "研究": ("けんきゅう", "NGHIÊN CỨU", "nghiên cứu"),
    "技術": ("ぎじゅつ", "KỸ THUẬT", "kỹ thuật"),
    "大学": ("だいがく", "ĐẠI HỌC", "đại học"),
    "高校": ("こうこう", "CAO HIỆU", "trường cấp 3"),
    "社会": ("しゃかい", "XÃ HỘI", "xã hội"),
    "歴史": ("れきし", "LỊCH SỬ", "lịch sử"),
    "外国語": ("がいこくご", "NGOẠI QUỐC NGỮ", "ngoại ngữ"),
    "日本語": ("にほんご", "NHẬT BẢN NGỮ", "tiếng Nhật"),
    "英語": ("えいご", "ANH NGỮ", "tiếng Anh"),
    "経験": ("けいけん", "KINH NGHIỆM", "kinh nghiệm"),
    "練習": ("れんしゅう", "LUYỆN TẬP", "luyện tập"),
    "約束": ("やくそく", "ƯỚC THÚC", "lời hứa, cuộc hẹn"),
    "毎日": ("まいにち", "MỖI NHẬT", "mỗi ngày"),
    "最近": ("さいきん", "TỐI CẬN", "gần đây"),
    "大切": ("たいせつ", "ĐẠI THIẾT", "quan trọng"),
    "必要": ("ひつよう", "TẤT YẾU", "cần thiết"),
    "重要": ("じゅうよう", "TRỌNG YẾU", "trọng yếu"),
    "安心": ("あんしん", "AN TÂM", "yên tâm"),
    "説明": ("せつめい", "THUYẾT MINH", "giải thích"),
    "確認": ("かくにん", "XÁC NHẬN", "xác nhận"),
    "連絡": ("れんらく", "LIÊN LẠC", "liên lạc"),
    "準備": ("じゅんび", "CHUẨN BỊ", "chuẩn bị"),
    "参加": ("さんか", "THAM GIA", "tham gia"),
    "相談": ("そうだん", "TƯƠNG ĐÀM", "bàn bạc, tư vấn"),
    "協力": ("きょうりょく", "HIỆP LỰC", "hợp tác"),
    "販売": ("はんばい", "PHIẾN MẠI", "bán hàng"),
    "寄付": ("きふ", "KÝ PHÓ", "quyên góp"),
    "対象": ("たいしょう", "ĐỐI TƯỢNG", "đối tượng"),
    "休診": ("きゅうしん", "HƯU CHẨN", "nghỉ khám"),
    "注意": ("ちゅうい", "CHÚ Ý", "lưu ý"),
    "受付": ("うけつけ", "THỤ PHÓ", "tiếp nhận, lễ tân"),
    "午前": ("ごぜん", "NGỌ TIỀN", "buổi sáng"),
    "午後": ("ごご", "NGỌ HẬU", "buổi chiều"),
    "医師": ("いし", "Y SƯ", "bác sĩ"),
    "症状": ("しょうじょう", "CHỨNG TRẠNG", "triệu chứng"),
    "使用": ("しよう", "SỬ DỤNG", "sử dụng"),
    "容器": ("ようき", "DUNG KHÍ", "vật chứa, lọ"),
    "植物": ("しょくぶつ", "THỰC VẬT", "thực vật"),
    "水分": ("すいぶん", "THỦY PHÂN", "hơi ẩm, nước"),
    "太陽": ("たいよう", "THÁI DƯƠNG", "mặt trời"),
    "空気": ("くうき", "KHÔNG KHÍ", "không khí"),
    "場所": ("ばしょ", "TRƯỜNG SỞ", "địa điểm"),
    "理由": ("りゆう", "LÝ DO", "lý do"),
    "意味": ("いみ", "Ý VỊ", "ý nghĩa"),
    "原因": ("げんいん", "NGUYÊN NHÂN", "nguyên nhân"),
    "結果": ("けっか", "KẾT QUẢ", "kết quả"),
    "事件": ("じけん", "SỰ KIỆN", "vụ việc"),
    "性格": ("せいかく", "TÍNH CÁCH", "tính cách"),
    "離婚": ("りこん", "LY HÔN", "ly hôn"),
    "歌手": ("かしゅ", "CA THỦ", "ca sĩ"),
    "季節": ("きせつ", "QUÝ TIẾT", "mùa"),
    "読書": ("どくしょ", "ĐỘC THƯ", "đọc sách"),
    "間違い": ("まちがい", "GIAN VI", "lỗi sai"),
    "掃除": ("そうじ", "TẢO TRỪ", "dọn dẹp"),
    "給料": ("きゅうりょう", "CẤP LIỆU", "tiền lương"),
    "荷物": ("にもつ", "HÀ VẬT", "hành lý, bưu kiện"),
    "食事": ("しょくじ", "THỰC SỰ", "bữa ăn"),
    "運動": ("うんどう", "VẬN ĐỘNG", "vận động"),
    "時間": ("じかん", "THỜI GIAN", "thời gian"),
    "会議": ("かいぎ", "HỘI NGHỊ", "cuộc họp"),
    "経済": ("けいざい", "KINH TẾ", "kinh tế"),
    "情報": ("じょうほう", "TÌNH BÁO", "thông tin"),
    "現代": ("げんだい", "HIỆN ĐẠI", "hiện đại"),
    "教育": ("きょういく", "GIÁO DỤC", "giáo dục"),
    "台風": ("たいふう", "ĐÀI PHONG", "bão"),
    "天気予報": ("てんきよほう", "THIÊN KHÍ DỰ BÁO", "dự báo thời tiết"),
    "普通": ("ふつう", "PHỔ THÔNG", "thông thường"),
    "特別": ("とくべつ", "ĐẶC BIỆT", "đặc biệt"),
    "最近": ("さいきん", "TỐI CẬN", "gần đây"),
    "自分": ("じぶん", "TỰ PHÂN", "bản thân"),
    "相手": ("あいて", "TƯƠNG THỦ", "đối phương"),
    "必要": ("ひつよう", "TẤT YẾU", "cần thiết"),
    "海外": ("かいがい", "HẢI NGOẠI", "nước ngoài"),
    "国際": ("こくさい", "QUỐC TẾ", "quốc tế"),
    "料理": ("りょうり", "LIỆU LÝ", "món ăn, nấu ăn"),
    "健康": ("けんこう", "KIẾN KHANG", "sức khỏe"),
    "公園": ("こうえん", "CÔNG VIÊN", "công viên"),
    "図書館": ("としょかん", "ĐỒ THƯ QUÁN", "thư viện"),
    "病院": ("びょういん", "BỆNH VIỆN", "bệnh viện"),
    "木曜日": ("もくようび", "MỘC DIỆU NHẬT", "Thứ 5"),
    "金曜日": ("きんようび", "KIM DIỆU NHẬT", "Thứ 6"),
    "土曜日": ("どようび", "THỔ DIỆU NHẬT", "Thứ 7"),
    "日曜日": ("にちようび", "NHẬT DIỆU NHẬT", "Chủ nhật"),
    "月曜日": ("げつようび", "NGUYỆT DIỆU NHẬT", "Thứ 2"),
    "時間": ("じかん", "THỜI GIAN", "thời gian"),
    "自転車": ("じてんしゃ", "TỰ CHUYỂN XA", "xe đạp"),
    "気持ち": ("きもち", "KHÍ TRÌ", "tâm trạng"),
    "習慣": ("しゅうかん", "TẬP QUÁN", "thói quen"),
    "文化": ("ぶんか", "VĂN HÓA", "văn hóa"),
    "自然": ("しぜん", "TỰ NHIÊN", "thiên nhiên"),
    "将来": ("しょうらい", "TƯƠNG LAI", "tương lai"),
    "利用": ("りよう", "LỢI DỤNG", "sử dụng"),
    "方法": ("ほうほう", "PHƯƠNG PHÁP", "phương pháp"),
    "場所": ("ばしょ", "TRƯỜNG SỞ", "địa điểm"),
    "案内": ("あんない", "ÁN NỘI", "hướng dẫn"),
    "返事": ("へんじ", "PHẢN SỰ", "trả lời"),
    "質問": ("しつもん", "CHẤT VẤN", "câu hỏi"),
    "回答": ("かいとう", "HỒI ĐÁP", "câu trả lời"),
    "失敗": ("しっぱい", "THẤT BẠI", "thất bại"),
    "成功": ("せいこう", "THÀNH CÔNG", "thành công"),
    "合格": ("ごうかく", "HỢP CÁCH", "đỗ kỳ thi"),
    "留学": ("りゅうがく", "LƯU HỌC", "du học"),
    "市民": ("しみん", "THỊ DÂN", "người dân"),
    "交流": ("こうりゅう", "GIAO LƯU", "giao lưu"),
    "雑誌": ("ざっし", "TẠP CHÍ", "tạp chí"),
    "漫画": ("まんが", "MẠN HỌA", "truyện tranh"),
    "教科書": ("きょうかしょ", "GIÁO KHOA THƯ", "sách giáo khoa"),
    "問題集": ("もんだいしゅう", "VẤN ĐỀ TẬP", "sách bài tập"),
    "贈り物": ("おくりもの", "TẶNG VẬT", "món quà"),
    "笑顔": ("えがお", "TIẾU NHAN", "khuôn mặt cười"),
    "記憶": ("きおく", "KÝ ỨC", "ký ức"),
    "記録": ("きろく", "KÝ LỤC", "ghi chép"),
    "製品": ("せいひん", "CHẾ PHẨM", "sản phẩm"),
    "故障": ("こしょう", "CỐ CHƯỚNG", "hỏng hóc"),
    "無料": ("むりょう", "VÔ LIỆU", "miễn phí"),
    "有料": ("ゆうりょう", "HỮU LIỆU", "có phí"),
    "予定": ("よてい", "DỰ ĐỊNH", "dự định"),
    "出席": ("しゅっせき", "XUẤT TỊCH", "tham dự"),
    "欠席": ("けっせき", "KHUYẾT TỊCH", "vắng mặt"),
    "全員": ("ぜんいん", "TOÀN VIÊN", "toàn bộ thành viên"),
    "気温": ("きおん", "KHÍ ÔN", "nhiệt độ không khí"),
    "夏休み": ("なつやすみ", "HẠ HƯU", "nghỉ hè"),
    "小学生": ("しょうがくせい", "TIỂU HỌC SINH", "học sinh tiểu học"),
    "中学生": ("ちゅうがくせい", "TRUNG HỌC SINH", "học sinh cấp 2"),
    "大学生": ("だいがくせい", "ĐẠI HỌC SINH", "sinh viên đại học"),
    "新幹線": ("しんかんせん", "TÂN CÁN TUYẾN", "tàu Shinkansen"),
    "駅前": ("えきまえ", "DỊCH TIỀN", "trước nhà ga"),
    "近所": ("きんじょ", "CẬN SỞ", "hàng xóm, gần nhà"),
    "花屋": ("はなや", "HOA ỐC", "tiệm hoa"),
    "本屋": ("ほんや", "BẢN ỐC", "hiệu sách"),
    "部屋": ("へや", "BỘ ỐC", "căn phòng"),
    "海岸": ("かいがん", "HẢI NGẠN", "bờ biển"),
    "道路": ("どうろ", "ĐẠO LỘ", "con đường"),
    "季節": ("きせつ", "QUÝ TIẾT", "mùa"),
    "昔": ("むかし", "TÍCH", "ngày xưa"),
    "人間": ("にんげん", "NHÂN GIAN", "con người"),
    "上司": ("じょうし", "THƯỢNG TI", "cấp trên"),
    "部下": ("ぶか", "BỘ HẠ", "cấp dưới"),
    "機会": ("きかい", "CƠ HỘI", "cơ hội"),
    "選手": ("せんしゅ", "TUYỂN THỦ", "vận động viên"),
    "試合": ("しあい", "THÍ HỢP", "trận đấu"),
    "優勝": ("ゆうしょう", "ƯU THẮNG", "vô địch"),
    "湿度": ("しつど", "THẤP ĐỘ", "độ ẩm"),
    "否定": ("ひてい", "PHỦ ĐỊNH", "phủ nhận"),
    "不便": ("ふべん", "BẤT TIỆN", "bất tiện"),
    "小鳥": ("ことり", "TIỂU ĐIỂU", "chim nhỏ"),
    "態度": ("たいど", "THÁI ĐỘ", "thái độ"),
    "礼儀": ("れいぎ", "LỄ NGHI", "lễ nghi"),
    "文句": ("もんく", "VĂN CÚ", "lời phàn nàn"),
    "幸福": ("こうふく", "HẠNH PHÚC", "hạnh phúc"),
    "改善": ("かいぜん", "CẢI THIỆN", "cải thiện"),
    "物事": ("ものごと", "VẬT SỰ", "sự vật, sự việc"),
    "中止": ("ちゅうし", "TRUNG CHỈ", "hủy bỏ"),
    "管理": ("かんり", "QUẢN LÝ", "quản lý"),
    "以降": ("いこう", "DĨ GIÁNG", "trở đi"),
    "遠慮": ("えんりょ", "VIỄN LỰ", "ngại ngùng"),
    "事故": ("じこ", "SỰ CỐ", "tai nạn"),
    "満足": ("まんぞく", "MÃN TÚC", "hài lòng"),
    "急行": ("きゅうこう", "CẤP HÀNH", "tàu tốc hành"),
    "意識": ("いしき", "Ý THỨC", "ý thức"),
    "広告": ("こうこく", "QUẢNG CÁO", "quảng cáo"),
    "禁止": ("きんし", "CẤM CHỈ", "nghiêm cấm"),
    "豊富": ("ほうふ", "PHONG PHÚ", "phong phú"),
    "暗記": ("あんき", "ÁM KÝ", "học thuộc lòng"),
    "興味": ("きょうみ", "HỨNG VỊ", "hứng thú"),
    "夫婦": ("ふうふ", "PHU PHỤ", "vợ chồng"),
    "乾燥": ("かんそう", "KHÔ TÁO", "khô ráo"),
    "本音": ("ほんね", "BẢN ÂM", "lời thật lòng"),
    "感謝": ("かんしゃ", "CẢM TẠ", "cảm ơn"),
    "現実": ("げんじつ", "HIỆN THỰC", "hiện thực"),
}

# Build sorted word pattern longest-first
_SORTED_WORDS = sorted(BACKGROUND_LEXICON.keys(), key=len, reverse=True)
_WORD_REGEX = re.compile("|".join(re.escape(w) for w in _SORTED_WORDS))
_ORIG_RUBY_RE = re.compile(r"([\u4e00-\u9faf々〆ヶ]+)（([\u3040-\u309f]+)）")
_MASKED_SPAN_RE = re.compile(r"(【[^】]*】)")
_VARIANT_PREFIX_RE = re.compile(r"^(【(?:Evidence-First|Đảo |Biến thể|Chẩn đoán)[^】]*】)\s*")


def determine_scaffold_tier(stability: float, exam_mode: bool = False) -> int:
    """Compute scaffolding tier (1, 2, or 3) from FSRS stability and exam mode."""
    if exam_mode or stability >= SCAFFOLD_TIER3_STABILITY:
        return 3
    if stability >= SCAFFOLD_TIER2_STABILITY:
        return 2
    return 1


def tier_label_vi(tier: int) -> str:
    if tier == 1:
        return "Hỗ trợ Mức 1: Hiện phiên âm từ xung quanh (che từ đang hỏi 【...】)"
    if tier == 2:
        return "Hỗ trợ Mức 2: Ẩn phiên âm phụ (bấm phím H nếu cần 1 gợi ý)"
    return "Mức 3: Như thi thật (không gợi ý, không phiên âm phụ)"


def _extract_masked_terms(
    text: str,
    focus_keyword: Optional[str] = None,
    options: Optional[List[str]] = None,
) -> Set[str]:
    """Identify all terms enclosed in 【...】, target keywords, or short option tokens to prevent answer leaks."""
    masked: Set[str] = set()
    for m in _MASKED_SPAN_RE.finditer(text or ""):
        inner = m.group(1)[1:-1].strip()
        if inner:
            masked.add(inner)
            # Also add Kanji sub-stems
            for k in re.findall(r"[\u4e00-\u9faf]+", inner):
                masked.add(k)
    if focus_keyword:
        for tok in re.split(r"[\s→＝/・（）()]+", focus_keyword):
            tok = tok.strip()
            if tok and re.search(r"[\u4e00-\u9faf\u3040-\u309f\u30a0-\u30ff]", tok):
                masked.add(tok)
    if options:
        for opt in options:
            clean_opt = re.sub(r"（[^）]{1,12}）", "", str(opt or "")).strip()
            if clean_opt and len(clean_opt) <= 12 and "。" not in clean_opt:
                masked.add(clean_opt)
                for k in re.findall(r"[\u4e00-\u9faf]{2,}", clean_opt):
                    masked.add(k)
    return masked


def _render_orig_ruby_only(segment: str) -> str:
    """Preserve ONLY exam-original 漢字（かな） inline furigana as <ruby class='orig-ruby'>."""
    parts: List[str] = []
    pos = 0
    for m in _ORIG_RUBY_RE.finditer(segment):
        if m.start() > pos:
            parts.append(html.escape(segment[pos : m.start()]))
        kanji = html.escape(m.group(1))
        kana = html.escape(m.group(2))
        parts.append(f'<ruby class="orig-ruby">{kanji}<rt>{kana}</rt></ruby>')
        pos = m.end()
    if pos < len(segment):
        parts.append(html.escape(segment[pos:]))
    return "".join(parts)


def _render_tier1_segment(
    segment: str,
    masked_terms: Set[str],
    collected_glossary: List[Dict[str, str]],
    seen_words: Set[str],
) -> str:
    """Render Tier 1 scaffolding on non-target background text while protecting masked terms."""
    parts: List[str] = []
    pos = 0
    # Preserve exam-original 漢字（かな） chunks intact first
    for m in _ORIG_RUBY_RE.finditer(segment):
        if m.start() > pos:
            parts.append(
                _annotate_plain_chunk(
                    segment[pos : m.start()], masked_terms, collected_glossary, seen_words
                )
            )
        kanji = html.escape(m.group(1))
        kana = html.escape(m.group(2))
        parts.append(f'<ruby class="orig-ruby">{kanji}<rt>{kana}</rt></ruby>')
        pos = m.end()
    if pos < len(segment):
        parts.append(
            _annotate_plain_chunk(segment[pos:], masked_terms, collected_glossary, seen_words)
        )
    return "".join(parts)


def _annotate_plain_chunk(
    chunk: str,
    masked_terms: Set[str],
    collected_glossary: List[Dict[str, str]],
    seen_words: Set[str],
) -> str:
    out: List[str] = []
    pos = 0
    for m in _WORD_REGEX.finditer(chunk):
        word = m.group(0)
        hira, hv, meaning = BACKGROUND_LEXICON[word]
        # Strict Anti-Leak check: never annotate any word overlapping masked terms or option readings
        if any(
            word in mt or mt in word or hira == mt or (len(mt) >= 2 and mt in hira)
            for mt in masked_terms
        ):
            continue
        if m.start() > pos:
            out.append(html.escape(chunk[pos : m.start()]))
        out.append(
            f'<ruby class="scaffold-ruby" data-hv="{html.escape(hv)}" '
            f'data-meaning="{html.escape(meaning)}">{html.escape(word)}<rt>{html.escape(hira)}</rt></ruby>'
        )
        if word not in seen_words:
            seen_words.add(word)
            collected_glossary.append(
                {"word": word, "reading": hira, "han_viet": hv, "meaning_vi": meaning}
            )
        pos = m.end()
    if pos < len(chunk):
        out.append(html.escape(chunk[pos:]))
    return "".join(out)


def apply_scaffolding(
    prompt_jp: str,
    options: List[str],
    stability: float,
    exam_mode: bool = False,
    focus_keyword: Optional[str] = None,
) -> Dict[str, Any]:
    """Render question prompt and options according to 3-tier scaffolding rules."""
    tier = determine_scaffold_tier(stability, exam_mode=exam_mode)
    raw_prompt = prompt_jp or ""
    prefix_html = ""
    m_vp = _VARIANT_PREFIX_RE.match(raw_prompt)
    if m_vp:
        prefix_html = f'<span class="badge accent" style="margin-right:6px;">{html.escape(m_vp.group(1)[1:-1])}</span> '
        raw_prompt = raw_prompt[m_vp.end() :]

    masked_terms = _extract_masked_terms(raw_prompt, focus_keyword=focus_keyword, options=options)
    glossary: List[Dict[str, str]] = []
    seen_words: Set[str] = set()

    rendered_parts: List[str] = [prefix_html] if prefix_html else []
    pos = 0
    for m in _MASKED_SPAN_RE.finditer(raw_prompt):
        if m.start() > pos:
            seg = raw_prompt[pos : m.start()]
            if tier == 1:
                rendered_parts.append(_render_tier1_segment(seg, masked_terms, glossary, seen_words))
            else:
                rendered_parts.append(_render_orig_ruby_only(seg))
        # Target inside 【...】 is ALWAYS masked without artificial furigana or Hán-Việt
        masked_text = html.escape(m.group(1))
        rendered_parts.append(f'<span class="target-mask">{masked_text}</span>')
        pos = m.end()

    if pos < len(raw_prompt):
        tail = raw_prompt[pos:]
        if tier == 1:
            rendered_parts.append(_render_tier1_segment(tail, masked_terms, glossary, seen_words))
        else:
            rendered_parts.append(_render_orig_ruby_only(tail))

    # Options MUST NEVER receive injected scaffolding furigana or Hán-Việt
    options_html = [_render_orig_ruby_only(opt) for opt in options]

    return {
        "tier": tier,
        "tier_label": tier_label_vi(tier),
        "prompt_html": "".join(rendered_parts),
        "options_html": options_html,
        "background_glossary": glossary if tier == 1 else [],
        "hint_allowed": (tier == 2 and not exam_mode),
        "masked_terms": sorted(masked_terms),
    }


def apply_passage_scaffolding(
    japanese_text: str,
    stability: float,
    exam_mode: bool = False,
    sentences: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Apply 3-tier scaffolding to a Dokkai or cloze passage (preserving exam-original furigana)."""
    tier = determine_scaffold_tier(stability, exam_mode=exam_mode)
    glossary: List[Dict[str, str]] = []
    seen_words: Set[str] = set()

    def _render_line(line: str) -> str:
        parts: List[str] = []
        pos = 0
        for m in _MASKED_SPAN_RE.finditer(line):
            if m.start() > pos:
                seg = line[pos : m.start()]
                parts.append(
                    _render_tier1_segment(seg, set(), glossary, seen_words)
                    if tier == 1
                    else _render_orig_ruby_only(seg)
                )
            parts.append(f'<span class="target-mask">{html.escape(m.group(1))}</span>')
            pos = m.end()
        if pos < len(line):
            tail = line[pos:]
            parts.append(
                _render_tier1_segment(tail, set(), glossary, seen_words)
                if tier == 1
                else _render_orig_ruby_only(tail)
            )
        return "".join(parts)

    sentence_htmls = [_render_line(s) for s in (sentences or [])]
    full_html = "<br>".join(_render_line(ln) for ln in str(japanese_text or "").splitlines())
    return {
        "tier": tier,
        "full_html": full_html,
        "sentence_htmls": sentence_htmls,
        "background_glossary": glossary[:15] if tier == 1 else [],
    }


def get_contextual_hint(
    prompt_jp: str,
    stability: float,
    exam_mode: bool = False,
    focus_keyword: Optional[str] = None,
    bridge_focus: Optional[str] = None,
    options: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Provide max 1 safe contextual hint in Tier 2 (or Tier 1), strictly locked in Tier 3 / Exam Mode."""
    tier = determine_scaffold_tier(stability, exam_mode=exam_mode)
    if tier == 3 or exam_mode:
        return {
            "allowed": False,
            "tier": tier,
            "hint_text": None,
            "reason": "Chế độ Phòng thi (Cấp 3) khóa 100% gợi ý Giàn giáo.",
        }

    masked_terms = _extract_masked_terms(prompt_jp, focus_keyword=focus_keyword, options=options)
    # Find up to 2 background words outside 【...】 to aid sentence comprehension without leaking the target
    bg_items: List[str] = []
    cleaned_prompt = _MASKED_SPAN_RE.sub(" ", prompt_jp or "")
    for m in _WORD_REGEX.finditer(cleaned_prompt):
        w = m.group(0)
        hira, hv, meaning = BACKGROUND_LEXICON[w]
        if any(w in mt or mt in w or hira == mt or (len(mt) >= 2 and mt in hira) for mt in masked_terms):
            continue
        entry = f"{w} ({hira} | {hv}): {meaning}"
        if entry not in bg_items:
            bg_items.append(entry)
        if len(bg_items) >= 2:
            break

    if bg_items:
        hint_text = "Từ nền ngữ cảnh: " + " ; ".join(bg_items)
    elif bridge_focus:
        hint_text = f"Khung nền N4->N3 cần nhớ: {bridge_focus}"
    else:
        hint_text = "Đọc kỹ trợ từ ngay trước/sau vị trí cần điền và loại các đáp án trái nghĩa."

    return {
        "allowed": True,
        "tier": tier,
        "hint_text": hint_text,
        "penalty_note": "Dùng gợi ý (H) sẽ giới hạn đánh giá tối đa ở mức Hard và chưa tính vào [MASTERED 10/10].",
    }
