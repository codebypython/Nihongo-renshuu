"""Comprehensive JLPT (N5-N2) Grammar Corpus, Diagnostic Drills, and Curated Foundation Vocab.

Grounded directly in:
- 7 exam workbooks in exam_downloads/ (163 unique questions, 22 passages)
- Shin-N3-List.pdf (105 core N3 patterns)
- So-do-ngu-pha-p-N5-N1-2-0.pdf (N5->N1 mindmap system)
- Kosei-Giao-trinh-doc-hieu-online.pdf (Dokkai sentence & discourse analysis)
- Tu-vung-Mimikara-Oboeru-N3.pdf, N3-Somatome-Kanji-List-VN.pdf, 214-Bo-Thu.pdf
- anki_grammar_tier1.csv & 03_Grammar/ course drills
"""

from typing import Any, Dict, List

CATEGORY_LABELS: Dict[str, str] = {
    "conjugation": "Chia thể & Hình thái",
    "particle": "Trợ từ & Nhấn mạnh",
    "clause_connector": "Liên kết Mệnh đề & Điều kiện",
    "modality": "Phán đoán, Ý chí & Nghĩa vụ",
    "aspect": "Thể & Diễn biến Thời gian",
    "contrast_concession": "Tương phản & Nhượng bộ",
    "passive_causative": "Bị động & Sai khiến",
    "discourse": "Liên từ & Mạch diễn ngôn",
    "keigo": "Kính ngữ & Trao nhận",
}

GRAMMAR_POINTS_DATA: List[Dict[str, Any]] = [
    # =========================================================================
    # JLPT N5 FOUNDATION (GP-N5-01 .. GP-N5-18)
    # =========================================================================
    {
        "code": "GP-N5-01",
        "pattern": "Chia động từ Nhóm 1/2/3 & Thể て・た・ない",
        "jlpt_level": "N5",
        "category": "conjugation",
        "category_label_vi": CATEGORY_LABELS["conjugation"],
        "in_exam_corpus": True,
        "formation_formula": "V1(u-i-te-ta-nai theo hàng âm) | V2(bỏ る + ます/て/た/ない) | V3(する->し/して/した, 来る->き/きて/きた/こない)",
        "formation_table": [
            {"pos": "Nhóm 1 (Godan)", "rule": "う/つ/る -> って; む/ぶ/ぬ -> んで; く -> いて (行く->いって); ぐ -> いで; す -> して"},
            {"pos": "Nhóm 1 (Thể ない)", "rule": "Đổi âm cuối cột う -> cột あ + ない (riêng う -> わない, ví dụ 会う->会わない)"},
            {"pos": "Nhóm 2 (Ichidan)", "rule": "Bỏ る + て / た / ない / ます (ví dụ 食べる -> 食べて / 食べた / 食べない)"},
            {"pos": "Nhóm 3 (Bất quy tắc)", "rule": "する -> して / した / しない; 来る(くる) -> きて(来て) / きた / こない"},
        ],
        "core_meaning_vi": "Hệ thống chia 4 thể gốc động từ tiếng Nhật làm nền tảng cho mọi cấu trúc N4-N2",
        "deep_explanation_vi": (
            "Mọi mẫu ngữ pháp N4-N2 đều ghép trực tiếp vào một trong 4 gốc động từ (Từ điển Vる, Thể Vます, Thể Vない, Thể Vて/Vた). "
            "Điểm hay nhầm nhất ở người học xuất phát từ N5 là các động từ nhóm 1 có đuôi -iru/-eru giả nhóm 2 (như 帰る -> 帰って, 入る -> 入って, 切る -> 切って, 散る -> 散って, 走る -> 走って). "
            "Khi gặp câu đề 問題1 hay 問題3, nếu không nhận ra động từ nhóm 1 chia て thành って (như 散る -> 散って trong Q#104, 混ざる -> 混ざって trong Q#41), rất dễ đọc sai hoặc nối sai hậu tố."
        ),
        "register_tag": "Nền tảng Toàn hệ thống",
        "confusable_pairs": [
            {
                "rival_pattern": "V1 đuôi る (散る・切る・入る) vs V2 đuôi る (見る・起きる)",
                "difference_vi": "V1 giữ lại hoặc biến âm thành って/らない (散って, 散らない); V2 bỏ hẳn る (見て, 見ない).",
                "quick_test_vi": "Kiểm tra nguyên âm trước る: nếu là a/u/o chắc chắn V1; nếu là i/e kiểm tra danh sách ngoại lệ V1 quen thuộc (帰る, 入る, 切る, 知る, 走る, 散る).",
            }
        ],
        "examples": [
            {
                "jp": "桜の花は、もう散ってしまった。",
                "reading_note": "さくらのはなは、もうちってしまった。",
                "vi": "Hoa anh đào thì đã rụng mất rồi.",
                "grammar_note": "散る (ちる) là động từ nhóm 1 ngoại lệ nên chia thể て thành 散って (không phải 散て).",
            },
            {
                "jp": "男女が混ざってサッカーをした。",
                "reading_note": "だんじょがまざってさっかーをした。",
                "vi": "Nam và nữ đã hòa chung chơi bóng đá.",
                "grammar_note": "混ざる (tự động từ nhóm 1) -> 混ざって, khác với 混ぜる (tha động từ nhóm 2) -> 混ぜて.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 (Trang 1) | Đề .xlsx (Q41, Q104)",
        "search_keywords": "chia dong tu nhom 1 2 3 the te ta nai godan ichidan 散る 混ざる",
        "match_patterns": ["てしま", "ないで", "って", "んで", "散って", "まざって"],
    },
    {
        "code": "GP-N5-02",
        "pattern": "Trợ từ cốt lõi は・が・を",
        "jlpt_level": "N5",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": True,
        "formation_formula": "Chủ đề + は | Chủ thể / Đối tượng tính chất + が | Tân ngữ trực tiếp + を",
        "formation_table": [
            {"pos": "Danh từ + は", "rule": "Đánh dấu chủ đề câu, đối lập tương phản hai vế (Aは...が、Bは...)"},
            {"pos": "Danh từ + が", "rule": "Đánh dấu chủ thể của tự động từ, bị động, khả năng, mệnh đề phụ"},
            {"pos": "Danh từ + を", "rule": "Đánh dấu tân ngữ chịu tác động của tha động từ, hoặc điểm đi qua/rời khỏi (出る・歩く)"},
        ],
        "core_meaning_vi": "Phân định vai trò ngữ pháp: Chủ đề (は) - Chủ thể/Nội tại (が) - Tân ngữ tác động (を)",
        "deep_explanation_vi": (
            "Tiếng Việt không có trợ từ tách bạch chủ thể và tân ngữ như tiếng Nhật nên người học hay dùng nhầm が và を. "
            "Trong đề thi N3, cặp が vs を là chìa khóa giải nhanh tới 35% câu điền từ 問題3 và câu ghép sao ★ 問題2: "
            "nếu trước chỗ trống là が (ví dụ 男女が..., 家が...), động từ bắt buộc là tự động từ hoặc bị động; nếu là を (ví dụ 魚を..., 入るのを...), bắt buộc là tha động từ. "
            "Ngoài ra trong mệnh đề định ngữ bổ nghĩa danh từ, chủ thể thường dùng が hoặc の chứ không dùng は."
        ),
        "register_tag": "Trung tính (Cơ bản bắt buộc)",
        "confusable_pairs": [
            {
                "rival_pattern": "N + が vs N + を",
                "difference_vi": "が đi với tự động từ, thể bị động, thể khả năng và tính từ (好きな/上手な); を đi với tha động từ tác động trực tiếp.",
                "quick_test_vi": "Nhìn động từ cuối cụm: nếu là V-tự động hoặc Vられる/Vえる chọn が; nếu có hành động tác động lên vật chọn を.",
            }
        ],
        "examples": [
            {
                "jp": "機内における携帯電話の使用は禁止されています。",
                "reading_note": "きないにおけるけいたいでんわのしようはきんしされています。",
                "vi": "Việc sử dụng điện thoại di động trên máy bay bị nghiêm cấm.",
                "grammar_note": "Cụm danh từ dài '携帯電話の使用' được chốt chủ đề bằng は trước vị ngữ bị động '禁止されています'.",
            },
            {
                "jp": "冬には冷たい空気が部屋の中に入るのを防ぎます。",
                "reading_note": "ふゆにはつめたいくうきがへやのなかにはいるのをふせぎます。",
                "vi": "Vào mùa đông, cửa ngăn việc không khí lạnh lọt vào phòng.",
                "grammar_note": "Trong mệnh đề phụ dùng '空気が入る', còn tân ngữ của tha động từ 防ぐ bắt buộc dùng のを.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 (Trang 1) | Đề .xlsx (Q22, Q56, Q149)",
        "search_keywords": "tro tu wa ga o chu de tan ngu は が を",
        "match_patterns": ["の使用は", "空気が", "のを防"],
    },
    {
        "code": "GP-N5-03",
        "pattern": "Trợ từ địa điểm・thời gian・phương tiện に・で・へ",
        "jlpt_level": "N5",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": True,
        "formation_formula": "Điểm tồn tại / Thời điểm / Đích đến + に | Nơi diễn ra hành động / Phương tiện / Nguyên nhân + で | Hướng đi + へ",
        "formation_table": [
            {"pos": "N(địa điểm/thời gian) + に", "rule": "Chỉ vị trí tồn tại (ある・いる・住む), điểm đến (行く・着く), đích tác động (に備える・に遭う)"},
            {"pos": "N(địa điểm/công cụ) + で", "rule": "Chỉ nơi diễn ra hành động (V), phương tiện/nguyên liệu (電車で・日本語で), phạm vi (1年で)"},
            {"pos": "N(phương hướng) + へ", "rule": "Chỉ hướng di chuyển (tiếp nối với の tạo への + N để bổ nghĩa danh từ)"},
        ],
        "core_meaning_vi": "Định vị chính xác nơi chốn tồn tại (に), nơi hành động/công cụ (で) và hướng di chuyển (へ)",
        "deep_explanation_vi": (
            "Người Việt dịch cả に và で là 'ở', dẫn đến nhầm lẫn kinh điển: với động từ chỉ trạng thái tĩnh hoặc điểm đến (ある・いる・住む・並ぶ・乗る・着く・備える・感謝する), luôn dùng に; "
            "còn với động từ hành động diễn ra tại không gian đó (勉強する・開く・食べる・買う) hoặc phương tiện/nguyên liệu/lý do, dùng で. "
            "Khi chuyển lên N3, に mở rộng thành に沿って, に備えて, に遭う, に対して, において (thay thế で ở văn viết)."
        ),
        "register_tag": "Trung tính (Cơ bản bắt buộc)",
        "confusable_pairs": [
            {
                "rival_pattern": "Địa điểm + に vs Địa điểm + で",
                "difference_vi": "に đánh dấu vị trí tồn tại tĩnh hoặc điểm đích bám vào; で đánh dấu sân khấu nơi hành động diễn ra.",
                "quick_test_vi": "Nếu là ある/いる/住む/座る/並んでいる dùng に; nếu là động từ hành động tích cực dùng で.",
            }
        ],
        "examples": [
            {
                "jp": "りんごが箱の中に並んでいる。",
                "reading_note": "りんごがはこのなかにならんでいる。",
                "vi": "Những quả táo được xếp ngay ngắn trong hộp.",
                "grammar_note": "並ぶ ở trạng thái tồn tại kết quả (並んでいる) dùng trợ từ vị trí に (箱の中に).",
            },
            {
                "jp": "大きな川に沿って歩く。",
                "reading_note": "おおきなかわにそってあるく。",
                "vi": "Đi bộ dọc theo con sông lớn.",
                "grammar_note": "沿う bám dọc theo vật thể dùng に; hành động đi bộ diễn ra ở không gian rộng dùng で khi không có 沿う.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 (Trang 1) | Đề .xlsx (Q69, Q79)",
        "search_keywords": "tro tu ni de e dia diem phuong tien に で へ",
        "match_patterns": ["の中に", "において", "に沿って"],
    },
    {
        "code": "GP-N5-04",
        "pattern": "Trợ từ phạm vi & so sánh から・まで・より",
        "jlpt_level": "N5",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": True,
        "formation_formula": "Điểm đầu + から | Điểm cuối / Mức giới hạn + まで | Mốc so sánh + より (～のほうが)",
        "formation_table": [
            {"pos": "N / Thời gian + から～まで", "rule": "Từ điểm A đến điểm B (không gian, thời gian, mức độ)"},
            {"pos": "N + より + A / V", "rule": "Hơn so với N (AはBより～; BよりAのほうが～)"},
            {"pos": "Động từ + まで", "rule": "Cho đến tận khi xảy ra V (Vる + まで)"},
        ],
        "core_meaning_vi": "Xác định điểm xuất phát (から), điểm kết thúc (まで) và mốc đối chiếu so sánh (より)",
        "deep_explanation_vi": (
            "Trong đề Đọc hiểu 情報検索 và 短文 (như Q#30, Q#64, Q#162), から・まで・までに là bẫy chốt lịch trình: "
            "まで là liên tục cho đến thời điểm X, còn までに là hạn chót phải hoàn thành trước thời điểm X. "
            "Còn より xuất hiện thường xuyên trong các đáp án nhiễu của Đọc hiểu (Q#30: '他より大事だ' bị loại vì bài nói hai môn quan trọng ngang nhau)."
        ),
        "register_tag": "Trung tính (Cơ bản bắt buộc)",
        "confusable_pairs": [
            {
                "rival_pattern": "まで vs までに",
                "difference_vi": "まで chỉ trạng thái kéo dài liên tục tới mốc đó; までに chỉ hạn chót hoàn thành một hành động dứt điểm trước mốc đó.",
                "quick_test_vi": "Thử với câu 'nộp báo cáo': động từ hoàn thành 1 lần (出す・返事する・連絡する) dùng までに; trạng thái/mở cửa dùng まで.",
            }
        ],
        "examples": [
            {
                "jp": "出席できるかどうか、4月6日までにお返事ください。",
                "reading_note": "しゅっせきできるかどうか、しがつむいかまでにおへんじください。",
                "vi": "Hãy trả lời trước ngày 6/4 xem có tham dự được hay không.",
                "grammar_note": "お返事ください là hành động hoàn thành 1 lần nên dùng hạn chót までに.",
            },
            {
                "jp": "予約受付時間は、前日の午前9時から当日午後3時までです。",
                "reading_note": "よやくうけつけじかんは、ぜんじつのごぜんくじからとうじつごごさんじまでです。",
                "vi": "Thời gian tiếp nhận đặt lịch là từ 9 giờ sáng hôm trước đến 3 giờ chiều ngày khám.",
                "grammar_note": "Khung thời gian mở liên tục dùng cặp から～まで.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 | Đề .xlsx (Q30, Q64, Q162)",
        "search_keywords": "kara made made ni yori so sanh han chot から まで までに より",
        "match_patterns": ["までに", "から", "より"],
    },
    {
        "code": "GP-N5-05",
        "pattern": "Chia Tính từ đuôi い & Tính từ đuôi な (bổ nghĩa N, + なる)",
        "jlpt_level": "N5",
        "category": "conjugation",
        "category_label_vi": CATEGORY_LABELS["conjugation"],
        "in_exam_corpus": True,
        "formation_formula": "Aい: Aい+N / Aく+なる / Aくない / Aかった | Aな: Aな+N / Aに+なる / Aではない / Aだった",
        "formation_table": [
            {"pos": "Tính từ đuôi い (Aい)", "rule": "Bổ nghĩa N: giữ い (難しい問題); Đi với なる/する/V: đổi い->く (つけやすくなる, 早く治る); Phủ định: くない"},
            {"pos": "Tính từ đuôi な (Aな)", "rule": "Bổ nghĩa N: thêm な (素直な性格, 必要なとき); Đi với なる/する/V: thêm に (元気になる, 静かに話す)"},
            {"pos": "Ngoại lệ いい / よい", "rule": "Phải đổi về gốc よ trước khi chia: よくなる, よくない, よかった (cấm *いくなる)"},
        ],
        "core_meaning_vi": "Quy tắc biến hình tính từ tiếng Nhật khi bổ nghĩa danh từ, nối động từ và chia với なる",
        "deep_explanation_vi": (
            "Lỗi chia nhầm Aい thành Aな (như thêm に vào sau đuôi い: *つけやすいに trong Q#28) là bẫy kinh điển của đề N3 vì nhiều mẫu ngữ pháp N4/N3 kết thúc bằng い như ～やすい, ～にくい, ～たい, ～ほしい. "
            "Ngược lại, tính từ đuôi な như 素直な, 静かな, 不便な, 重要な khi đứng trước danh từ bắt buộc giữ な, và đứng trước なる/する phải đổi thành に."
        ),
        "register_tag": "Trung tính (Nền tảng chia thể)",
        "confusable_pairs": [
            {
                "rival_pattern": "Aい + くなる vs Aな + になる",
                "difference_vi": "Đuôi い (kể cả ～やすい, ～にくい, ～ない) bỏ い thêm く; đuôi な thêm に trước なる.",
                "quick_test_vi": "Thấy tận cùng là やすい / にくい / たい? Luôn chia như Aい -> やすくなる, にくくなる.",
            }
        ],
        "examples": [
            {
                "jp": "容器の先にスポンジがついているので、つけやすくなっています。",
                "reading_note": "ようきのさきにすぽんじがついているので、つけやすくなっています。",
                "vi": "Vì đầu lọ có miếng mút nên trở nên dễ thoa.",
                "grammar_note": "つけやすい mang đuôi い nên ghép với なっています phải đổi thành つけやすく (loại bẫy *つけやすいに).",
            },
            {
                "jp": "彼女は素直な性格だ。",
                "reading_note": "かのじょはすなおなせいかくだ。",
                "vi": "Cô ấy có tính cách hiền lành, ngoan ngoãn.",
                "grammar_note": "素直 là tính từ đuôi な nên bổ nghĩa danh từ 性格 phải chèn な.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 (Trang 1) | Đề .xlsx (Q23, Q28, Q74)",
        "search_keywords": "tinh tu duoi i na chia the ku naru ni naru やすい 素直",
        "match_patterns": ["やすくな", "にくくな", "くなる", "になる"],
    },
    {
        "code": "GP-N5-06",
        "pattern": "Mệnh đề định ngữ bổ nghĩa Danh từ (普通形 + N)",
        "jlpt_level": "N5",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": True,
        "formation_formula": "[Mệnh đề thể thông thường (Vる/Vた/Vない/Vている/Aい/Aな+な/N+の)] + Danh từ",
        "formation_table": [
            {"pos": "Động từ (V)", "rule": "Thể thông thường trực tiếp + N (乗っている電車, 使ったお金, 知らない人)"},
            {"pos": "Tính từ い / な", "rule": "Aい + N; Aな + な + N (大切な仕事, 必要なとき)"},
            {"pos": "Danh từ (N1)", "rule": "N1 + の + N2 (日本の家, 私の母)"},
            {"pos": "Chủ ngữ trong định ngữ", "rule": "Dùng が hoặc の thay cho は (母が作った料理, 窓の外側の植物が出す水分)"},
        ],
        "core_meaning_vi": "Ráp mệnh đề đứng TRƯỚC danh từ để định nghĩa hoặc mô tả chi tiết cho danh từ đó",
        "deep_explanation_vi": (
            "Tiếng Việt đặt định ngữ SAU danh từ ('chuyến tàu mà bạn đang đi'), còn tiếng Nhật đặt 100% mệnh đề định ngữ TRƯỚC danh từ (乗っている電車). "
            "Khi giải 問題2 ★ và Đọc hiểu câu dài N3, luôn tìm danh từ trung tâm đứng sau động từ thể thông thường (Vる/Vた/Vている) và nhớ không bao giờ dùng thể lịch sự ます/です hay trợ từ は bên trong mệnh đề định ngữ."
        ),
        "register_tag": "Trung tính (Cấu trúc cốt lõi)",
        "confusable_pairs": [
            {
                "rival_pattern": "V普通形 + N (Định ngữ) vs Vます + N (Sai ngữ pháp)",
                "difference_vi": "Định ngữ bắt buộc dùng thể thông thường (乗っている電車), tuyệt đối không dùng ます/です (*乗っています電車).",
                "quick_test_vi": "Gặp danh từ đứng ngay sau động từ? Động từ đó chắc chắn ở thể thông thường (る/た/ない/ている).",
            }
        ],
        "examples": [
            {
                "jp": "会う約束をした友だちから乗っている電車が止まっているというメールが来た。",
                "reading_note": "あうやくそくをしたともだちからのっているでんしゃがとまっているというめーるがきた。",
                "vi": "Tôi nhận được email từ người bạn đã hẹn gặp báo rằng chuyến tàu bạn ấy đang đi bị dừng.",
                "grammar_note": "3 tầng định ngữ lồng nhau: [会う約束をした]友だち và [乗っている]電車 và [止まっているという]メール.",
            },
            {
                "jp": "窓の外側の植物が出す水分によって冷やされている。",
                "reading_note": "まどのそとがわのしょくぶつがだすすいぶんによってひやされている。",
                "vi": "Được làm mát bởi hơi nước do cây cối bên ngoài cửa sổ tỏa ra.",
                "grammar_note": "Chủ thể bên trong mệnh đề định ngữ dùng が (植物が出す水分), bổ nghĩa cho danh từ 水分.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 | Đề .xlsx (Q24, Q151, Đọc hiểu)",
        "search_keywords": "dinh ngu menh de bo nghia danh tu 普通形 修飾",
        "match_patterns": ["ている電車", "約束をした", "出す水分", "というメール"],
    },
    {
        "code": "GP-N5-07",
        "pattern": "Danh từ hóa động từ bằng こと & の",
        "jlpt_level": "N5",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": True,
        "formation_formula": "V普通形 / Aい / Aな+な + こと / の (+ が / を / は / だ)",
        "formation_table": [
            {"pos": "Động từ (V)", "rule": "Vる / Vた / Vない + こと / の (読書すること, 部屋に入るの)"},
            {"pos": "Đi với vị ngữ tri giác / ngăn chặn", "rule": "Thấy / Nghe / Đợi / Giúp / Ngăn chặn (見る・聞く・待つ・手伝う・防ぐ) -> ưu tiên の"},
            {"pos": "Đi với định nghĩa / thói quen / khả năng", "rule": "ことです (định nghĩa), ことができる, ことがある -> bắt buộc dùng こと"},
        ],
        "core_meaning_vi": "Biến cả một hành động hoặc mệnh đề động từ thành cụm danh từ để làm chủ ngữ/tân ngữ",
        "deep_explanation_vi": (
            "Tiếng Nhật không thể đặt thẳng trợ từ が/を/は ngay sau động từ (không nói *入るを防ぎます). "
            "Phải chèn こと hoặc の để danh từ hóa hành động đó trước khi gắn trợ từ. "
            "Khác biệt tinh tế lên N3: với các động từ cảm nhận trực tiếp hay tác động tại chỗ như 見る, 聞く, 待つ, 手伝う, 止める, 防ぐ, tiếng Nhật dùng の (như 入るのを防ぎます trong Q#149), không dùng もの (chỉ đồ vật cụ thể)."
        ),
        "register_tag": "Trung tính (Nền tảng)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vる + の vs Vる + こと vs Vる + もの",
                "difference_vi": "の gắn với hành động cụ thể đang diễn ra/tri giác/ngăn chặn; こと gắn với khái niệm trừu tượng và cuối câu ...ことです; もの chỉ đồ vật.",
                "quick_test_vi": "Trước các động từ 見る・聞く・待つ・忘れる・防ぐ -> chọn の + trợ từ (を/が).",
            }
        ],
        "examples": [
            {
                "jp": "冬には冷たい空気が部屋の中に入るのを防ぎます。",
                "reading_note": "ふゆにはつめたいくうきがへやのなかにはいるのをふせぎます。",
                "vi": "Vào mùa đông, cửa ngăn việc không khí lạnh tràn vào phòng.",
                "grammar_note": "Động từ 防ぐ nhận tân ngữ với を nên danh từ hóa cụm '入る' bằng のを.",
            },
            {
                "jp": "親子のコミュニケーションをとることは、大切だ。",
                "reading_note": "おやこのこみゅにけーしょんをとることは、たいせつだ。",
                "vi": "Việc giao tiếp giữa cha mẹ và con cái rất quan trọng.",
                "grammar_note": "Nhận xét khái quát dùng こと làm chủ ngữ (～ことは大切だ).",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 | Đề .xlsx (Q17, Q89, Q149)",
        "search_keywords": "danh tu hoa koto no mono こと の ものを 防ぐ",
        "match_patterns": ["のを", "ことが", "ことは", "ことを"],
    },
    {
        "code": "GP-N5-08",
        "pattern": "Thể tiếp diễn, Thói quen & Trạng thái kết quả ～ている",
        "jlpt_level": "N5",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": True,
        "formation_formula": "Vて + いる / います (Phủ định: Vて + いない)",
        "formation_table": [
            {"pos": "V hành động kéo dài", "rule": "Đang diễn ra ngay lúc nói (歩いている, 住んでいる, 降っている)"},
            {"pos": "V tức thời (tự động từ)", "rule": "Trạng thái kết quả còn lưu giữ (電車が止まっている, 窓が開いている, 乾いている, 並んでいる)"},
            {"pos": "V lặp lại / Nghề nghiệp", "rule": "Thói quen, nghề nghiệp, xu hướng hiện tại (毎日散歩している, 増えている)"},
        ],
        "core_meaning_vi": "Diễn tả hành động đang diễn tiến, thói quen lặp lại, hoặc trạng thái kết quả sau khi sự việc xảy ra",
        "deep_explanation_vi": (
            "Người Việt thường chỉ hiểu ～ている là 'đang...'. Nhưng trong 70% câu Đọc hiểu và Từ vựng N3, "
            "khi ～ている gắn với động từ tức thời/tự động từ (止まる, 乾く, 並ぶ, 似る, 減る, 結婚する, 知る), nó chỉ TRẠNG THÁI HIỆN TẠI sau khi hành động đã xảy ra ('tàu đang bị dừng', 'cổ đang khô', 'giống bố', 'chưa kết hôn'). "
            "Lưu ý đặc biệt với 知る: khẳng định dùng 知っている (biết), phủ định dùng 知らない (không biết, chứ ít dùng 知っていない)."
        ),
        "register_tag": "Trung tính (Cốt lõi)",
        "confusable_pairs": [
            {
                "rival_pattern": "Tự động từ + ている vs Tha động từ + てある",
                "difference_vi": "Tự động từ + ている mô tả trạng thái tự nhiên hoặc kết quả khách quan (窓が開いている); Tha động từ + てある hàm ý có người cố ý làm sẵn (窓が開けてある).",
                "quick_test_vi": "Kiểm tra động từ gốc: 止まる/開く/乾く/並ぶ (tự động từ) -> ている; 作る/並べる/書く (tha động từ có chủ ý) -> てある.",
            }
        ],
        "examples": [
            {
                "jp": "乗っている電車が止まっている。",
                "reading_note": "のっているでんしゃがとまっている。",
                "vi": "Chuyến tàu tôi đang đi hiện đang bị dừng lại.",
                "grammar_note": "乗っている (đang ngồi trên tàu) và 止まっている (tự động từ chỉ trạng thái tàu đang đứng yên).",
            },
            {
                "jp": "空気も乾いていますし、風も強く吹いています。",
                "reading_note": "くうきもかわいていますし、かぜもつよくふいています。",
                "vi": "Không khí cũng đang khô hanh và gió cũng đang thổi mạnh.",
                "grammar_note": "乾いている chỉ trạng thái hanh khô hiện hữu; 吹いている chỉ hành động đang diễn ra.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 | Đề .xlsx (Q24, Q69, Q72, Q119, Q120)",
        "search_keywords": "te iru tiep dien trang thai ket qua ている 止まっている",
        "match_patterns": ["ている", "ています", "ていない"],
    },
    {
        "code": "GP-N5-09",
        "pattern": "Trải nghiệm Vたことがある & Lời khuyên Vた/Vないほうがいい",
        "jlpt_level": "N5",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": True,
        "formation_formula": "Vた + ことがある (Đã từng) | Vた / Vない + ほうがいい (Nên / Không nên)",
        "formation_table": [
            {"pos": "Trải nghiệm quá khứ", "rule": "Vた + ことがある / ことがない (phủ định tuyệt đối: chưa từng một lần nào)"},
            {"pos": "Lời khuyên nên làm", "rule": "Vた + ほうがいい (Nên làm V hơn; tránh dùng Vる nếu khuyên cụ thể)"},
            {"pos": "Lời khuyên không nên", "rule": "Vない + ほうがいい (Không nên làm V thì hơn)"},
        ],
        "core_meaning_vi": "Nói về kinh nghiệm đã từng trải qua (Vたことがある) và khuyên phương án tối ưu (Vたほうがいい)",
        "deep_explanation_vi": (
            "Hai mẫu này cực kỳ dễ bị nhầm với 2 mẫu N3 sát nghĩa: "
            "1) Vたことがある (đã từng trải qua trong quá khứ) hoàn toàn khác Vることがある (thỉnh thoảng có lúc xảy ra — như trong Q#156). Chỉ thay đổi thì Vた vs Vる là đổi hẳn ý nghĩa! "
            "2) Vたほうがいい dùng để khuyên giữa các lựa chọn thực tế (như '必要以上にマグロを捕るのをやめたほうがいい' trong Q#34), nhẹ nhàng hơn nghĩa vụ đạo đức ～べきだ."
        ),
        "register_tag": "Trung tính (Hội thoại & Nghị luận)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vたことがある vs Vることがある",
                "difference_vi": "Vたことがある = kinh nghiệm đã từng làm ít nhất 1 lần trong đời; Vることがある = tần suất thỉnh thoảng có lúc xảy ra.",
                "quick_test_vi": "Thấy thì quá khứ Vた -> trải nghiệm; thấy nguyên thể Vる -> tần suất thỉnh thoảng.",
            }
        ],
        "examples": [
            {
                "jp": "スペイン語は全然勉強したことがありません。",
                "reading_note": "すぺいんごはぜんぜんべんきょうしたことがありません。",
                "vi": "Tiếng Tây Ban Nha thì tôi hoàn toàn chưa từng học bao giờ.",
                "grammar_note": "Vた + ことがありません khẳng định chưa có kinh nghiệm học trước đây.",
            },
            {
                "jp": "必要以上にマグロを捕るのをやめたほうがいい。",
                "reading_note": "ひつよういじょうにまぐろをとるのをやめたほうがいい。",
                "vi": "Nên ngừng việc đánh bắt cá ngừ vượt quá mức cần thiết thì hơn.",
                "grammar_note": "Đưa ra giải pháp khuyên nhủ bằng Vた + ほうがいい.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 | 03_Grammar/Group_05 | Đề .xlsx (Q34, Q160)",
        "search_keywords": "ta koto ga aru ta hou ga ii trai nghiem loi khuyen たことがある ほうがいい",
        "match_patterns": ["たことがある", "たことがありません", "たほうがいい", "ないほうがいい"],
    },
    {
        "code": "GP-N5-10",
        "pattern": "Yêu cầu & Cấm đoán ～てください / ～ないでください / ～てはいけない",
        "jlpt_level": "N5",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": True,
        "formation_formula": "Vて + ください (Hãy làm) | Vない + でください (Xin đừng) | Vて + はいけない (Không được phép)",
        "formation_table": [
            {"pos": "Đề nghị lịch sự", "rule": "Vて + ください (phần hướng dẫn dùng おVください / ごNください)"},
            {"pos": "Cấm đoán nhẹ / Nhắc nhở", "rule": "Vない + でください (chú ý giữ nguyên ない, bỏ い? Không: Vない + でください)"},
            {"pos": "Cấm quy tắc", "rule": "Vて + はいけない / はいけません / てはだめ"},
        ],
        "core_meaning_vi": "Đưa ra chỉ dẫn thực hiện, nhắc nhở tránh làm và quy tắc cấm đoán",
        "deep_explanation_vi": (
            "Đây là xương sống trong các bài Đọc hiểu thông báo, hướng dẫn sử dụng thuốc (Passage 1: 使用しないでください, 相談してください) và bài nghị luận (Passage 15: 軽く考えてはいけない). "
            "Ở N3, mẫu yêu cầu nhẹ nhàng gián tiếp sẽ nâng cấp lên Vる/Vない + ようにしてください."
        ),
        "register_tag": "Trung tính (Hội thoại & Hướng dẫn)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vないでください vs Vてはいけない",
                "difference_vi": "Vないでください là lời yêu cầu/nhắc người nghe đừng làm (hướng tới người nhận); Vてはいけない là quy tắc/khẳng định cấm đoán chung.",
                "quick_test_vi": "Trong tờ rơi hướng dẫn người dùng -> ないでください; trong bài nghị luận khuyên răn chân lý -> てはいけない.",
            }
        ],
        "examples": [
            {
                "jp": "同じところに続けて長く使用しないでください。",
                "reading_note": "おなじところにつづけてながくしようしないでください。",
                "vi": "Xin đừng sử dụng liên tục trong thời gian dài ở cùng một vị trí.",
                "grammar_note": "Vない + でください nêu điều cấm kỵ trực tiếp cho người dùng thuốc.",
            },
            {
                "jp": "「あいさつなんて」と軽く考えてはいけない。",
                "reading_note": "「あいさつなんて」とかるくかんがえてはいけない。",
                "vi": "Không được phép coi nhẹ kiểu 'chỉ là chào hỏi thôi mà'.",
                "grammar_note": "Vてはいけない nêu nguyên tắc nghiêm túc trong văn nghị luận.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 | 03_Grammar/Group_05 | Đề .xlsx (Passages 1, 15)",
        "search_keywords": "te kudasai naide kudasai te wa ikenai cam doan yeu cau てください ないでください てはいけない",
        "match_patterns": ["てください", "ないでください", "てはいけない"],
    },
    {
        "code": "GP-N5-11",
        "pattern": "Biểu đạt ý muốn Vたい & Mong cầu người khác Vてほしい",
        "jlpt_level": "N5",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": True,
        "formation_formula": "Vます(bỏ ます) + たい (Muốn tự làm) | Vて + ほしい / ほしくない (Muốn ai đó làm cho mình)",
        "formation_table": [
            {"pos": "Bản thân muốn làm", "rule": "Vます + たい (chia như tính từ い: たいです, たくない, たかった; ngôi 3 dùng たがる)"},
            {"pos": "Muốn người khác làm", "rule": "N(người)に + Vて + ほしい / てほしくない"},
            {"pos": "Muốn được phép làm", "rule": "Nâng cấp N3: V(sai khiến)て + ほしい (đổi chủ thể hành động sang chính mình)"},
        ],
        "core_meaning_vi": "Diễn đạt nguyện vọng bản thân muốn làm gì (たい) hoặc mong muốn người khác làm gì (てほしい)",
        "deep_explanation_vi": (
            "Lỗi kinh điển khi làm đề N3 (như Q#17: わたしにも読ませてほしい) là nhầm giữa Vてほしい và V(sai khiến)てほしい: "
            "[Aに Vてほしい] có nghĩa là tôi muốn A làm V cho tôi (ví dụ: 'bạn đọc cho tôi nghe' = 読んでほしい). "
            "Khi bạn muốn CHÍNH MÌNH được làm V ('cho tôi đọc với'), phải đổi động từ sang thể sai khiến rồi mới gắn てほしい -> 読ませてほしい. "
            "Ngoài ra, たい chỉ dùng cho ngôi 1 (hoặc hỏi ngôi 2); khi nói về mong muốn của ngôi 3 bắt buộc đổi thành たがっている (hoặc たいと思っている)."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vてほしい vs V(sai khiến)てほしい",
                "difference_vi": "Vてほしい = muốn người khác thực hiện hành động; V(sai khiến)てほしい = muốn người khác cho phép mình thực hiện hành động.",
                "quick_test_vi": "Thấy 'わたしにも' (cho tôi cũng...) đứng trước chỗ trống? Bắt buộc dùng thể sai khiến + てほしい.",
            }
        ],
        "examples": [
            {
                "jp": "父の仕事を手伝いたいと思った。",
                "reading_note": "ちちのしごとをてつだいたいとおもった。",
                "vi": "Tôi nghĩ muốn phụ giúp công việc của bố.",
                "grammar_note": "Mong muốn của bản thân người nói dùng Vます + たい.",
            },
            {
                "jp": "年を取った親にはもう無理をしてほしくない。",
                "reading_note": "としをとったおやにはもうむりをしてほしくない。",
                "vi": "Tôi không muốn bố mẹ đã lớn tuổi còn phải làm việc quá sức nữa.",
                "grammar_note": "Mong muốn người khác (bố mẹ) không làm gì dùng Vて + ほしくない.",
            },
        ],
        "source_ref": "Shin-N3-List #42 | Đề .xlsx (Q17, Passage 13)",
        "search_keywords": "tai te hoshii mong muon y nguyen たい てほしい",
        "match_patterns": ["てほしい", "てほしくない", "たいと思"],
    },
    {
        "code": "GP-N5-12",
        "pattern": "Động từ Cho & Nhận cơ bản あげる・もらう・くれる",
        "jlpt_level": "N5",
        "category": "keigo",
        "category_label_vi": CATEGORY_LABELS["keigo"],
        "in_exam_corpus": True,
        "formation_formula": "[Cho]は [Nhận]に V/Nを あげる | [Nhận]は [Cho]に/から V/Nを もらう | [Cho]は わたしに V/Nを くれる",
        "formation_table": [
            {"pos": "あげる / さしあげる", "rule": "Tôi/người khác cho đối tượng ngang hoặc dưới (không dùng khi người ngoài cho mình)"},
            {"pos": "くれる / くださる", "rule": "Người khác cho TÔI hoặc người thân trong gia đình tôi (trợ từ chủ ngữ là người cho)"},
            {"pos": "もらう / いただく", "rule": "Tôi (hoặc người nhận) nhận được từ người khác (chủ ngữ là người nhận)"},
        ],
        "core_meaning_vi": "Xác định đúng chiều di chuyển của hành động/vật phẩm theo điểm nhìn 'trong - ngoài' (Uchi-Soto)",
        "deep_explanation_vi": (
            "Đây là phần khiến người học tiếng Nhật mất điểm nhiều nhất trong cả Ngữ pháp lẫn Đọc hiểu. "
            "Khi nhân vật 'tôi' được người khác giúp đỡ (gói hộp bánh giúp, giải thích cho nghe, làm dịu cái nóng), tiếng Nhật BẮT BUỘC dùng くれる / くださる (với chủ ngữ là người giúp) hoặc もらう / いただく (với chủ ngữ là người được giúp). "
            "Tuyệt đối không dùng あげる cho hướng người ngoài tác động vào mình."
        ),
        "register_tag": "Trung tính & Lịch sự",
        "confusable_pairs": [
            {
                "rival_pattern": "くれる vs もらう",
                "difference_vi": "Cả hai đều chỉ chiều 'người ngoài -> mình', nhưng くれる lấy NGƯỜI CHO làm chủ ngữ (は/が), còn もらう lấy NGƯỜI NHẬN làm chủ ngữ (は/が).",
                "quick_test_vi": "Nhìn chủ ngữ có は/が (hoặc bị ẩn): nếu là đối phương/vật giúp mình -> くれる; nếu là 'tôi' nhận -> もらう.",
            }
        ],
        "examples": [
            {
                "jp": "花屋さんはきれいな紙で箱を包み、リボンをつけてくれた。",
                "reading_note": "はなやさんはきれいなかみではこをつつみ、りぼんをつけてくれた。",
                "vi": "Tiệm hoa đã gói hộp bằng giấy đẹp và thắt nơ giúp tôi.",
                "grammar_note": "Người thực hiện là tiệm hoa giúp nhân vật 'tôi' nên cuối câu dùng てくれた.",
            },
            {
                "jp": "イグサは蒸し暑さを弱めてくれます。",
                "reading_note": "いぐさはむしあつさをよわめてくれます。",
                "vi": "Cỏ Igusa giúp làm dịu cái nóng ẩm cho chúng ta.",
                "grammar_note": "Dùng てくれます mang sắc thái biết ơn lợi ích mà thiên nhiên/vật liệu mang lại.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 | Đề .xlsx (Passages 8, 18)",
        "search_keywords": "cho nhan ageru morau kureru kudasaru itadaku あげる もらう くれる",
        "match_patterns": ["てくれた", "てくれます", "てもら", "ていただ", "てあげ"],
    },
    {
        "code": "GP-N5-13",
        "pattern": "Liên kết nguyên nhân cơ bản ～から / ～ので",
        "jlpt_level": "N5",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": True,
        "formation_formula": "普通形 / 丁寧形 + から | 普通形 (Aな+な / N+な) + ので",
        "formation_table": [
            {"pos": "～から (Nguyên nhân chủ quan)", "rule": "Chấp nhận cả です・ます lẫn thể thông thường; vế sau thường là ý chí, mệnh lệnh, phỏng đoán"},
            {"pos": "～ので (Nguyên nhân khách quan)", "rule": "Danh từ/Tính từ な thêm な + ので (雨なので, 急いでいるので); sắc thái mềm, khách quan"},
            {"pos": "Đuôi giải thích ～からだ / ～のです", "rule": "Đặt cuối câu để giải thích lý do cho câu hỏi hoặc nhận định trước đó"},
        ],
        "core_meaning_vi": "Nối mệnh đề nguyên nhân - kết quả ở mức cơ bản (chủ quan với から, khách quan lịch sự với ので)",
        "deep_explanation_vi": (
            "Ở N3, hai từ nối này làm nền cho sự phân tách sắc thái nguyên nhân nâng cao (～せいで xấu, ～おかげで tốt, ～ことから căn cứ, ～ものだから thanh minh). "
            "Lưu ý hình thái: với danh từ và tính từ な, trước から dùng だ (hoặc です), còn trước ので BẮT BUỘC dùng な (ví dụ: 無香料なので, 急いでいたので). "
            "Trong Đọc hiểu, đuôi câu ～からです là tín hiệu trực tiếp giải thích câu hỏi 'Tại sao?' (どうしてか)."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "N/Aな + だから vs N/Aな + なので",
                "difference_vi": "Sau N/Aな dùng だ trước から, nhưng phải đổi thành な trước ので.",
                "quick_test_vi": "Kiểm tra nối sau danh từ: だから (đúng) / なから (sai); なので (đúng) / だので (sai).",
            }
        ],
        "examples": [
            {
                "jp": "無香料なので、においを気にせず使用できます。",
                "reading_note": "むこうりょうなので、においをきにせずしようできます。",
                "vi": "Vì không có hương liệu nên có thể dùng mà không phải lo lắng về mùi.",
                "grammar_note": "無香料 (danh từ) kết nối bằng なので để nêu nguyên nhân khách quan.",
            },
            {
                "jp": "これは、月にある黒っぽい模様がウサギに見えるからです。",
                "reading_note": "これは、つきにあるくろっぽいもようがうさぎにみえるからです。",
                "vi": "Đó là vì hoa văn hơi đen trên mặt trăng trông giống con thỏ.",
                "grammar_note": "Cấu trúc 'これは～からです' chuyên dùng ở câu 2 để giải thích cho nhận định câu 1.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 | Đề .xlsx (Passages 1, 5, 18)",
        "search_keywords": "nguyen nhan kara node na node karada から ので からです",
        "match_patterns": ["なので", "からです", "ますから"],
    },
    {
        "code": "GP-N5-14",
        "pattern": "Liệt kê hành động & lý do Vたり～たりする / ～し～し",
        "jlpt_level": "N5",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": True,
        "formation_formula": "Vた + り、Vた + りする | 普通形 (N/Aな + だ) + し、～し",
        "formation_table": [
            {"pos": "Vたり～たりする", "rule": "Liệt kê đại diện 2-3 hành động không theo thứ tự (nhấn mạnh 'làm những việc như...'). Chia thì ở động từ する cuối câu!"},
            {"pos": "～し、～し", "rule": "Liệt kê nhiều đặc điểm hoặc nhiều nguyên nhân cộng dồn dẫn đến kết luận vế sau"},
            {"pos": "Lưu ý chia たり với Aい/Aな", "rule": "Aい -> Aかったり; Aな/N -> だったり (ví dụ: 大きかったり小さかったり)"},
        ],
        "core_meaning_vi": "Liệt kê tiêu biểu hành động/trạng thái không cố định (たり) và cộng dồn nhiều lý do song song (し)",
        "deep_explanation_vi": (
            "Lỗi sai phổ biến của người mới lên N3 là dùng Vたり mà quên động từ する ở cuối, hoặc dùng Vて～Vて (trình tự thời gian) thay cho Vたり～たり (liệt kê mẫu ngẫu nhiên). "
            "Trong Đọc hiểu, mẫu ～し～し báo hiệu đáp án đúng phải gom đủ cả hai lý do được tác giả liệt kê (tương tự từ nối それに trong Q#31 và Passage 4)."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vて、Vて vs Vたり、Vたりする",
                "difference_vi": "Vて～Vて là chuỗi hành động nối tiếp theo trình tự thời gian; Vたり～たりする là liệt kê ví dụ đại diện trong nhiều việc.",
                "quick_test_vi": "Nếu có 'tôi xem phim, nghe nhạc, đọc sách...' (không theo thứ tự cố định) -> dùng たり～たりする.",
            }
        ],
        "examples": [
            {
                "jp": "最近はコンピューターが使えたり、外国語が話せたりすることが大事にされている。",
                "reading_note": "さいきんはこんぴゅーたーがつかえたり、がいこくごがはなせたりすることがだいじにされている。",
                "vi": "Gần đây những năng lực như dùng máy tính hay nói ngoại ngữ được coi trọng.",
                "grammar_note": "Thể khả năng chia quá khứ + り (使えたり・話せたり) để liệt kê ví dụ tiêu biểu.",
            },
            {
                "jp": "今の日本には安い寿司屋がたくさんあるし、スーパーでも売っている。",
                "reading_note": "いまのにほんにはやすいすしやがたくさんあるし、すーぱーでもうっている。",
                "vi": "Ở Nhật hiện nay vừa có nhiều quán sushi rẻ, lại vừa bán cả ở siêu thị.",
                "grammar_note": "Nối 2 nguyên nhân dẫn tới việc dễ ăn sushi bằng し.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 | Đề .xlsx (Passages 2, 4, 9)",
        "search_keywords": "liet ke tari tari shi shi たり し",
        "match_patterns": ["たり、", "たりする", "あるし"],
    },
    {
        "code": "GP-N5-15",
        "pattern": "Liên từ cơ bản しかし・けれども・それに・それで・それから",
        "jlpt_level": "N5",
        "category": "discourse",
        "category_label_vi": CATEGORY_LABELS["discourse"],
        "in_exam_corpus": True,
        "formation_formula": "[Câu 1]。Liên từ、[Câu 2]。",
        "formation_table": [
            {"pos": "Đối lập (Tuy nhiên)", "rule": "しかし (văn viết/trang trọng), けれども / けれど (mềm mại hơn), でも (khẩu ngữ)"},
            {"pos": "Bổ sung (Hơn nữa)", "rule": "それに (thêm luận cứ cùng chiều), また (ngoài ra), それから (tiếp theo là)"},
            {"pos": "Nhân quả (Vì vậy)", "rule": "それで (hội thoại/kể chuyện), ですから / だから (vì thế nên)"},
        ],
        "core_meaning_vi": "Nhóm liên từ đầu câu định hướng mạch lập luận: đối lập (しかし), cộng dồn (それに), tuần tự (それから), kết quả (それで)",
        "deep_explanation_vi": (
            "Đây là nhóm biển báo quan trọng nhất trong Đọc hiểu ngắn/trung và Đục lỗ 問題3. "
            "Quy tắc vàng trong Đọc hiểu Kosei & Đề .xlsx: 1) Chủ trương thật của tác giả gần như luôn nằm ngay SAU chữ しかし / けれども (Q#30). "
            "2) Khi tác giả dùng それに để thêm lý do thứ hai, đáp án đúng BẮT BUỘC phải chứa đủ cả hai lý do (Q#31). "
            "3) Trong Đục lỗ (Q#49, Q#62), phải phân biệt rạch ròi nhân quả (それで・ですから・そのため) với giải thích khái niệm (つまり) và thứ tự liệt kê (それから)."
        ),
        "register_tag": "Trung tính & Văn viết",
        "confusable_pairs": [
            {
                "rival_pattern": "それで / ですから vs それから vs それに",
                "difference_vi": "それで/ですから = kết quả suy ra từ câu trước; それから = bước tiếp theo hoặc liệt kê thêm; それに = bổ sung thêm lý do cùng chiều.",
                "quick_test_vi": "Kiểm tra quan hệ giữa 2 câu: Nếu câu 1 là nguyên nhân -> それで/ですから; nếu đánh số 'まず…' trước -> それから; nếu cộng thêm lý do -> それに.",
            }
        ],
        "examples": [
            {
                "jp": "しかし、他の科目も重要であることは変わらない。",
                "reading_note": "しかし、ほかのかもくもじゅうようであることはかわらない。",
                "vi": "Tuy nhiên, việc các môn học khác cũng quan trọng là điều không thay đổi.",
                "grammar_note": "しかし lật ngược ý kiến phổ biến ở câu trước để chốt luận điểm của tác giả.",
            },
            {
                "jp": "それに、大きな音を聞き続けると、小さい音が聞こえにくくなる。",
                "reading_note": "それに、おおきなおとをききつづけると、ちいさいおとがきこえにくくなる。",
                "vi": "Hơn nữa, nếu tiếp tục nghe âm thanh lớn thì sẽ khó nghe thấy âm thanh nhỏ.",
                "grammar_note": "それに bổ sung luận cứ thứ 2 (hỏng tai) bên cạnh luận cứ 1 (nguy hiểm giao thông).",
            },
        ],
        "source_ref": "Kosei Đọc hiểu | Đề .xlsx (Q29, Q30, Q31, Q49, Q62)",
        "search_keywords": "lien tu shikashi keredomo soreni sorede sorekara しかし けれども それに それで それから",
        "match_patterns": ["しかし", "けれども", "それに、", "それで", "それから", "ですから"],
    },
    {
        "code": "GP-N5-16",
        "pattern": "Phỏng đoán cơ bản ～かもしれない / ～でしょう・だろう",
        "jlpt_level": "N5",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": True,
        "formation_formula": "普通形 (Aな / N bỏ だ) + かもしれない | 普通形 (Aな / N bỏ だ) + でしょう / だろう",
        "formation_table": [
            {"pos": "～かもしれない (~40-50%)", "rule": "Có lẽ, biết đâu chừng (không chắc chắn; Aな/N không có だ: 雨かもしれない)"},
            {"pos": "～でしょう / だろう (~70-80%)", "rule": "Chắc là, có lẽ là (suy đoán có cơ sở hoặc làm mềm câu khẳng định)"},
            {"pos": "～ていくだろう / ～のだろう", "rule": "Kết hợp thì tiếp diễn hoặc giải thích (が使われていくでしょう, 必要なのだろう)"},
        ],
        "core_meaning_vi": "Đo lường độ chắc chắn khi phỏng đoán (かもしれない: có thể xảy ra; でしょう/だろう: chắc là)",
        "deep_explanation_vi": (
            "Độ chắc chắn trong Đọc hiểu N3 quyết định đáp án đúng hay sai: khi bài văn dùng ～かもしれない (như 'マグロがいなくなってしまうかもしれない', '一生が変ってしまうかもしれない'), đáp án nào đổi thành 必ず (chắc chắn 100%) là bẫy sai ngay lập tức (Q#143). "
            "Lưu ý hình thái: cả かもしれない lẫn でしょう/だろう đều bỏ だ sau danh từ và tính từ な."
        ),
        "register_tag": "Trung tính (Phỏng đoán)",
        "confusable_pairs": [
            {
                "rival_pattern": "～かもしれない vs ～に違いない / ～必ず",
                "difference_vi": "かもしれない chỉ khả năng có thể xảy ra (~50%), không khẳng định chắc; に違いない / 必ず khẳng định độ tin cậy rất cao (~90-100%).",
                "quick_test_vi": "Trong câu đọc hiểu thấy かもしれない thì loại ngay các phương án chứa 必ず hoặc 絶対に.",
            }
        ],
        "examples": [
            {
                "jp": "このままでは、将来マグロがいなくなってしまうかもしれない。",
                "reading_note": "このままでは、しょうらいまぐろがいなくなってしまうかもしれない。",
                "vi": "Nếu cứ thế này, trong tương lai cá ngừ có thể sẽ biến mất.",
                "grammar_note": "Cảnh báo khả năng rủi ro ở mức phán đoán chưa chắc chắn 100%.",
            },
            {
                "jp": "これからの日本の家に使われていくでしょう。",
                "reading_note": "これからのにほんのいえにつかわれていくでしょう。",
                "vi": "Chắc sẽ tiếp tục được sử dụng trong những ngôi nhà Nhật tương lai.",
                "grammar_note": "Vられる + ていく + でしょう diễn đạt dự đoán xu hướng tương lai mềm mại.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 | Đề .xlsx (Q143, Q152, Passage 4)",
        "search_keywords": "kamoshirenai deshou darou phong doan かもしれない でしょう だろう",
        "match_patterns": ["かもしれない", "でしょう", "だろう"],
    },
    {
        "code": "GP-N5-17",
        "pattern": "Giới hạn phạm vi ～だけ vs ～しか～ない",
        "jlpt_level": "N5",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": True,
        "formation_formula": "N / Vる + だけ (Chỉ...) | N / Vる + しか + Động từ/Tính từ PHỦ ĐỊNH (Chỉ... thôi, không hơn)",
        "formation_table": [
            {"pos": "～だけ", "rule": "Đi với cả khẳng định lẫn phủ định (少しだけ食べる; それだけではない); sắc thái trung tính"},
            {"pos": "～しか～ない", "rule": "BẮT BUỘC cuối câu phải ở dạng phủ định (しかできません); sắc thái chê ít, không đủ"},
            {"pos": "Lưu ý với trợ từ", "rule": "が và を thường lược bỏ trước だけ/しか (あいさつぐらいしかできない)"},
        ],
        "core_meaning_vi": "Giới hạn số lượng/phạm vi 'chỉ': だけ mang tính trung tính, còn しか～ない nhấn mạnh sự ít ỏi ngoài mong đợi",
        "deep_explanation_vi": (
            "Đây là bẫy thường xuyên cài vào đề 問題1 và 問題3 (như Q#52, Q#154). "
            "Khi kiểm tra 4 phương án, nếu thấy cuối câu ở thể KHẲNG ĐỊNH (ví dụ 探していたものだ trong Q#52) thì しか bị loại ngay 100% vì しか bắt buộc hô ứng với phủ định ～ない. "
            "Ngược lại trong câu phủ định có từ 'ngay cả một chút cũng...' (言葉さえできなくても trong Q#154), nếu chọn しか sẽ làm méo nghĩa câu thành 'nếu chỉ nói được tiếng thôi'."
        ),
        "register_tag": "Trung tính",
        "confusable_pairs": [
            {
                "rival_pattern": "～だけ vs ～しか～ない",
                "difference_vi": "だけ dùng tự do với câu khẳng định; しか BẮT BUỘC đi kèm vị ngữ phủ định và mang sắc thái 'chỉ có bấy nhiêu (ít ỏi)'.",
                "quick_test_vi": "Nhìn cuối câu trước: không có ない/ません/できない -> loại thẳng しか!",
            }
        ],
        "examples": [
            {
                "jp": "僕はあいさつぐらいしかドイツ語はできません。",
                "reading_note": "ぼくはあいさつぐらいしかどいつごはできません。",
                "vi": "Tôi chỉ nói được tiếng Đức ở mức chào hỏi thôi.",
                "grammar_note": "しか hô ứng chặt với できません để nhấn mạnh vốn từ rất ít.",
            },
            {
                "jp": "日本文化に関することだけです。",
                "reading_note": "にほんぶんかにかんすることだけです。",
                "vi": "Chỉ là những điều liên quan đến văn hóa Nhật Bản thôi.",
                "grammar_note": "Câu khẳng định です chỉ được dùng だけ, không dùng しか.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 | Đề .xlsx (Q26, Q52, Q154)",
        "search_keywords": "shika dake chi gioi han しか だけ",
        "match_patterns": ["しか", "だけです", "だけ"],
    },
    {
        "code": "GP-N5-18",
        "pattern": "Cặp Tự động từ (が) vs Tha động từ (を)",
        "jlpt_level": "N5",
        "category": "conjugation",
        "category_label_vi": CATEGORY_LABELS["conjugation"],
        "in_exam_corpus": True,
        "formation_formula": "[Chủ thể] が Tự động từ (trạng thái tự biến đổi) | [Chủ thể] は [Tân ngữ] を Tha động từ (hành động tác động)",
        "formation_table": [
            {"pos": "Cặp âm -aru / -eru", "rule": "決まる(が) <-> 決める(を); 集まる <-> 集める; 混ざる <-> 混ぜる; 上がる <-> 上げる"},
            {"pos": "Cặp âm -u / -eru", "rule": "開く(あく) <-> 開ける; 建つ <-> 建てる; 焼ける <-> 焼く; 並ぶ <-> 並べる"},
            {"pos": "Cặp âm -reru / -su", "rule": "倒れる <-> 倒す; 壊れる <-> 壊す; 汚れる <-> 汚す"},
        ],
        "core_meaning_vi": "Phân biệt động từ tự diễn biến không cần tân ngữ (が) với động từ có chủ ý tác động lên đối tượng (を)",
        "deep_explanation_vi": (
            "Đây là điểm giao thoa trực tiếp giữa Từ vựng 問題3/問題5 và Ngữ pháp N4->N3. "
            "Trong đề thi (như Q#41: 男女がまざって vs たまごと牛乳をまぜて trong Q#135, Q#86: 魚を焼いて, Q#120: 風が吹いて), "
            "chỉ cần soi đúng trợ từ が hay を liền trước động từ là loại ngay được cặp nhiễu đồng nghĩa."
        ),
        "register_tag": "Trung tính (Cốt lõi)",
        "confusable_pairs": [
            {
                "rival_pattern": "混ざる (が) vs 混ぜる (を)",
                "difference_vi": "混ざる là tự động từ (các đối tượng tự hòa lẫn vào nhau với が); 混ぜる là tha động từ (người trộn A với B bằng を).",
                "quick_test_vi": "Thấy danh từ + が ngay trước chỗ trống -> chọn tự động từ 混ざる; thấy danh từ + を -> chọn 混ぜる.",
            }
        ],
        "examples": [
            {
                "jp": "男女が混ざってサッカーをした。",
                "reading_note": "だんじょがまざってさっかーをした。",
                "vi": "Nam và nữ cùng hòa chung chơi bóng đá.",
                "grammar_note": "Chủ ngữ 男女が đi với tự động từ 混ざる.",
            },
            {
                "jp": "たまごと牛乳をよく混ぜてください。",
                "reading_note": "たまごとぎゅうにゅうをよくまぜてください。",
                "vi": "Hãy trộn đều trứng và sữa vào nhau.",
                "grammar_note": "Tân ngữ đi với を bắt buộc dùng tha động từ 混ぜる.",
            },
        ],
        "source_ref": "Giáo trình N4->N3 | Đề .xlsx (Q41, Q86, Q119, Q120, Q135)",
        "search_keywords": "tu dong tu tha dong tu jidoushi tadoushi 混ざる 混ぜる 焼く",
        "match_patterns": ["が混ざ", "を混ぜ", "が乾燥", "が強く吹", "を焼いて"],
    },

    # =========================================================================
    # JLPT N4 BRIDGE (GP-N4-01 .. GP-N4-24)
    # =========================================================================
    {
        "code": "GP-N4-01",
        "pattern": "Thể Khả năng Vえる / Vられる",
        "jlpt_level": "N4",
        "category": "conjugation",
        "category_label_vi": CATEGORY_LABELS["conjugation"],
        "in_exam_corpus": True,
        "formation_formula": "V1(đổi cột う -> cột え + る) | V2(bỏ る + られる) | V3(する->できる, 来る->こられる)",
        "formation_table": [
            {"pos": "Nhóm 1", "rule": "読む->読める, 書く->書ける, 弾く->弾ける, 話す->話せる, 買う->買える"},
            {"pos": "Nhóm 2", "rule": "食べる->食べられる, 見る->見られる, 寝る->寝られる (khẩu ngữ hay lược ら thành 食べれる - tránh dùng trong thi viết JLPT)"},
            {"pos": "Nhóm 3", "rule": "する -> できる; 来る(くる) -> こられる"},
            {"pos": "Trợ từ đi kèm", "rule": "Tân ngữ chuyển từ を thành が (ピアノが弾ける, 日本語が話せる); tự nó chia như động từ V2"},
        ],
        "core_meaning_vi": "Diễn tả năng lực bản thân có thể làm gì hoặc điều kiện hoàn cảnh cho phép làm gì",
        "deep_explanation_vi": (
            "Thể khả năng là cửa ngõ bắt buộc trước khi bước vào N3. "
            "Điểm mấu chốt sư phạm: bản thân thể khả năng là động từ KHÔNG Ý CHÍ (chỉ năng lực/trạng thái có thể), do đó: "
            "1) Khi kết hợp chỉ mục đích, BẮT BUỘC đi với ように (読めるように), CẤM tuyệt đối đi với ために (*読めるために trong Q#27 là bẫy sai ngữ pháp kinh điển). "
            "2) Trợ từ tân ngữ thường dùng が thay cho を."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "V2 られる (Khả năng) vs V2 られる (Bị động)",
                "difference_vi": "Hình thái giống hệt nhau (見られる, 食べられる), phân biệt bằng trợ từ: Khả năng đi với が/を (tân ngữ); Bị động đi với [Aは Bに Vられる].",
                "quick_test_vi": "Nếu có người tác động đứng trước に (先生に注意される) -> Bị động; nếu nói năng lực/cơ hội -> Khả năng.",
            }
        ],
        "examples": [
            {
                "jp": "必要なときに読めるように、大切にしまっておいてください。",
                "reading_note": "ひつようなときによめるように、たいせつにしまっておいてください。",
                "vi": "Hãy cất giữ cẩn thận để có thể đọc được vào lúc cần thiết.",
                "grammar_note": "読む -> 読める (khả năng V1) kết hợp ように.",
            },
            {
                "jp": "ピアノばかりでなくバイオリンもひけるなんて、すごいですね。",
                "reading_note": "ぴあのばかりでなくばいおりんもひけるなんて、すごいですね。",
                "vi": "Không chỉ piano mà còn chơi được cả violin nữa, thật giỏi quá.",
                "grammar_note": "弾く(ひく) -> 弾ける(ひける) là thể khả năng nhóm 1.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 (Trang 5) | Đề .xlsx (Q18, Q27, Q60)",
        "search_keywords": "the kha nang kanoukei Vえる Vられる 読める ひける できる",
        "match_patterns": ["読める", "ひける", "話せる", "使える", "できな"],
    },
    {
        "code": "GP-N4-02",
        "pattern": "Thể Sai khiến Vさせる / Vあせる",
        "jlpt_level": "N4",
        "category": "passive_causative",
        "category_label_vi": CATEGORY_LABELS["passive_causative"],
        "in_exam_corpus": True,
        "formation_formula": "V1(đổi cột う -> cột あ + せる) | V2(bỏ る + させる) | V3(する->させる, 来る->こさせる)",
        "formation_table": [
            {"pos": "Nhóm 1", "rule": "読む->読ませる, 行く->行かせる, 待つ->待たせる, 買う->買わせる (đuôi う -> わ + せる)"},
            {"pos": "Nhóm 2", "rule": "食べる->食べさせる, 覚える->覚えさせる, 見る->見させる"},
            {"pos": "Nhóm 3", "rule": "する -> させる (学習させる, 留学させる, 成功させる); 来る -> こさせる"},
            {"pos": "Trợ từ người thực hiện", "rule": "Nếu là tự động từ: [Người bị sai] を; Nếu là tha động từ có sẵn を: [Người bị sai] に"},
        ],
        "core_meaning_vi": "Bắt buộc ai làm gì (cưỡng ép) hoặc cho phép ai làm gì (tạo điều kiện)",
        "deep_explanation_vi": (
            "Thể sai khiến mang 2 sắc thái trái ngược tùy ngữ cảnh: "
            "(1) Bắt/sai bảo/làm cho ai làm (như 留学させてくれた trong Q#126: cho tôi đi du học; 学習させる trong Passage 2: giúp học sinh học; 成功させる trong Passage 15: đưa bạn đến thành công). "
            "(2) Khi chia sang thể て + ほしい / ください / いただく (như 読ませてほしい trong Q#17), nó mang nghĩa 'xin phép cho tôi được làm'."
        ),
        "register_tag": "Trung tính",
        "confusable_pairs": [
            {
                "rival_pattern": "Vさせる (Sai khiến) vs Vられる (Bị động)",
                "difference_vi": "Sai khiến là chủ ngữ TÁC ĐỘNG khiến người khác làm (Aが Bに/を Vさせる); Bị động là chủ ngữ CHỊU tác động từ người khác (Bが Aに Vられる).",
                "quick_test_vi": "Nhìn chủ ngữ: người ra lệnh/gây ra -> Sai khiến; người hứng chịu -> Bị động.",
            }
        ],
        "examples": [
            {
                "jp": "留学させてくれた両親に、感謝しています。",
                "reading_note": "りゅうがくさせてくれたりょうしんに、かんしゃしています。",
                "vi": "Tôi luôn biết ơn bố mẹ đã cho tôi đi du học.",
                "grammar_note": "留学させる (cho phép đi du học) + てくれた (làm ơn cho mình).",
            },
            {
                "jp": "学校ではこれらをバランスよく学習させる工夫が必要だろう。",
                "reading_note": "がっこうではこれらをばらんすよくがくしゅうさせるくふうがひつようだろう。",
                "vi": "Ở trường học cần có phương pháp giúp học sinh học cân bằng các môn này.",
                "grammar_note": "学習する -> 学習させる (làm cho / giúp học sinh học).",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 (Trang 5) | Đề .xlsx (Q17, Q126, Passages 2, 15)",
        "search_keywords": "sai khien shieki saseru Vさせる 読ませて 学習させる 成功させる",
        "match_patterns": ["させて", "させる", "読ませて"],
    },
    {
        "code": "GP-N4-03",
        "pattern": "Thể Bị động Vられる / Vあれる",
        "jlpt_level": "N4",
        "category": "passive_causative",
        "category_label_vi": CATEGORY_LABELS["passive_causative"],
        "in_exam_corpus": True,
        "formation_formula": "V1(đổi cột う -> cột あ + れる) | V2(bỏ る + られる) | V3(する->される, 来る->こられる)",
        "formation_table": [
            {"pos": "Nhóm 1", "rule": "作る->作られる, 捕る->捕られる, 呼ぶ->呼ばれる, 買う->買われる (đuôi う -> わ + れる)"},
            {"pos": "Nhóm 2", "rule": "見る->見られる, ほめる->ほめられる, 育てる->育てられる"},
            {"pos": "Nhóm 3", "rule": "する -> される (禁止される, 逮捕される, 評価される); 来る -> こられる"},
            {"pos": "Tác nhân câu bị động", "rule": "Tác nhân là người: に; Tác nhân là vật/phương tiện/sáng tác: によって / から"},
        ],
        "core_meaning_vi": "Diễn tả chủ thể chịu tác động của hành động (bị động trực tiếp, bị động phiền toái, bị động khách quan)",
        "deep_explanation_vi": (
            "Câu bị động xuất hiện dày đặc trong văn bản khách quan, thông báo và bài đọc Đục lỗ N3 (như Q#56: 禁止されています; Q#148: 家がつくられてきました; Passage 4: 大量に捕られる; Passage 18: 和室と呼ばれています, 冷やされている). "
            "Khi chủ ngữ là vật vô tri đi với が/は (家がつくられる, 携帯電話の使用は禁止される), bắt buộc dùng bị động chứ không dùng chủ động."
        ),
        "register_tag": "Trung tính & Văn viết khách quan",
        "confusable_pairs": [
            {
                "rival_pattern": "Vられる (Bị động) vs Tha động từ + てある",
                "difference_vi": "Bị động nhấn mạnh quá trình hoặc hành động khách quan được thực hiện (bởi ai/từ xưa); てある chỉ kết quả tĩnh hiện đang bày ra trước mắt.",
                "quick_test_vi": "Có chủ ngữ hành động tự nhiên/lịch sử/quy định (昔から, 禁止, によって) -> Bị động.",
            }
        ],
        "examples": [
            {
                "jp": "日本では昔からこの気候に合わせた家がつくられてきました。",
                "reading_note": "にほんではむかしからこのきこうにあわせたいえがつくられてきました。",
                "vi": "Ở Nhật từ xưa đến nay những ngôi nhà hợp khí hậu này đã được xây dựng.",
                "grammar_note": "Chủ ngữ 家が kết hợp bị động つくられる + てきました.",
            },
            {
                "jp": "犯人は金を取りに現れたところを逮捕された。",
                "reading_note": "はんにんはかねをとりにあらわれたところをたいほされた。",
                "vi": "Tên tội phạm đã bị bắt ngay lúc xuất hiện để lấy tiền.",
                "grammar_note": "逮捕する -> 逮捕された (bị bắt giữ).",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 (Trang 5) | Đề .xlsx (Q42, Q56, Q148, Passages 4, 18)",
        "search_keywords": "bi dong ukemi rareru sareru Vられる されている つくられて 捕られる",
        "match_patterns": ["されています", "つくられて", "捕られる", "呼ばれて", "冷やされて", "逮捕された"],
    },
    {
        "code": "GP-N4-04",
        "pattern": "Thể Sai khiến Bị động Vさせられる / Vあされる",
        "jlpt_level": "N4",
        "category": "passive_causative",
        "category_label_vi": CATEGORY_LABELS["passive_causative"],
        "in_exam_corpus": True,
        "formation_formula": "V1(cột あ + される / せられる) | V2(bỏ る + させられる) | V3(する->させられる, 来る->こさせられる)",
        "formation_table": [
            {"pos": "Nhóm 1 (Rút gọn hay thi)", "rule": "待つ->待たされる (hoặc 待たせられる), 書く->書かされる, 行く->行かされる, 思う->思わせられる (riêng đuôi す giữ させられる: 話させられる)"},
            {"pos": "Nhóm 2", "rule": "食べる->食べさせられる, 覚える->覚えさせられる"},
            {"pos": "Nhóm 3", "rule": "する -> させられる (練習させられる); 来る -> こさせられる"},
        ],
        "core_meaning_vi": "Bị ép buộc phải làm hoặc tự nhiên bị gợi cảm xúc bất đắc dĩ",
        "deep_explanation_vi": (
            "Một trong những bẫy kinh điển của đề JLPT N3: phân biệt dạng rút gọn Nhóm 1 (行かされる = bị bắt đi, 待たされる = bị bắt đợi) với động từ Nhóm 1 đuôi す không được rút gọn (話させられる, không có *話さされる). "
            "Ngoài nghĩa bị người khác ép buộc, trong văn đọc hiểu (như Passage 3: 大丈夫かな、と思わせられることがある), Vさせられる diễn tả việc nhìn thấy cảnh tượng gì khiến người viết 'bất giác phải lo nghĩ/cảm thấy'."
        ),
        "register_tag": "Trung tính (Văn viết & Hội thoại)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vさせられる (Bị bắt làm) vs Vさせる (Bắt ai làm)",
                "difference_vi": "Vさせられる: chủ ngữ là NGƯỜI CHỊU ĐỰNG (私は母に練習させられた); Vさせる: chủ ngữ là NGƯỜI RA LỆNH (母は私に練習させた).",
                "quick_test_vi": "Thấy 'Ai đó に' + cảm giác ấm ức/bắt buộc -> Vさせられる.",
            }
        ],
        "examples": [
            {
                "jp": "歩行者を見ると、時々、大丈夫かな、と思わせられることがある。",
                "reading_note": "ほこうしゃをみると、ときどき、だいじょうぶかな、とおもわせられることがある。",
                "vi": "Nhìn người đi bộ vừa đeo tai nghe, thỉnh thoảng tôi bị khiến phải lo lắng không biết có ổn không.",
                "grammar_note": "思う -> 思わせられる diễn tả cảm xúc trỗi dậy một cách bị động.",
            },
            {
                "jp": "子どもの頃、母に毎日ピアノを練習させられた。",
                "reading_note": "こどものころ、ははにまいにちぴあのをれんしゅうさせられた。",
                "vi": "Hồi nhỏ tôi ngày nào cũng bị mẹ bắt luyện piano.",
                "grammar_note": "Người ép là 母に, người chịu là tôi -> 練習させられた.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 (Trang 5) | anki #25 | Đề .xlsx (Passage 3)",
        "search_keywords": "sai khien bi dong shieki ukemi saserareru させられる 思わせられる 待たされる",
        "match_patterns": ["させられ", "せられ", "あされ"],
    },
    {
        "code": "GP-N4-05",
        "pattern": "～ておく (Làm sẵn trước để chuẩn bị)",
        "jlpt_level": "N4",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": True,
        "formation_formula": "Vて + おく (Khẩu ngữ rút gọn: ～とく / ～どく)",
        "formation_table": [
            {"pos": "Chuẩn bị trước", "rule": "Làm sẵn để chuẩn bị cho sự việc sắp tới (予約しておく, しまっておく, 考えておく)"},
            {"pos": "Giữ nguyên hiện trạng", "rule": "Để tạm nguyên trạng thái có mục đích (開けておく, つけておく)"},
            {"pos": "Đi với yêu cầu lịch sự", "rule": "Vて + おいてください (Hãy làm sẵn đi nhé)"},
        ],
        "core_meaning_vi": "Thực hiện trước một hành động để chuẩn bị cho tương lai hoặc để nguyên một trạng thái có chủ đích",
        "deep_explanation_vi": (
            "Đừng nhầm ～ておく (chủ động làm sẵn, dùng với tha động từ) với ～てある (mô tả trạng thái kết quả đã được ai đó làm sẵn, đi với が). "
            "Trong đề thi (Passage 1: 大切にしまっておいてください; Q#68 distractor: 考えておくこと; Q#148 distractor: つくっておきました), "
            "nếu chủ ngữ là vật đi với tự động từ/bị động (家が...) thì CẤM dùng ～ておきました (loại ngay đáp án nhiễu 4 ở Q#148)."
        ),
        "register_tag": "Trung tính (Hội thoại & Hướng dẫn)",
        "confusable_pairs": [
            {
                "rival_pattern": "V(tha)ておく vs V(tha)てある",
                "difference_vi": "ておく nhấn mạnh HÀNH ĐỘNG chuẩn bị trước của chủ thể (tân ngữ đi với を); てある nhấn mạnh TRẠNG THÁI kết quả đang tồn tại (đối tượng đi với が).",
                "quick_test_vi": "Nếu là mệnh lệnh hãy làm sẵn (てください) hoặc có を -> ておく; nếu mô tả trạng thái hiện tại với が -> てある.",
            }
        ],
        "examples": [
            {
                "jp": "必要なときに読めるように、大切にしまっておいてください。",
                "reading_note": "ひつようなときによめるように、たいせつにしまっておいてください。",
                "vi": "Hãy cất giữ cẩn thận trước để lúc cần có thể đọc được.",
                "grammar_note": "しまう (cất đi) + ておく + ください: cất sẵn để sau này dùng.",
            },
            {
                "jp": "旅行の前に、ホテルを予約しておきました。",
                "reading_note": "りょこうのまえに、ほてるをよやくしておきました。",
                "vi": "Trước chuyến du lịch tôi đã đặt sẵn khách sạn rồi.",
                "grammar_note": "Hành động chủ động chuẩn bị trước khi đi.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 (Trang 4) | Đề .xlsx (Passage 1, Q68, Q148)",
        "search_keywords": "te oku chuan bi truoc ておく しまっておいて 考えておく",
        "match_patterns": ["ておく", "ておいて", "ておきま"],
    },
    {
        "code": "GP-N4-06",
        "pattern": "～てある (Trạng thái tồn tại kết quả có chủ ý)",
        "jlpt_level": "N4",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": True,
        "formation_formula": "N + が + V(tha động từ)て + ある / あります",
        "formation_table": [
            {"pos": "Điều kiện động từ", "rule": "BẮT BUỘC là Tha động từ (開ける, 書く, 並べる, 置く, 貼る); CẤM dùng tự động từ"},
            {"pos": "Trợ từ đối tượng", "rule": "Tân ngữ vốn dùng を chuyển thành が (hoặc は) để mô tả trạng thái hiện có"},
        ],
        "core_meaning_vi": "Mô tả kết quả của một hành động do ai đó cố ý làm trước vẫn đang hiện hữu trước mắt",
        "deep_explanation_vi": (
            "Đây là bẫy ngữ pháp xuất hiện trong Q#148 (つくってあります bị loại vì với mốc lịch sử '昔から' và chủ ngữ công trình mang tính tiếp diễn dài lâu, phải dùng bị động tiếp diễn つくられてきました). "
            "～てある chỉ dùng để miêu tả trạng thái tĩnh đã hoàn thành do chủ ý con người tại một thời điểm (như 机の上にメモが置いてある trong Passage 10: tờ giấy nhớ được đặt sẵn trên bàn)."
        ),
        "register_tag": "Trung tính (Mô tả hiện trạng)",
        "confusable_pairs": [
            {
                "rival_pattern": "V(tha)てある vs V(bị động)てきた",
                "difference_vi": "てある mô tả kết quả tĩnh hiện diện trước mắt (cái bàn có đặt tờ giấy); られてきた mô tả quá trình được làm lặp đi lặp lại từ xưa đến nay.",
                "quick_test_vi": "Thấy mốc thời gian '昔から' (từ xưa đến nay) -> chọn られてきた, loại てある.",
            }
        ],
        "examples": [
            {
                "jp": "木村さんの机の上に、先生からメモが置いてある。",
                "reading_note": "きむらさんのつくえのうえに、せんせいからめもがおいてある。",
                "vi": "Trên bàn của anh Kimura có đặt sẵn tờ lời nhắn từ thầy giáo.",
                "grammar_note": "置く (tha động từ) + てある mô tả trạng thái tờ giấy đang nằm sẵn trên bàn.",
            },
            {
                "jp": "壁に世界地図が貼ってあります。",
                "reading_note": "かべにせかいちずがはってあります。",
                "vi": "Trên tường có dán sẵn bản đồ thế giới.",
                "grammar_note": "貼る (dán - tha động từ) đi với 地図が và てあります.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 (Trang 4) | Đề .xlsx (Passage 10, Q148)",
        "search_keywords": "te aru trang thai co chu y てある 置いてある つくってあります",
        "match_patterns": ["てある", "てあります"],
    },
    {
        "code": "GP-N4-07",
        "pattern": "～てくる (Biến chuyển từ quá khứ đến nay / Bắt đầu xuất hiện)",
        "jlpt_level": "N4",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": True,
        "formation_formula": "Vて + くる / きた / きました",
        "formation_table": [
            {"pos": "Trục thời gian (Quá khứ -> Hiện tại)", "rule": "Đã và đang biến đổi/duy trì từ trước cho tới nay (減ってきている, つくられてきました, 育ってきた)"},
            {"pos": "Xuất hiện / Bắt đầu", "rule": "Hiện tượng hoặc cảm xúc bắt đầu nảy sinh tiến gần tới hiện tại (雨が降ってきた, わかってきた)"},
            {"pos": "Không gian (Làm rồi quay lại)", "rule": "Đi đâu làm gì rồi quay về chỗ cũ (ちょっと買ってくる)"},
        ],
        "core_meaning_vi": "Diễn tả sự biến đổi hoặc duy trì liên tục từ quá khứ tiến đến hiện tại, hoặc hiện tượng bắt đầu nảy sinh",
        "deep_explanation_vi": (
            "Đây là điểm ngữ pháp trọng tâm bậc nhất trong Đọc hiểu & Đục lỗ N3 (03_Grammar/Group_02, Q#148, Q#152, Passage 4). "
            "Khi thấy các từ chỉ mốc từ quá khứ tới nay như 昔から, だんだん, 今まで, 最近, động từ luôn gắn với ～てくる / ～てきている / ～てきた. "
            "Tuyệt đối tránh bẫy đảo chiều thời gian với ～ていく (như Q#152: thấy これからの hướng về tương lai thì PHẢI loại 増えてきました)."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "～てくる vs ～ていく",
                "difference_vi": "てくる hướng TỪ QUÁ KHỨ -> HIỆN TẠI (hoặc tiến vào gần người nói); ていく hướng TỪ HIỆN TẠI -> TƯƠNG LAI (hoặc đi xa dần).",
                "quick_test_vi": "Tìm từ chỉ thời gian: 昔から / 最近 / だんだん -> てくる; これからの / 将来 -> ていく.",
            }
        ],
        "examples": [
            {
                "jp": "しかし、今、そのマグロの数が減ってきている。",
                "reading_note": "しかし、いま、そのまぐろのかずがへってきている。",
                "vi": "Tuy nhiên, hiện nay số lượng cá ngừ đang giảm dần lại.",
                "grammar_note": "減る + てきている: quá trình suy giảm kéo dài từ trước đến thời điểm hiện tại.",
            },
            {
                "jp": "寒くなってきたので、かぜをひかないように気をつけてください。",
                "reading_note": "さむくなってきたので、かぜをひかないようにきをつけてください。",
                "vi": "Vì trời đã bắt đầu trở lạnh dần nên hãy cẩn thận kẻo bị cảm.",
                "grammar_note": "なる + てきた: sự chuyển biến nhiệt độ tới hiện tại.",
            },
        ],
        "source_ref": "03_Grammar/Group_02 | Sơ đồ N5-N1 | Đề .xlsx (Q50, Q148, Q152, Passage 4)",
        "search_keywords": "te kuru bien chuyen tu qua khu den nay てくる てきた てきている",
        "match_patterns": ["てきて", "てきた", "てきました", "てくる"],
    },
    {
        "code": "GP-N4-08",
        "pattern": "～ていく (Tiếp tục biến đổi hướng về tương lai)",
        "jlpt_level": "N4",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": True,
        "formation_formula": "Vて + いく / いきます / いくでしょう",
        "formation_table": [
            {"pos": "Trục thời gian (Hiện tại -> Tương lai)", "rule": "Tiếp tục diễn ra, duy trì hoặc biến đổi dần về sau (使われていくでしょう, 失われていく, 育てていく)"},
            {"pos": "Biến mất / Đi xa dần", "rule": "Hiện tượng phai nhạt, mất dần đi theo thời gian (消えていく, 減っていく)"},
        ],
        "core_meaning_vi": "Diễn tả hành động hoặc xu hướng tiếp tục kéo dài, phát triển hoặc biến đổi từ hiện tại hướng về tương lai",
        "deep_explanation_vi": (
            "～ていく là nửa kia của trục thời gian tiếng Nhật đối xứng với ～てくる. "
            "Trong bài đục lỗ '緑のカーテン' (Q#152), cụm 'これからの日本の家に...' chốt hướng tương lai nên phải chọn 使われていくでしょう, loại 増えてきました. "
            "Ngoài ra, trong Passage 9 ('普通は成長すると失われていくものなのだ'), 失われていく diễn tả sự mất dần đi theo quá trình trưởng thành về sau."
        ),
        "register_tag": "Trung tính (Văn viết & Hội thoại)",
        "confusable_pairs": [
            {
                "rival_pattern": "～ていく vs ～てくる",
                "difference_vi": "ていく đi từ hiện tại hướng ra tương lai; てくる đi từ quá khứ tiến vào hiện tại.",
                "quick_test_vi": "Có dấu hiệu tương lai (これから, 今後, 将来) hoặc động từ tiêu biến dần (失われる, 消える) -> chọn ていく.",
            }
        ],
        "examples": [
            {
                "jp": "緑のカーテンはこれからの日本の家に使われていくでしょう。",
                "reading_note": "みどりのかーてんはこれからのにほんのいえにつかわれていくでしょう。",
                "vi": "Rèm xanh chắc hẳn sẽ tiếp tục được sử dụng trong những ngôi nhà Nhật từ nay về sau.",
                "grammar_note": "これからの (từ nay về sau) kết hợp bị động + ていく + でしょう.",
            },
            {
                "jp": "普通は成長すると共感覚は失われていくものだ。",
                "reading_note": "ふつうはせいちょうするときょうかんかくはうしなわれていくものだ。",
                "vi": "Thông thường khi trưởng thành, cảm giác kèm sẽ mất dần đi.",
                "grammar_note": "Quá trình biến mất dần theo thời gian dùng 失われていく.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 (Trang 4) | Đề .xlsx (Q152, Passages 9, 13)",
        "search_keywords": "te iku tuong lai tiep dien ていく ていきます 使われていく",
        "match_patterns": ["ていく", "ていきま", "ていくだろう", "ていくでしょう"],
    },
    {
        "code": "GP-N4-09",
        "pattern": "～てしまう (Hoàn tất trọn vẹn / Lỡ mất đáng tiếc)",
        "jlpt_level": "N4",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": True,
        "formation_formula": "Vて + しまう / しまった (Khẩu ngữ: ～ちゃう / ～じゃう)",
        "formation_table": [
            {"pos": "Hoàn tất triệt để", "rule": "Làm xong hết toàn bộ (読んでしまった, 食べてしまった)"},
            {"pos": "Nuối tiếc / Ngoài ý muốn", "rule": "Lỡ làm mất, kết cục đáng tiếc không mong muốn (忘れてしまい, 散ってしまった, 減ってしまっている, 昼になってしまった)"},
        ],
        "core_meaning_vi": "Diễn tả hành động đã hoàn tất triệt để hoặc sự việc lỡ xảy ra gây cảm giác nuối tiếc, áy náy",
        "deep_explanation_vi": (
            "～てしまう mang 2 tầng nghĩa: hoàn thành dứt điểm 100% và sắc thái cảm xúc 'lỡ mất / mất rồi'. "
            "Trong đề thi (như Q#92: いつのまにか昼になってしまった; Q#104: 桜の花はもう散ってしまった; Passage 4: 育つ量も減ってしまっている; Passage 8: 入力するのを忘れてしまい), "
            "～てしまう báo hiệu thái độ tiếc nuối hoặc lo ngại của người viết đối với sự cố đang kể."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vてしまう vs Vきる",
                "difference_vi": "Cả hai đều có nghĩa 'làm hết hoàn toàn', nhưng てしまう mang sắc thái cảm xúc hoàn tất/nuối tiếc, còn Vきる (như 食べきる) chỉ mức độ năng lực/triệt để hoàn thành toàn bộ khối lượng.",
                "quick_test_vi": "Nếu có sắc thái 'lỡ quên / lỡ hỏng / đáng tiếc' -> bắt buộc dùng てしまう.",
            }
        ],
        "examples": [
            {
                "jp": "プレゼント用だと入力するのを忘れてしまい、ラッピングがされていなかった。",
                "reading_note": "ぷれぜんとようだとにゅうりょくするのをわすれてしまい、らっぴんぐがされていなかった。",
                "vi": "Tôi lỡ quên nhập mục làm quà tặng nên hộp không được gói.",
                "grammar_note": "忘れてしまい diễn tả sai sót ngoài ý muốn gây rắc rối.",
            },
            {
                "jp": "一生けん命仕事をしていたら、いつのまにか昼になってしまった。",
                "reading_note": "いっしょうけんめいしごとをしていたら、いつのまにかひるになってしまった。",
                "vi": "Mải làm việc quá, lúc nào không hay đã đến trưa mất rồi.",
                "grammar_note": "Đi cùng いつのまにか để nhấn mạnh sự việc trôi qua ngoài dự kiến.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 (Trang 4) | Đề .xlsx (Q92, Q104, Passages 4, 8)",
        "search_keywords": "te shimau lo mat hoan tat てしまう てしまった てしまい",
        "match_patterns": ["てしま", "てしまい"],
    },
    {
        "code": "GP-N4-10",
        "pattern": "Vます + やすい / にくい (Dễ làm / Khó làm)",
        "jlpt_level": "N4",
        "category": "conjugation",
        "category_label_vi": CATEGORY_LABELS["conjugation"],
        "in_exam_corpus": True,
        "formation_formula": "Vます(bỏ ます) + やすい / にくい (Chia như Tính từ đuôi い!)",
        "formation_table": [
            {"pos": "Vます + やすい", "rule": "Dễ làm gì / Có tính chất dễ xảy ra (つけやすい, 読みやすい, 壊れやすい)"},
            {"pos": "Vます + にくい", "rule": "Khó làm gì (聞こえにくい, 言いにくい, わかりにくい)"},
            {"pos": "Quy tắc chia tiếp", "rule": "Là Tính từ い -> đứng trước なる phải đổi い->く (つけやすくなる, 聞こえにくくなる); bổ nghĩa N giữ い (読みやすい本)"},
        ],
        "core_meaning_vi": "Đánh giá tính chất dễ hay khó thực hiện một hành động (về mặt thao tác hoặc tâm lý)",
        "deep_explanation_vi": (
            "Đây là mẫu N4 có tần suất xuất hiện cực cao trong cả 3 phần đề N3 (Q#28, Q#150, Passage 3, Passage 12). "
            "Hai nguyên tắc vàng: 1) Chỉ ghép vào Vます bỏ ます (không ghép với Vる hay thể bị động: *つけられやすい trong Q#28 là sai). "
            "2) Toàn bộ cụm Vやすい/Vにくい biến thành TÍNH TỪ ĐUÔI い nên kết hợp với なる bắt buộc phải đổi thành やすく/にくくなる (つけやすくなっています), tuyệt đối không dùng *つけやすいに."
        ),
        "register_tag": "Trung tính",
        "confusable_pairs": [
            {
                "rival_pattern": "Vます + にくい vs Vます + づらい (N3-N2)",
                "difference_vi": "にくい chỉ độ khó chung (cả vật lý lẫn tâm lý: 聞こえにくい, 言いにくい); づらい nhấn mạnh sự khó khăn gây đau đớn, gượng gạo về tâm lý/thể chất (歩きづらい).",
                "quick_test_vi": "Trong đề N3 chuẩn mực chia với なる: luôn chia やすく/にくく + なる (tránh bẫy *やすいに).",
            }
        ],
        "examples": [
            {
                "jp": "容器の先にスポンジがついているので、つけやすくなっています。",
                "reading_note": "ようきのさきにすぽんじがついているので、つけやすくなっています。",
                "vi": "Vì đầu lọ có miếng mút nên trở nên dễ thoa.",
                "grammar_note": "つける -> つけやすい -> つけやすく + なっています.",
            },
            {
                "jp": "大きな音を聞き続けると、小さい音が聞こえにくくなる。",
                "reading_note": "おおきなおとをききつづけると、ちいさいおとがきこえにくくなる。",
                "vi": "Nếu tiếp tục nghe âm thanh lớn, sẽ trở nên khó nghe thấy âm thanh nhỏ.",
                "grammar_note": "聞こえる -> 聞こえにくい -> 聞こえにくく + なる.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 | Đề .xlsx (Q28, Q150, Passages 3, 12)",
        "search_keywords": "yasui nikui de kho Vますやすい にくい つけやすく 聞こえにくく",
        "match_patterns": ["やすい", "やすく", "にくい", "にくく"],
    },
    {
        "code": "GP-N4-11",
        "pattern": "～ように (Mục đích hướng tới trạng thái không ý chí / khả năng)",
        "jlpt_level": "N4",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": True,
        "formation_formula": "Vえる(khả năng) / Vない(phủ định) / Vる(không ý chí) + ように",
        "formation_table": [
            {"pos": "Thể khả năng + ように", "rule": "Để có thể làm được V (読めるように, 話せるように)"},
            {"pos": "Thể phủ định Vない + ように", "rule": "Để không bị / để đừng... (かぜをひかないように, 忘れないように)"},
            {"pos": "Động từ không ý chí + ように", "rule": "Để đạt được trạng thái (よく眠れるように, 病気が治るように, わかるように)"},
        ],
        "core_meaning_vi": "Diễn tả mục đích 'để có thể / sao cho' gắn với động từ khả năng, phủ định hoặc tự động từ không ý chí",
        "deep_explanation_vi": (
            "Phân biệt ～ように và ～ために là cặp bẫy số 1 của trình độ N4->N3 (xuất hiện trực tiếp ở Q#27, Q#50, Q#18): "
            "1) ように đi với động từ KHÔNG mang ý chí chủ động kiểm soát trực tiếp (thể khả năng Vえる, thể phủ định Vない, tự động từ 治る・わかる・見える). "
            "2) Khi chủ thể phía trước và sau ように khác nhau (tôi mua sách để con đọc: 子どもが読めるように), vẫn dùng ように. "
            "3) TUYỆT ĐỐI không gắn ために vào sau thể khả năng (*読めるために là sai ngữ pháp)."
        ),
        "register_tag": "Trung tính (Cốt lõi N4->N3)",
        "confusable_pairs": [
            {
                "rival_pattern": "～ように vs ～ために",
                "difference_vi": "ように đi với V khả năng / Vない / V không ý chí (chỉ trạng thái kỳ vọng); ために đi với V ý chí / Danh từ + の (chỉ mục đích trực tiếp của cùng 1 chủ ngữ).",
                "quick_test_vi": "Soi động từ trước chỗ trống: thấy Vえる (読める) hoặc Vない (ひかない) -> CHỌN NGAY ように!",
            }
        ],
        "examples": [
            {
                "jp": "必要なときに読めるように、大切にしまっておいてください。",
                "reading_note": "ひつようなときによめるように、たいせつにしまっておいてください。",
                "vi": "Để có thể đọc được khi cần, hãy cất giữ cẩn thận.",
                "grammar_note": "読める (thể khả năng) bắt buộc kết hợp với ように (loại *読めるために).",
            },
            {
                "jp": "かぜをひかないように気をつけてください。",
                "reading_note": "かぜをひかないようにきをつけてください。",
                "vi": "Xin hãy chú ý để không bị cảm lạnh.",
                "grammar_note": "かぜをひかない (không bị cảm - trạng thái ngoài ý muốn) + ように.",
            },
        ],
        "source_ref": "Shin-N3-List #63 | Sơ đồ N5-N1 | Đề .xlsx (Q18, Q27, Q50, Q88)",
        "search_keywords": "you ni muc dich kha nang phu dinh ように 読めるように ひかないように",
        "match_patterns": ["ないように", "えるように", "るように"],
    },
    {
        "code": "GP-N4-12",
        "pattern": "～ために / ～ための (Mục đích ý chí & Nguyên nhân)",
        "jlpt_level": "N4",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": True,
        "formation_formula": "[Mục đích] Vる(ý chí) / N + の + ために (hoặc + ための + N) | [Nguyên nhân] 普通形(Vた/Aい/Aな+な/N+の) + ために",
        "formation_table": [
            {"pos": "Chỉ Mục đích (Để)", "rule": "Vる(hành động chủ ý) + ために / N + の + ために (日本語を勉強するために, 新しい仕事のために). Chủ ngữ 2 vế phải giống nhau!"},
            {"pos": "Chỉ Nguyên nhân (Vì)", "rule": "Vた / Vている / A / Nの + ために (văn phong trang trọng hơn から: 大雨のため, 働きすぎたために)"},
            {"pos": "Bổ nghĩa Danh từ", "rule": "Vる / Nの + ための + N (chú ý nối bằng の chứ không phải に)"},
        ],
        "core_meaning_vi": "Diễn tả mục đích có ý chí chủ động (để làm V / cho N) hoặc nguyên nhân trang trọng (vì... nên)",
        "deep_explanation_vi": (
            "ため(に) có hai vai trò hoàn toàn khác nhau dựa vào dạng từ đứng trước: "
            "1) Nếu đứng trước là Vる có ý chí hoặc N của người/mục tiêu (戦うために, 体のために, 練習のために) -> nghĩa 'vì mục đích...'. Không bao giờ đặt thể khả năng Vえる hay Vない trước ために chỉ mục đích (Q#27, Q#50). "
            "2) Nếu đứng trước là Vた/A/N sự cố thiên tai (大雨のため, 働きすぎたために trong Q#100, Q#155) -> nghĩa 'tại vì / do nguyên nhân...'. "
            "Chú ý: trong Q#155 (冗談がわからないせいで), 聞こえなかったために bị loại vì sai ý (nghe thấy nhưng không hiểu nghĩa) chứ không phải sai cấu trúc nguyên nhân của ために."
        ),
        "register_tag": "Trung tính & Văn viết trang trọng",
        "confusable_pairs": [
            {
                "rival_pattern": "Vる(ý chí) + ために vs Vえる/Vない + ように",
                "difference_vi": "ために đòi hỏi động từ ý chí kiểm soát được và cùng 1 chủ ngữ; ように dùng cho thể khả năng, phủ định hoặc ước mong trạng thái.",
                "quick_test_vi": "Có chủ đích thực hiện rõ ràng (戦う, 合格する) + cùng chủ ngữ -> ために; Vえる/Vない -> ように.",
            }
        ],
        "examples": [
            {
                "jp": "大雨のため、大会の中止が決まった。",
                "reading_note": "おおあめのため、たいかいのちゅうしがきまった。",
                "vi": "Vì mưa lớn nên việc hủy bỏ giải đấu đã được quyết định.",
                "grammar_note": "N + の + ため chỉ nguyên nhân trang trọng trong thông báo.",
            },
            {
                "jp": "練習のために、先生が言ったことを何度も繰り返した。",
                "reading_note": "れんしゅうのために、せんせいがいったことをなんどもくりかえした。",
                "vi": "Để luyện tập, tôi đã lặp lại nhiều lần điều thầy nói.",
                "grammar_note": "N(hành động chủ đích) + の + ために chỉ mục đích.",
            },
        ],
        "source_ref": "Shin-N3-List #19 | Sơ đồ N5-N1 | Đề .xlsx (Q27, Q50, Q84, Q99, Q155)",
        "search_keywords": "tame ni muc dich nguyen nhan ために ための ため",
        "match_patterns": ["ために", "ための", "のため"],
    },
    {
        "code": "GP-N4-13",
        "pattern": "～ことにする / ～ことにしている (Chủ động quyết định / Thói quen tự đặt)",
        "jlpt_level": "N4",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": True,
        "formation_formula": "Vる / Vない + ことにする (Quyết định) | Vる / Vない + ことにしている (Duy trì thói quen tự đề ra)",
        "formation_table": [
            {"pos": "Quyết định tức thời", "rule": "Vる / Vない + ことにする / ことにした (Tôi quyết định sẽ làm/không làm V)"},
            {"pos": "Thói quen tự quy định", "rule": "Vる / Vない + ことにしている (Tôi luôn tự đặt ra thói quen làm/không làm V)"},
            {"pos": "Không dùng Vた trước こと", "rule": "Cấm dùng *使ったことにする (chỉ dùng thì ở する cuối câu: 使うことにした)"},
        ],
        "core_meaning_vi": "Bản thân chủ động đưa ra quyết định (ことにする) hoặc tự duy trì nguyên tắc/thói quen cá nhân (ことにしている)",
        "deep_explanation_vi": (
            "Đây là cặp nền tảng được giảng trực tiếp trong giáo trình 03_Grammar/Group_01 (ことにする_vs_ことになる.md) và thi trực tiếp ở 問題2 ★ Q#25 (掃除用具として使うことにした). "
            "Cần nhớ hai quy tắc: (1) Chủ thể quyết định là bản thân người nói ('tôi quyết định mua/dùng'), đối lập với ことになる (quyết định khách quan/tập thể). "
            "(2) Động từ trước こと luôn ở nguyên thể Vる hoặc Vない."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "～ことにする vs ～ことになる",
                "difference_vi": "ことにする = ý chí chủ quan của cá nhân tự quyết; ことになる = kết quả khách quan, lịch trình hay tổ chức quyết định thay cho mình.",
                "quick_test_vi": "Nếu là quyết định cá nhân ('tôi mua áo vì thích' trong Q#134) -> ことにした; nếu là chuyển công tác/quy định trường/được cử đi thi đấu (Q#57) -> ことになった.",
            }
        ],
        "examples": [
            {
                "jp": "古くなった歯ブラシを掃除用具として使うことにした。",
                "reading_note": "ふるくなったはぶらしをそうじようぐとしてつかうことにした。",
                "vi": "Tôi đã quyết định tận dụng bàn chải cũ làm dụng cụ vệ sinh.",
                "grammar_note": "Vる (使う) + こと + に + した (câu ghép 4 mảnh Q#25).",
            },
            {
                "jp": "その店の服がとても気に入ったので、買うことにした。",
                "reading_note": "そのみせのふくがとてもきにいったので、かうことにした。",
                "vi": "Vì rất ưng bộ quần áo ở tiệm đó nên tôi đã quyết định mua.",
                "grammar_note": "Lý do cá nhân tự chọn dùng 買うことにした.",
            },
        ],
        "source_ref": "03_Grammar/Group_01 | Shin-N3-List #49 | Đề .xlsx (Q25, Q134)",
        "search_keywords": "koto ni suru koto ni shite iru quyet dinh chu quan ことにする ことにした",
        "match_patterns": ["ことにする", "ことにした", "ことにしている"],
    },
    {
        "code": "GP-N4-14",
        "pattern": "～ことになる / ～ことになっている (Quyết định khách quan / Quy định chung)",
        "jlpt_level": "N4",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": True,
        "formation_formula": "Vる / Vない + ことになる (Được quyết định/kết cục là) | Vる / Vない + ことになっている (Có quy định/lịch trình là)",
        "formation_table": [
            {"pos": "Kết quả/Quyết định khách quan", "rule": "Vる / Vない + ことになる / ことになった (tổ chức quyết định hoặc tình thế dẫn đến)"},
            {"pos": "Quy định / Luật lệ / Lịch trình", "rule": "Vる / Vない + ことになっている (luật lệ xã hội, nội quy, lịch đã định sẵn)"},
        ],
        "core_meaning_vi": "Diễn tả việc được quyết định bởi tập thể/tình thế bên ngoài (ことになる) hoặc quy định, lịch trình cố định (ことになっている)",
        "deep_explanation_vi": (
            "Người Việt hay dịch 'đã quyết định' đều là ことにする, nhưng trong văn hóa khiêm nhường và ngữ pháp Nhật, ngay cả việc bạn đi thi đấu thay đàn anh (Q#57: 試合に出ることになった) hay bị mất việc (Q#115: 仕事を失うことになった) hay mất cơ hội (Passage 15: チャンスをなくすことになる) đều dùng ことになる để thể hiện kết quả khách quan do hoàn cảnh/tập thể đưa tới. "
            "Dạng tiếp diễn ～ことになっている chỉ quy định nội quy sẵn có (loại bẫy ở Q#147 vì cảnh báo rủi ro y khoa dùng おそれがある, không dùng quy định ことになっている)."
        ),
        "register_tag": "Trung tính (Hội thoại & Trang trọng)",
        "confusable_pairs": [
            {
                "rival_pattern": "～ことになっている vs ～おそれがある",
                "difference_vi": "ことになっている là quy định/lịch trình đã định trước (tích cực hoặc trung tính); おそれがある là dự báo nguy cơ rủi ro tiêu cực có thể xảy ra.",
                "quick_test_vi": "Vế trước là 'nếu không cẩn thận thì triệu chứng xấu đi...' (Q#147) -> chọn おそれがある, loại ことになっている.",
            }
        ],
        "examples": [
            {
                "jp": "けがをした先輩のかわりにチームの代表として試合に出ることになった。",
                "reading_note": "けがをしたせんぱいのかわりにちーむのだいひょうとしてしあいにでることになった。",
                "vi": "Tôi được quyết định sẽ ra thi đấu với tư cách đại diện đội thay đàn anh bị thương.",
                "grammar_note": "Quyết định do tập thể/tình huống phân công dùng 出ることになった.",
            },
            {
                "jp": "大きなミスをして、仕事を失うことになった。",
                "reading_note": "おおきなみすをして、しごとをうしなうことになった。",
                "vi": "Vì mắc sai lầm lớn nên kết cục là tôi phải mất việc.",
                "grammar_note": "Kết cục ngoài ý muốn dẫn tới cũng dùng ことになる.",
            },
        ],
        "source_ref": "03_Grammar/Group_01 | anki #7 | Đề .xlsx (Q19, Q57, Q115, Q147, Q156)",
        "search_keywords": "koto ni naru koto ni natte iru quyet dinh khach quan quy dinh ことになる ことになっている",
        "match_patterns": ["ことになる", "ことになった", "ことになっている", "ことになっています"],
    },
    {
        "code": "GP-N4-15",
        "pattern": "～ようにする vs ～ようになる (Cố gắng tạo thói quen vs Biến chuyển năng lực)",
        "jlpt_level": "N4",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": True,
        "formation_formula": "Vる(ý chí)/Vない + ようにする (Cố gắng làm) | Vる(khả năng/không ý chí)/Vない + ようになる (Trở nên có thể/thay đổi)",
        "formation_table": [
            {"pos": "～ようにする / ～ようにしている", "rule": "Chủ động nỗ lực duy trì thói quen hoặc chú ý thực hiện/tránh làm (食べるようにする, 捕るようにする)"},
            {"pos": "～ようになる / ～ようになった", "rule": "Sự thay đổi trạng thái hoặc năng lực từ không thể -> có thể (読めるようになる, 捕られるようになった)"},
        ],
        "core_meaning_vi": "Phân biệt nỗ lực chủ động giữ thói quen (ようにする) với sự biến chuyển tự nhiên về năng lực/trạng thái (ようになる)",
        "deep_explanation_vi": (
            "Cặp bài học trọng tâm trong 03_Grammar/Group_02 (ようにする_vs_ようになる.md) và xuất hiện ở Passage 4 (大量に捕られるようになった và 捕るようにすることも重要ではないだろうか). "
            "Quy tắc vàng: trước ようになる thường là động từ khả năng (話せるようになる) hoặc bị động/không ý chí để chỉ bước ngoặt biến đổi khách quan ('đã trở nên...'); còn trước ようにする là động từ hành động có ý chí ('cố gắng thực hiện...')."
        ),
        "register_tag": "Trung tính",
        "confusable_pairs": [
            {
                "rival_pattern": "～ようにする vs ～ことにする",
                "difference_vi": "ようにする là cố gắng từng bước để duy trì thói quen (nỗ lực liên tục); ことにする là đưa ra quyết định dứt khoát tại một thời điểm.",
                "quick_test_vi": "Có hàm ý 'chú ý rèn luyện / cố gắng từng ngày' -> ようにしている; 'quyết định chọn phương án' -> ことにした.",
            }
        ],
        "examples": [
            {
                "jp": "マグロは海外でも人気なので、大量に捕られるようになった。",
                "reading_note": "まぐろはかいがいでもにんきなので、たいりょうにとられるようになった。",
                "vi": "Vì cá ngừ được ưa chuộng cả ở nước ngoài nên nó đã trở nên bị đánh bắt với số lượng lớn.",
                "grammar_note": "Sự chuyển biến tình trạng theo thời gian dùng 捕られるようになった.",
            },
            {
                "jp": "消費に合った量のマグロを捕るようにすることも重要ではないだろうか。",
                "reading_note": "しょうひにあったりょうのまぐろをとるようにすることもじゅうようではないだろうか。",
                "vi": "Việc cố gắng điều chỉnh đánh bắt lượng cá ngừ khớp với tiêu thụ chẳng phải cũng rất quan trọng sao?",
                "grammar_note": "Hành động nỗ lực thực hiện có chủ đích dùng 捕るようにする.",
            },
        ],
        "source_ref": "03_Grammar/Group_02 | Shin-N3-List #50 | Đề .xlsx (Passage 4)",
        "search_keywords": "you ni suru you ni naru co gang bien chuyen ようにする ようになる",
        "match_patterns": ["ようにする", "ようにしている", "ようになる", "ようになった"],
    },
    {
        "code": "GP-N4-16",
        "pattern": "4 Câu điều kiện ～と / ～ば / ～たら / ～なら",
        "jlpt_level": "N4",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": True,
        "formation_formula": "Vる/Vない + と | V(đổi cột う->え+ば)/Aい->ければ | Vた/Aかった/Nだった + ら | 普通形(N/Aな bỏ だ) + なら",
        "formation_table": [
            {"pos": "～と (Tất yếu / Thói quen)", "rule": "Điều kiện tất yếu tự nhiên, quy luật, hoặc 2 việc nối tiếp quá khứ (cấm dùng mệnh lệnh/ý chí ở vế sau!)"},
            {"pos": "～ば (Điều kiện giả định chung)", "rule": "V1(e+ば), V2(bỏ る+れば), Aい(ければ), Phủ định(なければ). Cặp hay thi: ～ば～ほど, さえ～ば"},
            {"pos": "～たら (Nếu/Khi xong V1)", "rule": "Dùng rộng rãi nhất; đặc biệt dùng cho lời khuyên/rủ rê/ý chí ở vế sau và 'sau khi hoàn tất V1' (済んだら)"},
            {"pos": "～なら / ～のなら (Nếu như là...)", "rule": "Tiếp nhận chủ đề/thông tin từ người đối diện rồi đưa ra lời khuyên phù hợp (進学するなら...)"},
        ],
        "core_meaning_vi": "4 dạng mệnh đề điều kiện tiếng Nhật phân tách theo tính tất yếu (と), giả định chung (ば), hoàn tất cụ thể (たら) và tiếp nhận chủ đề (なら)",
        "deep_explanation_vi": (
            "Đây là lỗ hổng số 1 khi bước từ N4 lên N3: cả 4 mẫu đều dịch sang tiếng Việt là 'nếu/khi', nhưng quy tắc vế sau khác hẳn nhau. "
            "1) ～と CẤM dùng câu mệnh lệnh, rủ rê, yêu cầu (như ～てください, ～よう) ở vế sau; khi vế sau ở quá khứ (Vたと) nó có nghĩa 'khi làm V1 thì phát hiện ra V2' (như Q#11, Q#142). "
            "2) ～たら dùng được với mọi loại vế sau và mang nghĩa 'sau khi xong V1 thì...' (Q#46: 用事が済んだら). "
            "3) ～なら tiếp nhận bối cảnh đối phương vừa nói ('nếu định đi học lên cao thì...', Q#48) và không hợp kể nguyên nhân sự thật đã qua (loại ở Q#155: 理解できないなら)."
        ),
        "register_tag": "Trung tính (Cốt lõi N4->N3)",
        "confusable_pairs": [
            {
                "rival_pattern": "～と vs ～たら vs ～なら",
                "difference_vi": "と = tất yếu/tự nhiên (cấm mệnh lệnh vế sau); たら = sau khi xảy ra/nếu xảy ra cụ thể (mọi vế sau đều được); なら = giả định dựa trên đề tài vừa nêu ('nếu nói về việc...').",
                "quick_test_vi": "Vế sau có てください/ましょう? Loại と! Kể lại chuyện đã xảy ra trong quá khứ? Loại なら!",
            }
        ],
        "examples": [
            {
                "jp": "用事が済んだら、連絡してください。",
                "reading_note": "ようじがすんだら、れんらくしてください。",
                "vi": "Khi nào giải quyết xong việc thì hãy liên lạc cho tôi nhé.",
                "grammar_note": "Vế sau là yêu cầu lịch sự (してください) kết hợp 'sau khi xong' nên dùng たら.",
            },
            {
                "jp": "進学するなら、もっとしっかり勉強しなさい。",
                "reading_note": "しんがくするなら、もっとしっかりべんきょうしなさい。",
                "vi": "Nếu định học lên cao thì hãy học hành chăm chỉ hơn đi.",
                "grammar_note": "Tiếp nhận dự định của người nghe để đưa ra lời khuyên dùng なら.",
            },
        ],
        "source_ref": "Shin-N3-List #25 | Sơ đồ N5-N1 | Đề .xlsx (Q46, Q48, Q155)",
        "search_keywords": "dieu kien to ba tara nara nếu khi と ば たら なら",
        "match_patterns": ["んだら", "としたら", "するなら", "なければ", "と、"],
    },
    {
        "code": "GP-N4-17",
        "pattern": "～てみる / ～ようとする (Thử làm / Định làm, cố gắng làm)",
        "jlpt_level": "N4",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": True,
        "formation_formula": "Vて + みる (Thử làm xem sao) | V(ý chí う/よう) + とする (Định làm / Cố làm ngay lúc đó)",
        "formation_table": [
            {"pos": "～てみる", "rule": "Thử làm hành động V để xem kết quả ra sao (聞いてみる, 使ってみる)"},
            {"pos": "Thể ý chí V(y/o)う", "rule": "V1(cột う->お+う: 行こう, なろう), V2(bỏ る+よう: 食べよう, 譲ろう), V3(しよう, こよう)"},
            {"pos": "～ようとする", "rule": "Ngay lúc định bắt tay làm V (家を出ようとしたとき) hoặc cố gắng làm nhưng chưa thành"},
        ],
        "core_meaning_vi": "Diễn tả việc làm thử nghiệm (てみる) và thời điểm sắp sửa bắt tay thực hiện hoặc nỗ lực hướng tới (ようとする)",
        "deep_explanation_vi": (
            "Hai mẫu này kiểm tra kỹ năng nhận diện sắc thái ý định trong Đọc hiểu và Đục lỗ: "
            "trong Passage 3 ('以前は譲ろうとしたことがあるが'), 譲ろうとする diễn tả việc từng cố định nhường ghế nhưng bị từ chối. "
            "Còn trong Q#153 ('ストレスになろうとする' bị loại), ストレスになる là trạng thái tâm lý khách quan, không thể dùng thể ý chí Vようとする ('cố định trở thành áp lực')."
        ),
        "register_tag": "Trung tính",
        "confusable_pairs": [
            {
                "rival_pattern": "Vようとする vs Vるつもりだ",
                "difference_vi": "ようとする diễn tả khoảnh khắc ngay trước khi thực hiện hành động hoặc cố gắng tức thời; つもりだ là kế hoạch, dự định đã ấp ủ từ trước trong đầu.",
                "quick_test_vi": "Gặp 'đúng lúc đang định bước ra thì trời mưa' -> ようとしたとき; kế hoạch tương lai -> つもりだ.",
            }
        ],
        "examples": [
            {
                "jp": "席を譲らない若者に聞いてみると、以前は譲ろうとしたことがあるという。",
                "reading_note": "せきをゆずらないわかものにきいてみると、いぜんはゆずろうとしたことがあるという。",
                "vi": "Khi thử hỏi các bạn trẻ không nhường ghế, họ bảo trước đây từng định nhường rồi.",
                "grammar_note": "聞いてみる (thử hỏi xem) và 譲ろうとした (từng định nhường).",
            },
            {
                "jp": "家を出ようとしたとき、突然大雨が降り出した。",
                "reading_note": "いえをでようとしたとき、とつぜんおおあめがふりだした。",
                "vi": "Đúng lúc tôi vừa định ra khỏi nhà thì trời đột ngột đổ mưa to.",
                "grammar_note": "Khoảnh khắc chuẩn bị thực hiện hành động thì có biến cố xen vào.",
            },
        ],
        "source_ref": "Shin-N3-List #51 | Đề .xlsx (Q153, Passage 3)",
        "search_keywords": "te miru you to suru thu lam dinh lam てみる ようとする",
        "match_patterns": ["てみる", "てみると", "ようとする", "ようとした", "うとする"],
    },
    {
        "code": "GP-N4-18",
        "pattern": "～てあげる・～てもらう・～てくれる (Làm giúp / Được làm cho)",
        "jlpt_level": "N4",
        "category": "keigo",
        "category_label_vi": CATEGORY_LABELS["keigo"],
        "in_exam_corpus": True,
        "formation_formula": "Vて + あげる(sashiageru) / もらう(itadaku) / くれる(kudasaru)",
        "formation_table": [
            {"pos": "～てくれる / ～てくださる", "rule": "Ai đó làm giúp tôi (người làm là chủ ngữ: 迎えに来てくれた, 包んでくれた)"},
            {"pos": "～てもらう / ～ていただく", "rule": "Tôi nhận được sự giúp đỡ từ ai đó (người nhận là chủ ngữ: 食べてもらいたい, 教えてもらえる)"},
            {"pos": "～てあげる / ～てさしあげる", "rule": "Tôi làm giúp ai đó (cẩn thận khi dùng với bề trên, tránh mang sắc thái ban ơn)"},
        ],
        "core_meaning_vi": "Diễn tả sự trao đổi hành động giúp đỡ và thái độ biết ơn giữa người thực hiện và người thụ hưởng",
        "deep_explanation_vi": (
            "Gắn động từ thể て vào あげる/もらう/くれる là đặc trưng giao tiếp Nhật Bản để biểu thị 'ai làm lợi cho ai'. "
            "Trong đề thi (như Q#6: 空港まで迎えに来てくれた; Q#51: 家族に食べててもらいたい; Q#145: 電話で教えてもらえる), "
            "cần lưu ý dạng khả năng của もらう là もらえる (có thể được chỉ bảo cho) và dạng khiêm nhường いただく (見ていただきたい / 連絡いただく)."
        ),
        "register_tag": "Trung tính & Lịch sự",
        "confusable_pairs": [
            {
                "rival_pattern": "Vてくれる vs Vてもらう",
                "difference_vi": "Cùng miêu tả việc A giúp B: dùng くれる khi A là chủ ngữ ('anh ấy chỉ giúp tôi'); dùng もらう khi B là chủ ngữ ('tôi được anh ấy chỉ giúp').",
                "quick_test_vi": "Kiểm tra trợ từ sau tên người giúp: nếu là が/は -> くれる; nếu là に/から -> もらう.",
            }
        ],
        "examples": [
            {
                "jp": "友だちが空港まで迎えに来てくれた。",
                "reading_note": "ともだちがくうこうまでむかえにきてくれた。",
                "vi": "Bạn tôi đã ra tận sân bay đón tôi.",
                "grammar_note": "Chủ ngữ 友だちが thực hiện hành động vì tôi -> てくれた.",
            },
            {
                "jp": "母はいつも家族に炊きたてのごはんを食べてもらいたいと言っている。",
                "reading_note": "はははいつもかぞくにたきたてのごはんをたべてもらいたいといっている。",
                "vi": "Mẹ tôi luôn nói muốn gia đình ăn cơm mới nấu nóng hổi.",
                "grammar_note": "家族に + 食べてもらいたい (muốn gia đình đón nhận/ăn cơm mẹ nấu).",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 | Đề .xlsx (Q6, Q51, Q145)",
        "search_keywords": "te ageru te morau te kureru lam giup てあげる てもらう てくれる",
        "match_patterns": ["てくれた", "てもらいたい", "てもらえる", "ていただき"],
    },
    {
        "code": "GP-N4-19",
        "pattern": "～はずだ / ～はずがない (Chắc chắn theo logic / Không đời nào)",
        "jlpt_level": "N4",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": True,
        "formation_formula": "Vる/Vた/Vない/Aい / Aな+な / N+の + はずだ / はずがない",
        "formation_table": [
            {"pos": "Khẳng định ～はずだ", "rule": "Chắc chắn là (dựa trên căn cứ logic, lịch trình, kiến thức khách quan)"},
            {"pos": "Phủ định ～はずがない / ～はずはない", "rule": "Tuyệt đối không đời nào, làm gì có chuyện đó (căn cứ logic)"},
            {"pos": "Quá khứ ～はずだった", "rule": "Đáng lẽ ra đã phải (nhưng thực tế lại không xảy ra)"},
        ],
        "core_meaning_vi": "Suy đoán chắc chắn (hoặc bác bỏ hoàn toàn) dựa trên cơ sở logic, quy luật hoặc lịch trình khách quan",
        "deep_explanation_vi": (
            "Đứng trước danh từ はず, nhớ 2 quy tắc kết hợp: Aな phải thêm な (元気なはずだ) và Danh từ phải thêm の (休みの日の はずだ, như Q#35 Shin-N3: 休みのはずはありません). "
            "Khác với に違いない (suy đoán chắc nịch theo trực giác/dấu hiệu của người nói), はずだ có căn cứ suy luận khách quan. "
            "Trong Q#152, phương án 見られなくなるはずです bị loại vì mâu thuẫn với vế trước tích cực."
        ),
        "register_tag": "Trung tính",
        "confusable_pairs": [
            {
                "rival_pattern": "～はずがない vs ～わけではない",
                "difference_vi": "はずがない phủ định 100% theo logic ('làm sao có chuyện'); わけではない chỉ phủ định một phần ('không hẳn là tất cả đều vậy').",
                "quick_test_vi": "Gặp 'tuy là vậy nhưng không phải tất cả đều...' -> わけではない; gặp bằng chứng chắc chắn bác bỏ -> はずがない.",
            }
        ],
        "examples": [
            {
                "jp": "余って捨ててしまう量も少なくないはずだ。",
                "reading_note": "あまってすててしまうりょうもすくなくないはずだ。",
                "vi": "Lượng sushi thừa bị vứt bỏ chắc hẳn cũng không ít.",
                "grammar_note": "Suy luận logic từ việc nhiều quán rẻ -> 少なくないはずだ.",
            },
            {
                "jp": "あの店が今日休みのはずはありません。電話で確認したんですから。",
                "reading_note": "あのみせがきょうやすみのはずはありません。でんわでかくにんしたんですから。",
                "vi": "Cửa hàng đó hôm nay chắc chắn không thể nghỉ được. Vì tôi đã gọi xác nhận rồi.",
                "grammar_note": "Danh từ 休み + の + はずはありません.",
            },
        ],
        "source_ref": "Shin-N3-List #35 | anki #34 | Đề .xlsx (Q152, Passage 4)",
        "search_keywords": "hazu da hazu ga nai chac chan logic はずだ はずがない はずです",
        "match_patterns": ["はずだ", "はずです", "はずがない", "はずはありません"],
    },
    {
        "code": "GP-N4-20",
        "pattern": "Hệ 4 mẫu Phỏng đoán & Truyền đạt ～ようだ / ～みたいだ / ～らしい / ～そうだ",
        "jlpt_level": "N4",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": True,
        "formation_formula": "Trực quan: Vます/A(bỏ い/な)+そうだ | Nghe nói: 普通形+そうだ | Căn cứ/Ví von: 普通形(Nの/Aな)+ようだ / (bỏ だ)+みたいだ / +らしい",
        "formation_table": [
            {"pos": "～そうだ (Nghe nói / Truyền đạt)", "rule": "Thể thông thường (N/Aな giữ だ) + そうだ (多くの高校で...増えているそうだ)"},
            {"pos": "～そうだ (Trông có vẻ sắp)", "rule": "Vます / Aい(bỏ い) / Aな + そうだ (減っていきそうです; ngoại lệ いい->よさそう, ない->なさそう)"},
            {"pos": "～ようだ / ～みたいだ", "rule": "Có vẻ như / Giống như (suy đoán qua giác quan bản thân; ようだ trang trọng hơn みたいだ)"},
            {"pos": "～らしい", "rule": "Hình như (nghe tin hoặc suy luận khách quan từ nguồn khác, vd 入院したらしい; Nらしい = đúng chất N)"},
        ],
        "core_meaning_vi": "Hệ thống 4 mẫu phỏng đoán và truyền đạt thông tin phân cấp từ nhìn bằng mắt đến nghe tin khách quan",
        "deep_explanation_vi": (
            "Trong kỳ thi N3, việc nhầm quy tắc nối giữa 4 mẫu này là bẫy cực phổ biến (Q#50, Q#61, Q#152, Q#155): "
            "1) Phân biệt 2 chữ そうだ: [Vます + そうだ] là 'trông có vẻ sắp...' (tính từ な: 減っていきそうです), còn [V普通形 + そうだ] là 'nghe nói rằng...' (増えているそうだ). "
            "2) Phân biệt らしい vs っぽい trong Q#61: trước らしい phải giữ nguyên tính từ い (黒いらしい) hoặc danh từ hoàn chỉnh (春らしい); KHÔNG ghép gốc từ bỏ い như *黒らしい (chỉ có 黒っぽい!)."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vます + そうだ vs V普通形 + そうだ vs N/普通形 + らしい",
                "difference_vi": "Vます+そうだ = nhìn bằng mắt thấy sắp sửa; V普通形+そうだ = trích dẫn trực tiếp nguồn tin nghe được; らしい = nghe đồn/suy luận có căn cứ khách quan.",
                "quick_test_vi": "Thấy Vます (降りそうだ) -> trông sắp mưa; thấy Vる/Vた+そうだ -> nghe nói.",
            }
        ],
        "examples": [
            {
                "jp": "小川さんが入院したらしいと聞いて、お手紙を書きました。",
                "reading_note": "おがわさんがにゅういんしたらしいときいて、おてがみをかきました。",
                "vi": "Nghe nói anh/chị Ogawa hình như đã nhập viện nên tôi viết bức thư này.",
                "grammar_note": "Nghe tin chưa xác thực trực tiếp dùng Vた + らしい.",
            },
            {
                "jp": "最近子どもが悪い友だちと遊んでいたりするようなので心配しています。",
                "reading_note": "さいきんこどもがわるいともだちとあそんでいたりするようなのでしんぱいしています。",
                "vi": "Gần đây con có vẻ hay chơi với bạn xấu nên tôi rất lo lắng.",
                "grammar_note": "Cảm nhận chủ quan qua quan sát dùng ようだ (chia ようなので).",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 (Trang 2) | Đề .xlsx (Q50, Q61, Q152, Q155, Passages 2, 11, 20)",
        "search_keywords": "you da mitai da rashii sou da phong doan truyen dat ようだ みたいだ らしい そうだ",
        "match_patterns": ["そうだ", "そうです", "らしい", "ようだ", "ようなので", "みたいな"],
    },
    {
        "code": "GP-N4-21",
        "pattern": "～ところだ (Sắp sửa / Đang lúc / Vừa mới)",
        "jlpt_level": "N4",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": True,
        "formation_formula": "Vる + ところだ (Sắp sửa) | Vている + ところだ (Đang lúc) | Vた + ところだ (Vừa mới xong) | Vた + ところを (Đúng lúc vừa thì...)",
        "formation_table": [
            {"pos": "Vる + ところだ", "rule": "Ngay trước khi bắt đầu hành động (これから出かけるところです)"},
            {"pos": "Vている + ところだ", "rule": "Đang giữa chừng hành động ngay lúc này (今、調べているところです)"},
            {"pos": "Vた + ところだ / ところを", "rule": "Vừa mới kết thúc tức thì (今帰ったところだ) hoặc bị bắt gặp đúng lúc vừa xuất hiện (現れたところを逮捕された)"},
        ],
        "core_meaning_vi": "Xác định chính xác 3 điểm thời gian quanh một hành động: ngay trước lúc làm (Vる), ngay trong lúc làm (Vている), vừa dứt xong (Vた)",
        "deep_explanation_vi": (
            "Đây là bẫy thời điểm hay ghép vào câu hỏi so sánh với ～ばかり (như Q#20: したところでは / ところだと) và dùng trong câu Từ vựng (Q#42: 犯人は金を取りに現れたところを逮捕された). "
            "Lưu ý điểm phân biệt cốt lõi: Vた + ところだ chỉ khoảng thời gian CỰC NGẮN tính bằng giây/phút ngay sau khi xong, không dùng cho 'tháng trước mới tốt nghiệp' (cái đó dùng Vたばかりだ)."
        ),
        "register_tag": "Trung tính",
        "confusable_pairs": [
            {
                "rival_pattern": "Vた + ところだ vs Vた + ばかりだ",
                "difference_vi": "Vたところだ chỉ thời điểm ngay tức thì (vài giây/phút trước), còn Vたばかりだ mang tính cảm nhận chủ quan ('cảm giác như mới đây thôi', dùng được cho vài tháng/năm trước).",
                "quick_test_vi": "Thấy 'tháng trước/năm ngoái mới vào công ty' -> bắt buộc Vたばかり, không dùng ところ.",
            }
        ],
        "examples": [
            {
                "jp": "犯人は金を取りに現れたところを逮捕された。",
                "reading_note": "はんにんはかねをとりにあらわれたところをたいほされた。",
                "vi": "Tên tội phạm đã bị bắt giữ ngay lúc vừa xuất hiện để lấy tiền.",
                "grammar_note": "Vた + ところを đánh dấu khoảnh khắc hành động diễn ra bị tác động ngay lập tức.",
            },
            {
                "jp": "試験中、隣の人の答えを見ているところを先生に注意された。",
                "reading_note": "しけんちゅう、となりのひとのこたえをみているところをせんせいにちゅういされた。",
                "vi": "Trong lúc thi, đúng lúc đang nhìn bài người bên cạnh thì bị thầy nhắc.",
                "grammar_note": "Vている + ところを = ngay đúng lúc đang thực hiện.",
            },
        ],
        "source_ref": "Shin-N3-List #4 | Sơ đồ N5-N1 | Đề .xlsx (Q20, Q42)",
        "search_keywords": "tokoro da sap sua dang luc vua moi ところだ ところを",
        "match_patterns": ["ところだ", "ところです", "ところを", "ところでは"],
    },
    {
        "code": "GP-N4-22",
        "pattern": "～たばかりだ (Vừa mới... theo cảm nhận thời gian)",
        "jlpt_level": "N4",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": True,
        "formation_formula": "Vた + ばかりだ / ばかりの + N (Khác hoàn toàn Vて + ばかりいる!)",
        "formation_table": [
            {"pos": "Vị ngữ cuối câu", "rule": "Vた + ばかりだ / ばかりです (Vừa mới làm xong chưa lâu)"},
            {"pos": "Bổ nghĩa danh từ", "rule": "Vた + ばかりの + N (ví dụ: 買ったばかりの靴)"},
            {"pos": "Tránh nhầm với Vてばかりいる", "rule": "Vた + ばかり (vừa mới) <-> Vて + ばかりいる (suốt ngày chỉ toàn làm V)"},
        ],
        "core_meaning_vi": "Nhấn mạnh khoảng thời gian từ lúc hoàn thành hành động đến hiện tại theo cảm nhận là còn rất mới",
        "deep_explanation_vi": (
            "Đây là một trong những bẫy N4->N3 được cài trực tiếp vào Q#20 (したばかりだと vs してばかりいると). "
            "Hai cấu trúc cùng chứa chữ ばかり nhưng chỉ cần sai dạng chia động từ đứng trước (Vた vs Vて) là nghĩa rẽ sang hai hướng hoàn toàn đối lập: "
            "したばかり = vừa mới làm xong; してばかりいる = cứ làm suốt ngày không ngừng."
        ),
        "register_tag": "Trung tính",
        "confusable_pairs": [
            {
                "rival_pattern": "Vた + ばかりだ vs Vて + ばかりいる",
                "difference_vi": "Vた+ばかり = vừa mới làm xong (thời điểm); Vて+ばかりいる = suốt ngày chỉ toàn làm (tần suất lặp lại gây phàn nàn).",
                "quick_test_vi": "Có từ chỉ mức độ lặp lại '毎日 / そんなに' (Q#20, Q#55) -> Vてばかりいる; có từ chỉ thời gian mới qua 'さっき / 先月' -> Vたばかり.",
            }
        ],
        "examples": [
            {
                "jp": "さっき日本に着いたばかりだ。",
                "reading_note": "さっきにほんについたばかりだ。",
                "vi": "Tôi vừa mới đặt chân tới Nhật lúc nãy.",
                "grammar_note": "Vた (着いた) + ばかりだ chỉ việc vừa mới xảy ra.",
            },
            {
                "jp": "上司から「余裕を持って来るように」と言われたばかりなのに、また遅刻しそうだ。",
                "reading_note": "じょうしから「よゆうをもってくるように」といわれたばかりなのに、またちこくしそうだ。",
                "vi": "Vừa mới bị sếp nhắc 'hãy đi sớm dư dả thời gian' thế mà lại sắp muộn.",
                "grammar_note": "Bị động Vられた + ばかり chỉ sự việc mới diễn ra gần đây.",
            },
        ],
        "source_ref": "Shin-N3-List #68 | Kosei p.10 | Đề .xlsx (Q20)",
        "search_keywords": "ta bakari da vua moi たばかり ばかりだ ばかりの",
        "match_patterns": ["たばかり", "したばかり"],
    },
    {
        "code": "GP-N4-23",
        "pattern": "Kính ngữ N4->N3 nền tảng (おVになる / おVください / ごN・おVする)",
        "jlpt_level": "N4",
        "category": "keigo",
        "category_label_vi": CATEGORY_LABELS["keigo"],
        "in_exam_corpus": True,
        "formation_formula": "Tôn kính: お + Vます + になる / ください | Khiêm nhường: お + Vます + する / ご + N(Hán-Nhật) + する・いただく",
        "formation_table": [
            {"pos": "Tôn kính ngữ (Nâng đối phương)", "rule": "お + Vます + になる; お/ご + ください (お読みください, お越しください, ご確認ください, お待ちしています)"},
            {"pos": "Tôn kính đặc biệt hay thi", "rule": "いる/行く/来る -> いらっしゃる / お越しになる; 食べる/飲む -> 召し上がる; 見る -> ご覧になる"},
            {"pos": "Khiêm nhường ngữ (Hạ mình)", "rule": "お + Vます + する (お持ちになり, お返事ください); いただく (ご連絡いただく); 申し上げる"},
        ],
        "core_meaning_vi": "Thể hiện sự tôn trọng khách hàng/người trên trong thông báo, tờ rơi, email và hướng dẫn sử dụng",
        "deep_explanation_vi": (
            "Mặc dù đề Ngữ pháp câu đơn ít hỏi trực tiếp bảng kính ngữ, nhưng 100% bài Đọc hiểu kiểu tờ rơi/thông báo/email (Passages 1, 6, 7, 17, 21, 22 và câu Từ vựng Q#91: お召し上がりください) đều dùng kính ngữ. "
            "Không nhận diện được các động từ gốc đằng sau lớp vỏ kính ngữ (ví dụ お越しください = 来てください = hãy đến; お持ちになり = 持って = mang theo; ご確認ください = 確認してください = hãy kiểm tra) sẽ làm mất điểm Đọc hiểu dù câu hỏi rất dễ."
        ),
        "register_tag": "Kính ngữ / Công sở & Thông báo",
        "confusable_pairs": [
            {
                "rival_pattern": "おV + になる / ください (Tôn kính) vs おV + する (Khiêm nhường)",
                "difference_vi": "Chủ thể hành động là KHÁCH/ĐỐI PHƯƠNG dùng おVになる / おVください; Chủ thể hành động là BẢN THÂN MÌNH làm cho khách dùng おVする.",
                "quick_test_vi": "Trong tờ rơi bảo khách hàng làm gì -> luôn là お/ご〜ください hoặc ～ていただく (nhận được sự hợp tác của quý khách).",
            }
        ],
        "examples": [
            {
                "jp": "古本をお持ちになり、東京ボランティアセンターへお越しください。",
                "reading_note": "ふるほんをおもちになり、とうきょうぼらんてぃあせんたーへおこしください。",
                "vi": "Xin hãy mang theo sách cũ và đến Trung tâm tình nguyện Tokyo.",
                "grammar_note": "お持ちになり (= 持って) và お越しください (= 来てください) là cặp tôn kính ngữ trong tờ rơi.",
            },
            {
                "jp": "遠慮しないで、たくさんお召し上がりください。",
                "reading_note": "えんりょしないで、たくさんおめしあがりください。",
                "vi": "Xin đừng khách sáo, hãy dùng bữa thật nhiều nhé.",
                "grammar_note": "召し上がる là tôn kính ngữ của 食べる/飲む.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 | Đề .xlsx (Q91, Passages 1, 7, 17)",
        "search_keywords": "keigo ton kinh khiem nhuong お越しください ご確認 お持ちになり お召し上がり",
        "match_patterns": ["お読みください", "お越しください", "ご確認ください", "お召し上がり", "お持ちになり", "お買い上げ"],
    },
    {
        "code": "GP-N4-24",
        "pattern": "Câu hỏi tu từ & Xác nhận ～ではないだろうか / ～っけ",
        "jlpt_level": "N4",
        "category": "discourse",
        "category_label_vi": CATEGORY_LABELS["discourse"],
        "in_exam_corpus": True,
        "formation_formula": "普通形(N/Aな bỏ だ) + ではないだろうか / のではないだろうか | Vた/Nだ/Aかった + っけ",
        "formation_table": [
            {"pos": "～ではないだろうか", "rule": "Chẳng phải là... sao? (Câu hỏi tu từ khẳng định ý kiến tác giả một cách nhẹ nhàng)"},
            {"pos": "～はどうだろうか", "rule": "Làm như vậy thì sao nhỉ / Có nên chăng? (Đặt câu hỏi phản biện nhẹ ở cuối bài)"},
            {"pos": "～っけ (Shin #73)", "rule": "Ấy nhỉ? (Tự hỏi hoặc xác nhận lại thông tin mình từng biết nhưng hơi quên)"},
        ],
        "core_meaning_vi": "Khẳng định chủ trương tác giả dưới dạng câu hỏi tu từ mềm mại (～ではないだろうか) hoặc xác nhận ký ức (～っけ)",
        "deep_explanation_vi": (
            "Đây là dấu hiệu nhận biết KẾT LUẬN TÁC GIẢ (筆者の主張) số 1 trong Kosei Đọc hiểu và Đề thi (Passage 3: どうだろうか; Passage 4: 重要ではないだろうか; Passage 15: あいさつしているだろうか). "
            "Người học sơ cấp thường dịch ～ではないだろうか theo nghĩa đen thành 'có lẽ không phải sao?' rồi chọn nhầm đáp án phủ định! Thực chất đây là cách nói khẳng định rất lịch sự của văn nghị luận Nhật ('chẳng phải là rất quan trọng sao' = Rất quan trọng!)."
        ),
        "register_tag": "Văn viết nghị luận & Khẩu ngữ (っけ)",
        "confusable_pairs": [
            {
                "rival_pattern": "～ではないだろうか (Khẳng định nhẹ) vs ～ではない (Phủ định)",
                "difference_vi": "～ではない ở cuối câu là phủ định 'không phải'; nhưng thêm だろうか thành ～ではないだろうか lại là câu hỏi tu từ KHẲNG ĐỊNH quan điểm tác giả.",
                "quick_test_vi": "Ở câu cuối bài đọc hiểu thấy ～ではないだろうか? Đáp án đúng chính là mệnh đề khẳng định đứng ngay trước nó!",
            }
        ],
        "examples": [
            {
                "jp": "消費に合った量のマグロを捕るようにすることも重要ではないだろうか。",
                "reading_note": "しょうひにあったりょうのまぐろをとるようにすることもじゅうようではないだろうか。",
                "vi": "Việc đánh bắt lượng cá ngừ phù hợp với tiêu thụ chẳng phải cũng rất quan trọng sao?",
                "grammar_note": "Câu chốt đoạn 4 khẳng định chủ trương của tác giả bằng ではないだろうか.",
            },
            {
                "jp": "次の祝日っていつだっけ？来週だっけ？",
                "reading_note": "つぎのしゅくじつっていつだっけ？らいしゅうだっけ？",
                "vi": "Ngày lễ tiếp theo là khi nào ấy nhỉ? Là tuần sau ấy nhỉ?",
                "grammar_note": "～っけ dùng trong hội thoại khi xác nhận lại thông tin đã quên.",
            },
        ],
        "source_ref": "Shin-N3-List #73 | Kosei p.4 | Đề .xlsx (Q31, Q34, Passages 3, 4, 15)",
        "search_keywords": "de wa nai darou ka kke cau hoi tu tu ではないだろうか どうだろうか っけ",
        "match_patterns": ["ではないだろうか", "はどうだろうか", "だっけ"],
    },
]

# =========================================================================
# JLPT N3 CORE PART 1 (GP-N3-001 .. GP-N3-040)
# =========================================================================
GRAMMAR_POINTS_DATA.extend([
    {
        "code": "GP-N3-001",
        "pattern": "～うちに (Trong khi, tranh thủ lúc chưa biến đổi)",
        "jlpt_level": "N3",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": True,
        "formation_formula": "Vる / Vている / Vない / Aい / Aな+な / N+の + うちに",
        "formation_table": [
            {"pos": "Động từ (V)", "rule": "Vる / Vている / Vない + うちに (日本にいるうちに, 忘れないうちに)"},
            {"pos": "Tính từ い / な", "rule": "Aい + うちに (若いうちに); Aな + な + うちに (元気なうちに)"},
            {"pos": "Danh từ (N)", "rule": "N + の + うちに (独身のうちに, 朝のうちに)"},
        ],
        "core_meaning_vi": "Tranh thủ làm gì trong lúc trạng thái hiện tại vẫn còn duy trì (trước khi chuyển xấu/thay đổi), hoặc trong lúc đang làm A thì tự nhiên phát sinh B",
        "deep_explanation_vi": (
            "～うちに có 2 cách dùng cốt lõi ở N3: "
            "(1) Tranh thủ làm V2 trước khi trạng thái V1 kết thúc (như 若いうちに, 読書できるうちに trong Q#18 distractor; Vế sau thường là ý chí/lời khuyên). "
            "(2) Trong lúc đang diễn ra trạng thái V1 (như 聞いているうちに, 話しているうちに) thì biến cố/thay đổi tự nhiên B phát sinh (lúc nào không hay đã ngủ thiếp đi, trời tối sầm lại). "
            "Trong Q#18 ('秋は読書するのにとてもいい季節だ'), 読書できるうちに bị loại vì 'mùa thu thích hợp cho việc đọc sách' là đánh giá chung, không phải tranh thủ trước khi hết đọc được."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "～うちに vs ～間に (あいだに)",
                "difference_vi": "うちに mang sắc thái tranh thủ kẻo lỡ trước khi trạng thái thay đổi hoặc tự nhiên biến chuyển; 間に chỉ khoảng thời gian có giới hạn đầu-cuối rõ ràng (như trong kỳ nghỉ hè, khi vắng nhà).",
                "quick_test_vi": "Thấy 'trước khi nguội / trước khi quên / lúc còn trẻ' -> bắt buộc うちに; thấy khung giờ/thời gian cụ thể (昼休みの間) -> 間に.",
            }
        ],
        "examples": [
            {
                "jp": "日本にいるうちに、一度富士山に登ってみたい。",
                "reading_note": "にほんにいるうちに、いちどふじさんにのぼってみたい。",
                "vi": "Trong lúc còn đang ở Nhật, tôi muốn thử leo núi Phú Sĩ một lần.",
                "grammar_note": "Tranh thủ khoảng thời gian còn ở Nhật trước khi về nước -> うちに.",
            },
            {
                "jp": "音楽を聞いているうちに、眠ってしまった。",
                "reading_note": "おんがくをきいているうちに、ねむってしまった。",
                "vi": "Trong lúc đang nghe nhạc thì tôi ngủ thiếp đi mất.",
                "grammar_note": "Vている + うちに + biến đổi không chủ ý (眠ってしまった).",
            },
        ],
        "source_ref": "Shin-N3-List #1 | Đề .xlsx (Q18)",
        "search_keywords": "uchi ni trong khi tranh thu うちに いるうちに できるうちに",
        "match_patterns": ["うちに", "のうちに", "ないうちに"],
    },
    {
        "code": "GP-N3-002",
        "pattern": "～間 / ～間に (Trong suốt khoảng thời gian / Trong lúc)",
        "jlpt_level": "N3",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": True,
        "formation_formula": "Vる / Vている / Vない / Aい / Aな+な / N+の + 間（は） / 間に",
        "formation_table": [
            {"pos": "～間 (ずっと suốt)", "rule": "Hành động V2 kéo dài LIÊN TỤC suốt toàn bộ khoảng thời gian của V1 (寝ている間、ずっと…)"},
            {"pos": "～間に (trong lúc)", "rule": "Hành động tức thời V2 xảy ra tại MỘT thời điểm nằm trong khoảng V1 (留守の間に…)"},
            {"pos": "Cách nối danh từ", "rule": "N + の + 間 / 間に (夏休みの間, 4月17日から19日の間で)"},
        ],
        "core_meaning_vi": "Chỉ khoảng thời gian liên tục (間) hoặc điểm thời gian xen vào trong khoảng (間に)",
        "deep_explanation_vi": (
            "Điểm bẫy kinh điển giữa 間 và 間に nằm ở trợ từ に và bản chất hành động vế sau: "
            "Không có に (～間) thì vế sau phải là hành động/trạng thái kéo dài liên tục song song suốt thời gian đó (thường đi với ずっと). "
            "Có に (～間に) thì vế sau là một sự kiện xảy ra chớp nhoáng/một lần trong khoảng thời gian đó (như trộm lẻn vào nhà lúc vắng nhà, em bé ngủ nên mẹ tranh thủ nấu cơm). "
            "Trong Passage 6 cũng dùng khung thời gian danh từ '4月17日から19日の間で'."
        ),
        "register_tag": "Trung tính",
        "confusable_pairs": [
            {
                "rival_pattern": "～間 (không に) vs ～間に (có に)",
                "difference_vi": "間 = suốt từ đầu đến cuối khoảng thời gian; 間に = một điểm thời điểm xảy ra bên trong khoảng thời gian đó.",
                "quick_test_vi": "Vế sau có phó từ ずっと hoặc hành động kéo dài? Dùng 間. Vế sau là hành động dứt điểm 1 lần (入った, 終わった)? Dùng 間に.",
            }
        ],
        "examples": [
            {
                "jp": "彼は会議の間ずっと居眠りをしていた。",
                "reading_note": "かれはかいぎのあいだずっといねむりをしていた。",
                "vi": "Anh ta ngủ gật suốt cả buổi họp.",
                "grammar_note": "会議の間 + ずっと nhấn mạnh hành động kéo dài xuyên suốt cuộc họp.",
            },
            {
                "jp": "留守の間に泥棒が入った。",
                "reading_note": "るすのあいだにどろぼうがはいった。",
                "vi": "Trong lúc tôi vắng nhà đã có kẻ trộm lẻn vào.",
                "grammar_note": "Hành động xảy ra một lần trong lúc vắng nhà dùng 間に.",
            },
        ],
        "source_ref": "Shin-N3-List #2 | Đề .xlsx (Passage 6, Q137)",
        "search_keywords": "aida aida ni trong suot khoang thoi gian 間 間に あいだ",
        "match_patterns": ["の間", "の間に", "のあいだ"],
    },
    {
        "code": "GP-N3-003",
        "pattern": "～てからでないと / ～てからでなければ (Nếu không làm V1 trước thì khó mà V2)",
        "jlpt_level": "N3",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": False,
        "formation_formula": "Vて + からでないと / からでなければ + [V2 phủ định / không thể]",
        "formation_table": [
            {"pos": "Động từ (V)", "rule": "Vて + からでないと / からでなければ (chú ý giữ nguyên てから rồi mới nối でないと)"},
            {"pos": "Vế sau bắt buộc", "rule": "Thường là dạng phủ định, không thể, khó khăn (決められない, わからない, できない)"},
        ],
        "core_meaning_vi": "Nếu không làm xong hành động V1 làm điều kiện tiên quyết thì không thể thực hiện được V2",
        "deep_explanation_vi": (
            "～てからでないと kết hợp trình tự Vてから (sau khi làm V1) với điều kiện phủ định でないと (nếu không phải là...). "
            "Khác với câu điều kiện ～ないと thông thường, mẫu này nhấn mạnh THỨ TỰ BẮT BUỘC phải hoàn tất bước 1 thì bước 2 mới có thể diễn ra (phải bàn với gia đình xong mới quyết định được, phải đọc kỹ xong mới hiểu được). "
            "Vế sau hầu như luôn mang nghĩa phủ định hoặc bất khả năng."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vてからでないと vs Vないで",
                "difference_vi": "Vないで chỉ là 'không làm V1 mà vẫn làm V2'; Vてからでないと nhấn mạnh điều kiện tiên quyết 'nếu chưa làm xong V1 thì tuyệt đối không thể V2'.",
                "quick_test_vi": "Thấy vế sau là できない / わからない / 決められない kèm điều kiện phải làm xong bước 1 trước -> てからでないと.",
            }
        ],
        "examples": [
            {
                "jp": "家族と相談してからでないと、買うかどうかまだ決められない。",
                "reading_note": "かぞくとそうだんしてからでないと、かうかどうかまだきめられない。",
                "vi": "Nếu chưa bàn bạc với gia đình xong thì tôi vẫn chưa thể quyết định có mua hay không.",
                "grammar_note": "Vて (相談して) + からでないと + phủ định khả năng (決められない).",
            },
            {
                "jp": "実際に使ってみてからでなければ、この道具の良さはわからない。",
                "reading_note": "じっさいにつかってみてからでなければ、このどうぐのよさはわからない。",
                "vi": "Nếu không dùng thử trực tiếp trước thì không thể hiểu được cái hay của dụng cụ này.",
                "grammar_note": "Dạng trang trọng hơn là ～てからでなければ.",
            },
        ],
        "source_ref": "Shin-N3-List #3 | Sơ đồ N5-N1",
        "search_keywords": "te kara de nai to te kara de nakereba dieu kien tien quyet てからでないと てからでなければ",
        "match_patterns": ["てからでないと", "てからでなければ"],
    },
    {
        "code": "GP-N3-004",
        "pattern": "～とおり（に） / ～どおり（に） (Đúng theo như...)",
        "jlpt_level": "N3",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": True,
        "formation_formula": "Vる / Vた + とおり（に） | N + の + とおり（に） | N + どおり（に）",
        "formation_table": [
            {"pos": "Động từ (V)", "rule": "Vる / Vた + とおり（に） (思うとおりに, 私が言ったとおりに)"},
            {"pos": "Danh từ (N)", "rule": "N + の + とおり (下記の通り, 予定の通り) HOẶC ghép trực tiếp N + どおり (tạo biến âm ど: 予定どおり, 時刻表どおり)"},
            {"pos": "Quy tắc dấu đục", "rule": "Sau の giữ とおり (の通り); gắn thẳng vào Danh từ biến âm thành どおり!"},
        ],
        "core_meaning_vi": "Thực hiện hành động hoặc diễn ra sự việc giống hệt, khớp hoàn toàn theo một khuôn mẫu/lời nói/dự định sẵn",
        "deep_explanation_vi": (
            "Đây là bẫy ngữ âm & nối danh từ rất hay gặp trong bài thi: khi có trợ từ の ở giữa (下記の通り, 予想のとおり) thì đọc là とおり (không tenten); "
            "khi bỏ の và ghép thẳng vào danh từ (予定どおり, 説明書どおり, 時刻表どおり) thì đọc biến âm thành どおり! "
            "Xuất hiện thường xuyên trong email/tờ rơi Đọc hiểu (Passage 6: 下記のとおり = như dưới đây; Passage 7: 下記の通りです; Kosei p.10: 時刻表通り)."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn bản hành chính)",
        "confusable_pairs": [
            {
                "rival_pattern": "N + の + とおり vs N + どおり",
                "difference_vi": "Cùng nghĩa 'theo như N', nhưng có の thì đọc とおり, ghép thẳng vào N thì biến âm thành どおり.",
                "quick_test_vi": "Soi câu đọc: 計画の(とおり) vs 計画(どおり).",
            }
        ],
        "examples": [
            {
                "jp": "今年の国際交流会に向けて、下記のとおり第1回目の会議を行います。",
                "reading_note": "ことしのこくさいこうりゅうかいにむけて、かきのとおりだいいっかいのかいぎをおこないます。",
                "vi": "Hướng tới buổi giao lưu năm nay, chúng tôi tổ chức cuộc họp lần 1 như dưới đây.",
                "grammar_note": "Danh từ 下記 + の + とおり là cụm cố định trong email/thông báo.",
            },
            {
                "jp": "人生は自分の思うとおりにはいかない。",
                "reading_note": "じんせいはじぶんのおもうとおりにはいかない。",
                "vi": "Cuộc đời không phải lúc nào cũng diễn ra theo đúng như mình nghĩ.",
                "grammar_note": "Động từ Vる (思う) + とおりにはいかない.",
            },
        ],
        "source_ref": "Shin-N3-List #5 | Đề .xlsx (Passages 6, 7)",
        "search_keywords": "toori doori theo nhu dung nhu とおり どおり 下記の通り",
        "match_patterns": ["のとおり", "の通り", "どおり", "と思うとおり"],
    },
    {
        "code": "GP-N3-005",
        "pattern": "～によって / ～による / ～によっては (Tùy theo; Bởi; Bằng cách; Do)",
        "jlpt_level": "N3",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": True,
        "formation_formula": "N + によって / により / によっては | N1 + による + N2",
        "formation_table": [
            {"pos": "1. Tùy thuộc vào", "rule": "N + によって + 違う / 異なる / さまざまだ / 分ける (大きさによって分ける, 人によって違う)"},
            {"pos": "2. Bởi (Tác nhân bị động)", "rule": "N + によって + V(bị động) (植物が出す水分によって冷やされている)"},
            {"pos": "3. Bằng cách / Phương pháp", "rule": "N / Vること + によって (外国語を学ぶことによって hiểu được...)"},
            {"pos": "4. Do (Nguyên nhân)", "rule": "N(sự cố/thiên tai) + によって / により (台風によって電車が止まった)"},
            {"pos": "5. Bổ nghĩa danh từ", "rule": "N1 + による + N2 (tuyệt đối không dùng *によっての N2!)"},
        ],
        "core_meaning_vi": "Đa nghĩa theo ngữ cảnh: Tùy thuộc vào tiêu chí (1), Tác nhân câu bị động (2), Phương tiện/cách thức (3) hoặc Nguyên nhân (4)",
        "deep_explanation_vi": (
            "～によって là mẫu ngữ pháp N3 đa năng nhất, thi cả trong 問題1 (Q#16: 大きさによって三つに分けてください) lẫn 問題3 (Q#151: 水分によって冷やされている) và Bài đọc (Passage 5: 国や地域によって; Passage 9: 人によって違い). "
            "Mẹo phân biệt 4 nghĩa trong 3 giây: (1) Vế sau có 違う/異なる/分ける/さまざま -> 'Tùy theo'. (2) Vế sau chia thể Bị động -> 'Bởi/Nhờ tác nhân'. "
            "Lưu ý Q#156: không nối Vる + ことによる ở cuối mệnh đề làm động từ thay ことがある. Ngoài ra khi bổ nghĩa danh từ dùng による, không dùng によっての."
        ),
        "register_tag": "Trung tính & Văn viết trang trọng",
        "confusable_pairs": [
            {
                "rival_pattern": "～によって vs ～に対して vs ～にとって vs ～によると",
                "difference_vi": "によって = tùy vào / bởi tác nhân; に対して = đối với / trái ngược với; にとって = xét từ lập trường của ai; によると = theo như nguồn tin nghe nói.",
                "quick_test_vi": "Vế sau là Bị động hay 違う/分ける -> によって; Có 'nói/nghe nói' ở cuối câu -> によると; Đánh giá chủ quan 'quan trọng/khó' -> にとって.",
            }
        ],
        "examples": [
            {
                "jp": "大きさによって三つに分けてください。",
                "reading_note": "おおきさによってみっつにわけてください。",
                "vi": "Hãy phân thành ba nhóm tùy theo kích cỡ.",
                "grammar_note": "Q#16: によって chỉ tiêu chí phân loại (khác に比べて/について/に対して).",
            },
            {
                "jp": "窓から入ってくる風は植物が出す水分によって冷やされている。",
                "reading_note": "まどからはいってくるかぜはしょくぶつがだすすいぶんによってひやされている。",
                "vi": "Luồng gió thổi qua cửa sổ được làm mát bởi hơi nước do cây tỏa ra.",
                "grammar_note": "Q#151: động từ bị động 冷やされている chốt tác nhân bằng によって.",
            },
        ],
        "source_ref": "Shin-N3-List #6, #20 | anki #16 | Đề .xlsx (Q16, Q151, Q156, Passages 5, 9)",
        "search_keywords": "ni yotte ni yoru ni yotte wa tuy theo boi tac nhan によって による により",
        "match_patterns": ["によって", "によっては", "による", "により"],
    },
    {
        "code": "GP-N3-006",
        "pattern": "～たびに (Cứ mỗi lần... lại...)",
        "jlpt_level": "N3",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": False,
        "formation_formula": "Vる / N + の + たびに",
        "formation_table": [
            {"pos": "Động từ (V)", "rule": "Vる + たびに (Cấm dùng Vた! Đúng: 会うたびに, 行くたびに; Sai: *会ったたびに)"},
            {"pos": "Danh từ (N)", "rule": "N + の + たびに (試合のたびに, 旅行のたびに)"},
        ],
        "core_meaning_vi": "Diễn tả một sự việc B luôn lặp đi lặp lại không ngoại lệ mỗi khi A xảy ra ('cứ hễ A là lại B')",
        "deep_explanation_vi": (
            "Lỗi hình thái kinh điển nhất của ～たびに là chia động từ ở thì quá khứ Vた: vì diễn tả quy luật lặp đi lặp lại mỗi lần, trước たびに BẮT BUỘC là thể từ điển Vる hoặc Danh từ + の. "
            "Không dùng ～たびに cho những chuyện chỉ xảy ra 1 lần hay tần suất hằng ngày quá vụn vặt (như *朝起きるたびに顔を洗う nghe không tự nhiên — phải là sự kiện có tần suất rời rạc như đi du lịch, nghe bài hát đó, gặp lại bạn cũ)."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vる + たびに vs Vる/Vた + ときに",
                "difference_vi": "たびに nhấn mạnh sự LẶP LẠI đều đặn ('cứ mỗi lần...'); ときに chỉ một thời điểm chung chung hoặc sự kiện một lần.",
                "quick_test_vi": "Có từ gợi ý '毎回 / いつも' (lần nào cũng) và V đứng trước là Vる -> chọn たびに.",
            }
        ],
        "examples": [
            {
                "jp": "山に登るたびに、新しい発見がある。",
                "reading_note": "やまにのぼるたびに、あたらしいはっけんがある。",
                "vi": "Cứ mỗi lần leo núi lại có một phát hiện mới.",
                "grammar_note": "Vる (登る) + たびに; không chia 登ったたびに.",
            },
            {
                "jp": "この曲を聞くたびに、大学時代を思い出す。",
                "reading_note": "このきょくをきくたびに、だいがくじだいをおもいだす。",
                "vi": "Cứ mỗi lần nghe bản nhạc này tôi lại nhớ về thời đại học.",
                "grammar_note": "Lặp lại cảm xúc khi tác nhân xảy ra.",
            },
        ],
        "source_ref": "Shin-N3-List #7 | Sơ đồ N5-N1",
        "search_keywords": "tabi ni cu moi lan たびに のたびに",
        "match_patterns": ["たびに"],
    },
    {
        "code": "GP-N3-007",
        "pattern": "～ば～ほど (Càng... càng...)",
        "jlpt_level": "N3",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": False,
        "formation_formula": "[Động từ/Tính từ chia thể ば] + [Lặp lại đúng từ đó thể từ điển] + ほど (Hoặc lược vế đầu: N/Vる + ほど)",
        "formation_table": [
            {"pos": "Động từ (V)", "rule": "Vば + Vる + ほど (増えれば増えるほど, 読めば読むほど)"},
            {"pos": "Tính từ い", "rule": "Aければ + Aい + ほど (高ければ高いほど, 難しければ難しいほど)"},
            {"pos": "Tính từ な", "rule": "Aななら（であれば） + Aなな + ほど (静かなら静かなほど)"},
            {"pos": "Dạng rút gọn (Kosei p.6)", "rule": "Thường gặp trong văn đọc hiểu: Vる/N + ほど (多く飲む人ほどしみができにくい)"},
        ],
        "core_meaning_vi": "Biểu thị mức độ ở vế sau tăng/giảm tỷ lệ thuận với mức độ của vế trước ('càng A thì càng B')",
        "deep_explanation_vi": (
            "Khi dùng đầy đủ cả cặp, vế đầu chia thể ば và vế sau lặp lại chính động từ/tính từ đó ở thể thông thường + ほど (không dùng thể quá khứ Vた). "
            "Trong văn viết đọc hiểu N3 (như Kosei p.6: 'コーヒーを多く飲む人ほど、肌のしみができにくい'), vế ば hay được lược bỏ chỉ còn [Cụm danh từ/Động từ + ほど]."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "～ば～ほど vs ～につれて",
                "difference_vi": "～ば～ほど chỉ quy luật tỷ lệ thuận tổng quát (càng học càng thấy thú vị); ～につれて mô tả một sự biến đổi đang thực sự diễn ra theo thời gian.",
                "quick_test_vi": "Thấy cấu trúc lặp 2 từ giống nhau (増えれば増える...) -> chắc chắn là ほど.",
            }
        ],
        "examples": [
            {
                "jp": "物が増えれば増えるほど、片付けが大変になる。",
                "reading_note": "ものがふえればふえるほど、かたづけがたいへんになる。",
                "vi": "Đồ đạc càng nhiều lên thì việc dọn dẹp càng trở nên vất vả.",
                "grammar_note": "Động từ 増える chia ば (増えれば) + nguyên thể (増える) + ほど.",
            },
            {
                "jp": "コーヒーを多く飲む人ほど、肌のしみができにくい。",
                "reading_note": "こーひーをおおくのむひとほど、はだのしみができにくい。",
                "vi": "Người uống cà phê càng nhiều thì càng khó bị nám da.",
                "grammar_note": "Dạng rút gọn bỏ vế ば rất hay gặp trong bài đọc hiểu.",
            },
        ],
        "source_ref": "Shin-N3-List #8 | Kosei p.6",
        "search_keywords": "ba hodo cang cang ば ほど 飲めば飲むほど",
        "match_patterns": ["ば.*ほど", "れば.*ほど", "なればなるほど"],
    },
    {
        "code": "GP-N3-008",
        "pattern": "～ついでに (Nhân tiện, tiện thể)",
        "jlpt_level": "N3",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": False,
        "formation_formula": "Vる / Vた / N + の + ついでに",
        "formation_table": [
            {"pos": "Động từ (V)", "rule": "Vる (sắp làm việc chính) hoặc Vた (đã làm việc chính rồi tiện thể làm luôn) + ついでに"},
            {"pos": "Danh từ (N)", "rule": "N(hành động) + の + ついでに (散歩のついでに, 買い物のついでに)"},
        ],
        "core_meaning_vi": "Lợi dụng cơ hội đang làm việc chính A để làm ghép thêm việc phụ B ('nhân tiện A thì làm luôn B')",
        "deep_explanation_vi": (
            "Trong ～ついでに, A luôn là việc CHÍNH có chủ đích, còn B là việc PHỤ nhẹ nhàng tranh thủ làm kèm (như nhân tiện đi dạo thì bỏ thư vào hòm, nhân tiện đi công tác thì ghé thăm bạn). "
            "Không dùng ついでに khi hai việc hoàn toàn do tình cờ không chủ ý, và không dùng ngược việc phụ đứng trước việc chính."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "～ついでに vs ～かわりに",
                "difference_vi": "ついでに là làm THÊM cả 2 việc (A là chính + làm thêm B); かわりに là làm B THAY THẾ cho A (không làm A) hoặc bù đắp trao đổi.",
                "quick_test_vi": "Thấy 'đi siêu thị rồi mua giúp chai nước' -> ついでに; 'nghỉ làm việc này để làm việc kia' -> かわりに.",
            }
        ],
        "examples": [
            {
                "jp": "散歩のついでに、このはがきをポストに出してきた。",
                "reading_note": "さんぽのついでに、このはがきをぽすとにだしてきた。",
                "vi": "Nhân tiện đi dạo, tôi đã bỏ tấm bưu thiếp này vào hòm thư.",
                "grammar_note": "Danh từ hành động 散歩 + の + ついでに.",
            },
            {
                "jp": "東京へ出張したついでに、学生時代の友人に会った。",
                "reading_note": "とうきょうへしゅっちょうしたついでに、がくせいじだいのゆうじんにあった。",
                "vi": "Nhân tiện đi công tác Tokyo, tôi đã gặp người bạn thời đại học.",
                "grammar_note": "Vた + ついでに diễn tả việc phụ ghép thêm trong chuyến đi chính.",
            },
        ],
        "source_ref": "Shin-N3-List #9 | Sơ đồ N5-N1",
        "search_keywords": "tsuideni nhan tien tien the ついでに のついでに",
        "match_patterns": ["ついでに"],
    },
    {
        "code": "GP-N3-009",
        "pattern": "～くらい / ～ぐらい (Cỡ khoảng; Chí ít; Đến mức)",
        "jlpt_level": "N3",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": True,
        "formation_formula": "V普通形 / Aい / Aな+な / N + くらい / ぐらい",
        "formation_table": [
            {"pos": "Cỡ khoảng / Mức độ nhỏ (Chí ít)", "rule": "N + くらい / ぐらい (日曜日ぐらい休ませて, あいさつぐらいしかできない)"},
            {"pos": "Ước lượng tương đương", "rule": "Danh từ/Cụm số lượng + ぐらい (40才ぐらい, 同じぐらい, 聞いている人もいるくらい)"},
            {"pos": "Đến mức (tương đương ほど)", "rule": "Vる/Vない + くらい (毎日食べたいくらいだ, 動けないくらい疲れた)"},
        ],
        "core_meaning_vi": "Chỉ mức độ ước lượng ('cỡ khoảng'), mức tối thiểu khiêm tốn ('ít ra là / chỉ cỡ') hoặc mức độ cao ('đến mức')",
        "deep_explanation_vi": (
            "～くらい / ～ぐらい trong đề thi (Q#157 distractor; Passage 3: 周りの人に聞こえるくらい大音量で; Passage 14: 40才ぐらい; Passage 15: 同じぐらい; Passage 19: あいさつぐらいしか) thường mang 2 sắc thái: "
            "1) Hạ thấp mức độ xuống tối thiểu ('chỉ cỡ mức chào hỏi thôi', 'ít nhất ngày chủ nhật'). "
            "2) So sánh mức độ cao ('to đến mức người xung quanh cũng nghe thấy'). "
            "Lưu ý trong Q#157 ('前向きな考え方 [5] が必要'), không dùng くらい vì くらい sẽ hạ thấp ý nghĩa thành 'chỉ cỡ đó', làm yếu khẳng định của tác giả (phải dùng こそ)."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "～くらい vs ～ほど vs ～こそ",
                "difference_vi": "くらい ước lượng hoặc hạ nhẹ mức tối thiểu; ほど nhấn mạnh mức độ cao/cỡ lớn hơn trong văn viết; こそ nhấn mạnh khẳng định tuyệt đối chủ thể ('chính là').",
                "quick_test_vi": "Thấy 'chỉ cỡ / ít nhất cũng' hoặc đứng trước しか -> くらい; nhấn mạnh khẳng định kết luận cuối bài -> こそ.",
            }
        ],
        "examples": [
            {
                "jp": "周りの人に聞こえるくらい大音量で聞いている人もいる。",
                "reading_note": "まわりのひとにきこえるくらいだいおんりょうできいているひともいる。",
                "vi": "Cũng có người nghe với âm lượng lớn đến mức người xung quanh cũng nghe thấy.",
                "grammar_note": "Vる (聞こえる) + くらい mô tả mức độ âm lượng lớn.",
            },
            {
                "jp": "僕はあいさつぐらいしかドイツ語はできません。",
                "reading_note": "ぼくはあいさつぐらいしかどいつごはできません。",
                "vi": "Tôi chỉ nói được tiếng Đức cỡ mấy câu chào hỏi thôi.",
                "grammar_note": "あいさつ + ぐらい + しか nhấn mạnh mức tối thiểu ít ỏi.",
            },
        ],
        "source_ref": "Shin-N3-List #9, #10 | Đề .xlsx (Q157, Passages 3, 14, 15, 19)",
        "search_keywords": "kurai gurai co khoang chi it den muc くらい ぐらい",
        "match_patterns": ["くらい", "ぐらい"],
    },
    {
        "code": "GP-N3-010",
        "pattern": "～ほど (Đến mức; Không gì bằng; Cỡ bằng)",
        "jlpt_level": "N3",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": True,
        "formation_formula": "Vる/Vない / Aい / N + ほど | N + ほど + A/V + もの/人はいない (Không gì bằng)",
        "formation_table": [
            {"pos": "Mức độ cao (Đến mức)", "rule": "Vる / Aい + ほど (おどろくほど便利だ, 泣きたいほど嬉しい)"},
            {"pos": "So sánh nhất (Không gì bằng)", "rule": "N1 + ほど + A + N2 + はない (テストほどいやなものはない)"},
            {"pos": "So sánh phủ định (Không bằng)", "rule": "N1 + ほど + Phủ định (今年は去年ほど暑くない)"},
        ],
        "core_meaning_vi": "Diễn tả mức độ cao đáng kể ('đến mức...'), so sánh bằng phủ định ('không... bằng') hoặc nhất ('không gì... bằng')",
        "deep_explanation_vi": (
            "So với くらい, ほど có sắc thái trang trọng hơn và thường thiên về mức độ CAO / ĐÁNG KỂ (như Q#96 distractor: おどろくほど便利だ = tiện đến mức đáng kinh ngạc). "
            "Khi gặp cấu trúc so sánh phủ định [Aは Bほど ～ない] nghĩa là 'A không bằng B'. "
            "Trong Q#157 ('考え方 [5] が...必要なのだろう'), loại ほど vì ほど không gắn sau danh từ để đóng vai trò chủ ngữ khẳng định tuyệt đối như こそが."
        ),
        "register_tag": "Trung tính & Văn viết",
        "confusable_pairs": [
            {
                "rival_pattern": "N1 + ほど + A + はない vs N1 + ほど + A + ない",
                "difference_vi": "Có danh từ phạm trù + はない (như 嫌なものはない) = 'không có gì đáng ghét bằng N1' (so sánh nhất); không có danh từ sau tính từ (暑くない) = 'không nóng bằng N1'.",
                "quick_test_vi": "Để ý từ sau tính từ: có '...ものはない / ...人はいない' -> nhất; chỉ có đuôi phủ định -> kém hơn.",
            }
        ],
        "examples": [
            {
                "jp": "テストほどいやなものはない。",
                "reading_note": "てすとほどいやなものはない。",
                "vi": "Không có thứ gì đáng ghét bằng thi cử.",
                "grammar_note": "N + ほど + A + ものはない biểu đạt mức độ cao nhất.",
            },
            {
                "jp": "今年は去年ほど寒くない。",
                "reading_note": "ことしはきょねんほどさむくない。",
                "vi": "Năm nay không lạnh bằng năm ngoái.",
                "grammar_note": "So sánh hơn kém dùng ほど + tính từ phủ định.",
            },
        ],
        "source_ref": "Shin-N3-List #11 | Đề .xlsx (Q96, Q157)",
        "search_keywords": "hodo den muc khong bang khong gi bang ほど おどろくほど",
        "match_patterns": ["ほど", "ほどではない", "ほどいやな"],
    },
    {
        "code": "GP-N3-011",
        "pattern": "～くらいなら (Nếu phải làm V1 thì thà V2 còn hơn)",
        "jlpt_level": "N3",
        "category": "contrast_concession",
        "category_label_vi": CATEGORY_LABELS["contrast_concession"],
        "in_exam_corpus": False,
        "formation_formula": "Vる / Vない + くらいなら / ぐらいなら + ～ほうがましだ / ～ほうがいい",
        "formation_table": [
            {"pos": "Vế trước (Phương án ghét)", "rule": "Vる / Vない + くらいなら (Nếu phải rơi vào cảnh V1...)"},
            {"pos": "Vế sau (Hô ứng)", "rule": "Thường đi với ほうがましだ (thà chịu V2 còn hơn) hoặc ほうがいい"},
        ],
        "core_meaning_vi": "Bày tỏ thái độ từ chối gay gắt phương án A: nếu buộc phải làm A thì thà chấp nhận B còn hơn",
        "deep_explanation_vi": (
            "Đây là cách nói mang cảm xúc mạnh để bác bỏ phương án đầu tiên. Cả A và B đều không hẳn là chuyện vui vẻ, nhưng người nói coi A tệ hại đến mức thà chọn B (ví dụ: thà đi bộ chứ không nhờ hắn chở). "
            "Lưu ý vế sau luôn mang ý kiến đánh giá mạnh như ～ほうがましだ, ～たいくらいだ."
        ),
        "register_tag": "Khẩu ngữ / Bày tỏ thái độ mạnh",
        "confusable_pairs": [
            {
                "rival_pattern": "Vる + くらいなら vs Vる + のなら",
                "difference_vi": "のなら là giả định trung tính ('nếu anh làm V thì...'); くらいなら là giả định cực đoan mang thái độ chê bai/ghét bỏ phương án trước đó ('nếu phải chịu nhục làm thế thì thà...').",
                "quick_test_vi": "Thấy vế sau có ほうがましだ -> bắt buộc chọn くらいなら.",
            }
        ],
        "examples": [
            {
                "jp": "あいつに助けてもらうくらいなら、自分でやったほうがましだ。",
                "reading_note": "あいつにたすけてもらうくらいなら、じぶんでやったほうがましだ。",
                "vi": "Nếu phải nhờ tên đó giúp thì thà tự mình làm lấy còn hơn.",
                "grammar_note": "Vる + くらいなら hô ứng với ほうがましだ.",
            },
            {
                "jp": "満員電車に乗るくらいなら、30分歩いたほうがいい。",
                "reading_note": "まんいんでんしゃにのるくらいなら、さんじゅっぷんあるいたほうがいい。",
                "vi": "Nếu phải chen chúc trên tàu đông nghẹt thì thà đi bộ 30 phút còn hơn.",
                "grammar_note": "Chọn phương án ít tệ hơn so với 満員電車に乗る.",
            },
        ],
        "source_ref": "Shin-N3-List #12 | Sơ đồ N5-N1",
        "search_keywords": "kurai nara hou ga mashi da tha con hon くらいなら ほうがましだ",
        "match_patterns": ["くらいなら", "ぐらいなら", "ほうがまし"],
    },
    {
        "code": "GP-N3-012",
        "pattern": "～に限る (Là nhất, không gì bằng)",
        "jlpt_level": "N3",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": False,
        "formation_formula": "Vる / Vない / N + に限る（にかぎる）",
        "formation_table": [
            {"pos": "Động từ (V)", "rule": "Vる / Vない + に限る (映画は映画館で見るに限る, 寒い日は鍋を食べるに限る)"},
            {"pos": "Danh từ (N)", "rule": "N + に限る (夏はやっぱりビールに限る)"},
            {"pos": "Phân biệt với とは限らない", "rule": "～に限る (là tốt nhất - đánh giá chủ quan) ≠ ～とは限らない (chưa chắc đã đúng)"},
        ],
        "core_meaning_vi": "Khẳng định chủ quan của người nói rằng phương án hoặc sự vật đó là tốt nhất, thích hợp nhất",
        "deep_explanation_vi": (
            "Đừng bị mặt chữ 限 (Hạn) đánh lừa với とは限らない! "
            "Khi đứng ở thể khẳng định ～に限る, nó biểu thị sự lựa chọn số 1 theo kinh nghiệm/cảm nhận cá nhân ('cứ phải là... mới nhất'), thường đi kèm phó từ やっぱり / やはり. "
            "Chú ý không dùng cho sự thật khách quan (chỉ dùng cho ý kiến, gợi ý chủ quan)."
        ),
        "register_tag": "Hội thoại & Cảm nhận cá nhân",
        "confusable_pairs": [
            {
                "rival_pattern": "～に限る vs ～とは限らない",
                "difference_vi": "～に限る = 'làm cái này là nhất!' (khẳng định lựa chọn tốt nhất); ～とは限らない = 'không nhất thiết lúc nào cũng vậy' (phủ định sự tuyệt đối).",
                "quick_test_vi": "Có やっぱり và mang ý khuyên chọn món/cách tốt nhất -> に限る; có từ chỉ toàn thể (いつも・みんな) ở vế trước -> とは限らない.",
            }
        ],
        "examples": [
            {
                "jp": "やっぱり映画は映画館で見るに限る。",
                "reading_note": "やっぱりえいがはえいがかんでみるにかぎる。",
                "vi": "Quả nhiên xem phim cứ phải xem ở rạp chiếu phim là nhất.",
                "grammar_note": "Vる (見る) + に限る đi cùng やっぱり.",
            },
            {
                "jp": "疲れたときは、早く寝るに限りますよ。",
                "reading_note": "つかれたときは、はやくねるにかぎりますよ。",
                "vi": "Những lúc mệt mỏi thì đi ngủ sớm là tốt nhất đấy.",
                "grammar_note": "Khuyên phương án tối ưu theo kinh nghiệm.",
            },
        ],
        "source_ref": "Shin-N3-List #13 | Sơ đồ N5-N1",
        "search_keywords": "ni kagiru la nhat やっぱり に限る にかぎる",
        "match_patterns": ["に限る", "に限ります", "にかぎる"],
    },
    {
        "code": "GP-N3-013",
        "pattern": "～に対して / ～のに対して / ～に対する (Đối với / Trái ngược với)",
        "jlpt_level": "N3",
        "category": "contrast_concession",
        "category_label_vi": CATEGORY_LABELS["contrast_concession"],
        "in_exam_corpus": True,
        "formation_formula": "N + に対して / に対する + N | 普通形(N/Aな + な) + のに対して",
        "formation_table": [
            {"pos": "Nghĩa 1: Đối với (Hướng tác động)", "rule": "N + に対して / に対する + N (目上の人に対して敬語を使う, 質問に対する答え)"},
            {"pos": "Nghĩa 2: Trái ngược với (So sánh)", "rule": "Mệnh đề(V/Aい/Aなな/Nな) + のに対して (こちらの店が安いのに対して、あちらの店は…)"},
            {"pos": "Bổ nghĩa danh từ", "rule": "N1 + に対する + N2 (cấm dùng *に対しての N2)"},
        ],
        "core_meaning_vi": "Chỉ đối tượng tiếp nhận thái độ/hành động ('đối với N') hoặc đối chiếu hai vế tương phản ('trong khi A thì ngược lại B')",
        "deep_explanation_vi": (
            "～に対して xuất hiện liên tiếp trong đề thi (Q#53 là đáp án đúng, Q#16 và Q#54 là phương án nhiễu). "
            "Hai bẫy cần nắm chắc: "
            "1) Phân biệt với ～にとって: [N + に対して] là hướng hành động/thái độ (nghiêm khắc, lễ phép, giải thích) VÀO đối tượng N; [N + にとって] là đứng TỪ góc nhìn của N để đánh giá ('đối với tôi bức ảnh này rất quý'). "
            "2) Khi nối giữa 2 mệnh đề trái ngược nhau (Q#53: 'こちらの店が安い [のに対して]、あちらの店は量が多い'), bắt buộc chèn の trước に対して (と dùng な sau Aな/N: 静かなのに対して)."
        ),
        "register_tag": "Trung tính & Văn viết",
        "confusable_pairs": [
            {
                "rival_pattern": "～に対して vs ～にとって vs ～によって",
                "difference_vi": "に対して = hướng thái độ/hành động vào N hoặc tương phản A vs B; にとって = đứng trên lập trường N để đánh giá; によって = tùy theo / bởi tác nhân.",
                "quick_test_vi": "Thấy 2 vế đối chiếu tính chất trái ngược (A安い vs B多い) -> のに対して; thấy đánh giá (大切/必要) -> にとって.",
            }
        ],
        "examples": [
            {
                "jp": "こちらの店が安いのに対して、あちらの店は量が多いことで評判だ。",
                "reading_note": "こちらのみせがやすいのにたいして、あちらのみせはりょうがおおいことでひょうばんだ。",
                "vi": "Trái ngược với quán bên này giá rẻ, quán bên kia lại nổi tiếng vì đồ ăn nhiều.",
                "grammar_note": "Q#53: tính từ い (安い) + のに対して đối chiếu 2 cửa hàng.",
            },
            {
                "jp": "目上の人に対しては、敬語を使うべきだ。",
                "reading_note": "めうえのひとにたいしては、けいごをつかうべきだ。",
                "vi": "Đối với người bề trên thì nên sử dụng kính ngữ.",
                "grammar_note": "N + に対して chỉ đối tượng nhận hành động/thái độ.",
            },
        ],
        "source_ref": "Shin-N3-List #14 | anki #13 | Đề .xlsx (Q16, Q53, Q54)",
        "search_keywords": "ni taishite no ni taishite doi voi trai nguoc に対して のに対して に対する",
        "match_patterns": ["に対して", "のに対して", "に対する"],
    },
    {
        "code": "GP-N3-014",
        "pattern": "～反面 (Nhưng mặt khác, trái lại)",
        "jlpt_level": "N3",
        "category": "contrast_concession",
        "category_label_vi": CATEGORY_LABELS["contrast_concession"],
        "in_exam_corpus": False,
        "formation_formula": "Vる/Vた/Aい / Aな+な/である / N+である + 反面（はんめん）",
        "formation_table": [
            {"pos": "Động từ / Tính từ い", "rule": "普通形 + 反面 (よく効く反面, 便利な反面)"},
            {"pos": "Tính từ な / Danh từ", "rule": "Aな + な / である + 反面; N + である / の + 反面"},
        ],
        "core_meaning_vi": "Nêu hai mặt đối lập (thường là ưu điểm vs nhược điểm) cùng tồn tại trong MỘT sự vật, sự việc duy nhất",
        "deep_explanation_vi": (
            "Điểm cốt lõi để phân biệt ～反面 với ～のに対して: "
            "～のに対して thường so sánh HAI chủ thể khác nhau (anh hoạt bát <-> em trầm tính; quán A rẻ <-> quán B nhiều). "
            "Ngược lại, ～反面 chỉ nói về HAI MẶT TỐT - XẤU của CÙNG MỘT ĐỐI TƯỢNG (thuốc công hiệu tốt nhưng tác dụng phụ mạnh; sống ở thành phố thú vị nhưng nhiều stress; máy tính tiện lợi nhưng hại mắt)."
        ),
        "register_tag": "Văn viết & Nghị luận",
        "confusable_pairs": [
            {
                "rival_pattern": "～反面 vs ～のに対して",
                "difference_vi": "反面 đối lập 2 khía cạnh (ưu/nhược) của CÙNG 1 sự vật; のに対して đối lập 2 đối tượng/sự vật KHÁC NHAU.",
                "quick_test_vi": "Cùng 1 chủ thể có cả mặt tích cực và tiêu cực -> 反面; 2 chủ thể A và B khác nhau -> のに対して.",
            }
        ],
        "examples": [
            {
                "jp": "この薬はよく効く反面、強い副作用もある。",
                "reading_note": "このくすりはよくきくはんめん、つよいふくさようもある。",
                "vi": "Loại thuốc này hiệu quả rất tốt nhưng mặt khác cũng có tác dụng phụ mạnh.",
                "grammar_note": "Cùng đối tượng この薬 vừa có ưu điểm (よく効く) vừa có nhược điểm (副作用).",
            },
            {
                "jp": "都会の生活は便利な反面、ストレスも多い。",
                "reading_note": "とかいのせいかつはべんりなはんめん、すとれすもおおい。",
                "vi": "Cuộc sống đô thị tuy tiện lợi nhưng mặt khác cũng nhiều căng thẳng.",
                "grammar_note": "Aな (便利) + な + 反面.",
            },
        ],
        "source_ref": "Shin-N3-List #15 | anki #39",
        "search_keywords": "hanmen mat khac trai lai 反面 はんめん",
        "match_patterns": ["反面"],
    },
    {
        "code": "GP-N3-015",
        "pattern": "～一方で / ～一方だ (Một mặt thì... mặt khác thì / Ngày càng...)",
        "jlpt_level": "N3",
        "category": "contrast_concession",
        "category_label_vi": CATEGORY_LABELS["contrast_concession"],
        "in_exam_corpus": True,
        "formation_formula": "[Song song/Tương phản] 普通形(Aなな/Nの・である) + 一方で | [Xu hướng một chiều] Vる(biến đổi) + 一方だ",
        "formation_table": [
            {"pos": "1. ～一方で (Mặt khác)", "rule": "Diễn tả 2 mặt song song hoặc tương phản (Trong Passage 2: 一方で、古典や歴史は役に立たないと言う人も増えている)"},
            {"pos": "2. Vる + 一方だ (Càng ngày càng)", "rule": "Xu hướng biến đổi liên tục theo MỘT CHIỀU duy nhất (増える一方だ, 悪くなる一方だ)"},
        ],
        "core_meaning_vi": "Một mặt thì A, mặt khác thì B (一方で); hoặc một xu hướng tăng/giảm liên tục theo một chiều (一方だ)",
        "deep_explanation_vi": (
            "Cần phân biệt rạch ròi 2 dạng kết thúc của chữ 一方: "
            "1) Ở giữa câu (～一方で): nối 2 vế song hành hoặc tương phản nhau (giống Passage 2: các môn thực dụng được coi trọng, MẶT KHÁC người chê cổ văn cũng tăng). "
            "2) Ở cuối câu (Vる + 一方だ): CHỈ đi với động từ biến đổi (増える, 減る, 悪化する, 高くなる) để diễn tả xu thế dốc một chiều ngày càng trầm trọng (thường mang nghĩa tiêu cực)."
        ),
        "register_tag": "Văn viết & Thời sự",
        "confusable_pairs": [
            {
                "rival_pattern": "Vる + 一方だ vs Vます + つつある",
                "difference_vi": "Cả hai đều chỉ xu hướng biến đổi, nhưng 一方だ nhấn mạnh đà trượt theo 1 chiều ngày càng mạnh (thường tiêu cực), còn つつある mô tả sự thay đổi đang diễn ra dần dần (trung tính, giống 減りつつあります trong Q#150).",
                "quick_test_vi": "Thấy ở giữa câu nối 2 ý đối lập -> 一方で; ở cuối câu sau Vる biến đổi -> 一方だ.",
            }
        ],
        "examples": [
            {
                "jp": "一方で、古典や歴史などの科目は勉強する必要がないと言う人も増えているそうだ。",
                "reading_note": "いっぽうで、こてんやれきしなどのかもくはべんきょうするひつようがないというひともふえているそうだ。",
                "vi": "Mặt khác, nghe nói ngày càng nhiều người bảo các môn như cổ văn hay lịch sử không cần học.",
                "grammar_note": "Passage 2: 一方で đặt đầu câu chuyển sang quan điểm đối lập.",
            },
            {
                "jp": "不景気で失業者は増える一方だ。",
                "reading_note": "ふけいきでしつぎょうしゃはふえるいっぽうだ。",
                "vi": "Do kinh tế suy thoái, số người thất nghiệp ngày càng tăng thêm.",
                "grammar_note": "Vる biến đổi (増える) + 一方だ.",
            },
        ],
        "source_ref": "Shin-N3-List #16 | anki #40 | Đề .xlsx (Passage 2)",
        "search_keywords": "ippou de ippou da mot mat thi cang ngay cang 一方で 一方だ",
        "match_patterns": ["一方で", "一方だ", "一方です"],
    },
    {
        "code": "GP-N3-016",
        "pattern": "～というより (Nói là... thì đúng hơn là...)",
        "jlpt_level": "N3",
        "category": "contrast_concession",
        "category_label_vi": CATEGORY_LABELS["contrast_concession"],
        "in_exam_corpus": False,
        "formation_formula": "普通形 / N + というより（は） + [Cách diễn đạt chính xác hơn]",
        "formation_table": [
            {"pos": "V / A / N", "rule": "AというよりB (Anh ta nói là bạn thì đúng hơn là cấp trên / Nói là đi bộ thì đúng hơn là chạy)"},
            {"pos": "Lưu ý tính từ な/Danh từ", "rule": "Thường không cần だ trước というより (先生というより友だちみたいだ)"},
        ],
        "core_meaning_vi": "So sánh hai cách gọi A và B để khẳng định gọi là B thì chính xác hơn, sát bản chất hơn so với A",
        "deep_explanation_vi": (
            "Khi bạn phân vân mô tả một sự vật nằm giữa A và B, dùng [AというよりB] để hạ A xuống và đề cao B là cách diễn đạt chuẩn xác hơn. "
            "Ví dụ: 'Cô ấy nói là tiết kiệm thì đúng hơn là keo kiệt' hoặc 'đi nhanh đến mức giống chạy hơn là đi bộ'."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "AというよりB vs AかわりにB",
                "difference_vi": "というより dùng để CHỌN CÁCH DIỄN ĐẠT chuẩn xác hơn giữa A và B cho cùng 1 đối tượng; かわりに là THAY THẾ hành động/vật A bằng B.",
                "quick_test_vi": "Vế trước và sau cùng mô tả một tính chất/định danh của cùng 1 người/vật -> というより.",
            }
        ],
        "examples": [
            {
                "jp": "彼女は歩くのが速くて、歩くというより走っているようだ。",
                "reading_note": "かのじょはあるくのがはやくて、あるくというよりはしっているようだ。",
                "vi": "Cô ấy đi bộ nhanh đến mức nói là đang chạy thì đúng hơn là đi bộ.",
                "grammar_note": "So sánh 2 cách miêu tả 歩く vs 走っている.",
            },
            {
                "jp": "あの人は上司というより、頼りになる兄のような存在だ。",
                "reading_note": "あのひとはじょうしというより、たよりになるあにのようなそんざいだ。",
                "vi": "Người đó nói là một người anh đáng tin cậy thì đúng hơn là cấp trên.",
                "grammar_note": "Danh từ trực tiếp + というより.",
            },
        ],
        "source_ref": "Shin-N3-List #17 | Sơ đồ N5-N1",
        "search_keywords": "to iu yori noi la thi dung hon というより",
        "match_patterns": ["というより"],
    },
    {
        "code": "GP-N3-017",
        "pattern": "～かわりに / ～のかわりに (Thay cho; Bù lại)",
        "jlpt_level": "N3",
        "category": "contrast_concession",
        "category_label_vi": CATEGORY_LABELS["contrast_concession"],
        "in_exam_corpus": True,
        "formation_formula": "N + の + かわりに | Vる / Vた / Vない + かわりに",
        "formation_table": [
            {"pos": "1. Thay thế (Thay cho)", "rule": "N + の + かわりに / Vる + かわりに (先輩のかわりに, コーヒーのかわりに紅茶を飲む)"},
            {"pos": "2. Bù lại / Trao đổi có qua có lại", "rule": "V普通形 + かわりに (英語を教えてもらうかわりに、日本語を教える)"},
            {"pos": "3. Bù trừ ưu - nhược điểm", "rule": "Aい / Aな+な + かわりに (給料が高いかわりに、残業も多い)"},
        ],
        "core_meaning_vi": "Thay thế người/vật này bằng người/vật khác, hoặc bù trừ qua lại giữa hai hành động/điều kiện",
        "deep_explanation_vi": (
            "Mẫu này thi trực tiếp trong 問題2 ★ Q#57 ('けがをした先輩 [のかわり] [に] チームの代表として...') và dùng trong Kosei p.8 ('その代わりに'). "
            "Lưu ý hình thái: với Danh từ BẮT BUỘC có の (先輩のかわりに), còn với Động từ gắn thẳng thể thông thường không dùng の. "
            "Khi chỉ bù trừ đặc điểm (lương cao bù lại phải tăng ca nhiều), không có hàm ý thay thế người."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "N + のかわりに vs N + として",
                "difference_vi": "のかわりに = Đứng vào vị trí thay cho người/vật khác; として = Với tư cách, vai trò danh nghĩa của chính mình.",
                "quick_test_vi": "Trong Q#57 hai mẫu đi nối tiếp nhau: 先輩のかわりに (thay đàn anh) + チームの代表として (với tư cách đại diện đội).",
            }
        ],
        "examples": [
            {
                "jp": "けがをした先輩のかわりに、チームの代表として試合に出ることになった。",
                "reading_note": "けがをしたせんぱいのかわりに、ちーむのだいひょうとしてしあいにでることになった。",
                "vi": "Tôi sẽ ra thi đấu với tư cách đại diện đội thay cho đàn anh bị thương.",
                "grammar_note": "Q#57: Danh từ 先輩 + の + かわりに.",
            },
            {
                "jp": "この部屋は駅に近いかわりに、家賃が少し高い。",
                "reading_note": "このへやはえきにちかいかわりに、やちんがすこしたかい。",
                "vi": "Phòng này bù lại cho việc gần ga thì tiền thuê nhà hơi đắt một chút.",
                "grammar_note": "Aい (近い) + かわりに chỉ sự bù trừ ưu/nhược.",
            },
        ],
        "source_ref": "Shin-N3-List #18 | Kosei p.8 | Đề .xlsx (Q57)",
        "search_keywords": "kawari ni no kawari ni thay cho bu lai かわりに のかわりに 代わりに",
        "match_patterns": ["のかわりに", "代わりに", "かわりに"],
    },
    {
        "code": "GP-N3-018",
        "pattern": "～ことから (Bởi vì căn cứ từ... nên nhận ra / được gọi là)",
        "jlpt_level": "N3",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": False,
        "formation_formula": "普通形 (Aな + な/である, N + である/の) + ことから",
        "formation_table": [
            {"pos": "Động từ / Tính từ い", "rule": "普通形 + ことから (よく似ていることから, 富士山が見えることから)"},
            {"pos": "Tính từ な / Danh từ", "rule": "Aな + な/である + ことから; N + である / (lược だ) + ことから"},
            {"pos": "Vế sau đặc trưng", "rule": "Đưa ra phán đoán suy luận (とわかった) hoặc giải thích nguồn gốc tên gọi (と呼ばれている)"},
        ],
        "core_meaning_vi": "Từ một dấu hiệu/sự kiện làm căn cứ để suy ra kết luận hoặc giải thích nguồn gốc tên gọi",
        "deep_explanation_vi": (
            "Khác với から / ので chỉ nguyên nhân thông thường, ～ことから nêu DẤU HIỆU / CĂN CỨ KHÁCH QUAN giúp người ta nhận ra một sự thật hoặc đặt tên cho một nơi chốn/sự vật. "
            "Do đó vế sau gần như luôn có các động từ nhận thức hoặc gọi tên như ～とわかった, ～と言われている, ～と呼ばれるようになった. "
            "Không dùng ～ことから cho lời xin lỗi hay thỉnh cầu cá nhân."
        ),
        "register_tag": "Văn viết & Giải thích khách quan",
        "confusable_pairs": [
            {
                "rival_pattern": "～ことから vs ～ものだから",
                "difference_vi": "ことから dùng trong văn viết nêu căn cứ suy luận/nguồn gốc tên gọi khách quan; ものだから dùng trong khẩu ngữ để thanh minh, biện hộ lý do cá nhân.",
                "quick_test_vi": "Vế sau có ～と呼ばれる / ～とわかった -> ことから; có ～てしまった / 遅れてすみません -> ものだから.",
            }
        ],
        "examples": [
            {
                "jp": "顔がよく似ていることから、二人は親子だとすぐにわかった。",
                "reading_note": "かおがよくにていることから、ふたりはおやこだとすぐにわかった。",
                "vi": "Từ việc khuôn mặt rất giống nhau, tôi nhận ra ngay hai người là cha con.",
                "grammar_note": "Căn cứ quan sát 似ていることから dẫn đến suy luận わかった.",
            },
            {
                "jp": "富士山が見えることから、この町は富士見町と呼ばれている。",
                "reading_note": "ふじさんがみえることから、このまちはふじみちょうとよばれている。",
                "vi": "Từ việc có thể nhìn thấy núi Phú Sĩ nên thị trấn này được gọi là Fujimi.",
                "grammar_note": "Giải thích nguồn gốc tên gọi dùng ことから + と呼ばれている.",
            },
        ],
        "source_ref": "Shin-N3-List #21 | anki #9",
        "search_keywords": "koto kara can cu suy luan nguon goc ことから",
        "match_patterns": ["ことから"],
    },
    {
        "code": "GP-N3-019",
        "pattern": "～おかげで / ～おかげだ (Nhờ có - Kết quả tốt đẹp)",
        "jlpt_level": "N3",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": False,
        "formation_formula": "普通形(V/Aい / Aな+な / N+の) + おかげで / おかげだ",
        "formation_table": [
            {"pos": "Động từ / Tính từ い", "rule": "Vる/Vた/Aい + おかげで (早く治療したおかげで, 練習したおかげで)"},
            {"pos": "Tính từ な / Danh từ", "rule": "Aな + な + おかげで; N + の + おかげで (先生のおかげで, 冷房のおかげで)"},
            {"pos": "Sắc thái bắt buộc", "rule": "Vế sau PHẢI là kết quả TÍCH CỰC, biết ơn (tuyệt đối không dùng cho kết quả xấu trừ trường hợp nói mỉa mai)"},
        ],
        "core_meaning_vi": "Nhờ có nguyên nhân A mà đạt được kết quả tốt đẹp B (bày tỏ lòng biết ơn hoặc đánh giá tích cực)",
        "deep_explanation_vi": (
            "Đây là cặp đối lập kinh điển với ～せいで (Q#155): "
            "おかげで dùng 100% cho kết quả TỐT ĐẸP, may mắn (như Kosei p.8: '少ない資源のおかげでまじめな国民性が生まれた' hoặc Kosei p.11: '冷房のおかげで助けられている'). "
            "Khi danh từ đứng trước, nhớ chèn の (先生のおかげで) chứ không dùng だ."
        ),
        "register_tag": "Trung tính (Biết ơn & Tích cực)",
        "confusable_pairs": [
            {
                "rival_pattern": "～おかげで vs ～せいで",
                "difference_vi": "Cấu trúc chia giống hệt nhau, nhưng おかげで đi với kết quả TỐT ĐẸP (thi đỗ, khỏe lại, thành công), còn せいで đi với kết quả XẤU, đáng tiếc (muộn học, ấm ức, hỏng việc).",
                "quick_test_vi": "Kiểm tra cảm xúc cuối câu: vui/thành công/tốt -> おかげで; buồn/bực/rủi ro (くやしい, 遅刻) -> せいで.",
            }
        ],
        "examples": [
            {
                "jp": "私たちは暑い夏に冷房のおかげでいろいろ助けられている。",
                "reading_note": "わたしたちはあついなつにれいぼうのおかげでいろいろたすけられている。",
                "vi": "Vào mùa hè nóng nực, chúng ta được hỗ trợ rất nhiều nhờ có điều hòa.",
                "grammar_note": "Danh từ 冷房 + の + おかげで nêu nguyên nhân mang lại lợi ích.",
            },
            {
                "jp": "いい会社に就職できたのは先生のおかげです。",
                "reading_note": "いいかいしゃにしゅうしょくできたのはせんせいのおかげです。",
                "vi": "Việc tôi xin được vào công ty tốt là nhờ có thầy.",
                "grammar_note": "Đặt cuối câu dạng 先生のおかげです để cảm ơn.",
            },
        ],
        "source_ref": "Shin-N3-List #22 | Kosei p.8, p.11",
        "search_keywords": "okage de nho co ket qua tot おかげで おかげです",
        "match_patterns": ["おかげで", "おかげだ", "おかげです"],
    },
    {
        "code": "GP-N3-020",
        "pattern": "～せいで / ～せいだ (Tại vì - Kết quả tiêu cực, đổ lỗi)",
        "jlpt_level": "N3",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": True,
        "formation_formula": "普通形(V/Aい / Aな+な / N+の) + せいで / せいだ / せいか",
        "formation_table": [
            {"pos": "Động từ / Tính từ い", "rule": "Vる/Vた/Vない/Aい + せいで (わからないせいで, 忙しかったせいで)"},
            {"pos": "Tính từ な / Danh từ", "rule": "Aな + な + せいで; N + の + せいで (台風のせいで, 不注意のせいで)"},
            {"pos": "Dạng nghi vấn ～せいか", "rule": "Có lẽ tại vì... (dự đoán nguyên nhân gây ra trạng thái không ổn: 疲れているせいか...)"},
        ],
        "core_meaning_vi": "Tại vì nguyên nhân A mà dẫn đến kết quả tiêu cực, đáng tiếc hoặc bực bội B",
        "deep_explanation_vi": (
            "Mẫu này thi trực tiếp ở Bài Đục lỗ 3 Câu [3] (Q#155: '外国人が言った冗談が [わからないせいで] 自分だけ笑えないのがくやしかったからですよ'). "
            "Nhờ từ khóa cảm xúc tiêu cực 'くやしかった' (ấm ức, bực mình) ở cuối câu, ta chốt ngay わからないせいで mà không bị nhiễu bởi câu điều kiện なら hay sai nghĩa 聞こえなかったために. "
            "Lưu ý: không dùng せいで cho kết quả tốt đẹp."
        ),
        "register_tag": "Trung tính (Tiêu cực / Than phiền)",
        "confusable_pairs": [
            {
                "rival_pattern": "～せいで vs ～おかげで vs ～ために",
                "difference_vi": "せいで = tại vì (chỉ kết quả xấu, hàm ý đổ lỗi/tiếc nuối); おかげで = nhờ có (kết quả tốt); ために = trung tính trang trọng (vì lý do...).",
                "quick_test_vi": "Có cảm xúc hối tiếc, ấm ức, trách móc ở vế sau (くやしい, 失敗した) -> ưu tiên せいで.",
            }
        ],
        "examples": [
            {
                "jp": "外国人が言った冗談がわからないせいで、自分だけ笑えないのがくやしかった。",
                "reading_note": "がいこくじんがいったじょうだんがわからないせいで、じぶんだけわらえないのがくやしかった。",
                "vi": "Tại vì không hiểu câu nói đùa của người nước ngoài nên chỉ mình tôi không cười được, thật ấm ức.",
                "grammar_note": "Q#155: Vない (わからない) + せいで dẫn đến cảm giác ấm ức くやしかった.",
            },
            {
                "jp": "最近、忙しかったせいで、かなり疲れている。",
                "reading_note": "さいきん、いそがしかったせいで、かなりつかれている。",
                "vi": "Tại vì dạo gần đây bận rộn nên tôi khá mệt mỏi.",
                "grammar_note": "Aい quá khứ (忙しかった) + せいで.",
            },
        ],
        "source_ref": "Shin-N3-List #23 | Đề .xlsx (Q155)",
        "search_keywords": "sei de tai vi hau qua xau せいで せいだ せいか",
        "match_patterns": ["せいで", "せいだ", "せいです", "せいか"],
    },
    {
        "code": "GP-N3-021",
        "pattern": "～のだから / ～だから (Bởi vì sự thật là... nên đương nhiên)",
        "jlpt_level": "N3",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": False,
        "formation_formula": "V普通形 / Aい + のだから (んだから) | Aな + な / N + な + のだから",
        "formation_table": [
            {"pos": "Động từ / Tính từ い", "rule": "普通形 + のだから / んだから (せっかく入った会社なのだから)"},
            {"pos": "Tính từ な / Danh từ", "rule": "Aな + な + のだから; N + な + のだから (まだ子どもなのだから)"},
        ],
        "core_meaning_vi": "Dựa trên sự thật hiển nhiên mà cả hai người đều biết để khuyên nhủ, trách nhẹ hoặc đưa ra kết luận đương nhiên",
        "deep_explanation_vi": (
            "Việc thêm の vào trước だから biến câu nguyên nhân bình thường thành lời nhấn mạnh sự thật hiển nhiên đã biết ('vì vốn dĩ là... rồi nên đương nhiên phải...'). "
            "Vế sau thường đi kèm lời khuyên (べきだ, ほうがいい), câu nhận định đương nhiên (しかたがない, はずだ) hoặc trách móc nhẹ."
        ),
        "register_tag": "Hội thoại & Khuyên nhủ",
        "confusable_pairs": [
            {
                "rival_pattern": "N + な + のだから vs N + の + だから",
                "difference_vi": "Sau Danh từ và Tính từ な trước の bắt buộc đổi だ thành な (子どもなのだから), tuyệt đối không dùng *子どものだから hay *子どもだのだから.",
                "quick_test_vi": "Luôn dùng cấu trúc [N + な + のだから] khi nhấn mạnh tư cách/sự thật.",
            }
        ],
        "examples": [
            {
                "jp": "まだ子どもなのだから、わからなくても仕方がないでしょう。",
                "reading_note": "まだこどもなのだから、わからなくてもしかたがないでしょう。",
                "vi": "Vì cháu nó vẫn còn là trẻ con mà, nên không hiểu chuyện cũng đành vậy thôi.",
                "grammar_note": "Danh từ 子ども + な + のだから.",
            },
            {
                "jp": "せっかく入った会社なのだから、簡単に辞めるべきではない。",
                "reading_note": "せっかくはいったかいしゃなのだから、かんたんにやめるべきではない。",
                "vi": "Vì là công ty đã mất công mới vào được nên đừng nên nghỉ việc dễ dàng như vậy.",
                "grammar_note": "Kết hợp với べきではない ở vế sau để khuyên nhủ.",
            },
        ],
        "source_ref": "Shin-N3-List #24",
        "search_keywords": "no dakara vi su that hien nhien のだから なのだから",
        "match_patterns": ["のだから", "なのだから"],
    },
    {
        "code": "GP-N3-022",
        "pattern": "～ては / ～では (Nếu cứ thế này thì sẽ xấu / không được)",
        "jlpt_level": "N3",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": False,
        "formation_formula": "Vて + は / Vない + なくては | Aい(くて) + は | Aな/N + では + [Kết quả tiêu cực]",
        "formation_table": [
            {"pos": "Động từ (V)", "rule": "Vて + は / Vなくて + は (そんなに遊んでいては合格できない)"},
            {"pos": "Tính từ / Danh từ", "rule": "Aい -> Aくては; Aな/N -> では (時給500円では人が集まらない)"},
            {"pos": "Sắc thái vế sau", "rule": "Luôn kéo theo kết quả bất lợi, khó khăn, không thể thực hiện (困る, だめだ, できない)"},
        ],
        "core_meaning_vi": "Giả định một tình trạng đang tiếp diễn/tối thiểu mà nếu cứ giữ nguyên như vậy thì kết quả sau sẽ gặp rắc rối hoặc không thành",
        "deep_explanation_vi": (
            "Khác với điều kiện trung tính たら/ば, cặp [～ては / ～では] luôn đóng khung một điều kiện bất lợi hoặc chưa đạt yêu cầu, kéo theo hệ quả xấu ở vế sau. "
            "Khi tách rời cặp N4 ～てはいけない, bản chất phần đầu ては chính là 'nếu làm thế thì...'."
        ),
        "register_tag": "Trung tính (Khẩu ngữ & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vて + は vs Vて + も",
                "difference_vi": "Vては = Nếu làm V thì sẽ xảy ra kết quả xấu (tạo rắc rối); Vても = Cho dù làm V đi nữa thì kết quả vẫn không đổi (nhượng bộ).",
                "quick_test_vi": "Kiểm tra logic: 'Nếu lương 500 yên -> không tìm được người' (tạo hậu quả xấu) -> では; 'Dù lương thấp -> vẫn làm' (ngược kỳ vọng) -> でも.",
            }
        ],
        "examples": [
            {
                "jp": "この仕事、時給500円では人が見つかりません。",
                "reading_note": "このしごと、じきゅうごひゃくえんではひとがみつかりません。",
                "vi": "Công việc này mà lương giờ 500 yên thì không tìm nổi người đâu.",
                "grammar_note": "N + では dẫn đến kết quả bất khả thi 見つかりません.",
            },
            {
                "jp": "毎日そんなに夜更かしをしていては、体をこわしますよ。",
                "reading_note": "まいにちそんなによふかしをしていては、からだをこわしますよ。",
                "vi": "Ngày nào cũng thức khuya như vậy thì sẽ đổ bệnh đấy.",
                "grammar_note": "Vている chia ては cảnh báo hậu quả xấu.",
            },
        ],
        "source_ref": "Shin-N3-List #26",
        "search_keywords": "te wa de wa neu cu the nay thi xau ては では",
        "match_patterns": ["ていては", "円では"],
    },
    {
        "code": "GP-N3-023",
        "pattern": "～さえ / ～さえ～ば (Ngay cả... cũng / Chỉ cần... là đủ)",
        "jlpt_level": "N3",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": True,
        "formation_formula": "[1] N(+trợ từ) + さえ (Ngay cả đến... cũng) | [2] N + さえ + Vば / Aければ (Chỉ cần N thì đủ)",
        "formation_table": [
            {"pos": "1. Ngay cả / Đến cả (Cực đoan)", "rule": "N + さえ + Phủ định / Điều kiện (言葉さえできなくても, 名前さえ書けない). Thay thế cho が/を; đi sau に/で/へ"},
            {"pos": "2. Chỉ cần... là đủ (Điều kiện duy nhất)", "rule": "N + さえ + Vば / Aければ / Aななら (やる気さえあれば, お金さえあれば)"},
            {"pos": "Kết hợp động từ", "rule": "Vます + さえすれば / Vて + さえいれば"},
        ],
        "core_meaning_vi": "Nhấn mạnh yếu tố tối thiểu: (1) đến mức tối thiểu đó còn không có/không cần; hoặc (2) chỉ cần có duy nhất điều kiện đó là đủ",
        "deep_explanation_vi": (
            "～さえ có 2 mẫu thi cực kỳ phổ biến xuất hiện ở cả 問題1, 問題2 ★ và 問題3: "
            "1) Trong Q#58 (問題2 ★): 'この仕事は、やる気 [さえ] [あれば] 経験を問わず応募することができます' -> mẫu [N + さえ + あれば] nghĩa là 'chỉ cần có N là đủ'. "
            "2) Trong Q#154 (問題3): '日常生活だって言葉 [さえ] できなくても、なんとかなりますよ' -> 'ngay cả ngôn ngữ mà không biết đi nữa cũng xoay xở được'. "
            "3) Lưu ý Q#15: với số từ tối thiểu + khẳng định điều kiện ('一度でも会ったことがあれば'), khẩu ngữ tự nhiên dùng 一度でも chứ không dùng 一度さえ."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "N + さえ (ngay cả) vs N + しか (chỉ) vs Số từ + でも",
                "difference_vi": "さえ đưa ra ví dụ cực đoan ở đáy thang đo ('ngay cả cái cơ bản nhất cũng...'); しか giới hạn số lượng ('chỉ có chừng ấy thôi'); Số từ + でも = 'dù chỉ 1 lần'.",
                "quick_test_vi": "Thấy ば / あれば ngay sau -> chắc chắn là さえ; thấy Vなくても phía sau -> さえ!",
            }
        ],
        "examples": [
            {
                "jp": "この仕事は、やる気さえあれば経験を問わず応募することができます。",
                "reading_note": "このしごとは、やるきさえあればけいけんをとわずおうぼすることができます。",
                "vi": "Công việc này chỉ cần có tinh thần quyết tâm là có thể ứng tuyển bất kể kinh nghiệm.",
                "grammar_note": "Q#58: N + さえ + あれば = chỉ cần có N là đủ.",
            },
            {
                "jp": "日常生活だって言葉さえできなくても、なんとかなりますよ。",
                "reading_note": "にちじょうせいかつだってことばさえできなくても、なんとかなりますよ。",
                "vi": "Trong sinh hoạt hằng ngày, ngay cả tiếng không biết đi nữa thì rồi cũng xoay xở được thôi.",
                "grammar_note": "Q#154: N + さえ + phủ định nhượng bộ できなくても.",
            },
        ],
        "source_ref": "Shin-N3-List #27 | Đề .xlsx (Q15, Q58, Q154)",
        "search_keywords": "sae sae ba ngay ca chi can さえ さえあれば",
        "match_patterns": ["さえ", "さえあれば", "さえすれば"],
    },
    {
        "code": "GP-N3-024",
        "pattern": "たとえ～ても / ～でも (Cho dù... đi nữa thì vẫn...)",
        "jlpt_level": "N3",
        "category": "contrast_concession",
        "category_label_vi": CATEGORY_LABELS["contrast_concession"],
        "in_exam_corpus": True,
        "formation_formula": "たとえ + [Vて/Aくて/Aなで/Nで] + も (Hoặc たとえ + どんなに + Aい + N + でも)",
        "formation_table": [
            {"pos": "Đi với Động từ / Tính từ い", "rule": "たとえ + Vて + も / Aくても (たとえ反対されても, たとえ高くても)"},
            {"pos": "Đi với Danh từ / Tính từ な", "rule": "たとえ + N/Aな + でも (たとえどんなに難しい問題でも)"},
            {"pos": "Phó từ hô ứng bắt buộc", "rule": "たとえ luôn mở đầu mệnh đề để báo trước bên dưới PHẢI có ～ても / ～でも"},
        ],
        "core_meaning_vi": "Nhấn mạnh giả định cực đoan: cho dù tình huống có khó khăn đến đâu đi nữa thì kết luận vế sau vẫn không thay đổi",
        "deep_explanation_vi": (
            "Đây là cặp hô ứng trực tiếp xuất hiện trong 問題2 ★ Q#23 ('わたしは [たとえ] [どんなに] [難しい] [問題でも] 必ず答えはあると思う') và kết hợp với Q#9 ('どんなに頑張っても'). "
            "Lưu ý cấu trúc lắp ghép khi có phó từ nhấn mạnh どんなに: たとえ đứng đầu cụm -> どんなに -> Tính từ い -> Danh từ + でも (không chen vào sau danh từ)."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "たとえ～ても vs どんなに～ても",
                "difference_vi": "Cả hai đều kết thúc bằng ～ても/～でも, nhưng たとえ nhấn mạnh giả định cực đoan ('giả sử cho dù...'), còn どんなに nhấn mạnh mức độ cao ('dù đến mức nào đi nữa'). Hai phó từ này thường kết hợp cùng nhau: たとえ どんなに～ても.",
                "quick_test_vi": "Thấy 4 ô ghép sao có cả たとえ và どんなに (Q#23) -> xếp たとえ đứng ngay trước どんなに!",
            }
        ],
        "examples": [
            {
                "jp": "わたしはたとえどんなに難しい問題でも必ず答えはあると思う。",
                "reading_note": "わたしはたとえどんなにむずかしいもんだいでもかならずこたえはあるとおもう。",
                "vi": "Tôi nghĩ rằng cho dù là vấn đề khó đến đâu đi nữa thì nhất định cũng có lời giải.",
                "grammar_note": "Q#23: Chuỗi lắp ghép たとえ -> どんなに -> 難しい -> 問題でも.",
            },
            {
                "jp": "たとえどんなに反対されても、僕はプロの歌手になりたい。",
                "reading_note": "たとえどんなにはんたいされても、ぼくはぷろのかしゅになりたい。",
                "vi": "Cho dù bị phản đối thế nào đi nữa thì tôi vẫn muốn trở thành ca sĩ chuyên nghiệp.",
                "grammar_note": "たとえ～ても kết hợp bị động.",
            },
        ],
        "source_ref": "Shin-N3-List #28 | Đề .xlsx (Q9, Q23)",
        "search_keywords": "tatoe temo demo donnani cho du di nua たとえ どんなに ても でも",
        "match_patterns": ["たとえ", "どんなに"],
    },
    {
        "code": "GP-N3-025",
        "pattern": "～によれば / ～によると (Theo như nguồn tin... thì nghe nói)",
        "jlpt_level": "N3",
        "category": "discourse",
        "category_label_vi": CATEGORY_LABELS["discourse"],
        "in_exam_corpus": True,
        "formation_formula": "N(nguồn tin) + によれば / によると + [...そうだ / ...ということだ / ...らしい]",
        "formation_table": [
            {"pos": "Danh từ nguồn tin", "rule": "天気予報・ニュース・調査結果・先生の話 + によれば / によると"},
            {"pos": "Đuôi câu hô ứng bắt buộc", "rule": "Cuối câu PHẢI dùng dạng truyền đạt/nghe nói: ～そうだ, ～ということだ, ～らしい, ～と言われている"},
        ],
        "core_meaning_vi": "Trích dẫn nguồn thông tin (báo chí, dự báo thời tiết, lời kể) để truyền đạt lại nội dung nghe được",
        "deep_explanation_vi": (
            "Đây là bẫy kinh điển ở Q#54 ('場所の便利さ [からいうと] Aホテルのほうがおすすめです', có によれば làm nhiễu): "
            "1) によれば / によると BẮT BUỘC đi với NGUỒN TIN (báo, đài, kết quả khảo sát, lời người khác) và cuối câu có truyền đạt nghe nói (～そうだ/～ということだ). "
            "2) Trong Q#54, 'độ tiện lợi của vị trí' (場所の便利さ) là TIÊU CHÍ ĐÁNH GIÁ để đưa ra gợi ý chủ quan (おすすめ), KHÔNG phải nguồn tin nghe nói -> phải loại によれば và chọn からいうと!"
        ),
        "register_tag": "Trung tính & Tin tức",
        "confusable_pairs": [
            {
                "rival_pattern": "N + によれば / によると vs N + からいうと vs N + によって",
                "difference_vi": "によれば/によると = trích nguồn tin khách quan kèm đuôi nghe nói; からいうと = xét từ tiêu chí để nhận xét; によって = tùy theo tiêu chí/cách thức.",
                "quick_test_vi": "Cuối câu có おすすめだ/いい (nhận xét cá nhân)? Loại によれば ngay!",
            }
        ],
        "examples": [
            {
                "jp": "市のお知らせによれば、この道路は来週から工事が始まるということです。",
                "reading_note": "しのおしらせによれば、このどうろはらいしゅうからこうじがはじまるということです。",
                "vi": "Theo thông báo của thành phố thì nghe nói con đường này tuần sau sẽ khởi công.",
                "grammar_note": "Nguồn tin 市のお知らせ + によれば hô ứng với ということです.",
            },
            {
                "jp": "最近の調査によると、若者の読書時間が減っているそうだ。",
                "reading_note": "さいきんのちょうさによると、わかもののどくしょじかんがへっているそうだ。",
                "vi": "Theo điều tra gần đây thì thời gian đọc sách của giới trẻ đang giảm.",
                "grammar_note": "調査によると hô ứng với そうだ.",
            },
        ],
        "source_ref": "Shin-N3-List #29 | Đề .xlsx (Q54)",
        "search_keywords": "ni yoreba ni yoru to theo nhu nguon tin によれば によると",
        "match_patterns": ["によれば", "によると"],
    },
    {
        "code": "GP-N3-026",
        "pattern": "～と言われている (Được cho rằng, người ta nói rằng)",
        "jlpt_level": "N3",
        "category": "discourse",
        "category_label_vi": CATEGORY_LABELS["discourse"],
        "in_exam_corpus": True,
        "formation_formula": "普通形 + と言われている（といわれている）",
        "formation_table": [
            {"pos": "Động từ / Tính từ", "rule": "普通形 + と言われている (秋はいい季節だと言われている, 現代は情報の時代だと言われている)"},
            {"pos": "Nghĩa bị động tổng quát", "rule": "Không chỉ rõ ai nói, mà diễn đạt quan niệm phổ biến của xã hội hoặc giới khoa học"},
        ],
        "core_meaning_vi": "Trình bày một nhận định, truyền thuyết hoặc tri thức phổ biến được xã hội công nhận ('người ta vẫn nói rằng / được cho là')",
        "deep_explanation_vi": (
            "～と言われている (thể bị động tiếp diễn của 言う) xuất hiện cực kỳ nhiều trong đề thi N3: Q#18 ('いい季節だと言われている'), Q#37 ('現代は情報の時代だと言われている'), Passage 5 ('月にはウサギが住んでいると言われています'), Passage 9 ('共感覚を持っているとも言われている'). "
            "Khi đọc hiểu, chú ý phân biệt điều 'người ta nói vậy' (と言われている / そうだ) với 'chủ trương thực sự của tác giả'!"
        ),
        "register_tag": "Văn viết & Giải thích khách quan",
        "confusable_pairs": [
            {
                "rival_pattern": "～と言われている vs ～と言っている",
                "difference_vi": "と言われている = dư luận chung/người ta nói (chủ ngữ ẩn số đông); と言っている = một cá nhân/nhóm người cụ thể nói.",
                "quick_test_vi": "Thấy 'từ xưa ở Nhật... / trong nghiên cứu gần đây...' -> と言われている; thấy tên người cụ thể (田中さんは) -> と言っている.",
            }
        ],
        "examples": [
            {
                "jp": "日本では昔から、「月にはウサギが住んでいる」と言われています。",
                "reading_note": "にほんではむかしから、「つきにはうさぎがすんでいる」といわれています。",
                "vi": "Ở Nhật Bản từ xưa người ta vẫn nói rằng 'Trên mặt trăng có thỏ sinh sống'.",
                "grammar_note": "Passage 5: Truyền thuyết dân gian dùng と言われています.",
            },
            {
                "jp": "赤ちゃんのころは誰でも共感覚を持っているとも言われている。",
                "reading_note": "あかちゃんのころはだれでもきょうかんかくをもっているともいわれている。",
                "vi": "Người ta cũng nói rằng hồi sơ sinh bất kỳ ai cũng có cảm giác kèm.",
                "grammar_note": "Passage 9: Nhận định khoa học dùng とも言われている.",
            },
        ],
        "source_ref": "Shin-N3-List #30 | Đề .xlsx (Q18, Q37, Passages 5, 9)",
        "search_keywords": "to iwarete iru nguoi ta noi rang と言われている と言われています",
        "match_patterns": ["と言われている", "と言われています", "とも言われている"],
    },
    {
        "code": "GP-N3-027",
        "pattern": "～とか (Nghe đâu là / Liệt kê ví dụ như là...)",
        "jlpt_level": "N3",
        "category": "discourse",
        "category_label_vi": CATEGORY_LABELS["discourse"],
        "in_exam_corpus": True,
        "formation_formula": "[1] 普通形 + とか (Nghe đồn là) | [2] N1 + とか + N2 + とか (Chẳng hạn như A hay B)",
        "formation_table": [
            {"pos": "1. Truyền đạt tin đồn", "rule": "普通形 + とか（だ） / とか聞いた (Nghe phong phanh đâu là... - độ tin cậy không chắc chắn)"},
            {"pos": "2. Liệt kê ví dụ (khẩu ngữ)", "rule": "N / Vる + とか～とか (Khẩu ngữ tương đương ～たり～たり hoặc ～や～など)"},
        ],
        "core_meaning_vi": "Truyền đạt tin đồn chưa kiểm chứng ('nghe đâu thì phải') hoặc liệt kê vài ví dụ mang tính khẩu ngữ ('những thứ như là')",
        "deep_explanation_vi": (
            "Ở Q#149 ('冬には冷たい空気が部屋の中に入る [のを] 防ぎます'), とか xuất hiện làm đáp án nhiễu: không bao giờ dùng とか để danh từ hóa một mệnh đề làm tân ngữ trực tiếp trước 防ぐ! "
            "Ngược lại, khi thấy dấu hiệu tin đồn truyền miệng trong hội thoại (như nghe nói nhà hàng xóm sắp cưới), dùng 普通形 + とか."
        ),
        "register_tag": "Khẩu ngữ (Tin đồn / Liệt kê)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vる + とか vs Vる + のを",
                "difference_vi": "とか là trợ từ liệt kê ví dụ/tin đồn (không biến mệnh đề thành tân ngữ của tha động từ); のを là danh từ hóa mệnh đề làm tân ngữ bắt buộc của tha động từ (như 防ぐ).",
                "quick_test_vi": "Đứng ngay trước tha động từ 防ぐ/見る/止める -> dùng のを, loại とか.",
            }
        ],
        "examples": [
            {
                "jp": "隣の娘さんは来月結婚するとか聞きましたよ。",
                "reading_note": "となりのむすめさんはらいげつけっこんするとかききましたよ。",
                "vi": "Nghe đâu cô con gái nhà hàng xóm tháng sau kết hôn thì phải.",
                "grammar_note": "Tin đồn nghe loáng thoáng dùng Vる + とか.",
            },
            {
                "jp": "休みには映画を見るとか買い物に行くとかしている。",
                "reading_note": "やすみにはえいがをみるとかかいものにいくとかしている。",
                "vi": "Ngày nghỉ tôi làm những việc như xem phim hay đi mua sắm.",
                "grammar_note": "Liệt kê ví dụ khẩu ngữ dùng とか～とか.",
            },
        ],
        "source_ref": "Shin-N3-List #31 | Đề .xlsx (Q149)",
        "search_keywords": "toka nghe dau liet ke vi du とか",
        "match_patterns": ["とか"],
    },
    {
        "code": "GP-N3-028",
        "pattern": "～ということだ / ～という (Nghe nói rằng / Rằng nội dung là...)",
        "jlpt_level": "N3",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": True,
        "formation_formula": "普通形 + ということだ / とのことだ / そうだ | 普通形 + という + N (N có nội dung là...)",
        "formation_table": [
            {"pos": "1. Truyền đạt trang trọng", "rule": "普通形 + ということだ (Nghe nói rằng / Thông tin chính thức cho biết)"},
            {"pos": "2. Giải thích nghĩa", "rule": "AというのはBということだ (A có nghĩa là B)"},
            {"pos": "3. Bổ nghĩa Danh từ nội dung", "rule": "Mệnh đề + という + N (止まっているというメール, 実感という気持ち, 実感わかない -> Q#24, Q#136)"},
        ],
        "core_meaning_vi": "Trích dẫn nội dung thông tin trang trọng (～ということだ) hoặc nối nội dung cụ thể vào danh từ đứng sau (～という + N)",
        "deep_explanation_vi": (
            "Cấu trúc [Mệnh đề + という + Danh từ] là chìa khóa đọc hiểu và ghép câu ★ 問題2 (như Q#24: '乗っている電車が止まっている [という] メールが来た'; Q#26: 'いい [という] わけではなく'; Q#140: '失礼だったという手紙'). "
            "Nó giúp giải thích NỘI DUNG bên trong các danh từ truyền tin/nhận thức như メール, ニュース, 話, うわさ, わけ, ルール. "
            "Cẩn thận bẫy ở Q#21: khi định nghĩa từ vựng [Aというのは B ___ ], dùng のことだ (N2のことだ) chứ không dùng というのだ."
        ),
        "register_tag": "Trung tính & Văn viết trang trọng",
        "confusable_pairs": [
            {
                "rival_pattern": "～という + N vs ～ということだ vs ～のことだ",
                "difference_vi": "～という+N = N mang nội dung 'rằng...'; ～ということだ = nghe nói/có nghĩa là; [Aというのは Bのことだ] = định nghĩa từ ngữ (A là chỉ B).",
                "quick_test_vi": "Trước danh từ thông tin (メール・話・わけ) -> という; cuối câu định nghĩa [AというのはB...] -> のことだ.",
            }
        ],
        "examples": [
            {
                "jp": "友だちから乗っている電車が止まっているというメールが来た。",
                "reading_note": "ともだちからのっているでんしゃがとまっているというめーるがきた。",
                "vi": "Tôi nhận được email từ bạn báo rằng chuyến tàu bạn ấy đang đi bị dừng.",
                "grammar_note": "Q#24: メール có nội dung cụ thể là '電車が止まっている' nối qua という.",
            },
            {
                "jp": "この辺りは昔、広い草原だったということだ。",
                "reading_note": "このあたりはむかし、ひろいそうげんだったということだ。",
                "vi": "Nghe nói khu vực này ngày xưa từng là thảo nguyên rộng lớn.",
                "grammar_note": "Truyền đạt thông tin văn viết trang trọng.",
            },
        ],
        "source_ref": "Shin-N3-List #32, #33 | Đề .xlsx (Q21, Q24, Q26, Q140)",
        "search_keywords": "to iu to iu koto da noi dung rang nghe noi という ということだ",
        "match_patterns": ["ということだ", "というメール", "という話", "というルール", "という"],
    },
    {
        "code": "GP-N3-029",
        "pattern": "～わけだ (Thảo nào, hèn chi, suy ra kết quả tất yếu là)",
        "jlpt_level": "N3",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": True,
        "formation_formula": "普通形(V/Aい / Aな+な・である) / N+というわけだ・N+であるわけだ (khẩu ngữ: N+な+わけだ)",
        "formation_table": [
            {"pos": "Động từ / Tính từ い", "rule": "普通形 + わけだ (9時に着くわけだ, 高いわけだ)"},
            {"pos": "Tính từ な", "rule": "Aな + な / である + わけだ (日本語が上手なわけだ, 便利なわけだ)"},
            {"pos": "Danh từ (N)", "rule": "N + というわけだ / N + であるわけだ (khẩu ngữ: N + な + わけだ) (例: 専門家というわけだ, 日本人であるわけだ, khẩu ngữ: 日本人なわけだ)"},
        ],
        "core_meaning_vi": "Bày tỏ sự vỡ lẽ, kết luận hợp lý từ các dữ kiện đã biết ('thảo nào / hèn chi / tính ra là...')",
        "deep_explanation_vi": (
            "Đây là mẫu mở đầu cho gia đình chữ わけ cực kỳ hay thi ở N3 (わけだ vs わけではない vs わけがない vs わけにはいかない). "
            "わけだ ở khẳng định luôn có nghĩa 'hèn chi / tính ra là như vậy' (suy luận logic từ tiền đề). "
            "Do đó trong Q#63 ('世界中の人がみんなウサギにたとえている [わけではない]'), phương án わけです bị loại vì vế trước có từ nối đối lập けれども ('tuy nhiên') và câu sau chứng minh ở Nam Âu ví với cua!"
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "～わけだ vs ～わけではない vs ～はずだ",
                "difference_vi": "わけだ = thảo nào/hóa ra là (hiểu ra nguyên nhân/kết quả thực tế); わけではない = không hẳn là (phủ định một phần); はずだ = suy đoán chắc chắn về việc chưa kiểm chứng.",
                "quick_test_vi": "Thấy 'vậy thì tính ra là / thảo nào' -> わけだ; thấy câu trước dùng けれども / みんな -> わけではない.",
            }
        ],
        "examples": [
            {
                "jp": "ここから東京駅まで1時間半か。じゃ今から出れば9時に着くわけだ。",
                "reading_note": "ここからとうきょうえきまでいちじかんはんか。じゃいまからでればくじにつくわけだ。",
                "vi": "Từ đây tới ga Tokyo mất 1 tiếng rưỡi à. Vậy xuất phát bây giờ thì 9 giờ sẽ tới nơi.",
                "grammar_note": "Suy ra kết quả tính toán hiển nhiên bằng Vる + わけだ.",
            },
            {
                "jp": "彼のお母さんは日本人だ。だから日本語が上手なわけだ。",
                "reading_note": "かれのおかあさんはにほんじんだ。だからにほんごがじょうずなわけだ。",
                "vi": "Mẹ anh ấy là người Nhật. Thảo nào tiếng Nhật anh ấy giỏi thế.",
                "grammar_note": "Tính từ な (上手) + な + わけだ.",
            },
        ],
        "source_ref": "Shin-N3-List #34 | anki #6 | Đề .xlsx (Q63)",
        "search_keywords": "wake da thao nao hen chi suy ra わけだ わけです",
        "match_patterns": ["わけだ", "わけです"],
    },
    {
        "code": "GP-N3-030",
        "pattern": "～とは限らない (Không nhất thiết, chưa chắc lúc nào cũng...)",
        "jlpt_level": "N3",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": False,
        "formation_formula": "普通形(V/Aい / Aな・N bỏ だ hoặc giữ だ) + とは限らない（とはかぎらない）",
        "formation_table": [
            {"pos": "Động từ / Tính từ い", "rule": "普通形 + とは限らない (高いものがおいしいとは限らない)"},
            {"pos": "Danh từ / Tính từ な", "rule": "N / Aな (+ だ) + とは限らない (日本人とは限らない, いつも正しいとは限らない)"},
        ],
        "core_meaning_vi": "Phủ nhận tính tuyệt đối: 'không nhất thiết lúc nào cũng như vậy, vẫn có trường hợp ngoại lệ'",
        "deep_explanation_vi": (
            "Mẫu này gần nghĩa với ～わけではない nhưng thiên về phản bác các định kiến, quy luật phổ biến (thường đi với các từ toàn thể như いつも, すべて, みんな, 必ず). "
            "Ví dụ: không phải người dạy tiếng Nhật nào cũng nhất thiết là người Nhật; không phải đồ đắt tiền nào cũng chắc chắn ngon."
        ),
        "register_tag": "Trung tính & Văn viết nghị luận",
        "confusable_pairs": [
            {
                "rival_pattern": "～とは限らない vs ～わけではない",
                "difference_vi": "とは限らない nhấn mạnh 'vẫn có ngoại lệ, chưa chắc đúng 100%'; わけではない nhấn mạnh 'sự thật không có nghĩa là như vậy (phản bác hiểu nhầm)'.",
                "quick_test_vi": "Thấy phản bác định kiến chung ('đắt = ngon', 'giáo viên = người Nhật') -> とは限らない; thấy 'tuy A nhưng không hẳn B' -> わけではない.",
            }
        ],
        "examples": [
            {
                "jp": "日本語を教えているのは日本人とは限らない。",
                "reading_note": "にほんごをおしえているのはにほんじんとはかぎらない。",
                "vi": "Người dạy tiếng Nhật không nhất thiết phải là người Nhật.",
                "grammar_note": "Danh từ 日本人 + とは限らない nêu ngoại lệ.",
            },
            {
                "jp": "高い店がいつもおいしいとは限らない。",
                "reading_note": "たかいみせがいつもおいしいとはかぎらない。",
                "vi": "Quán đắt tiền chưa chắc lúc nào cũng ngon.",
                "grammar_note": "Hô ứng với いつも để phủ định tuyệt đối.",
            },
        ],
        "source_ref": "Shin-N3-List #36",
        "search_keywords": "to wa kagiranai khong nhat thiet chua chac とは限らない とはかぎらない",
        "match_patterns": ["とは限らない", "とは限りません", "とはかぎらない"],
    },
    {
        "code": "GP-N3-031",
        "pattern": "～わけではない / 決して～わけではない (Không hẳn là - Phủ định một phần)",
        "jlpt_level": "N3",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": True,
        "formation_formula": "(決して) + V普通形 / Aい / Aな+な・である / N+というわけではない / N+であるわけではない",
        "formation_table": [
            {"pos": "Động từ / Tính từ い", "rule": "普通形 + わけではない (たとえばているわけではない, 小さいわけではない)"},
            {"pos": "Tính từ な", "rule": "Aな + な / である + わけではない (嫌いなわけではない, 暇なわけではない)"},
            {"pos": "Danh từ (N)", "rule": "N + というわけではない / N + であるわけではない (学生というわけではない, 専門家であるわけではない — chú ý: N+の+わけではない chỉ mang nghĩa sở hữu 'của N', còn phủ định định danh dùng というわけ/である)"},
            {"pos": "Phó từ tăng cường", "rule": "決して ～ わけではない (Hoàn toàn không phải là...)"},
        ],
        "core_meaning_vi": "Phủ định một phần hoặc đính chính sự hiểu lầm: 'không phải tất cả đều vậy / điều đó không có nghĩa là...'",
        "deep_explanation_vi": (
            "Đây là mẫu N3 quan trọng bậc nhất trong đề thi, xuất hiện trực tiếp ở Q#26 ('何でもいいというわけではなく'), Q#59 ('決して小さいわけではない'), Q#63 ('みんなウサギにたとえているわけではありません') và Passage 9 ('すべてが同じというわけではない'). "
            "Quy tắc hình thái bắt buộc phân tách rõ từ loại: sau Aな phải có な/である (嫌いなわけではない, 暇なわけではない), sau N phải có というわけ hoặc である (学生というわけではない, 専門家であるわけではない — tránh nhầm N+の+わけではない chỉ dùng khi chỉ sở hữu như 自分のわけではない). "
            "Tuyệt đối không nhầm với ～わけがない (không thể nào có chuyện 100%) và ～わけにはいかない (không thể làm vì lý do đạo lý)."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "～わけではない vs ～わけがない vs ～わけにはいかない",
                "difference_vi": "わけではない = không hẳn là (thừa nhận phần đúng, phủ định sự tuyệt đối); わけがない = tuyệt đối không thể nào (phủ định 100%); わけにはいかない = dù muốn cũng không thể làm do quy tắc/đạo đức.",
                "quick_test_vi": "Thấy みんな / すべて / 決して / だからといって -> chọn ngay わけではない!",
            }
        ],
        "examples": [
            {
                "jp": "女性の平均からすると決して小さいわけではない。",
                "reading_note": "じょせいのへいきんからするとけっしてちいさいわけではない。",
                "vi": "Xét theo mức trung bình của phụ nữ thì hoàn toàn không phải là nhỏ bé.",
                "grammar_note": "Q#59: Cặp hô ứng 決して + Aい (小さい) + わけではない.",
            },
            {
                "jp": "世界中の人がみんなこの「海」を「ウサギ」にたとえているわけではありません。",
                "reading_note": "せかいじゅうのひとがみんなこの「うみ」を「うさぎ」にたとえているわけではありません。",
                "vi": "Không phải tất cả mọi người trên thế giới đều ví vùng 'biển' này với 'con thỏ'.",
                "grammar_note": "Q#63: みんな đi với phủ định một phần わけではありません.",
            },
        ],
        "source_ref": "Shin-N3-List #37 | anki #2 | Đề .xlsx (Q26, Q59, Q63, Passage 9)",
        "search_keywords": "wake de wa nai kesshite phu dinh mot phan わけではない わけではありません わけではなく",
        "match_patterns": ["わけではない", "わけではありません", "わけではなく", "わけじゃない"],
    },
    {
        "code": "GP-N3-032",
        "pattern": "～わけにはいかない / ～わけにもいかない (Không thể làm vì lý do đạo lý/xã hội)",
        "jlpt_level": "N3",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": True,
        "formation_formula": "Vる + わけにはいかない / わけにもいかない",
        "formation_table": [
            {"pos": "Động từ (V)", "rule": "Vる + わけにはいかない (休むわけにはいかない, 断るわけにはいかない)"},
            {"pos": "Dạng nhấn mạnh đồng tình", "rule": "Vる + わけにもいかない (Cũng không thể làm thế được)"},
            {"pos": "Bản chất cấm kỵ", "rule": "Về mặt thể chất/kỹ năng có thể làm, nhưng lương tâm, trách nhiệm hoặc quy tắc xã hội không cho phép"},
        ],
        "core_meaning_vi": "Không thể làm V được (dù có khả năng hoặc muốn làm) vì lý do đạo đức, lương tâm, trách nhiệm xã hội cản trở",
        "deep_explanation_vi": (
            "Xuất hiện làm phương án nhiễu trực tiếp ở Q#63 (わけにはいきません / わけにもいきません). "
            "Người học hay dịch chữ わけ và chữ いかない thành 'không thể' rồi chọn nhầm! "
            "Ghi nhớ quy tắc vàng: ～わけにはいかない CHỈ dùng khi chủ thể ĐỨNG TRƯỚC LỰA CHỌN ĐẠO ĐỨC/TRÁCH NHIỆM ('có cuộc họp quan trọng nên dù sốt cũng không thể nghỉ việc được'). Trong câu nói về sự thật khách quan ('người châu Âu ví trăng với con cua' ở Q#63), tuyệt đối không dùng わけにはいかない."
        ),
        "register_tag": "Trung tính (Trách nhiệm & Tâm lý)",
        "confusable_pairs": [
            {
                "rival_pattern": "～わけにはいかない vs ～ことができない vs ～わけではない",
                "difference_vi": "わけにはいかない = không thể do ràng buộc đạo lý/tình cảm/quy tắc; ことができない = không thể do thiếu năng lực/điều kiện khách quan; わけではない = không hẳn là.",
                "quick_test_vi": "Vế trước có lý do trách nhiệm (大事な会議, 約束) và V trước chỗ trống là Vる có ý chí -> chọn わけにはいかない.",
            }
        ],
        "examples": [
            {
                "jp": "今日は大事な会議があるので、熱があっても仕事を休むわけにはいかない。",
                "reading_note": "きょうはだいじなかいぎがあるので、ねつがあってもしごとをやすむわけにはいかない。",
                "vi": "Hôm nay có cuộc họp quan trọng nên dù có sốt tôi cũng không thể nghỉ làm được.",
                "grammar_note": "Vる (休む) + わけにはいかない thể hiện trách nhiệm công việc.",
            },
            {
                "jp": "先輩の頼みだから、断るわけにもいかない。",
                "reading_note": "せんぱいのたのみだから、ことわるわけにもいかない。",
                "vi": "Vì là lời nhờ vả của đàn anh nên tôi cũng không thể từ chối được.",
                "grammar_note": "Tình cảm/lễ nghĩa khiến không thể từ chối.",
            },
        ],
        "source_ref": "Shin-N3-List #38 | anki #4 | Đề .xlsx (Q63)",
        "search_keywords": "wake ni wa ikanai dao duc trach nhiem わけにはいかない わけにもいかない",
        "match_patterns": ["わけにはいか", "わけにもいか"],
    },
    {
        "code": "GP-N3-033",
        "pattern": "～ないわけにはいかない (Không thể không làm, buộc phải làm)",
        "jlpt_level": "N3",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": False,
        "formation_formula": "Vない + わけにはいかない (Phủ định kép -> Khẳng định bắt buộc)",
        "formation_table": [
            {"pos": "Động từ (V)", "rule": "Vない + わけにはいかない (行かないわけにはいかない, 買わないわけにはいかない)"},
            {"pos": "Nghĩa nâng cấp N2", "rule": "Tương đương N2 ～ざるを得ない (Vない bỏ ない + ざるを得ない)"},
        ],
        "core_meaning_vi": "Không thể không làm, đành phải làm (vì hoàn cảnh, nghĩa vụ hoặc lương tâm bắt buộc dù không muốn)",
        "deep_explanation_vi": (
            "Phủ định 2 lần [không làm + không thể] tạo thành khẳng định bắt buộc [buộc phải làm]. "
            "Khác với ～なければならない (nghĩa vụ quy tắc chung), ～ないわけにはいかない nhấn mạnh tâm trạng đắn đo của bản thân thấy tình thế hoặc tình nghĩa ép buộc không còn đường lui."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vない + わけにはいかない vs Vる + わけにはいかない",
                "difference_vi": "Vない+わけにはいかない = KHÔNG THỂ KHÔNG làm (= BUỘC PHẢI LÀM); Vる+わけにはいかない = KHÔNG THỂ LÀM (= PHẢI NHỊN/TRÁNH LÀM).",
                "quick_test_vi": "Kiểm tra đuôi động từ trước わけ: có ない -> phải làm; nguyên thể Vる -> không được làm.",
            }
        ],
        "examples": [
            {
                "jp": "社長の命令だから、残業しないわけにはいかない。",
                "reading_note": "しゃちょうのめいれいだから、ざんぎょうしないわけにはいかない。",
                "vi": "Vì là mệnh lệnh của giám đốc nên tôi không thể không tăng ca.",
                "grammar_note": "する -> しない + わけにはいかない.",
            },
            {
                "jp": "この町は交通が不便だから、車を買わないわけにはいかない。",
                "reading_note": "このまちはこうつうがふべんだから、くるまをかわないわけにはいかない。",
                "vi": "Thị trấn này giao thông bất tiện nên không thể không mua ô tô.",
                "grammar_note": "Hoàn cảnh bắt buộc phải mua.",
            },
        ],
        "source_ref": "Shin-N3-List #39 | anki #5",
        "search_keywords": "nai wake ni wa ikanai buoc phai lam ないわけにはいかない",
        "match_patterns": ["ないわけにはいか"],
    },
    {
        "code": "GP-N3-034",
        "pattern": "～ないことはない (Không phải là không thể / Cũng có thể nhưng...)",
        "jlpt_level": "N3",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": False,
        "formation_formula": "Vない / Aくない / Aなではない / Nではない + ことはない / こともない",
        "formation_table": [
            {"pos": "Động từ (V)", "rule": "Vない + ことはない / こともない (歩けないことはない, できないことはない)"},
            {"pos": "Tính từ / Danh từ", "rule": "Aくない + ことはない; Aな/N + ではない + ことはない (おいしくないことはない)"},
            {"pos": "Mạch câu thường gặp", "rule": "Thường nối với が / けど để nêu điều kiện khó khăn đi kèm"},
        ],
        "core_meaning_vi": "Khẳng định dè dặt: 'không phải là không thể làm, tuy nhiên cũng có hạn chế/khó khăn nhất định'",
        "deep_explanation_vi": (
            "Cũng là phủ định kép [không + không có] nhưng sắc thái hoàn toàn khác ～ないわけにはいかない: "
            "～ないことはない là cách nói giảm nhẹ, khiêm tốn hoặc lưỡng lự ('đi bộ thì cũng đi được đấy nhưng hơi xa'). "
            "Đừng nhầm với Vる + ことはない (không cần thiết phải làm)."
        ),
        "register_tag": "Trung tính (Hội thoại & Đánh giá dè dặt)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vない + ことはない vs Vる + ことはない",
                "difference_vi": "Vない+ことはない = không phải là không (tức là CÓ THỂ nhưng không hoàn hảo); Vる+ことはない = không cần thiết phải làm.",
                "quick_test_vi": "Thấy Vない trước ことはない và vế sau có が (nhưng hơi khó) -> phủ định kép dè dặt.",
            }
        ],
        "examples": [
            {
                "jp": "ここから駅まで歩けないことはないが、かなり時間がかかりますよ。",
                "reading_note": "ここからえきまであるけないことはないが、かなりじかんがかかりますよ。",
                "vi": "Từ đây ra ga không phải là không đi bộ được, nhưng khá tốn thời gian đấy.",
                "grammar_note": "Thể khả năng phủ định (歩けない) + ことはない + が.",
            },
            {
                "jp": "その料理は辛くないこともないが、十分食べられる。",
                "reading_note": "そのりょうりはからくないこともないが、じゅうぶんたべられる。",
                "vi": "Món ăn đó không phải là không cay, nhưng hoàn toàn ăn được.",
                "grammar_note": "Tính từ phủ định (辛くない) + こともない.",
            },
        ],
        "source_ref": "Shin-N3-List #40",
        "search_keywords": "nai koto wa nai khong phai la khong ないことはない ないこともない",
        "match_patterns": ["ないことはない", "ないこともない"],
    },
    {
        "code": "GP-N3-035",
        "pattern": "～ことは～が (Có làm thật đấy nhưng mà...)",
        "jlpt_level": "N3",
        "category": "contrast_concession",
        "category_label_vi": CATEGORY_LABELS["contrast_concession"],
        "in_exam_corpus": False,
        "formation_formula": "[Động từ/Tính từ] + ことは + [Lặp lại đúng từ đó] + が / けど",
        "formation_table": [
            {"pos": "Động từ (V)", "rule": "Vる/Vた + ことは + Vる/Vた + が (読んだことは読んだが, 使えることは使えるが)"},
            {"pos": "Tính từ い / な", "rule": "Aい + ことは + Aい + が (安いことは安いが); Aな + な/である + ことは + Aな + だ + が"},
        ],
        "core_meaning_vi": "Thừa nhận sự thật ở vế trước ('có... thì có thật đấy') nhưng mở đường cho một nhận xét hạn chế/chưa hài lòng ở vế sau",
        "deep_explanation_vi": (
            "Khi muốn thừa nhận một sự thật nhưng ngay lập tức bổ sung điểm chưa ổn ('đọc thì có đọc nhưng chẳng hiểu gì', 'rẻ thì có rẻ nhưng nhanh hỏng'), người Nhật lặp lại chính vị từ đó qua cầu nối ことは...が. "
            "Lưu ý bắt buộc phải lặp lại CÙNG MỘT ĐỘNG TỪ/TÍNH TỪ ở cả hai phía của ことは."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "VことはVが vs VばVほど",
                "difference_vi": "Cả hai đều lặp 1 từ 2 lần, nhưng ことは...が mang nghĩa thừa nhận đối lập ('có làm thật đấy nhưng mà...'), còn ば...ほど là tỷ lệ thuận ('càng... càng...').",
                "quick_test_vi": "Thấy ことは nằm giữa 2 từ giống nhau và có が ở cuối vế -> thừa nhận nhượng bộ.",
            }
        ],
        "examples": [
            {
                "jp": "その本を読んだことは読んだが、内容が難しくて全然わからなかった。",
                "reading_note": "そのほんをよんだことはよんだが、ないようがむずかしくてぜんぜんわからなかった。",
                "vi": "Cuốn sách đó thì tôi có đọc thật đấy, nhưng nội dung khó nên chẳng hiểu gì cả.",
                "grammar_note": "読んだことは読んだが thừa nhận đã đọc rồi phủ nhận kết quả hiểu.",
            },
            {
                "jp": "このパソコンは安いことは安いが、すぐ故障しそうだ。",
                "reading_note": "このぱそこんはやすいことはやすいが、すぐこしょうしそうだ。",
                "vi": "Chiếc máy tính này rẻ thì có rẻ đấy nhưng có vẻ sắp hỏng tới nơi.",
                "grammar_note": "Tính từ い lặp lại qua ことは...が.",
            },
        ],
        "source_ref": "Shin-N3-List #41",
        "search_keywords": "koto wa ga co that day nhung ma ことは が",
        "match_patterns": ["ことは読んだが", "ことはあるが", "ことはいいが"],
    },
    {
        "code": "GP-N3-036",
        "pattern": "V(sai khiến)て + ほしい / いただきたい (Xin phép cho tôi được làm)",
        "jlpt_level": "N3",
        "category": "passive_causative",
        "category_label_vi": CATEGORY_LABELS["passive_causative"],
        "in_exam_corpus": True,
        "formation_formula": "V(sai khiến)て + ほしい / ください / いただきたい",
        "formation_table": [
            {"pos": "Thân mật / Trung tính", "rule": "V(sai khiến)て + ほしい (わたしにも読ませてほしい, 私に行かせてほしい)"},
            {"pos": "Lịch sự / Kính ngữ công sở", "rule": "V(sai khiến)て + ください / いただきたい (この件は私にやらせていただきたい)"},
            {"pos": "Chuyển đổi chủ thể", "rule": "Vてほしい = muốn BẠN làm; Vさせてほしい = muốn bạn CHO PHÉP TÔI làm"},
        ],
        "core_meaning_vi": "Thể hiện mong muốn đối phương cho phép chính bản thân mình thực hiện một hành động",
        "deep_explanation_vi": (
            "Đây là điểm ngữ pháp kiểm tra trực tiếp ở Q#17 ('B: じゃ、わたしにも [読ませて] ほしいです。お借りしてもいいですか'). "
            "Học viên N4 rất dễ chọn nhầm 読んでほしい ('muốn bạn đọc cho tôi nghe'). Vì ngay phía sau B nói 'Tôi mượn sách đọc có được không?' nên người đọc là chính B ('わたしにも') -> BẮT BUỘC phải chia động từ 読む sang thể sai khiến 読ませる rồi chia thể て thành 読ませて!"
        ),
        "register_tag": "Hội thoại & Công sở (いただく)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vさせてほしい vs Vてほしい vs Vられてほしい",
                "difference_vi": "Vさせてほしい = cho phép TÔI làm; Vてほしい = muốn BẠN làm cho tôi; Vられてほしい (sai/không tự nhiên cho phép xin làm).",
                "quick_test_vi": "Thấy '私に(も)' đứng trước và hành động do chính mình thực hiện -> luôn dùng thể sai khiến Vさせて + ほしい/いただきたい.",
            }
        ],
        "examples": [
            {
                "jp": "じゃ、わたしにも読ませてほしいです。お借りしてもいいですか。",
                "reading_note": "じゃ、わたしにもよませてほしいです。おかりしてもいいですか。",
                "vi": "Vậy thì tôi cũng muốn được phép đọc với. Tôi mượn có được không?",
                "grammar_note": "Q#17: 読む -> 読ませる -> 読ませて + ほしい.",
            },
            {
                "jp": "この仕事はぜひ私に担当させていただきたいです。",
                "reading_note": "このしごとはぜひわたしにたんとうさせていただきたいです。",
                "vi": "Công việc này xin nhất định hãy cho phép tôi được đảm nhận ạ.",
                "grammar_note": "Dạng kính ngữ công sở dùng させていただきたい.",
            },
        ],
        "source_ref": "Shin-N3-List #43 | Đề .xlsx (Q17)",
        "search_keywords": "sasete hoshii sasete itadakitai cho phep toi duoc lam させてほしい させていただきたい 読ませて",
        "match_patterns": ["ませてほしい", "させてほしい", "させていただき", "せてください"],
    },
    {
        "code": "GP-N3-037",
        "pattern": "～たらいいのに / ～ばいい / ～たらどうですか (Ước gì; Nên/Thử làm xem sao)",
        "jlpt_level": "N3",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": False,
        "formation_formula": "Vたら / Aかったら / Aなだったら / Nだったら + いいのに (Ước gì) | Vたら + どうですか (Thử làm xem)",
        "formation_table": [
            {"pos": "～たらいいのに (Ước ao/Tiếc nuối)", "rule": "Ước cho điều trái với thực tế hoặc mong ước tương lai (もっと安かったらいいのに, 男の子だったらいいのだが)"},
            {"pos": "～たらいい / ～ばいい", "rule": "Khuyên nhẹ 'nên làm thế là ổn/tốt' (困ったら先生に聞いたらいいと思う)"},
            {"pos": "～たらどうですか", "rule": "Gợi ý lịch sự 'thử làm V xem sao ạ?' (一度病院へ行ったらどうでしょうか)"},
        ],
        "core_meaning_vi": "Bày tỏ điều ước tiếc nuối (～たらいいのに), khuyên nhẹ nhàng (～たらいい) hoặc đề xuất giải pháp (～たらどうですか)",
        "deep_explanation_vi": (
            "Đuôi のに khi đi sau ～たらいい biến câu khuyên bình thường thành lời ước ao pha chút tiếc nuối vì thực tế chưa được như vậy. "
            "Còn ～たらどうですか / ～たらどうでしょうか là câu gợi ý cực kỳ lịch sự dành cho người đối diện thử làm một phương án mới."
        ),
        "register_tag": "Hội thoại (Mong ước & Gợi ý)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vたらいいのに vs Vたらどうですか",
                "difference_vi": "たらいいのに diễn tả mong ước chủ quan cho tình huống hiện chưa có thật; たらどうですか là câu hỏi gợi ý lịch sự cho người nghe thử làm.",
                "quick_test_vi": "Cuối câu có dấu hỏi / でしょうか -> たらどうですか; mang tâm trạng tiếc 'ước gì...' -> たらいいのに.",
            }
        ],
        "examples": [
            {
                "jp": "体のことが心配なら、一度検査を受けたらどうでしょうか。",
                "reading_note": "からだのことがしんぱいなら、いちどけんさをうけたらどうでしょうか。",
                "vi": "Nếu lo lắng cho sức khỏe thì anh thử đi kiểm tra một lần xem sao.",
                "grammar_note": "Vた + ら + どうでしょうか để gợi ý khéo léo.",
            },
            {
                "jp": "家の近くに大きなスーパーがあったらいいのに。",
                "reading_note": "いえのちかくにおおきなすーぱーがあったらいいのに。",
                "vi": "Ước gì gần nhà có một siêu thị lớn nhỉ.",
                "grammar_note": "ある -> あったら + いいのに bày tỏ mong ước.",
            },
        ],
        "source_ref": "Shin-N3-List #44, #48",
        "search_keywords": "tara ii noni tara dou desu ka uoc gi thu xem sao たらいいのに たらどうですか",
        "match_patterns": ["たらいいのに", "たらどう", "たらいいと思"],
    },
    {
        "code": "GP-N3-038",
        "pattern": "～ように言う・伝える・注意する & 命令・禁止 (な)",
        "jlpt_level": "N3",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": True,
        "formation_formula": "Vる / Vない + ように + 言う / 伝える / 注意する / 頼む (Khác: Vる + な = Cấm làm!)",
        "formation_table": [
            {"pos": "Truyền đạt yêu cầu gián tiếp", "rule": "Vる / Vない + ように + 言われる / 伝えてください / 注意する (行動するようにと言われてきた, 連絡するように伝えてください)"},
            {"pos": "Mệnh lệnh trực tiếp (Cứng/Khẩu ngữ nam)", "rule": "V1(cột う->え: 行け, 走れ), V2(bỏ る+ろ: 食べろ, 見ろ), V3(しろ, こい)"},
            {"pos": "Cấm đoán trực tiếp (な)", "rule": "Vる + な (Đứng cuối câu sau V nguyên thể: お酒を飲むな = Cấm uống rượu!)"},
        ],
        "core_meaning_vi": "Tường thuật gián tiếp lời khuyên/mệnh lệnh/dặn dò ('bảo/nhắc hãy làm hoặc đừng làm gì') và dạng mệnh lệnh/cấm trực tiếp",
        "deep_explanation_vi": (
            "Cấu trúc [Vる / Vない + ように + động từ truyền đạt (言う・伝える・注意する)] xuất hiện liên tục trong đề thi: "
            "Q#22 ('周りのことを考えて行動するようにと言われてきた'), Passage 10 ('必ず出席するように伝えてください / わたしに連絡するように伝えてください'), Passage 22 ('診察に遅れないように来てください'). "
            "Lưu ý quan trọng: trong lời truyền đạt gián tiếp, KHÔNG giữ nguyên てください mà phải đổi về thể từ điển Vる hoặc thể phủ định Vない rồi mới gắn ように!"
        ),
        "register_tag": "Trung tính & Truyền đạt gián tiếp",
        "confusable_pairs": [
            {
                "rival_pattern": "Vる + ように言う vs Vて + くれと言う vs Vる + な",
                "difference_vi": "ように言う là cách tường thuật trung tính gián tiếp; くれと言う giữ sắc thái nhờ vả trực tiếp; Vる+な là câu mệnh lệnh cấm đoán thô trực tiếp.",
                "quick_test_vi": "Thấy 言われる / 伝えてください / 注意する ở cuối -> bắt buộc trước đó là Vる/Vない + ように.",
            }
        ],
        "examples": [
            {
                "jp": "子どものころから、周りのことを考えて行動するようにと言われてきた。",
                "reading_note": "こどものころから、まわりのことをかんがえてこうどうするようにといわれてきた。",
                "vi": "Từ hồi nhỏ tôi đã được dặn dò là phải suy nghĩ cho xung quanh rồi mới hành động.",
                "grammar_note": "Q#22: 行動する + ように + と言われてきた.",
            },
            {
                "jp": "出席できない場合は、19日までにわたしに連絡するように伝えてください。",
                "reading_note": "しゅっせきできないばあいは、じゅうくにちまでにわたしにれんらくするようにつたえてください。",
                "vi": "Trường hợp không thể dự họp, hãy nhắn họ liên hệ cho tôi trước ngày 19.",
                "grammar_note": "Passage 10: Vる (連絡する) + ように伝えてください.",
            },
        ],
        "source_ref": "Shin-N3-List #45, #64 | Đề .xlsx (Q22, Passages 10, 22)",
        "search_keywords": "you ni iu tsutaeru chuui suru truyen dat menh lenh cam doan ように言われる ように伝えて 飲むな",
        "match_patterns": ["ように言わ", "ように伝え", "ように注意", "ように来て"],
    },
    {
        "code": "GP-N3-039",
        "pattern": "～こと（文末・指示・心得） (Phải / Không được - Văn bản quy tắc)",
        "jlpt_level": "N3",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": True,
        "formation_formula": "Vる / Vない + こと。(Đặt ở cuối câu để nêu quy định hoặc tâm niệm)",
        "formation_table": [
            {"pos": "Chỉ thị / Nội quy văn bản", "rule": "Vる / Vない + こと (休むときは必ず連絡すること, 部屋では静かにすること)"},
            {"pos": "Tâm niệm / Lời tự nhủ (Passage 19)", "rule": "心配しすぎないこと。楽しい目標を作ること。"},
        ],
        "core_meaning_vi": "Kết thúc câu bằng danh từ hóa ～こと để nêu quy định bắt buộc ngắn gọn trên văn bản hoặc liệt kê điều cần tâm niệm",
        "deep_explanation_vi": (
            "Khác với câu hội thoại dùng ～てください / ～ないでください, trong bảng nội quy, đề thi, hướng dẫn chính thức hoặc đoạn tổng kết bài học (như Passage 19: '心配しすぎないこと。楽しい目標を作ること。'), tác giả dùng động từ nguyên thể hoặc phủ định kết hợp trực tiếp với こと ở cuối câu. "
            "Trong Passage 19, đây là 2 câu liệt kê nguyên tắc tư duy tích cực mà vận động viên cần ghi nhớ."
        ),
        "register_tag": "Văn viết / Quy định & Tâm niệm",
        "confusable_pairs": [
            {
                "rival_pattern": "Vる/Vない + こと (Cuối câu quy định) vs Vることだ (Lời khuyên)",
                "difference_vi": "Vる/Vない+こと (không có だ) dùng trong nội quy hành chính hoặc gạch đầu dòng tâm niệm; thêm だ (～ことだ) dùng để khuyên bảo người nghe trong văn viết/nói.",
                "quick_test_vi": "Thấy 2 câu kết thúc song song bằng Vないこと。Vること。 -> dạng liệt kê điều cần ghi nhớ.",
            }
        ],
        "examples": [
            {
                "jp": "「なんとかなる」と考えて心配しすぎないこと。楽しい目標を作ること。",
                "reading_note": "「なんとかなる」とかんがえてしんぱいしすぎないこと。たのしいもくひょうをつくること。",
                "vi": "Hãy nghĩ 'rồi sẽ ổn thôi' và đừng lo lắng quá mức. Hãy tạo ra những mục tiêu vui vẻ.",
                "grammar_note": "Passage 19: Dùng Vないこと / Vること để liệt kê 2 điều tâm niệm.",
            },
            {
                "jp": "欠席するときは、必ず事前に学校に連絡すること。",
                "reading_note": "けっせきするときは、かならずじぜんにがっこうにれんらくすること。",
                "vi": "Khi vắng mặt nhất định phải liên hệ trước với nhà trường.",
                "grammar_note": "Nội quy văn bản dùng Vる + こと.",
            },
        ],
        "source_ref": "Shin-N3-List #46 | Đề .xlsx (Passage 19)",
        "search_keywords": "koto quy dinh chi thi tam niem しないこと すること",
        "match_patterns": ["すぎないこと。", "作ること。", "連絡すること。"],
    },
    {
        "code": "GP-N3-040",
        "pattern": "～べきだ / ～べきではない (Nên / Không nên - Nghĩa vụ đạo lý)",
        "jlpt_level": "N3",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": True,
        "formation_formula": "Vる + べきだ / べきではない (Ngoại lệ bất quy tắc: する -> すべきだ / するべきだ)",
        "formation_table": [
            {"pos": "Động từ Nhóm 1 & 2", "rule": "Vる + べきだ / べきではない (守るべきだ, 徹底すべきだと思う, 辞めるべきではない)"},
            {"pos": "Động từ Nhóm 3 する", "rule": "する có thể rút gọn thành すべき (hoặc giữ するべき); trong văn viết hay dùng すべき"},
            {"pos": "Bổ nghĩa danh từ", "rule": "Vる + べき + N (やるべき仕事 = công việc cần phải làm)"},
        ],
        "core_meaning_vi": "Nhấn mạnh nghĩa vụ, bổn phận hiển nhiên phải làm (hoặc không nên làm) xét theo đạo đức, lẽ phải hay trách nhiệm chung",
        "deep_explanation_vi": (
            "Khác với Vたほうがいい (khuyên nhủ giữa hai phương án cụ thể cho cá nhân), ～べきだ mang sắc thái đạo lý, chuẩn mực xã hội hoặc chủ trương nghị luận mạnh mẽ (như Passage 4: 'マグロを守るには、まずこのルールを徹底すべきだと思う'). "
            "Lưu ý hình thái đặc biệt của する: すべき (đây là trường hợp duy nhất ở N3 bỏ る của する trước べき). Không dùng べきだ cho lời mời ăn uống hay yêu cầu cá nhân nhỏ nhặt."
        ),
        "register_tag": "Văn viết nghị luận & Chuẩn mực",
        "confusable_pairs": [
            {
                "rival_pattern": "～べきだ vs ～たほうがいい",
                "difference_vi": "べきだ chỉ bổn phận, lẽ phải chung trong xã hội/luận điểm nghị luận; たほうがいい chỉ lời khuyên tình huống cụ thể (nên đi tàu điện thay vì xe buýt).",
                "quick_test_vi": "Chủ đề mang tính trách nhiệm chung (giữ lời hứa, bảo vệ môi trường, tuân thủ luật quốc tế) -> べきだ.",
            }
        ],
        "examples": [
            {
                "jp": "マグロを守るには、まずこのルールを徹底すべきだと思う。",
                "reading_note": "まぐろをまもるには、まずこのるーるをてっていすべきだとおもう。",
                "vi": "Để bảo vệ cá ngừ, tôi nghĩ trước tiên cần thực hiện triệt để quy tắc này.",
                "grammar_note": "Passage 4: 徹底する -> 徹底すべき.",
            },
            {
                "jp": "せっかく入った会社なのだから、簡単に辞めるべきではない。",
                "reading_note": "せっかくはいったかいしゃなのだから、かんたんにやめるべきではない。",
                "vi": "Vì đã mất công vào được công ty rồi nên không nên từ bỏ dễ dàng như vậy.",
                "grammar_note": "Phủ định Vる + べきではない.",
            },
        ],
        "source_ref": "Shin-N3-List #47 | anki #36 | Đề .xlsx (Passage 4)",
        "search_keywords": "beki da beki de wa nai nen bo phan dao ly べきだ すべき べきではない",
        "match_patterns": ["べきだ", "すべき", "べきではない"],
    },
])

# =========================================================================
# JLPT N3 CORE PART 2 (GP-N3-041 .. GP-N3-080)
# =========================================================================
GRAMMAR_POINTS_DATA.extend([
    {
        "code": "GP-N3-041",
        "pattern": "～つもりだ（Vたつもり / Vるつもり / Vないつもり）",
        "jlpt_level": "N3",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": True,
        "formation_formula": "Vた + つもりだ (Cứ đinh ninh là đã) | Vる / Vない + つもりだ (Dự định) | N+の / Aな+な / Aい + つもりだ (Coi như / Tự thấy mình là)",
        "formation_table": [
            {"pos": "1. N3: Vた + つもりだ", "rule": "Cứ tưởng/đinh ninh là đã làm rồi, nhưng thực tế lại sai/chưa xong (書いたつもりだった)"},
            {"pos": "2. N4: Vる / Vない + つもりだ", "rule": "Dự định, kế hoạch của bản thân (乗るつもりだ, 行かないつもりだ)"},
            {"pos": "3. N3: Aい / Aな+な / N+の + つもりだ", "rule": "Tự nhận/cảm thấy mình như vậy dù thực tế không hẳn (まだまだ若いつもりです)"},
        ],
        "core_meaning_vi": "Cứ đinh ninh/tự cho rằng mình đã làm hoặc đang ở trạng thái đó dù thực tế trái ngược (Vたつもりだ); hoặc dự định làm (Vるつもりだ)",
        "deep_explanation_vi": (
            "Đây là bẫy trọng tâm của Q#19 ('きのうの試験で自分では正しい答えを [書いたつもりだった] が、わたしの答えは間違いだった'). "
            "Học viên chỉ nhớ nghĩa N4 (Vるつもり = dự định) sẽ bị bối rối khi thấy Vた + つもりだ! "
            "Khi gắn vào thì quá khứ Vた hoặc tính từ/danh từ, つもりだ mang nghĩa chủ quan sai lầm ('cứ tưởng mình đã viết đúng / tuy 77 tuổi nhưng vẫn tự thấy mình còn trẻ') và thường đi kèm 'が、実は…'."
        ),
        "register_tag": "Trung tính",
        "confusable_pairs": [
            {
                "rival_pattern": "Vた + つもりだった vs Vる + つもりになった vs Vる + ことになった",
                "difference_vi": "Vたつもりだった = cứ đinh ninh đã làm vậy rồi (trái thực tế); Vるつもりになった = mới nảy sinh ý định sẽ làm; Vることになった = được quyết định khách quan là sẽ làm.",
                "quick_test_vi": "Thấy '自分では…が、実際は間違いだった' (Q#19) -> chốt ngay Vた + つもりだった.",
            }
        ],
        "examples": [
            {
                "jp": "きのうの試験で自分では正しい答えを書いたつもりだったが、わたしの答えは間違いだった。",
                "reading_note": "きのうのしけんでじぶんではただしいこたえをかいたつもりだったが、わたしのこたえはまちがいだった。",
                "vi": "Trong bài thi hôm qua, bản thân tôi cứ đinh ninh là đã viết đáp án đúng, nhưng hóa ra câu trả lời của tôi lại sai.",
                "grammar_note": "Q#19: Vた (書いた) + つもりだった diễn tả sự ngộ nhận chủ quan.",
            },
            {
                "jp": "私は今年77歳ですが、まだまだ若いつもりです。",
                "reading_note": "わたしはことしななじゅうななさいですが、まだまだわかいつもりです。",
                "vi": "Năm nay tôi 77 tuổi rồi nhưng tự mình vẫn cứ thấy còn trẻ lắm.",
                "grammar_note": "Tính từ い + つもりです.",
            },
        ],
        "source_ref": "Shin-N3-List #52 | Đề .xlsx (Q19, Q106)",
        "search_keywords": "tsumori da dinh ninh cu tuong du dinh つもりだ つもりだった",
        "match_patterns": ["つもりだ", "つもりだった", "つもりです"],
    },
    {
        "code": "GP-N3-042",
        "pattern": "～こそ (Chính là... mới là)",
        "jlpt_level": "N3",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": True,
        "formation_formula": "N / [Vて/Aから] + こそ (+ が / は) (Thay thế cho が / を, đi sau に / で / から)",
        "formation_table": [
            {"pos": "Danh từ + こそ", "rule": "Chính cái N này mới thực sự là... (この写真集こそ, 前向きな考え方こそが)"},
            {"pos": "Mệnh đề nguyên nhân + からこそ", "rule": "Chính bởi vì... nên mới... (親だからこそ厳しく叱るのだ)"},
            {"pos": "Cụm giao tiếp cố định", "rule": "こちらこそ (Chính tôi mới phải cảm ơn/xin lỗi), 今度こそ (Chính lần này nhất định...)"},
        ],
        "core_meaning_vi": "Nhấn mạnh tuyệt đối danh từ hoặc lý do đứng trước ('chính cái này chứ không phải thứ nào khác')",
        "deep_explanation_vi": (
            "～こそ xuất hiện cả trong 問題1 (Q#52: 'この写真集 [こそ]、ぼくがずっと探していたものだ'), 問題3 (Q#157: '前向きな考え方 [こそ] が...必要なのだろう'), và làm phương án nhiễu ở Q#15. "
            "Quy tắc vàng: 1) こそ có thể kết hợp với が (～こそが) để nhấn mạnh chủ ngữ ở câu kết luận nghị luận (Q#157). "
            "2) Khi có phó từ 'ずっと探していた' (tìm kiếm bấy lâu nay) thì nhấn mạnh đối tượng tìm thấy bằng こそ (Q#52). "
            "3) Không dùng こそ sau số lượng tối thiểu trước điều kiện (như 一度でも会えば ở Q#15)."
        ),
        "register_tag": "Trung tính (Nhấn mạnh khẳng định)",
        "confusable_pairs": [
            {
                "rival_pattern": "～こそ vs ～さえ vs ～だけ vs ～しか",
                "difference_vi": "こそ khẳng định nổi bật 'chính là N'; さえ đưa ví dụ tối thiểu 'ngay cả N'; だけ giới hạn 'chỉ N'; しか đi với phủ định 'chỉ... thôi'.",
                "quick_test_vi": "Câu khẳng định đề cao giá trị hoặc tìm thấy thứ mong mỏi (ずっと探していた / 必要なのだろう) -> こそ.",
            }
        ],
        "examples": [
            {
                "jp": "この写真集こそ、ぼくがずっと探していたものだ。",
                "reading_note": "このしゃしんしゅうこそ、ぼくがずっとさがしていたものだ。",
                "vi": "Chính cuốn sách ảnh này là thứ mà tôi đã tìm kiếm bấy lâu nay.",
                "grammar_note": "Q#52: N + こそ nhấn mạnh đích danh đối tượng tìm kiếm.",
            },
            {
                "jp": "このような心の余裕や前向きな考え方こそが、スポーツ選手にとって必要なのだろう。",
                "reading_note": "このようなこころのよゆうやまえむきなかんがえかたこそが、すぽーつせんしゅにとってひつようなのだろう。",
                "vi": "Chính sự thoải mái trong tâm hồn và cách nghĩ tích cực này mới là điều cần thiết cho VĐV.",
                "grammar_note": "Q#157: Cụm danh từ + こそ + が nhấn mạnh luận điểm kết bài.",
            },
        ],
        "source_ref": "Shin-N3-List #50(p8) | Đề .xlsx (Q15, Q52, Q157)",
        "search_keywords": "koso chinh la nhan manh こそ こそが だからこそ",
        "match_patterns": ["こそ", "こそが", "だからこそ"],
    },
    {
        "code": "GP-N3-043",
        "pattern": "Số từ + でも / N + でも (Dù chỉ... thôi cũng; Ngay cả; Những thứ như là)",
        "jlpt_level": "N3",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": True,
        "formation_formula": "[Số lượng nhỏ] + でも + [Điều kiện ば/たら/ても] | N + でも (Ngay cả / Đề xuất nhẹ)",
        "formation_table": [
            {"pos": "1. Số lượng nhỏ + でも (Q#15)", "rule": "Dù chỉ một chút/một lần thôi cũng... (一度でも会ったことがあれば, 5分でもいい)"},
            {"pos": "2. N + でも (Ngay cả cực đoan)", "rule": "Ngay cả đối tượng hiển nhiên nhất cũng... (子どもでも知っている, 休みの日でも受付できる)"},
            {"pos": "3. N + でも (Đề xuất ví dụ)", "rule": "Những thứ như là... (お茶でも飲みましょうか, 漫画でもかまいません)"},
        ],
        "core_meaning_vi": "Đặt sau số lượng nhỏ để nói 'dù chỉ 1 ít thôi cũng', đặt sau danh từ để nói 'ngay cả N' hoặc gợi ý nhẹ 'cỡ như N'",
        "deep_explanation_vi": (
            "Thi trực tiếp ở Q#15 ('一度 [でも] 会ったことがあれば、友だちだと考える人もいる') và xuất hiện trong Passage 7 ('雑誌や漫画でもかまいません') & Passage 22 ('病院が休みの日でも、電話で受付できます'). "
            "Phân biệt cực kỳ quan trọng giữa số từ + も và số từ + でも: "
            "[一度も] + PHỦ ĐỊNH = chưa từng một lần nào (như Passage 16: いちどもお寺にいっていない); còn [一度でも] + ĐIỀU KIỆN KHẲNG ĐỊNH = dù chỉ 1 lần thôi mà có..."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "一度 + でも (+ ば/たら) vs 一度 + も (+ ない)",
                "difference_vi": "一度でも dùng trong câu điều kiện/khẳng định ('dù chỉ 1 lần thôi'); 一度も bắt buộc đi với thể phủ định ('chưa từng 1 lần nào').",
                "quick_test_vi": "Sau 一度 có 会ったことがあれば (khẳng định điều kiện, Q#15)? Chọn でも! Có ない / ていない (Passage 16)? Chọn も!",
            }
        ],
        "examples": [
            {
                "jp": "一度でも会ったことがあれば、友だちだと考える人もいる。",
                "reading_note": "いちどでもあったことがあれば、ともだちだとかんがえるひともいる。",
                "vi": "Cũng có người nghĩ rằng dù chỉ từng gặp mặt một lần thôi thì đã là bạn bè rồi.",
                "grammar_note": "Q#15: Số từ tối thiểu 一度 + でも + điều kiện あれば.",
            },
            {
                "jp": "病院が休みの日でも、電話で受付できます。",
                "reading_note": "びょういんがやすみのひでも、でんわでうけつけできます。",
                "vi": "Ngay cả vào ngày bệnh viện nghỉ khám vẫn có thể đặt lịch qua điện thoại.",
                "grammar_note": "Passage 22: Ngoại lệ quan trọng dùng N + でも.",
            },
        ],
        "source_ref": "Shin-N3-List #51(p8) | Đề .xlsx (Q15, Passages 7, 22)",
        "search_keywords": "demo so tu du chi ngay ca でも 一度でも 日でも",
        "match_patterns": ["一度でも", "日でも", "でもかまい", "でも知っている"],
    },
    {
        "code": "GP-N3-044",
        "pattern": "～も～ない / にも (Hoàn toàn không chút nào / Đến ngay cả ở... cũng)",
        "jlpt_level": "N3",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": True,
        "formation_formula": "[1] [Số 1 / Lượng tối thiểu] + も + Phủ định (Hoàn toàn không) | [2] N + にも (Ngay cả ở nơi/đối tượng... cũng)",
        "formation_table": [
            {"pos": "1. Số từ nhỏ '1' + も + ない", "rule": "Không một chút nào (一日も休まない, いちども行っていない, 一人も来なかった)"},
            {"pos": "2. N + にも / にも～がある", "rule": "Đến cả ở... cũng (山の上にも店がある, 植物にも栄養が必要だ)"},
        ],
        "core_meaning_vi": "Phủ định sạch trơn khi gắn も sau lượng từ '1' + phủ định, hoặc mở rộng phạm vi 'cả ở N cũng có'",
        "deep_explanation_vi": (
            "Đây là bẫy đối lập với Q#15: も sau số từ nhỏ (一度も, 一日も) CHỈ đi với vị ngữ PHỦ ĐỊNH ở phía sau (như Passage 16: '結婚してからいちどもお寺にいっていない'). "
            "Nếu câu sau ở thể khẳng định hoặc điều kiện khẳng định (như Q#15: '一度（　）会ったことがあれば'), thì も bị loại ngay!"
        ),
        "register_tag": "Trung tính",
        "confusable_pairs": [
            {
                "rival_pattern": "一度も + ない vs 一度でも + ば/たら",
                "difference_vi": "一度も luôn bắt cặp với phủ định; 一度でも luôn đi với điều kiện hoặc mong muốn tối thiểu.",
                "quick_test_vi": "Nhìn động từ ngay sau số từ: ない/ていない -> も; あれば/いい -> でも.",
            }
        ],
        "examples": [
            {
                "jp": "結婚してからいちどもお寺にいっていない。",
                "reading_note": "けっこんしてからいちどもおてらにいっていない。",
                "vi": "Từ sau khi kết hôn tôi chưa đi thăm chùa lấy một lần nào.",
                "grammar_note": "Passage 16: いちども đi với phủ định いっていない = 全然行っていない.",
            },
            {
                "jp": "こんなに高い山の上にも店がある。",
                "reading_note": "こんなにたかいやまのうえにもみせがある。",
                "vi": "Đến ngay cả trên đỉnh núi cao thế này mà cũng có cửa hàng.",
                "grammar_note": "にも nhấn mạnh sự tồn tại ở nơi không ngờ tới.",
            },
        ],
        "source_ref": "Shin-N3-List #52(p8) | Đề .xlsx (Q15, Passage 16)",
        "search_keywords": "ichidomo mo nai nimo hoan toan khong いちども 一度も にも",
        "match_patterns": ["いちども", "一度も", "にも"],
    },
    {
        "code": "GP-N3-045",
        "pattern": "～まで / ～までして (Tới cả... cũng)",
        "jlpt_level": "N3",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": False,
        "formation_formula": "N + まで / Vて + まで",
        "formation_table": [
            {"pos": "Danh từ + まで", "rule": "Đến cả đối tượng không ngờ tới cũng... (子どもにまで, 家族までが)"},
            {"pos": "Động từ thể て + まで", "rule": "Làm tới mức cực đoan đến cả V mà vẫn... (徹夜してまで, うそをついてまで)"},
        ],
        "core_meaning_vi": "Đưa ra ví dụ cực đoan ở mức cao bất ngờ ('tới cả... cũng', 'làm tới mức... để mà')",
        "deep_explanation_vi": (
            "Khác với まで chỉ mốc thời gian/không gian kết thúc ở N5, trong N3 まで đứng thay cho が/を (hoặc sau trợ từ khác như にまで) để bày tỏ sự ngạc nhiên trước một phạm vi vượt ngưỡng bình thường."
        ),
        "register_tag": "Trung tính (Nhấn mạnh ngạc nhiên)",
        "confusable_pairs": [
            {
                "rival_pattern": "N + まで (vượt ngưỡng) vs N + さえ (tối thiểu)",
                "difference_vi": "まで thường đi lên mức cao đáng ngạc nhiên ('thậm chí cả người xa lạ / cấp trên cũng...'); さえ thường đi xuống mức tối thiểu ('ngay cả cái tối thiểu nhất cũng không có').",
                "quick_test_vi": "Thấy Vて + ＿＿ + (làm quá mức như thức trắng đêm để...) -> まで.",
            }
        ],
        "examples": [
            {
                "jp": "会ったことがない人にまで年賀状を出した。",
                "reading_note": "あったことがないひとにまでねんがじょうをだした。",
                "vi": "Tôi gửi thiệp chúc Tết tới cả những người mình chưa từng gặp mặt.",
                "grammar_note": "に + まで mở rộng phạm vi vượt mức thông thường.",
            },
            {
                "jp": "借金をしてまで高い車を買う必要はない。",
                "reading_note": "しゃっきんをしてまでたかいくるまをかうひつようはない。",
                "vi": "Không cần thiết phải đi vay nợ tới mức đó để mua xe đắt tiền.",
                "grammar_note": "Vて + まで = chấp nhận làm tới mức cực đoan.",
            },
        ],
        "source_ref": "Shin-N3-List #53(p8)",
        "search_keywords": "made made shite toi ca cung まで にまで てまで",
        "match_patterns": ["にまで", "てまで", "までが"],
    },
    {
        "code": "GP-N3-046",
        "pattern": "～など / ～なんか / ～なんて (Chẳng hạn; Những thứ như là - coi nhẹ)",
        "jlpt_level": "N3",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": True,
        "formation_formula": "N / V普通形 + など (Trung tính/lịch sự) | なんか / なんて (Khẩu ngữ - coi nhẹ hoặc ngạc nhiên)",
        "formation_table": [
            {"pos": "～など (Lịch sự / Trung tính)", "rule": "Đưa ví dụ đại diện trong văn viết/lịch sự (傷があるところ、目のまわり、くちびるなど; 絵本・雑誌・漫画など)"},
            {"pos": "～なんか (Coi nhẹ / Khiêm tốn)", "rule": "Khẩu ngữ: xem nhẹ, không thèm (ダイエットなんかしたくない)"},
            {"pos": "～なんて (Ngạc nhiên / Coi nhẹ)", "rule": "Thán phục ('バイオリンもひけるなんて!') hoặc coi thường ('あいさつなんて')"},
        ],
        "core_meaning_vi": "Liệt kê ví dụ mang tính đại diện (など) hoặc bày tỏ thái độ coi nhẹ/kinh ngạc trong khẩu ngữ (なんか・なんて)",
        "deep_explanation_vi": (
            "Ba từ này xuất hiện dày đặc trong đề thi: 1) など liệt kê trung tính trong tờ rơi/hướng dẫn (Passages 1, 2, 7, 16, 18). "
            "2) なんて vừa dùng để cảm thán thán phục ở Q#60 ('バイオリンもひけるなんて、すごいですね'), vừa dùng để coi nhẹ ở Passage 15 ('「あいさつなんて」と軽く考えてはいけない'). "
            "3) なんか luôn mang sắc thái xem nhẹ hoặc khiêm tốn trong hội thoại, nên ở Q#154 ('言葉 [さえ] できなくても') loại なんか vì nhân vật chỉ nêu thực tế 'ngay cả ngôn ngữ không biết' chứ không chê bai ngôn ngữ."
        ),
        "register_tag": "Trung tính (など) & Khẩu ngữ (なんか・なんて)",
        "confusable_pairs": [
            {
                "rival_pattern": "～など vs ～なんか vs ～なんて",
                "difference_vi": "など trung tính dùng được trong văn viết/hướng dẫn; なんか khẩu ngữ thiên về coi nhẹ/tự ti; なんて dùng được cả coi nhẹ lẫn cảm thán ngạc nhiên.",
                "quick_test_vi": "Văn bản tờ rơi/báo chí -> など; cảm thán 'thật không ngờ lại...' (Q#60) -> なんて.",
            }
        ],
        "examples": [
            {
                "jp": "「あいさつなんて」と軽く考えてはいけない。",
                "reading_note": "「あいさつなんて」とかるくかんがえてはいけない。",
                "vi": "Không được coi nhẹ kiểu 'chỉ là chào hỏi thôi mà'.",
                "grammar_note": "Passage 15: なんて diễn tả thái độ xem nhẹ điều nhỏ nhặt.",
            },
            {
                "jp": "ピアノばかりでなくバイオリンもひけるなんて、すごいですね。",
                "reading_note": "ぴあのばかりでなくばいおりんもひけるなんて、すごいですね。",
                "vi": "Chơi được không chỉ piano mà cả violin nữa, thật đáng nể quá đi.",
                "grammar_note": "Q#60: なんて thể hiện sự ngạc nhiên thán phục.",
            },
        ],
        "source_ref": "Shin-N3-List #54(p8) | Đề .xlsx (Q60, Q154, Passages 1, 7, 15)",
        "search_keywords": "nado nanka nante chang han coi nhe ngac nhien など なんか なんて",
        "match_patterns": ["なんて", "なんか", "など"],
    },
    {
        "code": "GP-N3-047",
        "pattern": "～について / ～に関して / ～に関する (Về chủ đề / Liên quan đến)",
        "jlpt_level": "N3",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": True,
        "formation_formula": "N + について / についての + N | N + に関して / に関する + N",
        "formation_table": [
            {"pos": "～について", "rule": "Về một chủ đề trực tiếp (hỏi, nói, suy nghĩ, tìm hiểu: 問題についてコメントする, 内容についてアイデアを出し合う)"},
            {"pos": "～に関して (Trang trọng / Rộng)", "rule": "Liên quan đến lĩnh vực/vấn đề nói chung (thường rộng hơn について)"},
            {"pos": "Bổ nghĩa danh từ", "rule": "N1 + についての + N2 <-> N1 + に関する + N2 (日本文化に関すること)"},
        ],
        "core_meaning_vi": "Định vị chủ đề được đề cập, thảo luận hoặc nghiên cứu ('về vấn đề N', 'liên quan đến N')",
        "deep_explanation_vi": (
            "Cả について và に関して đều cực kỳ quen thuộc trong đề thi (Q#26: 日本文化に関すること; Q#124: その問題についてはコメントできません; Passage 6: 交流会の内容について; Passage 10: 講演会の準備について; Q#16 & Q#53 làm phương án nhiễu). "
            "Lưu ý hình thái bổ nghĩa danh từ: sau について phải chèn の (～についての本), còn に関して đổi thành に関する (～に関する本, như Q#26: 日本文化に関することだけです)."
        ),
        "register_tag": "Trung tính (について) & Trang trọng (に関して)",
        "confusable_pairs": [
            {
                "rival_pattern": "～について / ～に関して vs ～に対して",
                "difference_vi": "について/に関して = về nội dung/chủ đề (nói, viết, suy nghĩ, điều tra); に対して = hướng thái độ vào đối tượng hoặc đối lập 2 vế.",
                "quick_test_vi": "Vế sau là nói/bàn bạc/nghiên cứu/bình luận (話す・話し合う・コメントする・こと) -> について/に関して; Vế sau tương phản 2 đối tượng (Q#53) -> に対して.",
            }
        ],
        "examples": [
            {
                "jp": "スピーチのテーマは何でもいいというわけではなく日本文化に関することだけです。",
                "reading_note": "すぴーちのてーまはなんでもいいというわけではなくにほんぶんかにかんすることだけです。",
                "vi": "Chủ đề bài phát biểu không phải cái gì cũng được, mà chỉ giới hạn ở những điều liên quan đến văn hóa Nhật.",
                "grammar_note": "Q#26: N + に関する + こと.",
            },
            {
                "jp": "その問題については、よくわからないのでコメントできません。",
                "reading_note": "そのもんだいについては、よくわからないのでこめんとできません。",
                "vi": "Về vấn đề đó thì vì không rõ lắm nên tôi không thể bình luận.",
                "grammar_note": "Q#124: N + については đặt chủ đề cần phát biểu.",
            },
        ],
        "source_ref": "Shin-N3-List #55(p8) | anki #15 | Đề .xlsx (Q16, Q26, Q53, Q124, Passages 6, 10)",
        "search_keywords": "ni tsuite ni kanshite ni kansuru ve chu de lien quan den について に関して に関する",
        "match_patterns": ["について", "に関しては", "に関して", "に関する"],
    },
    {
        "code": "GP-N3-048",
        "pattern": "～にとって (Đối với - Xét từ góc độ, lập trường đánh giá)",
        "jlpt_level": "N3",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": True,
        "formation_formula": "N(người / tổ chức / lập trường) + にとって（は） / にとっての + N",
        "formation_table": [
            {"pos": "Danh từ đứng trước", "rule": "Chỉ người, tập thể hoặc sinh vật có góc nhìn/trải nghiệm (私にとって, 若い人にとって, スポーツ選手にとって, マグロにとって)"},
            {"pos": "Vị ngữ đi kèm bắt buộc", "rule": "Tính từ hoặc danh từ ĐÁNH GIÁ giá trị/cảm nhận (大切だ, 必要だ, 重要だ, 難しい, 暮らしづらい)"},
        ],
        "core_meaning_vi": "Đứng trên góc độ, lập trường hoặc lợi ích của chủ thể N để đưa ra nhận xét, đánh giá ('đối với N mà nói thì...')",
        "deep_explanation_vi": (
            "Đây là cặp hay bị dịch word-by-word nhầm với ～に対して và ～によって (thi ở Q#151, Passage 19, Q#32, Kosei p.7/p.8): "
            "Tiếng Việt đều dịch là 'đối với', nhưng ～にとって LUÔN LUÔN đi với câu NHẬN XÉT / ĐÁNH GIÁ ('đối với VĐV thì tư duy tích cực là cần thiết' trong Passage 19; 'đối với người trẻ thì bắt chuyện với người lạ hơi căng thẳng' trong Kosei p.7). "
            "Tuyệt đối không dùng にとって với động từ hành động hay bị động (như Q#151: '植物が出す水分 [によって] 冷やされている' -> loại にとって!)."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "～にとって vs ～に対して vs ～によって",
                "difference_vi": "にとって = đứng trên lập trường N để đánh giá (vế sau là tính từ/nhận xét); に対して = hướng hành động vào N hoặc tương phản 2 vế; によって = tác nhân bị động hoặc tùy vào.",
                "quick_test_vi": "Thấy 必要だ / 大切だ / 難しい / 暮らしづらい ở cuối câu -> にとって; thấy bị động 冷やされている -> によって.",
            }
        ],
        "examples": [
            {
                "jp": "前向きな考え方こそが、外国で活躍するスポーツ選手にとって必要なのだろう。",
                "reading_note": "まえむきなかんがえかたこそが、がいこくでかつやくするすぽーつせんしゅにとってひつようなのだろう。",
                "vi": "Chính lối suy nghĩ tích cực mới là điều cần thiết đối với các vận động viên thi đấu ở nước ngoài.",
                "grammar_note": "Passage 19: N(スポーツ選手) + にとって + 必要だ (đánh giá).",
            },
            {
                "jp": "マグロにとって暮らしづらい環境になったこと。",
                "reading_note": "まぐろにとってくらしづらいかんきょうになったこと。",
                "vi": "Việc trở thành môi trường khó sống đối với loài cá ngừ.",
                "grammar_note": "Q#32: Đánh giá tính chất môi trường đối với cá ngừ.",
            },
        ],
        "source_ref": "Shin-N3-List #56(p8) | anki #14 | Đề .xlsx (Q32, Q151, Passage 19)",
        "search_keywords": "ni totte doi voi lap truong danh gia にとって",
        "match_patterns": ["にとって"],
    },
    {
        "code": "GP-N3-049",
        "pattern": "～として / ～としても (Với tư cách là, vai trò là)",
        "jlpt_level": "N3",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": True,
        "formation_formula": "N + として / としては / としての + N | [Nhượng bộ] 普通形 + としても (Giả sử dù có... đi nữa)",
        "formation_table": [
            {"pos": "1. N + として (Vai trò/Tư cách)", "rule": "N + として (掃除用具として, チームの代表として, 正しいものはどれか)"},
            {"pos": "2. N1 + としての + N2", "rule": "Bổ nghĩa danh từ (代表としての責任 = trách nhiệm với tư cách đại diện)"},
            {"pos": "3. Mệnh đề + としても (Passage 3)", "rule": "Dù có giả sử cho là như vậy đi nữa thì... (音楽を楽しむのはいいとしても...)"},
        ],
        "core_meaning_vi": "Xác định tư cách, chức năng hoặc vai trò của danh từ (Nとして); khi đi sau mệnh đề là nhượng bộ 'dù có công nhận là... đi nữa' (～としても)",
        "deep_explanation_vi": (
            "Đây là mẫu xuất hiện lặp lại cả 2 đề 問題2 ★ (Q#25: '掃除用具として使うことにした'; Q#57: 'チームの代表として試合に出ることになった') lẫn Đọc hiểu (Passage 3: '音楽を楽しむのはいいとしても', Q#65 & Q#145: '正しいものとして'). "
            "Lưu ý: sau として không thể đặt trực tiếp vào câu mà quên ghép danh từ đứng trước (N + として)."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "N + として vs N + にとって",
                "difference_vi": "として chỉ VAI TRÒ, CHỨC NĂNG, TƯ CÁCH thực hiện ('dùng làm dụng cụ / ra sân với tư cách đại diện'); にとって chỉ LẬP TRƯỜNG CẢM NHẬN ('đối với tôi thì nó rất quý').",
                "quick_test_vi": "Dùng vật A làm chức năng B hoặc giữ chức vụ B -> として.",
            }
        ],
        "examples": [
            {
                "jp": "古くなった歯ブラシを掃除用具として使うことにした。",
                "reading_note": "ふるくなったはぶらしをそうじようぐとしてつかうことにした。",
                "vi": "Tôi quyết định dùng bàn chải đánh răng cũ làm dụng cụ vệ sinh.",
                "grammar_note": "Q#25: Danh từ vai trò 掃除用具 + として.",
            },
            {
                "jp": "音楽を楽しむのはいいとしても、あまり大きな音で聞くのはどうだろうか。",
                "reading_note": "おんがくをたのしむのはいいとしても、あまりおおきなおとできくのはどうだろうか。",
                "vi": "Dù việc thưởng thức âm nhạc là tốt đi nữa, nhưng nghe âm lượng quá lớn thì có ổn không?",
                "grammar_note": "Passage 3: Tính từ + としても thừa nhận một phần trước khi phản biện.",
            },
        ],
        "source_ref": "Shin-N3-List #57 | Đề .xlsx (Q25, Q57, Q65, Passage 3)",
        "search_keywords": "to shite to shite mo voi tu cach vai tro として としても としての",
        "match_patterns": ["として", "としても", "としての"],
    },
    {
        "code": "GP-N3-050",
        "pattern": "～ことがある (Thỉnh thoảng có lúc xảy ra)",
        "jlpt_level": "N3",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": True,
        "formation_formula": "Vる / Vない + ことがある / もある",
        "formation_table": [
            {"pos": "V thể từ điển + ことがある", "rule": "Thỉnh thoảng có lúc xảy ra (つらくなることもあるだろう, 遅れることがある)"},
            {"pos": "Vない + ことがある", "rule": "Thỉnh thoảng cũng có lúc KHÔNG làm (返事をしないことがある)"},
            {"pos": "Phân biệt thì Vた vs Vる", "rule": "Vた + ことがある (N5: Đã từng trải qua) ≠ Vる + ことがある (N3: Đôi khi có lúc)"},
        ],
        "core_meaning_vi": "Diễn tả một sự việc hoặc trạng thái không thường xuyên nhưng thỉnh thoảng vẫn xảy ra trong một số trường hợp",
        "deep_explanation_vi": (
            "Mẫu này thi trực tiếp ở Bài Đục lỗ 3 Câu [4] (Q#156: '努力し続けたら、つらくなる [こともある] だろう') và xuất hiện ở Passage 3 ('思わせられることがある') & Kosei p.11 ('温度差は10度以上になることもある'). "
            "Khi kiểm tra 4 lựa chọn ở Q#156, nhớ đối lập trực tiếp giữa こともある (đôi khi có lúc xảy ra) với ことはない (không cần thiết phải làm / không đời nào)."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vる + ことがある vs Vる + ことはない vs Vた + ことがある",
                "difference_vi": "Vる+ことがある = đôi khi có lúc; Vる+ことはない = không cần thiết phải; Vた+ことがある = đã từng trải qua.",
                "quick_test_vi": "Ngữ cảnh nói hệ quả có thể thỉnh thoảng xảy ra ('nếu cố quá thì có lúc sẽ thấy mệt' - Q#156) -> こともある.",
            }
        ],
        "examples": [
            {
                "jp": "努力し続けたら、つらくなることもあるだろう。",
                "reading_note": "どりょくしつづけたら、つらくなることもあるだろう。",
                "vi": "Nếu cứ gồng mình nỗ lực mãi thì cũng có lúc trở nên khổ sở đấy.",
                "grammar_note": "Q#156: Vる (つらくなる) + こともある + だろう.",
            },
            {
                "jp": "妻は僕が話しかけても返事をしないことがある。",
                "reading_note": "つまはぼくがはなしかけてもへんじをしないことがある。",
                "vi": "Vợ tôi có lúc tôi nói chuyện cũng không trả lời lại.",
                "grammar_note": "Vない + ことがある diễn tả tần suất thỉnh thoảng.",
            },
        ],
        "source_ref": "Shin-N3-List #58 | Kosei p.11 | Đề .xlsx (Q156, Passage 3)",
        "search_keywords": "koto ga aru koto mo aru doi khi co luc ことがある こともある",
        "match_patterns": ["こともある", "ことがある"],
    },
    {
        "code": "GP-N3-051",
        "pattern": "～ことはない (Không cần thiết phải... / Không đời nào)",
        "jlpt_level": "N3",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": True,
        "formation_formula": "Vる + ことはない / ことはありません",
        "formation_table": [
            {"pos": "Nghĩa 1: Không cần thiết", "rule": "Vる + ことはない (そんなに心配することはないよ, 責任を感じることはない)"},
            {"pos": "Nghĩa 2: Không đời nào / Chẳng bao giờ", "rule": "Vる + ことはない (Trong hoàn cảnh bình thường chuyện đó không xảy ra)"},
        ],
        "core_meaning_vi": "Khuyên nhủ, trấn an rằng 'không cần thiết phải làm V đâu' (tương đương ～する必要はない)",
        "deep_explanation_vi": (
            "Xuất hiện làm phương án nhiễu trực tiếp trong Q#156 ('つらくなる [ことはない] だろう' bị loại vì mâu thuẫn với mạch câu sau khuyên không nên lo lắng quá mức để khỏi khổ). "
            "Khi dùng để an ủi ai đó đang lo lắng hoặc tự trách bản thân ('không việc gì phải lo / không cần phải thấy có lỗi'), Vる + ことはない là mẫu cực kỳ tự nhiên."
        ),
        "register_tag": "Trung tính (Hội thoại khuyên nhủ)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vる + ことはない vs Vる + こともある vs Vない + ことはない",
                "difference_vi": "Vる+ことはない = không cần thiết phải; Vる+こともある = thỉnh thoảng có lúc; Vない+ことはない = không phải là không (có thể).",
                "quick_test_vi": "Thấy động từ tâm lý lo âu (心配する・焦る・気にする) + giọng khuyên trấn an -> ことはない.",
            }
        ],
        "examples": [
            {
                "jp": "面接の質問は簡単です。そんなに心配することはありませんよ。",
                "reading_note": "めんせつのしつもんはかんたんです。そんなにしんぱいすることはありませんよ。",
                "vi": "Câu hỏi phỏng vấn dễ lắm. Không cần phải lo lắng đến thế đâu.",
                "grammar_note": "Vる (心配する) + ことはありません để trấn an.",
            },
            {
                "jp": "君が一人で責任を感じることはない。",
                "reading_note": "きみがひとりでせきにんをかんじることはない。",
                "vi": "Cậu không cần thiết phải một mình cảm thấy có trách nhiệm đâu.",
                "grammar_note": "Bằng nghĩa với 責任を感じる必要はない.",
            },
        ],
        "source_ref": "Shin-N3-List #59 | anki #8 | Đề .xlsx (Q156)",
        "search_keywords": "koto wa nai khong can thiet phai ことはない ことはありません",
        "match_patterns": ["ことはない", "ことはありません"],
    },
    {
        "code": "GP-N3-052",
        "pattern": "まるで～ようだ / ～ように / ～のような (Giống như là / Đúng như)",
        "jlpt_level": "N3",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": True,
        "formation_formula": "(まるで) + [V普通形/Aい/Aなな/Nの] + ようだ / ような + N / ように + V",
        "formation_table": [
            {"pos": "1. So sánh ví von", "rule": "(まるで) + Nの / V普通形 + ようだ / ような + N (まるで春が来たかのようだ, ウサギがもちをついているような形)"},
            {"pos": "2. Đúng như đã nói/học", "rule": "Vた / Nの + ように (前にも話したように, 同じように)"},
            {"pos": "3. Nêu ví dụ minh họa", "rule": "N1 + のような + N2 (にんじんのような濃い色の野菜)"},
        ],
        "core_meaning_vi": "So sánh ví von giống như (まるで～ようだ), liệt kê ví dụ tiêu biểu (N1のようなN2) hoặc nhắc lại điều đã nói trước đó (～ように)",
        "deep_explanation_vi": (
            "Đây là mẫu chuyển tiếp rất hay gặp trong bài đọc hiểu N3 (Passage 5: 'ウサギがもちをついているような形に見える'; Q#30: '社会ですぐに役に立つ科目と同じように'; Q#136: '現実とは思えない' tương phản ví von). "
            "Cần chú ý dạng chia khi đứng trước Danh từ dùng ような (như ような形), trước Động từ/Tính từ dùng ように (như 同じように), và ở cuối câu dùng ようだ. Sau danh từ bắt buộc thêm の (春のような)."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "N + のような + N2 vs N + っぽい + N2",
                "difference_vi": "のような là so sánh tương đồng trọn vẹn ('hình dáng giống như con thỏ'); っぽい gắn vào gốc tính từ/danh từ để chỉ tính chất hơi ngả sang hoặc chê ('黒っぽい模様' = hoa văn hơi đen, Q#61).",
                "quick_test_vi": "Đứng sau gốc tính từ bỏ い (như 黒) -> っぽい; đứng sau mệnh đề hoặc N+の -> ような.",
            }
        ],
        "examples": [
            {
                "jp": "月にある黒っぽい模様が、ウサギがもちをついているような形に見える。",
                "reading_note": "つきにあるくろっぽいもようが、うさぎがもちをついているようなかたちにみえる。",
                "vi": "Hoa văn hơi đen trên mặt trăng trông giống hình dáng con thỏ đang giã bánh dày.",
                "grammar_note": "Passage 5: Mệnh đề + ような + danh từ 形.",
            },
            {
                "jp": "社会ですぐに役に立つ科目と同じように、他の科目の学習も大事だ。",
                "reading_note": "しゃかいですぐにやくにたつかもくとおなじように、ほかのかもくのがくしゅうもだいじだ。",
                "vi": "Giống như các môn học có ích ngay trong xã hội, việc học các môn khác cũng quan trọng.",
                "grammar_note": "Q#30: 同じ + ように dùng để so sánh ngang bằng.",
            },
        ],
        "source_ref": "Shin-N3-List #60, #61, #62 | Đề .xlsx (Q30, Q61, Passage 5)",
        "search_keywords": "you na you ni marude giong nhu vi du dung nhu ようだ ような ように まるで",
        "match_patterns": ["ような形", "同じように", "まるで", "のような"],
    },
    {
        "code": "GP-N3-053",
        "pattern": "～ばかりいる / Nばかり (Suốt ngày chỉ toàn...)",
        "jlpt_level": "N3",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": True,
        "formation_formula": "Vて + ばかりいる (Suốt ngày chỉ toàn làm V) | N + ばかり (Toàn là N)",
        "formation_table": [
            {"pos": "1. Động từ thể て + ばかりいる", "rule": "Chỉ hành động lặp đi lặp lại thái quá (仕事をしてばかりいると, 毎日寝てばかりいる, なってばかりいる)"},
            {"pos": "2. Danh từ + ばかり", "rule": "Chỉ toàn là N trong một tập hợp (漫画ばかり読んでいる, 変な電話ばかりかかってくる)"},
            {"pos": "Bẫy gắn từ (Q#55)", "rule": "Vて + ばかりいる (ĐÚNG) <-> Vて + だらけだ (SAI hoàn toàn vì だらけ chỉ đi với N!)"},
        ],
        "core_meaning_vi": "Phàn nàn, chê trách việc chủ thể lặp đi lặp lại mãi một hành động (Vてばかりいる) hoặc chỉ toàn tập trung vào một thứ (Nばかり)",
        "deep_explanation_vi": (
            "Đây là mẫu thi liên tiếp trong cả Q#20 ('そんなに仕事を [してばかりいると]、体をこわしますよ') và Q#55 ('夏休みになって毎日寝て [ばかりいる]'). "
            "Hai nguyên tắc vàng để không bao giờ sập bẫy: "
            "1) Phân biệt với Vた + ばかりだ (vừa mới xong — Q#20): してばかりいる dùng thể て + ばかりいる. "
            "2) Phân biệt với N + だらけ (toàn những thứ bẩn/lỗi — Q#55): sau động từ thể て (寝て) CẤM dùng だらけ, chỉ có thể dùng ばかりいる!"
        ),
        "register_tag": "Trung tính (Hội thoại & Than phiền)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vて + ばかりいる vs N + だらけ vs Vた + ばかりだ",
                "difference_vi": "Vて+ばかりいる = suốt ngày làm mãi 1 việc; N+だらけ = bề mặt/tập hợp đầy thứ bẩn/lỗi (chỉ đi với Danh từ); Vた+ばかりだ = vừa mới làm xong.",
                "quick_test_vi": "Thấy động từ thể て ngay trước chỗ trống (寝て, して) -> chốt ばかりいる!",
            }
        ],
        "examples": [
            {
                "jp": "そんなに仕事をしてばかりいると、体をこわしますよ。",
                "reading_note": "そんなにしごとをしてばかりいると、からだをこわしますよ。",
                "vi": "Nếu bạn cứ suốt ngày chỉ toàn làm việc nhiều như thế thì sẽ đổ bệnh đấy.",
                "grammar_note": "Q#20: Vて (して) + ばかりいる + と.",
            },
            {
                "jp": "夏休みになって毎日寝てばかりいる。",
                "reading_note": "なつやすみになってまいにちねてばかりいる。",
                "vi": "Từ khi nghỉ hè đến giờ, ngày nào tôi cũng chỉ toàn ngủ.",
                "grammar_note": "Q#55: Vて (寝て) + ばかりいる (loại だらけだ vì だらけ chỉ đi sau danh từ).",
            },
        ],
        "source_ref": "Shin-N3-List #65, #66 | Đề .xlsx (Q20, Q52, Q55, Q153, Q154)",
        "search_keywords": "te bakari iru suot ngay chi toan ばかりいる てばかりいる",
        "match_patterns": ["ばかりいる", "ばかりいると", "ばかりいた"],
    },
    {
        "code": "GP-N3-054",
        "pattern": "～ばかりでなく / ～ばかりか (Không chỉ... mà còn...)",
        "jlpt_level": "N3",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": True,
        "formation_formula": "N / 普通形(Aなな/Nである) + ばかりでなく / ばかりか + ～も / ～まで",
        "formation_table": [
            {"pos": "Cấu trúc chuẩn", "rule": "A + ばかりでなく + B + も (ピアノばかりでなくバイオリンもひける)"},
            {"pos": "Biến thể tăng tiến mạnh", "rule": "A + ばかりか + B + まで (会社ばかりか家族にまでバカにされている)"},
            {"pos": "Đồng nghĩa N4/N3", "rule": "Tương đương ～だけでなく (như Q#101: デザインだけではなく)"},
        ],
        "core_meaning_vi": "Không chỉ dừng lại ở A mà còn mở rộng thêm cả B (thường nhấn mạnh sự vượt mong đợi)",
        "deep_explanation_vi": (
            "Mẫu này thi trực tiếp trong 問題2 ★ Q#60 ('ピアノ [ばかり] [でなく] [バイオリン] [も] ひけるなんて、すごいですね'). "
            "Trong bài thi ghép sao ★, khi thấy các mảnh rời `ばかり`, `でなく`, `も`, hãy lập tức khóa khung [N1 + ばかり + でなく + N2 + も]. "
            "Lưu ý ばかりか có mức độ bất ngờ mạnh hơn ばかりでなく một bậc (nhất là khi đi với まで ở vế sau)."
        ),
        "register_tag": "Trung tính & Văn viết",
        "confusable_pairs": [
            {
                "rival_pattern": "～ばかりでなく～も vs ～だけでなく～も vs ～ばかりか～まで",
                "difference_vi": "ばかりでなく và だけでなく dùng song hành trung tính ('không chỉ A mà còn B'); ばかりか...まで nhấn mạnh sự tăng cấp gây ngạc nhiên hoặc nghiêm trọng hơn.",
                "quick_test_vi": "Gặp chuỗi mảnh ばかり / でなく / も -> ráp cặp [N1 ばかりでなく N2 も].",
            }
        ],
        "examples": [
            {
                "jp": "ピアノばかりでなくバイオリンもひけるなんて、すごいですね。",
                "reading_note": "ぴあのばかりでなくばいおりんもひけるなんて、すごいですね。",
                "vi": "Không chỉ chơi được piano mà còn chơi được cả violin nữa, thật là giỏi quá đi.",
                "grammar_note": "Q#60: N1 (ピアノ) + ばかりでなく + N2 (バイオリン) + も.",
            },
            {
                "jp": "山田さんは英語ばかりでなく中国語も話せる。",
                "reading_note": "やまださんはえいごばかりでなくちゅうごくごもはなせる。",
                "vi": "Anh Yamada không chỉ nói được tiếng Anh mà cả tiếng Trung nữa.",
                "grammar_note": "N1 + ばかりでなく + N2 + も.",
            },
        ],
        "source_ref": "Shin-N3-List #67 | Đề .xlsx (Q60, Q101)",
        "search_keywords": "bakari de naku bakari ka khong chi ma con ばかりでなく ばかりか だけではなく",
        "match_patterns": ["ばかりでなく", "ばかりか", "だけではなく"],
    },
    {
        "code": "GP-N3-055",
        "pattern": "～ばかりに (Chỉ tại vì...) & ～ばかりだ (Cứ ngày càng... / Chỉ còn chờ...)",
        "jlpt_level": "N3",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": False,
        "formation_formula": "普通形(Aなな/Nな・である) + ばかりに (Chỉ vì) | Vる + ばかりだ (Cứ ngày càng xấu đi / Chỉ còn mỗi việc làm V)",
        "formation_table": [
            {"pos": "1. ～ばかりに (Chỉ tại vì)", "rule": "Chỉ một nguyên nhân duy nhất gây ra hậu quả đáng tiếc kéo dài (ほんの一言言わなかったばかりに...)"},
            {"pos": "2. Vる + ばかりだ (Xu hướng xấu)", "rule": "Trạng thái tiếp tục trượt dốc không dừng (病状は悪くなるばかりだった)"},
            {"pos": "3. Vる + ばかりだ (Sẵn sàng hết)", "rule": "Mọi thứ đã chuẩn bị xong, chỉ còn mỗi việc làm bước cuối cùng (出かけるばかりになっている)"},
        ],
        "core_meaning_vi": "Nhấn mạnh nguyên nhân duy nhất dẫn đến kết cục buồn ('chỉ tại... mà ra') hoặc xu hướng tăng tiến/trạng thái chỉ còn chờ bước cuối",
        "deep_explanation_vi": (
            "Đừng nhầm ～ばかりに (có trợ từ に) với ～ばかりだ: "
            "Thêm に thành ～ばかりに biến nó thành liên từ chỉ nguyên nhân tiêu cực nhấn mạnh ('chỉ mỗi tại lỗi nhỏ đó mà hỏng hết cả việc'). "
            "Còn đứng cuối câu Vる + ばかりだ không có に giống ～一方だ (cứ ngày càng xấu đi) hoặc báo hiệu đã chuẩn bị 99% chỉ còn chờ thực hiện."
        ),
        "register_tag": "Văn viết & Biểu cảm mạnh",
        "confusable_pairs": [
            {
                "rival_pattern": "～ばかりに vs ～せいで",
                "difference_vi": "Cả hai đều chỉ nguyên nhân dẫn đến kết quả xấu, nhưng ばかりに nhấn mạnh 'CHỈ TẠI MỘT NGUYÊN NHÂN NHỎ/DUY NHẤT đó thôi mà gây hậu quả lớn nặng nề'.",
                "quick_test_vi": "Có sắc thái tiếc nuối sâu sắc vì một sai sót duy nhất (chỉ vì trễ 1 phút, chỉ vì lỡ lời) -> ばかりに.",
            }
        ],
        "examples": [
            {
                "jp": "確認しなかったばかりに、大きなミスをしてしまった。",
                "reading_note": "かくにんしなかったばかりに、おおきなみすをしてしまった。",
                "vi": "Chỉ tại vì không kiểm tra lại mà tôi đã mắc sai lầm lớn.",
                "grammar_note": "Vない quá khứ + ばかりに nhấn mạnh nguyên nhân hối tiếc.",
            },
            {
                "jp": "荷物はすべて用意して、あとは出かけるばかりだ。",
                "reading_note": "にもつはすべてよういして、あとはでかけるばかりだ。",
                "vi": "Hành lý đã chuẩn bị xong hết rồi, giờ chỉ còn mỗi việc lên đường nữa thôi.",
                "grammar_note": "あとは + Vる + ばかりだ chỉ công đoạn hoàn tất.",
            },
        ],
        "source_ref": "Shin-N3-List #69, #70",
        "search_keywords": "bakari ni bakari da chi tai vi cu ngay cang ばかりに ばかりだ",
        "match_patterns": ["ばかりに", "なるばかり"],
    },
    {
        "code": "GP-N3-056",
        "pattern": "～も～ば～も / ～も～なら～も (Vừa... vừa..., cả A cũng mà B cũng)",
        "jlpt_level": "N3",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": False,
        "formation_formula": "N1 + も + Vば / Aければ / Aななら + N2 + も + V / A",
        "formation_table": [
            {"pos": "Động từ (V)", "rule": "N1もVば、N2もV (酒も飲めばタバコも吸う = rượu cũng uống mà thuốc cũng hút)"},
            {"pos": "Tính từ (A)", "rule": "N1もAければ、N2もAい (値段も高ければ質もよい; 部屋も広ければ駅も近い)"},
            {"pos": "Danh từ / Aな", "rule": "N1もN/Aななら、N2もN/Aなだ (親も親なら子も子だ)"},
        ],
        "core_meaning_vi": "Nêu song song hai đặc điểm hoặc hai hành động cùng mức độ (cả hai mặt đều tốt hoặc đều xấu)",
        "deep_explanation_vi": (
            "Mẫu này ghép trợ từ も với thể điều kiện ば (ở vế đầu) và も ở vế sau để tạo câu đối xứng rất hay dùng trong tiếng Nhật. "
            "Lưu ý động từ/tính từ ở vế ば và vế sau thường mang CÙNG HƯỚNG đánh giá (vừa đắt lại vừa ngon, hoặc vừa uống rượu vừa hút thuốc)."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "～も～ば～も vs ～し～し",
                "difference_vi": "Cả hai đều liệt kê 2 đặc điểm song hành, nhưng ～も～ば～も mang nhịp điệu đối xứng nhấn mạnh chặt chẽ hơn giữa 2 danh từ đi với も.",
                "quick_test_vi": "Thấy danh từ 1 có も + động từ chia thể ば, ngay sau là danh từ 2 + も -> ～も～ば～も.",
            }
        ],
        "examples": [
            {
                "jp": "彼は心臓が悪いくせに、酒も飲めばタバコも吸う。",
                "reading_note": "かれはしんぞうがわるいくせに、さけものめばたばこもすう。",
                "vi": "Anh ta bị bệnh tim vậy mà rượu cũng uống, thuốc lá cũng hút.",
                "grammar_note": "飲む -> 飲めば kết hợp song hành 酒も...タバコも.",
            },
            {
                "jp": "この店は料理もおいしければ、店員の態度もとてもいい。",
                "reading_note": "このみせはりょうりもおいしければ、てんいんのたいどもとてもいい。",
                "vi": "Quán này món ăn vừa ngon mà thái độ nhân viên cũng rất tốt.",
                "grammar_note": "Tính từ い chia ければ (おいしければ).",
            },
        ],
        "source_ref": "Shin-N3-List #71",
        "search_keywords": "mo ba mo vua vua ca cung 飲めば ければ も",
        "match_patterns": ["も飲めば", "しければ"],
    },
    {
        "code": "GP-N3-057",
        "pattern": "～といった (Những thứ ví dụ như là...)",
        "jlpt_level": "N3",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": False,
        "formation_formula": "N1・N2 + といった + N(danh từ bao quát tập hợp)",
        "formation_table": [
            {"pos": "Danh từ ví dụ + といった + Danh từ tổng hợp", "rule": "タイやベトナムといったアジアの国々 (các nước châu Á như Thái Lan, Việt Nam)"},
            {"pos": "Khác với ～という", "rule": "という giải thích tên gọi cụ thể (1 cái); といった liệt kê vài ví dụ đại diện cho 1 nhóm danh từ tổng quát"},
        ],
        "core_meaning_vi": "Liệt kê một vài danh từ ví dụ tiêu biểu để làm rõ cho danh từ phạm trù đứng ngay phía sau",
        "deep_explanation_vi": (
            "～といった là phiên bản văn viết trang trọng của ～のような hoặc ～など. "
            "Luôn đặt sau 2-3 ví dụ (nối bằng や) và đứng ngay trước danh từ tổng quát bao trùm (国々, スポーツ, 問題, 食べ物)."
        ),
        "register_tag": "Văn viết & Báo chí",
        "confusable_pairs": [
            {
                "rival_pattern": "～といった vs ～という",
                "difference_vi": "という nêu định danh chính xác một vật hoặc trích dẫn mệnh đề; といった đưa ra ví dụ tiêu biểu thuộc một nhóm lớn hơn.",
                "quick_test_vi": "Có 2-3 ví dụ nối bằng や phía trước và danh từ tập hợp (国・場所・スポーツ) phía sau -> といった.",
            }
        ],
        "examples": [
            {
                "jp": "これまで、タイや中国、マレーシアといったアジアの国々を回った。",
                "reading_note": "これまで、たいやちゅうごく、まれーしあといったあじあのくにぐにをまわった。",
                "vi": "Cho đến nay tôi đã đi vòng quanh các nước châu Á như Thái Lan, Trung Quốc, Malaysia.",
                "grammar_note": "Liệt kê ví dụ + といった + danh từ tổng quát 国々.",
            },
            {
                "jp": "地震や台風といった自然災害に備えることが大切だ。",
                "reading_note": "じしんやたいふうといったしぜんさいがいにそなえることがたいせつだ。",
                "vi": "Việc phòng bị cho các thiên tai như động đất hay bão rất quan trọng.",
                "grammar_note": "地震や台風 là ví dụ của 自然災害.",
            },
        ],
        "source_ref": "Shin-N3-List #72",
        "search_keywords": "to itta vi du nhu la van viet といった",
        "match_patterns": ["といった"],
    },
    {
        "code": "GP-N3-058",
        "pattern": "～たがる (Muốn làm gì - chỉ dùng cho ngôi thứ 3)",
        "jlpt_level": "N3",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": False,
        "formation_formula": "Vます(bỏ ます) + たがる / たがっている | Aい(bỏ い) + がる / がっている",
        "formation_table": [
            {"pos": "Động từ (V)", "rule": "Vます + たがる / たがっている (知りたがる, やりたがる, 行きたがっている)"},
            {"pos": "Tính từ cảm xúc (A)", "rule": "Aい(bỏ い) + がる (怖がる, 寂しがる, 羨ましがる, ほしがる)"},
            {"pos": "Chuyển đổi thành động từ nhóm 1", "rule": "Tân ngữ đi kèm hay dùng を (彼は私の給料を知りたがっている)"},
        ],
        "core_meaning_vi": "Miêu tả biểu hiện bên ngoài cho thấy ngôi thứ 3 (anh ấy/cô ấy/người khác) muốn làm gì hoặc đang cảm thấy thế nào",
        "deep_explanation_vi": (
            "Tiếng Nhật phân tách rạch ròi cảm xúc chủ quan của người nói (たい, 怖い, 嬉しい) với cảm xúc quan sát từ người khác (ngôi thứ 3): "
            "không bao giờ nói thẳng *彼は日本へ行きたい (trừ khi thêm と言っている / ようだ), mà phải đổi sang thể quan sát biểu hiện bên ngoài 彼は日本へ行きたがっている. "
            "Lưu ý: Vたがる tự chia như động từ nhóm 1 (たがらない, たがって, たがっている) và thường dùng dạng たがっている để miêu tả trạng thái đang biểu lộ."
        ),
        "register_tag": "Trung tính",
        "confusable_pairs": [
            {
                "rival_pattern": "Vたい (Ngôi 1) vs Vたがっている (Ngôi 3)",
                "difference_vi": "たい dùng trực tiếp cho bản thân (ngôi 1) hoặc hỏi trực tiếp (ngôi 2); たがる/たがっている bắt buộc dùng khi kể về mong muốn của ngôi thứ 3 qua quan sát.",
                "quick_test_vi": "Chủ ngữ là 彼/彼女/子ども/みんな -> chọn たがる / たがっている.",
            }
        ],
        "examples": [
            {
                "jp": "彼はいつも私の給料の額を知りたがっている。",
                "reading_note": "かれはいつもわたしのきゅうりょうのがくをしりたがっている。",
                "vi": "Anh ta lúc nào cũng tò mò muốn biết mức lương của tôi.",
                "grammar_note": "Chủ ngữ ngôi 3 (彼は) + 知る -> 知りたがっている.",
            },
            {
                "jp": "妹は犬を怖がって、なかなか近づこうとしない。",
                "reading_note": "いもうとはいぬをこわがって、なかなかちかづこうとしない。",
                "vi": "Em gái tôi sợ chó nên mãi không chịu lại gần.",
                "grammar_note": "Tính từ 怖い bỏ い + がる -> 怖がる (đi với tân ngữ を).",
            },
        ],
        "source_ref": "Shin-N3-List #74",
        "search_keywords": "tagaru garu ngoi thu 3 muon bieu hien たがる たがっている がる",
        "match_patterns": ["たがる", "たがって", "がって"],
    },
    {
        "code": "GP-N3-059",
        "pattern": "～てたまらない / ～てしょうがない / ～てならない (Đến mức không chịu nổi)",
        "jlpt_level": "N3",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": False,
        "formation_formula": "Vて / Aい(くて) / Aな(で) + たまらない / しょうがない / しかたがない / ならない",
        "formation_table": [
            {"pos": "Tính từ cảm giác / Động từ tâm lý", "rule": "Aい -> Aくて (暑くてたまらない, 会いたくてたまらない); Aな -> Aで (心配でならない); Vて (気になってしょうがない)"},
            {"pos": "Giới hạn chủ ngữ", "rule": "Chỉ dùng cho cảm xúc/cảm giác sinh lý tự nhiên không kìm chế nổi của NGÔI 1 (muốn làm gì dùng Vたくてたまらない)"},
            {"pos": "～てならない (Trang trọng)", "rule": "Thiên về cảm xúc dâng trào tự nhiên trong nội tâm hoặc suy nghĩ (残念でならない, 心配してならない)"},
        ],
        "core_meaning_vi": "Diễn đạt cảm xúc, cảm giác cơ thể dâng trào tự nhiên mãnh liệt đến mức không thể kìm nén được",
        "deep_explanation_vi": (
            "Bộ 3 mẫu cảm xúc cực mạnh này không dùng với hành động chủ ý (không nói *毎日勉強してたまらない), mà CHỈ đi với cảm giác thể chất (đói, khát, nóng, đau, buồn ngủ) và tâm trạng tự nhiên (nhớ nhà, lo lắng, tò mò, muốn gặp Vたくて). "
            "Lưu ý hình thái nối: tính từ đuôi い đổi thành くて (暑くて, 会いたくて), tính từ đuôi な đổi thành で (心配で)."
        ),
        "register_tag": "Trung tính (Cảm xúc ngôi 1)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vたくてたまらない vs Vてならない",
                "difference_vi": "たまらない/しょうがない dùng rộng cho cả cảm giác cơ thể (nóng, đói, ngứa) và mong muốn (Vたくて); てならない thiên về tâm trạng sâu sắc, trăn trở mang sắc thái văn viết hơn.",
                "quick_test_vi": "Gặp tính từ cảm giác/tâm lý chia くて/で ở vế trước -> chọn たまらない/しょうがない/ならない.",
            }
        ],
        "examples": [
            {
                "jp": "夏はエアコンが使えないと暑くてたまらない。",
                "reading_note": "なつはえあこんがつかえないとあつくてたまらない。",
                "vi": "Mùa hè mà không dùng điều hòa thì nóng đến mức không chịu nổi.",
                "grammar_note": "Aい (暑い) -> 暑くて + たまらない.",
            },
            {
                "jp": "遠くに住んでいる母のことを心配してならない。",
                "reading_note": "とおくにすんでいるははのことをしんぱいしてならない。",
                "vi": "Tôi vô cùng lo lắng cho mẹ đang sống ở nơi xa.",
                "grammar_note": "Vて + ならない diễn tả nỗi lo lắng tự nhiên trào dâng.",
            },
        ],
        "source_ref": "Shin-N3-List #75 | anki #41",
        "search_keywords": "te tamaranai te shouganai te naranai khong chiu noi てたまらない てしょうがない てならない",
        "match_patterns": ["てたまらない", "てしょうがない", "てならない"],
    },
    {
        "code": "GP-N3-060",
        "pattern": "～最中に（さいちゅうに） (Đúng lúc đang diễn ra cao trào thì...)",
        "jlpt_level": "N3",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": False,
        "formation_formula": "Vている / N + の + 最中に（さいちゅうに） / 最中だ",
        "formation_table": [
            {"pos": "Động từ (V)", "rule": "Vている + 最中に (話している最中に, 試験を受けている最中に)"},
            {"pos": "Danh từ hành động (N)", "rule": "N + の + 最中に (会議の最中に, 食事の最中に)"},
            {"pos": "Vế sau điển hình", "rule": "Thường là sự việc bất ngờ xen ngang làm gián đoạn (mất điện, có chuông reo, ngất xỉu)"},
        ],
        "core_meaning_vi": "Ngay đúng lúc sự việc A đang diễn ra ở thời điểm cao trào/giữa chừng thì biến cố B đột ngột xen vào",
        "deep_explanation_vi": (
            "～最中に mạnh hơn ～間に và ～ているときに ở chỗ A phải là một hành động/sự kiện có tính liên tục đang ở cao trào (cuộc họp, bài phát biểu, bữa ăn, trận đấu), và vế sau là sự việc bất ngờ chen ngang (mất điện, điện thoại reo). "
            "Chú ý hình thái: với động từ BẮT BUỘC là Vている (không dùng Vる hay Vた)."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vている + 最中に vs Vた + とたんに vs Vている + うちに",
                "difference_vi": "最中に = đúng lúc đang giữa chừng cao trào thì bị chen ngang; とたんに = vừa mới XONG V1 thì ngay lập tức xảy ra V2; うちに = trong lúc đang A thì tự nhiên chuyển sang B.",
                "quick_test_vi": "Thấy Vている hoặc Danh từ sự kiện (会議の・食事の) + biến cố bất ngờ xen vào -> 最中に.",
            }
        ],
        "examples": [
            {
                "jp": "大切な会議の最中に、突然停電になった。",
                "reading_note": "たいせつなかいぎのさいちゅうに、とつぜんていでんになった。",
                "vi": "Đúng lúc cuộc họp quan trọng đang diễn ra thì đột ngột bị mất điện.",
                "grammar_note": "N + の + 最中に + biến cố chen ngang.",
            },
            {
                "jp": "スピーチをしている最中に、マイクの調子が悪くなった。",
                "reading_note": "すぴーちをしているさいちゅうに、まいくのちょうしがわるくなった。",
                "vi": "Ngay lúc đang phát biểu giữa chừng thì micro bị trục trặc.",
                "grammar_note": "Vている + 最中に.",
            },
        ],
        "source_ref": "Shin-N3-List #76",
        "search_keywords": "saichuu ni dung luc dang giua chung 最中に さいちゅうに",
        "match_patterns": ["最中に", "最中だ", "さいちゅうに"],
    },
    {
        "code": "GP-N3-061",
        "pattern": "～たとたん（に） (Vừa mới... thì ngay lập tức...)",
        "jlpt_level": "N3",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": True,
        "formation_formula": "Vた + とたん（に） + [Sự biến bất ngờ ngoài ý muốn]",
        "formation_table": [
            {"pos": "Động từ (V)", "rule": "Bắt buộc dùng thì quá khứ Vた (開けたとたん, 立ったとたん, 飲んだとたん)"},
            {"pos": "Giới hạn vế sau", "rule": "Sự việc xảy ra ngay tích tắc tiếp theo mang tính bất ngờ, KHÁCH QUAN (Cấm dùng ý chí, mệnh lệnh, rủ rê ở vế sau!)"},
        ],
        "core_meaning_vi": "Ngay khoảnh khắc vừa hoàn thành động tác V1 thì sự kiện bất ngờ V2 lập tức xảy ra",
        "deep_explanation_vi": (
            "Mẫu này xuất hiện làm phương án nhiễu trong Q#51 ('母はいつも、家族には [炊きたて] のごはんを食べてもらいたいと言っている', với bẫy '炊いたとたん'). "
            "Hai lỗi sai khiến thí sinh mất điểm với ～たとたん: "
            "1) ～たとたん KHÔNG bao giờ dùng để bổ nghĩa trực tiếp cho danh từ kiểu *炊いたとたんのごはん (đó là chức năng của Vます + たて + の + N). "
            "2) Vế sau của ～たとたん phải là một sự việc bất ngờ tự nhiên xảy đến, tuyệt đối không dùng mệnh lệnh hay ý định chủ động (không nói *家に着いたとたんにすぐ勉強してください)."
        ),
        "register_tag": "Trung tính (Kể lại biến cố bất ngờ)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vた + とたん vs Vます + たて + の + N",
                "difference_vi": "たとたん nối 2 mệnh đề ('vừa mở cửa thì gió thổi ùa vào'); Vます+たて bổ nghĩa danh từ để chỉ độ tươi mới vừa làm xong ('cơm vừa nấu xong nóng hổi' - Q#51).",
                "quick_test_vi": "Trước chỗ trống nối với 'のごはん' -> chọn たて; nối 2 mệnh đề xảy ra liên tiếp tích tắc -> とたん.",
            }
        ],
        "examples": [
            {
                "jp": "窓を開けたとたん、強い風が入ってきた。",
                "reading_note": "まどをあけたとたん、つよいかぜがはいってきた。",
                "vi": "Tôi vừa mở cửa sổ ra thì một luồng gió mạnh ùa vào ngay lập tức.",
                "grammar_note": "Vた (開けた) + とたん + hiện tượng tức thì ngoài ý muốn.",
            },
            {
                "jp": "彼は部屋に入ったとたんに、ベッドに倒れ込んだ。",
                "reading_note": "かれはへやにはいったとたんに、べっどにたおれこんだ。",
                "vi": "Anh ấy vừa bước vào phòng là ngã vật ngay xuống giường.",
                "grammar_note": "Sự việc xảy ra trong tích tắc nối tiếp.",
            },
        ],
        "source_ref": "Shin-N3-List #77 | Đề .xlsx (Q51)",
        "search_keywords": "ta totan ni vua moi thi ngay lap tuc たとたん 炊いたとたん",
        "match_patterns": ["たとたん", "たとたんに"],
    },
    {
        "code": "GP-N3-062",
        "pattern": "～から～にかけて (Từ... đến... - Khoảng thời gian/không gian liên tục)",
        "jlpt_level": "N3",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": False,
        "formation_formula": "N1 + から + N2 + にかけて",
        "formation_table": [
            {"pos": "Thời gian", "rule": "Từ khoảng thời gian N1 kéo sang N2 (今夜から明日にかけて, 8月から9月にかけて)"},
            {"pos": "Không gian / Địa lý", "rule": "Từ vùng N1 lan sang vùng N2 (関東から東北にかけて大雨になる)"},
        ],
        "core_meaning_vi": "Diễn đạt phạm vi thời gian hoặc khu vực trải dài tương đối ước lượng từ A sang B (biên độ rộng hơn から～まで)",
        "deep_explanation_vi": (
            "Trong bản tin thời tiết hay báo chí (như anki #35: '今夜から明日にかけて、大雨になるおそれがあります'), ～から～にかけて phổ biến hơn ～から～まで vì nó chỉ vùng chuyển tiếp ước lượng chứ không đòi hỏi ranh giới giờ/phút chính xác tuyệt đối."
        ),
        "register_tag": "Trung tính & Tin tức thời sự",
        "confusable_pairs": [
            {
                "rival_pattern": "N1からN2にかけて vs N1からN2まで",
                "difference_vi": "から～まで chỉ điểm bắt đầu và kết thúc chính xác (9時から5時まで); から～にかけて chỉ phạm vi trải rộng ước chừng (từ tối nay sang ngày mai / từ vùng này sang vùng kia).",
                "quick_test_vi": "Ngữ cảnh dự báo thời tiết, mùa vụ, khu vực địa lý -> にかけて; giờ làm việc cố định -> まで.",
            }
        ],
        "examples": [
            {
                "jp": "今夜から明日にかけて、大雨になるおそれがあります。",
                "reading_note": "こんやからあしたにかけて、おおあめになるおそれがあります。",
                "vi": "Từ đêm nay sang ngày mai, có nguy cơ sẽ xảy ra mưa lớn.",
                "grammar_note": "Thời tiết chuyển giao dùng から～にかけて kết hợp おそれがある.",
            },
            {
                "jp": "このぶどうは8月から9月にかけて収穫される。",
                "reading_note": "このぶどうははちがつからくがつにかけてしゅうかくされる。",
                "vi": "Loại nho này được thu hoạch từ khoảng tháng 8 sang tháng 9.",
                "grammar_note": "Khoảng thời gian mùa vụ liên tục.",
            },
        ],
        "source_ref": "Shin-N3-List #78 | anki #35",
        "search_keywords": "kara ni kakete tu den khoang thoi gian dia ly から にかけて",
        "match_patterns": ["にかけて"],
    },
    {
        "code": "GP-N3-063",
        "pattern": "～もの / ～もん (Ấy là tại vì... - Khẩu ngữ biện minh)",
        "jlpt_level": "N3",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": False,
        "formation_formula": "普通形(N/Aな giữ だ) + もの / もん / だもん",
        "formation_table": [
            {"pos": "Động từ / Tính từ い", "rule": "Vる/Vた/Vない/Aい + もの / もん (だって知らなかったんだもん)"},
            {"pos": "Tính từ な / Danh từ", "rule": "Aな + だ + もん; N + だ + もん (子どもなんだもん)"},
        ],
        "core_meaning_vi": "Giải thích lý do mang tính cá nhân, nũng nịu hoặc tự bào chữa trong giao tiếp thân mật ('ấy là tại vì...')",
        "deep_explanation_vi": (
            "Đây là dạng khẩu ngữ rút gọn đặt ở cuối câu của ～ものだから (nói thân mật với bạn bè, người nhà, trẻ con hay dùng もん/だもん). "
            "Tuyệt đối không dùng ～もん trong văn bản trang trọng, báo cáo hay khi nói chuyện với cấp trên."
        ),
        "register_tag": "Khẩu ngữ thân mật",
        "confusable_pairs": [
            {
                "rival_pattern": "～だもん (Cuối câu thân mật) vs ～ものだから (Thanh minh lịch sự hơn)",
                "difference_vi": "Cả hai đều để giải thích/thanh minh lý do cá nhân, nhưng ものだから lịch sự dùng nối giữa 2 mệnh đề ('バスが遅れたものだから遅刻しました'), còn だもん chỉ đặt cuối câu thân mật.",
                "quick_test_vi": "Gặp văn nói nũng nịu/bào chữa của bạn bè, kết thúc bằng だって… -> もん / だもん.",
            }
        ],
        "examples": [
            {
                "jp": "今日の試験、できなかった。だって難しかったんだもん。",
                "reading_note": "きょうのしけん、できなかった。だってむずかしかったんだもん。",
                "vi": "Bài thi hôm nay tớ không làm được. Tại vì đề khó quá mà.",
                "grammar_note": "Hô ứng với だって để tự bào chữa trong khẩu ngữ.",
            },
            {
                "jp": "まだ食べないの？ — うん、さっき食べたばかりだもの。",
                "reading_note": "まだたべないの？ — うん、さっきたべたばかりだもの。",
                "vi": "Cậu chưa ăn à? — Ừ, tại lúc nãy tớ vừa mới ăn xong mà.",
                "grammar_note": "Đuôi câu giải thích nhẹ nhàng thân mật.",
            },
        ],
        "source_ref": "Shin-N3-List #79",
        "search_keywords": "mono mon damon tai vi khau ngu だもん もの",
        "match_patterns": ["だもん", "んだもん"],
    },
    {
        "code": "GP-N3-064",
        "pattern": "～に決まっている (Chắc chắn, nhất định là - Suy đoán chủ quan mạnh)",
        "jlpt_level": "N3",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": True,
        "formation_formula": "普通形(N/Aな bỏ だ) + に決まっている（にきまっている）",
        "formation_table": [
            {"pos": "Động từ / Tính từ い", "rule": "Vる/Vた/Vない/Aい + に決まっている (反対されるに決まっている)"},
            {"pos": "Tính từ な / Danh từ", "rule": "Aな/N (bỏ だ) + に決まっている (嘘に決まっている, 彼なら合格するに決まっている)"},
        ],
        "core_meaning_vi": "Khẳng định chắc nịch theo cảm tính/niềm tin chủ quan của người nói ('chắc chắn là thế, không lệch đi đâu được')",
        "deep_explanation_vi": (
            "Đây là bẫy ngữ dụng cực kỳ quan trọng ở Bài Đục lỗ 1 Câu [5] (Q#147: '以上のことに気をつけないと、症状が [悪くなるおそれがあります]', loại '悪くなるにきまっています'). "
            "Lý do loại: ～にきまっている là SỰ QUẢ QUYẾT CHỦ QUAN mang khẩu khí cá nhân ('chắc chắn 100% là thế thôi!'), hoàn toàn không phù hợp với văn bản hướng dẫn y khoa hoặc tin tức khách quan (vốn dùng ～おそれがある để cảnh báo rủi ro có thể xảy ra)."
        ),
        "register_tag": "Khẩu ngữ / Quả quyết chủ quan",
        "confusable_pairs": [
            {
                "rival_pattern": "～に決まっている vs ～おそれがある vs ～に違いない",
                "difference_vi": "に決まっている = quả quyết chủ quan cá nhân (thường dùng khẩu ngữ); に違いない = suy luận chắc chắn có căn cứ/trực giác; おそれがある = cảnh báo nguy cơ xấu trong y tế/báo chí.",
                "quick_test_vi": "Trong tờ hướng dẫn thuốc/tin tức thời sự cảnh báo rủi ro (Q#147) -> chọn おそれがある, loại に決まっている!",
            }
        ],
        "examples": [
            {
                "jp": "一人で外国へ旅行するなんて、親に反対されるに決まっている。",
                "reading_note": "ひとりであるがいこくへりょこうするなんて、おやにはんたいされるにきまっている。",
                "vi": "Đi du lịch nước ngoài một mình thì chắc chắn bị bố mẹ phản đối là cái chắc.",
                "grammar_note": "Suy đoán chủ quan quả quyết trong giao tiếp.",
            },
            {
                "jp": "あんなに練習したのだから、彼が勝つに決まっている。",
                "reading_note": "あんなにれんしゅうしたのだから、かれがかつにきまっている。",
                "vi": "Luyện tập nhiều thế kia cơ mà, anh ấy thắng chắc rồi.",
                "grammar_note": "Khẩu ngữ thể hiện niềm tin mạnh.",
            },
        ],
        "source_ref": "Shin-N3-List #80 | Đề .xlsx (Q147)",
        "search_keywords": "ni kimatte iru chac chan chu quan に決まっている にきまっている",
        "match_patterns": ["に決まっている", "にきまっている", "にきまっています"],
    },
    {
        "code": "GP-N3-065",
        "pattern": "～に違いない (Chắc chắn là, hẳn là - おそらく～に違いない)",
        "jlpt_level": "N3",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": True,
        "formation_formula": "(おそらく) + 普通形(N/Aな bỏ だ) + に違いない（にちがいない）",
        "formation_table": [
            {"pos": "Động từ / Tính từ い", "rule": "普通形 + に違いない (大きなストレスになるに違いない, 持っていったに違いない)"},
            {"pos": "Tính từ な / Danh từ", "rule": "Aな/N (bỏ だ) + に違いない (本物に違いない, 犯人に違いない)"},
            {"pos": "Phó từ hô ứng kinh điển", "rule": "おそらく / きっと ～ に違いない (như Bài 3 Câu 1 Q#153)"},
        ],
        "core_meaning_vi": "Suy đoán có độ tin cậy rất cao (trên 90%) của người nói/người viết dựa vào lý lẽ hoặc dấu hiệu quan sát",
        "deep_explanation_vi": (
            "Thi trực tiếp ở Bài Đục lỗ 3 Câu [1] (Q#153: 'その国の言葉ができないことは、おそらく大きなストレスに [なるに違いない]'). "
            "Khác với ～に決まっている (mang khẩu khí cảm tính áp đặt), ～に違いない dùng được rộng rãi cả trong văn viết nghị luận lẫn hội thoại khi có từ khóa hô ứng おそらく (có lẽ, chắc hẳn)."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "～に違いない vs ～にすぎない vs ～はずだ",
                "difference_vi": "に違いない = chắc chắn là (suy đoán tin cậy cao); にすぎない = chẳng qua chỉ là (hạ thấp mức độ); はずだ = chắc chắn theo lịch trình/logic hiển nhiên.",
                "quick_test_vi": "Thấy phó từ おそらく đứng trước và cần kết luận suy đoán (Q#153) -> に違いない.",
            }
        ],
        "examples": [
            {
                "jp": "その国の言葉ができないことは、おそらく大きなストレスになるに違いない。",
                "reading_note": "そのくにのことばができないことは、おそらくおおきなすとれすになるにちがいない。",
                "vi": "Việc không nói được ngôn ngữ nước đó hẳn là sẽ trở thành áp lực lớn.",
                "grammar_note": "Q#153: おそらく hô ứng chặt chẽ với になるに違いない.",
            },
            {
                "jp": "私の傘がない。誰かが間違えて持っていったに違いない。",
                "reading_note": "わたしのかさがない。だれかがまちがえてもっていったにちがいない。",
                "vi": "Ô của tôi biến mất rồi. Chắc chắn ai đó đã cầm nhầm mất rồi.",
                "grammar_note": "Suy đoán từ dấu hiệu thực tế dùng Vた + に違いない.",
            },
        ],
        "source_ref": "Shin-N3-List #81 | anki #33 | Đề .xlsx (Q153)",
        "search_keywords": "ni chigainai osoraku chac chan han la に違いない おそらく",
        "match_patterns": ["に違いない", "にちがいない"],
    },
    {
        "code": "GP-N3-066",
        "pattern": "～おそれがある (Có nguy cơ, e rằng sẽ xảy ra rủi ro)",
        "jlpt_level": "N3",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": True,
        "formation_formula": "Vる / N + の + おそれがある / おそれがあります",
        "formation_table": [
            {"pos": "Động từ (V)", "rule": "Vる + おそれがある (悪くなるおそれがあります, 建物が倒れるおそれがある)"},
            {"pos": "Danh từ (N)", "rule": "N(sự cố/rủi ro) + の + おそれがある (台風の発生・故障のおそれがある)"},
            {"pos": "Văn phong chuyên biệt", "rule": "Chuyên dùng trong y tế, hướng dẫn an toàn, dự báo thời tiết, thông cáo báo chí"},
        ],
        "core_meaning_vi": "Cảnh báo trang trọng về một nguy cơ, tác hại hoặc kết quả tiêu cực có khả năng xảy ra",
        "deep_explanation_vi": (
            "Thi trực tiếp ở Bài Đục lỗ 1 Câu [5] (Q#147: '以上のことに気をつけないと、症状が [悪くなるおそれがあります]'). "
            "Đây là mẫu văn viết/hướng dẫn chuẩn mực mà người học hay nhầm với ～にきまっている (suy đoán chủ quan). "
            "Lưu ý 2 điều: (1) Vế sau BẮT BUỘC là kết quả XẤU/NGUY HIỂM (triệu chứng nặng hơn, sập nhà, tai nạn, bão) — không bao giờ dùng cho việc tốt ('có nguy cơ trúng số'). (2) Trước おそれがある chỉ dùng Vる hoặc Nの (không dùng Vた)."
        ),
        "register_tag": "Trang trọng / Y khoa & Thời sự",
        "confusable_pairs": [
            {
                "rival_pattern": "～おそれがある vs ～にきまっている vs ～かもしれない",
                "difference_vi": "おそれがある = cảnh báo rủi ro tiêu cực mang tính trang trọng/khách quan; にきまっている = quả quyết cảm tính; かもしれない = trung tính (dùng được cho cả việc tốt lẫn xấu).",
                "quick_test_vi": "Thấy ngữ cảnh hướng dẫn sử dụng, y khoa, thiên tai và kết quả xấu -> chốt ngay おそれがある!",
            }
        ],
        "examples": [
            {
                "jp": "以上のことに気をつけないと、症状が悪くなるおそれがあります。",
                "reading_note": "いじょうのことにきをつけないと、しょうじょうがわるくなるおそれがあります。",
                "vi": "Nếu không chú ý những điều trên, triệu chứng có nguy cơ sẽ trở nên nặng hơn.",
                "grammar_note": "Q#147: Cảnh báo y khoa chuẩn xác dùng Vる + おそれがあります.",
            },
            {
                "jp": "大きな地震が起きたら、この古い建物は倒れるおそれがある。",
                "reading_note": "おおきなじしんがおきたら、このふるいたてものはたおれるおそれがある。",
                "vi": "Nếu động đất lớn xảy ra, tòa nhà cũ này có nguy cơ bị đổ sập.",
                "grammar_note": "Dự báo rủi ro thiên tai.",
            },
        ],
        "source_ref": "Shin-N3-List #82 | anki #35 | Đề .xlsx (Q147)",
        "search_keywords": "osore ga aru nguy co e rang y khoa bao chi おそれがある 恐れがある",
        "match_patterns": ["おそれがある", "おそれがあります", "恐れがある"],
    },
    {
        "code": "GP-N3-067",
        "pattern": "～にすぎない (Chỉ là... mà thôi - Coi nhẹ mức độ)",
        "jlpt_level": "N3",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": True,
        "formation_formula": "普通形(N/Aな bỏ だ) + にすぎない",
        "formation_table": [
            {"pos": "Danh từ (N)", "rule": "N + にすぎない (子どもにすぎない, 一つの方法にすぎない, うわさにすぎない)"},
            {"pos": "Động từ (V)", "rule": "Vる/Vた + にすぎない (手伝ったにすぎない, 見たにすぎない)"},
        ],
        "core_meaning_vi": "Nhấn mạnh sự việc/đối tượng chẳng qua chỉ ở mức nhỏ bé, đơn giản, không đáng kể hơn thế ('chỉ là... mà thôi')",
        "deep_explanation_vi": (
            "Xuất hiện làm phương án nhiễu ở Bài Đục lỗ 3 Câu [1] (Q#153: '大きなストレスになる [にすぎない]' bị loại vì tác giả muốn nhấn mạnh áp lực LỚN chứ không hề coi nhẹ nó!). "
            "～にすぎない thường đi kèm phó từ ただ ('chỉ đơn thuần là...')."
        ),
        "register_tag": "Văn viết & Nghị luận",
        "confusable_pairs": [
            {
                "rival_pattern": "～にすぎない vs ～に違いない",
                "difference_vi": "にすぎない hạ thấp tầm quan trọng ('chẳng qua chỉ là...'); に違いない nhấn mạnh phán đoán chắc chắn ('chắc chắn là...').",
                "quick_test_vi": "Thấy 'ただ' hoặc hàm ý phủ nhận tầm quan trọng -> にすぎない; thấy おそらく / chắc chắn -> に違いない.",
            }
        ],
        "examples": [
            {
                "jp": "それはただのうわさにすぎないから、信じる必要はない。",
                "reading_note": "それはただのうわさにすぎないから、しんじるひつようはない。",
                "vi": "Đó chẳng qua chỉ là lời đồn thôi nên không cần phải tin.",
                "grammar_note": "ただの + N + にすぎない hạ thấp mức độ tin đồn.",
            },
            {
                "jp": "私は自分の仕事をしたにすぎません。",
                "reading_note": "わたしはじぶんのしごとをしたにすぎません。",
                "vi": "Tôi chẳng qua chỉ làm phần việc của mình mà thôi.",
                "grammar_note": "Vた + にすぎません diễn tả sự khiêm tốn.",
            },
        ],
        "source_ref": "Shin-N3-List #83 | Đề .xlsx (Q153)",
        "search_keywords": "ni suginai chi la ma thoi にすぎない に過ぎない",
        "match_patterns": ["にすぎない", "にすぎません"],
    },
    {
        "code": "GP-N3-068",
        "pattern": "～ことか / ～ものか (Thật là... biết bao / Không đời nào!)",
        "jlpt_level": "N3",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": False,
        "formation_formula": "[どんなに/なんと] + 普通形(Aなな/Nな) + ことか (Biết bao) | 普通形(Aなな/Nな) + ものか (Không đời nào)",
        "formation_table": [
            {"pos": "1. ～ことか (Cảm thán mức độ cao)", "rule": "どんなに + A/V + ことか (どんなにうれしいことか = thật vui biết bao nhiêu!)"},
            {"pos": "2. ～ものか / もんか (Phủ nhận mạnh)", "rule": "Vる/Vた/A + ものか (こんな仕事が明日までに終わるものか = làm sao mà xong được!)"},
        ],
        "core_meaning_vi": "Bày tỏ cảm xúc dâng trào biết bao nhiêu (～ことか) hoặc phủ định mạnh mẽ không đời nào xảy ra (～ものか)",
        "deep_explanation_vi": (
            "Hai đuôi câu cảm thán này đối lập hoàn toàn về nghĩa nhưng hay bị nhầm khi đọc nhanh: "
            "～ことか luôn đứng với từ nghi vấn mức độ (どんなに, どれほど, 何回) để cảm thán 'biết bao nhiêu'. "
            "～ものか (khẩu ngữ もんか) mang nghĩa phản bác gay gắt 'làm gì có chuyện đó / không bao giờ có chuyện ấy đâu!'"
        ),
        "register_tag": "Văn viết cảm thán (ことか) & Khẩu ngữ (ものか)",
        "confusable_pairs": [
            {
                "rival_pattern": "～ことか vs ～ものか",
                "difference_vi": "ことか = cảm thán mức độ cao ('thật vui/vất vả biết bao'); ものか = phản đối, phủ định mạnh ('không đời nào làm/xảy ra đâu').",
                "quick_test_vi": "Có どんなに / どれほど -> ことか; giọng phản bác tức giận hoặc từ chối dứt khoát -> ものか.",
            }
        ],
        "examples": [
            {
                "jp": "N3に合格できたら、どんなにうれしいことか。",
                "reading_note": "えぬさんにごうかくできたら、どんなにうれしいことか。",
                "vi": "Nếu đỗ được N3 thì thật là vui biết bao nhiêu.",
                "grammar_note": "どんなに hô ứng với Aい + ことか.",
            },
            {
                "jp": "こんなにたくさんの仕事、今日中に終わるものか。",
                "reading_note": "こんなにたくさんのしごと、きょうじゅうにおわるものか。",
                "vi": "Nhiều việc thế này thì làm sao mà xong trong hôm nay được cơ chứ.",
                "grammar_note": "Phủ định hoàn toàn khả năng bằng Vる + ものか.",
            },
        ],
        "source_ref": "Shin-N3-List #84, #85",
        "search_keywords": "koto ka mono ka biet bao khong doi nao ことか ものか もんか",
        "match_patterns": ["ことか", "ものか", "もんか"],
    },
    {
        "code": "GP-N3-069",
        "pattern": "～としたら / ～とすれば (Giả sử nếu... thì)",
        "jlpt_level": "N3",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": False,
        "formation_formula": "普通形 + としたら / とすれば / とすると",
        "formation_table": [
            {"pos": "V / A / N", "rule": "普通形(N/Aな giữ だ) + としたら / とすれば (その話が本当だとしたら = giả sử chuyện đó là thật)"},
            {"pos": "Khác với ～たら", "rule": "としたら chuyên dùng cho giả thiết chưa xác thực hoặc giả định tưởng tượng ('giả sử điều chưa chắc kia là đúng thì...')"},
        ],
        "core_meaning_vi": "Đặt giả thiết chưa chắc chắn là sự thật để suy luận xem nếu đúng như vậy thì kết quả sẽ ra sao",
        "deep_explanation_vi": (
            "Khác với điều kiện たら thông thường dùng cho việc dự kiến sẽ làm ('nếu mai rảnh thì đi'), ～としたら / ～とすれば dùng để đặt giả thuyết logic hoặc giả định tình huống giả tưởng ('giả sử tin đồn kia là thật thì...', 'giả sử được chọn 1 điều ước thì...')."
        ),
        "register_tag": "Trung tính (Hội thoại & Nghị luận)",
        "confusable_pairs": [
            {
                "rival_pattern": "～としたら vs ～たら",
                "difference_vi": "たら dùng cho điều kiện tự nhiên có thật hoặc dự kiến; としたら nhấn mạnh 'giả sử ta tạm coi A là đúng/xảy ra' để bàn luận hệ quả.",
                "quick_test_vi": "Có từ giả định 'もしも / 仮に' hoặc '本当だ…' (giả sử đúng thì) -> としたら.",
            }
        ],
        "examples": [
            {
                "jp": "その話が本当だとしたら、とてもうれしいです。",
                "reading_note": "そのはなしがほんとうだとしたら、とてもうれしいです。",
                "vi": "Nếu giả sử câu chuyện đó là sự thật thì tôi rất vui.",
                "grammar_note": "N + だ + としたら đặt giả thiết chưa xác thực.",
            },
            {
                "jp": "来月から新しい制度が始まるとすれば、今から準備が必要だ。",
                "reading_note": "らいげつからあたらしいせいどがはじまるとすれば、いまからじゅんびがひつようだ。",
                "vi": "Giả sử từ tháng sau chế độ mới bắt đầu thì ngay từ bây giờ cần phải chuẩn bị.",
                "grammar_note": "Vる + とすれば để suy luận biện pháp.",
            },
        ],
        "source_ref": "Shin-N3-List #86",
        "search_keywords": "to shitara to sureba gia su neu thi としたら とすれば",
        "match_patterns": ["としたら", "とすれば"],
    },
    {
        "code": "GP-N3-070",
        "pattern": "～を通じて / ～を通して (Thông qua phương tiện / Suốt khoảng thời gian)",
        "jlpt_level": "N3",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": False,
        "formation_formula": "N + を通じて（をつうじて） / を通して（をとおして）",
        "formation_table": [
            {"pos": "1. Thông qua trung gian / cách thức", "rule": "N(người trung gian, phương tiện truyền thông, trải nghiệm) + を通じて / を通して (友だちを通じて知り合った)"},
            {"pos": "2. Suốt khoảng thời gian", "rule": "N(thời gian/mùa/năm) + を通じて / を通して (一年を通じて温暖だ = ấm áp suốt cả năm; giống Q#76 '1年中')"},
        ],
        "core_meaning_vi": "Thực hiện việc gì thông qua trung gian/phương tiện N, hoặc diễn ra liên tục xuyên suốt khoảng thời gian N",
        "deep_explanation_vi": (
            "Hai mẫu ～を通じて và ～を通して hầu như thay thế được cho nhau, nhưng nhớ 2 quy tắc giới hạn quan trọng: "
            "1) Khi chỉ trung gian: chỉ dùng cho NGƯỜI MÔI GIỚI, MẠNG XÃ HỘI, SÁCH BÁO, HOẠT ĐỘNG (スポーツを通して). Không dùng cho phương tiện giao thông vật lý như xe buýt/tàu điện (phải dùng で). "
            "2) Khi chỉ thời gian: danh từ đứng trước phải là chu kỳ trọn vẹn (一年, 季節, 四季, 生涯)."
        ),
        "register_tag": "Trung tính & Văn viết",
        "confusable_pairs": [
            {
                "rival_pattern": "～を通じて / ～を通して vs ～によって",
                "difference_vi": "を通じて nhấn mạnh CẦU NỐI trung gian (người giới thiệu, internet) hoặc SUỐT thời gian; によって là phương pháp trực tiếp hoặc tác nhân câu bị động.",
                "quick_test_vi": "Thấy 'qua bạn bè / qua internet / suốt cả năm (一年)' -> を通じて / を通して.",
            }
        ],
        "examples": [
            {
                "jp": "子どもたちはスポーツを通して、いろいろなことを学ぶことができる。",
                "reading_note": "こどもたちはすぽーつをとおして、いろいろなことをまなぶことができる。",
                "vi": "Thông qua thể thao, trẻ em có thể học được rất nhiều điều.",
                "grammar_note": "N(hoạt động trung gian) + を通して.",
            },
            {
                "jp": "この町は一年を通じて温暖な気候だ。",
                "reading_note": "このまちはいちねんをつうじておんだんなきこうだ。",
                "vi": "Thị trấn này khí hậu ôn hòa suốt cả một năm.",
                "grammar_note": "一年 + を通じて = trong suốt cả năm.",
            },
        ],
        "source_ref": "Shin-N3-List #87 | anki #19 | Đề .xlsx (Q76)",
        "search_keywords": "wo tsuujite wo tooshite thong qua suot khoang thoi gian を通じて を通して",
        "match_patterns": ["を通じて", "を通して"],
    },
    {
        "code": "GP-N3-071",
        "pattern": "～しかない / ～ほかはない (Không còn cách nào khác, đành phải)",
        "jlpt_level": "N3",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": False,
        "formation_formula": "Vる + しかない / ほかはない / ほか（は）しかたがない",
        "formation_table": [
            {"pos": "～しかない", "rule": "Vる + しかない (Khẩu ngữ & văn viết đều dùng: 新しいのを買うしかない)"},
            {"pos": "～ほかはない", "rule": "Vる + ほかはない (Trang trọng hơn しかない: 上司の命令なので従うほかはない)"},
        ],
        "core_meaning_vi": "Bày tỏ tâm trạng bất đắc dĩ vì mọi phương án khác đều bế tắc nên chỉ còn duy nhất một cách làm V",
        "deep_explanation_vi": (
            "Đây là dạng kết hợp của trợ từ giới hạn しか + ない với động từ thể từ điển Vる. "
            "Khác với ～なければならない (nghĩa vụ quy định), ～しかない mang cảm giác 'hết cách rồi, đành phải làm thế thôi'."
        ),
        "register_tag": "Trung tính (しかない) & Văn viết (ほかはない)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vる + しかない vs Vない + わけにはいかない",
                "difference_vi": "Vる+しかない nhấn mạnh hết lựa chọn thực tế ('hỏng rồi nên đành phải mua mới'); Vない+わけにはいかない nhấn mạnh áp lực trách nhiệm/đạo đức ('sếp giao nên không thể không làm').",
                "quick_test_vi": "Động từ đứng trước ở thể khẳng định Vる -> しかない / ほかはない; đứng trước ở thể phủ định Vない -> わけにはいかない.",
            }
        ],
        "examples": [
            {
                "jp": "パソコンが直せないから、新しいのを買うしかない。",
                "reading_note": "ぱそこんがなおせないから、あたらしいのをかうしかない。",
                "vi": "Không sửa được máy tính nên chẳng còn cách nào khác là phải mua cái mới.",
                "grammar_note": "Vる (買う) + しかない.",
            },
            {
                "jp": "電車が止まっているので、歩いて帰るほかはない。",
                "reading_note": "でんしゃがとまっているので、あるいてかえるほかはない。",
                "vi": "Vì tàu điện đang dừng hoạt động nên đành phải đi bộ về thôi.",
                "grammar_note": "Vる + ほかはない diễn tả giải pháp duy nhất còn lại.",
            },
        ],
        "source_ref": "Shin-N3-List #88",
        "search_keywords": "shika nai hoka wa nai danh phai khong con cach nao khac しかない ほかはない",
        "match_patterns": ["しかない", "ほかはない"],
    },
    {
        "code": "GP-N3-072",
        "pattern": "～をこめて (Gửi gắm tất cả tình cảm, tấm lòng vào...)",
        "jlpt_level": "N3",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": False,
        "formation_formula": "N(tình cảm / tâm ý: 愛・感謝・願い・心) + をこめて / をこめた + N",
        "formation_table": [
            {"pos": "Bổ nghĩa động từ", "rule": "感謝の気持ちをこめて (với tất cả lòng biết ơn), 平和への願いをこめて"},
            {"pos": "Bổ nghĩa danh từ", "rule": "N1 + をこめた + N2 (愛情をこめた料理 = món ăn chứa đựng tình yêu thương)"},
        ],
        "core_meaning_vi": "Đặt, gửi gắm trọn vẹn cảm xúc hoặc tâm nguyện vào một hành động, lời nói hay tác phẩm",
        "deep_explanation_vi": (
            "Danh từ đứng trước をこめて BẮT BUỘC phải là danh từ chỉ tình cảm, tâm ý, lời chúc tốt đẹp (愛, 感謝, 心を, 願い, 祈り). "
            "Không dùng cho vật chất cụ thể."
        ),
        "register_tag": "Trung tính (Trang trọng & Tình cảm)",
        "confusable_pairs": [
            {
                "rival_pattern": "N(tình cảm) + をこめて vs N + を通じて",
                "difference_vi": "をこめて = dồn hết tâm tình bên trong vào hành động/món quà; を通じて = thông qua phương tiện trung gian.",
                "quick_test_vi": "Thấy danh từ chỉ cảm xúc/tâm niệm (感謝, 愛, 願い, 心) đi kèm động từ làm quà/viết/hát -> をこめて.",
            }
        ],
        "examples": [
            {
                "jp": "平和への願いをこめて、この歌を作りました。",
                "reading_note": "へいわへのねがいをこめて、このうたをつくりました。",
                "vi": "Tôi đã sáng tác bài hát này với tất cả ước nguyện về hòa bình gửi gắm trong đó.",
                "grammar_note": "願い + をこめて + 作った.",
            },
            {
                "jp": "両親への感謝の気持ちをこめて、プレゼントを贈った。",
                "reading_note": "りょうしんへのかんしゃのきもちをこめて、ぷれぜんとをおくった。",
                "vi": "Tôi đã tặng món quà gửi gắm trọn vẹn lòng biết ơn tới bố mẹ.",
                "grammar_note": "感謝の気持ち + をこめて.",
            },
        ],
        "source_ref": "Shin-N3-List #89",
        "search_keywords": "wo komete gui gam tinh cam tam long をこめて を込めて",
        "match_patterns": ["をこめて", "を込めて", "をこめた"],
    },
    {
        "code": "GP-N3-073",
        "pattern": "～っぱなし (Cứ để nguyên trạng thái V không dọn/không xử lý)",
        "jlpt_level": "N3",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": True,
        "formation_formula": "Vます(bỏ ます) + っぱなしだ / っぱなしにする",
        "formation_table": [
            {"pos": "Động từ hành động", "rule": "Vます + っぱなし (テレビをつけっぱなし, 窓を開けっぱなし, 出しっぱなし)"},
            {"pos": "Sắc thái ngữ dụng", "rule": "Luôn mang ý CHÊ TRÁCH sự cẩu thả, quên làm bước thu dọn/tắt tiếp theo"},
        ],
        "core_meaning_vi": "Để nguyên kết quả hành động V kéo dài như vậy mà không làm động tác khắc phục tiếp theo (tắt, đóng, cất)",
        "deep_explanation_vi": (
            "Mẫu này xuất hiện làm phương án nhiễu trong Q#51 ('[炊きたて] のごはん' với bẫy '炊きっぱなし'). "
            "Hai lý do giúp nhận diện ngay lập tức: "
            "1) っぱなし luôn mang nghĩa chê trách sự lơ đãng (bật TV rồi ngủ quên, mở cửa không đóng, bật nước chảy tràn). Không bao giờ dùng để khen cơm ngon nóng hổi như trong Q#51! "
            "2) Khi bổ nghĩa cho danh từ hoặc làm trạng ngữ hay dùng っぱなしの + N hoặc っぱなしで + V."
        ),
        "register_tag": "Khẩu ngữ (Phàn nàn / Chê trách)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vます + っぱなし vs Vます + たて vs Vて + ある",
                "difference_vi": "っぱなし = bỏ mặc nguyên đó gây khó chịu (tiêu cực); たて = vừa mới làm xong nóng hổi (tích cực); てある = cố ý đặt/mở sẵn có mục đích.",
                "quick_test_vi": "Ngữ cảnh chê cẩu thả (quên tắt đèn, vứt đồ bừa bãi) -> っぱなし; ngữ cảnh khen đồ ăn mới nấu/mới nướng (Q#51) -> たて.",
            }
        ],
        "examples": [
            {
                "jp": "テレビをつけっぱなしで寝てしまった。",
                "reading_note": "てれびをつけっぱなしでねてしまった。",
                "vi": "Tôi để tivi bật nguyên như vậy rồi ngủ thiếp đi mất.",
                "grammar_note": "つける -> つけ + っぱなしで.",
            },
            {
                "jp": "使った道具は出しっぱなしにしないで、片付けてください。",
                "reading_note": "つかったどうぐはだしっぱなしにしないで、かたづけてください。",
                "vi": "Dụng cụ dùng xong đừng để bày nguyên ra đấy, hãy dọn lại đi.",
                "grammar_note": "出しっぱなしにする = để bừa không cất.",
            },
        ],
        "source_ref": "Shin-N3-List #90 | anki #32 | Đề .xlsx (Q51)",
        "search_keywords": "ppanashi de nguyen khong thu don cau tha っぱなし 炊きっぱなし",
        "match_patterns": ["っぱなし"],
    },
    {
        "code": "GP-N3-074",
        "pattern": "～きり / ～っきり (Kể từ khi... thì không còn xảy ra nữa / Chỉ có...)",
        "jlpt_level": "N3",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": False,
        "formation_formula": "Vた + きり / っきり (Kể từ lúc đó bặt vô âm tín) | N / Số từ + きり / っきり (Chỉ có chừng ấy)",
        "formation_table": [
            {"pos": "1. Vた + きり (Bặt tin / Không đổi)", "rule": "Kể từ khi làm V lần đó cho tới nay vẫn chưa quay lại / chưa làm tiếp (行ったきり戻ってこない, 会ったきり会っていない)"},
            {"pos": "2. N / Số từ + きり / っきり (Chỉ có)", "rule": "Giới hạn số lượng 'chỉ có từng này' (2人っきり, これっきり)"},
        ],
        "core_meaning_vi": "Kể từ mốc hành động V ở quá khứ đến nay vẫn giữ nguyên trạng thái không đổi (Vたきり), hoặc giới hạn chỉ có bấy nhiêu (Nきり)",
        "deep_explanation_vi": (
            "～きり có hai nghĩa tách bạch theo từ loại đứng trước: "
            "Nếu đứng trước là Vた (行ったきり, 別れたきり) -> 'kể từ lần đó đến nay chưa từng làm lại / chưa thấy về', vế sau hầu như luôn mang nghĩa phủ định tiếp diễn (～ない, ～ていない). "
            "Nếu đứng trước là Danh từ/Số từ (2人っきり, 一度きり) -> 'chỉ có 2 người / chỉ duy nhất 1 lần'."
        ),
        "register_tag": "Trung tính (Hội thoại & Kể chuyện)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vた + きり vs Vて + から",
                "difference_vi": "Vてから = sau khi làm V1 thì làm tiếp V2 (tiếp nối); Vたきり = kể từ khi làm V1 thì CHẤM DỨT luôn đến giờ chưa hề có bước tiếp theo (ngừng trệ).",
                "quick_test_vi": "Thấy vế sau là まだ～ていない (vẫn chưa quay lại / vẫn chưa gặp lại) -> Vたきり.",
            }
        ],
        "examples": [
            {
                "jp": "ひろしは本屋へ行ったきり、まだ戻ってこない。",
                "reading_note": "ひろしはほんやへいったきり、まだもどってこない。",
                "vi": "Hiroshi kể từ lúc đi hiệu sách tới giờ vẫn chưa thấy quay về.",
                "grammar_note": "Vた (行った) + きり + phủ định hiện tại.",
            },
            {
                "jp": "今日は2人っきりでゆっくり話したいです。",
                "reading_note": "きょうはふたりっきりでゆっくりはなしたいです。",
                "vi": "Hôm nay tôi muốn chỉ có hai người nói chuyện thong thả với nhau.",
                "grammar_note": "Số từ 2人 + っきり = chỉ riêng 2 người.",
            },
        ],
        "source_ref": "Shin-N3-List #91, #92",
        "search_keywords": "kiri kkiri ke tu khi chi co きり っきり",
        "match_patterns": ["たきり", "っきり"],
    },
    {
        "code": "GP-N3-075",
        "pattern": "～ふりをする (Giả vờ như là...)",
        "jlpt_level": "N3",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": False,
        "formation_formula": "V普通形 / Aい / Aな+な / N+の + ふりをする",
        "formation_table": [
            {"pos": "Động từ (V)", "rule": "Vる / Vた / Vている / Vない + ふりをする (知らないふりをする, 寝ているふりをする, 聞こえないふり)"},
            {"pos": "Tính từ / Danh từ", "rule": "Aい + ふりをする; Aな + な + ふりをする; N + の + ふりをする (金持ちのふりをする)"},
        ],
        "core_meaning_vi": "Cố tình làm ra vẻ, giả bộ bên ngoài như đang ở trạng thái đó dù bên trong sự thật hoàn toàn ngược lại",
        "deep_explanation_vi": (
            "Khác với ～ようだ / ～みたいだ (trông có vẻ tự nhiên hoặc suy đoán khách quan), ～ふりをする là HÀNH ĐỘNG CÓ CHỦ Ý đánh lừa người nhìn. "
            "Lưu ý quy tắc nối: Aな thêm な, Danh từ thêm の trước ふりをする."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "～ふりをする vs ～みたいだ",
                "difference_vi": "ふりをする = chủ động giả bộ (biết mà giả vờ không biết); みたいだ = trông có vẻ như vậy (người nói quan sát nhận xét).",
                "quick_test_vi": "Có từ trái nghĩa ở vế đối lập ('dù biết rõ nhưng vẫn làm bộ không biết') -> ふりをする.",
            }
        ],
        "examples": [
            {
                "jp": "彼女は私の声が聞こえないふりをした。",
                "reading_note": "かのじょはわたしのこえがきこえないふりをした。",
                "vi": "Cô ấy đã giả vờ như không nghe thấy tiếng tôi.",
                "grammar_note": "Vない (聞こえない) + ふりをする.",
            },
            {
                "jp": "彼は本当はわかっていないのに、わかっているふりをしている。",
                "reading_note": "かれはほんとうはわかっていないのに、わかっているふりをしている。",
                "vi": "Anh ta thực ra chẳng hiểu gì nhưng cứ giả vờ như đang hiểu rõ lắm.",
                "grammar_note": "Vている + ふりをしている.",
            },
        ],
        "source_ref": "Shin-N3-List #93 | anki #31",
        "search_keywords": "furi wo suru gia vo lam bo ふりをする",
        "match_patterns": ["ふりをする", "ふりをした", "ふりをしている"],
    },
    {
        "code": "GP-N3-076",
        "pattern": "～くせに (Mặc dù... vậy mà - Sắc thái chê trách, bực mình)",
        "jlpt_level": "N3",
        "category": "contrast_concession",
        "category_label_vi": CATEGORY_LABELS["contrast_concession"],
        "in_exam_corpus": False,
        "formation_formula": "V普通形 / Aい / Aな+な / N+の + くせに",
        "formation_table": [
            {"pos": "Động từ / Tính từ い", "rule": "普通形 + くせに (知っているくせに, できないくせに)"},
            {"pos": "Tính từ な / Danh từ", "rule": "Aな + な + くせに; N + の + くせに (子どものくせに)"},
            {"pos": "Quy tắc ngữ dụng bắt buộc", "rule": "CHỈ dùng để chê trách người khác (hoặc tự trách) khi hành động trái ngược thái quá; CẤM dùng cho bề trên hoặc sự kiện tự nhiên vô tri"},
        ],
        "core_meaning_vi": "Mặc dù ở tư cách/tình trạng A thế mà lại làm B trái khoáy (mang hàm ý trách móc, coi thường, bực tức)",
        "deep_explanation_vi": (
            "Khác với ～のに (bày tỏ sự ngạc nhiên/tiếc nuối chung cho cả người, vật, thời tiết), ～くせに mang cảm xúc CHỈ TRÍCH gay gắt nhắm vào CON NGƯỜI. "
            "Tuyệt đối không dùng cho thời tiết (*いい天気のくせに là sai ngữ pháp) và không dùng với người bề trên khi giao tiếp lịch sự."
        ),
        "register_tag": "Khẩu ngữ (Chê trách / Bất mãn)",
        "confusable_pairs": [
            {
                "rival_pattern": "～くせに vs ～のに vs ～ものの",
                "difference_vi": "くせに = chê trách hành vi mâu thuẫn của người; のに = tiếc nuối/bất ngờ trung tính (dùng cho cả thời tiết/vật); ものの = văn viết trang trọng ('tuy... nhưng').",
                "quick_test_vi": "Chủ ngữ là người + giọng chê trách ('biết mà chẳng chịu chỉ / con nít mà bày đặt...') -> くせに.",
            }
        ],
        "examples": [
            {
                "jp": "知っているくせに、教えてくれなかった。",
                "reading_note": "しっているくせに、おしえてくれなかった。",
                "vi": "Rõ ràng là biết vậy mà anh ta chẳng chịu chỉ cho tôi.",
                "grammar_note": "Vている + くせに bày tỏ sự bất mãn.",
            },
            {
                "jp": "自分でやる気もないくせに、人の文句ばかり言っている。",
                "reading_note": "じぶんでやるきもないくせに、ひとのもんくばかりいっている。",
                "vi": "Bản thân chẳng có chí làm việc vậy mà suốt ngày chỉ biết càm ràm người khác.",
                "grammar_note": "Chê trách thái độ mâu thuẫn của đối tượng.",
            },
        ],
        "source_ref": "Shin-N3-List #94",
        "search_keywords": "kuse ni mac du vay ma che trach くせに",
        "match_patterns": ["くせに"],
    },
    {
        "code": "GP-N3-077",
        "pattern": "～はもちろん (N1 là đương nhiên rồi, mà cả N2 cũng...)",
        "jlpt_level": "N3",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": True,
        "formation_formula": "N1 + はもちろん（のこと）、N2 + も",
        "formation_table": [
            {"pos": "Danh từ (N1, N2)", "rule": "N1 + はもちろん、N2 + も (英語はもちろん、フランス語も話せる)"},
            {"pos": "Khi đứng một mình (Q#146)", "rule": "もちろん = Tất nhiên rồi (điều hiển nhiên ai cũng biết; khác たとえば = ví dụ minh họa)"},
        ],
        "core_meaning_vi": "Khẳng định N1 là điều hiển nhiên khỏi phải bàn, không những thế cả N2 mở rộng hơn cũng tương tự",
        "deep_explanation_vi": (
            "～はもちろん gần nghĩa với ～だけでなく nhưng N1 luôn là cấp độ cơ bản/hiển nhiên nhất. "
            "Lưu ý もちろん còn đứng độc lập ở đầu câu hoặc đầu hội thoại với nghĩa 'tất nhiên rồi' (xuất hiện làm phương án nhiễu ở Q#146 đối chiếu với たとえば)."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "N1はもちろんN2も vs N1ばかりでなくN2も",
                "difference_vi": "もちろん nhấn mạnh N1 là điều HIỂN NHIÊN ai cũng biết trước tiên rồi mở rộng sang N2; ばかりでなく đơn thuần liệt kê mở rộng 'không chỉ N1 mà còn N2'.",
                "quick_test_vi": "Nếu đứng giữa câu nối 2 danh từ kèm も ở cuối -> はもちろん; nếu đầu câu đưa ví dụ con số cụ thể (Q#146) -> たとえば (loại もちろん).",
            }
        ],
        "examples": [
            {
                "jp": "彼は英語はもちろん、フランス語も話せる。",
                "reading_note": "かれはえいごはもちろん、ふらんすごもはなせる。",
                "vi": "Anh ấy nói được tiếng Anh là đương nhiên rồi, mà tiếng Pháp cũng nói được.",
                "grammar_note": "N1 + はもちろん + N2 + も.",
            },
            {
                "jp": "日本語の勉強では、文法はもちろん、語彙力も大切だ。",
                "reading_note": "にほんごのべんきょうでは、ぶんぽうはもちろん、ごいりょくもたいせつだ。",
                "vi": "Trong việc học tiếng Nhật, ngữ pháp là tất nhiên rồi, nhưng vốn từ vựng cũng rất quan trọng.",
                "grammar_note": "Mở rộng từ yếu tố hiển nhiên sang yếu tố thứ 2.",
            },
        ],
        "source_ref": "Shin-N3-List #95 | Đề .xlsx (Q146)",
        "search_keywords": "wa mochiron la duong nhien ma con はもちろん もちろん",
        "match_patterns": ["はもちろん"],
    },
    {
        "code": "GP-N3-078",
        "pattern": "Vます + 始める / 終わる / 続ける (Bắt đầu / Kết thúc / Tiếp tục)",
        "jlpt_level": "N3",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": True,
        "formation_formula": "Vます(bỏ ます) + 始める / 終わる / 続ける",
        "formation_table": [
            {"pos": "Vます + 始める", "rule": "Bắt đầu hành động có quá trình (使われ始めている, 勉強し始める)"},
            {"pos": "Vます + 終わる", "rule": "Làm xong/kết thúc hoàn toàn một khối lượng việc (読み終わる, 書き終わる)"},
            {"pos": "Vます + 続ける", "rule": "Tiếp tục làm liên tục không ngừng nghỉ (聞き続ける, 努力し続ける)"},
        ],
        "core_meaning_vi": "Biểu thị 3 giai đoạn vận động của hành động ghép vào gốc Vます: bắt đầu (始める), hoàn tất (終わる) và duy trì liên tục (続ける)",
        "deep_explanation_vi": (
            "Động từ ghép với Vます xuất hiện liên tục trong đề thi: Passage 3 ('聞き続けると'), Passage 18 ('使われ始めています'), Passage 19 ('努力し続けたら'), và làm nhiễu ở Q#55 ('毎日寝て [続けている]' bị loại vì động từ ghép phải gắn sau Vます bỏ ます -> 寝続けている, không gắn sau Vて '寝て'!). "
            "Đây là bài kiểm tra kép cả nghĩa lẫn hình thái chia Vます."
        ),
        "register_tag": "Trung tính",
        "confusable_pairs": [
            {
                "rival_pattern": "Vます + 続ける vs Vて + ばかりいる vs Vます + 出す",
                "difference_vi": "Vます+続ける gắn sau gốc Vます (không bao giờ gắn sau Vて như Q#55!); Vます+始める bắt đầu có quá trình/xu hướng; Vます+出す bắt đầu đột ngột.",
                "quick_test_vi": "Thấy động từ chia thể て đứng trước chỗ trống (寝て___ trong Q#55)? Loại ngay 続けている!",
            }
        ],
        "examples": [
            {
                "jp": "最近は新しく「緑のカーテン」というものが使われ始めている。",
                "reading_note": "さいきんはあたらしく「みどりのかーてん」というものがつかわれはじめている。",
                "vi": "Gần đây một thứ mới gọi là 'rèm xanh' đang bắt đầu được sử dụng.",
                "grammar_note": "Passage 18: Thể bị động 使われる bỏ る thành 使われ + 始めている.",
            },
            {
                "jp": "長時間大きな音を聞き続けると、小さい音が聞こえにくくなる。",
                "reading_note": "ちょうじかんおおきなおとをききつづけると、ちいさいおとがきこえにくくなる。",
                "vi": "Nếu tiếp tục nghe âm thanh lớn trong thời gian dài thì sẽ khó nghe âm nhỏ.",
                "grammar_note": "Passage 3: 聞く -> 聞き + 続ける.",
            },
        ],
        "source_ref": "Shin-N3-List #97 | Đề .xlsx (Q55, Passages 3, 18, 19)",
        "search_keywords": "hajimeru owaru tsuzukeru bat dau ket thuc tiep tuc 始める 終わる 続ける",
        "match_patterns": ["始め", "続け", "終わ"],
    },
    {
        "code": "GP-N3-079",
        "pattern": "～て初めて (Kể từ khi làm V thì lần đầu mới nhận ra / mới xảy ra)",
        "jlpt_level": "N3",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": False,
        "formation_formula": "Vて + 初めて（はじめて） + [Nhận thức mới / Thay đổi mới]",
        "formation_table": [
            {"pos": "Động từ (V)", "rule": "Vて + 初めて (一人暮らしをして初めて, 病気になって初めて)"},
            {"pos": "Vế sau đặc trưng", "rule": "Động từ nhận thức, hiểu ra giá trị (わかった, 気がついた, 実感した)"},
        ],
        "core_meaning_vi": "Chỉ sau khi trực tiếp trải qua sự việc A thì lúc đó mới lần đầu tiên thấu hiểu hoặc nhận ra giá trị B",
        "deep_explanation_vi": (
            "Đừng nhầm với trạng từ '初めて' đứng một mình (= lần đầu tiên làm gì: 初めて日本へ来た). "
            "Khi đặt ngay sau Vて thành [Vて + 初めて], nó mang nghĩa 'chỉ đến khi trải qua A rồi mới nhận ra/mới làm được B' (sống một mình rồi mới hiểu công ơn bố mẹ, ốm rồi mới biết sức khỏe quý giá)."
        ),
        "register_tag": "Trung tính (Suy ngẫm & Trải nghiệm)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vて + 初めて vs Vて + からでないと",
                "difference_vi": "Vて初めて kể lại trải nghiệm đã qua giúp mình vỡ lẽ ra điều gì; Vてからでないと đặt điều kiện bắt buộc cho tương lai ('nếu chưa làm V1 thì chưa làm được V2').",
                "quick_test_vi": "Thấy thì quá khứ nhận ra giá trị (わかった, 大切さを知った) -> Vて初めて.",
            }
        ],
        "examples": [
            {
                "jp": "一人暮らしをして初めて、家族の大切さがわかってきた。",
                "reading_note": "ひとりぐらしをしてはじめて、かぞくのたいせつさがわかってきた。",
                "vi": "Chỉ đến khi sống tự lập một mình, tôi mới bắt đầu hiểu ra tầm quan trọng của gia đình.",
                "grammar_note": "Vて + 初めて nối với nhận thức わかってきた.",
            },
            {
                "jp": "実際に失敗してみて初めて、準備の重要性に気がついた。",
                "reading_note": "じっさいにしっぱいしてみてはじめて、じゅんびのじゅうようせいにきがついた。",
                "vi": "Chỉ sau khi tự mình thất bại thử một lần mới nhận ra tầm quan trọng của việc chuẩn bị.",
                "grammar_note": "Trải nghiệm thực tế dẫn đến sự thức tỉnh.",
            },
        ],
        "source_ref": "Shin-N3-List #98",
        "search_keywords": "te hajimete ke tu khi moi nhan ra て初めて",
        "match_patterns": ["て初めて"],
    },
    {
        "code": "GP-N3-080",
        "pattern": "～をはじめ（として） (Trước tiên phải kể đến là...)",
        "jlpt_level": "N3",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": False,
        "formation_formula": "N1(ví dụ tiêu biểu hàng đầu) + をはじめ（として）、N2(tập hợp rộng hơn)",
        "formation_table": [
            {"pos": "Chức năng ngữ pháp", "rule": "Đưa N1 làm đại diện nổi bật nhất đứng đầu một nhóm đông đảo (富士山をはじめ、多くの名山)"},
            {"pos": "Bổ nghĩa danh từ", "rule": "N1 + をはじめとする + N2 (東京をはじめとする大都市)"},
        ],
        "core_meaning_vi": "Lấy N1 làm ví dụ tiêu biểu, nổi bật nhất đứng đầu để đại diện cho cả một tập hợp nhiều đối tượng cùng loại",
        "deep_explanation_vi": (
            "N1 đứng trước ～をはじめ BẮT BUỘC phải là ví dụ ĐẠI DIỆN HÀNG ĐẦU/TIÊU BIỂU NHẤT của nhóm (ví dụ nói về núi ở Nhật thì chọn Phú Sĩ, nói về thành phố lớn chọn Tokyo). "
            "Khác với ～といった (chỉ liệt kê 2-3 ví dụ bình đẳng), ～をはじめ chỉ lấy 1 đại diện số 1 rồi mở rộng ra số nhiều phía sau."
        ),
        "register_tag": "Văn viết & Phát biểu trang trọng",
        "confusable_pairs": [
            {
                "rival_pattern": "N1をはじめ vs N1やN2といった",
                "difference_vi": "をはじめ lấy 1 đại diện tiêu biểu nhất làm đầu tàu; といった liệt kê vài ví dụ ngang hàng nhau.",
                "quick_test_vi": "Chỉ có 1 danh từ nổi tiếng nhất đứng trước chỗ trống + phía sau có '多くの～ / さまざまな～' -> をはじめ.",
            }
        ],
        "examples": [
            {
                "jp": "日本には富士山をはじめ、多くの美しい山がある。",
                "reading_note": "にほんにはふじさんをはじめ、おおくのうつくしいやまがある。",
                "vi": "Ở Nhật Bản có rất nhiều ngọn núi đẹp, trước hết phải kể đến núi Phú Sĩ.",
                "grammar_note": "富士山 là ví dụ đại diện số 1 cho nhóm 美しい山.",
            },
            {
                "jp": "社長をはじめ、社員全員が新しい計画に賛成した。",
                "reading_note": "しゃちょうをはじめ、しゃいんぜんいんがあたらしいけいかくにさんせいした。",
                "vi": "Trước hết là giám đốc và toàn thể nhân viên đều tán thành kế hoạch mới.",
                "grammar_note": "社長 đứng đầu đại diện cho tập thể nhân viên.",
            },
        ],
        "source_ref": "Shin-N3-List #99 | anki #22",
        "search_keywords": "wo hajime to shite truoc tien phai ke den la をはじめ をはじめとする",
        "match_patterns": ["をはじめ", "をはじめとして", "をはじめとする"],
    },
])

# =========================================================================
# JLPT N3 CORE PART 3 & EXAM CORPUS SPECIALS (GP-N3-081 .. GP-N3-118)
# =========================================================================
GRAMMAR_POINTS_DATA.extend([
    {
        "code": "GP-N3-081",
        "pattern": "Vます + かけ（だ・の） (Đang làm dở dang chưa xong)",
        "jlpt_level": "N3",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": True,
        "formation_formula": "Vます(bỏ ます) + かけだ / かけている / かけの + N",
        "formation_table": [
            {"pos": "Bổ nghĩa danh từ", "rule": "Vます + かけ + の + N (読みかけの本, 食べかけのケーキ, 炊きかけのごはん)"},
            {"pos": "Vị ngữ", "rule": "Vます + かけだ / かけている (nói dở, làm dở dang giữa chừng)"},
        ],
        "core_meaning_vi": "Diễn tả hành động mới làm được một nửa hoặc đang dở dang giữa chừng thì dừng lại",
        "deep_explanation_vi": (
            "Mẫu này là một trong 4 phương án bẫy kinh điển ở Q#51 ('[炊きたて] のごはん' với nhiễu '炊きかけ'). "
            "Khi bổ nghĩa cho danh từ qua の, 炊きかけのごはん = cơm đang nấu dở (chưa chín!), hoàn toàn trái nghĩa với 炊きたてのごはん = cơm vừa mới nấu chín xong nóng hổi!"
        ),
        "register_tag": "Trung tính (Hội thoại & Miêu tả)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vます + かけ + の + N vs Vます + たて + の + N",
                "difference_vi": "かけ = đang làm dở dang chưa hoàn thành; たて = vừa mới hoàn thành xong còn tươi/nóng hổi.",
                "quick_test_vi": "Ngữ cảnh sách đọc dở/cà phê uống dở -> かけ; bánh mới nướng/cơm mới nấu (Q#51) -> たて.",
            }
        ],
        "examples": [
            {
                "jp": "これは私が読みかけの本です。",
                "reading_note": "これはわたしがよみかけのほんです。",
                "vi": "Đây là cuốn sách tôi đang đọc dở.",
                "grammar_note": "読む -> 読み + かけ + の + 本.",
            },
            {
                "jp": "食べかけのりんごがテーブルの上に置いてある。",
                "reading_note": "たべかけのりんごがてーぶるのうえにおいてある。",
                "vi": "Quả táo đang ăn dở đang được đặt trên bàn.",
                "grammar_note": "Vます + かけ của động từ ăn uống.",
            },
        ],
        "source_ref": "Shin-N3-List #100 | Đề .xlsx (Q51)",
        "search_keywords": "kake dang do dang Vますかけ かけの 炊きかけ",
        "match_patterns": ["かけの", "かけだ", "かけている", "炊きかけ"],
    },
    {
        "code": "GP-N3-082",
        "pattern": "Vます + たて（だ・の） (Vừa mới làm xong, còn tươi/nóng hổi)",
        "jlpt_level": "N3",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": True,
        "formation_formula": "Vます(bỏ ます) + たて + の + N / たてだ",
        "formation_table": [
            {"pos": "Bổ nghĩa danh từ", "rule": "Vます + たて + の + N (炊きたてのごはん, 焼きたてのパン, できたての料理)"},
            {"pos": "Giới hạn kết hợp", "rule": "Dùng cho đồ ăn mới chế biến, sản phẩm mới ra lò, đồ mới sơn/làm xong còn giữ nguyên trạng thái mới mẻ"},
        ],
        "core_meaning_vi": "Vừa mới hoàn thành xong tức thì nên vẫn giữ nguyên độ tươi mới, nóng hổi (sắc thái tích cực)",
        "deep_explanation_vi": (
            "Thi trực tiếp ở Q#51 ('母はいつも、家族には [炊きたて] のごはんを食べてもらいたいと言っている'). "
            "Khác với Vたばかり (dùng được cho mọi hành động như vừa mới đến, vừa mới cưới), Vます+たて CHỈ đi với hành động tạo ra/chế biến ra một vật phẩm mới (nấu cơm 炊きたて, nướng bánh 焼きたて, hái quả とれたて, mới tốt nghiệp 卒業したて)."
        ),
        "register_tag": "Trung tính (Tích cực)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vます + たて vs Vます + かけ vs Vます + っぱなし",
                "difference_vi": "たて = vừa làm xong ngon/mới (tích cực); かけ = đang làm dở chưa xong; っぱなし = làm xong bỏ mặc không dọn (tiêu cực).",
                "quick_test_vi": "Trước 'のごはん' hoặc 'のパン' với nghĩa ngon nóng hổi (Q#51) -> chốt ngay たて!",
            }
        ],
        "examples": [
            {
                "jp": "母はいつも、家族には炊きたてのごはんを食べてもらいたいと言っている。",
                "reading_note": "はははいつも、かぞくにはたきたてのごはんをたべてもらいたいといっている。",
                "vi": "Mẹ tôi lúc nào cũng nói muốn cho gia đình ăn cơm vừa mới nấu xong.",
                "grammar_note": "Q#51: 炊く -> 炊き + たて + の + ごはん.",
            },
            {
                "jp": "このパン屋さんの焼きたてのパンはとてもおいしい。",
                "reading_note": "このぱんやさんのやきたてのぱんはとてもおいしい。",
                "vi": "Bánh mì mới nướng xong của tiệm bánh này rất ngon.",
                "grammar_note": "焼く -> 焼き + たて + の + パン.",
            },
        ],
        "source_ref": "Shin-N3-List #101 | Đề .xlsx (Q51)",
        "search_keywords": "tate vua moi xong nong hoi Vますたて 炊きたて 焼きたて",
        "match_patterns": ["たての", "たてだ", "炊きたて"],
    },
    {
        "code": "GP-N3-083",
        "pattern": "Vます + 上がる / 上げる (Hoàn thành xong xuôi một sản phẩm)",
        "jlpt_level": "N3",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": True,
        "formation_formula": "Vます(bỏ ます) + 上がる(tự động từ: が) / 上げる(tha động từ: を)",
        "formation_table": [
            {"pos": "Tự động từ (が + V上がる)", "rule": "Món ăn, tác phẩm tự hoàn thành xong xuôi (出来上がる, 焼き上がる)"},
            {"pos": "Tha động từ (を + V上げる)", "rule": "Người hoàn thành xong sản phẩm/báo cáo (書き上げる, 作り上げる)"},
        ],
        "core_meaning_vi": "Diễn tả việc chế tạo, nấu nướng hoặc viết lách đạt đến bước hoàn thiện cuối cùng",
        "deep_explanation_vi": (
            "Gặp trực tiếp ở Q#138 ('料理が [できあがった] ので、食べてください'). "
            "Nhớ phân biệt cặp tự/tha động từ ngay ở đuôi ghép: 上がる đi với trợ từ chủ ngữ が (món ăn đã nấu xong: 料理が出来上がる), còn 上げる đi với tân ngữ を (tôi viết xong báo cáo: レポートを書き上げる)."
        ),
        "register_tag": "Trung tính",
        "confusable_pairs": [
            {
                "rival_pattern": "Vます + 上がる (が) vs Vます + 上げる (を)",
                "difference_vi": "上がる là tự động từ (báo hiệu chủ thể đã hoàn tất với が); 上げる là tha động từ (báo hiệu người nói làm xong vật gì với を).",
                "quick_test_vi": "Thấy 料理が / 建物が (Q#138) -> 出来上がる; thấy レポートを -> 書き上げる.",
            }
        ],
        "examples": [
            {
                "jp": "料理ができあがったので、食べてください。",
                "reading_note": "りょうりができあがったので、たべてください。",
                "vi": "Món ăn đã làm xong xuôi rồi, mời bạn ăn nhé.",
                "grammar_note": "Q#138: 出来る + 上がる đi với chủ ngữ 料理が.",
            },
            {
                "jp": "やっとレポートを書き上げた。",
                "reading_note": "やっとれぽーとをかきあげた。",
                "vi": "Cuối cùng thì tôi cũng đã viết xong xuôi bản báo cáo.",
                "grammar_note": "Tân ngữ レポートを đi với tha động từ 書き上げる.",
            },
        ],
        "source_ref": "Shin-N3-List #101b | Đề .xlsx (Q138)",
        "search_keywords": "agaru ageru hoan thanh xong xuoi 上がる 上げる 出来上がる できあがった",
        "match_patterns": ["できあが", "出来上が", "書き上"],
    },
    {
        "code": "GP-N3-084",
        "pattern": "Vます + きる / きれない (Làm hết sạch triệt để / Không làm xuể)",
        "jlpt_level": "N3",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": False,
        "formation_formula": "Vます(bỏ ます) + きる / きれる / きれない",
        "formation_table": [
            {"pos": "1. Làm triệt để / đến tận cùng", "rule": "Vます + きる (疲れきる = mệt rã rời kiệt sức, 信じきる = tin tuyệt đối)"},
            {"pos": "2. Hoàn thành trọn khối lượng", "rule": "Vます + きる / きれる (読みきる = đọc hết sạch, 使いきる = dùng cạn sạch)"},
            {"pos": "3. Không làm xuể (hay thi)", "rule": "Vます + きれない (食べきれない = nhiều quá ăn không xuể, 数えきれない = không đếm xuể)"},
        ],
        "core_meaning_vi": "Thực hiện hành động đến mức triệt để hoàn toàn (きる) hoặc không thể hoàn thành nổi vì số lượng quá lớn (きれない)",
        "deep_explanation_vi": (
            "～きる tự chia như động từ Nhóm 1 (dù kết thúc là る!), nên dạng khả năng phủ định là きれない (không thể ăn hết = 食べきれない, không thể dùng hết = 使いきれない) chứ không phải *きられない. "
            "Đây là cặp hay thi cùng ～やすい/にくい và ～てしまう."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vます + きれない vs Vて + しまう",
                "difference_vi": "きる/きれない đo năng lực hoàn tất toàn bộ số lượng/mức độ triệt để ('ăn không hết nổi'); てしまう chỉ trạng thái đã kết thúc trọn vẹn hoặc lỡ mất.",
                "quick_test_vi": "Thấy khối lượng quá nhiều (こんなにたくさん… / 一人では…) -> きれない.",
            }
        ],
        "examples": [
            {
                "jp": "こんなにたくさんの料理は、一人では食べきれません。",
                "reading_note": "こんなにたくさんのりょうりは、ひとりではたべきれません。",
                "vi": "Nhiều món ăn thế này một mình tôi không thể ăn hết nổi.",
                "grammar_note": "食べる -> 食べ + きれない (không ăn xuể).",
            },
            {
                "jp": "一週間働いて、体も心も疲れきってしまった。",
                "reading_note": "いっしゅうかんはたらいて、からだもこころもつかれきってしまった。",
                "vi": "Làm việc suốt cả tuần khiến cả thể xác lẫn tinh thần mệt rã rời hoàn toàn.",
                "grammar_note": "疲れる -> 疲れ + きる (mệt kiệt sức).",
            },
        ],
        "source_ref": "Shin-N3-List #102 | anki #30",
        "search_keywords": "kiru kirenai lam het sach khong xue きる きれない 食べきれない",
        "match_patterns": ["きれない", "きれません", "きった", "きって"],
    },
    {
        "code": "GP-N3-085",
        "pattern": "Vます + 出す (Bắt đầu đột ngột / Khởi xướng ra)",
        "jlpt_level": "N3",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": True,
        "formation_formula": "Vます(bỏ ます) + 出す（だす）",
        "formation_table": [
            {"pos": "1. Bắt đầu đột ngột", "rule": "Hành động tự nhiên bộc phát bất ngờ (雨が降り出した = trời đột nhiên đổ mưa, 笑い出した = bật cười)"},
            {"pos": "2. Khởi xướng / Phát minh ra", "rule": "言い出す (mở lời đề xuất trước tiên - Q#97), 考え出す (nghĩ ra ý tưởng), 出し合う (cùng đóng góp - Q#83)"},
        ],
        "core_meaning_vi": "Bắt đầu phát sinh hành động một cách đột ngột, bất ngờ hoặc khởi xướng/tạo ra một điều mới",
        "deep_explanation_vi": (
            "Xuất hiện trực tiếp ở câu Từ vựng đồng nghĩa Q#97 ('計画を [言い出した] のは、井上くんだ' = 一番先に言った). "
            "Khác với Vます + 始める (bắt đầu có kế hoạch, diễn tiến từ từ như 'bắt đầu học tiếng Nhật từ 2 năm trước'), Vます + 出す mang tính ĐỘT NGỘT (đang đi thì trời bỗng đổ mưa, nhìn mặt nhau là bật cười) hoặc NGƯỜI ĐẦU TIÊN MỞ LỜI (言い出す)."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vます + 出す vs Vます + 始める",
                "difference_vi": "出す = bắt đầu bất thình lình/đột ngột hoặc mở lời khởi xướng trước; 始める = bắt đầu có chủ ý, tiến độ tự nhiên có quá trình.",
                "quick_test_vi": "Động từ đột ngột (bật khóc, bật cười, mưa ập xuống) hoặc 言い出す -> 出す; quá trình học tập/áp dụng mới (使われ始める) -> 始める.",
            }
        ],
        "examples": [
            {
                "jp": "計画を言い出したのは、井上くんだ。",
                "reading_note": "けいかくをいいだしたのは、いのうえくんだ。",
                "vi": "Người đầu tiên mở lời đề xuất kế hoạch là cậu Inoue.",
                "grammar_note": "Q#97: 言う -> 言い + 出す = mở lời đầu tiên (一番先に言った).",
            },
            {
                "jp": "彼は私の顔を見ると、急に笑い出した。",
                "reading_note": "かれはわたしのかおをみると、きゅうにわらいだした。",
                "vi": "Anh ấy vừa nhìn thấy mặt tôi là đột nhiên bật cười.",
                "grammar_note": "Hành động đột ngột phát sinh dùng Vます + 出す.",
            },
        ],
        "source_ref": "Shin-N3-List #103 | Đề .xlsx (Q97)",
        "search_keywords": "dasu bat dau dot ngot khoi xuong 出す 言い出した 降り出した",
        "match_patterns": ["言い出した", "降り出した", "笑い出した"],
    },
    {
        "code": "GP-N3-086",
        "pattern": "Vます + 抜く / 通す / 切る (Kiên trì suốt từ đầu đến cuối)",
        "jlpt_level": "N3",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": False,
        "formation_formula": "Vます(bỏ ます) + 抜く（ぬく） / 通す（とおす） / 切る（きる）",
        "formation_table": [
            {"pos": "Vます + 抜く", "rule": "Kiên trì vượt qua khó khăn đến tận cùng (走り抜く, 考え抜く, やり抜く)"},
            {"pos": "Vます + 通す", "rule": "Làm liên tục một mạch không đổi từ đầu tới cuối (黙り通す, 立ち通す)"},
        ],
        "core_meaning_vi": "Thực hiện hành động xuyên suốt từ đầu đến cuối mà không bỏ cuộc hay thay đổi giữa chừng",
        "deep_explanation_vi": (
            "Đây là nhóm hậu tố Vます mở rộng từ Shin-N3 #104 giúp mô tả tính bền bỉ hoặc tính xuyên suốt: "
            "Vます+抜く nhấn mạnh vượt qua gian nan tới đích; Vます+通す nhấn mạnh giữ nguyên một trạng thái suốt chặng đường (đứng suốt, im lặng suốt)."
        ),
        "register_tag": "Trung tính & Văn viết",
        "confusable_pairs": [
            {
                "rival_pattern": "Vます + 抜く vs Vます + 続ける",
                "difference_vi": "続ける đơn thuần là 'làm tiếp tục'; 抜く nhấn mạnh 'vượt qua khó khăn để hoàn thành đến tận đích cuối cùng'.",
                "quick_test_vi": "Có sắc thái nỗ lực vượt thử thách tới vạch đích (42km marathon, suy nghĩ nát óc) -> 抜く.",
            }
        ],
        "examples": [
            {
                "jp": "彼は何を聞かれても、最後まで黙り通した。",
                "reading_note": "かれはなにをきかれても、さいごまでだまりとおした。",
                "vi": "Dù bị hỏi bất cứ gì, anh ta cũng giữ im lặng suốt từ đầu đến cuối.",
                "grammar_note": "黙る -> 黙り + 通す.",
            },
            {
                "jp": "つらくても、目標に向かって最後までやり抜くつもりだ。",
                "reading_note": "つらくても、もくひょうにむかってさいごまでやりぬくつもりだ。",
                "vi": "Dù vất vả thế nào tôi cũng quyết tâm làm tới cùng hướng về mục tiêu.",
                "grammar_note": "やり抜く = hoàn thành xuyên suốt dù khó khăn.",
            },
        ],
        "source_ref": "Shin-N3-List #104",
        "search_keywords": "nuku toosu suot tu dau den cuoi kien tri 抜く 通す",
        "match_patterns": ["抜く", "通した", "通りした"],
    },
    {
        "code": "GP-N3-087",
        "pattern": "～がち (Hay có khuynh hướng xấu, dễ bị...)",
        "jlpt_level": "N3",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": False,
        "formation_formula": "Vます(bỏ ます) / N + がちだ / がちな + N / がちに",
        "formation_table": [
            {"pos": "Động từ (Vます)", "rule": "Vます + がちだ (忘れがちだ = hay quên, 遅れがちだ = hay trễ, 不足しがち)"},
            {"pos": "Danh từ (N)", "rule": "N + がちだ (病気がちだ = hay ốm vặt, 留守がちだ = thường vắng nhà, 曇りがち = trời hay âm u)"},
            {"pos": "Lưu ý chia", "rule": "Là Tính từ đuôi な -> bổ nghĩa danh từ dùng がちな + N"},
        ],
        "core_meaning_vi": "Có xu hướng hay xảy ra, dễ rơi vào trạng thái (hầu như chỉ dùng cho điều tiêu cực, khuyết điểm, thời tiết xấu)",
        "deep_explanation_vi": (
            "～がち luôn mang sắc thái TIÊU CỰC hoặc bất lợi (hay quên, hay ốm, hay vắng nhà, thiếu rau xanh, trời hay âm u). "
            "Không dùng cho chuyện tích cực (không nói *合格しがち)."
        ),
        "register_tag": "Trung tính (Khuynh hướng tiêu cực)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vます/N + がち vs Vます + やすい vs N + 気味",
                "difference_vi": "がち = thường xuyên xảy ra thành thói quen/khuynh hướng xấu; やすい = tính chất khách quan dễ xảy ra (tốt hoặc xấu); 気味 = cảm giác hơi có triệu chứng ngay lúc này.",
                "quick_test_vi": "Thói quen lặp đi lặp lại không tốt (忘れがち, 病気がち, 遅れがち) -> がち.",
            }
        ],
        "examples": [
            {
                "jp": "一人暮らしの人は、どうしても野菜不足になりがちだ。",
                "reading_note": "ひとりぐらしのひとは、どうしてもやさいぶそくになりがちだ。",
                "vi": "Người sống một mình thường rất hay rơi vào tình trạng thiếu rau xanh.",
                "grammar_note": "なる -> なり + がちだ.",
            },
            {
                "jp": "最近、約束を忘れがちなのでメモをとるようにしている。",
                "reading_note": "さいきん、やくそくをわすれがちなのでめもをとるようにしている。",
                "vi": "Dạo này tôi hay quên lịch hẹn nên đang cố gắng ghi chép lại.",
                "grammar_note": "Vます (忘れ) + がち + なので.",
            },
        ],
        "source_ref": "Shin-N3-List #105 | anki #26",
        "search_keywords": "gachi khuynh huong tieu cuc hay bi がち 忘れがち 病気がち",
        "match_patterns": ["がちだ", "がちな", "がちです"],
    },
    {
        "code": "GP-N3-088",
        "pattern": "～だらけ (Đầy những, toàn là thứ bẩn/lỗi sai - Chỉ đi với Danh từ!)",
        "jlpt_level": "N3",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": True,
        "formation_formula": "N + だらけだ / だらけの + N (TUYỆT ĐỐI KHÔNG gắn sau động từ!)",
        "formation_table": [
            {"pos": "Danh từ (N)", "rule": "N(bụi bẩn, rác, vết thương, lỗi sai) + だらけ (ゴミだらけ, 間違いだらけ, 傷だらけ, 泥だらけ)"},
            {"pos": "Cấm kết hợp với Vて (Q#55)", "rule": "SAI: *寝てだらけだ (phải là 寝てばかりいる!). だらけ CHỈ gắn sau DANH TỪ"},
        ],
        "core_meaning_vi": "Bị bao phủ dày đặc hoặc chứa đầy những thứ gây khó chịu, dơ bẩn, sai sót",
        "deep_explanation_vi": (
            "Xuất hiện làm bẫy hình thái kinh điển ở Q#55 ('夏休みになって毎日寝て [ばかりいる]', bẫy 'だらけだ'). "
            "Hai tiêu chuẩn để nhận diện ～だらけ: "
            "1) Hình thái: 100% chỉ đi sau DANH TỪ (間違いだらけ, ゴミだらけ), tuyệt đối không đi sau Vて (寝てだらけだ là sai ngay lập tức!). "
            "2) Ngữ nghĩa: 100% chỉ vật tiêu cực, bừa bộn, bẩn thỉu, sai sót (không nói *幸せだらけ hoặc *お金だらけ!)."
        ),
        "register_tag": "Trung tính (Chê trách tiêu cực)",
        "confusable_pairs": [
            {
                "rival_pattern": "N + だらけ vs Vて + ばかりいる vs N + ばかり",
                "difference_vi": "だらけ chỉ đứng sau Danh từ tiêu cực/bẩn/lỗi; ばかり đứng được cả sau Vて (lặp lại hành động) lẫn sau Danh từ (không chỉ tiêu cực).",
                "quick_test_vi": "Trước chỗ trống là động từ Vて (Q#55)? Loại だらけ không cần suy nghĩ!",
            }
        ],
        "examples": [
            {
                "jp": "彼の部屋はゴミだらけで、足の踏み場もない。",
                "reading_note": "かれのへやはごみだらけで、あしのふみばもない。",
                "vi": "Phòng của anh ta toàn là rác rưởi, đến chỗ đặt chân cũng không có.",
                "grammar_note": "Danh từ tiêu cực ゴミ + だらけ.",
            },
            {
                "jp": "急いで書いたので、作文は間違いだらけだった。",
                "reading_note": "いそいでかいたので、さくぶんはまちがいだらけだった。",
                "vi": "Vì viết vội nên bài văn toàn là lỗi sai.",
                "grammar_note": "Danh từ 間違い + だらけ.",
            },
        ],
        "source_ref": "Shin-N3-List #106 | anki #29 | Đề .xlsx (Q55)",
        "search_keywords": "darake day nhung toan la ban loi sai だらけ 間違いだらけ ゴミだらけ",
        "match_patterns": ["だらけ"],
    },
    {
        "code": "GP-N3-089",
        "pattern": "～っぽい (Hơi ngả sang; Có vẻ như / Tính chất nổi trội)",
        "jlpt_level": "N3",
        "category": "conjugation",
        "category_label_vi": CATEGORY_LABELS["conjugation"],
        "in_exam_corpus": True,
        "formation_formula": "Aい(bỏ い) / Vます(bỏ ます) / N + っぽい (Chia như Tính từ đuôi い!)",
        "formation_table": [
            {"pos": "Tính từ い (bỏ い)", "rule": "黒っぽい (hơi đen/ngả đen - Q#61), 白っぽい (hơi trắng)"},
            {"pos": "Động từ (Vます)", "rule": "怒りっぽい (hay nổi cáu), 忘れっぽい (mau quên), 飽きっぽい (mau chán)"},
            {"pos": "Danh từ (N)", "rule": "子どもっぽい (trẻ con), 安っぽい (nhìn rẻ tiền), 水っぽい (lỏng bỏng nhiều nước)"},
        ],
        "core_meaning_vi": "Mang tính chất hơi ngả sang màu/trạng thái nào đó (黒っぽい) hoặc mang tính cách dễ bộc lộ, có vẻ như (thường chê nhẹ)",
        "deep_explanation_vi": (
            "Thi trực tiếp ở Bài Đục lỗ 問題3 Q#61 ('これは、月にある黒 [っぽい] 模様が、ウサギがもちをついているような形に見えるからです'). "
            "Chú ý quy tắc hình thái cực độc đáo của ～っぽい: "
            "khi gắn với tính từ màu sắc 黒い / 白い, PHẢI BỎ ĐUÔI い thành gốc 黒 + っぽい -> 黒っぽい! "
            "Các phương án nhiễu như 的な (chỉ gắn danh từ), らしい (không gắn vào gốc bỏ い như *黒らしい), みたいな (phải có đầy đủ 黒いみたいな) đều sai ngữ pháp!"
        ),
        "register_tag": "Trung tính & Khẩu ngữ",
        "confusable_pairs": [
            {
                "rival_pattern": "Aい(bỏ い) + っぽい vs N + 的な vs 普通形 + らしい/みたいだ",
                "difference_vi": "っぽい gắn trực tiếp vào gốc bỏ い (黒っぽい), Vます (忘れっぽい), hoặc N (子どもっぽい); 的な chỉ gắn N Hán-Nhật; らしい/みたい phải giữ nguyên tính từ đứng trước.",
                "quick_test_vi": "Thấy chữ Hán của tính từ bị cắt mất đuôi い (黒___模様 trong Q#61) -> chốt 100% っぽい!",
            }
        ],
        "examples": [
            {
                "jp": "月にある黒っぽい模様が、ウサギがもちをついているような形に見える。",
                "reading_note": "つきにあるくろっぽいもようが、うさぎがもちをついているようなかたちにみえる。",
                "vi": "Hoa văn hơi đen trên mặt trăng trông giống hình dáng con thỏ đang giã bánh.",
                "grammar_note": "Q#61: 黒い bỏ い thành 黒 + っぽい + 模様.",
            },
            {
                "jp": "彼は大人なのに、まだ少し子どもっぽいところがある。",
                "reading_note": "かれはおとななのに、まだすこしこどもっぽいところがある。",
                "vi": "Anh ấy lớn rồi mà vẫn còn chút nét hơi trẻ con.",
                "grammar_note": "Danh từ 子ども + っぽい.",
            },
        ],
        "source_ref": "anki #28 | Đề .xlsx (Q61)",
        "search_keywords": "ppoi hoi nga mau tinh chat っぽい 黒っぽい 怒りっぽい",
        "match_patterns": ["っぽい", "黒っぽい", "っぽく"],
    },
    {
        "code": "GP-N3-090",
        "pattern": "～において / ～における (Tại, ở, trong phạm vi - Văn viết trang trọng của で)",
        "jlpt_level": "N3",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": True,
        "formation_formula": "N + において（は / も） | N1 + における + N2",
        "formation_table": [
            {"pos": "Vị trí / Bối cảnh / Thời đại", "rule": "N(địa điểm trang trọng, sự kiện, lĩnh vực, thời đại) + において (日本において, 現代社会において)"},
            {"pos": "Bổ nghĩa danh từ (Q#56)", "rule": "N1 + における + N2 (機内における携帯電話の使用 = việc sử dụng điện thoại trên máy bay)"},
        ],
        "core_meaning_vi": "Chỉ địa điểm, bối cảnh, thời kỳ hoặc lĩnh vực diễn ra sự việc trong văn viết trang trọng (tương đương trợ từ で ở mức lịch sự cao)",
        "deep_explanation_vi": (
            "Thi trực tiếp ở 問題2 ★ Q#56 ('機内 [における] [携帯電話の] [使用は] [禁止] されています') và làm nhiễu ở Q#53 ('こちらの店が安いの [に対して]', loại 'において'). "
            "Hai quy tắc phải nhớ: "
            "1) Bổ nghĩa danh từ N2 bằng danh từ N1 chỉ nơi chốn/bối cảnh trang trọng -> dùng N1 + における + N2 (không dùng *においての). "
            "2) Trong Q#53, trước chỗ trống là mệnh đề có đuôi の ('安いの___') so sánh 2 quán ăn -> không thể dùng において (chỉ đi sau danh từ để chỉ địa điểm/lĩnh vực)."
        ),
        "register_tag": "Văn viết / Trang trọng & Thông báo",
        "confusable_pairs": [
            {
                "rival_pattern": "N + において / における vs N + に対して / のに対して",
                "difference_vi": "において chỉ địa điểm/phạm vi bối cảnh ('tại/trong N'); に対して chỉ đối tượng nhận hành động hoặc tương phản 2 vế trái ngược.",
                "quick_test_vi": "Thấy danh từ không gian trang trọng (機内, 会場, 現代社会) đứng trước chỗ trống và N2 đứng sau -> における.",
            }
        ],
        "examples": [
            {
                "jp": "機内における携帯電話の使用は禁止されています。",
                "reading_note": "きないにおけるけいたいでんわのしようはきんしされています。",
                "vi": "Việc sử dụng điện thoại di động trên khoang máy bay bị nghiêm cấm.",
                "grammar_note": "Q#56: N1(機内) + における + N2(携帯電話の使用).",
            },
            {
                "jp": "日本においては、少ない資源のおかげで高い技術力が育った。",
                "reading_note": "にほんにおいては、すくないしげんのおかげでたかいぎじゅつりょくがそだった。",
                "vi": "Tại Nhật Bản, nhờ ít tài nguyên mà năng lực kỹ thuật cao đã phát triển.",
                "grammar_note": "Kosei p.8: N + においては trong văn nghị luận.",
            },
        ],
        "source_ref": "anki #20 | Kosei p.8 | Đề .xlsx (Q53, Q56)",
        "search_keywords": "ni oite ni okeru tai o trong pham vi において における",
        "match_patterns": ["において", "における"],
    },
    {
        "code": "GP-N3-091",
        "pattern": "～からいうと / ～からすると / ～から見れば (Xét từ góc độ / Dựa theo tiêu chuẩn)",
        "jlpt_level": "N3",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": True,
        "formation_formula": "N + からいうと / からいえば / からすると / からすれば / から見ると",
        "formation_table": [
            {"pos": "～からいうと (Xét về mặt)", "rule": "Đưa ra một tiêu chí cụ thể để nhận xét, gợi ý (場所の便利さからいうとAホテルのほうがおすすめ - Q#54)"},
            {"pos": "～からすると (Dựa theo chuẩn/dấu hiệu)", "rule": "Từ mức chuẩn hoặc dấu hiệu N mà đánh giá/suy đoán (女性の平均からすると - Q#59)"},
            {"pos": "～から見ると / ～から見れば", "rule": "Nhìn từ góc độ/lập trường của N (外国人の目から見ると)"},
        ],
        "core_meaning_vi": "Chọn một tiêu chí, mức chuẩn hoặc góc nhìn làm điểm tựa để đưa ra đánh giá, kết luận ở vế sau",
        "deep_explanation_vi": (
            "Đây là cặp mẫu thi trực tiếp ở cả Q#54 ('場所の便利さ [からいうと] Aホテルのほうがおすすめです') lẫn 問題2 ★ Q#59 ('女性の平均 [からすると] [決して] [小さい] [わけ] ではない'). "
            "Khi thấy danh từ chỉ TIÊU CHÍ ĐÁNH GIÁ (場所の便利さ, 値段, 平均, 性格) đứng trước và vế sau là câu NHẬN ĐỊNH/ĐÁNH GIÁ của người nói, hãy chốt ngay ～からいうと / ～からすると!"
        ),
        "register_tag": "Trung tính & Văn viết nghị luận",
        "confusable_pairs": [
            {
                "rival_pattern": "～からいうと / ～からすると vs ～によれば",
                "difference_vi": "からいうと / からすると lấy tiêu chí làm cơ sở để TỰ ĐÁNH GIÁ; によれば trích dẫn nguồn tin NGHE NÓI lại từ bên thứ ba.",
                "quick_test_vi": "Cuối câu là nhận xét chủ quan (おすすめだ, わけではない) -> からいうと / からすると.",
            }
        ],
        "examples": [
            {
                "jp": "どちらもいいホテルですが、場所の便利さからいうとAホテルのほうがおすすめです。",
                "reading_note": "どちらもいいほてるですが、ばしょのべんりさからいうとえーほてるのほうがおすすめです。",
                "vi": "Cả hai đều là khách sạn tốt, nhưng xét về độ tiện lợi của vị trí thì khách sạn A đáng gợi ý hơn.",
                "grammar_note": "Q#54: Tiêu chí 場所の便利さ + からいうと.",
            },
            {
                "jp": "女性の平均からすると決して小さいわけではない。",
                "reading_note": "じょせいのへいきんからするとけっしてちいさいわけではない。",
                "vi": "Xét theo mức trung bình của nữ giới thì hoàn toàn không phải là nhỏ bé.",
                "grammar_note": "Q#59: Mức chuẩn 平均 + からすると + 決して～わけではない.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 | Đề .xlsx (Q54, Q59)",
        "search_keywords": "kara iu to kara suru to xet ve mat tu goc do からいうと からすると から見ると",
        "match_patterns": ["からいうと", "からすると", "からいえば", "から見れば", "から見ると"],
    },
    {
        "code": "GP-N3-092",
        "pattern": "～を問わず (Bất kể, không phân biệt N)",
        "jlpt_level": "N3",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": True,
        "formation_formula": "N + を問わず（をとわず） / は問わず",
        "formation_table": [
            {"pos": "Danh từ cặp đối lập / Phạm trù", "rule": "経験・年齢・性別・国籍・昼夜・晴雨 + を問わず"},
            {"pos": "Dạng phủ định đi kèm thường gặp", "rule": "Tuyển dụng, thông báo công khai: 経験を問わず応募できる (Q#58)"},
        ],
        "core_meaning_vi": "Không đặt ra điều kiện giới hạn hay phân biệt đối với tiêu chí N ('bất kể, không phân biệt N')",
        "deep_explanation_vi": (
            "Thi trực tiếp ở 問題2 ★ Q#58 ('この仕事は、やる気さえあれば [経験] [を問わず] 応募することができます'). "
            "Danh từ đi trước を問わず thường là các tiêu chí tuyển chọn (kinh nghiệm 経験, tuổi tác 年齢, giới tính 性別, quốc tịch 国籍) hoặc cặp từ đối lập (ngày đêm 昼夜, nắng mưa 晴雨). "
            "Rất hay đi cặp với điều kiện tối thiểu duy nhất ～さえあれば ('chỉ cần có X là đủ, bất kể Y')."
        ),
        "register_tag": "Trang trọng / Thông báo tuyển dụng",
        "confusable_pairs": [
            {
                "rival_pattern": "N + を問わず vs N + によって",
                "difference_vi": "を問わず = KHÔNG phân biệt, tất cả đều giống nhau bất chấp N; によって = TÙY THEO từng N mà khác nhau.",
                "quick_test_vi": "Ngữ cảnh tuyển dụng/quy định 'ai cũng tham gia được không cần biết tuổi/kinh nghiệm' -> を問わず.",
            }
        ],
        "examples": [
            {
                "jp": "この仕事は、やる気さえあれば経験を問わず応募することができます。",
                "reading_note": "このしごとは、やるきさえあればけいけんをとわずおうぼすることができます。",
                "vi": "Công việc này chỉ cần có tinh thần quyết tâm là có thể ứng tuyển bất kể kinh nghiệm.",
                "grammar_note": "Q#58: 経験 + を問わず.",
            },
            {
                "jp": "この公園は昼夜を問わず誰でも利用できる。",
                "reading_note": "このこうえんはちゅうやをとわずだれでもりようできる。",
                "vi": "Công viên này bất kể ngày đêm ai cũng có thể sử dụng.",
                "grammar_note": "Cặp đối lập 昼夜 + を問わず.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 | Đề .xlsx (Q58)",
        "search_keywords": "wo towazu bat ke khong phan biet を問わず",
        "match_patterns": ["を問わず", "をとわず"],
    },
    {
        "code": "GP-N3-093",
        "pattern": "～つつある (Đang dần dần biến đổi - Văn viết)",
        "jlpt_level": "N3",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": True,
        "formation_formula": "Vます(bỏ ます) + つつある / つつあります",
        "formation_table": [
            {"pos": "Động từ biến đổi (Vます)", "rule": "Vます + つつある (減りつつあります, 増えつつある, 変わりつつある, 回復しつつある)"},
            {"pos": "Hạn chế động từ", "rule": "Chỉ dùng cho động từ chỉ quá trình biến đổi theo xu thế (không dùng cho ăn uống, ngủ nghỉ tức thời)"},
        ],
        "core_meaning_vi": "Diễn tả một sự biến đổi hoặc xu hướng xã hội/tự nhiên đang diễn ra từng chút một ở hiện tại ('đang dần dần...')",
        "deep_explanation_vi": (
            "Thi trực tiếp ở Bài Đục lỗ 2 Câu [3] (Q#150: '日本の家では和室が [減りつつあります]'). "
            "Điểm quan trọng phân biệt giữa ～つつある và ～ている / ～ていく: "
            "1) ～つつある gắn trực tiếp vào Vます bỏ ます (減り + つつあります) và chuyên dùng trong văn viết, phóng sự để mô tả XU HƯỚNG ĐANG BIẾN ĐỔI DẦN Ở HIỆN TẠI (giảm dần, tăng dần, hồi phục dần, thay đổi dần). "
            "2) Loại 3 phương án nhiễu ở Q#150: 減るだけです (chỉ có giảm - quá cực đoan), 減りやすい (tính chất dễ giảm - sai trục xu hướng thực tế), 減ってもかまいません (giảm cũng chẳng sao - sai logic)."
        ),
        "register_tag": "Văn viết & Báo chí / Thống kê",
        "confusable_pairs": [
            {
                "rival_pattern": "Vます + つつある vs Vます + やすい vs Vる + 一方だ",
                "difference_vi": "つつある = đang dần dần diễn ra ở hiện tại (xu hướng trung tính); やすい = có tính chất dễ bị (không nói đang diễn ra); 一方だ = cứ trượt theo một chiều ngày càng trầm trọng.",
                "quick_test_vi": "Thấy xu hướng xã hội biến chuyển dần gần đây (最近… / 減り・増え・変わり) trong bài báo -> つつある.",
            }
        ],
        "examples": [
            {
                "jp": "いすに座ることが多くなりましたから、日本の家では和室が減りつつあります。",
                "reading_note": "いすにすわることがおおくなりましたから、にほんのいえではわしつがへりつつあります。",
                "vi": "Vì việc ngồi ghế trở nên nhiều hơn nên phòng kiểu Nhật đang ngày càng giảm dần.",
                "grammar_note": "Q#150: 減る -> 減り + つつあります.",
            },
            {
                "jp": "都市部の環境問題は少しずつ改善されつつある。",
                "reading_note": "としぶのかんきょうもんだいはすこしずつかいぜんされつつある。",
                "vi": "Vấn đề môi trường ở khu vực đô thị đang từng chút một được cải thiện dần.",
                "grammar_note": "Thể bị động 改善される + つつある.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 | Đề .xlsx (Q150)",
        "search_keywords": "tsutsu aru dang dan dan xu huong van viet つつある 減りつつ",
        "match_patterns": ["つつある", "つつあります"],
    },
    {
        "code": "GP-N3-094",
        "pattern": "AというのはBのことだ (Định nghĩa khái niệm: A có nghĩa là B)",
        "jlpt_level": "N3",
        "category": "discourse",
        "category_label_vi": CATEGORY_LABELS["discourse"],
        "in_exam_corpus": True,
        "formation_formula": "N1 + というのは / とは + [Giải thích] + のことだ / ということだ",
        "formation_table": [
            {"pos": "Định nghĩa danh từ", "rule": "Aというのは + B(cụm danh từ) + のことだ (スポーツのことだ - Q#21)"},
            {"pos": "Định nghĩa hành động/mệnh đề", "rule": "Aというのは + [Mệnh đề] + ということだ"},
        ],
        "core_meaning_vi": "Giải thích, định nghĩa ý nghĩa của một từ vựng hoặc thuật ngữ ('A có nghĩa là / chỉ B')",
        "deep_explanation_vi": (
            "Thi trực tiếp ở Q#21 ('球技というのは、ボールを使うスポーツ [のことだ]'). "
            "Khi B là một DANH TỪ / CỤM DANH TỪ (như ボールを使うスポーツ), cuối câu BẮT BUỘC nối bằng のことだ (tuyệt đối không dùng というのだ hay というものだ). "
            "Đừng nhầm với ～というものだ (diễn đạt bản chất đương nhiên của cuộc sống hoặc chân lý đạo đức)."
        ),
        "register_tag": "Trung tính (Giải thích thuật ngữ)",
        "confusable_pairs": [
            {
                "rival_pattern": "N + のことだ (Định nghĩa) vs ～というものだ (Chân lý/Bản chất)",
                "difference_vi": "Aというのは Bのことだ dùng để định nghĩa khái niệm từ điển ('A chính là chỉ đối tượng B'); ～というものだ dùng để cảm thán hoặc nêu quy luật hiển nhiên ('cuộc đời vốn là thế đấy').",
                "quick_test_vi": "Thấy mở đầu câu là 'Xというのは...' để giải thích nghĩa từ -> kết thúc bằng のことだ.",
            }
        ],
        "examples": [
            {
                "jp": "球技というのは、ボールを使うスポーツのことだ。",
                "reading_note": "きゅうぎというのは、ぼーるをつかうすぽーつのことだ。",
                "vi": "Môn thể thao dùng bóng (Kyuugi) nghĩa là các môn thể thao sử dụng quả bóng.",
                "grammar_note": "Q#21: Danh từ スポーツ + のことだ.",
            },
            {
                "jp": "休診というのは、病院が休みで診察をしない日のことだ。",
                "reading_note": "きゅうしんというのは、びょういんがやすみでしんさつをしないひのことだ。",
                "vi": "Kyuushin nghĩa là ngày bệnh viện nghỉ không khám bệnh.",
                "grammar_note": "Định nghĩa từ vựng thông báo.",
            },
        ],
        "source_ref": "Đề .xlsx (Q21, Passages 9, 14, 17)",
        "search_keywords": "to iu no wa no koto da dinh nghia thuat ngu というのは のことだ",
        "match_patterns": ["というのは", "のことだ"],
    },
    {
        "code": "GP-N3-095",
        "pattern": "Vる + のに + いい・便利だ・役に立つ (Tốt/Thích hợp/Tiện cho việc làm V)",
        "jlpt_level": "N3",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": True,
        "formation_formula": "Vる + のに + [いい / 便利だ / 役に立つ / 時間がかかる / 必要だ]",
        "formation_table": [
            {"pos": "Động từ (Vる)", "rule": "Vる + のに + Tính từ đánh giá công dụng/chi phí (読書するのにとてもいい季節だ - Q#18)"},
            {"pos": "Phân biệt với ～のに (Mặc dù)", "rule": "Mệnh đề + のに (tương phản 'mặc dù... vậy mà') ≠ Vる + のに + A(いい/便利/必要) = 'cho việc làm V thì rất...'"},
        ],
        "core_meaning_vi": "Đánh giá mức độ phù hợp, tiện lợi hoặc chi phí cần thiết đối với việc thực hiện hành động V",
        "deep_explanation_vi": (
            "Thi trực tiếp ở Q#18 ('日本では、秋は [読書するのに] とてもいい季節だと言われている'). "
            "Học viên thường chỉ nhớ のに nghĩa là 'mặc dù' nên bỏ qua phương án đúng ở Q#18! "
            "Thực chất, khi đằng sau Vる + のに là các tính từ/động từ đánh giá công dụng, mức độ phù hợp hay thời gian/tiền bạc (いい, 便利だ, 役に立つ, 時間がかかる, 使う), の chính là danh từ hóa và に chỉ mục đích ('cho việc đọc sách'). "
            "Các phương án nhiễu trong Q#18: 読書することで ('bằng cách đọc sách' - sai quan hệ phương tiện), 読書できるように ('để có thể đọc sách' - mùa thu là mùa phù hợp chứ không tạo mục đích hành động)."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vる + のに + いい/便利だ vs Vる + ことで vs Vえる + ように",
                "difference_vi": "Vる+のに+A đánh giá sự thích hợp/tiện dụng của một thời điểm hay dụng cụ cho việc làm V; ことで chỉ phương tiện đạt kết quả; ように chỉ mục đích nỗ lực.",
                "quick_test_vi": "Sau chỗ trống là tính từ いい / 便利だ / 時間がかかる / 役に立つ -> chốt Vる + のに!",
            }
        ],
        "examples": [
            {
                "jp": "日本では、秋は読書するのにとてもいい季節だと言われている。",
                "reading_note": "にほんでは、あきはどくしょするのにとてもいいきせつだといわれている。",
                "vi": "Ở Nhật Bản, người ta nói mùa thu là mùa rất thích hợp cho việc đọc sách.",
                "grammar_note": "Q#18: 読書する + のに + とてもいい季節.",
            },
            {
                "jp": "この辞書は意味を調べるのにとても便利だ。",
                "reading_note": "このじしょはいみをしらべるのにとてもべんりだ。",
                "vi": "Cuốn từ điển này rất tiện lợi cho việc tra cứu ý nghĩa.",
                "grammar_note": "調べる + のに + 便利だ.",
            },
        ],
        "source_ref": "Đề .xlsx (Q18)",
        "search_keywords": "no ni ii benri thich hop cho viec のに 読書するのに",
        "match_patterns": ["するのに", "べるのに", "うのに"],
    },
    {
        "code": "GP-N3-096",
        "pattern": "～ことで (Bằng cách làm V / Nhờ việc V mà...)",
        "jlpt_level": "N3",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": True,
        "formation_formula": "Vる / Vた / Vない + ことで",
        "formation_table": [
            {"pos": "1. Chỉ phương tiện / cách thức", "rule": "Vる + ことで (毎日練習することで上達する = bằng cách luyện mỗi ngày sẽ tiến bộ)"},
            {"pos": "2. Chỉ nguyên nhân trực tiếp", "rule": "Vる/Vた + ことで (ニュースを見たことで安心した); N + のこと + で (chuyện về N)"},
        ],
        "core_meaning_vi": "Thông qua hành động/biện pháp V để đạt được kết quả ở vế sau ('bằng việc V / do việc V')",
        "deep_explanation_vi": (
            "Xuất hiện làm phương án nhiễu ở Q#18 ('読書することで' bị loại vì mùa thu không phải phương tiện đạt được bằng cách đọc sách) và làm cấu trúc chính trong Q#53 ('量が多いことで評判だ' = nổi tiếng VÌ lượng đồ ăn nhiều). "
            "Đừng nhầm ～ことで với ～ことによって (văn viết trang trọng hơn cho tác nhân/phương pháp) hay ～のに (đánh giá tính thích hợp)."
        ),
        "register_tag": "Trung tính",
        "confusable_pairs": [
            {
                "rival_pattern": "Vる + ことで vs Vる + のに + いい",
                "difference_vi": "ことで = bằng phương tiện/cách thức làm V (hoặc vì đặc điểm V nên nổi tiếng/vui); のに = thích hợp cho mục đích làm V.",
                "quick_test_vi": "Vế sau là kết quả hành động đạt được hoặc lý do nổi tiếng (Q#53) -> ことで; vế sau là いい季節/便利だ (Q#18) -> のに.",
            }
        ],
        "examples": [
            {
                "jp": "あちらの店は量が多いことで評判だ。",
                "reading_note": "あちらのみせはりょうがおおいことでひょうばんだ。",
                "vi": "Quán bên kia nổi tiếng vì lượng thức ăn nhiều.",
                "grammar_note": "Q#53: Mệnh đề nguyên nhân 量が多い + ことで.",
            },
            {
                "jp": "毎日声を出して読むことで、発音が良くなる。",
                "reading_note": "まいにちこえをだしてよむことで、はつおんがよくなる。",
                "vi": "Bằng cách đọc thành tiếng mỗi ngày, phát âm sẽ tốt lên.",
                "grammar_note": "Vる + ことで chỉ phương pháp luyện tập.",
            },
        ],
        "source_ref": "Đề .xlsx (Q18, Q53)",
        "search_keywords": "koto de bang cach nho viec ことで",
        "match_patterns": ["ことで"],
    },
    {
        "code": "GP-N3-097",
        "pattern": "～ものだ / ～ものではない (Bản chất đương nhiên / Quy chuẩn đạo đức / Hoài niệm)",
        "jlpt_level": "N3",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": True,
        "formation_formula": "Vる/Vない / Aい / Aな+な + ものだ / ものではない | Vた + ものだ (Hồi tưởng)",
        "formation_table": [
            {"pos": "1. Bản chất đương nhiên", "rule": "Đặt cuối nhận định khái quát (家族は懐かしいものだ - Q#103; 失われていくものなのだ - Passage 9)"},
            {"pos": "2. Quy chuẩn đạo đức chung", "rule": "Vる + ものだ / Vる + ものではない (人の悪口は言うものではない = không nên nói xấu người khác)"},
            {"pos": "3. Hoài niệm quá khứ", "rule": "Vた + ものだ (Hồi nhỏ thường hay làm V lắm: よく遊んだものだ)"},
        ],
        "core_meaning_vi": "Nêu chân lý/bản chất tự nhiên (～ものだ), khuyên răn chuẩn mực đạo đức chung (～ものではない) hoặc hồi tưởng thói quen xưa (Vたものだ)",
        "deep_explanation_vi": (
            "Gặp cả trong Q#103 ('やはり国の家族はなつかしいものだ'), Passage 9 ('普通は成長すると失われていくものなのだ') và làm nhiễu ở Q#21 ('球技というのはスポーツ [のことだ]', loại 'というものだ'). "
            "Nhớ phân biệt rõ: ～というものだ nêu CHÂN LÝ CHUNG của đời sống (人生とはそういうものだ), KHÔNG dùng để định nghĩa thuật ngữ từ điển (cái đó phải dùng のことだ!)."
        ),
        "register_tag": "Trung tính & Văn viết triết lý",
        "confusable_pairs": [
            {
                "rival_pattern": "～というものだ (Chân lý) vs ～のことだ (Định nghĩa) vs ～べきではない",
                "difference_vi": "ものだ nêu bản chất tự nhiên/quy chuẩn chung không nhắm cá nhân; のことだ định nghĩa nghĩa của từ; べきではない khuyên/cấm trực diện vào trách nhiệm cụ thể.",
                "quick_test_vi": "Thấy '国の家族は懐かしい___' (cảm nhận bản chất phổ quát) -> ものだ; thấy 'XというのはY___' (Q#21) -> のことだ.",
            }
        ],
        "examples": [
            {
                "jp": "日本へ来て何年たっても、やはり国の家族はなつかしいものだ。",
                "reading_note": "にほんへきてなんねんたっても、やはりくにのかぞくはなつかしいものだ。",
                "vi": "Dù đến Nhật bao nhiêu năm trôi qua đi nữa, gia đình ở quê nhà vẫn thật đáng nhớ biết bao.",
                "grammar_note": "Q#103: Cảm nhận phổ quát mang tính chân lý dùng Aい + ものだ.",
            },
            {
                "jp": "人の悪口は言うものではない。",
                "reading_note": "ひとのわるぐちはいうものではない。",
                "vi": "Không nên nói xấu sau lưng người khác.",
                "grammar_note": "Quy chuẩn đạo đức chung dùng Vる + ものではない.",
            },
        ],
        "source_ref": "anki #10 | Đề .xlsx (Q21, Q103, Passage 9)",
        "search_keywords": "mono da mono de wa nai ban chat dao duc hoai niem ものだ ものではない ものなのだ",
        "match_patterns": ["ものだ", "ものではない", "ものなのだ"],
    },
    {
        "code": "GP-N3-098",
        "pattern": "～ものだから (Thanh minh lý do) & ～ものの (Mặc dù... nhưng)",
        "jlpt_level": "N3",
        "category": "contrast_concession",
        "category_label_vi": CATEGORY_LABELS["contrast_concession"],
        "in_exam_corpus": True,
        "formation_formula": "普通形(Aなな/Nな) + ものだから (Thanh minh) | 普通形(Aなな・である/Nである) + ものの (Mặc dù... nhưng)",
        "formation_table": [
            {"pos": "1. ～ものだから / もので (Thanh minh)", "rule": "Giải thích lý do cá nhân ngoài ý muốn (バスが遅れたものだから遅刻しました)"},
            {"pos": "2. ～ものの (Mặc dù... nhưng - Văn viết)", "rule": "Thừa nhận A là thật nhưng B chưa tương xứng/khác mong đợi (大きな事故にあったものの助かった - Q#93)"},
        ],
        "core_meaning_vi": "Biện minh lý do cá nhân cho sai sót (ものだから) và đối lập trang trọng 'tuy A nhưng B' (ものの)",
        "deep_explanation_vi": (
            "Hai mẫu cùng chứa gốc もの nhưng nghĩa ngược chiều nhau: "
            "～ものだから là LÝ DO THANH MINH trong hội thoại (tránh dùng ものだから với câu mệnh lệnh hay ý chí!). "
            "Còn ～ものの xuất hiện trực tiếp ở câu Từ vựng Q#93 ('大きな事故にあったものの、なんとか助かった' = mặc dù gặp tai nạn lớn nhưng vẫn thoát chết), là cách nói nhượng bộ trang trọng tương đương ～けれども nhưng mang sắc thái văn viết."
        ),
        "register_tag": "Khẩu ngữ thanh minh (ものだから) & Văn viết (ものの)",
        "confusable_pairs": [
            {
                "rival_pattern": "～ものだから vs ～ものの vs ～のに",
                "difference_vi": "ものだから = bởi vì (thanh minh); ものの = mặc dù nhưng (nhượng bộ văn viết, vế sau thường là kết quả hạn chế/may mắn); のに = mặc dù nhưng (tiếc nuối/trách).",
                "quick_test_vi": "Thấy vế trước có tai nạn/bằng cấp mà vế sau trái kỳ vọng (Q#93) -> ものの; thấy lời xin lỗi vì kẹt xe/ngủ quên -> ものだから.",
            }
        ],
        "examples": [
            {
                "jp": "大きな事故にあったものの、なんとか助かった。",
                "reading_note": "おおきなじこにあったものの、なんとかたすかった。",
                "vi": "Mặc dù gặp phải vụ tai nạn lớn nhưng bằng cách nào đó tôi vẫn thoát nạn.",
                "grammar_note": "Q#93: Vた + ものの nối nhượng bộ văn viết.",
            },
            {
                "jp": "バスが遅れたものだから、遅刻してしまいました。",
                "reading_note": "ばすがおくれたものだから、ちこくしてしまいました。",
                "vi": "Vì xe buýt đến muộn nên tôi lỡ bị đi trễ mất rồi.",
                "grammar_note": "Thanh minh nguyên nhân ngoài ý muốn dùng ものだから.",
            },
        ],
        "source_ref": "anki #11, #12 | Đề .xlsx (Q93)",
        "search_keywords": "mono dakara monono thanh minh mac du nhung ものだから ものの",
        "match_patterns": ["ものの", "ものだから", "もので"],
    },
    {
        "code": "GP-N3-099",
        "pattern": "～にしたがって / ～につれて / ～にともなって (Càng... càng... / Cùng với sự biến đổi)",
        "jlpt_level": "N3",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": True,
        "formation_formula": "Vる / N(sự biến đổi) + にしたがって / につれて / にともなって",
        "formation_table": [
            {"pos": "1. ～につれて (Tự nhiên đồng biến)", "rule": "Khi A thay đổi thì B tự nhiên thay đổi theo một chiều (年をとるにつれて, 登るにつれて)"},
            {"pos": "2. ～にしたがって (Đồng biến / Tuân theo)", "rule": "Dùng cho biến đổi song hành HOẶC tuân theo chỉ thị/quy tắc (指示にしたがって)"},
            {"pos": "3. ～にともなって (Kéo theo - Trang trọng)", "rule": "Dùng với danh từ quy mô lớn, xã hội/kinh tế (人口の増加にともなって)"},
        ],
        "core_meaning_vi": "Diễn tả hai hiện tượng biến đổi song hành cùng chiều ('cùng với A biến đổi thì B cũng kéo theo biến đổi')",
        "deep_explanation_vi": (
            "Xuất hiện làm phương án nhiễu ở Bài Đục lỗ 2 Câu [4] (Q#151: '風は植物が出す水分 [によって] 冷やされているので', với 2 nhiễu 'につれて' và 'にともなって'). "
            "Cách loại bẫy ngay lập tức: "
            "～につれて / ～にともなって BẮT BUỘC đi với ĐỘNG TỪ BIẾN ĐỔI (như 増える, 減る, 進む, 涼しくなる, 高くなる) ở cả 2 vế, KHÔNG bao giờ dùng để chỉ tác nhân của động từ bị động tĩnh như 冷やされている (được làm mát bởi hơi nước)!"
        ),
        "register_tag": "Trung tính & Văn viết",
        "confusable_pairs": [
            {
                "rival_pattern": "～につれて / ～にともなって vs ～によって",
                "difference_vi": "につれて/にともなって = sự biến đổi tỷ lệ thuận (A tăng thì B cũng thay đổi); によって = tác nhân gây ra hành động bị động hoặc tùy thuộc vào.",
                "quick_test_vi": "Vế sau là thể Bị động tĩnh (冷やされている trong Q#151) -> loại ngay につれて / にともなって, chọn によって!",
            }
        ],
        "examples": [
            {
                "jp": "山に登るにつれて、気温が下がってきた。",
                "reading_note": "やまにのぼるにつれて、きおんがさがってきた。",
                "vi": "Càng leo lên núi cao thì nhiệt độ càng hạ xuống dần.",
                "grammar_note": "Vる (登る) + につれて + biến đổi tỷ lệ thuận 下がってきた.",
            },
            {
                "jp": "高齢化が進むにしたがって、介護の問題が深刻になっている。",
                "reading_note": "こうれいかがすすむにしたがって、かいごのもんだいがしんこくになっている。",
                "vi": "Cùng với sự già hóa dân số tiến triển, vấn đề chăm sóc người già ngày càng nghiêm trọng.",
                "grammar_note": "Biến đổi xã hội song hành dùng にしたがって.",
            },
        ],
        "source_ref": "anki #17 | Đề .xlsx (Q151)",
        "search_keywords": "ni tsurete ni shitagatte ni tomonatte bien doi song hanh につれて にしたがって にともなって",
        "match_patterns": ["につれて", "にしたがって", "にともなって", "に従って", "に伴って"],
    },
    {
        "code": "GP-N3-100",
        "pattern": "～にわたって / ～にわたる (Suốt, trải dài trên diện rộng thời gian/không gian)",
        "jlpt_level": "N3",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": False,
        "formation_formula": "N(khoảng thời gian / không gian / phạm vi rộng) + にわたって / にわたる + N",
        "formation_table": [
            {"pos": "Danh từ thời gian rộng", "rule": "3日間にわたって, 10年間にわたって, 長期間にわたって"},
            {"pos": "Danh từ không gian / lĩnh vực rộng", "rule": "全国にわたって, 多方面にわたる研究"},
        ],
        "core_meaning_vi": "Nhấn mạnh quy mô rộng lớn hoặc thời gian kéo dài liên tục suốt toàn bộ phạm vi N",
        "deep_explanation_vi": (
            "Danh từ đi trước ～にわたって PHẢI mang tính rộng/dài (nhiều ngày, nhiều năm, toàn quốc, nhiều lĩnh vực). "
            "Không dùng cho khoảng thời gian quá ngắn (không nói *5分間にわたって!)."
        ),
        "register_tag": "Văn viết & Báo chí",
        "confusable_pairs": [
            {
                "rival_pattern": "～にわたって vs ～を通じて",
                "difference_vi": "にわたって nhấn mạnh quy mô RỘNG LỚN / DÀI LÂU gây ấn tượng (suốt 3 năm ròng, trên khắp toàn quốc); を通じて nhấn mạnh tính liên tục đều đặn trong một chu kỳ trọn vẹn (一年を通じて).",
                "quick_test_vi": "Thấy số lượng năm/tháng lớn (3年間, 全国, 多くの分野) -> にわたって.",
            }
        ],
        "examples": [
            {
                "jp": "工事は3年間にわたって行われた。",
                "reading_note": "こうじはさんねんかんにわたっておこなわれた。",
                "vi": "Công trình xây dựng đã được tiến hành suốt 3 năm ròng.",
                "grammar_note": "Khoảng thời gian dài 3年間 + にわたって.",
            },
            {
                "jp": "台風は九州から関東にわたって大きな被害を出した。",
                "reading_note": "たいふうはきゅうしゅうからかんとうにわたっておおきなひがいをだした。",
                "vi": "Cơn bão đã gây thiệt hại lớn trải dài trên diện rộng từ Kyushu tới Kanto.",
                "grammar_note": "Phạm vi địa lý rộng dùng にわたって.",
            },
        ],
        "source_ref": "anki #18",
        "search_keywords": "ni watatte ni wataru suot trai dai dien rong にわたって にわたる",
        "match_patterns": ["にわたって", "にわたる"],
    },
    {
        "code": "GP-N3-101",
        "pattern": "～に際して / ～にあたって (Nhân dịp, trước thềm sự kiện quan trọng)",
        "jlpt_level": "N3",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": False,
        "formation_formula": "Vる / N(sự kiện trang trọng) + に際して（にさいして） / にあたって",
        "formation_table": [
            {"pos": "Danh từ / Động từ", "rule": "お申し込みに際して (khi đăng ký), 開店にあたって (nhân dịp khai trương), 卒業に際して"},
            {"pos": "Giới hạn ngữ cảnh", "rule": "Chỉ dùng cho bước ngoặt quan trọng hoặc thủ tục trang trọng (kết hôn, nhập học, ký hợp đồng, khởi nghiệp) — không dùng cho sinh hoạt thường ngày"},
        ],
        "core_meaning_vi": "Nhân dịp hoặc ngay thời điểm bắt đầu thực hiện một sự kiện, thủ tục quan trọng",
        "deep_explanation_vi": (
            "～に際して và ～にあたって đều dùng trong văn phong trang trọng khi đứng trước một dấu mốc lớn (phát biểu khai mạc, lưu ý khi làm hồ sơ đăng ký, chia tay tốt nghiệp). "
            "～にあたって mang sắc thái tích cực hướng về khởi đầu mới (nhân dịp mở cửa hàng mới, chuẩn bị dự án mới), còn ～に際して dùng rộng cho cả quy định thủ tục hành chính."
        ),
        "register_tag": "Trang trọng / Phát biểu & Thủ tục",
        "confusable_pairs": [
            {
                "rival_pattern": "～に際して / ～にあたって vs ～ときに",
                "difference_vi": "ときに dùng mọi tình huống đời thường; に際して / にあたって chỉ dùng cho sự kiện trang trọng, thủ tục chính thức hoặc bước ngoặt đời người.",
                "quick_test_vi": "Thấy お申し込み / 卒業 / 開始 / 開会 + kính ngữ hoặc lời nhắc thủ tục -> に際して / にあたって.",
            }
        ],
        "examples": [
            {
                "jp": "お申し込みに際して、身分証明書が必要です。",
                "reading_note": "おもうしこみにさいして、みぶんしょうめいしょがひつようです。",
                "vi": "Khi tiến hành đăng ký, quý khách cần có giấy tờ tùy thân.",
                "grammar_note": "Thủ tục hành chính dùng に際して.",
            },
            {
                "jp": "新しい店を開くにあたって、家族や友人が協力してくれた。",
                "reading_note": "あたらしいみせをひらくにあたって、かぞくやゆうじんがきょうりょくしてくれた。",
                "vi": "Nhân dịp mở cửa hàng mới, gia đình và bạn bè đã giúp đỡ tôi.",
                "grammar_note": "Bước ngoặt khởi đầu tích cực dùng Vる + にあたって.",
            },
        ],
        "source_ref": "anki #21",
        "search_keywords": "ni saishite ni atatte nhan dip su kien quan trong に際して にあたって",
        "match_patterns": ["に際して", "にあたって", "に当たって"],
    },
    {
        "code": "GP-N3-102",
        "pattern": "～をめぐって / ～をめぐる (Xoay quanh vấn đề tranh cãi)",
        "jlpt_level": "N3",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": False,
        "formation_formula": "N(vấn đề tranh luận) + をめぐって / をめぐる + N",
        "formation_table": [
            {"pos": "Bổ nghĩa động từ", "rule": "N + をめぐって + [争う / 議論する / 対立する / 話し合う]"},
            {"pos": "Bổ nghĩa danh từ", "rule": "N1 + をめぐる + N2 (環境問題をめぐる議論 = cuộc tranh luận xoay quanh vấn đề môi trường)"},
        ],
        "core_meaning_vi": "Lấy vấn đề N làm tâm điểm cho nhiều bên tranh cãi, đối lập ý kiến hoặc thảo luận sôi nổi",
        "deep_explanation_vi": (
            "Khác với ～について (thảo luận/hỏi thông thường), ～をめぐって LUÔN gắn với hình ảnh NHIỀU BÊN CÓ Ý KIẾN KHÁC NHAU xoay quanh một vấn đề nóng (di sản, dự án, chính sách, môi trường). "
            "Vế sau thường xuất hiện các động từ 争う (tranh chấp), 議論する (tranh luận), 対立する (đối lập), 意見が分かれる (ý kiến chia rẽ)."
        ),
        "register_tag": "Văn viết & Thời sự",
        "confusable_pairs": [
            {
                "rival_pattern": "～をめぐって vs ～について",
                "difference_vi": "について là 'nói/viết/hỏi về chủ đề N' (trung tính 1 chiều); をめぐって là 'nhiều bên tranh cãi, chia rẽ ý kiến xoay quanh N'.",
                "quick_test_vi": "Vế sau có 争う / 議論する / 対立する / 意見が分かれる -> をめぐって.",
            }
        ],
        "examples": [
            {
                "jp": "新しい空港の建設をめぐって、市民の間で議論が続いている。",
                "reading_note": "あたらしいくうこうのけんせつをめぐって、しみんのあいだでぎろんがつづいている。",
                "vi": "Xoay quanh việc xây dựng sân bay mới, cuộc tranh luận giữa người dân vẫn đang tiếp diễn.",
                "grammar_note": "Danh từ vấn đề + をめぐって + 議論が続く.",
            },
            {
                "jp": "親の遺産をめぐって、兄弟が争っている。",
                "reading_note": "おやのいさんをめぐって、きょうだいがあらそっている。",
                "vi": "Các anh em đang tranh chấp xoay quanh khối di sản của cha mẹ.",
                "grammar_note": "Động từ tranh chấp 争う đi cùng をめぐって.",
            },
        ],
        "source_ref": "anki #23",
        "search_keywords": "wo megutte wo meguru xoay quanh tranh cai をめぐって をめぐる",
        "match_patterns": ["をめぐって", "をめぐる"],
    },
    {
        "code": "GP-N3-103",
        "pattern": "～に基づいて / ～に基づく (Dựa trên, căn cứ vào tiêu chuẩn/dữ liệu)",
        "jlpt_level": "N3",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": False,
        "formation_formula": "N(luật lệ / số liệu / sự thật / điều tra) + に基づいて / に基づく + N",
        "formation_table": [
            {"pos": "Bổ nghĩa động từ", "rule": "N + に基づいて (調査の結果に基づいて計画を立てる = lập kế hoạch dựa trên kết quả khảo sát)"},
            {"pos": "Bổ nghĩa danh từ", "rule": "N1 + に基づく + N2 (事実に基づく映画 = phim dựa trên sự thật)"},
        ],
        "core_meaning_vi": "Lấy dữ liệu thực tế, luật pháp, quy chuẩn hoặc sự thật khách quan N làm nền tảng để thực hiện, phán đoán",
        "deep_explanation_vi": (
            "～に基づいて chuyên đi với các danh từ có tính căn cứ chuẩn mực: 調査 (điều tra), データ (dữ liệu), 法律 (pháp luật), 経験 (kinh nghiệm), 事実 (sự thật). "
            "Khác với ～をもとに (lấy làm chất liệu sáng tác tự do hơn như lấy cảm hứng từ tiểu thuyết để viết kịch bản), に基づいて nhấn mạnh sự tuân thủ chặt chẽ cơ sở dữ liệu/quy định."
        ),
        "register_tag": "Văn viết & Báo cáo chuyên môn",
        "confusable_pairs": [
            {
                "rival_pattern": "～に基づいて vs ～をもとに vs ～によって",
                "difference_vi": "に基づいて = căn cứ vào số liệu/quy định chuẩn mực; をもとに = lấy làm chất liệu/ý tưởng gốc để sáng tạo; によって = tùy vào / bởi tác nhân.",
                "quick_test_vi": "Thấy 調査結果 / 法律 / ルール / データ -> に基づいて.",
            }
        ],
        "examples": [
            {
                "jp": "アンケート調査の結果に基づいて、新しい計画を立てた。",
                "reading_note": "あんけーとちょうさのけっかにもとづいて、あたらしいけいかくをたてた。",
                "vi": "Tôi đã lập kế hoạch mới dựa trên kết quả điều tra bảng hỏi.",
                "grammar_note": "Kết quả khảo sát (căn cứ khách quan) + に基づいて.",
            },
            {
                "jp": "これは実際に起きた出来事に基づく物語だ。",
                "reading_note": "これはじっさいにおきたできごとにもとづくものがたりだ。",
                "vi": "Đây là câu chuyện dựa trên sự việc có thật đã xảy ra.",
                "grammar_note": "N1 + に基づく + N2.",
            },
        ],
        "source_ref": "anki #24",
        "search_keywords": "ni motozuite ni motozuku dua tren can cu vao に基づいて に基づく",
        "match_patterns": ["に基づいて", "に基づく"],
    },
    {
        "code": "GP-N3-104",
        "pattern": "～気味（ぎみ） (Có triệu chứng, cảm giác hơi hơi...)",
        "jlpt_level": "N3",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": False,
        "formation_formula": "Vます(bỏ ます) / N + 気味だ / 気味に",
        "formation_table": [
            {"pos": "Động từ (Vます)", "rule": "Vます + 気味 (疲れ気味だ = hơi mệt, 遅れ気味 = hơi trễ tiến độ, 太り気味 = hơi tăng cân)"},
            {"pos": "Danh từ (N)", "rule": "N + 気味 (かぜ気味 = hơi có triệu chứng cảm, 緊張気味 = hơi căng thẳng)"},
        ],
        "core_meaning_vi": "Cảm nhận cơ thể, tâm trạng hoặc tình hình có dấu hiệu, triệu chứng hơi hơi nghiêng về chiều hướng xấu",
        "deep_explanation_vi": (
            "～気味 diễn tả trạng thái nhẹ đang bắt đầu chớm xuất hiện ở thời điểm hiện tại (như hôm nay hơi cảm, dạo này hơi mập lên chút, hơi mệt). "
            "Khác với ～がち (thói quen thường xuyên lặp lại nhiều lần) và ～っぽい (tính chất bên ngoài rõ rệt hoặc chê tính cách)."
        ),
        "register_tag": "Trung tính (Sức khỏe & Trạng thái nhẹ)",
        "confusable_pairs": [
            {
                "rival_pattern": "～気味 vs ～がち vs ～っぽい",
                "difference_vi": "気味 = hơi có triệu chứng nhẹ hiện tại (かぜ気味, 疲れ気味); がち = khuynh hướng lặp lại thường xuyên (忘れがち, 病気がち); っぽい = tính chất nổi trội (黒っぽい, 怒りっぽい).",
                "quick_test_vi": "Cảm giác hơi ốm/hơi mệt/hơi căng thẳng nhẹ (少し…) -> 気味.",
            }
        ],
        "examples": [
            {
                "jp": "今日は少し風邪気味なので、早く寝ます。",
                "reading_note": "きょうはすこしかぜぎみなので、はやくねます。",
                "vi": "Hôm nay tôi thấy hơi có triệu chứng cảm nhẹ nên sẽ đi ngủ sớm.",
                "grammar_note": "Danh từ 風邪 + 気味.",
            },
            {
                "jp": "最近運動不足で、少し太り気味になってきた。",
                "reading_note": "さいきんうんどうぶそくで、すこしふとりぎみになってきた。",
                "vi": "Dạo này thiếu vận động nên tôi hơi có dấu hiệu tăng cân.",
                "grammar_note": "Vます (太り) + 気味.",
            },
        ],
        "source_ref": "anki #27",
        "search_keywords": "gimi hoi co trieu chung 気味 ぎみ 風邪気味",
        "match_patterns": ["気味", "ぎみ"],
    },
    {
        "code": "GP-N3-105",
        "pattern": "～わりに（は） / ～にしては (So với chuẩn mực... thì lại bất ngờ trái mong đợi)",
        "jlpt_level": "N3",
        "category": "contrast_concession",
        "category_label_vi": CATEGORY_LABELS["contrast_concession"],
        "in_exam_corpus": True,
        "formation_formula": "V普通形 / Aい / Aな+な / N+の + わりに（は） | N / V普通形 + にしては",
        "formation_table": [
            {"pos": "～わりに（は）", "rule": "So với tiêu chuẩn chung về mức độ (tuổi tác, giá cả, công sức): 年のわりに若い, 安さのわりに美味しい"},
            {"pos": "～にしては", "rule": "Dù mang danh nghĩa/thông số cụ thể đó nhưng lại không khớp hình dung (日本人にしては, 10年住んでいるにしては)"},
            {"pos": "Liên từ đầu câu (Q#62)", "rule": "そのわりに = tuy thế nhưng mà (không hợp câu nhân quả 'Vì mặt trăng quay 1 mặt -> Do đó hoa văn giống nhau' ở Q#62!)"},
        ],
        "core_meaning_vi": "Đặt hai vế đối lập với kỳ vọng thông thường: 'so với chuẩn A thì kết quả B lại bất ngờ vượt/kém hơn'",
        "deep_explanation_vi": (
            "Dạng liên từ đầu câu そのわりに xuất hiện làm nhiễu ở Bài Đục lỗ Q#62 ('月はいつも同じ面を向けています。[そのため]、月の模様はどこから見ても同じです'). "
            "Học viên cần nhớ: わりに và にしては chỉ dùng khi hai vế TRÁI KỲ VỌNG (giá rẻ mà ngon, học 10 năm mà không nói được), tuyệt đối không dùng khi hai vế thuận chiều nhân-quả! "
            "Điểm khác giữa hai mẫu: わりに có thể đi với danh từ tính chất (値段のわりに) còn にしては đi với đối tượng thực thể cụ thể (小学生にしては, 初級者にしては)."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "～わりに vs ～にしては vs そのわりに vs そのため",
                "difference_vi": "わりに/にしては/そのわりに đều mang nghĩa tương phản trái kỳ vọng ('tuy vậy mà...'); そのため mang nghĩa nhân quả thuận chiều ('vì vậy nên...').",
                "quick_test_vi": "Hai vế thuận chiều nguyên nhân -> kết quả (Q#62) -> そのため; hai vế ngược mong đợi -> わりに / にしては.",
            }
        ],
        "examples": [
            {
                "jp": "このレストランは、値段が安いわりに料理がおいしい。",
                "reading_note": "このれすとらんは、ねだんがやすいわりにりょうりがおいしい。",
                "vi": "Nhà hàng này so với mức giá rẻ thì món ăn lại rất ngon.",
                "grammar_note": "Kết quả vượt kỳ vọng so với mức giá -> わりに.",
            },
            {
                "jp": "彼は日本に10年も住んでいるにしては、日本語があまり話せない。",
                "reading_note": "かれはにほんにじゅうねんもすんでいるにしては、にほんごがあまりはなせない。",
                "vi": "Anh ấy sống ở Nhật tận 10 năm rồi thế mà lại không nói được nhiều tiếng Nhật.",
                "grammar_note": "Số liệu cụ thể 10年 + にしては + kết quả thấp hơn kỳ vọng.",
            },
        ],
        "source_ref": "anki #37, #38 | Đề .xlsx (Q62)",
        "search_keywords": "wari ni ni shite wa so voi chuan muc trai ky vong わりに にしては そのわりに",
        "match_patterns": ["わりに", "にしては", "そのわりに"],
    },
    {
        "code": "GP-N3-106",
        "pattern": "～に比べて (So với đối tượng cụ thể...)",
        "jlpt_level": "N3",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": True,
        "formation_formula": "N + に比べて（にくらべて） / にくらべると",
        "formation_table": [
            {"pos": "Danh từ đối chiếu (N)", "rule": "N + に比べて (昔にくらべて = so với ngày xưa - Q#136; 去年と比べて)"},
            {"pos": "Mệnh đề so sánh", "rule": "Vるのに比べて (So với việc làm V)"},
        ],
        "core_meaning_vi": "Đặt hai đối tượng lên bàn cân để so sánh sự khác biệt về mức độ, tính chất ('so với N thì...')",
        "deep_explanation_vi": (
            "Xuất hiện trực tiếp trong Q#136 ('昔にくらべて、現在はきびしい時代だと思います') và làm phương án nhiễu ở Q#16 ('大きさ [によって] 三つに分けてください', loại 'に比べて'). "
            "Lưu ý Q#16: 'phân loại thành 3 nhóm theo kích cỡ' là dựa theo tiêu chí (によって), không phải so sánh giữa các chai với một chuẩn cố định (に比べて)."
        ),
        "register_tag": "Trung tính (Hội thoại & Văn viết)",
        "confusable_pairs": [
            {
                "rival_pattern": "N + に比べて vs N + によって vs N + に対して",
                "difference_vi": "に比べて = đặt A cạnh B để so sánh hơn/kém/khác nhau; によって = dựa theo tiêu chí để phân loại/tùy thuộc; に対して = đối lập tương phản hoặc hướng vào đối tượng.",
                "quick_test_vi": "Thấy cặp so sánh quá khứ-hiện tại (昔に比べて) hoặc tăng/giảm hơn năm ngoái -> に比べて.",
            }
        ],
        "examples": [
            {
                "jp": "昔にくらべて、現在は生活がずっと便利になった。",
                "reading_note": "むかしにくらべて、げんざいはせいかつがずっとべんりになった。",
                "vi": "So với ngày xưa, hiện nay cuộc sống đã trở nên tiện lợi hơn hẳn.",
                "grammar_note": "Q#136: 昔 + にくらべて đối chiếu 2 mốc thời gian.",
            },
            {
                "jp": "兄に比べて、弟のほうが背が高い。",
                "reading_note": "あににくらべて、おとうとのほうがせがたかい。",
                "vi": "So với người anh thì người em cao hơn.",
                "grammar_note": "So sánh trực tiếp giữa hai đối tượng.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 | Đề .xlsx (Q16, Q136)",
        "search_keywords": "ni kurabete so voi doi chieu に比べて にくらべて",
        "match_patterns": ["に比べて", "にくらべて"],
    },
    {
        "code": "GP-N3-107",
        "pattern": "～ずにはいられない / ～ずに（は） (Không thể kìm nén / Mà không làm)",
        "jlpt_level": "N3",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": True,
        "formation_formula": "V(cột あ) + ずにはいられない (Không thể nhịn được) | V(cột あ) + ずに (Mà không làm - trang trọng của ないで) [Ngoại lệ: する -> せず]",
        "formation_table": [
            {"pos": "1. Chia thể ず (Vない bỏ ない + ず)", "rule": "言う->言わず (Q#122), 気にする->気にせず (Passage 1), 悪くなる->悪くならず (Q#147), する->せず"},
            {"pos": "2. ～ずに (Mà không làm V1 để làm V2)", "rule": "うそを言わず、本音で話し合いたい (Q#122); においを気にせず使用できます (Passage 1)"},
            {"pos": "3. ～ずにはいられない (Cảm xúc không kìm nổi)", "rule": "Tự động nảy sinh cảm xúc/hành động không kìm nén được (笑わずにはいられない, 心配せずにはいられない)"},
        ],
        "core_meaning_vi": "Làm V2 mà không làm V1 (～ずに, dạng trang trọng của ～ないで), hoặc không thể kiềm chế bản thân không làm V (～ずにはいられない)",
        "deep_explanation_vi": (
            "Đây là mẫu xuất hiện ở cả dạng thực chiến lẫn bẫy đề thi: "
            "1) Dạng ～ず / ～ずに gặp trong Passage 1 ('においを気にせず使用できます') và Q#122 ('うそを言わず、本音で話し合いたい'). Nhớ ngoại lệ する -> せず! "
            "2) Dạng ～ずにはいられない làm phương án nhiễu ở Bài Đục lỗ 1 Câu [5] (Q#147: '症状が [悪くなるおそれがあります]', loại '悪くならずにはいられません'). Lý do loại cực rõ ràng: ずにはいられない CHỈ dùng cho cảm xúc/hành động tự nhiên của CON NGƯỜI ('không thể nhịn cười / không thể không lo'), tuyệt đối không dùng cho 'triệu chứng bệnh' (症状)!"
        ),
        "register_tag": "Văn viết & Biểu cảm nội tâm",
        "confusable_pairs": [
            {
                "rival_pattern": "Vずにはいられない vs Vるおそれがある vs Vずに",
                "difference_vi": "ずにはいられない chỉ dùng cho cảm xúc/phản ứng tâm lý của con người ('không nhịn được'); おそれがある dùng cho cảnh báo rủi ro khách quan; ずに là 'mà không làm' (= ないで).",
                "quick_test_vi": "Chủ ngữ là vật/triệu chứng (症状が)? Loại ngay ずにはいられない!",
            }
        ],
        "examples": [
            {
                "jp": "無香料なので、においを気にせず使用できます。",
                "reading_note": "むこうりょうなので、においをきにせずしようできます。",
                "vi": "Vì không chứa hương liệu nên có thể sử dụng mà không cần bận tâm về mùi.",
                "grammar_note": "Passage 1: 気にする -> 気にせず (= 気にしないで).",
            },
            {
                "jp": "うそを言わず、本音で話し合いたい。",
                "reading_note": "うそをいわず、ほんねではなしあいたい。",
                "vi": "Tôi muốn không nói dối mà trao đổi thẳng thắn bằng lời thật lòng.",
                "grammar_note": "Q#122: 言う -> 言わず.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 | Đề .xlsx (Q122, Q147, Passage 1)",
        "search_keywords": "zu ni zu ni wa irarenai ma khong khong kim nen ずに せず ずにはいられない",
        "match_patterns": ["ずにはいられ", "気にせず", "を言わず", "せずに"],
    },
    {
        "code": "GP-N3-108",
        "pattern": "～のみだ / ～のみならず (Chỉ có / Không chỉ)",
        "jlpt_level": "N3",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": True,
        "formation_formula": "N / Vる + のみだ (Văn viết của だけだ) | 普通形 / N + のみならず (Không chỉ... mà còn)",
        "formation_table": [
            {"pos": "1. N / Vる + のみだ", "rule": "Giới hạn trang trọng: chỉ có N hoặc chỉ còn làm V (Cấm gắn sau Vて! Ví dụ *寝てのみだ ở Q#55 là sai)"},
            {"pos": "2. ～のみならず", "rule": "Phiên bản văn viết của ～だけでなく (国内のみならず海外でも)"},
        ],
        "core_meaning_vi": "Chỉ giới hạn ở N/V (のみだ - trang trọng của だけ) hoặc mở rộng 'không chỉ... mà còn' (のみならず)",
        "deep_explanation_vi": (
            "Xuất hiện làm phương án nhiễu ở Q#55 ('毎日寝て [ばかりいる]', loại 'のみだ'). "
            "Hai lý do loại ở Q#55: 1) Về hình thái, のみ không gắn sau thể て (寝て), chỉ gắn sau Danh từ hoặc Vる. 2) Về nghĩa, のみ mang sắc thái trang trọng khách quan ('chỉ còn cách chờ kết quả mà thôi'), không dùng để phàn nàn thói quen ngủ suốt ngày."
        ),
        "register_tag": "Văn viết trang trọng",
        "confusable_pairs": [
            {
                "rival_pattern": "Vる/N + のみだ vs Vて + ばかりいる",
                "difference_vi": "のみだ gắn sau Vる/N trong văn viết; ばかりいる gắn sau Vて để diễn tả hành động lặp đi lặp lại.",
                "quick_test_vi": "Sau Vて (寝て___ trong Q#55) -> loại のみだ!",
            }
        ],
        "examples": [
            {
                "jp": "あとは試験の結果を待つのみだ。",
                "reading_note": "あとはしけんのけっかをまつのみだ。",
                "vi": "Giờ chỉ còn mỗi việc chờ đợi kết quả kỳ thi thôi.",
                "grammar_note": "Vる (待つ) + のみだ trong văn viết.",
            },
            {
                "jp": "マグロは日本のみならず海外でも人気が高い。",
                "reading_note": "まぐろはにほんのみならずかいがいでもにんきがたかい。",
                "vi": "Cá ngừ được ưa chuộng không chỉ ở Nhật Bản mà cả ở nước ngoài.",
                "grammar_note": "N + のみならず = だけでなく.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 | Đề .xlsx (Q55, Passage 4)",
        "search_keywords": "nomi da nomi narazu chi co khong chi のみだ のみならず",
        "match_patterns": ["のみだ", "のみならず"],
    },
    {
        "code": "GP-N3-109",
        "pattern": "～だけ / ～だけです / ～だけでは (Chỉ giới hạn ở mức...)",
        "jlpt_level": "N3",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": True,
        "formation_formula": "V普通形 / Aい / Aな+な / N + だけ（だ・です・でなく）",
        "formation_table": [
            {"pos": "Giới hạn cuối câu (Q#26)", "rule": "日本文化に関することだけです = chỉ giới hạn ở những điều liên quan văn hóa Nhật thôi"},
            {"pos": "Bẫy giới hạn N3 (Q#150)", "rule": "Vる + だけです (chỉ có V thôi — không diễn tả tiến trình biến đổi dần như つつあります)"},
            {"pos": "Không chỉ... (Q#101)", "rule": "デザインだけではなく / だけでなく"},
        ],
        "core_meaning_vi": "Giới hạn phạm vi duy nhất ở mức độ hay đối tượng đã nêu ('chỉ... thôi', 'không chỉ...')",
        "deep_explanation_vi": (
            "～だけ xuất hiện ở nhiều dạng câu hỏi trong đề thi: vừa là đáp án chuẩn ở Q#26 ('ことだけです'), vừa là phương án nhiễu ở Q#52 (đối lập với こそ), Q#150 (減るだけです vs 減りつつあります), và Q#157 (考え方 [こそ] が vs だけ). "
            "Lưu ý quy tắc phân biệt: khi muốn nhấn mạnh ĐÂY LÀ YẾU TỐ CỐT LÕI QUAN TRỌNG (Q#52, Q#157) dùng こそ, còn muốn thu hẹp giới hạn bình thường ('chỉ là điều liên quan văn hóa Nhật thôi' - Q#26) dùng だけ."
        ),
        "register_tag": "Trung tính",
        "confusable_pairs": [
            {
                "rival_pattern": "～だけです vs ～こそ vs ～つつあります",
                "difference_vi": "だけです giới hạn phạm vi 'chỉ thế thôi'; こそ nhấn mạnh khẳng định giá trị 'chính là'; つつあります mô tả quá trình đang diễn biến dần dần.",
                "quick_test_vi": "Có mẫu đối lập 'không phải cái gì cũng được, mà chỉ là X thôi' (Q#26) -> だけです.",
            }
        ],
        "examples": [
            {
                "jp": "スピーチのテーマは何でもいいというわけではなく日本文化に関することだけです。",
                "reading_note": "すぴーちのてーまはなんでもいいというわけではなくにほんぶんかにかんすることだけです。",
                "vi": "Chủ đề phát biểu không phải cái gì cũng được, mà chỉ là những nội dung liên quan đến văn hóa Nhật thôi.",
                "grammar_note": "Q#26: Chốt phạm vi giới hạn bằng ことだけです.",
            },
            {
                "jp": "この車は、デザインだけではなく性能がとてもよい。",
                "reading_note": "このくるまは、でざいんだけではなくせいのうがとてもよい。",
                "vi": "Chiếc xe này không chỉ có thiết kế mà tính năng cũng rất tốt.",
                "grammar_note": "Q#101: だけではなく mở rộng sang mặt thứ hai.",
            },
        ],
        "source_ref": "Đề .xlsx (Q26, Q52, Q101, Q150, Q157)",
        "search_keywords": "dake dakedesu dake de wa naku chi gioi han だけです だけ だけではなく",
        "match_patterns": ["だけです", "だけではなく", "だけでなく"],
    },
    {
        "code": "GP-N3-110",
        "pattern": "～てもかまわない (Dù có... cũng không sao / không vấn đề gì)",
        "jlpt_level": "N3",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": True,
        "formation_formula": "Vて / Aくて / Aなで / Nで + もかまわない / もかまいません",
        "formation_table": [
            {"pos": "Cho phép / Chấp nhận nhẹ", "rule": "雑誌や漫画でもかまいません (Passage 7 = tạp chí hay truyện tranh cũng không sao/được cả)"},
            {"pos": "Bẫy logic (Q#150)", "rule": "減ってもかまいません = có giảm đi cũng không sao (bị loại vì trái logic khách quan mô tả xu hướng thực tế)"},
        ],
        "core_meaning_vi": "Cho phép hoặc chấp nhận một tình huống/đối tượng ('dù là... cũng không sao, không thành vấn đề')",
        "deep_explanation_vi": (
            "Xuất hiện thực tế trong tờ rơi Đọc hiểu Passage 7 ('なお、古本は雑誌や漫画でもかまいません' = ngoài ra sách cũ là tạp chí hay truyện tranh cũng được/không sao cả) và làm bẫy ở Q#150 ('和室が [減りつつあります]', loại '減ってもかまいません'). "
            "Đây là cách cho phép lịch sự hơn ～てもいいです, rất hay gặp trong thông báo quy định điều kiện linh hoạt."
        ),
        "register_tag": "Trung tính & Lịch sự (Thông báo / Hội thoại)",
        "confusable_pairs": [
            {
                "rival_pattern": "～てもかまわない vs ～てもいい vs ～つつある",
                "difference_vi": "てもかまわない = chấp nhận cho phép ('có thế cũng chẳng sao'); てもいい = được phép; つつある = xu hướng đang xảy ra dần dần.",
                "quick_test_vi": "Thông báo cho phép ngoại lệ nhẹ (tạp chí hay truyện tranh cũng nhận) -> でもかまいません.",
            }
        ],
        "examples": [
            {
                "jp": "なお、古本は雑誌や漫画でもかまいません。",
                "reading_note": "なお、ふるほんはざっしやまんがでもかまいません。",
                "vi": "Ngoài ra, sách cũ có là tạp chí hay truyện tranh cũng không sao (đều nhận).",
                "grammar_note": "Passage 7: N + でもかまいません.",
            },
            {
                "jp": "ペンは黒でも青でもかまいません。",
                "reading_note": "ぺんはくろでもあおでもかまいません。",
                "vi": "Bút màu đen hay màu xanh đều được không sao cả.",
                "grammar_note": "Cho phép chọn lựa thoải mái.",
            },
        ],
        "source_ref": "Đề .xlsx (Q150, Passage 7)",
        "search_keywords": "temo kamawanai demo kamawanai cung khong sao てもかまいません でもかまいません",
        "match_patterns": ["てもかまい", "でもかまい"],
    },
    {
        "code": "GP-N3-111",
        "pattern": "～てきた / ～られてきた (Đã và đang từ quá khứ đến hiện tại)",
        "jlpt_level": "N3",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": True,
        "formation_formula": "Vて / V(bị động)て + きた / きました",
        "formation_table": [
            {"pos": "Chủ động tiếp diễn", "rule": "Vて + きた / きました (言われてきた - Q#22; 見て育ってきた - Passage 13)"},
            {"pos": "Bị động tiếp diễn (Q#148)", "rule": "V(bị động)て + きた / きました (昔からつくられてきました = đã và đang được xây dựng từ xưa tới nay)"},
        ],
        "core_meaning_vi": "Diễn tả một truyền thống, hành động hay hiện tượng bắt đầu từ quá khứ và liên tục kéo dài/lặp lại cho đến tận hiện tại",
        "deep_explanation_vi": (
            "Đây là trục ngữ pháp cốt lõi trong Bài Đục lỗ 2 Câu [1] (Q#148: '日本では昔からこの気候に合わせた家が [つくられてきました]') và Câu Sao ★ Q#22 ('子どものころから... [と言われてきた]'). "
            "Nhờ cụm từ khóa thời gian quá khứ kéo dài đến nay ('昔から', '子どものころから'), ta phân biệt ngay được: "
            "1) Nếu chỉ dùng quá khứ đơn (つくられました) -> mất sắc thái kéo dài liên tục tới hiện tại. "
            "2) Nếu chủ ngữ là vật đi với が (家が) -> động từ phải kết hợp thể BỊ ĐỘNG + てきた (つくられてきました), không dùng てあります hay ておきました."
        ),
        "register_tag": "Trung tính & Văn viết",
        "confusable_pairs": [
            {
                "rival_pattern": "Vられてきた vs Vられました vs Vてある",
                "difference_vi": "られてきた = quá trình được duy trì liên tục từ quá khứ đến hiện tại; られました = sự kiện đã chấm dứt trong quá khứ; てある = trạng thái tĩnh hiện hữu.",
                "quick_test_vi": "Thấy 昔から / 子どものころから + bị động -> chọn られてきた!",
            }
        ],
        "examples": [
            {
                "jp": "日本では昔からこの気候に合わせた家がつくられてきました。",
                "reading_note": "にほんではむかしからこのきこうにあわせたいえがつくられてきました。",
                "vi": "Ở Nhật Bản, từ xưa đến nay những ngôi nhà phù hợp với khí hậu này đã và đang được xây dựng.",
                "grammar_note": "Q#148: 昔から + 家が + bị động つくられる + てきました.",
            },
            {
                "jp": "子どものころから、周りのことを考えて行動するようにと言われてきた。",
                "reading_note": "こどものころから、まわりのことをかんがえてこうどうするようにといわれてきた。",
                "vi": "Từ hồi nhỏ đến giờ tôi luôn được dặn dò phải nghĩ cho xung quanh rồi mới hành động.",
                "grammar_note": "Q#22: 子どものころから + 言われてきた.",
            },
        ],
        "source_ref": "Đề .xlsx (Q22, Q148, Passage 13)",
        "search_keywords": "rarete kita te kita tu xua den nay られてきた られてきました てきた",
        "match_patterns": ["られてきた", "られてきました", "れてきた"],
    },
    {
        "code": "GP-N3-112",
        "pattern": "～ていく / ～られていく (Sẽ tiếp tục hướng tới tương lai)",
        "jlpt_level": "N3",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": True,
        "formation_formula": "Vて / V(bị động)て + いく (+ でしょう / だろう)",
        "formation_table": [
            {"pos": "Bị động hướng tương lai (Q#152)", "rule": "V(bị động)て + いく + でしょう (これからの日本の家に使われていくでしょう)"},
            {"pos": "Chủ động hướng tương lai", "rule": "Vて + いく (これからも努力していく, 減っていきそうだ)"},
        ],
        "core_meaning_vi": "Diễn tả hành động hoặc tình trạng sẽ tiếp tục được duy trì, phát triển từ hiện tại hướng về tương lai",
        "deep_explanation_vi": (
            "Thi trực tiếp ở Bài Đục lỗ 2 Câu [5] (Q#152: 'よく合っていますから、これからの日本の家に [使われていくでしょう]'). "
            "Khi thấy từ khóa tương lai 'これからの' (từ nay về sau) kết hợp đánh giá tích cực ở vế trước ('rất phù hợp với lối sống hiện đại'), "
            "ta loại ngay các phương án ngược chiều thời gian ('増えてきました' là quá khứ -> hiện tại) và phương án ngược nghĩa ('減っていきそうです' / '見られなくなるはずです')."
        ),
        "register_tag": "Trung tính & Văn viết dự báo",
        "confusable_pairs": [
            {
                "rival_pattern": "Vられていくでしょう vs Vてきました",
                "difference_vi": "ていく hướng TỪ HIỆN TẠI -> TƯƠNG LAI (これからの); てきた hướng TỪ QUÁ KHỨ -> HIỆN TẠI (昔から).",
                "quick_test_vi": "Thấy これからの / 今後 / 将来 -> ていく; thấy 昔から / 今まで -> てきた.",
            }
        ],
        "examples": [
            {
                "jp": "緑のカーテンは現代日本人の暮らし方によく合っていますから、これからの日本の家に使われていくでしょう。",
                "reading_note": "みどりのかーてんはげんだいにほんじんのくらしかたによくあっていますから、これからのにほんのいえにつかわれていくでしょう。",
                "vi": "Vì rèm xanh rất hợp với lối sống người Nhật hiện đại nên từ nay về sau chắc sẽ tiếp tục được sử dụng trong các ngôi nhà Nhật.",
                "grammar_note": "Q#152: これからの + bị động 使われる + ていく + でしょう.",
            },
            {
                "jp": "これからも地域のみんなで自然を守り育てていきたい。",
                "reading_note": "これからもちいきのみんなでしぜんをまもりそだてていきたい。",
                "vi": "Từ nay về sau tôi muốn cùng mọi người trong khu vực tiếp tục bảo vệ và vun trồng thiên nhiên.",
                "grammar_note": "これからの + ていきたい.",
            },
        ],
        "source_ref": "Đề .xlsx (Q152, Passage 18)",
        "search_keywords": "rarete iku te iku tuong lai sap toi られていく 使われていく いくでしょう",
        "match_patterns": ["られていく", "れていく", "ていくでしょう"],
    },
    {
        "code": "GP-N3-113",
        "pattern": "～のを / ～ことが (Danh từ hóa mệnh đề khớp với Tha/Tự động từ)",
        "jlpt_level": "N3",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": True,
        "formation_formula": "Vる / Vない + の + を + [Tha động từ] | Vる + こと/の + が + [Tự động từ / Tính từ]",
        "formation_table": [
            {"pos": "Đi với Tha động từ (防ぐ・忘れる・見る・聞く・手伝う)", "rule": "BẮT BUỘC dùng のを (部屋の中に入るのを防ぎます - Q#149; 入力するのを忘れて - Passage 8)"},
            {"pos": "Đi với Tính từ / Tự động từ (大事だ・必要だ・わかる)", "rule": "Dùng ことが / のが (座ることが多くなりました; 笑えないのがくやしかった - Q#155)"},
        ],
        "core_meaning_vi": "Kết hợp danh từ hóa mệnh đề (の/こと) với đúng trợ từ (を hoặc が) tương thích với động từ chính của câu",
        "deep_explanation_vi": (
            "Thi trực tiếp ở Bài Đục lỗ 2 Câu [2] (Q#149: '冷たい空気が部屋の中に入る [のを] 防ぎます'). "
            "Chiến thuật giải 5 giây: nhìn ngay động từ đứng sau chỗ trống! "
            "Ở Q#149 là tha động từ 防ぎます ('ngăn chặn cái gì đó' -> ～を防ぐ), nên buộc phải chọn trợ từ を (のを). "
            "Các phương án nhiễu đều gãy ngay: ことが (sai trợ từ が cho tha động từ 防ぐ), とか (liệt kê ví dụ), ものを (chỉ vật thể cụ thể hoặc sắc thái than thở cuối câu, không dùng danh từ hóa hành động vào phòng)."
        ),
        "register_tag": "Trung tính & Văn viết",
        "confusable_pairs": [
            {
                "rival_pattern": "Vる + のを + 防ぐ vs Vる + ことが vs Vる + ものを",
                "difference_vi": "のを nối mệnh đề làm TÂN NGỮ trực tiếp cho tha động từ (防ぐ・忘れる・待つ); ことが làm CHỦ NGỮ cho tự động từ/tính từ; ものを chỉ đồ vật hữu hình.",
                "quick_test_vi": "Động từ sau là tha động từ (防ぐ, 止める, 忘れる, 手伝う) -> chọn のを!",
            }
        ],
        "examples": [
            {
                "jp": "和紙は冬には冷たい空気が部屋の中に入るのを防ぎます。",
                "reading_note": "わしはふゆにはつめたいくうきがへやのなかにはいるのをふせぎます。",
                "vi": "Giấy Washi vào mùa đông giúp ngăn việc không khí lạnh lọt vào trong phòng.",
                "grammar_note": "Q#149: Mệnh đề 入る danh từ hóa bằng のを cho tha động từ 防ぐ.",
            },
            {
                "jp": "外国人が言った冗談がわからないせいで、自分だけ笑えないのがくやしかった。",
                "reading_note": "がいこくじんがいったじょうだんがわからないせいで、じぶんだけわらえないのがくやしかった。",
                "vi": "Tại không hiểu câu đùa của người nước ngoài nên việc chỉ mình không cười được làm tôi ấm ức.",
                "grammar_note": "Passage 19: 笑えない + の + が làm chủ ngữ cho tính từ くやしかった.",
            },
        ],
        "source_ref": "Đề .xlsx (Q149, Passages 8, 18, 19)",
        "search_keywords": "no wo koto ga danh tu hoa menh de tha dong tu のを ことが 防ぎます",
        "match_patterns": ["入るのを", "するのを", "ないのが"],
    },
    {
        "code": "GP-N3-114",
        "pattern": "～た結果 / ～た末に (Kết quả sau quá trình...)",
        "jlpt_level": "N3",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": True,
        "formation_formula": "Vた / N + の + 結果（けっか） | Vた / N + の + 末に（すえに）",
        "formation_table": [
            {"pos": "～た結果 (Trung tính khách quan)", "rule": "Sau quá trình khảo sát/nỗ lực/thảo luận (努力した結果, 調査した結果; その結果 - Passage 4)"},
            {"pos": "～た末に (Gian truân trăn trở)", "rule": "Sau nhiều gian khổ, đắn đo rất lâu mới ra kết quả cuối cùng (いろいろ考えた末に)"},
        ],
        "core_meaning_vi": "Chỉ kết quả tự nhiên sau một quá trình kéo dài (～た結果) hoặc kết cục sau nhiều trăn trở, gian nan (～た末に)",
        "deep_explanation_vi": (
            "Mẫu này được học trong 03_Grammar/Group_04 (た結果_けっか.md) và xuất hiện ở dạng liên từ đầu câu 'その結果' trong Passage 4 ('マグロは大量に捕られるようになった。その結果、新しく生まれるマグロの子どもの数が減り...') và danh từ '調査結果' trong Passage 3. "
            "Lưu ý: cả hai mẫu đều dùng thì quá khứ Vた hoặc Danh từ + の ở phía trước."
        ),
        "register_tag": "Văn viết & Báo cáo",
        "confusable_pairs": [
            {
                "rival_pattern": "Vた + 結果 vs Vた + 末に",
                "difference_vi": "結果 trình bày kết quả khách quan (sau khảo sát, nghiên cứu, nỗ lực); 末に nhấn mạnh quá trình vất vả, suy nghĩ trăn trở rất lâu trước kết luận cuối.",
                "quick_test_vi": "Thấy 'khảo sát / nghiên cứu / thảo luận' khách quan -> 結果; thấy 'suy nghĩ mãi / tranh cãi gay gắt mãi' -> 末に.",
            }
        ],
        "examples": [
            {
                "jp": "大量に捕られるようになった。その結果、新しく生まれるマグロの子どもの数が減っている。",
                "reading_note": "たいりょうにとられるようになった。そのけっか、あたらしくうまれるまぐろのこどものかずがへっている。",
                "vi": "Cá ngừ bị đánh bắt số lượng lớn. Kết quả là số lượng cá con mới sinh cũng giảm đi.",
                "grammar_note": "Passage 4: Liên từ その結果 nối hệ quả trực tiếp.",
            },
            {
                "jp": "努力した結果、初めはできなかったことが、できるようになった。",
                "reading_note": "どりょくしたけっか、はじめはできなかったことが、できるようになった。",
                "vi": "Kết quả sau khi nỗ lực, việc lúc đầu không làm được nay đã có thể làm được.",
                "grammar_note": "03_Grammar/Group_04: Vた (努力した) + 結果.",
            },
        ],
        "source_ref": "03_Grammar/Group_04 | Đề .xlsx (Passages 3, 4)",
        "search_keywords": "ta kekka ta sue ni ket qua sau qua trinh た結果 その結果 た末に",
        "match_patterns": ["その結果", "た結果", "た末に", "の結果"],
    },
    {
        "code": "GP-N3-115",
        "pattern": "Liên từ mạch văn: つまり・たとえば・そのため・それでも・なぜなら・それとも",
        "jlpt_level": "N3",
        "category": "discourse",
        "category_label_vi": CATEGORY_LABELS["discourse"],
        "in_exam_corpus": True,
        "formation_formula": "[Câu 1]。Liên từ、[Câu 2]。",
        "formation_table": [
            {"pos": "つまり (Tức là / Nói cách khác)", "rule": "Diễn giải lại khái niệm/tóm tắt ý (おおみそか、つまり一年の最後の日 - Q#49)"},
            {"pos": "たとえば (Ví dụ như)", "rule": "Đưa ví dụ số liệu/tình huống cụ thể minh họa quy tắc (たとえば、顔は2週間以内 - Q#146)"},
            {"pos": "そのため (Vì thế / Do đó)", "rule": "Nhân quả trực tiếp giữa 2 câu (月は同じ面を向けている。そのため模様も同じ - Q#62)"},
            {"pos": "それでも (Dù vậy vẫn) / それとも (Hay là)", "rule": "それでも = nhượng bộ (vẫn không giải quyết được - Passage 17); それとも = câu hỏi lựa chọn"},
            {"pos": "なぜなら (Bởi vì) / なお (Ngoài ra lưu ý)", "rule": "なぜなら giải thích lý do phía sau; なお bổ sung điều kiện phụ trong thông báo (Passage 7)"},
        ],
        "core_meaning_vi": "Hệ thống liên từ chuyển ý chuẩn xác trong mạch văn Đọc hiểu & Đục lỗ 問題3",
        "deep_explanation_vi": (
            "Đây là nhóm liên từ quyết định trực tiếp 4 câu hỏi thi thật (Q#29, Q#49, Q#62, Q#146) và xuyên suốt 22 đoạn văn đọc hiểu! "
            "Phân biệt 2 cặp bẫy kinh điển nhất: "
            "1) つまり (đúc kết/định nghĩa lại CÙNG MỘT ĐỐI TƯỢNG, Q#49) vs たとえば (lấy một vài ví dụ CỤ THỂ NHỎ HƠN để minh họa quy tắc chung, Q#146). "
            "2) そのため (vì lý do vừa nêu ở câu trước -> kết quả thuận chiều, Q#62) vs それでも (dù như thế đi nữa nhưng vẫn..., Passage 17: 'それでも解決しない場合は')."
        ),
        "register_tag": "Trung tính & Văn viết mạch lạc",
        "confusable_pairs": [
            {
                "rival_pattern": "つまり vs たとえば vs そのため vs それでも",
                "difference_vi": "つまり = nói cách khác/tóm lại; たとえば = ví dụ cụ thể; そのため = do đó (nhân quả); それでも = dù vậy vẫn (nhượng bộ).",
                "quick_test_vi": "Câu sau nêu con số/tình huống con minh họa (2 tuần/Nam Âu) -> たとえば; giải thích lại 1 từ -> つまり; kết quả logic thuận -> そのため.",
            }
        ],
        "examples": [
            {
                "jp": "今日はおおみそか、つまり一年の最後の日です。",
                "reading_note": "きょうはおおみそか、つまりいちねんのさいごのひです。",
                "vi": "Hôm nay là đêm giao thừa Omisoka, tức là ngày cuối cùng của năm.",
                "grammar_note": "Q#49: つまり diễn giải lại khái niệm おおみそか.",
            },
            {
                "jp": "同じところに続けて長く使用しないでください。たとえば、顔は2週間以内にしてください。",
                "reading_note": "おなじところにつづけてながくしようしないでください。たとえば、かおはにしゅうかんいないにしてください。",
                "vi": "Đừng dùng liên tục ở một chỗ quá lâu. Ví dụ như vùng mặt chỉ dùng trong vòng 2 tuần trở lại.",
                "grammar_note": "Q#146: たとえば đưa ví dụ cụ thể cho quy tắc chung.",
            },
        ],
        "source_ref": "Đề .xlsx (Q29, Q49, Q62, Q146, Passages 1, 5, 7, 17)",
        "search_keywords": "lien tu tsumari tatoeba sono tame soredemo nazenara soretomo つまり たとえば そのため それでも なぜなら それとも",
        "match_patterns": ["つまり", "たとえば", "例えば", "そのため", "それでも", "なぜなら", "それとも", "なお、"],
    },
    {
        "code": "GP-N3-116",
        "pattern": "～的（な） (Mang tính chất... - Hậu tố tạo tính từ từ danh từ Hán-Nhật)",
        "jlpt_level": "N3",
        "category": "conjugation",
        "category_label_vi": CATEGORY_LABELS["conjugation"],
        "in_exam_corpus": True,
        "formation_formula": "N(Danh từ Hán-Nhật 2 chữ) + 的だ / 的な + N / 的に + V",
        "formation_table": [
            {"pos": "Tính từ đuôi な", "rule": "国際的な決まり (Passage 4), 否定的・肯定的 (Q#129), 消極的・積極的 (Q#94)"},
            {"pos": "Phó từ hóa", "rule": "N + 的に (具体的に = một cách cụ thể, 徹底的に = triệt để)"},
            {"pos": "Giới hạn kết hợp (Q#61)", "rule": "KHÔNG bao giờ gắn 的 vào tính từ thuần Nhật bỏ い như *黒的な!"},
        ],
        "core_meaning_vi": "Biến danh từ Hán-Nhật 2 chữ thành tính từ đuôi な diễn tả 'mang tính chất...', 'thuộc về...'",
        "deep_explanation_vi": (
            "Hậu tố 的 (てき) xuất hiện rộng khắp từ vựng và đọc hiểu N3 (国際的な, 否定的, 肯定的, 積極的, 消極的). "
            "Trong Q#61 ('月にある黒 [っぽい] 模様'), phương án 的な là bẫy sai hình thái vì trước chỗ trống là gốc tính từ thuần Nhật 黒 (くろ), không phải danh từ Hán-Nhật hai âm!"
        ),
        "register_tag": "Văn viết & Từ Hán-Nhật",
        "confusable_pairs": [
            {
                "rival_pattern": "N(Hán-Nhật) + 的な vs Aい(bỏ い) + っぽい",
                "difference_vi": "的な chỉ gắn vào Danh từ (đa số Hán-Nhật 2 chữ như 国際的, 肯定的); っぽい gắn vào gốc tính từ thuần Nhật bỏ い (黒っぽい), Vます hoặc danh từ đời thường.",
                "quick_test_vi": "Gặp gốc màu sắc thuần Nhật 黒 (Q#61) -> loại 的な ngay!",
            }
        ],
        "examples": [
            {
                "jp": "マグロを捕ってもいい量を国ごとに定めた国際的な決まりがある。",
                "reading_note": "まぐろをとってもいいりょうをくにごとにさだめたこくさいてきなきまりがある。",
                "vi": "Có quy định mang tính quốc tế ấn định sản lượng cá ngừ được phép bắt theo từng nước.",
                "grammar_note": "Passage 4: Danh từ 国際 + 的な + 決まり.",
            },
            {
                "jp": "彼の考え方は、いつもネガティブ（否定的）だ。",
                "reading_note": "かれのかんがえかたは、いつもひていてきだ。",
                "vi": "Cách suy nghĩ của anh ấy lúc nào cũng mang tính tiêu cực (phủ định).",
                "grammar_note": "Q#129: 否定 + 的だ.",
            },
        ],
        "source_ref": "Somatome N3 | Đề .xlsx (Q61, Q94, Q129, Passage 4)",
        "search_keywords": "teki teki na teki ni hau to tinh tu han nhat 的 的な 的に 国際的 否定的",
        "match_patterns": ["的な", "的に", "的だ"],
    },
    {
        "code": "GP-N3-117",
        "pattern": "～と思えば / ～と思ったら (Vừa mới tưởng là... thì lại trái ngược)",
        "jlpt_level": "N3",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": True,
        "formation_formula": "普通形(Vた/Aかった/Nだ) + と思えば / と思ったら / と思っていたら",
        "formation_table": [
            {"pos": "1. Thay đổi nhanh bất ngờ", "rule": "Vừa mới A xong đã chuyển ngay sang B trái ngược (さっきまで晴れていたと思えば、急に雨が降り出した)"},
            {"pos": "2. Thực tế khác tưởng tượng (Passage 14)", "rule": "～と思っていたら、… (Tôi cứ tưởng bà cụ 70 tuổi sẽ lên tàu, ai ngờ là cô gái 30 tuổi)"},
            {"pos": "Bẫy Q#54", "rule": "場所の便利さ [と思えば] bị loại vì と思えば đi sau mệnh đề câu nhận định chứ không gắn trực tiếp vào danh từ tiêu chí"},
        ],
        "core_meaning_vi": "Diễn tả sự chuyển biến bất ngờ ngay sau khi vừa nghĩ/vừa thấy một trạng thái (hoặc sự thật trái với dự đoán)",
        "deep_explanation_vi": (
            "Trong Passage 14 ('70才ぐらいのおばあさんが来るのだろうと思っていたら、30代の女性が乗ってきた'), ～と思っていたら mô tả cú sốc khi thực tế khác hẳn dự đoán trong đầu. "
            "Còn trong Q#54 ('場所の便利さ [からいうと]'), と思えば bị loại vì 場所の便利さ là danh từ thiếu vị ngữ mệnh đề và ngữ cảnh đang chọn khách sạn theo tiêu chí chứ không phải ngạc nhiên thay đổi."
        ),
        "register_tag": "Trung tính (Kể chuyện & Hội thoại)",
        "confusable_pairs": [
            {
                "rival_pattern": "普通形 + と思えば / と思ったら vs N + からいうと",
                "difference_vi": "と思えば/と思ったら gắn sau mệnh đề hoàn chỉnh diễn tả sự biến đổi bất ngờ; からいうと gắn sau danh từ tiêu chí để đưa ra kết luận gợi ý.",
                "quick_test_vi": "Thấy đứng sau danh từ tiêu chí không phải mệnh đề (場所の便利さ trong Q#54) -> loại と思えば.",
            }
        ],
        "examples": [
            {
                "jp": "70才ぐらいのおばあさんが来るのだろうと思っていたら、30代の女性が乗ってきた。",
                "reading_note": "ななじゅっさいぐらいのおばあさんがくるのだろうとおもっていたら、さんじゅうだいのじょせいがのってきた。",
                "vi": "Tôi cứ tưởng bà cụ tầm 70 tuổi sẽ bước lên, ai ngờ lại là phụ nữ độ tuổi 30 bước lên.",
                "grammar_note": "Passage 14: と思っていたら tạo bước ngoặt bất ngờ.",
            },
            {
                "jp": "さっきまで泣いていたと思えば、もう元気に笑っている。",
                "reading_note": "さっきまでないていたとおもえば、もうげんきにわらっている。",
                "vi": "Vừa mới thấy khóc lúc nãy xong đã thấy cười tươi ngay được rồi.",
                "grammar_note": "Thay đổi trạng thái trái ngược nhanh chóng.",
            },
        ],
        "source_ref": "Đề .xlsx (Q54, Passage 14)",
        "search_keywords": "to omoeba to omottara vua tuong bat ngo と思えば と思ったら と思っていたら",
        "match_patterns": ["と思えば", "と思ったら", "と思っていたら"],
    },
    {
        "code": "GP-N3-118",
        "pattern": "Kính ngữ Thông báo & Email công việc (おVくださる / ごNいただく / いただく)",
        "jlpt_level": "N3",
        "category": "keigo",
        "category_label_vi": CATEGORY_LABELS["keigo"],
        "in_exam_corpus": True,
        "formation_formula": "お + Vます + くださる / ください | ご + N(Hán-Nhật) + いただく / ください | Vて + いただく",
        "formation_table": [
            {"pos": "Khi khách hàng hành động", "rule": "お買い上げくださり (đã mua giúp chúng tôi - Passage 17), ご協力くださる方 (những người hợp tác - Passage 7)"},
            {"pos": "Khi yêu cầu khách chuẩn bị thông tin", "rule": "ご連絡いただくときは (khi quý khách liên hệ - Passage 17), お使いのコンピューター名 (máy tính quý khách đang dùng)"},
            {"pos": "Động từ khiêm nhường đặc biệt", "rule": "見る -> 拝見する; 聞く/行く -> うかがう; 食べる/もらう -> いただく (Q#127: いただいた本 = sách được tặng)"},
        ],
        "core_meaning_vi": "Cách diễn đạt lịch sự chuẩn mực trong văn bản hướng dẫn khách hàng, thông báo sự kiện và email giao dịch N3",
        "deep_explanation_vi": (
            "Nâng cấp trực tiếp từ kính ngữ N4 lên ngữ cảnh thực tế của các bài Đọc hiểu thông báo/email N3 (Passages 6, 7, 17, Q#127). "
            "Khi đọc bài Passage 17 (hướng dẫn bảo hành USB), nắm được 'お買い上げくださり' = quý khách đã mua, 'お使いの' = quý khách đang dùng, 'ご連絡いただくときは' = khi quý khách liên hệ cho chúng tôi là hiểu chính xác đối tượng của văn bản là người ĐÃ MUA hàng (loại bẫy '買いたいとき' ở Q#145!)."
        ),
        "register_tag": "Kính ngữ / Email & Thông báo Khách hàng",
        "confusable_pairs": [
            {
                "rival_pattern": "お/ご〜くださる (Tôn kính) vs ご〜いただく (Khiêm nhường nhận sự hợp tác)",
                "difference_vi": "くださる lấy KHÁCH HÀNG làm chủ ngữ ('quý khách đã mua/hợp tác cho chúng tôi'); いただく lấy CHÚNG TÔI làm chủ ngữ ('chúng tôi được quý khách liên hệ/hợp tác').",
                "quick_test_vi": "Trong thông báo doanh nghiệp gửi khách hàng, cả お/ご〜くださる và ご〜いただく đều ám chỉ hành động do phía khách thực hiện!",
            }
        ],
        "examples": [
            {
                "jp": "この度はabc社のUSBメモリーをお買い上げくださり、ありがとうございます。",
                "reading_note": "このたびはえーびーしーしゃのゆーえすびーめもりーをおかいあげくださり、ありがとうございます。",
                "vi": "Chân thành cảm ơn quý khách lần này đã mua thẻ nhớ USB của công ty abc.",
                "grammar_note": "Passage 17: お買い上げくださり xác định người đọc là khách đã mua.",
            },
            {
                "jp": "いただいた本をさっそく読もうと思います。",
                "reading_note": "いただいたほんをさっそくよもうとおもいます。",
                "vi": "Tôi định sẽ đọc ngay cuốn sách vừa được tặng.",
                "grammar_note": "Q#127: いただく dùng khiêm nhường cho もらう.",
            },
        ],
        "source_ref": "Đề .xlsx (Q127, Q145, Passages 6, 7, 17)",
        "search_keywords": "keigo email thong bao kudasaru itadaku くださり いただく お使いの",
        "match_patterns": ["くださり", "くださる", "いただく", "いただいた"],
    },
])

# =========================================================================
# JLPT N2 BRIDGE EXTENSIONS (GP-N2-01 .. GP-N2-14)
# =========================================================================
GRAMMAR_POINTS_DATA.extend([
    {
        "code": "GP-N2-01",
        "pattern": "～ざるを得ない (Buộc phải làm, không còn cách nào khác)",
        "jlpt_level": "N2",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": False,
        "formation_formula": "Vない(bỏ ない) + ざるを得ない [Ngoại lệ: する -> せざるを得ない]",
        "formation_table": [
            {"pos": "Nhóm 1 & 2", "rule": "V(cột あ) + ざるを得ない (行かざるを得ない, 諦めざるを得ない, 認めざるを得ない)"},
            {"pos": "Nhóm 3 (Ngoại lệ bắt buộc)", "rule": "する -> せざるを得ない (中止せざるを得ない); 来る -> こざるを得ない"},
        ],
        "core_meaning_vi": "Dù bản thân không muốn nhưng hoàn cảnh bắt buộc nên không thể không làm ('đành buộc phải làm')",
        "deep_explanation_vi": (
            "Đây là dạng văn viết nâng cấp trực tiếp từ N3 ～ないわけにはいかない. "
            "Điểm bẫy hình thái số 1 ở kỳ thi N2 là động từ する: KHÔNG bao giờ chia thành *しざるを得ない mà BẮT BUỘC chia thành せざるを得ない (theo cổ ngữ せ)."
        ),
        "register_tag": "Văn viết & Báo chí trang trọng (N2)",
        "confusable_pairs": [
            {
                "rival_pattern": "～ざるを得ない (N2) vs ～ないわけにはいかない (N3)",
                "difference_vi": "Cùng mang nghĩa 'buộc phải làm', nhưng ～ざるを得ない mang sắc thái văn viết trang trọng, khách quan hơn (thường gặp trong thông báo, kinh tế, nghị luận).",
                "quick_test_vi": "Thấy gốc động từ cắt ない hoặc せ___ (する -> せ) + ざるを得ない -> chốt N2.",
            }
        ],
        "examples": [
            {
                "jp": "台風が近づいているため、明日のイベントは中止せざるを得ない。",
                "reading_note": "たいふうがちかづいているため、あしたのいべんとはちゅうしせざるをえない。",
                "vi": "Do bão đang tiến gần nên sự kiện ngày mai buộc phải hủy bỏ.",
                "grammar_note": "する -> せ + ざるを得ない (bất quy tắc quan trọng nhất).",
            },
            {
                "jp": "証拠がある以上、自分のミスを認めざるを得なかった。",
                "reading_note": "しょうこがあるいじょう、じぶんのみすをみとめざるをえなかった。",
                "vi": "Một khi đã có bằng chứng thì tôi buộc phải thừa nhận sai sót của mình.",
                "grammar_note": "認める -> 認め + ざるを得なかった.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 (N2 P2)",
        "search_keywords": "zaru wo enai buoc phai ざるを得ない せざるを得ない",
        "match_patterns": ["ざるを得ない", "ざるをえない", "せざるを得"],
    },
    {
        "code": "GP-N2-02",
        "pattern": "～かねない (Có nguy cơ dẫn tới hậu quả xấu)",
        "jlpt_level": "N2",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": False,
        "formation_formula": "Vます(bỏ ます) + かねない",
        "formation_table": [
            {"pos": "Động từ (Vます)", "rule": "Vます + かねない (事故を起こしかねない, 信頼を失いかねない, 誤解を招きかねない)"},
            {"pos": "Quy tắc ngữ dụng", "rule": "Dù mặt chữ có ない nhưng mang nghĩa KHẲNG ĐỊNH dự báo xấu ('rất có thể dẫn tới việc không hay')"},
        ],
        "core_meaning_vi": "Cảnh báo khả năng rất có thể xảy ra một hậu quả tiêu cực nếu cứ tiếp tục tình trạng hiện tại ('không khéo sẽ...')",
        "deep_explanation_vi": (
            "～かねない là cấp độ N2 nâng cấp từ N3 ～おそれがある. "
            "Bẫy dịch phổ biến ở người mới lên N2: thấy đuôi ない nên tưởng là phủ định ('không thể'), nhưng thực tế かねない có nghĩa là 'HOÀN TOÀN CÓ NGUY CƠ SẼ XẢY RA' (kết quả xấu)!"
        ),
        "register_tag": "Văn viết & Cảnh báo trang trọng (N2)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vます + かねない vs Vます + かねる vs ～おそれがある",
                "difference_vi": "かねない = có nguy cơ dẫn tới chuyện xấu (khẳng định rủi ro, gần nghĩa おそれがある); かねる = khó mà làm được (từ chối lịch sự).",
                "quick_test_vi": "Hậu quả tiêu cực (事故, 失敗, 病気) + cảnh báo 'nếu bất cẩn thì...' -> かねない.",
            }
        ],
        "examples": [
            {
                "jp": "そんな運転をしていたら、いつか大きな事故を起こしかねない。",
                "reading_note": "そんなうんてんをしていたら、いつかおおきなじこをおこしかねない。",
                "vi": "Nếu cứ lái xe kiểu đó thì không khéo có ngày gây tai nạn lớn đấy.",
                "grammar_note": "起こす -> 起こし + かねない.",
            },
            {
                "jp": "約束を守らなければ、取引先の信用を失いかねない。",
                "reading_note": "やくそくをまもらなければ、とりひきさきのしんようをうしないかねない。",
                "vi": "Nếu không giữ lời hứa thì có nguy cơ đánh mất uy tín với đối tác.",
                "grammar_note": "失う -> 失い + かねない.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 (N2 P2)",
        "search_keywords": "kanenai co nguy co dan toi xau かねない",
        "match_patterns": ["かねない", "かねません"],
    },
    {
        "code": "GP-N2-03",
        "pattern": "～かねる (Khó mà làm được - Từ chối khéo léo trong công sở)",
        "jlpt_level": "N2",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": False,
        "formation_formula": "Vます(bỏ ます) + かねる / かねます",
        "formation_table": [
            {"pos": "Động từ (Vます)", "rule": "Vます + かねます (お答えしかねます, 賛成しかねます, 引き受けかねます)"},
            {"pos": "Ngữ cảnh giao tiếp", "rule": "Giao tiếp khách hàng / công sở khi muốn từ chối nhẹ nhàng thay cho できません"},
        ],
        "core_meaning_vi": "Bày tỏ rằng vì lý do tâm lý, quy định hoặc hoàn cảnh nên rất khó để đáp ứng yêu cầu ('xin phép khó mà có thể...')",
        "deep_explanation_vi": (
            "Trong văn hóa kinh doanh Nhật Bản, nói thẳng できません với khách hàng hay cấp trên là quá cứng nhắc. "
            "Thay vào đó, dùng Vます + かねます (hoặc kính ngữ おVいたしかねます) để từ chối mềm mỏng nhưng dứt khoát."
        ),
        "register_tag": "Kính ngữ công sở & Dịch vụ khách hàng (N2)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vます + かねる vs Vます + かねない",
                "difference_vi": "かねる = khó lòng mà đáp ứng/làm được (từ chối lịch sự); かねない = có nguy cơ dẫn tới hậu quả xấu.",
                "quick_test_vi": "Thấy giao tiếp khách hàng lịch sự với động từ trả lời/chấp nhận (答える, 賛成する, 引き受ける) -> かねます.",
            }
        ],
        "examples": [
            {
                "jp": "申し訳ございませんが、そのご質問にはお答えしかねます。",
                "reading_note": "もうしわけございませんが、そのごしつもんにはおこたえしかねます。",
                "vi": "Thành thật xin lỗi, nhưng về câu hỏi đó tôi khó lòng có thể trả lời được ạ.",
                "grammar_note": "お + Vます + しかねます (từ chối chuẩn mực công sở).",
            },
            {
                "jp": "条件が厳しすぎるため、この提案には賛成しかねる。",
                "reading_note": "じょうけんがきびしすぎるため、このていあんにはさんせいしかねる。",
                "vi": "Vì điều kiện quá khắt khe nên tôi khó mà tán thành đề xuất này được.",
                "grammar_note": "賛成する -> 賛成し + かねる.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 (N2 P2)",
        "search_keywords": "kaneru kanemasu kho ma lam duoc tu choi kheo かねる かねます",
        "match_patterns": ["かねます", "かねる"],
    },
    {
        "code": "GP-N2-04",
        "pattern": "～にほかならない (Chính là, chẳng qua là không gì khác)",
        "jlpt_level": "N2",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": False,
        "formation_formula": "N / [～から] + にほかならない",
        "formation_table": [
            {"pos": "Danh từ (N)", "rule": "N + にほかならない (努力の結果にほかならない, 愛情の表れにほかならない)"},
            {"pos": "Mệnh đề nguyên nhân", "rule": "～からにほかならない (Chính vì lý do... chứ không vì gì khác)"},
        ],
        "core_meaning_vi": "Khẳng định dứt khoát nguyên nhân hoặc bản chất duy nhất ('chính là nhờ/do N chứ không thể là điều nào khác')",
        "deep_explanation_vi": (
            "Đây là bản nâng cấp văn viết trang trọng ở N2 của N3 ～こそ và ～からだ. "
            "Rất hay xuất hiện ở câu kết bài luận N2-N1 để chốt nguyên nhân cốt lõi của một thành tựu hoặc hiện tượng."
        ),
        "register_tag": "Văn viết nghị luận trang trọng (N2)",
        "confusable_pairs": [
            {
                "rival_pattern": "～にほかならない vs ～にすぎない (N3)",
                "difference_vi": "にほかならない = khẳng định mạnh mẽ 'chính xác là N không gì khác' (đề cao); にすぎない = hạ thấp 'chỉ là N tầm thường mà thôi'.",
                "quick_test_vi": "Thấy luận văn khẳng định bản chất/nguyên nhân duy nhất với ほかならない -> khẳng định tuyệt đối.",
            }
        ],
        "examples": [
            {
                "jp": "彼が成功できたのは、日々の努力の結果にほかならない。",
                "reading_note": "かれがせいこうできたのは、ひびのどりょくのけっかにほかならない。",
                "vi": "Việc anh ấy thành công chính là kết quả của sự nỗ lực hằng ngày chứ không gì khác.",
                "grammar_note": "Danh từ 結果 + にほかならない.",
            },
            {
                "jp": "親が厳しく叱るのは、子どもの将来を心配しているからにほかならない。",
                "reading_note": "おやがきびしくしかるのは、こどものしょうらいをしんぱいしているからにほかならない。",
                "vi": "Cha mẹ mắng nghiêm khắc chính là vì lo lắng cho tương lai của con cái.",
                "grammar_note": "～から + にほかならない.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 (N2 P2)",
        "search_keywords": "ni hoka naranai chinh la khong gi khac にほかならない",
        "match_patterns": ["にほかならない", "に他ならない"],
    },
    {
        "code": "GP-N2-05",
        "pattern": "～とはいえ (Tuy nói là... nhưng trên thực tế vẫn...)",
        "jlpt_level": "N2",
        "category": "contrast_concession",
        "category_label_vi": CATEGORY_LABELS["contrast_concession"],
        "in_exam_corpus": False,
        "formation_formula": "普通形(N/Aな giữ だ hoặc bỏ だ) + とはいえ",
        "formation_table": [
            {"pos": "Danh từ / Tính từ な", "rule": "N / Aな + (だ) + とはいえ (春だとはいえ、まだ寒い = tuy nói là xuân rồi nhưng vẫn lạnh)"},
            {"pos": "Động từ / Tính từ い", "rule": "普通形 + とはいえ (合格したとはいえ、まだ安心できない)"},
        ],
        "core_meaning_vi": "Công nhận sự thật ở vế trước ('tuy nói là...') nhưng nhấn mạnh thực tế ở vế sau vẫn chưa tương xứng/vẫn còn hạn chế",
        "deep_explanation_vi": (
            "Nâng cấp trực tiếp từ ～ものの (N3) lên văn viết N2. "
            "Thường đi với các trạng huống chuyển mùa, cấp bậc mới đạt được, hay điều kiện danh nghĩa ('tuy nói là mùa xuân / tuy đã đỗ N3 / tuy là công ty lớn nhưng...')."
        ),
        "register_tag": "Văn viết & Bình luận (N2)",
        "confusable_pairs": [
            {
                "rival_pattern": "～とはいえ (N2) vs ～ものの (N3)",
                "difference_vi": "Rất gần nghĩa, nhưng とはいえ chấp nhận gắn thẳng sau Danh từ trần (春とはいえ, 子どもとはいえ) và nhấn mạnh 'dù mang danh là/nói là A nhưng thực tế vẫn...'.",
                "quick_test_vi": "Sau danh từ trần (春・休日・病気) đối lập thực tế -> とはいえ.",
            }
        ],
        "examples": [
            {
                "jp": "カレンダーの上では春だとはいえ、朝晩はまだかなり冷え込む。",
                "reading_note": "かれんだーのうえでははるだとはいえ、あさばんはまだかなりひえこむ。",
                "vi": "Tuy trên lịch nói là đã sang xuân nhưng sáng tối trời vẫn còn khá rét.",
                "grammar_note": "N + だ + とはいえ.",
            },
            {
                "jp": "趣味で始めたとはいえ、毎日3時間も練習している。",
                "reading_note": "しゅみではじめたとはいえ、まいにちさんじかんもれんしゅうしている。",
                "vi": "Tuy nói là bắt đầu vì sở thích nhưng ngày nào tôi cũng tập tận 3 tiếng.",
                "grammar_note": "Vた + とはいえ.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 (N2 P1)",
        "search_keywords": "to wa ie tuy noi la nhung thuc te とはいえ",
        "match_patterns": ["とはいえ"],
    },
    {
        "code": "GP-N2-06",
        "pattern": "～にもかかわらず (Bất chấp, mặc dù... vậy mà vẫn)",
        "jlpt_level": "N2",
        "category": "contrast_concession",
        "category_label_vi": CATEGORY_LABELS["contrast_concession"],
        "in_exam_corpus": False,
        "formation_formula": "V普通形 / Aい / Aな(bỏ だ hoặc である) / N(bỏ だ) + にもかかわらず",
        "formation_table": [
            {"pos": "Danh từ / Tính từ な", "rule": "N / Aな + にもかかわらず (大雨にもかかわらず = bất chấp mưa lớn; 不便であるにもかかわらず)"},
            {"pos": "Động từ / Tính từ い", "rule": "普通形 + にもかかわらず (何度も注意したにもかかわらず)"},
        ],
        "core_meaning_vi": "Bất chấp hoàn cảnh, điều kiện hay cảnh báo ở vế trước, kết quả hoàn toàn trái ngược vẫn xảy ra ở vế sau (mạnh hơn のに)",
        "deep_explanation_vi": (
            "Phiên bản văn viết trang trọng và mạnh mẽ hơn nhiều so với ～のに (N4) hay ～ても (N5). "
            "Lưu ý hình thái danh từ: trước にもかかわらず KHÔNG thêm だ hay の (viết thẳng 大雨にもかかわらず, 休日にもかかわらず)."
        ),
        "register_tag": "Văn viết & Thời sự trang trọng (N2)",
        "confusable_pairs": [
            {
                "rival_pattern": "N + にもかかわらず vs N + のに",
                "difference_vi": "Sau danh từ, のに phải thêm な (大雨なのに), còn にもかかわらず gắn thẳng vào danh từ trần (大雨にもかかわらず) và dùng trong văn viết trang trọng.",
                "quick_test_vi": "Thấy danh từ không có な/だ đứng trước chỗ trống + kết quả trái ngược gây bất ngờ -> にもかかわらず.",
            }
        ],
        "examples": [
            {
                "jp": "激しい雨にもかかわらず、会場には多くの人が集まった。",
                "reading_note": "はげしいあめにもかかわらず、かいじょうにはおおくのひとがあつまった。",
                "vi": "Bất chấp cơn mưa nặng hạt, rất nhiều người vẫn tập trung tới hội trường.",
                "grammar_note": "Danh từ 雨 gắn trực tiếp + にもかかわらず.",
            },
            {
                "jp": "何度も確認したにもかかわらず、ミスが見つかった。",
                "reading_note": "なんどもかくにんしたにもかかわらず、みすがみつかった。",
                "vi": "Mặc dù đã kiểm tra đi kiểm tra lại nhiều lần nhưng vẫn phát hiện ra lỗi.",
                "grammar_note": "Vた + にもかかわらず.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 (N2 P1)",
        "search_keywords": "ni mo kakawarazu bat chap mac du にもかかわらず",
        "match_patterns": ["にもかかわらず", "にも関わらず"],
    },
    {
        "code": "GP-N2-07",
        "pattern": "～次第（しだい） / ～次第だ (Ngay sau khi V / Tùy thuộc vào N)",
        "jlpt_level": "N2",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": False,
        "formation_formula": "[1] Vます(bỏ ます) + 次第 (Ngay sau khi xong V) | [2] N + 次第だ (Tùy thuộc vào N)",
        "formation_table": [
            {"pos": "1. Vます + 次第 (Ngay khi)", "rule": "Ngay sau khi hành động V hoàn tất thì lập tức thực hiện vế sau (分かり次第ご連絡します, 到着次第)"},
            {"pos": "2. N + 次第だ (Tùy thuộc vào)", "rule": "Kết quả tùy thuộc hoàn toàn vào N (あなたの努力次第だ, 天気次第で決まる)"},
            {"pos": "Lưu ý Q#37", "rule": "Nhớ cách đọc: 時代 (じだい: thời đại) ≠ 次第 (しだい: tùy vào / ngay sau khi)"},
        ],
        "core_meaning_vi": "Thực hiện hành động ngay lập tức khi điều kiện hoàn tất (Vます次第), hoặc hoàn toàn phụ thuộc vào yếu tố N (N次第だ)",
        "deep_explanation_vi": (
            "Đây là cặp từ xuất hiện cả trong bẫy đọc âm Kanji N3 (Q#37: 時代 じだい vs 次第 しだい) lẫn ngữ pháp N2! "
            "Khi dùng Vます + 次第 (như 'hễ có kết quả sẽ báo ngay': 決まり次第お知らせします), vế sau luôn ở thì tương lai/ý chí lịch sự công sở, KHÔNG dùng quá khứ đã xong."
        ),
        "register_tag": "Công sở & Văn viết (N2)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vます + 次第 vs Vた + とたんに vs N + 次第だ",
                "difference_vi": "Vます+次第 hướng về tương lai có kế hoạch ('ngay khi A xong thì tôi sẽ làm B'); Vた+とたんに kể lại việc bất ngờ đã xảy ra; N+次第だ nghĩa là 'tùy thuộc vào N'.",
                "quick_test_vi": "Trong email công sở ('ngay khi xác nhận xong tôi sẽ liên lạc'): 確認し次第ご連絡いたします.",
            }
        ],
        "examples": [
            {
                "jp": "詳細が決まり次第、メールでご連絡いたします。",
                "reading_note": "しょうさいがきまりしだい、めーるでごれんらくいたします。",
                "vi": "Ngay sau khi chi tiết được quyết định, tôi sẽ liên lạc qua email ngay.",
                "grammar_note": "Vます (決まり) + 次第 + hành động tương lai lịch sự.",
            },
            {
                "jp": "合格できるかどうかは、これからの努力次第だ。",
                "reading_note": "ごうかくできるかどうかは、これからのどりょくしだいだ。",
                "vi": "Có đỗ được hay không là hoàn toàn tùy thuộc vào sự nỗ lực từ nay về sau.",
                "grammar_note": "Danh từ 努力 + 次第だ.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 (N2 P2) | Đề .xlsx (Q37)",
        "search_keywords": "shidai ngay sau khi tuy thuoc vao 次第 次第だ",
        "match_patterns": ["次第", "しだい"],
    },
    {
        "code": "GP-N2-08",
        "pattern": "～とともに / ～に伴って (Đồng thời cùng với / Kéo theo sự biến đổi)",
        "jlpt_level": "N2",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": False,
        "formation_formula": "Vる / N + とともに | Vる / N + に伴って（にともなって） / に伴う + N",
        "formation_table": [
            {"pos": "1. ～とともに (Cùng với / Đồng thời)", "rule": "Cùng một người/tập thể, hoặc hai tính chất/biến đổi song song (年の経過とともに, 友人と共に)"},
            {"pos": "2. ～に伴って (Kéo theo hệ quả)", "rule": "Biến đổi quy mô lớn kéo theo hệ lụy/thay đổi tương ứng (都市化に伴って, 気温の上昇に伴い)"},
        ],
        "core_meaning_vi": "Diễn tả sự đồng hành (cùng với A, vừa A vừa B) hoặc biến đổi kéo theo hàng loạt thay đổi liên đới (～に伴って)",
        "deep_explanation_vi": (
            "Hai mẫu này nâng cấp trực tiếp N3 ～につれて / ～にしたがって vào văn phong học thuật và báo chí N2. "
            "Lưu ý dạng bổ nghĩa danh từ: ～に伴う + N (ví dụ: 引越しに伴う手続き = thủ tục kéo theo khi chuyển nhà)."
        ),
        "register_tag": "Văn viết & Báo chí (N2)",
        "confusable_pairs": [
            {
                "rival_pattern": "～とともに vs ～に伴って vs ～につれて",
                "difference_vi": "とともに còn mang nghĩa 'cùng với ai' hoặc 'vừa mang đặc điểm A vừa mang đặc điểm B'; に伴って/につれて chỉ sự biến đổi tỷ lệ thuận, trong đó に伴って trang trọng và hay gắn danh từ trừu tượng.",
                "quick_test_vi": "Thấy danh từ biến đổi vĩ mô (増加, 発展, 変化) hoặc đi với danh từ phía sau (に伴うN) -> に伴って.",
            }
        ],
        "examples": [
            {
                "jp": "技術の発達とともに、私たちの生活は大きく変わった。",
                "reading_note": "ぎじゅつのはったつとともに、わたしたちのせいかつはおおきくかわった。",
                "vi": "Cùng với sự phát triển của kỹ thuật, cuộc sống của chúng ta đã thay đổi mạnh mẽ.",
                "grammar_note": "N(発達) + とともに.",
            },
            {
                "jp": "人口の増加に伴って、水不足の問題が起きている。",
                "reading_note": "じんこうのぞうかにともなって、みずぶそくのもんだいがおきている。",
                "vi": "Kéo theo sự gia tăng dân số, vấn đề thiếu nước đang xảy ra.",
                "grammar_note": "N + に伴って nêu hệ quả đi kèm.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 (N2 P1)",
        "search_keywords": "to tomo ni ni tomonatte dong thoi keo theo とともに に伴って に伴う",
        "match_patterns": ["とともに", "と共に", "に伴って", "に伴う"],
    },
    {
        "code": "GP-N2-09",
        "pattern": "～に限らず (Không chỉ giới hạn ở N mà còn mở rộng ra...)",
        "jlpt_level": "N2",
        "category": "particle",
        "category_label_vi": CATEGORY_LABELS["particle"],
        "in_exam_corpus": False,
        "formation_formula": "N + に限らず（にかぎらず） + ～も / ～まで",
        "formation_table": [
            {"pos": "Danh từ (N)", "rule": "N + に限らず (日本に限らず, 若者に限らず, 男性に限らず)"},
            {"pos": "Vế sau", "rule": "Mở rộng phạm vi bao quát hơn (世界中, 年配の人, あらゆる世代) + も"},
        ],
        "core_meaning_vi": "Phá bỏ giới hạn ở phạm vi N: không chỉ riêng N mà các đối tượng rộng hơn cũng tương tự",
        "deep_explanation_vi": (
            "Đây là dạng nâng cấp N2 của N3 ～だけでなく / ～ばかりでなく. "
            "Khác với N3 ～とは限らない (chưa chắc lúc nào cũng đúng), ～に限らず nghĩa là 'không chỉ giới hạn trong phạm vi N, mà rộng ra nhiều đối tượng khác nữa'."
        ),
        "register_tag": "Văn viết & Thời sự (N2)",
        "confusable_pairs": [
            {
                "rival_pattern": "N + に限らず vs ～とは限らない (N3)",
                "difference_vi": "に限らず = không chỉ N mà còn đối tượng khác nữa (tương đương だけでなく); とは限らない = chưa chắc đã 100% (phủ định sự tuyệt đối).",
                "quick_test_vi": "Thấy cấu trúc mở rộng 'N1だけでなく他の人も' (không chỉ giới trẻ mà cả người lớn tuổi cũng) -> に限らず.",
            }
        ],
        "examples": [
            {
                "jp": "このアニメは日本に限らず、世界中の人々に愛されている。",
                "reading_note": "このあにめはにほんにかぎらず、せかいじゅうのひとびとにあいされている。",
                "vi": "Bộ anime này không chỉ ở Nhật Bản mà còn được người dân trên toàn thế giới yêu mến.",
                "grammar_note": "日本 + に限らず mở rộng phạm vi ra 世界中.",
            },
            {
                "jp": "最近は女性に限らず、男性の間でも料理教室が人気だ。",
                "reading_note": "さいきんはじょせいにかぎらず、だんせいのあいだでもりょうりきょうしつがにんきだ。",
                "vi": "Gần đây không chỉ phụ nữ mà ngay cả trong giới nam giới lớp học nấu ăn cũng được ưa chuộng.",
                "grammar_note": "女性に限らず + 男性の間でも.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 (N2 P1)",
        "search_keywords": "ni kagirazu khong chi gioi han o に限らず",
        "match_patterns": ["に限らず", "にかぎらず"],
    },
    {
        "code": "GP-N2-10",
        "pattern": "～を契機に / ～をきっかけに (Lấy N làm bước ngoặt / cơ hội khởi đầu)",
        "jlpt_level": "N2",
        "category": "clause_connector",
        "category_label_vi": CATEGORY_LABELS["clause_connector"],
        "in_exam_corpus": False,
        "formation_formula": "N + を契機に（をけいきに） / をきっかけに（して）",
        "formation_table": [
            {"pos": "～をきっかけに (N3-N2)", "rule": "Lấy một sự kiện tình cờ hoặc cụ thể làm động lực/khởi nguồn (日本留学をきっかけに)"},
            {"pos": "～を契機に (N2 trang trọng)", "rule": "Lấy một sự kiện lớn mang tính bước ngoặt lịch sử/chính sách để thay đổi (オリンピックを契機に)"},
        ],
        "core_meaning_vi": "Lấy sự kiện N làm điểm xuất phát, động lực hoặc bước ngoặt dẫn đến sự thay đổi lớn sau này",
        "deep_explanation_vi": (
            "Đây là dạng ngữ pháp nâng cấp trực tiếp từ mẫu từ vựng thi N3 Q#81 ('これを機会に、たばこをやめようと思う' = nhân dịp này tôi sẽ bỏ thuốc). "
            "Khi lên N2, ～をきっかけに (ngẫu nhiên/cá nhân) và ～を契機に (bước ngoặt lớn) giúp diễn đạt cội nguồn của sự thay đổi."
        ),
        "register_tag": "Văn viết & Kể chuyện (N2)",
        "confusable_pairs": [
            {
                "rival_pattern": "～を契機に / ～をきっかけに vs ～を機会に (N3)",
                "difference_vi": "を機会に thiên về tận dụng cơ hội sắp tới/hiện tại ('nhân dịp này tôi quyết định...'); をきっかけに / を契機に thường nhìn lại một sự kiện đã qua làm điểm bùng phát thay đổi.",
                "quick_test_vi": "Kể lại sự việc bước ngoặt trong quá khứ khiến mình thay đổi đến bây giờ -> をきっかけに / を契機に.",
            }
        ],
        "examples": [
            {
                "jp": "大きな病気をきっかけに、生活習慣を見直すことにした。",
                "reading_note": "おおきなびょうきをきっかけに、せいかつしゅうかんをみなおすことにした。",
                "vi": "Lấy trận ốm nặng làm bước ngoặt, tôi quyết định xem xét lại thói quen sinh hoạt.",
                "grammar_note": "Danh từ sự kiện 病気 + をきっかけに.",
            },
            {
                "jp": "1964年のオリンピックを契機に、日本の交通網は急速に発展した。",
                "reading_note": "せんきゅうひゃくろくじゅうよねんのおりんぴっくをけいきに、にほんのこうつうもうはきゅうそくにはってんした。",
                "vi": "Lấy Thế vận hội 1964 làm bước ngoặt, mạng lưới giao thông Nhật Bản đã phát triển nhanh chóng.",
                "grammar_note": "Sự kiện vĩ mô dùng を契機に.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 (N2 P1) | Đề .xlsx (Q81)",
        "search_keywords": "wo keiki ni wo kikkake ni buoc ngoat co hoi を契機に をきっかけに",
        "match_patterns": ["を契機に", "をきっかけに"],
    },
    {
        "code": "GP-N2-11",
        "pattern": "～に先立って (Trước khi tiến hành sự kiện quan trọng N)",
        "jlpt_level": "N2",
        "category": "aspect",
        "category_label_vi": CATEGORY_LABELS["aspect"],
        "in_exam_corpus": False,
        "formation_formula": "N(sự kiện/hành động) / Vる + に先立って（にさきだって） / に先立ち",
        "formation_table": [
            {"pos": "Danh từ / Động từ", "rule": "開店に先立って (trước khi khai trương), 試験の実施に先立ち"},
            {"pos": "So sánh với N3 ～にあたって", "rule": "にあたって = ngay thời điểm bắt đầu sự kiện; に先立って = làm bước chuẩn bị TRƯỚC KHI sự kiện chính diễn ra"},
        ],
        "core_meaning_vi": "Làm bước chuẩn bị, công bố hoặc nghi thức trước thềm một sự kiện chính thức sắp diễn ra",
        "deep_explanation_vi": (
            "Nâng cấp trực tiếp từ ～の前に (N5) và ～にあたって / ～に際して (N3). "
            "～に先立って nhấn mạnh tính TRÌNH TỰ THỜI GIAN: việc chuẩn bị/thông báo ở vế sau phải xảy ra TRƯỚC KHI sự kiện trọng đại ở vế trước chính thức mở màn."
        ),
        "register_tag": "Trang trọng / Thông cáo & Sự kiện (N2)",
        "confusable_pairs": [
            {
                "rival_pattern": "～に先立って vs ～にあたって (N3)",
                "difference_vi": "に先立って nhấn mạnh thực hiện TRƯỚC khi sự kiện diễn ra (ví dụ phát phiếu kiểm tra trước khi thi); にあたって nhấn mạnh thời điểm BƯỚC VÀO sự kiện.",
                "quick_test_vi": "Thấy hành động chuẩn bị tiền trạm (tập huấn trước lễ, kiểm tra trước khi mở bán) -> に先立って.",
            }
        ],
        "examples": [
            {
                "jp": "新製品の発売に先立って、記者会見が開かれた。",
                "reading_note": "しんせいひんのはつばいにさきだって、きしゃかいけんがひらかれた。",
                "vi": "Trước khi mở bán sản phẩm mới, một buổi họp báo đã được tổ chức.",
                "grammar_note": "N(発売) + に先立って.",
            },
            {
                "jp": "会議を始めるに先立ち、まず資料をお配りします。",
                "reading_note": "かいぎをはじめるにさきだち、まずしりょうをおくばりします。",
                "vi": "Trước khi bắt đầu cuộc họp, trước tiên tôi xin phép phát tài liệu.",
                "grammar_note": "Vる + に先立ち (dạng liên dụng trang trọng).",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 (N2 P1)",
        "search_keywords": "ni sakidatte truoc khi su kien quan trong に先立って に先立ち",
        "match_patterns": ["に先立って", "に先立ち"],
    },
    {
        "code": "GP-N2-12",
        "pattern": "～得る（うる・える） / ～得ない（えない） (Có khả năng xảy ra / Không thể nào)",
        "jlpt_level": "N2",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": False,
        "formation_formula": "Vます(bỏ ます) + 得る（うる / える） / 得ない（えない）",
        "formation_table": [
            {"pos": "Khẳng định (Có thể xảy ra)", "rule": "Vます + 得る (đọc là うる hoặc える: 起こり得る, あり得る, 原因になり得る - Kosei p.11)"},
            {"pos": "Phủ định (Không thể xảy ra)", "rule": "Vます + 得ない (CHỈ đọc là えない, cấm *うない!: あり得ない = chuyện không thể nào!)"},
        ],
        "core_meaning_vi": "Đánh giá tính khả thi về mặt lý thuyết/logic: việc đó 'có thể xảy ra' (得る) hay 'tuyệt đối không thể xảy ra' (得ない)",
        "deep_explanation_vi": (
            "Mẫu N2 này xuất hiện ngay trong giáo trình Kosei Đọc hiểu N3 p.11 ('思わぬ体調不良の原因にもなりうる' = cũng có thể trở thành nguyên nhân gây suy nhược cơ thể bất ngờ)! "
            "Lưu ý quy tắc phát âm kinh điển: dạng khẳng định đọc được cả うる và える (trước danh từ thường đọc うる: ありうる話), nhưng dạng phủ định BẮT BUỘC chỉ đọc là えない (ありえない)."
        ),
        "register_tag": "Văn viết & Học thuật (N2)",
        "confusable_pairs": [
            {
                "rival_pattern": "Vます + 得る / 得ない vs Vられる / ことができる",
                "difference_vi": "ことができる chỉ năng lực thực hiện hành động cụ thể của người; Vます+得る đánh giá xác suất/khả năng logic một sự việc có thể phát sinh hay không.",
                "quick_test_vi": "Thấy あり得る / 起こり得る / なり得る (Kosei p.11) -> xác suất logic N2.",
            }
        ],
        "examples": [
            {
                "jp": "冷房は優れた技術ではあるが、思わぬ体調不良の原因にもなりうる。",
                "reading_note": "れいぼうはすぐれたぎじゅつではあるが、おもわぬたいちょうふりょうのげんいんにもなりうる。",
                "vi": "Điều hòa tuy là công nghệ tuyệt vời nhưng cũng có thể trở thành nguyên nhân gây ốm bất ngờ.",
                "grammar_note": "Kosei p.11: なる -> なり + うる.",
            },
            {
                "jp": "そんなことは常識的に考えてあり得ない。",
                "reading_note": "そんなことはじょうしきてきにかんがえてありえない。",
                "vi": "Chuyện như vậy xét theo lẽ thường là hoàn toàn không thể xảy ra được.",
                "grammar_note": "あり + 得ない (chỉ đọc え-ない).",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 (N2 P2) | Kosei p.11",
        "search_keywords": "uru eru enai co the xay ra khong the nao 得る 得ない ありえない なりうる",
        "match_patterns": ["なりうる", "あり得る", "あり得ない", "ありえない", "得ない"],
    },
    {
        "code": "GP-N2-13",
        "pattern": "～どころか (Chẳng những không... mà ngược lại còn...)",
        "jlpt_level": "N2",
        "category": "contrast_concession",
        "category_label_vi": CATEGORY_LABELS["contrast_concession"],
        "in_exam_corpus": False,
        "formation_formula": "N / V普通形 / Aい / Aな + どころか",
        "formation_table": [
            {"pos": "Bác bỏ vế trước -> Đi xa hơn hẳn", "rule": "AどころかB (Đừng nói là A, ngay cả đến mức tệ/khác xa hơn là B còn...)"},
            {"pos": "Kết nối danh từ", "rule": "N + どころか (漢字どころか、ひらがなも書けない)"},
        ],
        "core_meaning_vi": "Phủ nhận mức độ nêu ở vế trước để nhấn mạnh thực tế ở vế sau đi xa hơn hoặc trái ngược hẳn ('nào có phải A đâu, trái lại còn B')",
        "deep_explanation_vi": (
            "Mẫu này nâng cấp từ ～ばかりか (N3) ở chỗ ～ばかりか đi theo hướng TĂNG TIẾN CÙNG CHIỀU ('không chỉ biết tiếng Anh mà còn biết cả tiếng Pháp'), "
            "còn ～どころか thường đi theo hướng PHỦ NHẬN / ĐỐI LẬP MẠNH ('chẳng những không nghỉ ngơi được mà còn phải tăng ca tới khuya'; 'nào có biết chữ Kanji đâu, Hiragana còn chưa thuộc' — rất hay xuất hiện ngay trong bài đọc hiểu Kosei p.11: '仕事や勉強どころか、遊びも楽しめない')."
        ),
        "register_tag": "Trung tính & Văn viết (N2)",
        "confusable_pairs": [
            {
                "rival_pattern": "～どころか (N2) vs ～ばかりか (N3)",
                "difference_vi": "ばかりか giữ nguyên sự thật vế trước rồi cộng thêm vế sau cùng hướng; どころか bác bỏ hoàn toàn khả năng vế trước ('đừng nói đến A, đến B còn...').",
                "quick_test_vi": "Thấy vế trước và vế sau đối chọi cực mạnh ('không được tăng lương mà còn bị giảm lương') -> どころか.",
            }
        ],
        "examples": [
            {
                "jp": "体調を崩すと、仕事や勉強どころか、遊びも楽しめないだろう。",
                "reading_note": "たいちょうをくずすと、しごとやべんきょうどころか、あそびもたのしめないだろう。",
                "vi": "Một khi đổ bệnh thì đừng nói đến làm việc hay học tập, ngay cả đi chơi cũng chẳng thể tận hưởng nổi.",
                "grammar_note": "Kosei p.11: Danh từ + どころか bác bỏ mức độ cao trước.",
            },
            {
                "jp": "休むどころか、毎日深夜まで残業が続いている。",
                "reading_note": "やすむどころか、まいにちしんやまでざんぎょうがつづいている。",
                "vi": "Nghỉ ngơi đâu chẳng thấy, ngày nào cũng phải tăng ca đến tận nửa đêm.",
                "grammar_note": "Vる + どころか nêu thực tế trái ngược.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 (N2 P2) | Kosei p.11",
        "search_keywords": "dokoro ka chang nhung khong ma con どころか",
        "match_patterns": ["どころか"],
    },
    {
        "code": "GP-N2-14",
        "pattern": "～というものではない / ～というわけでもない (Không hẳn cứ thế là xong)",
        "jlpt_level": "N2",
        "category": "modality",
        "category_label_vi": CATEGORY_LABELS["modality"],
        "in_exam_corpus": False,
        "formation_formula": "普通形 + というものではない / というものでもない / というわけでもない",
        "formation_table": [
            {"pos": "～というものではない", "rule": "Phản bác quan niệm đơn giản hóa bản chất ('không phải cứ hễ A là sẽ được B đâu')"},
            {"pos": "～というわけでもない", "rule": "Phủ định nhẹ nhàng hơn わけではない ('cũng không hẳn là vậy đâu')"},
        ],
        "core_meaning_vi": "Phản bác suy nghĩ phiến diện, nhắc nhở rằng bản chất vấn đề không đơn giản chỉ như vậy",
        "deep_explanation_vi": (
            "Đây là sự kết hợp nâng cao từ gia đình ～わけではない và ～ものだ của N3 lên N2. "
            "Thường kết hợp với ただ / ～さえ～ば để nhắc rằng một điều kiện đơn lẻ chưa đủ tạo nên giá trị thực chất (không phải cứ giá đắt là tốt, không phải cứ nhiều từ vựng là nói giỏi)."
        ),
        "register_tag": "Văn viết nghị luận & Đánh giá (N2)",
        "confusable_pairs": [
            {
                "rival_pattern": "～というものではない (N2) vs ～わけではない (N3)",
                "difference_vi": "わけではない phủ định một phần sự kiện cụ thể; というものではない nêu quan điểm mang tính triết lý, bản chất chung ('bản chất mọi việc không phải cứ... là xong').",
                "quick_test_vi": "Thấy '～さえすればいい___' hoặc 'ただ安ければいい___' -> というものではない.",
            }
        ],
        "examples": [
            {
                "jp": "料理はただ値段が高ければおいしいというものではない。",
                "reading_note": "りょうりはただねだんがたかければおいしいというものではない。",
                "vi": "Món ăn không phải cứ hễ giá đắt là sẽ ngon đâu.",
                "grammar_note": "ただ～ば + というものではない phản bác quan điểm phiến diện.",
            },
            {
                "jp": "試験に合格すればそれで終わりというものでもない。",
                "reading_note": "しけんにごうかくすればそれでおわりというものでもない。",
                "vi": "Cũng không phải hễ cứ thi đỗ là mọi chuyện kết thúc ở đó đâu.",
                "grammar_note": "Dùng も để giảm nhẹ giọng điệu nhưng giữ vững lập luận.",
            },
        ],
        "source_ref": "Sơ đồ N5-N1 (N2 P2)",
        "search_keywords": "to iu mono de wa nai to iu wake demo nai khong han cu the la xong というものではない というわけでもない",
        "match_patterns": ["というものではない", "というものでもない", "というわけでもない"],
    },
])

# =========================================================================
# DIAGNOSTIC GRAMMAR DRILLS (GRAMMAR_DRILLS_DATA)
# =========================================================================
GRAMMAR_DRILLS_DATA: List[Dict[str, Any]] = [
    # --- GP-N5-01 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N5-01-F",
        "grammar_code": "GP-N5-01",
        "drill_type": "formation",
        "prompt_jp": "風が強くて、桜の花がみんな（　　）しまった。",
        "options": ["散て", "散って", "散んで", "散いで"],
        "correct_index": 1,
        "translation_vi": "Gió mạnh nên hoa anh đào đã rụng hết mất rồi.",
        "explanation_vi": "Động từ 散る (ちる) kết thúc bằng る có nguyên âm trước là い nhưng là động từ NHÓM 1 ngoại lệ, nên chia thể て thành 散って (biến âm って).",
        "option_diagnostics": [
            "[SAI - Nhầm nhóm động từ]: 散る tuy kết thúc bằng い+る nhưng không thuộc Nhóm 2; bỏ る gắn thẳng て thành *散て là sai chia thể.",
            "[ĐÚNG - Hình thái Nhóm 1]: 散る là động từ Nhóm 1 ngoại lệ đuôi る -> biến âm xúc âm thành 散って.",
            "[SAI - Nhầm hàng chia thể]: Biến âm んで chỉ áp dụng cho động từ kết thúc bằng む・ぶ・ぬ (như 読む・飛ぶ・死ぬ), không dùng cho đuôi る.",
            "[SAI - Nhầm hàng chia thể]: Biến âm いで chỉ áp dụng cho động từ kết thúc bằng ぐ (như 泳ぐ・急ぐ).",
        ],
    },
    {
        "drill_key": "DR-GP-N5-01-C",
        "grammar_code": "GP-N5-01",
        "drill_type": "contrast",
        "prompt_jp": "子どもたちが急いで家へ（　　）から、宿題を始めた。",
        "options": ["帰て", "帰って", "帰して", "帰いて"],
        "correct_index": 1,
        "translation_vi": "Lũ trẻ vội vã về tới nhà rồi mới bắt đầu làm bài tập.",
        "explanation_vi": "帰る (かえる) là động từ Nhóm 1 ngoại lệ (tuy có え trước る), chia thể て phải biến thành 帰って (khác với 変える là Nhóm 2 chia 変えて).",
        "option_diagnostics": [
            "[SAI - Nhầm với 変える (Nhóm 2)]: 帰る (về) thuộc Nhóm 1 ngoại lệ nên không bỏ る để thành *帰て; chỉ 変える (thay đổi) mới chia 変えて.",
            "[ĐÚNG - Ngoại lệ Nhóm 1]: 帰る chia thể て là 帰って (và thể ない là 帰らない).",
            "[SAI - Nhầm đuôi す]: Biến âm して chỉ dùng cho động từ kết thúc bằng す hoặc động từ する.",
            "[SAI - Nhầm đuôi く]: Biến âm いて chỉ dùng cho động từ kết thúc bằng く (như 書く).",
        ],
    },
    # --- GP-N5-02 (contrast + application) ---
    {
        "drill_key": "DR-GP-N5-02-C",
        "grammar_code": "GP-N5-02",
        "drill_type": "contrast",
        "prompt_jp": "冬の冷たい空気（　　）部屋の中に入るのを防ぎます。",
        "options": ["を", "が", "は", "に"],
        "correct_index": 1,
        "translation_vi": "Ngăn việc không khí lạnh mùa đông tràn vào trong phòng.",
        "explanation_vi": "Trong mệnh đề định ngữ/danh từ hóa làm tân ngữ (冷たい空気が入る), chủ thể của tự động từ 入る phải đánh dấu bằng が (không dùng は trong mệnh đề phụ, không dùng を vì 入る không tác động lên không khí).",
        "option_diagnostics": [
            "[SAI - Nhầm vai trò chủ thể/tân ngữ]: 空気 là chủ thể tự di chuyển vào phòng chứ không phải tân ngữ chịu tác động của động từ 入る.",
            "[ĐÚNG - Chủ thể mệnh đề phụ]: Tự động từ 入る đi với chủ thể が bên trong mệnh đề danh từ hóa (...入るの).",
            "[SAI - Bẫy trợ từ は trong mệnh đề phụ]: Trợ từ chủ đề は không đặt ở chủ ngữ bên trong mệnh đề phụ bổ nghĩa/danh từ hóa.",
            "[SAI - Nhầm trợ từ đích đến]: に đánh dấu đích đến (部屋の中に入る), không đánh dấu chủ thể 空気.",
        ],
    },
    {
        "drill_key": "DR-GP-N5-02-A",
        "grammar_code": "GP-N5-02",
        "drill_type": "application",
        "prompt_jp": "この部屋は窓が大きいので、春になるときれいな花（　　）よく見えます。",
        "options": ["を", "が", "で", "へ"],
        "correct_index": 1,
        "translation_vi": "Phòng này cửa sổ lớn nên hễ đến mùa xuân là có thể nhìn thấy hoa đẹp rất rõ.",
        "explanation_vi": "Động từ 見える (có thể tự nhiên nhìn thấy) mang tính tự động/tri giác tự nhiên nên đối tượng nhìn thấy bắt buộc dùng trợ từ が (khác với 見る dùng を).",
        "option_diagnostics": [
            "[SAI - Nhầm 見る với 見える]: Trợ từ を dùng với tha động từ chủ động 見る (花を見る); còn tự động từ tri giác 見える bắt buộc dùng が.",
            "[ĐÚNG - Trợ từ tri giác 見える]: Đối tượng lọt vào tầm mắt của 見える luôn đi với が (花が見える).",
            "[SAI - Nhầm phương tiện/địa điểm]: で chỉ nơi diễn ra hành động hoặc công cụ, không đánh dấu đối tượng nhìn thấy.",
            "[SAI - Nhầm phương hướng]: へ chỉ hướng di chuyển, không đi với 見える.",
        ],
    },
    # --- GP-N5-03 (formation + application) ---
    {
        "drill_key": "DR-GP-N5-03-F",
        "grammar_code": "GP-N5-03",
        "drill_type": "formation",
        "prompt_jp": "田中さんは今、駅前の喫茶店（　　）友だちとコーヒーを飲んでいます。",
        "options": ["に", "で", "へ", "を"],
        "correct_index": 1,
        "translation_vi": "Anh Tanaka hiện đang uống cà phê cùng bạn tại quán cà phê trước ga.",
        "explanation_vi": "Uống cà phê (飲んでいます) là động từ HÀNH ĐỘNG tích cực diễn ra tại không gian quán cà phê nên địa điểm phải dùng で.",
        "option_diagnostics": [
            "[SAI - Nhầm tồn tại tĩnh với hành động]: に chỉ nơi tồn tại tĩnh (いる・ある・住む) hoặc điểm đến (行く), không dùng cho hành động tích cực như uống cà phê.",
            "[ĐÚNG - Địa điểm diễn ra hành động]: Động từ hành động (飲む・食べる・勉強する) xảy ra ở địa điểm nào thì địa điểm đó dùng で.",
            "[SAI - Nhầm phương hướng]: へ chỉ hướng đi tới nơi nào đó, không dùng cho hành động đang ngồi tại chỗ.",
            "[SAI - Nhầm điểm đi qua]: を đi với động từ di chuyển qua không gian (歩く・渡る), không dùng với quán cà phê đang ngồi uống.",
        ],
    },
    {
        "drill_key": "DR-GP-N5-03-A",
        "grammar_code": "GP-N5-03",
        "drill_type": "application",
        "prompt_jp": "大きな地震（　　）備えて、水や食料を買い置きしている。",
        "options": ["で", "を", "に", "へ"],
        "correct_index": 2,
        "translation_vi": "Để đề phòng trận động đất lớn, tôi mua trữ sẵn nước và lương thực.",
        "explanation_vi": "Động từ 備える (phòng bị, chuẩn bị cho tình huống) kết hợp cố định với trợ từ đích đến に (地震に備える).",
        "option_diagnostics": [
            "[SAI - Nhầm nguyên nhân で]: 地震で備える nghe thành 'dùng động đất để chuẩn bị', sai quan hệ mục tiêu phòng ngừa.",
            "[SAI - Nhầm tân ngữ trực tiếp]: 備える nhận mục tiêu phòng ngừa bằng に, còn vật dùng để dự trữ mới dùng を (水を買い置きする).",
            "[ĐÚNG - Kết hợp cố định に備える]: Động từ 備える (phòng bị cho rủi ro) luôn đòi hỏi trợ từ mục tiêu に.",
            "[SAI - Nhầm phương hướng vật lý]: へ chỉ hướng di chuyển vật lý, không kết hợp với 備える.",
        ],
    },
    # --- GP-N5-04 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N5-04-F",
        "grammar_code": "GP-N5-04",
        "drill_type": "formation",
        "prompt_jp": "出席できるかどうか、4月6日（　　）お返事ください。",
        "options": ["まで", "までに", "より", "から"],
        "correct_index": 1,
        "translation_vi": "Xin hãy trả lời trước ngày 6 tháng 4 xem bạn có tham dự được hay không.",
        "explanation_vi": "Trả lời (お返事ください) là hành động dứt điểm một lần nên cần hạn chót là までに ('trước thời điểm ngày 6/4').",
        "option_diagnostics": [
            "[SAI - Nhầm liên tục với hạn chót]: まで diễn tả hành động kéo dài liên tục suốt tới ngày 6/4 ('trả lời liên tục từ nay đến ngày 6/4'), sai với tính chất dứt điểm của お返事する.",
            "[ĐÚNG - Hạn chót までに]: Hành động hoàn thành một lần trước mốc thời hạn bắt buộc dùng までに.",
            "[SAI - Nhầm so sánh hơn]: より mang nghĩa 'so với' hoặc 'từ (trang trọng)', không diễn đạt hạn chót trước ngày 6/4.",
            "[SAI - Nhầm điểm xuất phát]: から nghĩa là 'kể từ ngày 6/4 trở đi', ngược với yêu cầu nộp phản hồi trước hạn.",
        ],
    },
    {
        "drill_key": "DR-GP-N5-04-C",
        "grammar_code": "GP-N5-04",
        "drill_type": "contrast",
        "prompt_jp": "電車で行く（　　）、バスのほうがずっと安い。",
        "options": ["から", "まで", "より", "ほど"],
        "correct_index": 2,
        "translation_vi": "So với việc đi bằng tàu điện thì đi xe buýt rẻ hơn nhiều.",
        "explanation_vi": "Cấu trúc so sánh [Aより Bのほうが...] dùng trợ từ より làm mốc so sánh để khẳng định B hơn A.",
        "option_diagnostics": [
            "[SAI - Nhầm nguyên nhân]: から ở đây tạo nghĩa 'vì đi bằng tàu nên xe buýt rẻ hơn', sai logic nhân quả.",
            "[SAI - Nhầm giới hạn]: まで nghĩa là 'đến tận việc đi tàu', không khớp với cấu trúc đối chiếu ～のほうが.",
            "[ĐÚNG - Mốc so sánh より]: Mẫu so sánh hơn giữa hai phương án Vる+より ～のほうが.",
            "[SAI - Nhầm so sánh phủ định]: ほど trong so sánh phải đi với động/tính từ PHỦ ĐỊNH ở cuối câu (như ほど高くない); ở đây cuối câu là khẳng định 安い.",
        ],
    },
    # --- GP-N5-05 (contrast + application) ---
    {
        "drill_key": "DR-GP-N5-05-C",
        "grammar_code": "GP-N5-05",
        "drill_type": "contrast",
        "prompt_jp": "この薬はスポンジがついているので、とても（　　）なった。",
        "options": ["ぬりやすいに", "ぬりやすく", "ぬりやすくて", "ぬりやすいで"],
        "correct_index": 1,
        "translation_vi": "Thuốc này có gắn miếng mút nên đã trở nên rất dễ bôi.",
        "explanation_vi": "Mẫu Vます+やすい là tính từ đuôi い, nên khi kết hợp với なった phải bỏ い thêm く -> ぬりやすくなった.",
        "option_diagnostics": [
            "[SAI - Lỗi chia Aい thành Aな]: Thêm に trước なった chỉ áp dụng cho tính từ đuôi な hoặc danh từ; やすい mang đuôi い nên *やすいに là sai hình thái.",
            "[ĐÚNG - Quy tắc Aい + くなる]: Bỏ い ở cuối ぬりやすい và đổi thành く trước なった.",
            "[SAI - Sai dạng nối trước なる]: やすくて là thể て dùng để nối câu hoặc nêu nguyên nhân, không đứng trực tiếp trước なる.",
            "[SAI - Sai cả từ loại lẫn trợ từ]: *やすいで không tồn tại trong hệ chia tính từ đuôi い.",
        ],
    },
    {
        "drill_key": "DR-GP-N5-05-A",
        "grammar_code": "GP-N5-05",
        "drill_type": "application",
        "prompt_jp": "母の家は駅から遠いので、買い物が（　　）場所にある。",
        "options": ["不便く", "不便な", "不便に", "不便だ"],
        "correct_index": 1,
        "translation_vi": "Nhà của mẹ tôi xa ga nên nằm ở một nơi bất tiện cho việc mua sắm.",
        "explanation_vi": "不便 (ふべん) là tính từ đuôi な nên khi bổ nghĩa trực tiếp cho danh từ 場所 bắt buộc phải thêm な -> 不便な場所.",
        "option_diagnostics": [
            "[SAI - Chia Aな theo quy tắc Aい]: 不便 là tính từ đuôi な, không có dạng biến đuôi *不便く.",
            "[ĐÚNG - Aな + な + N]: Tính từ đuôi な bổ nghĩa cho danh từ 場所 phía sau phải có な.",
            "[SAI - Dùng dạng trạng từ に]: 不便に bổ nghĩa cho động từ (như 不便になる), không đứng trực tiếp bổ nghĩa cho danh từ 場所.",
            "[SAI - Dùng dạng kết thúc câu だ]: Dạng 普通形 khẳng định だ chỉ dùng kết thúc câu, không đặt trước danh từ 場所.",
        ],
    },
    # --- GP-N5-06 (formation + application) ---
    {
        "drill_key": "DR-GP-N5-06-F",
        "grammar_code": "GP-N5-06",
        "drill_type": "formation",
        "prompt_jp": "友だちが（　　）電車が事故で止まっているそうだ。",
        "options": ["乗ります", "乗っている", "乗って", "乗り"],
        "correct_index": 1,
        "translation_vi": "Nghe nói chuyến tàu mà bạn tôi đang đi bị dừng lại do tai nạn.",
        "explanation_vi": "Động từ đứng trước danh từ 電車 để làm mệnh đề định ngữ BẮT BUỘC ở thể thông thường (普通形), tuyệt đối không dùng thể lịch sự ます.",
        "option_diagnostics": [
            "[SAI - Dùng thể lịch sự ます trong định ngữ]: Mệnh đề bổ nghĩa trước danh từ cấm dùng thể ます (*乗ります電車).",
            "[ĐÚNG - Thể thông thường tiếp diễn]: 乗っている (thể thông thường) bổ nghĩa trực tiếp cho danh từ 電車.",
            "[SAI - Thể て không bổ nghĩa danh từ]: Thể て dùng nối hành động, không đứng trực tiếp làm định ngữ trước danh từ 電車.",
            "[SAI - Gốc Vます rời]: Gốc 乗り chỉ dùng ghép từ vựng (như 乗り場), không biểu đạt mệnh đề có chủ ngữ 友だちが.",
        ],
    },
    {
        "drill_key": "DR-GP-N5-06-A",
        "grammar_code": "GP-N5-06",
        "drill_type": "application",
        "prompt_jp": "（　　）ときにすぐ読めるように、説明書を机の引き出しにしまっておく。",
        "options": ["必要", "必要な", "必要に", "必要だ"],
        "correct_index": 1,
        "translation_vi": "Để có thể đọc ngay vào lúc cần thiết, tôi cất sẵn tờ hướng dẫn vào ngăn kéo bàn.",
        "explanation_vi": "Danh từ thời gian とき (khi, lúc) cần được bổ nghĩa như một danh từ thông thường: tính từ đuôi な (必要) phải thêm な -> 必要なとき.",
        "option_diagnostics": [
            "[SAI - Thiếu な khi bổ nghĩa とき]: 必要 là tính từ đuôi な, bỏ rơi な trước danh từ とき là thiếu trợ liên kết.",
            "[ĐÚNG - Aな + な + とき]: 必要なとき = vào lúc cần thiết.",
            "[SAI - Dùng に bổ nghĩa động từ]: 必要に chỉ kết hợp với なる/する, không bổ nghĩa trực tiếp cho danh từ とき.",
            "[SAI - Dùng だ kết thúc câu]: だ không đứng giữa tính từ な và danh từ とき.",
        ],
    },
    # --- GP-N5-07 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N5-07-F",
        "grammar_code": "GP-N5-07",
        "drill_type": "formation",
        "prompt_jp": "冬の寒い日に冷たい風が部屋に（　　）防ぐために、窓を閉める。",
        "options": ["入る", "入るのを", "入ることが", "入るものを"],
        "correct_index": 1,
        "translation_vi": "Để ngăn việc gió lạnh tràn vào phòng vào ngày đông rét, tôi đóng cửa sổ.",
        "explanation_vi": "Động từ 防ぐ (ngăn chặn) là tha động từ đòi hỏi tân ngữ với trợ từ を, vì vậy mệnh đề 入る phải danh từ hóa bằng の + を.",
        "option_diagnostics": [
            "[SAI - Thiếu danh từ hóa và trợ từ]: Không thể nối thẳng động từ 入る vào tha động từ 防ぐ mà thiếu のを.",
            "[ĐÚNG - Danh từ hóa の + を]: Cụm 入るの đóng vai trò danh từ làm tân ngữ với を cho động từ 防ぐ.",
            "[SAI - Sai trợ từ chủ ngữ が]: 防ぐ nhận đối tượng tác động bằng を, không dùng が.",
            "[SAI - Dùng sai danh từ もの]: もの chỉ vật thể cụ thể (đồ vật), không dùng danh từ hóa hành động gió tràn vào phòng.",
        ],
    },
    {
        "drill_key": "DR-GP-N5-07-C",
        "grammar_code": "GP-N5-07",
        "drill_type": "contrast",
        "prompt_jp": "私の趣味は、週末に古い映画を（　　）。",
        "options": ["見るのです", "見ることです", "見るものです", "見るはずです"],
        "correct_index": 1,
        "translation_vi": "Sở thích của tôi là xem những bộ phim cũ vào cuối tuần.",
        "explanation_vi": "Khi định nghĩa sở thích, ước mơ hoặc mục tiêu ở cuối câu [私の趣味/夢は ～ことです], bắt buộc dùng danh từ hóa こと (không dùng の).",
        "option_diagnostics": [
            "[SAI - Nhầm の với こと trước です]: Trong mẫu giải thích sở thích/ước mơ (～は～ことです), không dùng のです (vốn mang nghĩa giải thích nguyên nhân).",
            "[ĐÚNG - Cấu trúc định nghĩa こと]: [Nは Vることです] dùng こと để danh từ hóa hoạt động làm vị ngữ định nghĩa.",
            "[SAI - Nhầm もの (bản chất)]: 見るものです tạo nghĩa 'xem phim vốn là lẽ tự nhiên/nên làm', không dùng nêu sở thích.",
            "[SAI - Nhầm phỏng đoán はず]: はずです là suy đoán chắc chắn theo logic, sai cấu trúc định nghĩa sở thích.",
        ],
    },
    # --- GP-N5-08 (contrast + application) ---
    {
        "drill_key": "DR-GP-N5-08-C",
        "grammar_code": "GP-N5-08",
        "drill_type": "contrast",
        "prompt_jp": "田中さんは日本人の友達に「その歌を知っていますか」と聞かれて、「いいえ、（　　）」と答えた。",
        "options": ["知っていません", "知りません", "知っています", "知りませんでした"],
        "correct_index": 1,
        "translation_vi": "Anh Tanaka được bạn người Nhật hỏi 'Bạn có biết bài hát đó không?' và trả lời 'Không, tôi không biết'.",
        "explanation_vi": "Động từ đặc biệt 知る (biết): khẳng định chia tiếp diễn trạng thái 知っています, nhưng PHỦ ĐỊNH luôn dùng thể đơn giản 知りません (tránh dùng *知っていません).",
        "option_diagnostics": [
            "[SAI - Lỗi phủ định động từ tri giác 知る]: Tiếng Nhật không dùng *知っていません để nói 'không biết' hiện tại; phủ định của 知っています là 知りません.",
            "[ĐÚNG - Bất quy tắc phủ định của 知る]: Trả lời 'Tôi không biết' dùng 知りません.",
            "[SAI - Mâu thuẫn với いいえ]: Đầu câu trả lời là いいえ (Không) nên không thể kết thúc bằng khẳng định 知っています.",
            "[SAI - Sai thì quá khứ]: Câu hỏi hỏi trạng thái hiểu biết hiện tại, không dùng quá khứ 知りませんでした.",
        ],
    },
    {
        "drill_key": "DR-GP-N5-08-A",
        "grammar_code": "GP-N5-08",
        "drill_type": "application",
        "prompt_jp": "スーパーの棚に、新鮮なりんごがきれいに（　　）。",
        "options": ["並べています", "並んでいます", "並びます", "並べる"],
        "correct_index": 1,
        "translation_vi": "Trên kệ siêu thị, những quả táo tươi được xếp ngay ngắn.",
        "explanation_vi": "Chủ thể đi với が là りんご (vật vô tri), nên phải dùng tự động từ 並ぶ chia trạng thái kết quả 並んでいます (đang xếp hàng ngay ngắn).",
        "option_diagnostics": [
            "[SAI - Dùng tha động từ với chủ thể が]: 並べる là tha động từ (người bày táo: りんごを並べる), không đi với chủ ngữ りんごが.",
            "[ĐÚNG - Tự động từ + ている chỉ kết quả]: 並ぶ chia thể ている mô tả trạng thái vật đang bày sẵn trước mắt.",
            "[SAI - Dùng thì hiện tại đơn]: 並びます chỉ hành động thói quen hoặc tương lai, không mô tả trạng thái hiện hữu trước mắt.",
            "[SAI - Thiếu kết thúc câu lịch sự/tiếp diễn]: Động từ nguyên thể 並べる là tha động từ và không khớp trạng thái đang tồn tại.",
        ],
    },
    # --- GP-N5-09 (formation + application) ---
    {
        "drill_key": "DR-GP-N5-09-F",
        "grammar_code": "GP-N5-09",
        "drill_type": "formation",
        "prompt_jp": "私はまだ一度も北海道へ（　　）ことがありません。",
        "options": ["行く", "行った", "行って", "行かない"],
        "correct_index": 1,
        "translation_vi": "Tôi vẫn chưa từng đi Hokkaido lần nào cả.",
        "explanation_vi": "Nói về kinh nghiệm đã từng (hoặc chưa từng) trải qua trong quá khứ dùng cấu trúc [Vた + ことがある / ことがありません].",
        "option_diagnostics": [
            "[SAI - Nhầm với Vることがある]: Vる+ことがある mang nghĩa 'thỉnh thoảng có lúc đi', không đi với phó từ kinh nghiệm 一度も～ありません.",
            "[ĐÚNG - Vた + ことがありません]: Trải nghiệm quá khứ bắt buộc chia động từ sang thể た (行った).",
            "[SAI - Thể て không nối trực tiếp với ことがある]: Không có mẫu *行ってことがある.",
            "[SAI - Lỗi phủ định kép]: Đã có ことがありません ở cuối câu thì động từ trước đó không chia Vない.",
        ],
    },
    {
        "drill_key": "DR-GP-N5-09-A",
        "grammar_code": "GP-N5-09",
        "drill_type": "application",
        "prompt_jp": "資源を守るためにも、必要以上に魚を（　　）ほうがいい。",
        "options": ["捕らない", "捕る", "捕って", "捕ろう"],
        "correct_index": 0,
        "translation_vi": "Để bảo vệ tài nguyên, không nên đánh bắt cá vượt quá mức cần thiết.",
        "explanation_vi": "Lời khuyên không nên làm gì (trước ほうがいい) dùng thể phủ định ngắn Vない + ほうがいい (tuyệt đối không dùng thể て hay thể ý chí).",
        "option_diagnostics": [
            "[ĐÚNG - Vない + ほうがいい]: Lời khuyên nên tránh làm điều gì luôn dùng thể ない ở động từ đứng trước.",
            "[SAI - Ngược nghĩa câu]: 捕るほうがいい khuyên nên đánh bắt vượt quá mức, mâu thuẫn với mục tiêu bảo vệ tài nguyên.",
            "[SAI - Sai hình thái trước ほうがいい]: Không chia thể て trước ほうがいい.",
            "[SAI - Sai hình thái thể ý chí]: Thể ý chí Vおう không đứng trước ほうがいい.",
        ],
    },
    # --- GP-N5-10 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N5-10-F",
        "grammar_code": "GP-N5-10",
        "drill_type": "formation",
        "prompt_jp": "目のまわりや傷があるところには、この薬を（　　）ください。",
        "options": ["使わない", "使わなくて", "使わないで", "使わずに"],
        "correct_index": 2,
        "translation_vi": "Xin đừng bôi loại thuốc này vào vùng quanh mắt hoặc chỗ có vết thương.",
        "explanation_vi": "Yêu cầu lịch sự 'xin đừng làm V' dùng công thức [Vない + でください] (không dùng なくて hay đứng trần ない).",
        "option_diagnostics": [
            "[SAI - Thiếu trợ từ で]: Phải có で đứng giữa thể ない và ください (Vないでください).",
            "[SAI - Nhầm なくて (nêu nguyên nhân)]: Vなくて dùng để nối nguyên nhân ('vì không làm nên...'), không dùng trước ください.",
            "[ĐÚNG - Công thức Vない + でください]: Nhắc nhở cấm đoán lịch sự trên hướng dẫn sử dụng.",
            "[SAI - Sai hình thái trước ください]: ずに dùng để nối mệnh đề hành động ('mà không làm V1 thì làm V2'), không ghép thành *ずにください.",
        ],
    },
    {
        "drill_key": "DR-GP-N5-10-C",
        "grammar_code": "GP-N5-10",
        "drill_type": "contrast",
        "prompt_jp": "あいさつは人間関係の基本だ。「あいさつなんて」と軽く（　　）。",
        "options": ["考えてみてください", "考えてはいけません", "考えないでいいです", "考えてもかまいません"],
        "correct_index": 1,
        "translation_vi": "Chào hỏi là nền tảng quan hệ con người. Không được phép coi nhẹ kiểu 'chỉ là chào hỏi thôi mà'.",
        "explanation_vi": "Bày tỏ quy tắc nghiêm túc 'không được phép làm gì' dùng [Vて + はいけない / はいけません].",
        "option_diagnostics": [
            "[SAI - Ngược nghĩa]: 考えてみてください nghĩa là 'hãy thử coi nhẹ xem', trái hẳn luận điểm bảo vệ tầm quan trọng của lời chào.",
            "[ĐÚNG - Quy tắc cấm đoán]: 軽く考えてはいけません = không được phép coi nhẹ.",
            "[SAI - Nhầm nghĩa không cần thiết]: 考えないでいいです nghĩa là 'không cần suy nghĩ cũng được', không phải cấm đoán.",
            "[SAI - Nhầm nghĩa cho phép]: 考えてもかまいません nghĩa là 'có coi nhẹ cũng chẳng sao', ngược hoàn toàn mạch bài.",
        ],
    },
    # --- GP-N5-11 (contrast + application) ---
    {
        "drill_key": "DR-GP-N5-11-C",
        "grammar_code": "GP-N5-11",
        "drill_type": "contrast",
        "prompt_jp": "母はもう年をとったので、これ以上無理を（　　）。",
        "options": ["したくない", "してほしくない", "したがっている", "してほしい"],
        "correct_index": 1,
        "translation_vi": "Mẹ tôi đã có tuổi rồi nên tôi không muốn mẹ làm việc quá sức hơn nữa.",
        "explanation_vi": "Người nói mong muốn NGƯỜI KHÁC (mẹ) không làm gì dùng [Vて + ほしくない] (khác với Vたい là chính bản thân mình muốn làm).",
        "option_diagnostics": [
            "[SAI - Nhầm chủ thể hành động]: したくない là 'bản thân TÔI không muốn làm quá sức', không phải mong muốn dành cho mẹ.",
            "[ĐÚNG - Mong muốn đối với người khác]: [母には + 無理をしてほしくない] diễn tả nỗi lo của con không muốn mẹ cố quá sức.",
            "[SAI - Ngược ý hoàn toàn]: したがっている nghĩa là 'mẹ đang muốn làm việc quá sức', không hợp với kết luận khuyên ngăn từ vế 'đã có tuổi rồi'.",
            "[SAI - Ngược nghĩa khẳng định]: してほしい là 'tôi muốn mẹ làm việc quá sức hơn nữa', vô lý với ngữ cảnh.",
        ],
    },
    {
        "drill_key": "DR-GP-N5-11-A",
        "grammar_code": "GP-N5-11",
        "drill_type": "application",
        "prompt_jp": "大学を卒業したら、両親の仕事を手伝い（　　）強く思うようになった。",
        "options": ["たいと", "てほしいと", "たがると", "ようと"],
        "correct_index": 0,
        "translation_vi": "Sau khi tốt nghiệp đại học, tôi ngày càng nghĩ mạnh mẽ rằng muốn phụ giúp công việc của bố mẹ.",
        "explanation_vi": "Chính nhân vật 'tôi' muốn thực hiện hành động giúp đỡ (手伝う) và trích dẫn suy nghĩ trước 思う dùng [Vます + たいと].",
        "option_diagnostics": [
            "[ĐÚNG - Ý muốn của ngôi 1]: 手伝う -> 手伝いたい + と + 思う.",
            "[SAI - Nhầm chiều hành động]: 手伝ってほしいと nghĩa là 'muốn ai đó phụ giúp mình', ngược với việc con muốn phụ giúp bố mẹ.",
            "[SAI - Dùng đuôi ngôi 3 cho bản thân]: たがる chỉ dùng mô tả ngôi thứ 3 từ bên ngoài, không dùng khi tự kể suy nghĩ của chính mình.",
            "[SAI - Sai hình thái]: Trích dẫn ý nghĩ với 思う nếu dùng thể ý chí phải là 手伝おうと (không phải *手伝いようと).",
        ],
    },
    # --- GP-N5-12 (formation + application) ---
    {
        "drill_key": "DR-GP-N5-12-F",
        "grammar_code": "GP-N5-12",
        "drill_type": "formation",
        "prompt_jp": "日本へ留学したとき、近所の花屋さんがお菓子の箱をきれいに包んで（　　）。",
        "options": ["あげた", "くれた", "もらった", "さしあげた"],
        "correct_index": 1,
        "translation_vi": "Khi tôi du học ở Nhật, cô chủ tiệm hoa gần nhà đã gói hộp bánh thật đẹp giúp tôi.",
        "explanation_vi": "Chủ ngữ đi với が là người ngoài (花屋さんが) làm giúp cho bản thân người nói ('tôi') -> BẮT BUỘC dùng てくれた.",
        "option_diagnostics": [
            "[SAI - Ngược chiều Uchi-Soto]: あげた là mình làm cho người khác; người ngoài làm giúp mình tuyệt đối không dùng あげた.",
            "[ĐÚNG - Người ngoài giúp mình (chủ ngữ が)]: 花屋さんが + 包んでくれた.",
            "[SAI - Sai cặp chủ ngữ với もらった]: もらった đòi hỏi NGƯỜI NHẬN (私は花屋さんに) làm chủ ngữ, không đi với chủ ngữ là người cho (花屋さんが).",
            "[SAI - Kính ngữ ngược chiều]: さしあげた là mình làm kính trọng cho người trên, sai hoàn toàn chiều cho-nhận.",
        ],
    },
    {
        "drill_key": "DR-GP-N5-12-A",
        "grammar_code": "GP-N5-12",
        "drill_type": "application",
        "prompt_jp": "私は困ったときに、いつも先輩（　　）相談に乗ってもらっている。",
        "options": ["が", "を", "に", "へ"],
        "correct_index": 2,
        "translation_vi": "Những lúc gặp khó khăn, tôi luôn được đàn anh lắng nghe tư vấn giúp.",
        "explanation_vi": "Khi chủ ngữ là 'tôi' (私は) dùng động từ ～てもらっている, người mang lại sự giúp đỡ (先輩) phải đi với trợ từ に (hoặc から).",
        "option_diagnostics": [
            "[SAI - Nhầm trợ từ với くれる]: Nếu dùng 先輩が thì động từ cuối phải là くれている; ở đây cuối câu là もらっている.",
            "[SAI - Nhầm tân ngữ]: 先輩 không phải đối tượng bị động tác động với を.",
            "[ĐÚNG - Người cho trong cấu trúc もらう]: [私は 先輩に Vてもらう] đánh dấu người giúp bằng に.",
            "[SAI - Nhầm phương hướng]: へ chỉ hướng di chuyển, không đứng trước 相談に乗ってもらう.",
        ],
    },
    # --- GP-N5-13 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N5-13-F",
        "grammar_code": "GP-N5-13",
        "drill_type": "formation",
        "prompt_jp": "この薬は無香料（　　）、においを気にせず使用できます。",
        "options": ["だから", "なので", "のだ", "ので"],
        "correct_index": 1,
        "translation_vi": "Vì loại thuốc này không có hương liệu nên có thể sử dụng mà không cần bận tâm về mùi.",
        "explanation_vi": "無香料 là danh từ, khi nối với ので để nêu nguyên nhân khách quan lịch sự bắt buộc chèn な -> 無香料なので (trong văn bản hướng dẫn ưu tiên なので hơn だから).",
        "option_diagnostics": [
            "[SAI - Văn phong chủ quan hơn trong tờ hướng dẫn]: だから đúng ngữ pháp nhưng mang khẩu khí chủ quan đời thường; trong hướng dẫn sản phẩm chuẩn là なので.",
            "[ĐÚNG - N + な + ので]: Danh từ nối ので phải đổi だ thành な.",
            "[SAI - Thiếu từ nối nhân quả]: のだ chỉ kết thúc giải thích chứ không nối được hai mệnh đề bằng dấu phẩy trong ngữ cảnh này.",
            "[SAI - Thiếu な sau danh từ]: Không gắn trực tiếp ので vào sau danh từ trần (*無香料ので).",
        ],
    },
    {
        "drill_key": "DR-GP-N5-13-C",
        "grammar_code": "GP-N5-13",
        "drill_type": "contrast",
        "prompt_jp": "日本では月にウサギがいると言われるのは、模様がウサギに見える（　　）。",
        "options": ["のですか", "からです", "ので", "し"],
        "correct_index": 1,
        "translation_vi": "Sở dĩ ở Nhật người ta nói có thỏ trên mặt trăng là vì hoa văn trông giống con thỏ.",
        "explanation_vi": "Mẫu giải thích lý do kinh điển [～のは ～からだ / からです] bắt buộc kết thúc bằng からです.",
        "option_diagnostics": [
            "[SAI - Sai ngữ khí câu hỏi]: Câu mở đầu dùng ～のは... nêu mệnh đề giải thích khẳng định, không phải câu hỏi か.",
            "[ĐÚNG - Cặp hô ứng ～のは ～からです]: Định danh nguyên nhân ở cuối câu luôn dùng からです.",
            "[SAI - Thiếu kết thúc câu với ので]: ので dùng nối giữa 2 vế, không đặt kết thúc thay cho からです trong mẫu ～のは～からだ.",
            "[SAI - Nhầm từ liệt kê]: し liệt kê nguyên nhân giữa câu, không chốt câu giải thích ～のは...からです.",
        ],
    },
    # --- GP-N5-14 (contrast + application) ---
    {
        "drill_key": "DR-GP-N5-14-C",
        "grammar_code": "GP-N5-14",
        "drill_type": "contrast",
        "prompt_jp": "最近の高校では、コンピューターが（　　）、外国語が話せたりする授業が人気だ。",
        "options": ["使って", "使えたり", "使うし", "使ったりと"],
        "correct_index": 1,
        "translation_vi": "Ở các trường cấp 3 gần đây, các môn như sử dụng được máy tính hay nói được ngoại ngữ rất được ưa chuộng.",
        "explanation_vi": "Vế sau là '外国語が話せたりする' (thể khả năng chia たり), nên vế trước song hành cũng phải chia thể khả năng + たり -> 使えたり.",
        "option_diagnostics": [
            "[SAI - Sai cấu trúc song hành]: Vế sau dùng ～たりする (liệt kê mẫu ví dụ), không nối bằng thể て đơn thuần.",
            "[ĐÚNG - Song hành V(khả năng)たり～たりする]: 使える -> 使えた + り khớp hoàn toàn với 話せたりする.",
            "[SAI - Lệch dạng liệt kê]: Vế sau dùng たりする nên không kết hợp し ở vế đầu.",
            "[SAI - Dùng sai dạng động từ & thừa と]: 使う chia たり là chủ động ('sử dụng') chứ không phải khả năng ('dùng được'), và không thêm と sau たり.",
        ],
    },
    {
        "drill_key": "DR-GP-N5-14-A",
        "grammar_code": "GP-N5-14",
        "drill_type": "application",
        "prompt_jp": "この店は駅からも（　　）、料理もおいしいので、いつも混んでいる。",
        "options": ["近くて", "近いし", "近かったり", "近くても"],
        "correct_index": 1,
        "translation_vi": "Quán này vừa gần ga, đồ ăn lại vừa ngon nên lúc nào cũng đông khách.",
        "explanation_vi": "Liệt kê nhiều nguyên nhân cộng dồn dẫn đến kết quả 'nên lúc nào cũng đông' dùng mẫu [A1い + し、A2 + ので].",
        "option_diagnostics": [
            "[SAI - Không khớp cấu trúc も～も]: Khi có 駅からも... 料理も... cộng dồn lý do, dùng し tự nhiên và đúng chuẩn hơn て.",
            "[ĐÚNG - Cộng dồn lý do với し]: Tính từ い giữ nguyên trước し (近いし) nối với 料理もおいしいので.",
            "[SAI - Sai ngữ nghĩa liệt kê ngẫu nhiên]: 近かったり dùng khi lúc gần lúc xa, vô lý đối với vị trí cố định của quán.",
            "[SAI - Ngược nghĩa nhượng bộ]: 近くても nghĩa là 'dù có gần đi nữa thì...', trái nghĩa hoàn toàn.",
        ],
    },
    # --- GP-N5-15 (formation + application) ---
    {
        "drill_key": "DR-GP-N5-15-F",
        "grammar_code": "GP-N5-15",
        "drill_type": "formation",
        "prompt_jp": "後ろから車が来てもわからない。（　　）、大きな音を聞き続けると耳も悪くなる。",
        "options": ["しかし", "それに", "それで", "なぜなら"],
        "correct_index": 1,
        "translation_vi": "Xe ô tô tới từ phía sau cũng không biết. Hơn nữa, nếu tiếp tục nghe âm thanh lớn thì tai cũng hỏng.",
        "explanation_vi": "Câu trước nêu nguy hiểm giao thông, câu sau bổ sung thêm tác hại thứ hai đối với thính giác -> liên từ cộng dồn lý do それに.",
        "option_diagnostics": [
            "[SAI - Nhầm liên từ đối lập]: Hai câu cùng chứng minh tác hại của việc bật tai nghe to, không hề đối lập nên loại しかし.",
            "[ĐÚNG - Cộng dồn luận cứ それに]: Nêu thêm lý do/tác hại thứ hai cùng chiều lập luận.",
            "[SAI - Nhầm quan hệ nhân quả]: Việc không biết xe đi tới từ phía sau không phải nguyên nhân sinh ra việc hỏng tai khi nghe lâu.",
            "[SAI - Nhầm giải thích nguyên nhân]: Vế sau không phải nguyên nhân của câu 'không nghe thấy tiếng xe'.",
        ],
    },
    {
        "drill_key": "DR-GP-N5-15-A",
        "grammar_code": "GP-N5-15",
        "drill_type": "application",
        "prompt_jp": "役に立つ科目が大事にされている。（　　）、他の科目も重要であることは変わらない。",
        "options": ["それで", "それから", "しかし", "つまり"],
        "correct_index": 2,
        "translation_vi": "Các môn thực dụng đang được coi trọng. Tuy nhiên, việc các môn học khác cũng quan trọng là điều không đổi.",
        "explanation_vi": "Chuyển từ xu hướng xã hội sang lập luận phản biện khẳng định của tác giả dùng liên từ đối lập しかし.",
        "option_diagnostics": [
            "[SAI - Nhầm nhân quả]: Các môn khác quan trọng không phải kết quả suy ra từ việc môn thực dụng được coi trọng.",
            "[SAI - Nhầm trình tự thời gian]: それから dùng để kể tiếp bước tiếp theo hoặc liệt kê thêm, không thể hiện sự phản biện.",
            "[ĐÚNG - Chuyển hướng đối lập しかし]: Lật ngược lại xu hướng chỉ coi trọng môn thực dụng ở câu trước.",
            "[SAI - Nhầm diễn giải lại]: Câu sau không phải cách nói khác (tóm lại) của câu trước.",
        ],
    },
    # --- GP-N5-16 (contrast + application) ---
    {
        "drill_key": "DR-GP-N5-16-C",
        "grammar_code": "GP-N5-16",
        "drill_type": "contrast",
        "prompt_jp": "明日は午後から（　　）かもしれない。",
        "options": ["雨だ", "雨な", "雨", "雨の"],
        "correct_index": 2,
        "translation_vi": "Ngày mai từ buổi chiều có lẽ sẽ mưa.",
        "explanation_vi": "Trước ～かもしれない, Danh từ và Tính từ な BẮT BUỘC bỏ だ -> nối trực tiếp 雨かもしれない.",
        "option_diagnostics": [
            "[SAI - Lỗi giữ だ trước かもしれない]: Tuyệt đối không nói *雨だかもしれない; danh từ/tính từ な phải lược bỏ だ.",
            "[SAI - Lỗi thêm な sau danh từ]: かもしれない không phải danh từ như ので hay ために nên không thêm な.",
            "[ĐÚNG - Danh từ trần + かもしれない]: Bỏ だ ghép thẳng 雨 + かもしれない.",
            "[SAI - Lỗi thêm の]: Không chèn trợ từ の trước かもしれない.",
        ],
    },
    {
        "drill_key": "DR-GP-N5-16-A",
        "grammar_code": "GP-N5-16",
        "drill_type": "application",
        "prompt_jp": "このまま乱獲（らんかく）が続けば、将来マグロがいなくなって（　　）。",
        "options": ["しまうかもしれない", "しまうはずがない", "しまうに決まっている", "しまったにちがいない"],
        "correct_index": 0,
        "translation_vi": "Nếu tình trạng đánh bắt bừa bãi cứ tiếp diễn như thế này, trong tương lai cá ngừ có thể sẽ biến mất.",
        "explanation_vi": "Dự báo một nguy cơ trong tương lai chưa chắc chắn tuyệt đối 100% dùng Vる + かもしれない.",
        "option_diagnostics": [
            "[ĐÚNG - Phỏng đoán khả năng tương lai]: Vる + かもしれない nêu cảnh báo có thể xảy ra ở tương lai.",
            "[SAI - Ngược nghĩa phủ định]: しまうはずがない nghĩa là 'làm sao có chuyện cá ngừ biến mất được', mâu thuẫn với cảnh báo của đoạn văn.",
            "[SAI - Quả quyết chủ quan quá mức]: Văn nghị luận khoa học/môi trường không khẳng định chủ quan 100% tương lai xa bằng に決まっている.",
            "[SAI - Sai thì quá khứ]: しまった là quá khứ đã xảy ra, không khớp với trạng từ tương lai 将来.",
        ],
    },
    # --- GP-N5-17 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N5-17-F",
        "grammar_code": "GP-N5-17",
        "drill_type": "formation",
        "prompt_jp": "ドイツへ来たばかりなので、ドイツ語はあいさつぐらい（　　）できません。",
        "options": ["だけ", "しか", "ばかり", "さえ"],
        "correct_index": 1,
        "translation_vi": "Vì mới sang Đức nên tiếng Đức tôi chỉ nói được cỡ mấy câu chào hỏi thôi.",
        "explanation_vi": "Cuối câu ở thể phủ định できません và mang sắc thái hạn chế ít ỏi ('chỉ có chừng đó thôi') -> dùng cặp hô ứng [しか + Phủ định].",
        "option_diagnostics": [
            "[SAI - Thiếu sắc thái hạn chế ít ỏi với phủ định]: *あいさつぐらいだけできません dễ hiểu sai thành 'chỉ mỗi câu chào hỏi là tôi không làm được'.",
            "[ĐÚNG - Cặp phủ định giới hạn しか～ない]: Chỉ biết mỗi chừng đó không hơn -> しか + できません.",
            "[SAI - Sai nghĩa 'toàn là']: ばかり không đi với phủ định để diễn tả 'chỉ biết mỗi chừng đó'.",
            "[SAI - Ngược nghĩa cực đoan]: あいさつぐらいさえできません nghĩa là 'đến ngay cả câu chào cũng không biết', lệch nghĩa với câu gốc muốn nói biết được chút ít chào hỏi.",
        ],
    },
    {
        "drill_key": "DR-GP-N5-17-C",
        "grammar_code": "GP-N5-17",
        "drill_type": "contrast",
        "prompt_jp": "この写真集（　　）、私がずっと探していたものだ。",
        "options": ["しか", "こそ", "だけ", "ばかり"],
        "correct_index": 1,
        "translation_vi": "Chính cuốn sách ảnh này là thứ mà tôi đã tìm kiếm bấy lâu nay.",
        "explanation_vi": "Cuối câu là khẳng định だ (loại しか vì しか đòi hỏi phủ định), và ngữ cảnh tìm kiếm bấy lâu nay nhấn mạnh 'chính là cuốn này' -> dùng こそ.",
        "option_diagnostics": [
            "[SAI - Lỗi thiếu phủ định cuối câu]: Cuối câu là khẳng định ものだ nên dùng しか là sai ngữ pháp bắt buộc.",
            "[ĐÚNG - Nhấn mạnh đích danh こそ]: N + こそ làm nổi bật đúng thứ mình tìm kiếm.",
            "[SAI - Sắc thái giới hạn không hợp]: だけ chỉ mang nghĩa 'chỉ mỗi cuốn này', không diễn tả cảm xúc 'chính xác là thứ đã tìm bấy lâu'.",
            "[SAI - Sai nghĩa]: ばかり mang nghĩa 'toàn là', không hợp với một cuốn sách ảnh duy nhất.",
        ],
    },
    # --- GP-N5-18 (contrast + application) ---
    {
        "drill_key": "DR-GP-N5-18-C",
        "grammar_code": "GP-N5-18",
        "drill_type": "contrast",
        "prompt_jp": "今日は体育の授業で、男女が（　　）サッカーをした。",
        "options": ["まぜて", "まざって", "あつめて", "くらべて"],
        "correct_index": 1,
        "translation_vi": "Hôm nay trong giờ thể dục, nam và nữ đã cùng hòa chung chơi bóng đá.",
        "explanation_vi": "Trợ từ ngay trước chỗ trống là が (男女が) nên động từ bắt buộc phải là TỰ ĐỘNG TỪ 混ざる -> まざって.",
        "option_diagnostics": [
            "[SAI - Dùng tha động từ với trợ từ が]: 混ぜる (まぜる) là tha động từ đòi hỏi tân ngữ を (như たまごと牛乳を混ぜる), sai khi đi sau 男女が.",
            "[ĐÚNG - Tự động từ đi với が]: 男女が混ざって = nam nữ hòa lẫn vào nhau.",
            "[SAI - Dùng tha động từ 集める]: 集める là tha động từ (cần を); tự động từ tương ứng phải là 集まる.",
            "[SAI - Sai cả nghĩa lẫn tha động từ]: 比べる (so sánh) là tha động từ đi với を và sai nghĩa câu.",
        ],
    },
    {
        "drill_key": "DR-GP-N5-18-A",
        "grammar_code": "GP-N5-18",
        "drill_type": "application",
        "prompt_jp": "ボウルに卵と牛乳を入れて、よく（　　）ください。",
        "options": ["まざって", "まぜて", "かわいて", "ならんで"],
        "correct_index": 1,
        "translation_vi": "Cho trứng và sữa vào bát rồi hãy trộn đều lên nhé.",
        "explanation_vi": "Vế trước có tân ngữ đi với trợ từ を (卵と牛乳を) nên động từ tiếp theo phải là THA ĐỘNG TỪ 混ぜる -> まぜて.",
        "option_diagnostics": [
            "[SAI - Dùng tự động từ sau tân ngữ を]: まざる là tự động từ, không nhận tân ngữ 卵と牛乳を.",
            "[ĐÚNG - Tha động từ đi với を]: 卵と牛乳を入れて混ぜる = trộn trứng và sữa.",
            "[SAI - Sai nghĩa & là tự động từ]: 乾く (khô) là tự động từ và không hợp bước trộn nguyên liệu.",
            "[SAI - Tự động từ không hợp nghĩa]: 並ぶ (xếp hàng) không dùng cho chất lỏng trứng và sữa.",
        ],
    },
    # --- GP-N4-01 (formation + contrast + application) ---
    {
        "drill_key": "DR-GP-N4-01-F",
        "grammar_code": "GP-N4-01",
        "drill_type": "formation",
        "prompt_jp": "彼女はピアノだけでなく、難しいバイオリンも（　　）そうだ。",
        "options": ["ひく", "ひける", "ひかれる", "ひかせる"],
        "correct_index": 1,
        "translation_vi": "Nghe nói cô ấy không chỉ chơi được piano mà còn chơi được cả đàn violin khó nữa.",
        "explanation_vi": "Động từ Nhóm 1 弾く (ひく) chuyển sang thể khả năng bằng cách đổi đuôi く -> け + る thành 弾ける (ひける).",
        "option_diagnostics": [
            "[SAI - Dùng nguyên thể thay khả năng]: 弾く chỉ hành động bình thường, ở đây ngữ cảnh khen tài năng chơi được cả nhạc cụ khó cần thể khả năng.",
            "[ĐÚNG - Thể khả năng Nhóm 1]: 弾く (hàng か cột う) -> 弾ける (cột え + る).",
            "[SAI - Nhầm thể bị động]: 弾かれる nghĩa là 'bị chơi / bị đánh bật', không phải khả năng chơi đàn của cô ấy.",
            "[SAI - Nhầm thể sai khiến]: 弾かせる nghĩa là 'bắt người khác chơi đàn'.",
        ],
    },
    {
        "drill_key": "DR-GP-N4-01-C",
        "grammar_code": "GP-N4-01",
        "drill_type": "contrast",
        "prompt_jp": "必要なときにすぐ（　　）ように、説明書は引き出しに入れておきます。",
        "options": ["読む", "読める", "読まれる", "読ませる"],
        "correct_index": 1,
        "translation_vi": "Để có thể đọc được ngay vào lúc cần thiết, tôi cất tờ hướng dẫn vào ngăn kéo.",
        "explanation_vi": "Để diễn đạt mục đích tạo ra khả năng có thể làm V trong tương lai, kết hợp Thể khả năng (読める) + ように.",
        "option_diagnostics": [
            "[SAI - V ý chí đi với ように tạo nghĩa khác]: 読むように nghĩa là 'hãy đọc / cố gắng đọc', không mang nghĩa 'để có thể đọc được khi cần'.",
            "[ĐÚNG - Thể khả năng + ように]: 読めるように = để có thể đọc được.",
            "[SAI - Nhầm thể bị động]: 読まれる là 'bị người khác đọc'.",
            "[SAI - Nhầm thể sai khiến]: 読ませる là 'bắt/cho phép người khác đọc'.",
        ],
    },
    {
        "drill_key": "DR-GP-N4-01-A",
        "grammar_code": "GP-N4-01",
        "drill_type": "application",
        "prompt_jp": "毎日少しずつ練習したおかげで、やっと漢字が（　　）ようになった。",
        "options": ["書く", "書ける", "書かれる", "書かせる"],
        "correct_index": 1,
        "translation_vi": "Nhờ luyện tập mỗi ngày một chút, cuối cùng tôi đã trở nên viết được chữ Kanji rồi.",
        "explanation_vi": "Mẫu ～ようになる biểu thị sự biến đổi năng lực từ chưa biết sang có thể làm -> đi với Thể khả năng (書ける) và trợ từ が (漢字が).",
        "option_diagnostics": [
            "[SAI - Thiếu thể khả năng]: Với trợ từ 漢字が và ý nghĩa 'đạt được năng lực viết', dùng 書く không diễn tả được khả năng.",
            "[ĐÚNG - Khả năng + ようになる]: 書く -> 書ける + ようになった.",
            "[SAI - Nhầm thể bị động]: 書かれる là 'chữ Kanji bị viết'.",
            "[SAI - Nhầm thể sai khiến]: 書かせる là 'bắt ai viết'.",
        ],
    },
    # --- GP-N4-02 (contrast + application) ---
    {
        "drill_key": "DR-GP-N4-02-C",
        "grammar_code": "GP-N4-02",
        "drill_type": "contrast",
        "prompt_jp": "両親は、私がずっと行きたいと言っていた日本へ（　　）くれた。",
        "options": ["留学して", "留学されて", "留学させて", "留学できて"],
        "correct_index": 2,
        "translation_vi": "Bố mẹ đã cho phép tôi đi du học ở Nhật — nơi tôi luôn nói muốn tới.",
        "explanation_vi": "Khi chủ thể (bố mẹ) CHO PHÉP người khác (tôi) làm hành động gì và được biết ơn (くれた), dùng Thể sai khiến 留学させる -> 留学させてくれた.",
        "option_diagnostics": [
            "[SAI - Nhầm người thực hiện]: 留学してくれた sẽ có nghĩa là 'bố mẹ tự đi du học giùm tôi', sai chủ thể hành động.",
            "[SAI - Nhầm thể bị động]: 留学された là bố mẹ chịu thiệt hại vì việc đi du học, không kết hợp くれた.",
            "[ĐÚNG - Sai khiến cho phép + くれた]: 留学させてくれた = đã tạo điều kiện cho phép tôi đi du học.",
            "[SAI - Nhầm thể khả năng]: 留学できてくれた là sai cấu trúc ngữ pháp vì khả năng không gắn くれた.",
        ],
    },
    {
        "drill_key": "DR-GP-N4-02-A",
        "grammar_code": "GP-N4-02",
        "drill_type": "application",
        "prompt_jp": "学校では、子どもたちにいろいろな科目をバランスよく（　　）工夫が必要だ。",
        "options": ["学習して", "学習させる", "学習される", "学習できる"],
        "correct_index": 1,
        "translation_vi": "Ở trường học, cần có phương pháp giúp cho học sinh học cân bằng nhiều môn khác nhau.",
        "explanation_vi": "Nhà trường/giáo viên tổ chức, hướng dẫn giúp học sinh (子どもたちに) học -> dùng Thể sai khiến 学習させる bổ nghĩa cho 工夫.",
        "option_diagnostics": [
            "[SAI - Thể て không bổ nghĩa danh từ 工夫]: Thể て không thể đứng làm định ngữ trực tiếp trước danh từ 工夫.",
            "[ĐÚNG - Sai khiến bổ nghĩa danh từ]: 子どもたちに + 学習させる + 工夫.",
            "[SAI - Nhầm thể bị động]: 学習される là 'bị học', sai vai trò chủ thể nhà trường.",
            "[SAI - Nhầm chủ thể khả năng]: Trường học tạo phương pháp giúp học sinh học (tác động sang học sinh), dùng させる chuẩn xác hơn できる.",
        ],
    },
    # --- GP-N4-03 (formation + application) ---
    {
        "drill_key": "DR-GP-N4-03-F",
        "grammar_code": "GP-N4-03",
        "drill_type": "formation",
        "prompt_jp": "マグロは海外でも人気があるため、世界中で大量に（　　）いる。",
        "options": ["捕って", "捕られて", "捕らせて", "捕れて"],
        "correct_index": 1,
        "translation_vi": "Vì cá ngừ được ưa chuộng cả ở nước ngoài nên bị đánh bắt với số lượng lớn trên khắp thế giới.",
        "explanation_vi": "Chủ ngữ là マグロは (đối tượng bị con người đánh bắt), nên động từ 捕る (とる - Nhóm 1) phải chia sang thể bị động 捕られる -> 捕られている.",
        "option_diagnostics": [
            "[SAI - Dùng thể chủ động]: Cá ngừ không tự mình đi đánh bắt nên không dùng 捕っている.",
            "[ĐÚNG - Thể bị động Nhóm 1]: 捕る (tận cùng る) -> cột あ là ら + れる -> 捕られる -> 捕られている.",
            "[SAI - Nhầm thể sai khiến]: 捕らせて nghĩa là cá ngừ sai bảo ai đi bắt.",
            "[SAI - Nhầm thể khả năng]: 捕れて nghĩa là 'bắt được' (thường đi với が để nói ngư dân đánh bắt được nhiều), ở đây chủ đề là マグロは bị khai thác.",
        ],
    },
    {
        "drill_key": "DR-GP-N4-03-A",
        "grammar_code": "GP-N4-03",
        "drill_type": "application",
        "prompt_jp": "その泥棒は、店から逃げようとしたところを警察に（　　）。",
        "options": ["逮捕した", "逮捕された", "逮捕させた", "逮捕できた"],
        "correct_index": 1,
        "translation_vi": "Tên trộm đó đúng lúc định bỏ trốn khỏi cửa hàng thì bị cảnh sát bắt giữ.",
        "explanation_vi": "Chủ ngữ là tên trộm (泥棒は), tác nhân thực hiện bắt là cảnh sát (警察に) -> câu bị động trực tiếp 逮捕された.",
        "option_diagnostics": [
            "[SAI - Ngược chủ động/bị động]: 逮捕した sẽ thành 'tên trộm bắt giữ cảnh sát', ngược hoàn toàn ngữ nghĩa.",
            "[ĐÚNG - Câu bị động 警察に～された]: Chủ thể chịu tác động là tên trộm nên chia 逮捕された.",
            "[SAI - Nhầm thể sai khiến]: 逮捕させた nghĩa là tên trộm sai cảnh sát đi bắt người.",
            "[SAI - Nhầm thể khả năng]: 逮捕できた không đi với tác nhân 警察に.",
        ],
    },
    # --- GP-N4-04 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N4-04-F",
        "grammar_code": "GP-N4-04",
        "drill_type": "formation",
        "prompt_jp": "駅でバスがなかなか来なくて、寒い中20分も（　　）。",
        "options": ["待たれた", "待たせた", "待たされた", "待てられた"],
        "correct_index": 2,
        "translation_vi": "Ở trạm xe buýt mãi không tới nên tôi bị bắt đợi suốt 20 phút giữa trời lạnh.",
        "explanation_vi": "Chủ thể chịu cảnh phải chờ đợi khổ sở ngoài ý muốn dùng Thể sai khiến bị động: 待つ (Nhóm 1) -> 待たされる -> 待たされた.",
        "option_diagnostics": [
            "[SAI - Dùng bị động đơn thuần]: 待たれた nghĩa là 'được người ta mong đợi', không diễn tả cảm giác bị bắt đứng chờ khổ sở.",
            "[SAI - Ngược chủ thể sai khiến]: 待たせた nghĩa là 'tôi đã bắt xe buýt đợi mình', ngược vai trò.",
            "[ĐÚNG - Sai khiến bị động Nhóm 1]: 待つ -> cột あ là た + される -> 待たされた (rút gọn của 待たせられた).",
            "[SAI - Sai quy tắc biến âm]: Không lấy gốc khả năng *待て để gắn られた.",
        ],
    },
    {
        "drill_key": "DR-GP-N4-04-C",
        "grammar_code": "GP-N4-04",
        "drill_type": "contrast",
        "prompt_jp": "子どもの頃、母に毎日ピアノを（　　）。",
        "options": ["練習させた", "練習された", "練習させられた", "練習できた"],
        "correct_index": 2,
        "translation_vi": "Hồi nhỏ ngày nào tôi cũng bị mẹ bắt luyện tập đàn piano.",
        "explanation_vi": "Khi thấy trợ từ tác nhân 母に ở phía trước ('bị mẹ bắt...') mà không có tân ngữ 'con' đứng với を, chủ ngữ là chính 'tôi' -> dùng Sai khiến bị động 練習させられた.",
        "option_diagnostics": [
            "[SAI - Ngược chiều sai khiến]: 母に練習させた nghĩa là 'tôi bắt mẹ luyện đàn', sai vai vế.",
            "[SAI - Bị động trực tiếp không hợp ngữ cảnh ép buộc]: 練習された chỉ mang nghĩa thụ động bình thường hoặc bị mẹ tập mất phần, thiếu sắc thái 'bị mẹ bắt phải tập'.",
            "[ĐÚNG - Sai khiến bị động Nhóm 3]: する -> させられる -> 練習させられた.",
            "[SAI - Sai trợ từ với khả năng]: Thể khả năng không đi với tác nhân 母に.",
        ],
    },
    # --- GP-N4-05 (contrast + application) ---
    {
        "drill_key": "DR-GP-N4-05-C",
        "grammar_code": "GP-N4-05",
        "drill_type": "contrast",
        "prompt_jp": "会議が始まる前に、資料を机の上に（　　）ください。",
        "options": ["並べてある", "並べておいて", "並んでおいて", "並べてしまって"],
        "correct_index": 1,
        "translation_vi": "Trước khi cuộc họp bắt đầu, hãy xếp sẵn tài liệu lên trên bàn giúp tôi.",
        "explanation_vi": "Yêu cầu người nghe thực hiện hành động chuẩn bị trước khi sự việc diễn ra dùng Tha động từ + ておく -> 並べておいてください.",
        "option_diagnostics": [
            "[SAI - Không dùng てある cho mệnh lệnh chuẩn bị]: てある mô tả trạng thái đã có sẵn từ trước, không kết hợp với ください để nhờ người khác làm sẵn.",
            "[ĐÚNG - Tha động từ + ておく + ください]: 資料を + 並べる (tha động từ) -> 並べておいてください.",
            "[SAI - Dùng tự động từ cho tân ngữ 資料を]: 並ぶ là tự động từ, không nhận tân ngữ 資料を.",
            "[SAI - Nhầm てしまう]: てしまって chỉ sự hoàn tất lỡ mất, không mang nghĩa chuẩn bị sẵn cho cuộc họp.",
        ],
    },
    {
        "drill_key": "DR-GP-N4-05-A",
        "grammar_code": "GP-N4-05",
        "drill_type": "application",
        "prompt_jp": "次の会議で話し合いたいことがあれば、事前に（　　）おいてください。",
        "options": ["考えて", "考えられて", "考えあって", "考えさせて"],
        "correct_index": 0,
        "translation_vi": "Nếu có điều gì muốn thảo luận trong cuộc họp tới, hãy nghĩ sẵn trước đi nhé.",
        "explanation_vi": "Chủ động chuẩn bị trước suy nghĩ/ý tưởng dùng Vて + おく -> 考えておいてください.",
        "option_diagnostics": [
            "[ĐÚNG - Vて + おいてください]: 考える -> 考えて + おいてください (nghĩ chuẩn bị trước).",
            "[SAI - Nhầm thể bị động]: Không dùng thể bị động trong lời nhắc nhở thành viên tự suy nghĩ trước.",
            "[SAI - Lỗi ghép động từ 考えあう]: Sai dạng chia て của 考え合う (考え合って) và sai nghĩa chuẩn bị cá nhân.",
            "[SAI - Nhầm thể sai khiến]: Không mang nghĩa 'bắt ai nghĩ sẵn'.",
        ],
    },
    # --- GP-N4-06 (formation + application) ---
    {
        "drill_key": "DR-GP-N4-06-F",
        "grammar_code": "GP-N4-06",
        "drill_type": "formation",
        "prompt_jp": "木村さんの机の上に、先生からのメモが（　　）。",
        "options": ["置いておいた", "置いてある", "置かれてきた", "置いている"],
        "correct_index": 1,
        "translation_vi": "Trên bàn của anh Kimura có đặt sẵn tờ lời nhắn từ thầy giáo.",
        "explanation_vi": "Đối tượng đi với trợ từ が (メモが) và diễn tả trạng thái hiện tại do ai đó chủ động đặt sẵn lên bàn -> dùng Tha động từ + てある (置いてある).",
        "option_diagnostics": [
            "[SAI - Sai trợ từ với ておく]: ておく nhấn mạnh hành động chủ động của người đặt (先生がメモを置いておいた), không đi với chủ ngữ メモが.",
            "[ĐÚNG - Nが + Tha động từ てある]: 置く (tha động từ) chia 置いてある mô tả kết quả hiện hữu.",
            "[SAI - Sai trục thời gian lịch sử]: 置かれてきた mang nghĩa 'được đặt liên tục từ xưa đến nay', không phù hợp tờ giấy nhắn trên bàn.",
            "[SAI - Sai tha động từ với ている]: 置く là tha động từ, chia 置いている mang nghĩa 'đang thực hiện động tác đặt', không đi với chủ ngữ メモが.",
        ],
    },
    {
        "drill_key": "DR-GP-N4-06-A",
        "grammar_code": "GP-N4-06",
        "drill_type": "application",
        "prompt_jp": "来客があるので、玄関にはきれいな花が（　　）。",
        "options": ["飾ってある", "飾っておく", "飾っている", "飾られていく"],
        "correct_index": 0,
        "translation_vi": "Vì sắp có khách tới nên ở lối vào có cắm trang trí sẵn bình hoa đẹp.",
        "explanation_vi": "Chủ ngữ 花が mô tả trạng thái bông hoa đang được cắm bày sẵn có chủ đích của gia chủ -> 花が飾ってある.",
        "option_diagnostics": [
            "[ĐÚNG - Trạng thái kết quả có chủ ý]: 飾る (tha động từ) + てある với chủ ngữ 花が.",
            "[SAI - Lệch trợ từ với ておく]: Nếu dùng ておく (sẽ cắm sẵn) thì phải là 花を飾っておく.",
            "[SAI - Thiếu tân ngữ/sai chủ thể]: 飾っている chỉ hành động người đang cắm (tân ngữ を), không dùng cho chủ ngữ 花が.",
            "[SAI - Sai hướng thời gian tương lai]: 飾られていく hướng tương lai kéo dài, không diễn tả cảnh bày sẵn ngay trước mắt.",
        ],
    },
    # --- GP-N4-07 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N4-07-F",
        "grammar_code": "GP-N4-07",
        "drill_type": "formation",
        "prompt_jp": "最近、だんだん朝晩が（　　）きましたね。",
        "options": ["寒い", "寒く", "寒くなって", "寒くて"],
        "correct_index": 2,
        "translation_vi": "Gần đây sáng tối dần dần trở nên lạnh lên rồi nhỉ.",
        "explanation_vi": "Để nói tính chất bắt đầu biến đổi dần tới hiện tại dùng [Aく + なる] chia thể て + くる -> 寒くなってきました.",
        "option_diagnostics": [
            "[SAI - Không ghép trực tiếp tính từ với くる]: 寒い + くる là sai cấu trúc ngữ pháp.",
            "[SAI - Thiếu động từ biến đổi なって]: 寒く + くる không tạo thành cụm biến chuyển trạng thái (trừ động từ đi lại); phải qua なって.",
            "[ĐÚNG - Aい(く) + なって + くる]: 寒くなってきました = đã trở nên lạnh dần tới giờ.",
            "[SAI - Thể て của tính từ không ghép くる]: 寒くてきました là sai hình thái.",
        ],
    },
    {
        "drill_key": "DR-GP-N4-07-C",
        "grammar_code": "GP-N4-07",
        "drill_type": "contrast",
        "prompt_jp": "私は小さいころから、くだものを作っている両親を（　　）。",
        "options": ["見ていきました", "見て育ってきました", "見ておきました", "見てしまいました"],
        "correct_index": 1,
        "translation_vi": "Từ hồi nhỏ đến giờ tôi đã lớn lên khi chứng kiến bố mẹ làm vườn cây ăn quả.",
        "explanation_vi": "Mốc thời gian '小さいころから' (từ nhỏ tới hiện tại) yêu cầu hướng thời gian tiến về hiện tại ～てくる -> 見て育ってきました.",
        "option_diagnostics": [
            "[SAI - Ngược trục thời gian]: ていく hướng từ hiện tại về tương lai, không dùng cho hồi ức 'từ nhỏ đến nay'.",
            "[ĐÚNG - Quá khứ -> Hiện tại với てくる]: 小さいころから kết hợp 育ってきました.",
            "[SAI - Sai nghĩa chuẩn bị trước]: ておく chỉ việc làm sẵn cho sự việc sắp tới.",
            "[SAI - Sai sắc thái hoàn tất/tiếc nuối]: てしまう không diễn tả quá trình lớn lên liên tục từ nhỏ tới giờ.",
        ],
    },
    # --- GP-N4-08 (contrast + application) ---
    {
        "drill_key": "DR-GP-N4-08-C",
        "grammar_code": "GP-N4-08",
        "drill_type": "contrast",
        "prompt_jp": "赤ちゃんのころ持っていた共感覚も、普通は成長すると（　　）ものだそうだ。",
        "options": ["失われていく", "失われてきた", "失っておく", "失ってある"],
        "correct_index": 0,
        "translation_vi": "Cảm giác kèm có hồi sơ sinh thông thường khi lớn lên sẽ mất dần đi.",
        "explanation_vi": "Từ mốc tuổi nhỏ tiến về tương lai trưởng thành và mang sắc thái tiêu biến dần đi dùng ～ていく -> 失われていく.",
        "option_diagnostics": [
            "[ĐÚNG - Tiến trình mất dần về tương lai]: Bị động 失われる + ていく diễn tả sự phai nhạt dần khi lớn lên.",
            "[SAI - Ngược hướng quy luật phát triển]: てきた nhìn ngược từ quá khứ về hiện tại của người nói, không dùng cho quy luật tổng quát 'lớn lên rồi sẽ mất đi'.",
            "[SAI - Sai chủ ý và nghĩa]: ておく chỉ hành động có chủ đích chuẩn bị trước, không dùng cho việc bị mất tự nhiên.",
            "[SAI - Sai cấu trúc]: てある chỉ gắn với tha động từ mô tả vật hiện hữu, không đi với 失う.",
        ],
    },
    {
        "drill_key": "DR-GP-N4-08-A",
        "grammar_code": "GP-N4-08",
        "drill_type": "application",
        "prompt_jp": "これからも日本の自然環境を大切に（　　）たいと思っています。",
        "options": ["守っていきたい", "守ってきた", "守っておきたい", "守ってある"],
        "correct_index": 0,
        "translation_vi": "Từ nay về sau tôi cũng muốn tiếp tục trân trọng và bảo vệ môi trường thiên nhiên Nhật Bản.",
        "explanation_vi": "Từ khóa tương lai 'これからも' (từ nay về sau) kết hợp mong muốn duy trì lâu dài dùng Vて + いく -> 守っていきたい.",
        "option_diagnostics": [
            "[ĐÚNG - Duy trì về tương lai]: これからも luôn hô ứng với ていく.",
            "[SAI - Sai thì quá khứ với これからも]: これからも chỉ tương lai, mâu thuẫn với quá khứ 守ってきた.",
            "[SAI - Sai sắc thái hành động một lần]: ておく chỉ làm sẵn một việc trước một mốc cụ thể, không chỉ sự duy trì lâu dài suốt tương lai.",
            "[SAI - Sai cấu trúc và nghĩa]: てある không kết hợp với たい và không biểu đạt ý chí bảo vệ tương lai.",
        ],
    },
    # --- GP-N4-09 (formation + application) ---
    {
        "drill_key": "DR-GP-N4-09-F",
        "grammar_code": "GP-N4-09",
        "drill_type": "formation",
        "prompt_jp": "プレゼント用だと入力するのを（　　）、箱がラッピングされていなかった。",
        "options": ["忘れるしまって", "忘れてしまい", "忘れてある", "忘れておき"],
        "correct_index": 1,
        "translation_vi": "Tôi lỡ quên nhập mục làm quà tặng nên chiếc hộp đã không được gói.",
        "explanation_vi": "Lỡ làm gì đáng tiếc dùng Vて + しまう; nối tiếp sang vế nguyên nhân bằng dạng liên dụng Vます bỏ ます -> 忘れてしまい (hoặc 忘れてしまって).",
        "option_diagnostics": [
            "[SAI - Chia nguyên thể trước しまう]: Phải chia động từ 忘れる sang thể て (忘れて) mới gắn しまう.",
            "[ĐÚNG - Thể て + しまい (lối viết liên dụng)]: Diễn tả sai sót ngoài ý muốn gây hậu quả.",
            "[SAI - Sai ý nghĩa và tha động từ]: てある không đi với 忘れる để chỉ sự lỡ quên.",
            "[SAI - Ngược nghĩa]: ておく là cố ý chuẩn bị sẵn, hoàn toàn trái nghĩa với sự cố quên.",
        ],
    },
    {
        "drill_key": "DR-GP-N4-09-A",
        "grammar_code": "GP-N4-09",
        "drill_type": "application",
        "prompt_jp": "一生けん命仕事をしていたら、いつのまにか夜に（　　）。",
        "options": ["なっておいた", "なってしまった", "なってあった", "なってくれた"],
        "correct_index": 1,
        "translation_vi": "Mải làm việc chăm chỉ, chẳng biết từ lúc nào trời đã tối mất rồi.",
        "explanation_vi": "Diễn biến ngoài tầm kiểm soát khiến người nói bất ngờ/tiếc thời gian trôi nhanh đi cùng いつのまにか -> なってしまった.",
        "option_diagnostics": [
            "[SAI - Không dùng ておく cho tự nhiên]: Đêm tối đến không phải hành động chủ ý chuẩn bị trước của con người.",
            "[ĐÚNG - Kết thúc ngoài ý muốn]: いつのまにか thường kết thúc bằng てしまった.",
            "[SAI - Sai cấu trúc tự động từ]: なる là tự động từ không đi với てある.",
            "[SAI - Sai ngữ nghĩa biết ơn]: てくれた diễn tả ai đó làm giúp mình với lòng biết ơn, không hợp 'lúc nào không hay đã tối'.",
        ],
    },
    # --- GP-N4-10 (formation + contrast + application) ---
    {
        "drill_key": "DR-GP-N4-10-F",
        "grammar_code": "GP-N4-10",
        "drill_type": "formation",
        "prompt_jp": "この本は字が大きくて、とても（　　）。",
        "options": ["読むやすいです", "読みやすいです", "読んでやすいです", "読めやすいです"],
        "correct_index": 1,
        "translation_vi": "Cuốn sách này chữ to nên rất dễ đọc.",
        "explanation_vi": "Hậu tố ～やすい / ～にくい BẮT BUỘC gắn sau gốc động từ Vます bỏ ます (読む -> 読みやすい).",
        "option_diagnostics": [
            "[SAI - Giữ nguyên thể Vる]: Không gắn やすい vào thể từ điển *読むやすい.",
            "[ĐÚNG - Vます(bỏ ます) + やすい]: 読む -> 読み + やすい.",
            "[SAI - Gắn sau thể て]: Không gắn やすい vào sau thể て (*読んでやすい).",
            "[SAI - Gắn vào thể khả năng]: Tự thân やすい đã biểu thị độ dễ thực hiện nên không ghép vào gốc khả năng (*読めやすい).",
        ],
    },
    {
        "drill_key": "DR-GP-N4-10-C",
        "grammar_code": "GP-N4-10",
        "drill_type": "contrast",
        "prompt_jp": "長時間大きな音を聞き続けると、小さい音が（　　）なるそうだ。",
        "options": ["聞こえにくい", "聞こえにくく", "聞こえにくいに", "聞こえられにくい"],
        "correct_index": 1,
        "translation_vi": "Nghe nói nếu tiếp tục nghe âm thanh lớn trong thời gian dài thì sẽ trở nên khó nghe thấy âm thanh nhỏ.",
        "explanation_vi": "聞こえにくい là tính từ đuôi い, nên trước động từ biến đổi なる phải đổi い thành く -> 聞こえにくくなる.",
        "option_diagnostics": [
            "[SAI - Thiếu biến đổi く trước なる]: Không đặt trực tiếp đuôi い nguyên vẹn ngay trước なる.",
            "[ĐÚNG - Đuôi い đổi thành く + なる]: 聞こえにくい -> 聞こえにくく + なる.",
            "[SAI - Nhầm sang chia tính từ な]: Đuôi にくい là tính từ い, không thêm に như *にくいに.",
            "[SAI - Thừa thể bị động]: 聞こえる là tự động từ tri giác tự nhiên, không chia *聞こえられる trước にくい.",
        ],
    },
    {
        "drill_key": "DR-GP-N4-10-A",
        "grammar_code": "GP-N4-10",
        "drill_type": "application",
        "prompt_jp": "石井さんはキクの花のタブーについて、少し（　　）話した。",
        "options": ["言いやすそうに", "言いにくそうに", "言いやすく", "言いたそうに"],
        "correct_index": 1,
        "translation_vi": "Anh Ishii đã nói về điều kiêng kỵ của hoa cúc với vẻ hơi khó mở lời (ngại ngùng).",
        "explanation_vi": "Nói điều có thể làm khách ngượng ngùng/buồn (tặng hoa đám tang khi đi thăm bệnh) dùng 言いにくい + そうに (trông có vẻ khó nói).",
        "option_diagnostics": [
            "[SAI - Ngược nghĩa tâm lý]: 言いやすそう nghĩa là 'trông rất dễ nói/hồ hởi nói', trái với hoàn cảnh tế nhị.",
            "[ĐÚNG - Vます + にくい + そうに]: 言いにくそうに = với vẻ mặt khó mở lời.",
            "[SAI - Ngược nghĩa]: 言いやすく nghĩa là 'một cách dễ nói'.",
            "[SAI - Sai ngữ cảnh]: 言いたそうに nghĩa là 'trông rất muốn nói/nóng lòng muốn nói', không phù hợp sự ngại ngùng.",
        ],
    },
    # --- GP-N4-11 (formation + contrast + application) ---
    {
        "drill_key": "DR-GP-N4-11-F",
        "grammar_code": "GP-N4-11",
        "drill_type": "formation",
        "prompt_jp": "寒い季節になってきたので、風邪をひかない（　　）気をつけている。",
        "options": ["ために", "ように", "ための", "ような"],
        "correct_index": 1,
        "translation_vi": "Vì đã bước sang mùa lạnh nên tôi đang chú ý để không bị cảm cúm.",
        "explanation_vi": "Động từ đứng trước là dạng phủ định không ý chí (ひかない = không bị cảm) nên bắt buộc chọn ように (không bao giờ dùng ために sau Vない).",
        "option_diagnostics": [
            "[SAI - Sai quy tắc kết hợp với Vない]: ために chỉ đi với động từ ý chí khẳng định Vる, không kết hợp với phủ định trạng thái *ひかないために.",
            "[ĐÚNG - Vない + ように]: Biểu thị mục đích phòng tránh trạng thái ngoài ý muốn (để không bị...).",
            "[SAI - Nhầm hình thái bổ nghĩa danh từ]: ための chỉ đứng trước danh từ, không đứng trước động từ 気をつけている.",
            "[SAI - Nhầm hình thái bổ nghĩa danh từ]: ような chỉ đứng trước danh từ, không dùng nối sang động từ 気をつけている.",
        ],
    },
    {
        "drill_key": "DR-GP-N4-11-C",
        "grammar_code": "GP-N4-11",
        "drill_type": "contrast",
        "prompt_jp": "必要なときに辞書がすぐ（　　）ように、いつもカバンに入れている。",
        "options": ["使う", "使える", "使われる", "使った"],
        "correct_index": 1,
        "translation_vi": "Để có thể dùng được từ điển ngay khi cần thiết, tôi luôn bỏ sẵn vào cặp.",
        "explanation_vi": "Mục đích tạo ra trạng thái có thể thực hiện được khi cần thiết kết hợp với ように phải dùng Thể khả năng (使える).",
        "option_diagnostics": [
            "[SAI - Nhầm V ý chí với ように]: 使うように mang nghĩa 'cố gắng dùng / bảo dùng', không diễn đạt mục đích 'để có thể dùng khi cần'.",
            "[ĐÚNG - Thể khả năng + ように]: 使えるように = để có thể dùng được.",
            "[SAI - Nhầm thể bị động]: 辞書が + 使われるように không diễn tả ý định của người bỏ từ điển vào cặp để tự mình sử dụng.",
            "[SAI - Sai thì quá khứ]: Trước ように chỉ mục đích không bao giờ dùng thì quá khứ Vた.",
        ],
    },
    {
        "drill_key": "DR-GP-N4-11-A",
        "grammar_code": "GP-N4-11",
        "drill_type": "application",
        "prompt_jp": "後ろの席の人にもしっかり（　　）、大きな声でゆっくり話した。",
        "options": ["聞こえるために", "聞こえるように", "聞くために", "聞くための"],
        "correct_index": 1,
        "translation_vi": "Tôi đã nói chậm rãi bằng giọng to để người ngồi hàng ghế sau cũng có thể nghe thấy rõ.",
        "explanation_vi": "Động từ tri giác không ý chí 聞こえる (nghe thấy) và khác chủ ngữ (tôi nói để người sau nghe) -> bắt buộc dùng ように.",
        "option_diagnostics": [
            "[SAI - Dùng ために với động từ không ý chí và khác chủ ngữ]: 聞こえる không mang ý chí chủ động và có chủ ngữ khác với vế sau, cấm dùng ために.",
            "[ĐÚNG - Khác chủ ngữ + V không ý chí + ように]: 後ろの人にも聞こえるように.",
            "[SAI - Sai chủ thể hành động]: 聞く là hành động chủ động của người nghe; người nói không làm thay hành động 聞く.",
            "[SAI - Sai hình thái]: ための phải bổ nghĩa cho danh từ ngay phía sau.",
        ],
    },
    # --- GP-N4-12 (formation + contrast + application) ---
    {
        "drill_key": "DR-GP-N4-12-F",
        "grammar_code": "GP-N4-12",
        "drill_type": "formation",
        "prompt_jp": "体の大きな選手たちの中で（　　）ためには、高い技術が必要である。",
        "options": ["戦える", "戦う", "戦った", "戦わない"],
        "correct_index": 1,
        "translation_vi": "Để chiến đấu giữa những vận động viên to cao, cần phải có kỹ thuật cao.",
        "explanation_vi": "Trước ために chỉ mục đích trực tiếp của động từ có ý chí, BẮT BUỘC chia về nguyên thể ý chí Vる (戦う), cấm dùng thể khả năng Vえる hay Vた.",
        "option_diagnostics": [
            "[SAI - Bẫy kết hợp Vえる + ために]: Thể khả năng (戦える) tuyệt đối không đi với ために (phải đi với ように).",
            "[ĐÚNG - Vる(ý chí) + ために]: 戦う là hành động chủ động có mục tiêu rõ ràng -> 戦うために.",
            "[SAI - Sai thì trước ために chỉ mục đích]: Vた + ために biến thành nghĩa nguyên nhân ('vì đã chiến đấu nên...'), sai với mục tiêu cần đạt ở vế sau.",
            "[SAI - Sai nghĩa và cấu trúc]: Vない không kết hợp với ために chỉ mục đích phòng tránh.",
        ],
    },
    {
        "drill_key": "DR-GP-N4-12-C",
        "grammar_code": "GP-N4-12",
        "drill_type": "contrast",
        "prompt_jp": "子どもたちが安心して（　　）、安全な遊び場を増やしている。",
        "options": ["遊べるために", "遊べるように", "遊ぶために", "遊ぶための"],
        "correct_index": 1,
        "translation_vi": "Người ta đang tăng thêm sân chơi an toàn để trẻ em có thể vui chơi yên tâm.",
        "explanation_vi": "Chủ ngữ hai vế khác nhau (chính quyền/người lớn tăng sân chơi để TRẺ EM có thể chơi) và dùng thể khả năng 遊べる -> bắt buộc chọn ように.",
        "option_diagnostics": [
            "[SAI - Lỗi kép Vえる + ために và khác chủ ngữ]: 遊べる là thể khả năng và khác chủ ngữ với vế sau nên không được dùng ために.",
            "[ĐÚNG - Khác chủ ngữ + V khả năng + ように]: 子どもたちが遊べるように.",
            "[SAI - Bẫy chủ ngữ khác nhau với ために]: ために đòi hỏi cùng 1 chủ ngữ thực hiện cả 2 hành động ('tôi làm X để tôi đạt Y').",
            "[SAI - Sai hình thái]: ための phải đứng trực tiếp trước danh từ.",
        ],
    },
    {
        "drill_key": "DR-GP-N4-12-A",
        "grammar_code": "GP-N4-12",
        "drill_type": "application",
        "prompt_jp": "台風による大雨（　　）、本日の試合は中止とさせていただきます。",
        "options": ["ように", "のため", "ことに", "ために"],
        "correct_index": 1,
        "translation_vi": "Vì mưa lớn do bão gây ra, chúng tôi xin phép hủy bỏ trận đấu hôm nay.",
        "explanation_vi": "Danh từ nguyên nhân 大雨 nối với ため trong thông báo chính thức phải có の -> 大雨のため.",
        "option_diagnostics": [
            "[SAI - Không gắn ように trực tiếp sau danh từ nguyên nhân]: ように không chỉ nguyên nhân sự cố.",
            "[ĐÚNG - N + のため (Nguyên nhân trang trọng)]: Thông báo hủy sự kiện dùng 大雨のため.",
            "[SAI - Sai mẫu]: ことに chỉ cảm xúc bất ngờ (驚くことに), không dùng cho danh từ nguyên nhân 大雨.",
            "[SAI - Thiếu trợ từ の]: Danh từ nối vào ため(に) bắt buộc phải có の (大雨のため, không viết *大雨ために).",
        ],
    },
    # --- GP-N4-13 (contrast + application) ---
    {
        "drill_key": "DR-GP-N4-13-C",
        "grammar_code": "GP-N4-13",
        "drill_type": "contrast",
        "prompt_jp": "健康のために、毎日寝る前に少しストレッチをする（　　）。",
        "options": ["ことになっている", "ことにしている", "ことになる", "ように見える"],
        "correct_index": 1,
        "translation_vi": "Vì sức khỏe, tôi tự tạo thói quen tập giãn cơ một chút mỗi tối trước khi ngủ.",
        "explanation_vi": "Thói quen lành mạnh do BẢN THÂN tự đặt ra và duy trì đều đặn mỗi ngày dùng Vる + ことにしている.",
        "option_diagnostics": [
            "[SAI - Nhầm quy định khách quan]: ことになっている chỉ luật lệ tập thể/nhà trường quy định từ bên ngoài, không phải thói quen tự giác vì sức khỏe cá nhân.",
            "[ĐÚNG - Thói quen tự quy định ことにしている]: Vる + ことにしている.",
            "[SAI - Sai thì và bản chất]: ことになる chỉ kết quả khách quan xảy ra một lần, không diễn tả thói quen lặp lại hằng ngày.",
            "[SAI - Sai nghĩa]: ように見える nghĩa là 'trông có vẻ như', không hợp câu nói về thói quen của mình.",
        ],
    },
    {
        "drill_key": "DR-GP-N4-13-A",
        "grammar_code": "GP-N4-13",
        "drill_type": "application",
        "prompt_jp": "使い捨てにするのはもったいないので、空き瓶を花瓶として（　　）。",
        "options": ["使うことになった", "使うことにした", "使われたことにした", "使うことはない"],
        "correct_index": 1,
        "translation_vi": "Vứt đi một lần thì phí quá nên tôi đã quyết định dùng cái chai rỗng làm bình hoa.",
        "explanation_vi": "Hành động xuất phát từ quyết định chủ quan của bản thân người nói ('thấy phí nên tự quyết định tận dụng') dùng 使うことにした.",
        "option_diagnostics": [
            "[SAI - Nhầm quyết định khách quan]: Không có tổ chức hay tình thế bên ngoài nào ép buộc; đây là ý tưởng cá nhân chủ động.",
            "[ĐÚNG - Quyết định chủ quan ことにした]: Vる + ことにした.",
            "[SAI - Sai thể bị động]: Tự mình quyết định dùng chai chứ không chia bị động 使われた.",
            "[SAI - Ngược nghĩa]: 使うことはない nghĩa là 'không cần thiết phải dùng'.",
        ],
    },
    # --- GP-N4-14 (formation + application) ---
    {
        "drill_key": "DR-GP-N4-14-F",
        "grammar_code": "GP-N4-14",
        "drill_type": "formation",
        "prompt_jp": "この図書館では、飲食を（　　）ことになっている。",
        "options": ["しない", "してはいけない", "した", "しなくて"],
        "correct_index": 0,
        "translation_vi": "Ở thư viện này có quy định là không được ăn uống.",
        "explanation_vi": "Trước ことになっている chỉ quy định chung luôn dùng động từ thể từ điển Vる hoặc thể phủ định ngắn Vない -> しないことになっている.",
        "option_diagnostics": [
            "[ĐÚNG - Vない + ことになっている]: Quy định cấm làm gì chia phủ định ngắn Vない trước ことになっている.",
            "[SAI - Trùng lặp cấu trúc cấm]: てはいけない không đứng trước ことになっている.",
            "[SAI - Sai thì quá khứ]: Quy định hiện hành không chia quá khứ Vた trước ことになっている.",
            "[SAI - Sai dạng nối]: Thể て (しなくて) không đứng trực tiếp trước ことになっている.",
        ],
    },
    {
        "drill_key": "DR-GP-N4-14-A",
        "grammar_code": "GP-N4-14",
        "drill_type": "application",
        "prompt_jp": "来月から大阪支社へ（　　）ことになったので、引っ越しの準備をしている。",
        "options": ["転勤する", "転勤しよう", "転勤した", "転勤して"],
        "correct_index": 0,
        "translation_vi": "Tháng sau tôi được quyết định chuyển công tác tới chi nhánh Osaka nên đang chuẩn bị chuyển nhà.",
        "explanation_vi": "Quyết định điều động nhân sự từ công ty dùng Vる + ことになった (nguyên thể 転勤する).",
        "option_diagnostics": [
            "[ĐÚNG - Vる + ことになった]: Lệnh điều chuyển khách quan dùng nguyên thể Vる + ことになった.",
            "[SAI - Sai hình thái thể ý chí]: Thể ý chí 転勤しよう không nối trước ことになった.",
            "[SAI - Sai thì động từ]: Việc chuyển công tác diễn ra vào tháng sau (tương lai), trước こと không chia quá khứ 転勤した.",
            "[SAI - Sai dạng nối]: Thể て không đứng trước ことになった.",
        ],
    },
    # --- GP-N4-15 (contrast + application) ---
    {
        "drill_key": "DR-GP-N4-15-C",
        "grammar_code": "GP-N4-15",
        "drill_type": "contrast",
        "prompt_jp": "魚を捕る技術が発達したため、マグロは以前より大量に（　　）ようになった。",
        "options": ["捕る", "捕られる", "捕ろうとする", "捕るようにする"],
        "correct_index": 1,
        "translation_vi": "Vì kỹ thuật đánh bắt phát triển nên cá ngừ đã trở nên bị đánh bắt với số lượng lớn hơn trước.",
        "explanation_vi": "Chủ ngữ là マグロは kết hợp với ようになった để chỉ sự biến chuyển thực trạng bị khai thác -> phải dùng Thể bị động 捕られる.",
        "option_diagnostics": [
            "[SAI - Nhầm chủ động với chủ ngữ マグロ]: Cá ngừ không tự đi bắt mà bị con người đánh bắt.",
            "[ĐÚNG - Bị động + ようになった]: Diễn tả bước ngoặt biến đổi trạng thái của cá ngừ.",
            "[SAI - Sai ngữ nghĩa ý định]: 捕ろうとする là 'định bắt', không nối được với ようになった ở đây.",
            "[SAI - Trùng cấu trúc]: Không lặp ようにする trước ようになった.",
        ],
    },
    {
        "drill_key": "DR-GP-N4-15-A",
        "grammar_code": "GP-N4-15",
        "drill_type": "application",
        "prompt_jp": "忘れ物をしないように、前日の夜に荷物を確認する（　　）。",
        "options": ["ようになった", "ようにしている", "ことになった", "に違いない"],
        "correct_index": 1,
        "translation_vi": "Để không quên đồ, tôi luôn cố gắng kiểm tra hành lý vào tối hôm trước.",
        "explanation_vi": "Nỗ lực chủ động rèn luyện/duy trì thói quen tốt mỗi lần chuẩn bị đồ dùng Vる + ようにしている.",
        "option_diagnostics": [
            "[SAI - Nhầm biến chuyển năng lực/tự nhiên]: Nỗ lực có ý thức tự giác hằng ngày dùng ようにしている, không phải tự nhiên biến đổi ようになった.",
            "[ĐÚNG - Chủ động nỗ lực duy trì ようにしている]: Vる + ようにしている.",
            "[SAI - Sai nghĩa quy định bên ngoài]: Việc tự kiểm tra đồ buổi tối không phải quy định công ty ép buộc.",
            "[SAI - Sai cấu trúc phỏng đoán]: に違いない là phỏng đoán, không diễn tả thói quen thực hiện.",
        ],
    },
    # --- GP-N4-16 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N4-16-F",
        "grammar_code": "GP-N4-16",
        "drill_type": "formation",
        "prompt_jp": "春に（　　）、公園の桜が一斉に咲き始める。",
        "options": ["なると", "なるなら", "なったと", "なればに"],
        "correct_index": 0,
        "translation_vi": "Hễ sang xuân là hoa anh đào trong công viên đồng loạt bắt đầu nở.",
        "explanation_vi": "Quy luật tự nhiên tất yếu lặp lại hằng năm dùng [Vる + と] -> 春になると.",
        "option_diagnostics": [
            "[ĐÚNG - Điều kiện tất yếu tự nhiên と]: 春になると + quy luật tự nhiên.",
            "[SAI - Sai ngữ dụng なら]: なら dùng tiếp nhận ý kiến/dự định từ đối phương trong hội thoại, không dùng mô tả quy luật tự nhiên sang xuân.",
            "[SAI - Sai thì trước と]: Điều kiện quy luật chung luôn dùng nguyên thể Vる (なると), không chia quá khứ Vた.",
            "[SAI - Sai hình thái thừa に]: Không bao giờ thêm に vào sau thể ば (*なればに).",
        ],
    },
    {
        "drill_key": "DR-GP-N4-16-C",
        "grammar_code": "GP-N4-16",
        "drill_type": "contrast",
        "prompt_jp": "明日の会議に（　　）場合は、必ず今日中に連絡してください。",
        "options": ["出席すると", "出席できない", "出席すれば", "出席したら"],
        "correct_index": 1,
        "translation_vi": "Trường hợp không thể tham dự cuộc họp ngày mai, nhất định hãy liên hệ trong hôm nay.",
        "explanation_vi": "Danh từ 場合 (trường hợp) đã tự mang nghĩa điều kiện ('nếu trường hợp...') nên đứng trước 場合 chỉ dùng mệnh đề bổ nghĩa 普通形 (không gắn と・ば・たら trước 場合!).",
        "option_diagnostics": [
            "[SAI - Chồng chéo 2 điều kiện]: Không đặt と ngay trước danh từ 場合 (*すると場合).",
            "[ĐÚNG - Định ngữ 普通形 + 場合]: 出席できない + 場合は = trường hợp không thể tham dự.",
            "[SAI - Chồng chéo điều kiện ば]: Thể ば không đứng trước danh từ 場合 (*すれば場合).",
            "[SAI - Chồng chéo điều kiện たら]: Thể たら không bổ nghĩa danh từ 場合 (*したら場合).",
        ],
    },
    # --- GP-N4-17 (contrast + application) ---
    {
        "drill_key": "DR-GP-N4-17-C",
        "grammar_code": "GP-N4-17",
        "drill_type": "contrast",
        "prompt_jp": "以前、電車でお年寄りに席を（　　）ことがあるが、断られてしまった。",
        "options": ["譲ってみた", "譲ろうとした", "譲るつもりだった", "譲られる"],
        "correct_index": 1,
        "translation_vi": "Trước đây tôi từng định nhường ghế cho người lớn tuổi trên tàu, nhưng đã bị từ chối.",
        "explanation_vi": "Ý định hành động chuẩn bị làm ngay lúc đó nhưng bị gián đoạn/từ chối chưa làm thành công -> Thể ý chí + とした (譲ろうとした).",
        "option_diagnostics": [
            "[SAI - Sai kết quả đã làm]: 譲ってみた nghĩa là đã nhường thử thành công rồi mới xét kết quả, nhưng câu sau bảo bị từ chối ngay khi ngỏ ý.",
            "[ĐÚNG - Định làm ngay lúc đó ようとした]: Thể ý chí 譲ろう + とした (với ことがある).",
            "[SAI - Sai ngữ cảnh ngộ nhận]: つもりだった là 'cứ đinh ninh mình đã nhường xong rồi', sai tình huống bị từ chối.",
            "[SAI - Sai thể bị động]: Người nói chủ động nhường ghế chứ không phải bị nhường.",
        ],
    },
    {
        "drill_key": "DR-GP-N4-17-A",
        "grammar_code": "GP-N4-17",
        "drill_type": "application",
        "prompt_jp": "その国の言葉ができないことは大きなストレスに（　　）に違いない。",
        "options": ["なろうとする", "なる", "なってばかり", "なるにすぎない"],
        "correct_index": 1,
        "translation_vi": "Việc không nói được tiếng nước đó hẳn là sẽ trở thành áp lực lớn.",
        "explanation_vi": "Trước に違いない dùng nguyên thể なる; không dùng なろうとする ('cố định trở thành áp lực') vì stress là trạng thái không mang ý chí chủ động.",
        "option_diagnostics": [
            "[SAI - Gắn thể ý chí cho trạng thái vô ý chí]: Không ai 'cố ý định trở thành áp lực lớn' cả; なろうとする sai chủ ý.",
            "[ĐÚNG - Vる + に違いない]: ストレスになる + に違いない.",
            "[SAI - Lặp ý chê trách]: なってばかり không nối trực tiếp trước に違いない và sai mạch nhấn mạnh.",
            "[SAI - Ngược sắc thái]: にすぎない hạ thấp mức độ ('chẳng qua chỉ là'), mâu thuẫn với 大きなストレス.",
        ],
    },
    # --- GP-N4-18 (formation + application) ---
    {
        "drill_key": "DR-GP-N4-18-F",
        "grammar_code": "GP-N4-18",
        "drill_type": "formation",
        "prompt_jp": "パソコンの使い方がわからないときは、電話で操作方法を（　　）。",
        "options": ["教えてあげられる", "教えてもらえる", "教えてくれる", "教えられる"],
        "correct_index": 1,
        "translation_vi": "Khi không biết cách dùng máy tính, bạn có thể được chỉ dẫn cách thao tác qua điện thoại.",
        "explanation_vi": "Người dùng (chủ ngữ ẩn) có thể NHẬN được sự hướng dẫn từ tổng đài -> dùng thể khả năng của もらう là 教えてもらえる.",
        "option_diagnostics": [
            "[SAI - Ngược chiều cho nhận]: あげられる là 'bạn có thể dạy cho tổng đài', sai hoàn toàn vai trò.",
            "[ĐÚNG - Khả năng nhận giúp đỡ てもらえる]: 教えてもらえる = có thể được chỉ bảo giúp.",
            "[SAI - Thiếu ý khả năng 'có thể' trong hướng dẫn]: Với câu mô tả tiện ích dịch vụ ('có thể nhận hỗ trợ'), 教えてもらえる chuẩn xác hơn 教えてくれる.",
            "[SAI - Bị động thuần không có sắc thái lợi ích]: 教えられる không thể hiện quyền lợi được hỗ trợ như てもらえる.",
        ],
    },
    {
        "drill_key": "DR-GP-N4-18-A",
        "grammar_code": "GP-N4-18",
        "drill_type": "application",
        "prompt_jp": "母はいつも家族に、温かい炊きたてのごはんを（　　）と言っている。",
        "options": ["食べてあげたい", "食べてもらいたい", "食べてほしいの", "食べてくれたい"],
        "correct_index": 1,
        "translation_vi": "Mẹ tôi lúc nào cũng nói muốn mọi người trong gia đình ăn cơm ấm vừa mới nấu xong.",
        "explanation_vi": "Mẹ muốn gia đình (家族に) đón nhận thưởng thức cơm do mẹ nấu -> dùng 食べてもらいたい (trợ từ に + てもらいたい).",
        "option_diagnostics": [
            "[SAI - Sắc thái ban ơn & sai chiều]: 食べてあげたい nghĩa là 'tôi muốn ăn giùm gia đình', vô lý.",
            "[ĐÚNG - Mong người thân đón nhận てもらいたい]: 家族に + 食べてもらいたい.",
            "[SAI - Đuôi の không đứng trước と]: Trích dẫn と言っている không dùng *食べてほしいのと言っている.",
            "[SAI - Lỗi ngữ pháp kết hợp くれ + たい]: Động từ くれる KHÔNG bao giờ chia sang たい (*くれたい là sai ngữ pháp tuyệt đối!).",
        ],
    },
    # --- GP-N4-19 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N4-19-F",
        "grammar_code": "GP-N4-19",
        "drill_type": "formation",
        "prompt_jp": "さっき電話で確認したばかりだから、あの店が今日（　　）。",
        "options": ["休みだはずがない", "休みなはずがない", "休みのはずがない", "休むはずがない"],
        "correct_index": 2,
        "translation_vi": "Vì lúc nãy tôi vừa gọi điện xác nhận rồi nên cửa hàng đó hôm nay chắc chắn không thể nghỉ được.",
        "explanation_vi": "休み là danh từ, nên khi nối với はずがない BẮT BUỘC phải thêm の -> 休みのはずがない.",
        "option_diagnostics": [
            "[SAI - Dùng だ trước はず]: Sau danh từ phải bỏ だ và dùng の, không viết *休みだはずがない.",
            "[SAI - Nhầm danh từ với tính từ な]: 休み là danh từ (không phải tính từ な), nên dùng の chứ không dùng な.",
            "[ĐÚNG - N + の + はずがない]: Danh từ 休み + の + はずがない.",
            "[SAI - Chia sai từ loại]: 休み ở đây là danh từ chỉ ngày nghỉ (lưu ý động từ 休む cũng đúng nghĩa 'cửa hàng nghỉ', nhưng không đổi 休み thành *休むはず khi câu cho khung danh từ 休み; ở đề kiểm tra danh từ phải là 休みの).",
        ],
    },
    {
        "drill_key": "DR-GP-N4-19-C",
        "grammar_code": "GP-N4-19",
        "drill_type": "contrast",
        "prompt_jp": "あんなに真面目で優しい人が、人の悪口を言う（　　）。",
        "options": ["わけにはいかない", "わけではない", "はずがない", "ことはない"],
        "correct_index": 2,
        "translation_vi": "Một người nghiêm túc và hiền lành như thế làm sao có chuyện đi nói xấu người khác được.",
        "explanation_vi": "Bác bỏ 100% khả năng xảy ra dựa trên tính cách hiển nhiên đã biết dùng ～はずがない (hoặc ～わけがない).",
        "option_diagnostics": [
            "[SAI - Nhầm nghĩa đạo lý cấm cản]: わけにはいかない nghĩa là 'bản thân anh ta muốn nói xấu nhưng bị quy tắc ngăn cấm không nói được', lệch hoàn toàn ý tin tưởng nhân cách.",
            "[SAI - Phủ định một phần không hợp]: わけではない nghĩa là 'không hẳn lúc nào anh ta cũng nói xấu', vẫn thừa nhận có lúc anh ta nói xấu.",
            "[ĐÚNG - Bác bỏ hoàn toàn theo logic はずがない]: Tin chắc chắn không có chuyện đó.",
            "[SAI - Nhầm nghĩa 'không cần thiết']: ことはない nghĩa là 'anh ta không cần thiết phải nói xấu', sai hoàn toàn logic.",
        ],
    },
    # --- GP-N4-20 (contrast + application) ---
    {
        "drill_key": "DR-GP-N4-20-C",
        "grammar_code": "GP-N4-20",
        "drill_type": "contrast",
        "prompt_jp": "田中君の話では、小川さんは先週から入院（　　）。",
        "options": ["しそうだ", "したらしい", "するようだ", "してみそうだ"],
        "correct_index": 1,
        "translation_vi": "Theo lời kể của cậu Tanaka thì nghe nói anh/chị Ogawa hình như đã nhập viện từ tuần trước rồi.",
        "explanation_vi": "Dựa vào nguồn tin nghe lại từ người thứ ba (田中君の話では) để suy đoán việc đã xảy ra -> Vた + らしい.",
        "option_diagnostics": [
            "[SAI - Nhầm Vます+そうだ (nhìn trực quan)]: しそうだ nghĩa là nhìn trực tiếp thấy sắp sửa nhập viện, sai thì với 先週から và nguồn nghe kể.",
            "[ĐÚNG - Truyền đạt nguồn tin nghe kể らしい]: 先週から入院した + らしい.",
            "[SAI - Sai thì và chủ quan]: するようだ là quan sát hiện tại thấy 'có vẻ sắp nhập viện', không khớp với sự việc đã xảy ra từ tuần trước.",
            "[SAI - Sai hình thái ghép]: Không ghép *してみそうだ cho bối cảnh nghe kể tin tức.",
        ],
    },
    {
        "drill_key": "DR-GP-N4-20-A",
        "grammar_code": "GP-N4-20",
        "drill_type": "application",
        "prompt_jp": "空が暗くなってきたし、冷たい風も吹いている。もうすぐ雨が（　　）。",
        "options": ["降るそうだ", "降りそうだ", "降ったらしい", "降るはずがない"],
        "correct_index": 1,
        "translation_vi": "Bầu trời tối sầm lại rồi, gió lạnh cũng đang thổi. Trời trông có vẻ sắp mưa tới nơi rồi.",
        "explanation_vi": "Quan sát dấu hiệu trực quan trước mắt (trời tối sầm, gió lạnh) để đoán việc sắp xảy ra ngay lập tức dùng Vます + そうだ -> 降りそうだ.",
        "option_diagnostics": [
            "[SAI - Nhầm sang nghĩa 'nghe nói']: 降るそうだ (nguyên thể + そうだ) nghĩa là 'nghe đài/báo nói sẽ mưa', không phải tự mình nhìn mây gió rồi đoán.",
            "[ĐÚNG - Phỏng đoán trực quan Vます+そうだ]: 降る -> 降り + そうだ.",
            "[SAI - Sai thì quá khứ]: Sự việc sắp xảy ra (もうすぐ) không dùng thì quá khứ 降ったらしい.",
            "[SAI - Ngược hoàn toàn logic]: Mây đen gió lạnh mà đoán 'không thể mưa' là mâu thuẫn.",
        ],
    },
    # --- GP-N4-21 (formation + application) ---
    {
        "drill_key": "DR-GP-N4-21-F",
        "grammar_code": "GP-N4-21",
        "drill_type": "formation",
        "prompt_jp": "犯人は、銀行から盗んだ金を取りに（　　）ところを警察に逮捕された。",
        "options": ["現れる", "現れた", "現れよう", "現れて"],
        "correct_index": 1,
        "translation_vi": "Tên tội phạm đã bị cảnh sát bắt giữ ngay lúc vừa xuất hiện để lấy số tiền trộm từ ngân hàng.",
        "explanation_vi": "Bị bắt gặp ngay khoảnh khắc vừa hoàn thành động tác xuất hiện dùng [Vた + ところを] -> 現れたところを.",
        "option_diagnostics": [
            "[SAI - Chưa xảy ra]: 現れるところを nghĩa là 'ngay trước khi định xuất hiện', nhưng cảnh sát chỉ bắt được khi đối tượng đã xuất hiện tại điểm lấy tiền.",
            "[ĐÚNG - Vた + ところを]: Khoảnh khắc vừa lộ diện xong thì bị tóm -> 現れたところを.",
            "[SAI - Sai hình thái]: Thể ý chí 現れよう không đứng trực tiếp trước ところを.",
            "[SAI - Sai dạng nối]: Thể て không nối trực tiếp với ところを.",
        ],
    },
    {
        "drill_key": "DR-GP-N4-21-A",
        "grammar_code": "GP-N4-21",
        "drill_type": "application",
        "prompt_jp": "「すみません、山田さんはいますか。」「あ、今ちょうど（　　）です。もう駅に着いたかもしれません。」",
        "options": ["帰るところ", "帰っているところ", "帰ったところ", "帰るばかり"],
        "correct_index": 2,
        "translation_vi": "'Xin lỗi, anh Yamada có ở đây không?' — 'À, anh ấy vừa mới về tức thì. Chắc giờ có lẽ đã tới ga rồi.'",
        "explanation_vi": "Sự việc vừa mới kết thúc ngay trước lúc hỏi dùng [Vた + ところだ] -> 帰ったところです.",
        "option_diagnostics": [
            "[SAI - Ngược thời điểm]: 帰るところ nghĩa là 'đang chuẩn bị về (vẫn còn ở đây)', mâu thuẫn với câu sau 'có lẽ đã tới ga rồi'.",
            "[SAI - Sai thời điểm]: 帰っているところ nghĩa là 'đang trên đường đi về hoặc đang thu dọn để về', chưa khớp 'vừa rời đi xong tức thì'.",
            "[ĐÚNG - Vừa mới xong Vた + ところ]: 帰ったところです.",
            "[SAI - Thiếu thì quá khứ của ばかり]: *帰るばかりです nghĩa là 'chỉ còn chờ mỗi việc về', không dùng trả lời người đã đi.",
        ],
    },
    # --- GP-N4-22 (contrast + application) ---
    {
        "drill_key": "DR-GP-N4-22-C",
        "grammar_code": "GP-N4-22",
        "drill_type": "contrast",
        "prompt_jp": "今朝、駅で会った上司に「遅刻しないように」と（　　）のに、また寝坊してしまった。",
        "options": ["言われてばかりいた", "言われたばかりな", "言われるところだった", "言ったばかりだ"],
        "correct_index": 1,
        "translation_vi": "Sáng nay vừa mới bị sếp nhắc 'đừng đi muộn' thế mà tôi lại ngủ quên nữa rồi.",
        "explanation_vi": "Vừa mới bị nhắc sáng nay (hiện giờ vẫn thấy còn mới nguyên) dùng [V(bị động)た + ばかりだ] bổ nghĩa cho のに -> 言われたばかりなのに.",
        "option_diagnostics": [
            "[SAI - Nhầm với Vてばかりいる]: 言われてばかりいた nghĩa là 'suốt ngày toàn bị sếp mắng', không khớp mốc sáng nay.",
            "[ĐÚNG - Vた + ばかり + なのに]: Bị động quá khứ 言われた + ばかり (chia tính từ な trước のに -> ばかりなのに).",
            "[SAI - Sai nghĩa 'suýt nữa']: ところだった nghĩa là 'suýt nữa thì bị nhắc' (thực tế chưa bị nhắc).",
            "[SAI - Ngược chủ thể và thiếu な]: 言った là mình đi nhắc sếp, và trước のに phải có な chứ không giữ だ.",
        ],
    },
    {
        "drill_key": "DR-GP-N4-22-A",
        "grammar_code": "GP-N4-22",
        "drill_type": "application",
        "prompt_jp": "先月日本に（　　）なので、まだ日本の生活に慣れていません。",
        "options": ["来たところ", "来たばかり", "来てばかり", "来るばかり"],
        "correct_index": 1,
        "translation_vi": "Vì tôi mới đến Nhật tháng trước nên vẫn chưa quen với cuộc sống ở Nhật.",
        "explanation_vi": "Mốc thời gian đã qua từ tháng trước (先月 - không phải vài giây trước) theo cảm nhận vẫn còn mới dùng Vた + ばかり (không dùng ところ!).",
        "option_diagnostics": [
            "[SAI - Dùng ところ cho mốc tháng trước]: Vたところ chỉ dùng cho khoảng thời gian cực ngắn vừa dứt tức thì vài phút trước, không dùng với 先月.",
            "[ĐÚNG - Cảm nhận thời gian mới qua Vた+ばかり]: 先月来たばかりなので.",
            "[SAI - Nhầm sang nghĩa 'suốt ngày chỉ toàn']: 来てばかり là 'suốt ngày chỉ toàn tới', vô lý với 先月.",
            "[SAI - Sai hình thái]: 来るばかり không mang nghĩa vừa mới đến.",
        ],
    },
    # --- GP-N4-23 (formation + application) ---
    {
        "drill_key": "DR-GP-N4-23-F",
        "grammar_code": "GP-N4-23",
        "drill_type": "formation",
        "prompt_jp": "古本をお持ちになり、5月31日までに東京ボランティアセンターへ（　　）。",
        "options": ["お越しして", "お越しください", "参ってください", "うかがってください"],
        "correct_index": 1,
        "translation_vi": "Xin quý vị hãy mang theo sách cũ và đến Trung tâm tình nguyện Tokyo trước ngày 31/5.",
        "explanation_vi": "Yêu cầu lịch sự khách hàng/người dân ĐẾN trung tâm phải dùng Tôn kính ngữ お越しください (từ 越す = 来てください).",
        "option_diagnostics": [
            "[SAI - Lỗi trộn Tôn kính và Khiêm nhường]: お越し thuộc tôn kính ngữ dành cho khách; không ghép với する thành *お越しして (lỗi kính ngữ kinh điển).",
            "[ĐÚNG - Tôn kính ngữ mời khách đến]: お越しください = hãy đến (tôn kính của 来てください).",
            "[SAI - Dùng Khiêm nhường ngữ cho đối phương]: 参る là khiêm nhường ngữ của 'tôi đến', cấm dùng yêu cầu khách hàng.",
            "[SAI - Dùng Khiêm nhường ngữ cho đối phương]: うかがう là khiêm nhường ngữ của 'tôi đến thăm/hỏi', không dùng yêu cầu người đọc.",
        ],
    },
    {
        "drill_key": "DR-GP-N4-23-A",
        "grammar_code": "GP-N4-23",
        "drill_type": "application",
        "prompt_jp": "故障した場合は、まずホームページで新しい情報を（　　）。",
        "options": ["ご確認いたしましょう", "ご確認ください", "ご拝見ください", "お伺いください"],
        "correct_index": 1,
        "translation_vi": "Trường hợp bị hỏng hóc, trước tiên xin quý khách hãy kiểm tra thông tin mới trên trang chủ.",
        "explanation_vi": "Danh từ Hán-Nhật 確認 (xác nhận) chuyển sang dạng đề nghị tôn kính lịch sự cho khách hàng dùng ご + N + ください -> ご確認ください.",
        "option_diagnostics": [
            "[SAI - Sai chủ thể và ý nghĩa]: いたしましょう là khiêm nhường 'để chúng tôi xác nhận giúp', sai vì tờ hướng dẫn bảo KHÁCH tự kiểm tra trên web.",
            "[ĐÚNG - Tôn kính ngữ chỉ dẫn ごNください]: ご確認ください = xin hãy kiểm tra.",
            "[SAI - Dùng khiêm nhường 拝見 cho khách]: 拝見 là khiêm nhường của 'tôi xem', không bao giờ viết *ご拝見ください cho khách.",
            "[SAI - Dùng khiêm nhường 伺う cho khách]: 伺う là 'tôi hỏi/tôi đến', không dùng cho khách.",
        ],
    },
    # --- GP-N4-24 (contrast + application) ---
    {
        "drill_key": "DR-GP-N4-24-C",
        "grammar_code": "GP-N4-24",
        "drill_type": "contrast",
        "prompt_jp": "消費に合った量のマグロを捕るようにすることも重要（　　）。",
        "options": ["ではないだろうか", "ではないはずだ", "ことではない", "というわけがない"],
        "correct_index": 0,
        "translation_vi": "Việc cố gắng đánh bắt lượng cá ngừ phù hợp với nhu cầu tiêu thụ chẳng phải cũng rất quan trọng sao?",
        "explanation_vi": "Câu hỏi tu từ khẳng định nhẹ chủ trương của tác giả ở đoạn kết bài nghị luận dùng [Aな + ではないだろうか].",
        "option_diagnostics": [
            "[ĐÚNG - Câu hỏi tu từ khẳng định nhẹ]: 重要ではないだろうか = chẳng phải rất quan trọng sao (= Rất quan trọng!).",
            "[SAI - Sai cấu trúc và nghĩa phủ định]: *ではないはずだ nghĩa là 'chắc chắn không quan trọng', trái ngược lập luận bài đọc.",
            "[SAI - Sai hình thái]: Tính từ 重要 không gắn trực tiếp *重要ことではない.",
            "[SAI - Phủ định 100% trái ý]: わけがない nghĩa là 'tuyệt đối không thể nào quan trọng', sai hoàn toàn chủ trương tác giả.",
        ],
    },
    {
        "drill_key": "DR-GP-N4-24-A",
        "grammar_code": "GP-N4-24",
        "drill_type": "application",
        "prompt_jp": "「ねえ、来月の日本語のテスト、何日から（　　）？」「15日からだよ。」",
        "options": ["だっけ", "だろう", "はずだ", "ではないだろうか"],
        "correct_index": 0,
        "translation_vi": "'Này, bài kiểm tra tiếng Nhật tháng sau bắt đầu từ ngày mấy ấy nhỉ?' — 'Từ ngày 15 đấy.'",
        "explanation_vi": "Hỏi xác nhận lại thông tin mình từng nghe nhưng hơi quên trong hội thoại thân mật dùng ～だっけ.",
        "option_diagnostics": [
            "[ĐÚNG - Xác nhận thông tin quên nhẹ ～っけ]: N + だっけ? trong hội thoại thân mật.",
            "[SAI - Phỏng đoán chứ không hỏi bạn]: だろう là tự suy đoán chứ không khớp ngữ điệu hỏi bạn nhắc lại trí nhớ.",
            "[SAI - Không phải câu hỏi]: はずだ là khẳng định chắc chắn không dùng hỏi đáp trực tiếp.",
            "[SAI - Văn phong nghị luận sai bối cảnh]: ではないだろうか là câu hỏi tu từ văn viết, không dùng hỏi lịch thi với bạn bè.",
        ],
    },

    # --- GP-N3-001 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-001-F",
        "grammar_code": "GP-N3-001",
        "drill_type": "formation",
        "prompt_jp": "料理が（　　）うちに、早く食べましょう。",
        "options": ["冷めない", "冷めて", "冷めた", "冷めなかった"],
        "correct_index": 0,
        "translation_vi": "Trong lúc món ăn còn chưa bị nguội đi, hãy ăn nhanh lên nào.",
        "explanation_vi": "Tranh thủ làm hành động V2 trước khi trạng thái xấu (nguội đi) xảy ra dùng [Vない + うちに] -> 冷めないうちに.",
        "option_diagnostics": [
            "[ĐÚNG - Vない + うちに]: Tranh thủ lúc chưa nguội -> 冷めないうちに.",
            "[SAI - Thể て không đứng trước うちに]: Không có mẫu *冷めてうちに.",
            "[SAI - Ngược nghĩa quá khứ]: 冷めたうちに không tồn tại cấu trúc này và trái nghĩa 'đã nguội mất rồi'.",
            "[SAI - Sai thì quá khứ]: Trạng thái hiện tại vẫn còn nóng nên không chia quá khứ 冷めなかった.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-001-C",
        "grammar_code": "GP-N3-001",
        "drill_type": "contrast",
        "prompt_jp": "図書館の本を読んでいる（　　）、外が暗くなっていた。",
        "options": ["ために", "うちに", "かわりに", "おかげで"],
        "correct_index": 1,
        "translation_vi": "Trong lúc đang mải mê đọc sách ở thư viện, bên ngoài trời đã tối sầm lại tự lúc nào.",
        "explanation_vi": "Trong suốt lúc hành động Vている diễn ra, sự biến đổi tự nhiên bên ngoài (trời tối lúc nào không hay) xuất hiện -> Vている + うちに.",
        "option_diagnostics": [
            "[SAI - Sai quan hệ nhân quả]: Việc mình đọc sách không phải nguyên nhân làm cho mặt trời lặn.",
            "[ĐÚNG - Vている + うちに + biến đổi tự nhiên]: Đang làm A thì B tự nhiên diễn ra.",
            "[SAI - Sai nghĩa thay thế]: Không mang nghĩa 'thay cho việc đọc sách thì trời tối'.",
            "[SAI - Sai nghĩa biết ơn]: Không phải nhờ đọc sách mà trời tối.",
        ],
    },
    # --- GP-N3-002 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-002-C",
        "grammar_code": "GP-N3-002",
        "drill_type": "contrast",
        "prompt_jp": "私が留守の（　　）、部屋に泥棒が入ってしまった。",
        "options": ["間ずっと", "間に", "うちに", "ついでに"],
        "correct_index": 1,
        "translation_vi": "Trong lúc tôi vắng nhà, kẻ trộm đã lẻn vào phòng mất rồi.",
        "explanation_vi": "Hành động trộm lẻn vào là sự kiện xảy ra 1 lần bên trong khoảng thời gian vắng nhà -> bắt buộc dùng có trợ từ に (間に).",
        "option_diagnostics": [
            "[SAI - Lỗi kéo dài suốt với hành động dứt điểm]: 間ずっと nghĩa là tên trộm cứ đi ra đi vào suốt cả khoảng thời gian vắng nhà, sai logic.",
            "[ĐÚNG - Khoảng thời gian + 間に + sự kiện 1 lần]: 留守の間に + 泥棒が入った.",
            "[SAI - Sai sắc thái tranh thủ]: うちに mang sắc thái tranh thủ hoặc tự nhiên biến đổi khi chưa hết trạng thái, không tự nhiên bằng 間に cho sự cố lúc vắng nhà.",
            "[SAI - Sai chủ thể và ý định]: ついでに nghĩa là 'nhân tiện chủ động làm thêm việc phụ'.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-002-A",
        "grammar_code": "GP-N3-002",
        "drill_type": "application",
        "prompt_jp": "彼は2時間の会議の（　　）ずっとスマホを見ていた。",
        "options": ["間に", "間", "うちに", "とおりに"],
        "correct_index": 1,
        "translation_vi": "Anh ta nhìn điện thoại suốt cả 2 tiếng đồng hồ cuộc họp.",
        "explanation_vi": "Có phó từ ずっと (suốt từ đầu đến cuối) và hành động nhìn kéo dài song song toàn bộ 2 tiếng -> dùng 間 (không có に).",
        "option_diagnostics": [
            "[SAI - Không dùng 間に với phó từ ずっと]: 間に chỉ sự kiện diễn ra trong 1 khoảnh khắc thuộc khoảng thời gian, trái với hành động kéo dài ずっと.",
            "[ĐÚNG - N + の + 間 + ずっと]: Kéo dài liên tục suốt từ đầu đến cuối cuộc họp.",
            "[SAI - Sai sắc thái]: うちに không đi với ずっと để chỉ hành động liên tục cố ý suốt 2 tiếng.",
            "[SAI - Sai nghĩa]: とおりに nghĩa là 'theo đúng như cuộc họp', vô nghĩa.",
        ],
    },
    # --- GP-N3-003 (formation + application) ---
    {
        "drill_key": "DR-GP-N3-003-F",
        "grammar_code": "GP-N3-003",
        "drill_type": "formation",
        "prompt_jp": "実際に（　　）でないと、この仕事の難しさはわからない。",
        "options": ["やって", "やってから", "やったら", "やるから"],
        "correct_index": 1,
        "translation_vi": "Nếu không trực tiếp làm thử trước rồi thì không thể hiểu được độ khó của công việc này.",
        "explanation_vi": "Điều kiện tiên quyết bắt buộc phải làm xong V1 trước mới thực hiện/hiểu được V2 dùng [Vて + からでないと].",
        "option_diagnostics": [
            "[SAI - Thiếu から]: Không có cấu trúc *やってでないと (trừ danh từ mới đi thẳng với でないと).",
            "[ĐÚNG - Công thức Vて + からでないと]: やって + からでないと + わからない.",
            "[SAI - Sai hình thái kết hợp でないと]: Không ghép *やったらでないと.",
            "[SAI - Sai hoàn toàn cấu trúc và nghĩa]: やるからでないと không phải cấu trúc điều kiện tiên quyết.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-003-A",
        "grammar_code": "GP-N3-003",
        "drill_type": "application",
        "prompt_jp": "家族とよく相談してからでないと、転職するかどうか（　　）。",
        "options": ["決めるつもりだ", "決めなければならない", "決められない", "決めるはずだ"],
        "correct_index": 2,
        "translation_vi": "Nếu không bàn bạc kỹ với gia đình trước thì tôi chưa thể quyết định có chuyển việc hay không.",
        "explanation_vi": "Vế sau của ～てからでないと bắt buộc mang nghĩa PHỦ ĐỊNH hoặc BẤT KHẢ NĂNG ('chưa thể quyết định được') -> 決められない.",
        "option_diagnostics": [
            "[SAI - Vế sau khẳng định ý định]: 'Nếu chưa bàn với gia đình thì tôi định quyết định' là mâu thuẫn hoàn toàn về logic.",
            "[SAI - Ngược nghĩa bắt buộc]: 'Nếu chưa bàn thì phải quyết định' sai hẳn ý nghĩa điều kiện tiên quyết.",
            "[ĐÚNG - Vế sau bất khả năng / phủ định]: Vてからでないと hô ứng với 決められない.",
            "[SAI - Sai logic suy đoán]: 'Chắc chắn sẽ quyết định nếu chưa bàn' là vô lý.",
        ],
    },
    # --- GP-N3-004 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-004-F",
        "grammar_code": "GP-N3-004",
        "drill_type": "formation",
        "prompt_jp": "今年の国際交流会に向けて、（　　）第1回目の会議を行います。",
        "options": ["下記どおり", "下記のとおり", "下記のどおり", "下記とおり"],
        "correct_index": 1,
        "translation_vi": "Hướng tới buổi giao lưu quốc tế năm nay, chúng tôi tổ chức cuộc họp lần thứ 1 như dưới đây.",
        "explanation_vi": "Cụm văn bản hành chính chuẩn là 下記のとおり (có の thì đọc とおり không đục; bỏ の mới ghép 予定どおり).",
        "option_diagnostics": [
            "[SAI - Dùng không tự nhiên với 下記]: 下記 thường nối qua trợ từ の thành 下記のとおり chứ ít ghép *下記どおり.",
            "[ĐÚNG - N + の + とおり]: Cụm chuẩn mực trong mọi thông báo, email Nhật.",
            "[SAI - Lỗi biến âm đục sau の]: Khi đã có trợ từ の đứng trước thì đọc là とおり (không thêm tenten thành どおり!).",
            "[SAI - Thiếu cả の lẫn biến âm]: Danh từ ghép trực tiếp với とおり không có の phải biến âm thành どおり.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-004-C",
        "grammar_code": "GP-N3-004",
        "drill_type": "contrast",
        "prompt_jp": "説明書に書いて（　　）組み立てたのに、なぜかうまく動かない。",
        "options": ["あるとおりに", "いるうちに", "あるかわりに", "おいたおかげで"],
        "correct_index": 0,
        "translation_vi": "Mặc dù tôi đã lắp ráp theo đúng như những gì viết trên tờ hướng dẫn, không hiểu sao vẫn không chạy được.",
        "explanation_vi": "Thực hiện đúng theo nội dung có sẵn trên hướng dẫn dùng 普通形 (書いてある) + とおりに.",
        "option_diagnostics": [
            "[ĐÚNG - V普通形 + とおりに]: 書いてあるとおりに = đúng như những gì đã viết sẵn.",
            "[SAI - Sai nghĩa thời gian]: うちに nghĩa là 'trong lúc đang...', không hợp hành động làm theo hướng dẫn.",
            "[SAI - Sai nghĩa thay thế]: かわりに nghĩa là 'thay cho việc viết', vô nghĩa.",
            "[SAI - Ngược kết quả xấu]: おかげで chỉ kết quả tốt đẹp, mâu thuẫn với うまく動かない.",
        ],
    },
    # --- GP-N3-005 (formation + contrast + application) ---
    {
        "drill_key": "DR-GP-N3-005-F",
        "grammar_code": "GP-N3-005",
        "drill_type": "formation",
        "prompt_jp": "昨日の台風（　　）被害は、全国で数百億円にのぼった。",
        "options": ["によっての", "による", "によると", "によれば"],
        "correct_index": 1,
        "translation_vi": "Thiệt hại do cơn bão hôm qua gây ra lên tới hàng chục tỷ yên trên toàn quốc.",
        "explanation_vi": "Khi nối giữa 2 danh từ (N1 gây ra N2: 台風 + ___ + 被害), bắt buộc dùng による (tuyệt đối không dùng *によっての).",
        "option_diagnostics": [
            "[SAI - Lỗi thêm の vào sau によって]: Tiếng Nhật không dùng *によっての để bổ nghĩa danh từ; phải đổi sang による.",
            "[ĐÚNG - N1 + による + N2]: Chỉ nguyên nhân/tác nhân của danh từ 被害 phía sau.",
            "[SAI - Nhầm sang trích dẫn nguồn tin]: によると chỉ đứng cuối cụm dẫn nguồn, không đặt trước danh từ 被害 để chỉ tác nhân gây hại.",
            "[SAI - Nhầm trích dẫn nguồn tin]: によれば không bổ nghĩa trực tiếp cho danh từ 被害.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-005-C",
        "grammar_code": "GP-N3-005",
        "drill_type": "contrast",
        "prompt_jp": "窓から入ってくる風は、植物が出す水分（　　）冷やされている。",
        "options": ["にとって", "につれて", "によって", "にともなって"],
        "correct_index": 2,
        "translation_vi": "Luồng gió thổi qua cửa sổ được làm mát bởi hơi nước do cây tỏa ra.",
        "explanation_vi": "Vị ngữ cuối câu ở thể BỊ ĐỘNG (冷やされている = được làm mát) -> tác nhân/phương tiện gây ra bị động bắt buộc dùng によって.",
        "option_diagnostics": [
            "[SAI - Nhầm sang lập trường đánh giá]: にとって ('đối với') chỉ đi với câu đánh giá (như 必要だ/大切だ), không chỉ tác nhân gây ra động từ bị động.",
            "[SAI - Nhầm biến đổi tỷ lệ thuận]: につれて đòi hỏi 2 quá trình biến đổi song hành, không hợp câu bị động mô tả cơ chế làm mát.",
            "[ĐÚNG - Tác nhân câu bị động によって]: 水分 + によって + 冷やされている.",
            "[SAI - Nhầm biến đổi kéo theo]: にともなって chỉ sự kiện kéo theo biến đổi, không chỉ tác nhân bị động.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-005-A",
        "grammar_code": "GP-N3-005",
        "drill_type": "application",
        "prompt_jp": "ここにたくさんのびんがあります。大きさ（　　）三つに分けてください。",
        "options": ["に比べて", "について", "によって", "に対して"],
        "correct_index": 2,
        "translation_vi": "Ở đây có rất nhiều chai lọ. Hãy phân loại thành ba nhóm tùy theo kích cỡ.",
        "explanation_vi": "Dựa theo tiêu chí phân loại ('tùy theo kích cỡ' mà chia nhóm) dùng N + によって.",
        "option_diagnostics": [
            "[SAI - Sai nghĩa đối chiếu]: に比べて nghĩa là 'so với kích cỡ', không mang nghĩa lấy kích cỡ làm tiêu chí phân nhóm.",
            "[SAI - Sai nghĩa chủ đề]: について nghĩa là 'nói/viết về chủ đề kích cỡ', sai với hành động 分ける.",
            "[ĐÚNG - Tiêu chí phân loại によって]: 大きさによって分ける.",
            "[SAI - Sai nghĩa đối tượng/tương phản]: に対して nghĩa là 'đối với' hoặc 'trái ngược với', không chỉ tiêu chuẩn phân loại.",
        ],
    },
    # --- GP-N3-006 (formation + application) ---
    {
        "drill_key": "DR-GP-N3-006-F",
        "grammar_code": "GP-N3-006",
        "drill_type": "formation",
        "prompt_jp": "この古い写真を（　　）たびに、国にいる家族のことを思い出す。",
        "options": ["見た", "見る", "見て", "見ている"],
        "correct_index": 1,
        "translation_vi": "Cứ mỗi lần nhìn tấm ảnh cũ này, tôi lại nhớ đến gia đình ở quê nhà.",
        "explanation_vi": "Trước ～たびに (cứ mỗi khi...) BẮT BUỘC dùng động từ thể từ điển Vる (không chia Vた dù câu mang sắc thái hồi tưởng).",
        "option_diagnostics": [
            "[SAI - Lỗi chia quá khứ trước たびに]: Dù diễn tả thói quen nhiều lần, trước たびに cấm dùng quá khứ Vた (*見たたびに).",
            "[ĐÚNG - Vる + たびに]: Nguyên thể 見る + たびに.",
            "[SAI - Sai dạng thể て]: Thể て không gắn trực tiếp trước たびに.",
            "[SAI - Sai dạng tiếp diễn]: Không dùng ている trước たびに.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-006-A",
        "grammar_code": "GP-N3-006",
        "drill_type": "application",
        "prompt_jp": "姉は海外へ出張する（　　）、私にかわいいお土産を買ってきてくれる。",
        "options": ["うちに", "たびに", "かわりに", "せいで"],
        "correct_index": 1,
        "translation_vi": "Cứ mỗi lần chị gái đi công tác nước ngoài là lại mua quà lưu niệm dễ thương về cho tôi.",
        "explanation_vi": "Sự việc lặp lại đều đặn mỗi khi xảy ra sự kiện A ('cứ mỗi lần đi công tác là lại mua quà') -> Vる + たびに.",
        "option_diagnostics": [
            "[SAI - Sai nghĩa thời gian tranh thủ]: うちに nghĩa là 'tranh thủ lúc đang đi công tác thì...', không nhấn mạnh sự lặp lại nhiều lần.",
            "[ĐÚNG - Quy luật lặp lại たびに]: 出張するたびに = cứ mỗi lần đi công tác.",
            "[SAI - Sai nghĩa thay thế]: かわりに nghĩa là 'thay vì đi công tác', vô lý.",
            "[SAI - Sai sắc thái tiêu cực]: せいで chỉ kết quả xấu, trái nghĩa hoàn toàn với nhận quà đáng yêu.",
        ],
    },
    # --- GP-N3-007 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-007-F",
        "grammar_code": "GP-N3-007",
        "drill_type": "formation",
        "prompt_jp": "部屋の荷物は増えれば（　　）ほど、引っ越しのとき大変になる。",
        "options": ["増えた", "増える", "増えて", "増えよう"],
        "correct_index": 1,
        "translation_vi": "Đồ đạc trong phòng càng nhiều lên bao nhiêu thì lúc chuyển nhà càng vất vả bấy nhiêu.",
        "explanation_vi": "Cấu trúc lặp tỷ lệ thuận [Vば + Vる + ほど]: vế sau lặp lại động từ đó ở thể TỪ ĐIỂN Vる (増える).",
        "option_diagnostics": [
            "[SAI - Chia quá khứ trước ほど trong mẫu lặp]: Không dùng thì quá khứ Vた trong cặp tỷ lệ thuận Vば + Vる + ほど.",
            "[ĐÚNG - Vば + Vる + ほど]: 増えれば + 増える + ほど.",
            "[SAI - Thể て không đứng trước ほど]: Không có mẫu *増えてほど.",
            "[SAI - Thể ý chí sai cấu trúc]: Không dùng thể ý chí trước ほど.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-007-C",
        "grammar_code": "GP-N3-007",
        "drill_type": "contrast",
        "prompt_jp": "練習を（　　）ほど、難しい曲も上手にひけるようになる。",
        "options": ["すればする", "したらする", "している", "するばかり"],
        "correct_index": 0,
        "translation_vi": "Càng luyện tập nhiều thì càng chơi được những bản nhạc khó một cách điêu luyện.",
        "explanation_vi": "Quy luật tỷ lệ thuận đầy đủ dùng cặp lặp [Vば + Vる + ほど] -> すればするほど.",
        "option_diagnostics": [
            "[ĐÚNG - Cặp chuẩn Vば + Vる + ほど]: する -> すればする + ほど.",
            "[SAI - Lỗi ghép たら thay cho ば]: Trong mẫu lặp ～ほど chỉ dùng thể điều kiện ば (すれば), không dùng たら (*したらするほど).",
            "[SAI - Thiếu tính quy luật tỷ lệ thuận]: しているほど không diễn đạt đúng nghĩa 'càng luyện càng giỏi'.",
            "[SAI - Sai nghĩa 'suốt ngày']: するばかりほど nghĩa là 'đến mức suốt ngày chỉ toàn luyện tập', lệch ý tỷ lệ thuận.",
        ],
    },
    # --- GP-N3-008 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-008-C",
        "grammar_code": "GP-N3-008",
        "drill_type": "contrast",
        "prompt_jp": "犬の散歩の（　　）、コンビニに寄って電気代を払ってきた。",
        "options": ["かわりに", "ついでに", "ために", "うちに"],
        "correct_index": 1,
        "translation_vi": "Nhân tiện đi dắt chó đi dạo, tôi ghé vào cửa hàng tiện lợi đóng tiền điện luôn.",
        "explanation_vi": "Làm thêm việc phụ (đóng tiền điện) trong lúc đang làm việc chính (dắt chó đi dạo) dùng N + の + ついでに.",
        "option_diagnostics": [
            "[SAI - Sai nghĩa thay thế]: かわりに nghĩa là 'thay vì dắt chó đi dạo thì tôi đi đóng tiền', sai với việc làm cả hai.",
            "[ĐÚNG - Làm ghép việc phụ ついでに]: 散歩 + の + ついでに.",
            "[SAI - Sai quan hệ mục đích]: Đóng tiền điện không phải mục đích chính của việc dắt chó đi dạo.",
            "[SAI - Sai sắc thái tranh thủ kẻo lỡ]: うちに nhấn mạnh tranh thủ trước khi trạng thái kết thúc, kém tự nhiên hơn ついでに cho việc tiện đường ghé qua.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-008-A",
        "grammar_code": "GP-N3-008",
        "drill_type": "application",
        "prompt_jp": "スーパーへ牛乳を買いに（　　）、ポストに手紙を出してきてもらえますか。",
        "options": ["行くついでに", "行ってからでないと", "行くくせに", "行くせいで"],
        "correct_index": 0,
        "translation_vi": "Nhân tiện lúc đi siêu thị mua sữa, bạn bỏ giúp tôi bức thư vào hòm thư được không?",
        "explanation_vi": "Nhờ vả thêm việc tiện đường trong khi người kia sắp làm việc chính (đi siêu thị) dùng Vる + ついでに.",
        "option_diagnostics": [
            "[ĐÚNG - Vる + ついでに]: Việc chính sắp đi làm + việc phụ nhờ ghép thêm.",
            "[SAI - Sai logic điều kiện]: Không có lý do gì 'phải mua sữa xong rồi mới có khả năng gửi thư'.",
            "[SAI - Sai sắc thái chê trách]: くせに là mắng mỏ hành vi mâu thuẫn, không dùng khi nhờ vả lịch sự.",
            "[SAI - Sai sắc thái kết quả xấu]: せいで chỉ nguyên nhân gây hậu quả xấu.",
        ],
    },
    # --- GP-N3-009 (formation + application) ---
    {
        "drill_key": "DR-GP-N3-009-F",
        "grammar_code": "GP-N3-009",
        "drill_type": "formation",
        "prompt_jp": "この店のケーキは本当においしい。毎日（　　）くらいだ。",
        "options": ["食べたい", "食べたくて", "食べよう", "食べて"],
        "correct_index": 0,
        "translation_vi": "Bánh ngọt của tiệm này ngon thật sự. Ngon đến mức ngày nào tôi cũng muốn ăn.",
        "explanation_vi": "Trước ～くらいだ chỉ mức độ dùng thể thông thường (Aい/Vる/Vたい) -> 毎日食べたいくらいだ.",
        "option_diagnostics": [
            "[ĐÚNG - 普通形 (Vたい) + くらいだ]: Biểu đạt mức độ cao bằng mong muốn.",
            "[SAI - Sai dạng nối trước くらい]: Thể て (食べたくて) không gắn trực tiếp vào くらいだ.",
            "[SAI - Thể ý chí không gắn trực tiếp trước くらい]: Không viết *食べようくらいだ.",
            "[SAI - Thể て không nối với くらいだ]: Không viết *食べてくらいだ.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-009-A",
        "grammar_code": "GP-N3-009",
        "drill_type": "application",
        "prompt_jp": "頭から離れないほど大好きで、毎日（　　）くらい聞こえる大音量で流している人もいる。",
        "options": ["隣の人に", "隣の人が", "隣の人は", "隣の人を"],
        "correct_index": 0,
        "translation_vi": "Cũng có người thích quá đến mức mở âm lượng to đến cỡ người bên cạnh cũng nghe thấy.",
        "explanation_vi": "Với động từ tri giác tự nhiên 聞こえる, người cảm nhận được âm thanh đó (chủ thể nhận thức) đánh dấu bằng に (周りの人に聞こえるくらい).",
        "option_diagnostics": [
            "[ĐÚNG - Đối tượng tiếp nhận âm thanh に + 聞こえる]: 周りの人に聞こえるくらい (Passage 3).",
            "[SAI - Sai trợ từ chủ thể của âm thanh]: Trong 聞こえる, âm thanh đi với が (音が聞こえる), còn người nghe thấy đi với に.",
            "[SAI - Trợ từ は không hợp bên trong định ngữ]: Cụm 聞こえるくらい đang bổ nghĩa cho 大音量 nên tránh dùng は.",
            "[SAI - Sai tân ngữ]: 隣の人 không phải đối tượng bị âm thanh tác động bằng を.",
        ],
    },
    # --- GP-N3-010 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-010-C",
        "grammar_code": "GP-N3-010",
        "drill_type": "contrast",
        "prompt_jp": "私にとって、家族と一緒に過ごす時間（　　）大切なものはない。",
        "options": ["ほど", "こそ", "だけ", "ばかり"],
        "correct_index": 0,
        "translation_vi": "Đối với tôi, không có thứ gì quý giá bằng khoảng thời gian ở bên gia đình.",
        "explanation_vi": "Cấu trúc so sánh nhất khẳng định không gì sánh bằng [N + ほど + A + ものはない] -> ほど.",
        "option_diagnostics": [
            "[ĐÚNG - So sánh nhất N + ほど + A + ものはない]: Đưa N lên vị trí số 1 không gì sánh bằng.",
            "[SAI - Lỗi ghép với 大切なものはない]: Nếu dùng こそ thì cuối câu phải khẳng định ('chính là thứ quan trọng'), không đi với phủ định '...はない'.",
            "[SAI - Sai nghĩa giới hạn]: だけ không tạo nghĩa so sánh 'bằng' trong '...大切なものはない'.",
            "[SAI - Sai nghĩa 'toàn là']: ばかり không dùng trong cấu trúc so sánh nhất.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-010-A",
        "grammar_code": "GP-N3-010",
        "drill_type": "application",
        "prompt_jp": "今年の夏は暑いと言われているが、去年の猛暑（　　）ではない。",
        "options": ["ほど", "こそ", "だけ", "さえ"],
        "correct_index": 0,
        "translation_vi": "Mùa hè năm nay được nói là nóng, nhưng không đến mức bằng cái nắng gay gắt năm ngoái.",
        "explanation_vi": "So sánh phủ định 'không bằng/không đến mức như năm ngoái' dùng [N + ほど + ではない].",
        "option_diagnostics": [
            "[ĐÚNG - So sánh phủ định ほどではない]: 去年の猛暑ほどではない.",
            "[SAI - Sai nghĩa phủ định]: こそ không dùng để phủ nhận mức độ bằng nhau.",
            "[SAI - Sai nghĩa]: だけではない nghĩa là 'không chỉ mỗi cái nắng năm ngoái', sai ý so sánh mức độ.",
            "[SAI - Sai nghĩa cực đoan]: さえ không mang nghĩa so sánh 'đến mức bằng'.",
        ],
    },
    # --- GP-N3-011 (formation + application) ---
    {
        "drill_key": "DR-GP-N3-011-F",
        "grammar_code": "GP-N3-011",
        "drill_type": "formation",
        "prompt_jp": "あんな失礼な人に頼む（　　）、自分で徹夜して終わらせたほうがましだ。",
        "options": ["くらいなら", "ほどなら", "ばかりなら", "だけなら"],
        "correct_index": 0,
        "translation_vi": "Nếu phải nhờ một người thất lễ như thế thì thà tự mình thức trắng đêm làm cho xong còn hơn.",
        "explanation_vi": "Hô ứng chặt chẽ với ほうがましだ ('thà làm B còn hơn là phải chịu A') là [Vる + くらいなら].",
        "option_diagnostics": [
            "[ĐÚNG - Cặp cố định くらいなら ～ほうがましだ]: Vる + くらいなら.",
            "[SAI - Không dùng ほどなら trong mẫu này]: Để nối với ほうがましだ, tiếng Nhật cố định dùng くらいなら chứ không dùng *ほどなら.",
            "[SAI - Không tồn tại mẫu *ばかりなら～ほうがましだ]: ばかり không dùng để bày tỏ sự ghét bỏ lựa chọn A.",
            "[SAI - Sai nghĩa]: だけなら nghĩa là 'nếu chỉ nhờ thôi thì...', không mang nghĩa thà chọn cách B còn hơn.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-011-A",
        "grammar_code": "GP-N3-011",
        "drill_type": "application",
        "prompt_jp": "毎日2時間も満員電車に揺られて通うくらいなら、会社の近くに（　　）。",
        "options": ["引っ越したほうがいい", "引っ越すにちがいない", "引っ越すわけにはいかない", "引っ越すおそれがある"],
        "correct_index": 0,
        "translation_vi": "Nếu mỗi ngày phải chen chúc trên tàu đông suốt 2 tiếng để đi làm thì thà chuyển nhà tới gần công ty còn hơn.",
        "explanation_vi": "Vế trước dùng くらいなら để bác bỏ cảnh chịu đựng quá khổ, vế sau bắt buộc chọn giải pháp thay thế đỡ tệ hơn với ほうがいい / ほうがましだ.",
        "option_diagnostics": [
            "[ĐÚNG - Vế sau đề xuất phương án thay thế]: 引っ越したほうがいい / ほうがましだ.",
            "[SAI - Sai ngữ nghĩa suy đoán]: くらいなら không dùng để phỏng đoán chắc chắn điều gì sẽ xảy ra.",
            "[SAI - Ngược logic câu]: Không thể dùng わけにはいかない ('không thể chuyển nhà') sau くらいなら ('nếu phải chịu cảnh kia thì thà...').",
            "[SAI - Sai ngữ dụng cảnh báo rủi ro]: おそれがある cảnh báo nguy hiểm, không dùng chọn phương án thay thế.",
        ],
    },
    # --- GP-N3-012 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-012-C",
        "grammar_code": "GP-N3-012",
        "drill_type": "contrast",
        "prompt_jp": "暑い夏の夜に飲むのは、やっぱり冷たい麦茶（　　）。",
        "options": ["とは限らない", "に限る", "にすぎない", "にかかわらない"],
        "correct_index": 1,
        "translation_vi": "Thức uống vào đêm hè nóng bức thì quả nhiên cứ phải là trà lúa mạch lạnh mới là nhất.",
        "explanation_vi": "Thấy phó từ やっぱり (quả nhiên) và nhận xét cá nhân khen phương án tối ưu số 1 -> chọn N + に限る.",
        "option_diagnostics": [
            "[SAI - Nhầm sang phủ định ngoại lệ]: とは限らない nghĩa là 'chưa chắc đã là trà lúa mạch', trái với giọng điệu khẳng định やっぱり.",
            "[ĐÚNG - Khẳng định lựa chọn số 1 に限る]: やっぱり ～ に限る.",
            "[SAI - Hạ thấp giá trị]: にすぎない nghĩa là 'chẳng qua chỉ là trà thôi', trái nghĩa đề cao.",
            "[SAI - Sai cấu trúc và nghĩa]: にかかわらない nghĩa là 'không liên quan đến'.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-012-A",
        "grammar_code": "GP-N3-012",
        "drill_type": "application",
        "prompt_jp": "風邪をひきそうなときは、無理をしないで（　　）に限ります。",
        "options": ["ゆっくり休む", "ゆっくり休んだ", "ゆっくり休むの", "ゆっくり休んで"],
        "correct_index": 0,
        "translation_vi": "Những lúc sắp bị cảm thì đừng cố quá, cứ nghỉ ngơi thong thả là tốt nhất.",
        "explanation_vi": "Trước ～に限る chỉ dùng động từ nguyên thể Vる (hoặc Vない / Danh từ), không chia quá khứ Vた hay thêm の.",
        "option_diagnostics": [
            "[ĐÚNG - Vる + に限る]: 休む + に限ります.",
            "[SAI - Sai thì quá khứ]: Đưa ra lời khuyên kinh nghiệm chung trước に限る không dùng thì quá khứ Vた.",
            "[SAI - Thừa trợ từ の]: Không chèn の vào giữa Vる và に限る.",
            "[SAI - Sai dạng thể て]: Thể て không gắn trực tiếp vào に限る.",
        ],
    },
    # --- GP-N3-013 (formation + contrast + application) ---
    {
        "drill_key": "DR-GP-N3-013-F",
        "grammar_code": "GP-N3-013",
        "drill_type": "formation",
        "prompt_jp": "こちらの店が値段が（　　）、あちらの店は量が多いことで評判だ。",
        "options": ["安いに対して", "安いのに対して", "安いなに対して", "安くに対して"],
        "correct_index": 1,
        "translation_vi": "Trái ngược với quán bên này giá rẻ, quán bên kia nổi tiếng vì đồ ăn nhiều.",
        "explanation_vi": "Khi ～に対して nối hai MỆNH ĐỀ tương phản nhau (mệnh đề 1 kết thúc bằng tính từ/động từ), bắt buộc phải danh từ hóa bằng の -> 安いのに対して.",
        "option_diagnostics": [
            "[SAI - Thiếu trợ từ の]: に対して chỉ gắn trực tiếp sau Danh từ; khi đứng sau động từ/tính từ BẮT BUỘC phải thêm の.",
            "[ĐÚNG - 普通形 + のに対して]: 安い + のに対して đối chiếu hai vế tương phản.",
            "[SAI - Lỗi thêm な sau Aい]: 安い là tính từ đuôi い, không bao giờ thêm な (*安いな).",
            "[SAI - Chia sai dạng く]: Không gắn に対して sau dạng phó từ く.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-013-C",
        "grammar_code": "GP-N3-013",
        "drill_type": "contrast",
        "prompt_jp": "会社では、目上の人（　　）丁寧な言葉遣いを心がけるべきだ。",
        "options": ["にとって", "に対して", "によって", "について"],
        "correct_index": 1,
        "translation_vi": "Ở công ty, chúng ta nên chú ý dùng ngôn từ lịch sự đối với người bề trên.",
        "explanation_vi": "Hướng thái độ, lời nói, hành động (dùng kính ngữ/lịch sự) TỚI một đối tượng cụ thể dùng N + に対して (không dùng にとって vốn chỉ đứng từ góc nhìn của N để đánh giá).",
        "option_diagnostics": [
            "[SAI - Nhầm lập trường đánh giá với đối tượng nhận hành động]: 目上の人にとって nghĩa là 'đứng trên lập trường của cấp trên mà đánh giá', không dùng cho hành động nói kính ngữ VỚI cấp trên.",
            "[ĐÚNG - Đối tượng nhận thái độ/hành động に対して]: 目上の人に対して + hành động 丁寧な言葉遣い.",
            "[SAI - Sai nghĩa 'tùy theo / bởi']: によって không chỉ đối tượng mình hướng lời nói lịch sự tới.",
            "[SAI - Sai nghĩa 'bàn luận về']: について nghĩa là 'nói về đề tài cấp trên', không phải nói lịch sự với họ.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-013-A",
        "grammar_code": "GP-N3-013",
        "drill_type": "application",
        "prompt_jp": "政府の新しい政策（　　）国民の意見は、賛成と反対に分かれている。",
        "options": ["に対しての", "に対する", "にとっての", "につれての"],
        "correct_index": 1,
        "translation_vi": "Ý kiến của người dân đối với chính sách mới của chính phủ đang chia rẽ thành tán thành và phản đối.",
        "explanation_vi": "Bổ nghĩa danh từ N2 (国民の意見) bằng 'đối với N1' (政策) chuẩn mực dùng N1 + に対する + N2.",
        "option_diagnostics": [
            "[SAI - Lỗi ghép の sau に対して]: Dạng bổ nghĩa danh từ chuẩn của に対して là に対する + N, tránh dùng *に対しての.",
            "[ĐÚNG - N1 + に対する + N2]: 政策に対する国民の意見.",
            "[SAI - Sai nghĩa lập trường]: Ý kiến phản ứng lại/hướng về chính sách chứ không phải chính sách đánh giá gì.",
            "[SAI - Sai nghĩa và hình thái]: につれて không có dạng *につれての bổ nghĩa danh từ kiểu này.",
        ],
    },
    # --- GP-N3-014 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-014-C",
        "grammar_code": "GP-N3-014",
        "drill_type": "contrast",
        "prompt_jp": "この薬は症状を抑える効果が高い（　　）、眠くなるという副作用もある。",
        "options": ["かわりに", "反面", "のに対して", "おかげで"],
        "correct_index": 1,
        "translation_vi": "Loại thuốc này hiệu quả kìm chế triệu chứng cao, nhưng mặt khác cũng có tác dụng phụ là gây buồn ngủ.",
        "explanation_vi": "Nêu ưu điểm và nhược điểm cùng tồn tại trên CÙNG MỘT ĐỐI TƯỢNG (この薬) dùng ～反面.",
        "option_diagnostics": [
            "[SAI - Sắc thái trao đổi/bù trừ kém tự nhiên bằng 反面]: かわりに thiên về sự lựa chọn thay thế hoặc bù trừ; với 2 mặt ưu-nhược cố hữu của 1 sự vật, chuẩn N3 là 反面.",
            "[ĐÚNG - 2 mặt đối lập của cùng 1 đối tượng]: 効果が高い (tốt) <-> 副作用もある (xấu) trên cùng この薬.",
            "[SAI - Thường dùng đối lập 2 đối tượng A vs B khác nhau]: Khi chỉ có 1 chủ thể duy nhất mang cả tốt lẫn xấu, dùng 反面 (còn のに対して thiếu の ở trước nếu chọn không có の, và ở đây đã ghi のに対して cũng thiên về so sánh 2 chủ thể khác nhau).",
            "[SAI - Ngược kết quả xấu]: Vế sau là tác dụng phụ tiêu cực, không thể dùng おかげで.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-014-A",
        "grammar_code": "GP-N3-014",
        "drill_type": "application",
        "prompt_jp": "インターネットは（　　）反面、個人情報が漏れる危険性もある。",
        "options": ["便利", "便利な", "便利だ", "便利の"],
        "correct_index": 1,
        "translation_vi": "Internet tuy tiện lợi nhưng mặt khác cũng có nguy cơ rò rỉ thông tin cá nhân.",
        "explanation_vi": "Trước danh từ 反面, tính từ đuôi な (便利) bắt buộc thêm な (hoặc である) -> 便利な反面.",
        "option_diagnostics": [
            "[SAI - Thiếu な sau tính từ đuôi な]: Không gắn trực tiếp *便利反面.",
            "[ĐÚNG - Aな + な + 反面]: 便利な反面.",
            "[SAI - Dùng dạng kết thúc câu だ]: だ không đứng trước danh từ 反面.",
            "[SAI - Lỗi ghép の cho tính từ な]: 便利 là tính từ đuôi な nên dùng な, không dùng の.",
        ],
    },
    # --- GP-N3-015 (formation + application) ---
    {
        "drill_key": "DR-GP-N3-015-F",
        "grammar_code": "GP-N3-015",
        "drill_type": "formation",
        "prompt_jp": "少子高齢化が進み、地方の人口はこれからも（　　）一方だ。",
        "options": ["減った", "減る", "減って", "減り"],
        "correct_index": 1,
        "translation_vi": "Tình trạng ít con và già hóa dân số tiến triển khiến dân số vùng địa phương từ nay về sau ngày càng giảm.",
        "explanation_vi": "Mẫu xu hướng một chiều [Vる + 一方だ] luôn đi với động từ biến đổi ở thể nguyên thể Vる -> 減る一方だ.",
        "option_diagnostics": [
            "[SAI - Sai thì quá khứ trước 一方だ]: Không chia quá khứ Vた trước 一方だ (nếu kể quá khứ thì chia ở cuối câu: 減る一方だった).",
            "[ĐÚNG - Vる(biến đổi) + 一方だ]: 減る一方だ = ngày càng giảm đi một chiều.",
            "[SAI - Thể て không đứng trước 一方だ]: Không có *減って一方だ.",
            "[SAI - Gốc Vます không đứng trước 一方だ]: Phải giữ nguyên thể Vる (đừng nhầm với Vます + つつある).",
        ],
    },
    {
        "drill_key": "DR-GP-N3-015-A",
        "grammar_code": "GP-N3-015",
        "drill_type": "application",
        "prompt_jp": "英語などの実用科目が重視されている。（　　）、古典や歴史も必要ないと言う人が増えているそうだ。",
        "options": ["一方で", "一方だ", "反面で", "ためで"],
        "correct_index": 0,
        "translation_vi": "Các môn thực dụng như tiếng Anh đang được coi trọng. Mặt khác, nghe nói người cho rằng cổ văn và lịch sử không cần thiết cũng đang tăng.",
        "explanation_vi": "Đặt ở đầu câu hoặc giữa câu để chuyển sang mặt đối lập/xu hướng song song khác dùng 一方で (như Passage 2).",
        "option_diagnostics": [
            "[ĐÚNG - Liên từ tương phản/song hành 一方で]: Đứng đầu câu mở sang vế đối lập thứ hai.",
            "[SAI - Dùng sai vị trí đuôi câu 一方だ]: 一方だ là đuôi vị ngữ kết thúc câu sau Vる, không đặt độc lập đầu câu.",
            "[SAI - Không dùng liên từ đứng đầu câu *反面で]: 反面 dùng nối 2 mệnh đề hoặc その反面.",
            "[SAI - Sai từ nối]: *ためで không đứng đầu câu tách rời bằng dấu phẩy như liên từ.",
        ],
    },
    # --- GP-N3-016 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-016-F",
        "grammar_code": "GP-N3-016",
        "drill_type": "formation",
        "prompt_jp": "あの人は先生（　　）、何でも相談できる頼もしい友達のような存在だ。",
        "options": ["というより", "のより", "というなら", "だけより"],
        "correct_index": 0,
        "translation_vi": "Người đó nói là thầy giáo thì đúng hơn là một người bạn đáng tin cậy có thể tâm sự mọi chuyện.",
        "explanation_vi": "Đánh giá cách gọi B chuẩn xác hơn cách gọi A dùng cấu trúc [A + というより + B].",
        "option_diagnostics": [
            "[ĐÚNG - N + というより]: Hạ nhẹ danh xưng A để đề cao danh xưng B sát hơn.",
            "[SAI - Không tồn tại *のより]: Không ghép の vào trước より để nói 'nói là A thì đúng hơn B'.",
            "[SAI - Sai nghĩa giả định]: というなら nghĩa là 'nếu gọi như thế thì...', không có nghĩa so sánh cách gọi chuẩn hơn.",
            "[SAI - Sai ngữ pháp]: Không ghép *だけより.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-016-C",
        "grammar_code": "GP-N3-016",
        "drill_type": "contrast",
        "prompt_jp": "今年の梅雨は、雨が降る（　　）毎日蒸し暑い日ばかり続いている。",
        "options": ["かわりに", "というより", "たびに", "せいで"],
        "correct_index": 1,
        "translation_vi": "Mùa mưa năm nay nói là trời mưa thì đúng hơn là suốt ngày chỉ thấy những ngày oi bức nối tiếp.",
        "explanation_vi": "Chỉnh lại cách mô tả tính chất thực tế (không hẳn mưa nhiều mà đúng hơn là toàn ngày oi nồng) dùng というより.",
        "option_diagnostics": [
            "[SAI - Sai nghĩa thay thế có chủ đích]: Thời tiết không 'cố ý thay thế' mưa bằng nóng ẩm.",
            "[ĐÚNG - Sửa cách diễn đạt chính xác hơn というより]: 降るというより～日ばかり続いている.",
            "[SAI - Sai nghĩa lặp lại]: Không phải 'cứ mỗi lần mưa thì oi bức'.",
            "[SAI - Sai quan hệ nhân quả]: Không nói 'tại vì trời mưa nên mới toàn ngày không mưa mà oi bức'.",
        ],
    },
    # --- GP-N3-017 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-017-C",
        "grammar_code": "GP-N3-017",
        "drill_type": "contrast",
        "prompt_jp": "けがをして出られなくなった先輩の（　　）、私が代表として出場することになった。",
        "options": ["かわりに", "ために", "せいで", "とおりに"],
        "correct_index": 0,
        "translation_vi": "Thay cho người đàn anh bị chấn thương không thể thi đấu, tôi được quyết định ra sân với tư cách đại diện.",
        "explanation_vi": "Vào thay vị trí của người khác dùng [N + の + かわりに] (Q#57).",
        "option_diagnostics": [
            "[ĐÚNG - N + の + かわりに (Thay thế)]: 先輩のかわりに.",
            "[SAI - Nhầm mục đích/lợi ích]: ために nghĩa là 'vì đàn anh', nhưng chính xác trong tình huống thi đấu hộ là 'thay vị trí của đàn anh'.",
            "[SAI - Sắc thái đổ lỗi]: Đàn anh bị thương không phải nguyên nhân đáng trách theo kiểu đổ lỗi của せいで.",
            "[SAI - Sai nghĩa 'đúng theo']: Không phải làm 'đúng theo đàn anh'.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-017-A",
        "grammar_code": "GP-N3-017",
        "drill_type": "application",
        "prompt_jp": "リーさんに英語を教えてもらう（　　）、私はリーさんに日本語を教えている。",
        "options": ["うちに", "かわりに", "せいで", "どころか"],
        "correct_index": 1,
        "translation_vi": "Đổi lại (bù lại) việc được bạn Lee dạy tiếng Anh, tôi đang dạy tiếng Nhật cho bạn Lee.",
        "explanation_vi": "Trao đổi có qua có lại giữa 2 hành động tương ứng dùng [Vる + かわりに].",
        "option_diagnostics": [
            "[SAI - Sai nghĩa thời gian]: うちに nghĩa là 'trong lúc được dạy tiếng Anh thì tự nhiên dạy tiếng Nhật', sai nghĩa trao đổi.",
            "[ĐÚNG - Bù lại / Trao đổi có qua có lại]: 教えてもらうかわりに.",
            "[SAI - Sai sắc thái tiêu cực]: Dạy trao đổi ngôn ngữ không phải hậu quả xấu nên loại せいで.",
            "[SAI - Sai nghĩa phủ nhận]: どころか bác bỏ vế trước, không dùng cho việc cùng thực hiện cả hai.",
        ],
    },
    # --- GP-N3-018 (formation + application) ---
    {
        "drill_key": "DR-GP-N3-018-F",
        "grammar_code": "GP-N3-018",
        "drill_type": "formation",
        "prompt_jp": "二人は顔や話し方がよく似ている（　　）、すぐに親子だとわかった。",
        "options": ["ことから", "ことに", "ことには", "ことを"],
        "correct_index": 0,
        "translation_vi": "Từ việc khuôn mặt và cách nói chuyện rất giống nhau, mọi người nhận ra ngay hai người là cha con.",
        "explanation_vi": "Căn cứ quan sát khách quan dẫn đến suy luận nhận biết (とわかった) dùng 普通形 + ことから.",
        "option_diagnostics": [
            "[ĐÚNG - Căn cứ suy luận ことから]: 似ている + ことから + わかった.",
            "[SAI - Nhầm cảm xúc bất ngờ]: ことに chỉ cảm xúc (驚くことに = đáng ngạc nhiên là), không gắn sau động từ 似ている để chỉ căn cứ suy luận.",
            "[SAI - Sai cấu trúc]: *似ていることには không diễn tả nguyên nhân căn cứ.",
            "[SAI - Thiếu động từ nhận tân ngữ]: Vế sau là とわかった (tự động từ nhận ra) chứ không phải tha động từ nhận tân ngữ trực tiếp với を.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-018-A",
        "grammar_code": "GP-N3-018",
        "drill_type": "application",
        "prompt_jp": "この山は形が富士山に似ていることから、地元の人々に「小富士」と（　　）。",
        "options": ["呼ばれるようになった", "呼ぶべきだ", "呼ぶつもりだ", "呼ぶわけにはいかない"],
        "correct_index": 0,
        "translation_vi": "Vì ngọn núi này có hình dáng giống núi Phú Sĩ nên từ đó được người dân địa phương gọi là 'Tiểu Phú Sĩ'.",
        "explanation_vi": "Giải thích nguồn gốc tên gọi sau ～ことから luôn đi kèm động từ gọi tên ở thể bị động (と呼ばれている / と呼ばれるようになった).",
        "option_diagnostics": [
            "[ĐÚNG - Nguồn gốc tên gọi ことから + と呼ばれる]: Cấu trúc đặc trưng giải thích tên địa danh.",
            "[SAI - Sai ngữ dụng khuyên bảo]: Không nói 'vì giống Phú Sĩ nên nên gọi như vậy'.",
            "[SAI - Sai chủ ngữ vô tri]: Ngọn núi không thể tự có 'dự định' (つもりだ).",
            "[SAI - Ngược nghĩa]: わけにはいかない ('không thể gọi được') vô lý với tên gọi đã có.",
        ],
    },
    # --- GP-N3-019 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-019-C",
        "grammar_code": "GP-N3-019",
        "drill_type": "contrast",
        "prompt_jp": "暑い夏でも快適に過ごせるのは、冷房という素晴らしい技術の（　　）。",
        "options": ["せいです", "おかげです", "ばかりです", "くせです"],
        "correct_index": 1,
        "translation_vi": "Việc có thể sống thoải mái ngay cả trong mùa hè nóng bức chính là nhờ vào công nghệ tuyệt vời mang tên điều hòa.",
        "explanation_vi": "Kết quả tích cực, thoải mái (快適に過ごせる) đòi hỏi nguyên nhân biết ơn ở cuối câu là おかげです (khác せいです vốn chỉ kết quả xấu).",
        "option_diagnostics": [
            "[SAI - Sai sắc thái kết quả xấu]: せいです chỉ nguyên nhân gây rắc rối tiêu cực, mâu thuẫn hoàn toàn với 快適に過ごせる.",
            "[ĐÚNG - N + の + おかげです (Kết quả tốt)]: Tri ân/đánh giá tích cực.",
            "[SAI - Sai cấu trúc và nghĩa]: 技術のばかりです sai ngữ pháp (ばかり không nối kiểu Nのばかりです cho nguyên nhân tốt).",
            "[SAI - Sai nghĩa 'tính xấu/thói quen']: くせです nghĩa là 'thói xấu của công nghệ', vô nghĩa.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-019-A",
        "grammar_code": "GP-N3-019",
        "drill_type": "application",
        "prompt_jp": "先生に丁寧に指導して（　　）、無事に志望校に合格することができた。",
        "options": ["いただいたおかげで", "いただいたせいで", "くださったくせに", "もらったばかりに"],
        "correct_index": 0,
        "translation_vi": "Nhờ được thầy giáo tận tình chỉ bảo giúp đỡ, tôi đã thi đỗ an toàn vào trường nguyện vọng.",
        "explanation_vi": "Kết quả tốt đẹp (合格できた) đi với việc được thầy giúp (指導していただく) -> いただいたおかげで.",
        "option_diagnostics": [
            "[ĐÚNG - Khiêm nhường nhận giúp đỡ + おかげで]: 指導していただいたおかげで.",
            "[SAI - Dùng せいで cho kết quả thi đỗ]: せいで mang nghĩa đổ lỗi tiêu cực, cấm dùng khi cảm ơn việc thi đỗ.",
            "[SAI - Dùng くせに chê trách thầy]: くせに là hỗn láo/chê trách, sai hoàn toàn văn phong biết ơn.",
            "[SAI - Dùng ばかりに cho kết quả tốt]: ばかりに nghĩa là 'chỉ tại vì... mà hỏng việc', sai sắc thái tích cực.",
        ],
    },
    # --- GP-N3-020 (formation + contrast + application) ---
    {
        "drill_key": "DR-GP-N3-020-F",
        "grammar_code": "GP-N3-020",
        "drill_type": "formation",
        "prompt_jp": "昨夜よく眠れなかった（　　）、今日は一日中頭がぼんやりしている。",
        "options": ["おかげで", "せいで", "せいに", "ためで"],
        "correct_index": 1,
        "translation_vi": "Tại vì tối qua không ngủ ngon nên hôm nay đầu óc cứ lơ mơ cả ngày.",
        "explanation_vi": "Nguyên nhân gây ra trạng thái mệt mỏi, khó chịu (頭がぼんやりしている) dùng [V普通形 + せいで] (dùng trợ từ で, không dùng に).",
        "option_diagnostics": [
            "[SAI - Sai sắc thái tích cực]: Không ai dùng おかげで ('nhờ có việc mất ngủ mà đầu óc lơ mơ') trừ khi nói mỉa.",
            "[ĐÚNG - V普通形 + せいで (Kết quả xấu)]: 眠れなかったせいで.",
            "[SAI - Sai trợ từ sau せい]: ～せいに chỉ dùng trong cụm せいにする ('đổ lỗi cho ai'), không dùng làm liên từ chỉ nguyên nhân thay せいで.",
            "[SAI - Sai trợ từ]: Nối mệnh đề nguyên nhân bằng ため dùng ために hoặc ため, không dùng *ためで.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-020-C",
        "grammar_code": "GP-N3-020",
        "drill_type": "contrast",
        "prompt_jp": "外国人が言った冗談が（　　）、自分だけ笑えないのがくやしかった。",
        "options": ["わからないおかげで", "わからないせいで", "理解できないなら", "むずかしそうで"],
        "correct_index": 1,
        "translation_vi": "Tại vì không hiểu câu nói đùa của người nước ngoài nên chỉ mỗi mình tôi không cười được, thật ấm ức.",
        "explanation_vi": "Kết quả đáng tiếc, ấm ức (笑えないのがくやしかった) chốt ngay nguyên nhân tiêu cực わからないせいで (Q#155).",
        "option_diagnostics": [
            "[SAI - Ngược sắc thái với くやしかった]: Không thể nói 'nhờ không hiểu mà ấm ức' bằng おかげで.",
            "[ĐÚNG - Nguyên nhân gây ấm ức せいで]: わからないせいで.",
            "[SAI - Dùng câu điều kiện なら cho trải nghiệm đã qua]: Vế sau là くやしかった (cảm xúc đã xảy ra), không đặt giả thiết điều kiện なら.",
            "[SAI - Sai quan hệ nhân quả]: 'Trông có vẻ khó nên không cười được' không khớp với động cơ học tiếng Anh của vận động viên.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-020-A",
        "grammar_code": "GP-N3-020",
        "drill_type": "application",
        "prompt_jp": "今年の夏は雨が少なかったせいで、野菜の値段が（　　）。",
        "options": ["安くなった", "高くなってしまった", "下がって助かった", "おいしくなった"],
        "correct_index": 1,
        "translation_vi": "Tại vì mùa hè năm nay ít mưa nên giá rau đã tăng cao mất rồi.",
        "explanation_vi": "Vì vế trước dùng せいで (tại vì...), vế sau BẮT BUỘC phải là kết quả XẤU/BẤT LỢI cho người nói -> 高くなってしまった.",
        "option_diagnostics": [
            "[SAI - Kết quả tốt không khớp せいで]: Giá rau rẻ đi là tin vui, không đi với せいで.",
            "[ĐÚNG - Hậu quả bất lợi 高くなってしまった]: Khớp hoàn toàn với せいで.",
            "[SAI - Kết quả đáng mừng]: 助かった (nhẹ nhõm/may quá) trái hẳn ngữ điệu than phiền của せいで.",
            "[SAI - Kết quả tích cực]: Ngon hơn là kết quả tốt, không dùng せいで.",
        ],
    },
    # --- GP-N3-021 (formation + application) ---
    {
        "drill_key": "DR-GP-N3-021-F",
        "grammar_code": "GP-N3-021",
        "drill_type": "formation",
        "prompt_jp": "せっかく自分の努力で入った会社（　　）、簡単に辞めるべきではない。",
        "options": ["のだから", "なのだから", "だから", "なだから"],
        "correct_index": 1,
        "translation_vi": "Vì đây là công ty mà bạn đã mất công nỗ lực mới vào được nên đừng nên nghỉ việc dễ dàng như vậy.",
        "explanation_vi": "Danh từ 会社 nối vào のだから BẮT BUỘC phải đổi だ thành な -> 会社なのだから.",
        "option_diagnostics": [
            "[SAI - Thiếu な sau danh từ]: Trước のだから danh từ không nối bằng だ hay đứng trần mà phải có な (hoặc giữ nguyên 会社なのだから).",
            "[ĐÚNG - N + な + のだから]: Nhấn mạnh sự thật hiển nhiên 会社なのだから.",
            "[SAI - Thiếu の nhấn mạnh]: 会社だから thiếu sắc thái 'vốn dĩ sự thật hiển nhiên mà cả hai đều biết' của なのだから.",
            "[SAI - Sai hình thái]: Không có mẫu *なだから (phải là なのだから).",
        ],
    },
    {
        "drill_key": "DR-GP-N3-021-A",
        "grammar_code": "GP-N3-021",
        "drill_type": "application",
        "prompt_jp": "もう高校生なのだから、自分のことは自分で（　　）。",
        "options": ["しないせいだ", "するべきだ", "したつもりだ", "するわけがない"],
        "correct_index": 1,
        "translation_vi": "Vì đã là học sinh cấp 3 rồi nên việc của bản thân thì tự mình nên làm đi.",
        "explanation_vi": "Mẫu ～のだから nêu sự thật hiển nhiên để khuyên nhủ hoặc nhắc nhở trách nhiệm ở vế sau (～べきだ / ～ほうがいい).",
        "option_diagnostics": [
            "[SAI - Sai cấu trúc]: Không gắn せいだ làm lời khuyên sau なのだから.",
            "[ĐÚNG - Lời khuyên/trách nhiệm べきだ sau なのだから]: 自分でやるべきだ.",
            "[SAI - Sai nghĩa 'cứ đinh ninh']: Không hợp ngữ cảnh khuyên bảo người nghe.",
            "[SAI - Ngược nghĩa]: 'Đã là học sinh cấp 3 thì không đời nào tự làm' là vô lý.",
        ],
    },
    # --- GP-N3-022 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-022-C",
        "grammar_code": "GP-N3-022",
        "drill_type": "contrast",
        "prompt_jp": "時給600円（　　）、応募してくる人はなかなか見つかりませんよ。",
        "options": ["では", "でも", "なら", "こそ"],
        "correct_index": 0,
        "translation_vi": "Lương giờ mà chỉ có 600 yên thế này thì khó mà tìm được người ứng tuyển đâu.",
        "explanation_vi": "Nêu điều kiện tối thiểu/bất lợi khiến kết quả vế sau không thực hiện được ('nếu cứ ở mức 600 yên thì không tìm nổi người') dùng N + では.",
        "option_diagnostics": [
            "[ĐÚNG - N + では + Kết quả bất khả/khó xử]: 時給600円では.",
            "[SAI - Ngược nghĩa nhượng bộ]: 600円でも nghĩa là 'dù có 600 yên đi nữa thì...', không hợp vế sau 'không tìm được người'.",
            "[SAI - Thiếu sắc thái điều kiện bất lợi]: なら thường dùng gợi ý trung tính ('nếu là 600 yên thì...'); với điều kiện thấp gây bất lợi rõ ràng phải dùng では.",
            "[SAI - Sai nghĩa nhấn mạnh]: こそ không đứng làm điều kiện khiến không tìm được người.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-022-A",
        "grammar_code": "GP-N3-022",
        "drill_type": "application",
        "prompt_jp": "そんなに毎日ゲームばかり（　　）、試験に合格できませんよ。",
        "options": ["していては", "していても", "したからには", "したおかげで"],
        "correct_index": 0,
        "translation_vi": "Nếu ngày nào cũng cứ chỉ toàn chơi game như thế thì không đỗ được kỳ thi đâu nhé.",
        "explanation_vi": "Tình trạng đang tiếp diễn ở vế trước nếu không sửa sẽ gây hậu quả xấu (合格できない) -> Vている chia thể て + は -> していては.",
        "option_diagnostics": [
            "[ĐÚNG - Vて + は + Hậu quả xấu]: していては + 合格できない.",
            "[SAI - Ngược nghĩa nhượng bộ]: していても nghĩa là 'dù có chơi game suốt thì vẫn...', mâu thuẫn với 合格できません.",
            "[SAI - Sai nghĩa quyết tâm]: からには nghĩa là 'một khi đã chơi game thì phải...', sai hoàn toàn.",
            "[SAI - Sai sắc thái biết ơn]: Không dùng おかげで cho kết quả trượt thi.",
        ],
    },
    # --- GP-N3-023 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-023-F",
        "grammar_code": "GP-N3-023",
        "drill_type": "formation",
        "prompt_jp": "この仕事は、やる気（　　）経験がなくても応募できます。",
        "options": ["さえあれば", "だけあれば", "ばかりあれば", "こそあれば"],
        "correct_index": 0,
        "translation_vi": "Công việc này chỉ cần có tinh thần quyết tâm là dù không có kinh nghiệm cũng ứng tuyển được.",
        "explanation_vi": "Cấu trúc điều kiện tối thiểu duy nhất 'chỉ cần có N là đủ' bắt buộc là [N + さえ + あれば / Vば] (Q#58).",
        "option_diagnostics": [
            "[ĐÚNG - N + さえ + あれば (Chỉ cần... là đủ)]: やる気さえあれば.",
            "[SAI - Thiếu sắc thái điều kiện tối thiểu]: Chỉ cần điều kiện duy nhất vượt qua mọi rào cản khác dùng さえあれば (không dùng *だけあれば).",
            "[SAI - Sai nghĩa 'chỉ toàn']: ばかり không dùng ghép cặp với あれば để nói điều kiện duy nhất.",
            "[SAI - Sai trợ từ kết hợp điều kiện]: こそ không ghép *こそあれば làm mẫu điều kiện.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-023-C",
        "grammar_code": "GP-N3-023",
        "drill_type": "contrast",
        "prompt_jp": "日常生活では、その国の言葉（　　）できなくても、なんとかなるものだ。",
        "options": ["しか", "さえ", "ばかり", "なんか"],
        "correct_index": 1,
        "translation_vi": "Trong sinh hoạt hằng ngày, ngay cả ngôn ngữ của nước đó mà không biết đi nữa thì rồi cũng xoay xở được thôi.",
        "explanation_vi": "Nhấn mạnh yếu tố cơ bản đến mức tối thiểu ('ngay cả ngôn ngữ') thiếu vắng nhưng vẫn ổn -> dùng trợ từ さえ (Q#154).",
        "option_diagnostics": [
            "[SAI - Đảo ngược nghĩa câu]: しか～できなくても nghĩa là 'dù chỉ làm được mỗi ngôn ngữ thôi', trái ngược hẳn với ý câu.",
            "[ĐÚNG - Nhấn mạnh cực đoan tối thiểu さえ]: 言葉さえできなくても (Q#154).",
            "[SAI - Sai nghĩa 'toàn là']: ばかり không mang nghĩa 'ngay cả đến mức cơ bản cũng không biết'.",
            "[SAI - Sắc thái coi thường không hợp]: なんか mang thái độ chê bai coi nhẹ ngôn ngữ, lệch ý lạc quan của câu.",
        ],
    },
    # --- GP-N3-024 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-024-C",
        "grammar_code": "GP-N3-024",
        "drill_type": "contrast",
        "prompt_jp": "わたしは、（　　）どんなに難しい問題でも必ず答えはあると思う。",
        "options": ["まるで", "たとえ", "おそらく", "決して"],
        "correct_index": 1,
        "translation_vi": "Tôi nghĩ rằng cho dù là vấn đề khó đến mức nào đi nữa thì nhất định cũng có lời giải.",
        "explanation_vi": "Phó từ hô ứng bắt buộc với どんなに～でも (cho dù... đi nữa) là たとえ (Q#23).",
        "option_diagnostics": [
            "[SAI - Sai cặp hô ứng]: まるで hô ứng với ようだ / みたいだ ('cứ như là'), không đi với ～ても/でも.",
            "[ĐÚNG - Cặp hô ứng たとえ～ても/でも]: たとえどんなに難しい問題でも.",
            "[SAI - Sai cặp hô ứng]: おそらく hô ứng với phỏng đoán だろう / に違いない, không mở đầu nhượng bộ どんなに～でも.",
            "[SAI - Sai cặp hô ứng phủ định]: 決して hô ứng với phủ định ない / わけではない, trái với khẳng định 必ずある.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-024-A",
        "grammar_code": "GP-N3-024",
        "drill_type": "application",
        "prompt_jp": "たとえ周りの人に反対（　　）、私は自分の夢をあきらめない。",
        "options": ["されれば", "されても", "されると", "されるなら"],
        "correct_index": 1,
        "translation_vi": "Cho dù có bị những người xung quanh phản đối đi nữa, tôi cũng sẽ không từ bỏ ước mơ của mình.",
        "explanation_vi": "Phó từ たとえ đầu câu đòi hỏi mệnh đề nhượng bộ kết thúc bằng ～ても / ～でも -> bị động される chia されても.",
        "option_diagnostics": [
            "[SAI - Sai dạng điều kiện]: たとえ không kết thúc bằng thể ば (nếu bị phản đối thì...).",
            "[ĐÚNG - Nhượng bộ たとえ～ても]: 反対される -> 反対されても.",
            "[SAI - Sai điều kiện tất yếu]: と không diễn đạt nghĩa nhượng bộ 'cho dù'.",
            "[SAI - Sai điều kiện giả định]: なら không hô ứng với たとえ.",
        ],
    },
    # --- GP-N3-025 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-025-F",
        "grammar_code": "GP-N3-025",
        "drill_type": "formation",
        "prompt_jp": "市の広報誌（　　）、来月からごみの分別ルールが変わるそうだ。",
        "options": ["によると", "によればに", "にとって", "について"],
        "correct_index": 0,
        "translation_vi": "Theo bản tin của thành phố thì nghe nói từ tháng sau quy định phân loại rác sẽ thay đổi.",
        "explanation_vi": "Trích nguồn thông tin báo/tạp chí/thông báo chính thức kết hợp đuôi nghe nói そうだ dùng N + によると / によれば (không thêm に).",
        "option_diagnostics": [
            "[ĐÚNG - N(nguồn tin) + によると]: Hô ứng với そうだ ở cuối câu.",
            "[SAI - Thừa trợ từ に]: Chỉ dùng によれば hoặc によると, không tồn tại *によればに.",
            "[SAI - Nhầm lập trường đánh giá]: にとって không dẫn nguồn tin nghe nói với そうだ.",
            "[SAI - Nhầm chủ đề bàn luận]: について là 'nói về bản tin', sai vai trò dẫn nguồn từ bản tin.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-025-C",
        "grammar_code": "GP-N3-025",
        "drill_type": "contrast",
        "prompt_jp": "どちらも静かな部屋ですが、日当たりの良さ（　　）南向きの部屋のほうがおすすめです。",
        "options": ["によれば", "からいうと", "によると", "にとって"],
        "correct_index": 1,
        "translation_vi": "Cả hai đều là phòng yên tĩnh, nhưng xét về độ đón nắng tốt thì căn phòng hướng nam đáng gợi ý hơn.",
        "explanation_vi": "Cuối câu đưa ra gợi ý/đánh giá chủ quan (おすすめです), không phải tin nghe nói lại từ báo đài -> chọn tiêu chí からいうと (loại によれば / によると).",
        "option_diagnostics": [
            "[SAI - Nhầm nguồn tin nghe nói]: 'Độ đón nắng' (日当たりの良さ) là tiêu chí đánh giá chứ không phải nguồn tin biết nói.",
            "[ĐÚNG - Tiêu chí đánh giá からいうと]: Xét về mặt đón nắng thì chọn phòng hướng nam.",
            "[SAI - Nhầm nguồn tin]: によると đòi hỏi nguồn tin và đuôi truyền đạt そうだ/ということだ, không đi với おすすめです.",
            "[SAI - Sai chủ thể lập trường]: にとって chỉ gắn sau chủ thể người/tập thể, không gắn sau tiêu chí vật lý 日当たりの良さ.",
        ],
    },
    # --- GP-N3-026 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-026-C",
        "grammar_code": "GP-N3-026",
        "drill_type": "contrast",
        "prompt_jp": "日本では昔から、月にウサギが住んでいる（　　）。",
        "options": ["と言っている", "と言われている", "と言うべきだ", "と決めている"],
        "correct_index": 1,
        "translation_vi": "Ở Nhật Bản từ xưa người ta vẫn nói rằng trên mặt trăng có thỏ sinh sống.",
        "explanation_vi": "Truyền thuyết dân gian hay quan niệm phổ biến lâu đời không gắn với một cá nhân cụ thể phải dùng Thể bị động tiếp diễn と言われている.",
        "option_diagnostics": [
            "[SAI - Thiếu chủ thể cá nhân]: と言っている cần chủ ngữ cụ thể ai đó đang nói, không dùng cho truyền thuyết chung '昔から ở Nhật'.",
            "[ĐÚNG - Dư luận/Quan niệm xã hội と言われている]: Dùng bị động tiếp diễn cho nhận thức phổ biến.",
            "[SAI - Sai ngữ dụng khuyên bảo]: 'Nên nói rằng trên trăng có thỏ' sai ý hoàn toàn.",
            "[SAI - Sai chủ ý cá nhân]: 決めている là tự quyết định, không dùng cho truyền thuyết dân gian.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-026-A",
        "grammar_code": "GP-N3-026",
        "drill_type": "application",
        "prompt_jp": "秋は空気が澄んでいて、読書をするのにとてもいい季節（　　）。",
        "options": ["だと言われている", "と言うことだ", "と言うのは", "と言うところだ"],
        "correct_index": 0,
        "translation_vi": "Người ta vẫn nói rằng mùa thu không khí trong lành, là mùa rất thích hợp cho việc đọc sách.",
        "explanation_vi": "Đánh giá nhận định chung được nhiều người công nhận từ trước đến nay nối bằng 普通形 + と言われている (với danh từ 季節 giữ だ -> 季節だと言われている).",
        "option_diagnostics": [
            "[ĐÚNG - 普通形 + と言われている]: いい季節だ + と言われている.",
            "[SAI - Thiếu mạch ngữ cảnh trích nguồn tin mới]: ということだ thiên về truyền đạt tin tức vừa nghe/đọc được chứ không hợp nhận định văn hóa chung như と言われている.",
            "[SAI - Không kết thúc câu bằng というのは]: というのは đứng giữa câu để mở đầu phần định nghĩa.",
            "[SAI - Sai mẫu thời điểm]: ところだ đi với động từ để chỉ thời điểm sắp/đang/vừa mới.",
        ],
    },
    # --- GP-N3-027 (formation + application) ---
    {
        "drill_key": "DR-GP-N3-027-F",
        "grammar_code": "GP-N3-027",
        "drill_type": "formation",
        "prompt_jp": "噂では、駅前に新しくできたレストランはすごく（　　）とか。",
        "options": ["おいしいだ", "おいしい", "おいしく", "おいしいな"],
        "correct_index": 1,
        "translation_vi": "Nghe đồn đâu nhà hàng mới mở trước nhà ga ngon lắm thì phải.",
        "explanation_vi": "Trước ～とか (nghe phong phanh đâu là...) tính từ đuôi い giữ nguyên thể từ điển (không thêm だ hay な) -> おいしいとか.",
        "option_diagnostics": [
            "[SAI - Thừa だ sau tính từ đuôi い]: Tính từ đuôi い tuyệt đối không gắn だ (*おいしいだ).",
            "[ĐÚNG - Aい + とか]: Truyền đạt tin đồn trong hội thoại.",
            "[SAI - Sai dạng phó từ く]: Không gắn とか sau dạng chia phó từ く.",
            "[SAI - Nhầm sang tính từ đuôi な]: おいしい là tính từ đuôi い, không thêm な.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-027-A",
        "grammar_code": "GP-N3-027",
        "drill_type": "application",
        "prompt_jp": "休みになると、いつも友達と買い物に行く（　　）、カフェで話したりしている。",
        "options": ["とか", "だけ", "ばかり", "ほど"],
        "correct_index": 0,
        "translation_vi": "Hễ đến ngày nghỉ là tôi lại làm những việc như đi mua sắm cùng bạn bè hay trò chuyện ở quán cà phê.",
        "explanation_vi": "Liệt kê các hành động ví dụ nhẹ nhàng trong khẩu ngữ nối với たり hoặc lặp lại dùng とか (tương đương たり).",
        "option_diagnostics": [
            "[ĐÚNG - Liệt kê ví dụ khẩu ngữ とか]: 買い物に行くとか、カフェで話したりしている.",
            "[SAI - Sai nghĩa giới hạn]: だけ không dùng để liệt kê ví dụ song hành cùng たり.",
            "[SAI - Sai ngữ pháp với mệnh đề tiếp theo]: ばかり nối câu liệt kê hành động đa dạng hai vế sẽ mâu thuẫn với 'chỉ toàn đi mua sắm'.",
            "[SAI - Sai nghĩa mức độ]: ほど chỉ mức độ so sánh, không liệt kê hoạt động ngày nghỉ.",
        ],
    },
    # --- GP-N3-028 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-028-F",
        "grammar_code": "GP-N3-028",
        "drill_type": "formation",
        "prompt_jp": "友達から、今乗っている電車が途中で（　　）というメールが来た。",
        "options": ["止まって", "止まっている", "止まります", "止まろう"],
        "correct_index": 1,
        "translation_vi": "Tôi nhận được email từ bạn báo rằng chuyến tàu bạn ấy đang đi bị dừng giữa đường.",
        "explanation_vi": "Trước ～という + Danh từ (メール) BẮT BUỘC dùng thể thông thường (普通形), không dùng thể lịch sự ます hay thể て.",
        "option_diagnostics": [
            "[SAI - Thể て không đứng trước という]: Không viết *止まってというメール.",
            "[ĐÚNG - 普通形 + という + メール]: 止まっているというメール.",
            "[SAI - Dùng thể lịch sự ます trước という]: Mệnh đề định danh nội dung dùng thể thông thường, không dùng *止まりますという.",
            "[SAI - Sai thể ý chí]: 止まろう không phù hợp trạng thái tàu đang bị dừng ngoài ý muốn.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-028-C",
        "grammar_code": "GP-N3-028",
        "drill_type": "contrast",
        "prompt_jp": "その手紙は、先日の見舞いの花が（　　）というお詫びの内容だった。",
        "options": ["失礼だった", "失礼だの", "失礼な", "失礼に"],
        "correct_index": 0,
        "translation_vi": "Bức thư đó có nội dung xin lỗi rằng bó hoa thăm bệnh hôm trước thật thất lễ.",
        "explanation_vi": "Trước という (nội dung sự việc đã xảy ra), tính từ đuôi な (失礼) chia quá khứ thông thường -> 失礼だったという.",
        "option_diagnostics": [
            "[ĐÚNG - Aな quá khứ だった + という]: Đúng thì quá khứ của sự việc đã xảy ra hôm trước.",
            "[SAI - Lỗi ghép *だの]: Không chèn の vào sau だ.",
            "[SAI - Sai hình thái bổ nghĩa trực tiếp]: 失礼な chỉ đứng trước danh từ, không nối thẳng vào という (*失礼なという).",
            "[SAI - Dùng phó từ に trước という]: Không dùng phó từ に trực tiếp trước という.",
        ],
    },
    # --- GP-N3-029 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-029-C",
        "grammar_code": "GP-N3-029",
        "drill_type": "contrast",
        "prompt_jp": "「彼、大阪で10年も暮らしていたんだって。」「なるほど、だから関西弁が（　　）。」",
        "options": ["上手なわけだ", "上手なわけではない", "上手なわけがない", "上手になるわけにはいかない"],
        "correct_index": 0,
        "translation_vi": "'Nghe bảo anh ấy sống ở Osaka tận 10 năm đấy.' — 'À ra thế, thảo nào anh ấy nói tiếng Kansai giỏi vậy.'",
        "explanation_vi": "Thấy なるほど / だから thể hiện sự vỡ lẽ hợp lý khi hiểu ra nguyên nhân -> dùng Aな + な + わけだ.",
        "option_diagnostics": [
            "[ĐÚNG - Vỡ lẽ nguyên nhân logic Aな+な+わけだ]: Thảo nào nói tiếng Kansai giỏi thế.",
            "[SAI - Ngược nghĩa phủ định một phần]: わけではない nghĩa là 'không hẳn là giỏi', mâu thuẫn với なるほど、だから.",
            "[SAI - Ngược nghĩa phủ định 100%]: わけがない nghĩa là 'làm sao mà giỏi được', trái logic.",
            "[SAI - Sai ngữ dụng đạo lý]: わけにはいかない nghĩa là 'không thể trở nên giỏi được vì quy tắc cấm'.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-029-A",
        "grammar_code": "GP-N3-029",
        "drill_type": "application",
        "prompt_jp": "ここから大阪まで車で片道3時間か。往復すると6時間は（　　）。",
        "options": ["かかるわけだ", "かかるわけではない", "かかるべきではない", "かからないわけがない"],
        "correct_index": 0,
        "translation_vi": "Từ đây tới Osaka một chiều mất 3 tiếng ô tô à. Vậy đi khứ hồi tính ra mất hẳn 6 tiếng đấy.",
        "explanation_vi": "Suy ra kết quả tính toán tất yếu từ dữ kiện vừa nêu (3 x 2 = 6 tiếng) dùng Vる + わけだ.",
        "option_diagnostics": [
            "[ĐÚNG - Suy luận tất yếu từ dữ kiện わけだ]: Vる (かかる) + わけだ.",
            "[SAI - Phủ định sai logic toán học]: わけではない ('không hẳn mất 6 tiếng') sai ngữ cảnh cộng nhân đơn giản.",
            "[SAI - Sai sắc thái khuyên răn]: べきではない là lời khuyên đạo lý, không dùng để tính thời gian đi đường.",
            "[SAI - Phủ định kép lủng củng không tự nhiên]: Dù về toán có nghĩa gần, ở ngữ cảnh vỡ lẽ tự nhiên phải dùng khẳng định かかるわけだ.",
        ],
    },
    # --- GP-N3-030 (formation + application) ---
    {
        "drill_key": "DR-GP-N3-030-F",
        "grammar_code": "GP-N3-030",
        "drill_type": "formation",
        "prompt_jp": "値段が高いレストランが、いつも美味しい（　　）。",
        "options": ["とは限らない", "に限る", "にすぎない", "わけがない"],
        "correct_index": 0,
        "translation_vi": "Nhà hàng giá đắt chưa chắc lúc nào cũng ngon.",
        "explanation_vi": "Phản bác nhận định tuyệt đối (đứng với いつも) để nêu vẫn có ngoại lệ dùng [普通形 + とは限らない].",
        "option_diagnostics": [
            "[ĐÚNG - Phủ định tuyệt đối とは限らない]: Đứng cùng いつも để chỉ vẫn có trường hợp ngoại lệ.",
            "[SAI - Ngược nghĩa hoàn toàn]: に限る nghĩa là 'cứ phải nhà hàng đắt mới ngon nhất'.",
            "[SAI - Sai nghĩa và cấu trúc]: にすぎない là 'chẳng qua chỉ là ngon', sai ý.",
            "[SAI - Phủ định cực đoan 100%]: わけがない nghĩa là 'nhà hàng đắt tuyệt đối không thể nào ngon', sai thực tế.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-030-A",
        "grammar_code": "GP-N3-030",
        "drill_type": "application",
        "prompt_jp": "漢字をたくさん知っているからといって、難しい本が読める（　　）。",
        "options": ["とは限らない", "はずがない", "に決まっている", "ばかりだ"],
        "correct_index": 0,
        "translation_vi": "Không phải cứ biết nhiều chữ Hán là nhất định đọc được sách khó đâu.",
        "explanation_vi": "Cặp hô ứng kinh điển [～からといって ～とは限らない] = 'không phải hễ cứ A là chắc chắn B'.",
        "option_diagnostics": [
            "[ĐÚNG - Cặp hô ứng からといって ～とは限らない]: Biết Kanji nhiều vẫn có thể không đọc hiểu hết sách khó.",
            "[SAI - Quá cực đoan 100%]: はずがない khẳng định người biết nhiều Kanji 'tuyệt đối không thể nào đọc nổi sách khó'.",
            "[SAI - Khẳng định ngược mạch からといって]: からといって luôn đi với phủ định một phần ở cuối câu, không đi với に決まっている.",
            "[SAI - Sai ngữ pháp và nghĩa]: ばかりだ không hô ứng với からといって.",
        ],
    },
    # --- GP-N3-031 (formation + contrast + application) ---
    {
        "drill_key": "DR-GP-N3-031-F",
        "grammar_code": "GP-N3-031",
        "drill_type": "formation",
        "prompt_jp": "私は甘いものが（　　）わけではないが、健康のために控えている。",
        "options": ["嫌い", "嫌いな", "嫌いだ", "嫌いの"],
        "correct_index": 1,
        "translation_vi": "Không hẳn là tôi ghét đồ ngọt, nhưng vì sức khỏe nên tôi đang kiêng bớt.",
        "explanation_vi": "嫌い là tính từ đuôi な, nên đứng trước わけではない BẮT BUỘC phải thêm な (hoặc である) -> 嫌いなわけではない.",
        "option_diagnostics": [
            "[SAI - Thiếu な sau tính từ đuôi な]: Không nối trực tiếp *嫌いわけではない.",
            "[ĐÚNG - Aな + な + わけではない]: 嫌いなわけではない.",
            "[SAI - Dùng だ trước わけ]: Tiếng Nhật không nói *嫌いだわけではない; phải đổi だ -> な hoặc である.",
            "[SAI - Nhầm Aな với Danh từ]: 嫌い là tính từ đuôi な nên dùng な, không dùng の.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-031-C",
        "grammar_code": "GP-N3-031",
        "drill_type": "contrast",
        "prompt_jp": "世界中の人がみんな月の模様をウサギにたとえている（　　）。",
        "options": ["わけにはいきません", "わけではありません", "わけがありません", "わけです"],
        "correct_index": 1,
        "translation_vi": "Không phải tất cả mọi người trên thế giới đều ví hoa văn trên mặt trăng với con thỏ.",
        "explanation_vi": "Phủ định một phần cho từ chỉ toàn thể 'みんな' (một số nước ví với cua hoặc lừa) dùng わけではありません (Q#63).",
        "option_diagnostics": [
            "[SAI - Nhầm với cấm cản đạo lý]: わけにはいきません nghĩa là 'không thể ví được vì đạo lý cấm cản', sai hoàn toàn ngữ cảnh văn hóa đa dạng.",
            "[ĐÚNG - Phủ định một phần わけではありません]: みんな...わけではありません (Q#63).",
            "[SAI - Phủ định sạch trơn 100%]: わけがありません nghĩa là 'không đời nào có chuyện ai ví với thỏ', sai vì ngay ở Nhật người ta đã ví với thỏ.",
            "[SAI - Khẳng định toàn phần trái sự thật]: わけです trái với câu sau liệt kê Nam Âu ví với cua, Nam Mỹ ví với lừa.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-031-A",
        "grammar_code": "GP-N3-031",
        "drill_type": "application",
        "prompt_jp": "女性の平均身長からすると、彼女の背は（　　）低いわけではない。",
        "options": ["決して", "もし", "必ず", "おそらく"],
        "correct_index": 0,
        "translation_vi": "Xét theo chiều cao trung bình của phụ nữ thì chiều cao của cô ấy hoàn toàn không phải là thấp.",
        "explanation_vi": "Phó từ tăng cường hô ứng với phủ định ～わけではない là 決して ('hoàn toàn không hẳn là...') (Q#59).",
        "option_diagnostics": [
            "[ĐÚNG - Cặp hô ứng 決して ～ わけではない]: Tăng cường phủ định một cách chắc chắn.",
            "[SAI - Mở đầu điều kiện]: もし dùng cho câu điều kiện たら/ば, không đi với わけではない.",
            "[SAI - Phủ định cặp với 必ず]: 必ず～わけではない chỉ dùng khi nói 'không hẳn lúc nào cũng chắc chắn', không hợp cụm mô tả chiều cao 1 người cụ thể như 決して.",
            "[SAI - Phó từ phỏng đoán]: おそらく đi với だろう / に違いない, không ghép với わけではない.",
        ],
    },
    # --- GP-N3-032 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-032-C",
        "grammar_code": "GP-N3-032",
        "drill_type": "contrast",
        "prompt_jp": "今日は大切なプレゼンがあるので、少し熱があっても仕事を（　　）。",
        "options": ["休むわけではない", "休むわけにはいかない", "休むわけがない", "休むことはない"],
        "correct_index": 1,
        "translation_vi": "Hôm nay có buổi thuyết trình quan trọng nên dù hơi sốt cũng không thể nghỉ làm được.",
        "explanation_vi": "Vì trách nhiệm/nghĩa vụ công việc cản trở dù sức khỏe không tốt muốn nghỉ -> Vる + わけにはいかない.",
        "option_diagnostics": [
            "[SAI - Nhầm sang phủ định một phần]: 休むわけではない nghĩa là 'không phải là tôi định nghỉ đâu', thiếu sắc thái không thể nghỉ vì trách nhiệm.",
            "[ĐÚNG - Ràng buộc trách nhiệm わけにはいかない]: Vる (休む) + わけにはいかない.",
            "[SAI - Nhầm sang phỏng đoán phủ định]: 休むわけがない nghĩa là 'làm sao có chuyện nghỉ', lệch hẳn tâm trạng cố gắng chịu đựng.",
            "[SAI - Nhầm nghĩa không cần thiết]: 休むことはない nghĩa là 'không cần thiết phải nghỉ đâu' (khuyên người khác), sai chủ thể chịu áp lực.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-032-A",
        "grammar_code": "GP-N3-032",
        "drill_type": "application",
        "prompt_jp": "友だちから「絶対に秘密にしてね」と言われたので、誰にも（　　）。",
        "options": ["話すわけにはいかない", "話さないわけにはいかない", "話すわけではない", "話さないことはない"],
        "correct_index": 0,
        "translation_vi": "Vì bạn đã dặn 'nhất định giữ bí mật nhé' nên tôi không thể nói cho ai biết được.",
        "explanation_vi": "Lời hứa giữ bí mật (lương tâm/lễ nghĩa) không cho phép nói ra -> Vる + わけにはいかない.",
        "option_diagnostics": [
            "[ĐÚNG - Giữ lời hứa nên không thể làm V]: 話す + わけにはいかない.",
            "[SAI - Ngược nghĩa thành 'buộc phải nói']: Vない + わけにはいかない nghĩa là 'không thể không nói -> phải nói ra', phản bội lời hứa.",
            "[SAI - Nhầm nghĩa]: 話すわけではない là 'không hẳn là tôi sẽ nói'.",
            "[SAI - Sai nghĩa 'không phải không nói']: 話さないことはない nghĩa là 'cũng có thể nói', sai lời hứa.",
        ],
    },
    # --- GP-N3-033 (formation + application) ---
    {
        "drill_key": "DR-GP-N3-033-F",
        "grammar_code": "GP-N3-033",
        "drill_type": "formation",
        "prompt_jp": "上司に頼まれた仕事なので、どんなに忙しくても（　　）わけにはいかない。",
        "options": ["引き受ける", "引き受けない", "引き受けた", "引き受けて"],
        "correct_index": 1,
        "translation_vi": "Vì là công việc sếp nhờ vả nên dù bận thế nào tôi cũng không thể không nhận (buộc phải nhận).",
        "explanation_vi": "Diễn đạt 'buộc phải làm / không thể từ chối' dùng phủ định kép: [Vない + わけにはいかない] -> 引き受けないわけにはいかない.",
        "option_diagnostics": [
            "[SAI - Ngược nghĩa thành 'không thể nhận']: 引き受けるわけにはいかない nghĩa là 'không được phép nhận việc của sếp', trái ngược hoàn toàn logic.",
            "[ĐÚNG - Phủ định kép Vない + わけにはいかない]: 不 nhận không được = buộc phải nhận.",
            "[SAI - Sai thì trước わけにはいかない]: Không chia quá khứ Vた trước わけにはいかない.",
            "[SAI - Sai dạng thể て]: Thể て không gắn vào わけにはいかない.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-033-A",
        "grammar_code": "GP-N3-033",
        "drill_type": "application",
        "prompt_jp": "もうすぐ卒業式なので、スピーチの練習を（　　）。",
        "options": ["するわけにはいかない", "しないわけにはいかない", "するわけがない", "したわけではない"],
        "correct_index": 1,
        "translation_vi": "Sắp đến lễ tốt nghiệp rồi nên tôi không thể không luyện tập bài phát biểu (buộc phải tập).",
        "explanation_vi": "Tình huống buộc phải thực hiện hành động chuẩn bị vì lễ tốt nghiệp cận kề -> Vない + わけにはいかない.",
        "option_diagnostics": [
            "[SAI - Ngược nghĩa]: 'Vì sắp lễ tốt nghiệp nên không được phép tập' là vô lý.",
            "[ĐÚNG - Buộc phải làm Vしないわけにはいかない]: Sắp tới hạn nên phải tập.",
            "[SAI - Sai logic suy đoán]: わけがない nghĩa là 'làm gì có chuyện tập'.",
            "[SAI - Sai thì và nghĩa]: したわけではない là 'không hẳn là đã tập'.",
        ],
    },
    # --- GP-N3-034 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-034-C",
        "grammar_code": "GP-N3-034",
        "drill_type": "contrast",
        "prompt_jp": "ここから駅まで歩いて（　　）、30分以上かかるのでバスに乗ろう。",
        "options": ["行けることはない", "行けないことはないが", "行くわけではないが", "行かないわけにはいかない"],
        "correct_index": 1,
        "translation_vi": "Từ đây đi bộ ra ga không phải là không đi được, nhưng vì mất hơn 30 phút nên đi xe buýt thôi.",
        "explanation_vi": "Khẳng định dè dặt khả năng ('cũng đi được đấy nhưng hơi bất tiện') dùng [V(khả năng)ない + ことはない + が].",
        "option_diagnostics": [
            "[SAI - Dùng Vる+ことはない sai nghĩa]: 行けることはない nghĩa là 'không cần thiết phải đi được', vô nghĩa.",
            "[ĐÚNG - Phủ định kép dè dặt Vない+ことはないが]: Cũng đi bộ được đấy nhưng hơi xa.",
            "[SAI - Sai nghĩa 'không hẳn là đi']: 行くわけではないが không diễn tả năng lực có thể đi bộ hay không.",
            "[SAI - Ngược kết luận đi xe buýt]: 行かないわけにはいかない nghĩa là 'buộc phải đi bộ', mâu thuẫn với vế sau バスに乗ろう.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-034-A",
        "grammar_code": "GP-N3-034",
        "drill_type": "application",
        "prompt_jp": "この問題、時間はかかるけれど、自分一人で（　　）ことはない。",
        "options": ["解く", "解ける", "解けない", "解いた"],
        "correct_index": 2,
        "translation_vi": "Bài toán này tuy tốn thời gian nhưng không phải là một mình không giải nổi.",
        "explanation_vi": "Để tạo phủ định kép 'không phải là không giải được' với ことはない ở cuối, động từ trước đó phải chia sang Khả năng phủ định (解けない).",
        "option_diagnostics": [
            "[SAI - Chuyển thành nghĩa 'không cần thiết']: 解くことはない nghĩa là 'không cần phải giải'.",
            "[SAI - Sai hình thái khả năng khẳng định]: Không dùng *解けることはない.",
            "[ĐÚNG - Khả năng phủ định + ことはない]: 解けないことはない = vẫn giải được.",
            "[SAI - Sai thì quá khứ]: Không dùng quá khứ Vた ở đây.",
        ],
    },
    # --- GP-N3-035 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-035-F",
        "grammar_code": "GP-N3-035",
        "drill_type": "formation",
        "prompt_jp": "その映画は見た（　　）見たが、難しくてストーリーがよくわからなかった。",
        "options": ["ことは", "ことを", "のが", "ものは"],
        "correct_index": 0,
        "translation_vi": "Bộ phim đó thì xem cũng có xem đấy, nhưng khó quá nên tôi chẳng hiểu rõ cốt truyện.",
        "explanation_vi": "Cấu trúc lặp thừa nhận một phần [V + ことは + V + が] dùng trợ từ chủ đề ことは.",
        "option_diagnostics": [
            "[ĐÚNG - Mẫu lặp thừa nhận VことはVが]: 見たことは見たが.",
            "[SAI - Sai trợ từ を]: Không dùng *見たことを見たが.",
            "[SAI - Sai danh từ hóa の]: Cấu trúc lặp cố định dùng ことは chứ không dùng のが.",
            "[SAI - Sai danh từ もの]: もの chỉ vật, không dùng trong mẫu lặp động từ thừa nhận hành động.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-035-C",
        "grammar_code": "GP-N3-035",
        "drill_type": "contrast",
        "prompt_jp": "このパソコンは（　　）、重くて持ち運びには向いていない。",
        "options": ["高いことは高いが", "安いことは安いが", "安ければ安いほど", "安いだけあって"],
        "correct_index": 1,
        "translation_vi": "Chiếc laptop này rẻ thì có rẻ đấy, nhưng nặng quá nên không hợp để mang theo bên mình.",
        "explanation_vi": "Thừa nhận một ưu điểm (giá rẻ) rồi nêu nhược điểm đối lập (nặng) bằng cấu trúc [AことはAが] -> 安いことは安いが.",
        "option_diagnostics": [
            "[SAI - Ngược logic ưu-nhược]: Vế sau chê nặng (nhược điểm) nên vế thừa nhận ưu điểm phải là giá rẻ, không phải giá đắt.",
            "[ĐÚNG - Thừa nhận ưu điểm rồi chuyển nhược điểm]: 安いことは安いが.",
            "[SAI - Sai cấu trúc tỷ lệ thuận]: ば～ほど cần hai vế cùng biến đổi, không hợp nối ý nhược điểm bằng が.",
            "[SAI - Ngược đánh giá だけあって]: だけあって khen tương xứng ('đúng như giá rẻ nên tốt'), mâu thuẫn với chê nặng.",
        ],
    },
    # --- GP-N3-036 (formation + contrast + application) ---
    {
        "drill_key": "DR-GP-N3-036-F",
        "grammar_code": "GP-N3-036",
        "drill_type": "formation",
        "prompt_jp": "A「この小説、面白かったですよ。」B「じゃ、私にもぜひ（　　）ほしいです。」",
        "options": ["読んで", "読まれて", "読ませて", "読めて"],
        "correct_index": 2,
        "translation_vi": "A: 'Cuốn tiểu thuyết này hay lắm đấy.' — B: 'Vậy thì tôi cũng nhất định muốn được phép đọc với (cho tôi đọc với).'",
        "explanation_vi": "Người nói B muốn A cho phép chính B ('私にも') làm hành động 読む -> chia Thể sai khiến 読ませる thành 読ませて + ほしい (Q#17).",
        "option_diagnostics": [
            "[SAI - Nhầm chủ thể đọc sách]: 読んでほしい là B muốn A ngồi đọc cho B nghe, trái với việc B muốn tự mượn đọc.",
            "[SAI - Nhầm thể bị động]: 読まれてほしい là thể bị động, sai ngữ nghĩa xin phép.",
            "[ĐÚNG - Sai khiến thể て + ほしい]: 読む -> 読ませる -> 読ませてほしい.",
            "[SAI - Không gắn thể khả năng vào ほしい]: Không tồn tại mẫu *読めてほしい.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-036-C",
        "grammar_code": "GP-N3-036",
        "drill_type": "contrast",
        "prompt_jp": "部長、その新しいプロジェクトはぜひ私に（　　）いただけませんか。",
        "options": ["やって", "やられて", "やらせて", "やりて"],
        "correct_index": 2,
        "translation_vi": "Trưởng phòng ơi, dự án mới đó xin hãy cho phép tôi được đảm nhận làm có được không ạ?",
        "explanation_vi": "Đề nghị lịch sự với cấp trên xin cho phép mình ('私に') thực hiện công việc dùng [V(sai khiến)て + いただけませんか].",
        "option_diagnostics": [
            "[SAI - Nhầm sang nhờ sếp làm]: やっていただけませんか nghĩa là 'nhờ trưởng phòng làm giúp', trái với ngữ cảnh nhận việc về mình (私に).",
            "[SAI - Dùng bị động sai nghĩa]: やられて mang sắc thái bị hại, sai ngữ dụng.",
            "[ĐÚNG - Sai khiến kính trọng xin phép]: やる -> やらせる -> やらせていただけませんか.",
            "[SAI - Sai hình thái chia て]: Nhóm 1 やる chia て là やって, không có *やりて.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-036-A",
        "grammar_code": "GP-N3-036",
        "drill_type": "application",
        "prompt_jp": "大切な用事があるので、今日は少し早退（　　）いただきたいのですが。",
        "options": ["させて", "されて", "して", "できて"],
        "correct_index": 0,
        "translation_vi": "Vì có việc quan trọng nên hôm nay xin phép cho tôi được về sớm một chút ạ.",
        "explanation_vi": "Xin phép nghỉ sớm/về sớm một cách lịch sự dùng 早退する -> sai khiến 早退させる -> 早退させていただきたい.",
        "option_diagnostics": [
            "[ĐÚNG - Sai khiến させる + いただきたい]: Xin phép về sớm lịch sự chuẩn công sở Nhật.",
            "[SAI - Nhầm bị động]: 早退される không phải cách xin phép cho bản thân về sớm.",
            "[SAI - Nhầm người thực hiện]: 早退していただきたい nghĩa là 'tôi muốn sếp về sớm đi', ngược vai vế.",
            "[SAI - Không ghép khả năng + いただきたい]: Không dùng *早退できていただきたい.",
        ],
    },
    # --- GP-N3-037 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-037-C",
        "grammar_code": "GP-N3-037",
        "drill_type": "contrast",
        "prompt_jp": "最近ずっと寝不足みたいですね。一度ゆっくり（　　）。",
        "options": ["休んだらいいのに", "休んだらどうですか", "休むものですか", "休むわけにはいきません"],
        "correct_index": 1,
        "translation_vi": "Dạo này trông bạn có vẻ thiếu ngủ suốt nhỉ. Thử nghỉ ngơi một bữa thật thoải mái xem sao?",
        "explanation_vi": "Đưa ra lời khuyên gợi ý lịch sự cho đối phương thử làm dùng [Vた + ら + どうですか].",
        "option_diagnostics": [
            "[SAI - Ngữ điệu trách móc/tiếc nuối]: 休んだらいいのに mang hàm ý chê trách 'lẽ ra nên nghỉ đi chứ (mà sao không chịu nghỉ)', không lịch sự bằng どうですか.",
            "[ĐÚNG - Gợi ý lịch sự Vたらどうですか]: 休んだらどうですか.",
            "[SAI - Phản bác mạnh]: 休むものですか nghĩa là 'làm gì có chuyện nghỉ được'.",
            "[SAI - Tự ràng buộc]: わけにはいきません không dùng để gợi ý cho người đối diện.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-037-A",
        "grammar_code": "GP-N3-037",
        "drill_type": "application",
        "prompt_jp": "家の前にもっと大きな公園が（　　）いいのに、と思うことがある。",
        "options": ["ある", "あったら", "あればのに", "あって"],
        "correct_index": 1,
        "translation_vi": "Thỉnh thoảng tôi nghĩ ước gì trước nhà có một công viên lớn hơn thì hay biết mấy.",
        "explanation_vi": "Bày tỏ điều ước cho hiện thực chưa có dùng [Vた + ら + いいのに] -> あったらいいのに.",
        "option_diagnostics": [
            "[SAI - Thiếu điều kiện ら]: Không nối trực tiếp *あるいいのに.",
            "[ĐÚNG - Vたら + いいのに]: あったらいいのに = ước gì có thì tốt.",
            "[SAI - Lỗi ghép trực tiếp ば + のに]: Trước いいのに dùng たら hoặc ば + いいのに (phải là あればいいのに, không có *あればのに).",
            "[SAI - Thể て sai cấu trúc]: Không viết *あっていいのに.",
        ],
    },
    # --- GP-N3-038 (formation + application) ---
    {
        "drill_key": "DR-GP-N3-038-F",
        "grammar_code": "GP-N3-038",
        "drill_type": "formation",
        "prompt_jp": "もし会議に出席できない場合は、19日までに先生に（　　）伝えてください。",
        "options": ["連絡してと", "連絡するように", "連絡しようと", "連絡するのを"],
        "correct_index": 1,
        "translation_vi": "Nếu trường hợp không thể dự họp, hãy nhắn lại họ liên lạc với thầy trước ngày 19.",
        "explanation_vi": "Tường thuật gián tiếp lời dặn dò/yêu cầu với 伝える dùng [Vる + ように + 伝えてください] (Passage 10).",
        "option_diagnostics": [
            "[SAI - Thiếu dấu trích dẫn trực tiếp đúng quy chuẩn]: Không nối trực tiếp *連絡してと伝えてください mà phải dùng nguyên thể + ように hoặc trích dẫn câu mệnh lệnh 「連絡してください」と.",
            "[ĐÚNG - Tường thuật gián tiếp ように伝える]: 連絡する + ように + 伝えてください.",
            "[SAI - Sai ngữ nghĩa ý chí]: 連絡しようと伝えてください sai mẫu tường thuật mệnh lệnh.",
            "[SAI - Sai mẫu danh từ hóa]: 連絡するのを伝えてください nghe thành 'kể lại sự kiện việc liên lạc', không phải truyền đạt lời nhắn 'hãy liên lạc'.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-038-A",
        "grammar_code": "GP-N3-038",
        "drill_type": "application",
        "prompt_jp": "父は医者から、健康のために毎日お酒を（　　）と言われている。",
        "options": ["飲まない", "飲むな", "飲んで", "飲みなさいな"],
        "correct_index": 1,
        "translation_vi": "Bố tôi bị bác sĩ dặn cấm là vì sức khỏe tuyệt đối đừng uống rượu mỗi ngày.",
        "explanation_vi": "Trích dẫn câu mệnh lệnh cấm trực tiếp trước と + 言う dùng [Vる + な] -> 飲むな.",
        "option_diagnostics": [
            "[SAI - Thiếu chất mệnh lệnh cấm]: 飲まないと言われている chỉ là tường thuật lời nói 'không uống', không phải lời cấm đoán nghiêm khắc của bác sĩ.",
            "[ĐÚNG - Mệnh lệnh cấm trực tiếp Vる + な]: 飲む + な + と言われている.",
            "[SAI - Không phải câu cấm]: 飲んで là thể て thiếu mệnh lệnh hoàn chỉnh.",
            "[SAI - Sai hình thái]: Không gắn な vào sau なさい (*飲みなさいな).",
        ],
    },
    # --- GP-N3-039 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-039-C",
        "grammar_code": "GP-N3-039",
        "drill_type": "contrast",
        "prompt_jp": "「なんとかなる」と考えて心配しすぎないこと。また、楽しい目標を（　　）。",
        "options": ["作ること", "作らないこと", "作ったこと", "作っていること"],
        "correct_index": 0,
        "translation_vi": "Hãy nghĩ 'rồi sẽ ổn thôi' và đừng lo lắng quá mức. Ngoài ra, hãy tạo ra những mục tiêu vui vẻ.",
        "explanation_vi": "Liệt kê chuỗi nguyên tắc/lời khuyên hành động ở cuối câu trong văn viết dùng [Vる / Vない + こと] (Passage 19).",
        "option_diagnostics": [
            "[ĐÚNG - Câu tâm niệm/chỉ dẫn Vる + こと]: Song hành khẳng định với 心配しすぎないこと.",
            "[SAI - Ngược nghĩa]: 'Đừng tạo mục tiêu vui vẻ' trái hoàn toàn thông điệp của đoạn văn.",
            "[SAI - Sai thì quá khứ]: Quy tắc hướng dẫn/tâm niệm không dùng thì quá khứ Vた trước こと.",
            "[SAI - Sai dạng tiếp diễn]: Câu chỉ dẫn quy tắc không dùng Vている + こと.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-039-A",
        "grammar_code": "GP-N3-039",
        "drill_type": "application",
        "prompt_jp": "【試験中の注意】答えを隣の人に聞いたり、見たり（　　）。",
        "options": ["しないこと", "すること", "したこと", "しないわけだ"],
        "correct_index": 0,
        "translation_vi": "[Lưu ý trong lúc thi] Không được hỏi hay nhìn bài của người ngồi bên cạnh.",
        "explanation_vi": "Bảng nội quy phòng thi nêu điều CẤM bằng văn bản ngắn gọn dùng [Vない + こと] -> しないこと.",
        "option_diagnostics": [
            "[ĐÚNG - Quy định cấm văn bản Vない + こと]: 聞いたり、見たりしないこと.",
            "[SAI - Ngược nội quy]: すること nghĩa là bắt buộc thí sinh nhìn bài bạn.",
            "[SAI - Sai thì quá khứ]: Nội quy không chia quá khứ したこと.",
            "[SAI - Sai mẫu]: しないわけだ là suy luận 'thảo nào không làm', không phải quy định.",
        ],
    },
    # --- GP-N3-040 (formation + application) ---
    {
        "drill_key": "DR-GP-N3-040-F",
        "grammar_code": "GP-N3-040",
        "drill_type": "formation",
        "prompt_jp": "マグロを守るためには、まず国際的なルールを（　　）だと思う。",
        "options": ["徹底するべき", "徹底すべき", "徹底したべき", "徹底してべき"],
        "correct_index": 1,
        "translation_vi": "Để bảo vệ cá ngừ, tôi nghĩ trước tiên cần phải thực hiện triệt để quy định quốc tế.",
        "explanation_vi": "Động từ Nhóm 3 する khi kết hợp với べき chuẩn mực thường rút gọn thành すべき (Passage 4: 徹底すべきだと思う; cả 徹底するべき cũng tồn tại nhưng すべき là chuẩn thi JLPT nhất).",
        "option_diagnostics": [
            "[SAI - Dạng chưa rút gọn ít ưu tiên hơn trong đề]: Tuy するべき cũng chấp nhận được ở khẩu ngữ, chuẩn văn viết N3 của する + べき là すべき (và đề thi chọn すべき).",
            "[ĐÚNG - Bất quy tắc する -> すべき]: 徹底する -> 徹底すべきだと思う.",
            "[SAI - Chia quá khứ trước べき]: Tuyệt đối không gắn べき sau Vた (*したべき).",
            "[SAI - Chia thể て trước べき]: Không gắn べき sau thể て (*してべき).",
        ],
    },
    {
        "drill_key": "DR-GP-N3-040-A",
        "grammar_code": "GP-N3-040",
        "drill_type": "application",
        "prompt_jp": "一度友だちと約束したのだから、きちんと（　　）と思う。",
        "options": ["守るべきだ", "守るわけがない", "守らなくてもいい", "守るにすぎない"],
        "correct_index": 0,
        "translation_vi": "Một khi đã hứa với bạn bè rồi thì tôi nghĩ đương nhiên nên giữ lời hứa đàng hoàng.",
        "explanation_vi": "Nói về bổn phận đạo đức hiển nhiên ('đã hứa thì nên giữ lời') dùng Vる + べきだ.",
        "option_diagnostics": [
            "[ĐÚNG - Nghĩa vụ đạo đức Vる + べきだ]: 守るべきだ.",
            "[SAI - Ngược nghĩa]: 'Làm sao có chuyện giữ lời hứa' trái đạo lý và logic.",
            "[SAI - Ngược nghĩa]: 'Không cần giữ lời hứa cũng được' sai hoàn toàn với のだから.",
            "[SAI - Hạ thấp giá trị sai nghĩa]: 'Chỉ là giữ lời thôi mà' không hợp ngữ cảnh.",
        ],
    },
    # --- GP-N3-041 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-041-C",
        "grammar_code": "GP-N3-041",
        "drill_type": "contrast",
        "prompt_jp": "きのうの試験で、自分では正しい答えを（　　）が、実際は間違いだった。",
        "options": ["書くつもりになった", "書いたつもりだった", "書くことになった", "書いたことだった"],
        "correct_index": 1,
        "translation_vi": "Trong bài thi hôm qua, bản thân tôi cứ đinh ninh là đã viết đáp án đúng, nhưng thực tế lại là sai.",
        "explanation_vi": "Niềm tin chủ quan sai lầm về hành động đã làm dùng [Vた + つもりだった] (Q#19).",
        "option_diagnostics": [
            "[SAI - Sai nghĩa dự định]: 書くつもりになった nghĩa là 'đã nảy sinh ý định sẽ viết', không hợp sự thật đã làm bài hôm qua và sai kết quả.",
            "[ĐÚNG - Cứ đinh ninh là đã làm Vた + つもりだった]: Đối lập với 実際は間違いだった (Q#19).",
            "[SAI - Sai nghĩa quyết định khách quan]: 書くことになった nghĩa là 'đã được quyết định sẽ viết'.",
            "[SAI - Sai cấu trúc]: *書いたことだった không diễn tả sự ngộ nhận chủ quan.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-041-A",
        "grammar_code": "GP-N3-041",
        "drill_type": "application",
        "prompt_jp": "祖父は80歳を過ぎているが、自分ではまだまだ（　　）で元気に働いている。",
        "options": ["若い", "若いつもり", "若いわけ", "若いばかり"],
        "correct_index": 1,
        "translation_vi": "Ông tôi đã qua tuổi 80 rồi, nhưng tự bản thân ông vẫn cứ nghĩ mình còn trẻ và làm việc rất khỏe.",
        "explanation_vi": "Tự nhận mình ở trạng thái đó dù thực tế đã cao tuổi dùng [Aい + つもり] (cách nói 'tự thấy mình còn trẻ') với で.",
        "option_diagnostics": [
            "[SAI - Thiếu つもり với で]: *若いで không dùng diễn tả sự tự nhận chủ quan đối lập với tuổi 80.",
            "[ĐÚNG - Aい + つもり + で]: 若いつもりで = tự coi mình vẫn còn trẻ.",
            "[SAI - Sai cấu trúc]: *若いわけで không thể nối thành 'tự thấy mình trẻ' trong câu này.",
            "[SAI - Sai cấu trúc và nghĩa]: *若いばかりで không mang nghĩa chủ quan của つもり.",
        ],
    },
    # --- GP-N3-042 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-042-F",
        "grammar_code": "GP-N3-042",
        "drill_type": "formation",
        "prompt_jp": "自分の子どもを愛している（　　）、悪いことをしたときは厳しく叱るのだ。",
        "options": ["からこそ", "のでこそ", "ためこそ", "だけこそ"],
        "correct_index": 0,
        "translation_vi": "Chính bởi vì yêu thương con mình nên khi con làm điều xấu mới mắng nghiêm khắc.",
        "explanation_vi": "Cấu trúc nhấn mạnh nguyên nhân sâu sắc 'chính bởi vì... nên mới...' cố định là [普通形 + から + こそ] (không dùng *のでこそ).",
        "option_diagnostics": [
            "[ĐÚNG - Cố định からこそ]: Nhấn mạnh nguyên nhân chân chính từ bên trong.",
            "[SAI - Sai kết hợp ので + こそ]: Tiếng Nhật không ghép *のでこそ.",
            "[SAI - Sai hình thái]: Không ghép *ためこそ thay cho からこそ.",
            "[SAI - Sai hình thái]: Không ghép *だけこそ.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-042-C",
        "grammar_code": "GP-N3-042",
        "drill_type": "contrast",
        "prompt_jp": "このような心の余裕や前向きな考え方（　　）が、選手にとって必要なのだろう。",
        "options": ["ほど", "こそ", "だけ", "くらい"],
        "correct_index": 1,
        "translation_vi": "Chính sự thoải mái trong tâm hồn và lối nghĩ tích cực này mới là điều cần thiết cho các vận động viên.",
        "explanation_vi": "Câu kết luận toàn bài đọc nhấn mạnh yếu tố cốt lõi quan trọng nhất dùng [N + こそ + が] (Q#157).",
        "option_diagnostics": [
            "[SAI - Không ghép ほどが ở đây]: ほど dùng chỉ mức độ hoặc so sánh phủ định, không nhấn mạnh chủ ngữ khẳng định cốt lõi của câu kết.",
            "[ĐÚNG - Chủ thể được nhấn mạnh tuyệt đối こそが]: 考え方こそが (Q#157).",
            "[SAI - Làm yếu thông điệp]: だけ chỉ mang nghĩa giới hạn 'chỉ thế thôi', làm giảm lực khẳng định của đoạn kết.",
            "[SAI - Hạ thấp mức độ]: くらい mang nghĩa ước lượng tầm thường 'cỡ đó thôi', ngược ý đề cao.",
        ],
    },
    # --- GP-N3-043 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-043-C",
        "grammar_code": "GP-N3-043",
        "drill_type": "contrast",
        "prompt_jp": "一度（　　）会ったことがあれば、もう友だちだと考える人もいる。",
        "options": ["も", "でも", "さえ", "こそ"],
        "correct_index": 1,
        "translation_vi": "Cũng có người nghĩ rằng dù chỉ từng gặp mặt một lần thôi thì đã là bạn bè rồi.",
        "explanation_vi": "Số từ tối thiểu + điều kiện khẳng định ('dù chỉ 1 lần thôi mà có gặp') dùng Số từ + でも (Q#15).",
        "option_diagnostics": [
            "[SAI - Lỗi đi với điều kiện khẳng định]: 一度も bắt buộc đi với thể phủ định ('chưa từng một lần nào'), không đi với 会ったことがあれば.",
            "[ĐÚNG - Số từ tối thiểu + でも + ば/たら]: 一度でも会ったことがあれば (Q#15).",
            "[SAI - Kém tự nhiên sau 一度 ở khẳng định]: Sau số từ tối thiểu với ば/たら trong câu khẳng định tự nhiên dùng 一度でも.",
            "[SAI - Sai nghĩa]: こそ nhấn mạnh 'chính là 1 lần', không mang nghĩa giả định nhượng bộ 'dù chỉ 1 lần'.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-043-A",
        "grammar_code": "GP-N3-043",
        "drill_type": "application",
        "prompt_jp": "当院では、病院が休みの日（　　）電話で予約を受け付けています。",
        "options": ["でも", "しか", "だけ", "も"],
        "correct_index": 0,
        "translation_vi": "Tại bệnh viện chúng tôi, ngay cả vào ngày nghỉ khám vẫn tiếp nhận đặt lịch qua điện thoại.",
        "explanation_vi": "Nêu ngoại lệ tích cực ngay cả trong trường hợp tưởng như không thể ('ngay cả vào ngày nghỉ cũng vẫn...') dùng N + でも (Passage 22).",
        "option_diagnostics": [
            "[ĐÚNG - Ngoại lệ 'ngay cả N cũng' với でも]: 休みの日でも受付できる.",
            "[SAI - Lỗi thiếu phủ định]: しか bắt buộc đi với phủ định ở cuối câu; ở đây cuối câu là khẳng định 受け付けています.",
            "[SAI - Ngược nghĩa hoàn toàn]: 休みの日だけ nghĩa là 'CHỈ mở đặt lịch vào ngày nghỉ khám thôi'.",
            "[SAI - Thiếu sắc thái ngoại lệ bất ngờ]: Ngày nghỉ vẫn làm là ngoại lệ trái kỳ vọng nên dùng でも chuẩn xác hơn も.",
        ],
    },
    # --- GP-N3-044 (formation + application) ---
    {
        "drill_key": "DR-GP-N3-044-F",
        "grammar_code": "GP-N3-044",
        "drill_type": "formation",
        "prompt_jp": "結婚してから、忙しくて一度（　　）お寺に行っていない。",
        "options": ["でも", "も", "しか", "こそ"],
        "correct_index": 1,
        "translation_vi": "Từ sau khi kết hôn, vì bận rộn nên tôi chưa từng đi chùa lấy một lần nào.",
        "explanation_vi": "Phủ định tuyệt đối với số từ 'một lần' (一度 + ___ + いっていない) dùng 一度も (Passage 16).",
        "option_diagnostics": [
            "[SAI - Sai ngữ nghĩa với phủ định]: 一度でも không dùng trong câu kể phủ định 'chưa từng một lần nào'.",
            "[ĐÚNG - Số 1 + も + Phủ định]: 一度も行っていない = hoàn toàn chưa đi lần nào.",
            "[SAI - Lỗi dịch nghĩa]: 一度しか～ない nghĩa là 'chỉ đi ĐÚNG MỘT LẦN thôi' (có đi 1 lần), trái với nghĩa chưa đi lần nào.",
            "[SAI - Sai trợ từ với phủ định]: Không ghép *一度こそ～行っていない.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-044-A",
        "grammar_code": "GP-N3-044",
        "drill_type": "application",
        "prompt_jp": "彼女は病気で入院していたが、今は元気になり、一日（　　）大学に通っている。",
        "options": ["も休まないで", "でも休んで", "だけ休んで", "しか休まないで"],
        "correct_index": 0,
        "translation_vi": "Cô ấy từng nhập viện vì ốm, nhưng giờ đã khỏe lại và đi học đại học đều đặn không nghỉ một ngày nào.",
        "explanation_vi": "Phủ định trọn vẹn 'không nghỉ lấy một ngày nào' dùng [一日 + も + 休まないで].",
        "option_diagnostics": [
            "[ĐÚNG - Phủ định sạch trơn 一日も休まないで]: Không nghỉ bất kỳ ngày nào.",
            "[SAI - Ngược nghĩa]: 'Dù chỉ 1 ngày cũng nghỉ rồi đi học' là vô nghĩa.",
            "[SAI - Ngược nghĩa]: 'Chỉ nghỉ 1 ngày rồi đi học'.",
            "[SAI - Sai ý câu]: 一日しか休まないで nghĩa là 'chỉ nghỉ có 1 ngày thôi' (tức là vẫn nghỉ 1 ngày), khác với đi học chuyên cần không nghỉ ngày nào.",
        ],
    },
    # --- GP-N3-045 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-045-C",
        "grammar_code": "GP-N3-045",
        "drill_type": "contrast",
        "prompt_jp": "普段あまり連絡しない遠い親戚に（　　）、毎年年賀状を出している。",
        "options": ["まで", "しか", "こそ", "だけ"],
        "correct_index": 0,
        "translation_vi": "Ngay cả tới những người họ hàng xa bình thường ít liên lạc, năm nào tôi cũng gửi thiệp chúc Tết.",
        "explanation_vi": "Mở rộng phạm vi hành động tới cả đối tượng xa xôi ít ngờ tới dùng に + まで.",
        "option_diagnostics": [
            "[ĐÚNG - Mở rộng phạm vi vượt mức まで]: 遠い親戚にまで = tới cả họ hàng xa.",
            "[SAI - Lỗi thiếu phủ định]: Cuối câu là khẳng định 出している nên không dùng しか.",
            "[SAI - Sai nghĩa]: こそ chỉ nhấn mạnh duy nhất đối tượng chính, không mang nghĩa mở rộng ra cả người ít liên lạc.",
            "[SAI - Sai nghĩa giới hạn]: だけに chỉ mang nghĩa 'chỉ gửi riêng cho họ hàng xa', vô lý.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-045-A",
        "grammar_code": "GP-N3-045",
        "drill_type": "application",
        "prompt_jp": "友達と約束したからといって、無理な借金を（　　）お金を貸す必要はない。",
        "options": ["してまで", "してさえ", "したばかりで", "するだけ"],
        "correct_index": 0,
        "translation_vi": "Không phải cứ hứa với bạn là phải đi vay nợ quá sức tới mức đó để cho bạn mượn tiền đâu.",
        "explanation_vi": "Hy sinh/làm điều cực đoan quá mức (đi vay nợ) để làm việc sau (cho vay tiền) dùng [Vて + まで].",
        "option_diagnostics": [
            "[ĐÚNG - Cực đoan quá mức Vて + まで]: 借金をしてまで = làm tới mức phải đi vay nợ.",
            "[SAI - Sai hình thái kết hợp さえ]: Không dùng *してさえ thay cho してまで.",
            "[SAI - Sai nghĩa 'vừa mới']: ばかり chỉ thời gian vừa qua.",
            "[SAI - Sai nghĩa]: するだけ không mang sắc thái cực đoan quá sức.",
        ],
    },
    # --- GP-N3-046 (formation + application) ---
    {
        "drill_key": "DR-GP-N3-046-F",
        "grammar_code": "GP-N3-046",
        "drill_type": "formation",
        "prompt_jp": "回収の対象とする本は、一般の書籍のほか、絵本・雑誌・漫画（　　）です。",
        "options": ["なんか", "など", "ばかり", "しか"],
        "correct_index": 1,
        "translation_vi": "Sách thuộc đối tượng thu gom ngoài sách thông thường còn có sách tranh, tạp chí, truyện tranh v.v...",
        "explanation_vi": "Tờ rơi thông báo chính thức khi liệt kê các ví dụ đại diện bắt buộc dùng từ trung tính/lịch sự など (tuyệt đối không dùng khẩu ngữ coi nhẹ なんか).",
        "option_diagnostics": [
            "[SAI - Sai văn phong và sắc thái]: なんか là khẩu ngữ mang nghĩa xem nhẹ ('mấy thứ tạp nham như...'), cấm dùng trong thông báo lịch sự.",
            "[ĐÚNG - Liệt kê trung tính trong thông báo など]: 絵本・雑誌・漫画などです (Passage 7).",
            "[SAI - Sai nghĩa giới hạn]: ばかり nghĩa là 'toàn là truyện tranh thôi', mâu thuẫn với 一般の書籍のほか.",
            "[SAI - Sai cấu trúc khẳng định]: しか không đi với câu khẳng định です.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-046-A",
        "grammar_code": "GP-N3-046",
        "drill_type": "application",
        "prompt_jp": "「あいさつ（　　）」と軽く考えてはいけない。一言が一生を変えることもある。",
        "options": ["なんて", "などとは", "ばかりは", "だけは"],
        "correct_index": 0,
        "translation_vi": "Không được coi nhẹ kiểu 'chỉ là chào hỏi thôi mà'. Một câu nói cũng có lúc thay đổi cả cuộc đời.",
        "explanation_vi": "Trích dẫn thái độ xem nhẹ điều nhỏ nhặt trong khẩu ngữ/nghị luận dùng N + なんて (Passage 15).",
        "option_diagnostics": [
            "[ĐÚNG - Coi nhẹ điều thường nhật なんて]: 「あいさつなんて」と軽く考える.",
            "[SAI - Sai kết hợp trích dẫn]: *などとは không khớp với cấu trúc cảm thán coi nhẹ nằm trong ngoặc kép 「...」.",
            "[SAI - Sai sắc thái]: ばかりは không thể hiện sự coi thường/xem nhẹ.",
            "[SAI - Sai sắc thái]: だけは nghĩa là 'riêng mỗi việc chào hỏi thôi thì', không hợp giọng điệu coi thường.",
        ],
    },
    # --- GP-N3-047 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-047-C",
        "grammar_code": "GP-N3-047",
        "drill_type": "contrast",
        "prompt_jp": "スピーチのテーマは何でもいいというわけではなく、日本文化（　　）ことだけです。",
        "options": ["について", "に関する", "に対して", "にとって"],
        "correct_index": 1,
        "translation_vi": "Chủ đề bài phát biểu không phải cái gì cũng được, mà chỉ là những nội dung liên quan đến văn hóa Nhật Bản thôi.",
        "explanation_vi": "Đứng trước danh từ こと để bổ nghĩa 'liên quan đến văn hóa Nhật' dùng [N + に関する + N] (Q#26; nếu dùng について thì phải có の thành についての).",
        "option_diagnostics": [
            "[SAI - Thiếu の khi bổ nghĩa danh từ こと]: について không thể đứng trực tiếp trước danh từ こと mà thiếu trợ từ の (*についてこと).",
            "[ĐÚNG - N + に関する + Danh từ]: 日本文化に関すること (Q#26).",
            "[SAI - Sai dạng và nghĩa]: に対して không đứng trực tiếp trước danh từ và mang nghĩa 'đối với/trái lại'.",
            "[SAI - Sai dạng và nghĩa]: にとって không đứng trực tiếp trước danh từ và mang nghĩa lập trường đánh giá.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-047-A",
        "grammar_code": "GP-N3-047",
        "drill_type": "application",
        "prompt_jp": "その新しい問題（　　）、まだ詳しく調べていないのでコメントできません。",
        "options": ["については", "にとっては", "によっては", "にくらべては"],
        "correct_index": 0,
        "translation_vi": "Về vấn đề mới đó thì vì tôi vẫn chưa tìm hiểu kỹ nên không thể bình luận được.",
        "explanation_vi": "Đặt chủ đề mà người nói chưa nắm rõ để bình luận/trả lời (Q#124) dùng N + については.",
        "option_diagnostics": [
            "[ĐÚNG - Nêu chủ đề phát biểu については]: 問題についてはコメントできません.",
            "[SAI - Sai nghĩa lập trường]: 'Đối với vấn đề đó thì tôi không bình luận' sai vai trò ngữ nghĩa (phải là về chủ đề vấn đề đó).",
            "[SAI - Sai nghĩa 'tùy theo vấn đề']: によっては chỉ sự thay đổi tùy thuộc trường hợp, không hợp động từ コメントできません.",
            "[SAI - Sai nghĩa so sánh]: Không hề so sánh với vấn đề nào khác.",
        ],
    },
    # --- GP-N3-048 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-048-F",
        "grammar_code": "GP-N3-048",
        "drill_type": "formation",
        "prompt_jp": "若い人（　　）、知らないお年寄りに声をかけるのは少し緊張する。",
        "options": ["にとって", "によって", "について", "にかけて"],
        "correct_index": 0,
        "translation_vi": "Đối với người trẻ tuổi, việc bắt chuyện với người cao tuổi xa lạ khiến họ hơi căng thẳng một chút.",
        "explanation_vi": "Đứng trên góc nhìn/trải nghiệm tâm lý của chủ thể 若い人 để đánh giá độ khó/cảm xúc (緊張する) dùng N + にとって (Kosei p.7).",
        "option_diagnostics": [
            "[ĐÚNG - Góc nhìn/Lập trường chủ thể にとって]: 若い人にとって + cảm nhận 緊張する.",
            "[SAI - Sai nghĩa tác nhân/tùy theo]: Câu sau chỉ có cảm nhận chung của người trẻ chứ không phải bị động hay sự khác biệt giữa các nhóm.",
            "[SAI - Sai nghĩa chủ đề]: Không phải 'nói về người trẻ thì căng thẳng'.",
            "[SAI - Sai mẫu thời gian/không gian]: にかけて chỉ phạm vi thời gian hoặc địa lý.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-048-C",
        "grammar_code": "GP-N3-048",
        "drill_type": "contrast",
        "prompt_jp": "海の環境が悪化したことは、マグロ（　　）暮らしづらい状況を生んでいる。",
        "options": ["に対して", "にとって", "を通じて", "をこめて"],
        "correct_index": 1,
        "translation_vi": "Việc môi trường biển xấu đi đang tạo ra tình trạng khó sống đối với loài cá ngừ.",
        "explanation_vi": "Đánh giá tính chất 'khó sống' (暮らしづらい) xét từ góc độ sinh tồn của loài cá ngừ -> マグロにとって (Q#32).",
        "option_diagnostics": [
            "[SAI - Nhầm hướng tác động]: に対して hướng hành động từ ngoài vào cá ngừ; còn tính từ đánh giá 暮らしづらい ('khó sống đối với ai') dùng にとって.",
            "[ĐÚNG - Lập trường sinh tồn của đối tượng にとって]: マグロにとって暮らしづらい.",
            "[SAI - Sai nghĩa trung gian]: Không phải 'thông qua cá ngừ'.",
            "[SAI - Sai nghĩa tình cảm]: Không phải 'gửi gắm tấm lòng vào cá ngừ'.",
        ],
    },
    # --- GP-N3-049 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-049-C",
        "grammar_code": "GP-N3-049",
        "drill_type": "contrast",
        "prompt_jp": "古くなった歯ブラシを捨てないで、掃除用具（　　）使うことにした。",
        "options": ["にとって", "として", "によって", "について"],
        "correct_index": 1,
        "translation_vi": "Tôi quyết định không vứt bàn chải đánh răng cũ đi mà dùng nó với vai trò là dụng cụ vệ sinh.",
        "explanation_vi": "Xác định vai trò, công năng sử dụng của danh từ (làm dụng cụ vệ sinh) dùng [N + として] (Q#25).",
        "option_diagnostics": [
            "[SAI - Nhầm sang lập trường đánh giá]: Dụng cụ vệ sinh là vật vô tri không có góc nhìn cảm nhận.",
            "[ĐÚNG - Vai trò / Chức năng sử dụng として]: 掃除用具として使う.",
            "[SAI - Sai nghĩa phương tiện]: によって không mang nghĩa 'sử dụng vật A với tư cách/công dụng là B'.",
            "[SAI - Sai nghĩa chủ đề]: Không phải dùng bàn chải 'về chủ đề dụng cụ vệ sinh'.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-049-A",
        "grammar_code": "GP-N3-049",
        "drill_type": "application",
        "prompt_jp": "自分の好きな音楽を楽しむの（　　）、あまり大きな音で聞くのは危険だ。",
        "options": ["はいいとしても", "としていいが", "にとっては", "によっても"],
        "correct_index": 0,
        "translation_vi": "Dù việc thưởng thức âm nhạc mình thích là tốt đi nữa, nhưng nghe với âm lượng quá lớn thì nguy hiểm.",
        "explanation_vi": "Công nhận vế trước hợp lý nhưng chuyển sang cảnh báo hạn chế ở vế sau dùng [Aい + としても] (Passage 3).",
        "option_diagnostics": [
            "[ĐÚNG - Nhượng bộ công nhận một phần としても]: いいとしても = dù có tốt đi nữa.",
            "[SAI - Sai trật tự và thiếu trợ từ]: *としていいが không phải cấu trúc nhượng bộ.",
            "[SAI - Sai hoàn toàn cấu trúc]: 楽しむのにとっては sai ngữ pháp vì にとって chỉ đi sau danh từ người/tổ chức.",
            "[SAI - Sai ngữ pháp]: *によっても không gắn sau động từ nguyên thể 楽しむの.",
        ],
    },
    # --- GP-N3-050 (formation + application) ---
    {
        "drill_key": "DR-GP-N3-050-F",
        "grammar_code": "GP-N3-050",
        "drill_type": "formation",
        "prompt_jp": "普段は優しい妻でも、私が約束を破るとたまに返事を（　　）ことがある。",
        "options": ["しない", "しなかった", "しなくて", "しよう"],
        "correct_index": 0,
        "translation_vi": "Vợ tôi bình thường hiền vậy đấy, nhưng hễ tôi thất hứa thì thỉnh thoảng cũng có lúc cô ấy không thèm trả lời.",
        "explanation_vi": "Diễn tả tần suất thỉnh thoảng không làm V dùng [Vない + ことがある] (không dùng quá khứ Vなかった).",
        "option_diagnostics": [
            "[ĐÚNG - Vない + ことがある (Tần suất)]: 返事をしないことがある = đôi khi không trả lời.",
            "[SAI - Sai thì quá khứ]: Thói quen/tần suất lặp lại thỉnh thoảng không dùng quá khứ phủ định しなかった.",
            "[SAI - Sai dạng thể て]: Thể て không nối trực tiếp vào ことがある.",
            "[SAI - Sai thể ý chí]: Thể ý chí しよう không kết hợp ことがある.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-050-A",
        "grammar_code": "GP-N3-050",
        "drill_type": "application",
        "prompt_jp": "「絶対に負けない」と無理をして努力し続けたら、心が（　　）だろう。",
        "options": ["つらくなることもある", "つらくなることはない", "つらくなったことによる", "つらくなることになっている"],
        "correct_index": 0,
        "translation_vi": "Nếu cứ ép bản thân nỗ lực với suy nghĩ 'tuyệt đối không được thua' thì cũng có lúc lòng thấy mệt mỏi đấy.",
        "explanation_vi": "Khả năng hệ quả tâm lý đôi khi xảy ra nếu tiếp tục ép mình quá mức dùng [Vる + こともある] (Q#156).",
        "option_diagnostics": [
            "[ĐÚNG - Khả năng thỉnh thoảng xảy ra こともある]: つらくなることもあるだろう (Q#156).",
            "[SAI - Ngược nghĩa hoàn toàn]: ことはない nghĩa là 'không cần thiết / không đời nào bị mệt mỏi', mâu thuẫn với lời khuyên phía sau.",
            "[SAI - Sai cấu trúc]: *ことによる không đặt cuối câu dự đoán cùng だろう.",
            "[SAI - Sai nghĩa quy định]: ことになっている là quy định/lịch trình đã định sẵn.",
        ],
    },
    # --- GP-N3-051 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-051-C",
        "grammar_code": "GP-N3-051",
        "drill_type": "contrast",
        "prompt_jp": "面接の質問はとても簡単なものばかりですから、そんなに（　　）。",
        "options": ["心配することもあります", "心配することはありません", "心配するわけにはいきません", "心配したつもりです"],
        "correct_index": 1,
        "translation_vi": "Câu hỏi phỏng vấn toàn là những câu rất đơn giản thôi nên bạn không cần thiết phải lo lắng đến thế đâu.",
        "explanation_vi": "Trấn an, khuyên người nghe 'không cần thiết phải lo lắng' dùng [Vる + ことはない / ことはありません].",
        "option_diagnostics": [
            "[SAI - Ngược ý trấn an]: こともあります nghĩa là 'thỉnh thoảng cũng có lúc lo lắng đấy', gây hoang mang thêm.",
            "[ĐÚNG - Trấn an 'không cần thiết phải' ことはありません]: 心配することはありません.",
            "[SAI - Sai nghĩa]: わけにはいきません nghĩa là 'không thể lo lắng được vì quy tắc cấm'.",
            "[SAI - Sai chủ thể và nghĩa]: 'Tôi cứ đinh ninh là đã lo' sai ngữ cảnh.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-051-A",
        "grammar_code": "GP-N3-051",
        "drill_type": "application",
        "prompt_jp": "失敗は誰にでもあることなのだから、君が一人で責任を（　　）。",
        "options": ["感じることはないよ", "感じることがあるよ", "感じるしかないよ", "感じるべきだよ"],
        "correct_index": 0,
        "translation_vi": "Thất bại là chuyện ai cũng có mà, nên cậu không việc gì phải tự mình ôm hết trách nhiệm đâu.",
        "explanation_vi": "Động viên bạn đừng tự trách mình quá mức -> 責任を感じることはないよ (= 感じる必要はない).",
        "option_diagnostics": [
            "[ĐÚNG - Khuyên đừng tự trách ことはない]: 責任を感じることはないよ.",
            "[SAI - Không phải câu động viên]: 感じることがあるよ ('thỉnh thoảng có lúc thấy có lỗi') không khớp vế nguyên nhân 'ai cũng từng sai'.",
            "[SAI - Ngược nghĩa ép buộc]: 感じるしかない ('đành phải tự nhận lỗi thôi') trái hẳn ý an ủi.",
            "[SAI - Ngược nghĩa trách móc]: 感じるべきだ ('cậu đáng phải chịu trách nhiệm đi') trái với vế trước.",
        ],
    },
    # --- GP-N3-052 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-052-F",
        "grammar_code": "GP-N3-052",
        "drill_type": "formation",
        "prompt_jp": "私はにんじんやピーマン（　　）濃い色の野菜が好きだ。",
        "options": ["のような", "のように", "のようだ", "らしい"],
        "correct_index": 0,
        "translation_vi": "Tôi thích các loại rau có màu đậm chẳng hạn như cà rốt hay ớt chuông.",
        "explanation_vi": "Đứng trước cụm danh từ '濃い色の野菜' để đưa ví dụ minh họa thì dùng dạng bổ nghĩa danh từ [N + のような + N].",
        "option_diagnostics": [
            "[ĐÚNG - N1 + のような + N2]: Bổ nghĩa cho cụm danh từ 濃い色の野菜.",
            "[SAI - Sai dạng phó từ のように]: のように bổ nghĩa cho động từ/tính từ (như のように赤い), không đứng trực tiếp bổ nghĩa cho cụm danh từ 濃い色の野菜 theo nghĩa 'những loại rau như...'.",
            "[SAI - Sai dạng kết thúc câu]: のようだ chỉ dùng kết thúc câu hoặc trước が.",
            "[SAI - Sai nghĩa]: らしい mang nghĩa 'đúng chất là cà rốt/ớt chuông', không dùng để liệt kê ví dụ.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-052-C",
        "grammar_code": "GP-N3-052",
        "drill_type": "contrast",
        "prompt_jp": "今日はとても暖かくて、（　　）春が来たかのようだ。",
        "options": ["たとえ", "まるで", "おそらく", "決して"],
        "correct_index": 1,
        "translation_vi": "Hôm nay trời ấm áp vô cùng, cứ như thể mùa xuân đã đến rồi vậy.",
        "explanation_vi": "Phó từ hô ứng bắt buộc với so sánh ví von ～かのようだ là まるで ('cứ như thể là...').",
        "option_diagnostics": [
            "[SAI - Sai phó từ điều kiện]: たとえ đi với ～ても/でも để nhượng bộ, không đi với ようだ.",
            "[ĐÚNG - Cặp hô ứng ví von まるで ～ ようだ]: まるで春が来たかのようだ.",
            "[SAI - Sai phó từ phỏng đoán]: おそらく đi với だろう/に違いない, không dùng trong so sánh ví von dù biết rõ chưa phải mùa xuân.",
            "[SAI - Sai phó từ phủ định]: 決して đi với phủ định, không ghép với かのようだ.",
        ],
    },
    # --- GP-N3-053 (formation + contrast + application) ---
    {
        "drill_key": "DR-GP-N3-053-F",
        "grammar_code": "GP-N3-053",
        "drill_type": "formation",
        "prompt_jp": "夏休みになってから、弟は毎日家で寝て（　　）。",
        "options": ["だらけだ", "ばかりいる", "のみだ", "続けている"],
        "correct_index": 1,
        "translation_vi": "Từ khi nghỉ hè đến giờ, em trai tôi ngày nào cũng chỉ toàn ngủ ở nhà.",
        "explanation_vi": "Ngay trước chỗ trống là động từ chia thể て (寝て) nên bắt buộc chọn ばかりいる (Q#55).",
        "option_diagnostics": [
            "[SAI - Lỗi ghép だらけ sau động từ Vて]: だらけ CHỈ gắn sau DANH TỪ tiêu cực (như 間違いだらけ), tuyệt đối không gắn sau Vて!",
            "[ĐÚNG - Vて + ばかりいる]: Suốt ngày chỉ toàn làm một hành động (chê lười biếng).",
            "[SAI - Lỗi ghép のみ sau Vて]: のみ chỉ đứng sau Vる hoặc Danh từ trong văn viết trang trọng.",
            "[SAI - Lỗi ghép 続ける sau Vて]: 続ける phải gắn sau gốc Vます bỏ ます (寝続けている), không gắn sau Vて (*寝て続けている).",
        ],
    },
    {
        "drill_key": "DR-GP-N3-053-C",
        "grammar_code": "GP-N3-053",
        "drill_type": "contrast",
        "prompt_jp": "そんなに仕事（　　）、そのうち体をこわしてしまいますよ。",
        "options": ["をしたばかりだと", "をしてばかりいると", "をしたところだと", "をしたばかりに"],
        "correct_index": 1,
        "translation_vi": "Nếu bạn cứ suốt ngày chỉ toàn làm việc nhiều như thế thì chẳng mấy chốc sẽ đổ bệnh mất đấy.",
        "explanation_vi": "Hành động lặp đi lặp lại quá mức ('cứ suốt ngày làm việc như vậy') dùng [Vて + ばかりいる] (Q#20).",
        "option_diagnostics": [
            "[SAI - Nhầm với Vたばかり (vừa mới làm xong)]: そんなに ('nhiều đến thế') không đi với nghĩa vừa mới làm việc xong.",
            "[ĐÚNG - Vて + ばかりいる + と]: 仕事をしてばかりいると.",
            "[SAI - Nhầm thời điểm Vたところ]: ところだ chỉ điểm vừa dứt việc, không gây hậu quả ốm đau vì làm quá sức.",
            "[SAI - Sai sắc thái quá khứ 1 lần]: ばかりに là 'chỉ tại vì (1 lỗi trong quá khứ)', không khớp lời khuyên cảnh báo tương lai.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-053-A",
        "grammar_code": "GP-N3-053",
        "drill_type": "application",
        "prompt_jp": "最近、夜遅くに無言の変な電話（　　）かかってきて困っている。",
        "options": ["ばかり", "こそ", "しか", "だけ"],
        "correct_index": 0,
        "translation_vi": "Gần đây vào đêm khuya tôi cứ bị toàn những cuộc điện thoại kỳ lạ không nói gì gọi tới, thật khó chịu.",
        "explanation_vi": "Phàn nàn tần suất toàn những chuyện lặp lại gây phiền toái dùng N + ばかり.",
        "option_diagnostics": [
            "[ĐÚNG - N + ばかり (Toàn là thứ gây bực mình)]: 変な電話ばかりかかってくる.",
            "[SAI - Ngược cảm xúc khen ngợi]: こそ dùng để đề cao đích danh thứ đáng quý, không dùng cho điện thoại quấy rối.",
            "[SAI - Thiếu phủ định cuối câu]: Cuối câu là khẳng định 困っている nên không thể dùng しか.",
            "[SAI - Thiếu sắc thái lặp đi lặp lại khó chịu]: だけ chỉ mang nghĩa 'chỉ có mỗi cuộc gọi lạ' chứ không nhấn mạnh sự lặp lại phiền phức bằng ばかり.",
        ],
    },
    # --- GP-N3-054 (formation + application) ---
    {
        "drill_key": "DR-GP-N3-054-F",
        "grammar_code": "GP-N3-054",
        "drill_type": "formation",
        "prompt_jp": "彼はピアノ（　　）、難しいバイオリンもひけるなんてすごいですね。",
        "options": ["ばかりでなく", "ばかりの", "ばかりしか", "ばかりほど"],
        "correct_index": 0,
        "translation_vi": "Anh ấy không chỉ chơi được piano mà còn chơi được cả violin khó nữa, thật giỏi quá.",
        "explanation_vi": "Mở rộng 'không chỉ N1 mà cả N2 cũng...' dùng [N1 + ばかりでなく + N2 + も] (Q#60).",
        "option_diagnostics": [
            "[ĐÚNG - N1 + ばかりでなく + N2 + も]: ピアノばかりでなくバイオリンも.",
            "[SAI - Không tồn tại *ピアノばかりのバイオリンも]: Thiếu cấu trúc phủ định でなく.",
            "[SAI - Sai kết hợp từ]: Không ghép *ばかりしか.",
            "[SAI - Sai kết hợp từ]: Không ghép *ばかりほど.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-054-A",
        "grammar_code": "GP-N3-054",
        "drill_type": "application",
        "prompt_jp": "このお店は味が美味しい（　　）、値段も安くて店員の態度まで素晴らしい。",
        "options": ["ばかりか", "ばかりに", "くせに", "わりに"],
        "correct_index": 0,
        "translation_vi": "Quán này không chỉ món ăn ngon, mà giá cả cũng rẻ và đến cả thái độ nhân viên cũng tuyệt vời.",
        "explanation_vi": "Tăng cấp khen ngợi liên tiếp từ ngon -> giá rẻ -> thái độ nhân viên tuyệt dùng ～ばかりか...～まで.",
        "option_diagnostics": [
            "[ĐÚNG - Tăng tiến ấn tượng ～ばかりか ～も/まで]: Ngon không thôi chưa đủ mà còn rẻ và phục vụ tốt.",
            "[SAI - Sai nghĩa 'chỉ tại vì']: ばかりに dùng để than trách hậu quả xấu.",
            "[SAI - Sai nghĩa chê trách]: くせに chỉ thái độ bất mãn chê bai.",
            "[SAI - Ngược chiều tương phản]: わりに nghĩa là 'dù ngon vậy nhưng...', mâu thuẫn với mạch khen liên hoàn.",
        ],
    },
    # --- GP-N3-055 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-055-C",
        "grammar_code": "GP-N3-055",
        "drill_type": "contrast",
        "prompt_jp": "うっかり確認し忘れた（　　）、大切な書類を送り間違えてしまった。",
        "options": ["ばかりか", "ばかりに", "ばかりだ", "ばかりいる"],
        "correct_index": 1,
        "translation_vi": "Chỉ tại vì lỡ quên không kiểm tra lại mà tôi đã gửi nhầm mất tập tài liệu quan trọng.",
        "explanation_vi": "Nhấn mạnh chỉ vì một lỗi sai duy nhất ở vế trước mà gây ra hậu quả đáng tiếc ở vế sau dùng [Vた + ばかりに].",
        "option_diagnostics": [
            "[SAI - Nhầm sang nghĩa 'không chỉ... mà còn']: ばかりか không giải thích nguyên nhân duy nhất gây hối tiếc.",
            "[ĐÚNG - Nguyên nhân duy nhất gây hậu quả xấu Vた + ばかりに]: 確認し忘れたばかりに.",
            "[SAI - Đặt sai vị trí đuôi câu]: ばかりだ là vị ngữ kết thúc câu, không nối nguyên nhân giữa câu.",
            "[SAI - Sai dạng sau Vた]: Vてばかりいる gắn sau thể て để chỉ thói quen lặp lại, không gắn sau Vた.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-055-A",
        "grammar_code": "GP-N3-055",
        "drill_type": "application",
        "prompt_jp": "手術が終わってからも、父の体調はなかなか良くならず、心配は（　　）。",
        "options": ["増えるばかりだ", "増えたばかりだ", "増やすばかりに", "増えてばかりだ"],
        "correct_index": 0,
        "translation_vi": "Ngay cả sau khi ca mổ kết thúc, sức khỏe của bố mãi không khá lên nên nỗi lo lắng cứ ngày càng tăng thêm.",
        "explanation_vi": "Xu hướng ngày càng tăng/xấu đi một chiều dùng [Vる + ばかりだ] -> 増えるばかりだ.",
        "option_diagnostics": [
            "[ĐÚNG - Xu hướng trượt dốc một chiều Vる + ばかりだ]: 心配は増えるばかりだ.",
            "[SAI - Nhầm với Vたばかり (vừa mới)]: 'Nỗi lo vừa mới tăng xong' không thể hiện đà tiếp diễn kéo dài không dứt.",
            "[SAI - Sai tự/tha động từ và trợ từ]: 心配は đi với tự động từ 増える, không đi với tha động từ 増やす.",
            "[SAI - Sai kết hợp]: Để nói 'suốt ngày chỉ toàn...' phải là ばかりいる chứ không gắn ばかりだ trực tiếp sau Vて.",
        ],
    },
    # --- GP-N3-056 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-056-F",
        "grammar_code": "GP-N3-056",
        "drill_type": "formation",
        "prompt_jp": "彼女は英語も（　　）、中国語もペラペラに話せる。",
        "options": ["話せれば", "話したら", "話せると", "話して"],
        "correct_index": 0,
        "translation_vi": "Cô ấy vừa nói được tiếng Anh mà tiếng Trung cũng nói lưu loát.",
        "explanation_vi": "Cấu trúc song hành đối xứng [Aも Vば、Bも V] bắt buộc chia động từ vế đầu sang thể ば -> 話せる chia 話せれば.",
        "option_diagnostics": [
            "[ĐÚNG - Cặp đối xứng AもVば、BもV]: 話せる -> 話せれば.",
            "[SAI - Không dùng たら trong mẫu song hành も～も]: Mẫu liệt kê đối xứng bắt buộc dùng thể ば.",
            "[SAI - Không dùng と trong mẫu song hành も～も]: と chỉ điều kiện tất yếu, không ghép cặp liệt kê も～も.",
            "[SAI - Thiếu kết nối song hành ば]: Nối bằng thể て không khớp khung nhấn mạnh も～ば～も.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-056-C",
        "grammar_code": "GP-N3-056",
        "drill_type": "contrast",
        "prompt_jp": "このホテルは部屋も（　　）、駅からのアクセスも抜群だ。",
        "options": ["広ければ", "広いのに", "広いと", "広いなら"],
        "correct_index": 0,
        "translation_vi": "Khách sạn này phòng vừa rộng rãi mà đường đi từ nhà ga cũng tiện tuyệt vời.",
        "explanation_vi": "Nêu hai ưu điểm song hành với hai trợ từ も bằng [Aければ～も] -> 広ければ.",
        "option_diagnostics": [
            "[ĐÚNG - Tính từ い chia ければ trong mẫu も～ば～も]: 広い -> 広ければ.",
            "[SAI - Ngược nghĩa nhượng bộ]: のに tạo nghĩa trái ngược 'tuy phòng rộng nhưng...', mâu thuẫn với ưu điểm thứ 2 抜群だ.",
            "[SAI - Sai cấu trúc song hành]: と không thay thế ば trong mẫu 部屋も～駅も～.",
            "[SAI - Sai nghĩa giả định]: なら đặt giả thuyết chứ không liệt kê song hành hai ưu điểm có thật.",
        ],
    },
    # --- GP-N3-057 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-057-C",
        "grammar_code": "GP-N3-057",
        "drill_type": "contrast",
        "prompt_jp": "東京や大阪（　　）大都市では、交通網が非常に発達している。",
        "options": ["といった", "という", "とした", "とよばれる"],
        "correct_index": 0,
        "translation_vi": "Ở các đô thị lớn ví dụ như Tokyo hay Osaka, mạng lưới giao thông phát triển rất mạnh.",
        "explanation_vi": "Đứng sau hai ví dụ tiêu biểu (東京や大阪) và trước danh từ tập hợp bao quát (大都市) dùng N1やN2 + といった + N.",
        "option_diagnostics": [
            "[ĐÚNG - Liệt kê ví dụ văn viết といった]: 東京や大阪といった大都市.",
            "[SAI - Lỗi nghĩa định danh]: という biến cả cụm thành 'đại đô thị tên là Tokyo hay Osaka', sai vì đó là 2 thành phố riêng lẻ thuộc nhóm đại đô thị.",
            "[SAI - Sai mẫu]: とした dùng trong 目的とした (lấy làm mục đích), không dùng liệt kê ví dụ.",
            "[SAI - Sai ngữ nghĩa]: と呼ばれる nghĩa là 'được gọi là đại đô thị', làm lệch chức năng liệt kê ví dụ.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-057-A",
        "grammar_code": "GP-N3-057",
        "drill_type": "application",
        "prompt_jp": "日本の春には、桜や梅（　　）美しい花々を楽しめる。",
        "options": ["といった", "に限って", "に際して", "のわりに"],
        "correct_index": 0,
        "translation_vi": "Vào mùa xuân Nhật Bản, ta có thể thưởng thức nhiều loài hoa đẹp ví dụ như hoa anh đào hay hoa mơ.",
        "explanation_vi": "Liệt kê đại diện hoa anh đào và hoa mơ cho nhóm tổng quát 美しい花々 dùng といった.",
        "option_diagnostics": [
            "[ĐÚNG - Ví dụ thuộc tập hợp といった]: 桜や梅といった花々.",
            "[SAI - Sai nghĩa 'chỉ riêng vào dịp']: に限って nghĩa là 'đúng vào dịp...', không nối ví dụ với danh từ tổng hợp.",
            "[SAI - Sai nghĩa 'nhân dịp']: に際して dùng cho sự kiện trang trọng, không nối tên hoa.",
            "[SAI - Sai nghĩa tương phản]: のわりに nghĩa là 'so với hoa đào hoa mơ thì...'.",
        ],
    },
    # --- GP-N3-058 (formation + application) ---
    {
        "drill_key": "DR-GP-N3-058-F",
        "grammar_code": "GP-N3-058",
        "drill_type": "formation",
        "prompt_jp": "隣の席の同僚は、いつも人の給料の額を（　　）いる。",
        "options": ["知りたくて", "知りたがって", "知りたいと思って", "知りたそうで"],
        "correct_index": 1,
        "translation_vi": "Đồng nghiệp ngồi bàn bên cạnh lúc nào cũng tò mò muốn biết mức lương của người khác.",
        "explanation_vi": "Diễn đạt biểu hiện mong muốn của NGÔI THỨ 3 (同僚) qua hành vi bên ngoài dùng Vます + たがっている.",
        "option_diagnostics": [
            "[SAI - Dùng たい của ngôi 1 cho ngôi 3]: Không nói *同僚は知りたくている cho mong muốn của người thứ ba.",
            "[ĐÚNG - Biểu hiện mong muốn ngôi 3 たがっている]: 知る -> 知り + たがって + いる.",
            "[SAI - Lỗi cấu trúc trước いる]: たいと思っている là 'đang nghĩ muốn', không nối *知りたいと思って + いる.",
            "[SAI - Sai hình thái]: *知りたそうで không nối với いる.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-058-A",
        "grammar_code": "GP-N3-058",
        "drill_type": "application",
        "prompt_jp": "うちの猫は初めて会う人をとても（　　）、すぐベッドの下に隠れてしまう。",
        "options": ["怖くて", "怖がって", "怖そうで", "怖くなって"],
        "correct_index": 1,
        "translation_vi": "Con mèo nhà tôi rất sợ người mới gặp lần đầu nên hễ thấy là trốn ngay dưới gầm giường.",
        "explanation_vi": "Tân ngữ đi với を (人を) và diễn tả biểu hiện sợ hãi của ngôi thứ 3 (con mèo) -> tính từ 怖い bỏ い + がる -> 怖がって.",
        "option_diagnostics": [
            "[SAI - Dùng tính từ cảm xúc chủ quan với tân ngữ を]: 怖い đi với が (人が怖い), không đi với tân ngữ を (*人を怖い) và không dùng cho con mèo.",
            "[ĐÚNG - Động từ hóa cảm xúc ngôi 3 với を]: 怖い bỏ い + がって -> 怖がって.",
            "[SAI - Sai nghĩa 'trông có vẻ đáng sợ']: 怖そうで nghĩa là 'người lạ trông đáng sợ' (và không nhận tân ngữ を).",
            "[SAI - Sai trợ từ を]: 怖くなる không nhận tân ngữ 人を.",
        ],
    },
    # --- GP-N3-059 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-059-F",
        "grammar_code": "GP-N3-059",
        "drill_type": "formation",
        "prompt_jp": "エアコンが壊れてしまい、部屋の中が（　　）たまらない。",
        "options": ["暑い", "暑くて", "暑く", "暑かった"],
        "correct_index": 1,
        "translation_vi": "Điều hòa bị hỏng mất rồi, trong phòng nóng đến mức không chịu nổi.",
        "explanation_vi": "Trước ～たまらない / ～しょうがない, tính từ đuôi い bắt buộc chia thể て -> 暑くてたまらない.",
        "option_diagnostics": [
            "[SAI - Thiếu chia thể て]: Tính từ đuôi い không đứng nguyên thể trước たまらない.",
            "[ĐÚNG - Aい(くて) + たまらない]: 暑い -> 暑くて + たまらない.",
            "[SAI - Chia dạng phó từ く]: Dạng く đi với なる/する, không đi với たまらない.",
            "[SAI - Chia quá khứ trực tiếp]: Thì quá khứ phải chia ở cuối câu (暑くてたまらなかった), không chia ở tính từ phía trước.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-059-C",
        "grammar_code": "GP-N3-059",
        "drill_type": "contrast",
        "prompt_jp": "もうすぐ日本に留学するので、今は毎日出発の日が（　　）。",
        "options": ["楽しみでならない", "楽しんでたまらない", "楽しみなわけがない", "楽しみなばかりだ"],
        "correct_index": 0,
        "translation_vi": "Vì sắp đi du học Nhật rồi nên bây giờ ngày nào tôi cũng háo hức mong chờ ngày xuất phát đến không chịu nổi.",
        "explanation_vi": "楽しみ là tính từ đuôi な (hoặc danh từ), nên trước ならない chia thành 楽しみでならない.",
        "option_diagnostics": [
            "[ĐÚNG - Aな(で) + ならない]: 楽しみでならない = háo hức mong chờ vô cùng.",
            "[SAI - Nhầm từ loại động từ 楽しむ]: Sau '日が' không dùng tha động từ 楽しんで (vì 楽しむ đi với を).",
            "[SAI - Ngược hoàn toàn cảm xúc]: わけがない nghĩa là 'làm sao mà háo hức được'.",
            "[SAI - Sai cấu trúc và nghĩa]: *楽しみなばかりだ không biểu đạt cảm xúc mãnh liệt.",
        ],
    },
    # --- GP-N3-060 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-060-C",
        "grammar_code": "GP-N3-060",
        "drill_type": "contrast",
        "prompt_jp": "大事な商談を（　　）最中に、携帯電話が鳴り出してしまった。",
        "options": ["した", "している", "する", "しておいた"],
        "correct_index": 1,
        "translation_vi": "Đúng lúc đang thực hiện cuộc thương lượng quan trọng giữa chừng thì điện thoại di động lại đổ chuông.",
        "explanation_vi": "Trước ～最中に (đúng lúc đang diễn ra cao trào) động từ bắt buộc ở thể tiếp diễn Vている -> している最中に.",
        "option_diagnostics": [
            "[SAI - Sai thì quá khứ Vた]: Sau Vた là xong rồi, không dùng *した最中に (trừ danh từ hóa bằng の như 商談の最中に).",
            "[ĐÚNG - Vている + 最中に]: Đang giữa chừng hành động thì biến cố xen ngang.",
            "[SAI - Sai nguyên thể Vる]: Trước 最中に không dùng nguyên thể *する最中に.",
            "[SAI - Sai dạng chuẩn bị ておいた]: ておいた là làm xong trước rồi, không có nghĩa đang diễn ra.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-060-A",
        "grammar_code": "GP-N3-060",
        "drill_type": "application",
        "prompt_jp": "家族で楽しく夕食を食べている（　　）、急に地震が起きてみんな驚いた。",
        "options": ["最中に", "とたんに", "せいで", "たびに"],
        "correct_index": 0,
        "translation_vi": "Đúng lúc cả nhà đang vui vẻ ăn bữa tối thì đột nhiên động đất xảy ra làm mọi người giật mình.",
        "explanation_vi": "Động đất xảy ra xen ngang vào giữa bữa ăn đang diễn ra -> Vている + 最中に.",
        "option_diagnostics": [
            "[ĐÚNG - Xen ngang giữa lúc đang Vている + 最中に]: 食べている最中に.",
            "[SAI - Dùng とたんに sau Vている]: とたんに bắt buộc đi sau Vた ('vừa mới ăn xong') chứ không gắn sau Vている.",
            "[SAI - Sai quan hệ nhân quả]: Không phải tại gia đình ăn cơm nên mới gây ra động đất.",
            "[SAI - Sai nghĩa lặp lại]: Không phải 'cứ mỗi lần ăn cơm tối là có động đất'.",
        ],
    },
    # --- GP-N3-061 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-061-F",
        "grammar_code": "GP-N3-061",
        "drill_type": "formation",
        "prompt_jp": "教室のドアを（　　）とたんに、みんなの視線が私に集まった。",
        "options": ["開ける", "開けた", "開けて", "開けている"],
        "correct_index": 1,
        "translation_vi": "Vừa mở cửa lớp học ra một cái là ánh mắt của mọi người đổ dồn ngay về phía tôi.",
        "explanation_vi": "Ngay khoảnh khắc vừa hoàn thành động tác mở cửa dùng [Vた + とたん（に）] -> 開けたとたんに.",
        "option_diagnostics": [
            "[SAI - Thiếu thì quá khứ Vた]: Trước とたん(に) bắt buộc dùng thể quá khứ Vた (không dùng Vる).",
            "[ĐÚNG - Vた + とたんに]: 開けたとたんに.",
            "[SAI - Thể て sai hình thái]: Không gắn とたん sau thể て (*開けてとたん).",
            "[SAI - Thể tiếp diễn sai hình thái]: Không gắn とたん sau Vている (*開けているとたん).",
        ],
    },
    {
        "drill_key": "DR-GP-N3-061-C",
        "grammar_code": "GP-N3-061",
        "drill_type": "contrast",
        "prompt_jp": "母は家族に、いつも（　　）のごはんを食べさせたいと思っている。",
        "options": ["炊いたとたん", "炊きたて", "炊きかけ", "炊きっぱなし"],
        "correct_index": 1,
        "translation_vi": "Mẹ lúc nào cũng muốn cho gia đình ăn cơm vừa mới nấu xong nóng hổi.",
        "explanation_vi": "Bổ nghĩa danh từ ごはん qua trợ từ の để tả cơm vừa nấu chín xong nóng hổi phải dùng Vます + たて (Q#51).",
        "option_diagnostics": [
            "[SAI - Không bổ nghĩa danh từ ごはん kiểu này]: Vた+とたん nối 2 mệnh đề xảy ra liên tiếp tích tắc, không gắn *炊いたとたんのごはん.",
            "[ĐÚNG - Vます + たて + の + N]: 炊きたてのごはん (Q#51).",
            "[SAI - Sai nghĩa đang dở dang]: 炊きかけのごはん là cơm đang nấu dở còn sống.",
            "[SAI - Sai sắc thái chê cẩu thả]: 炊きっぱなし là nấu xong cứ để mặc đấy không rút điện/dọn.",
        ],
    },
    # --- GP-N3-062 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-062-C",
        "grammar_code": "GP-N3-062",
        "drill_type": "contrast",
        "prompt_jp": "天気予報によると、今夜から明日の朝（　　）、雪が降るおそれがある。",
        "options": ["までに", "にかけて", "につれて", "によって"],
        "correct_index": 1,
        "translation_vi": "Theo dự báo thời tiết, từ đêm nay kéo sang sáng ngày mai có nguy cơ sẽ có tuyết rơi.",
        "explanation_vi": "Khoảng thời gian ước lượng chuyển giao từ tối nay sang sáng mai trong bản tin thời tiết dùng から～にかけて.",
        "option_diagnostics": [
            "[SAI - Nhầm với hạn chót hoàn thành]: までに chỉ hạn chót trước một mốc cụ thể, không đi cặp với から (から～までに không tự nhiên ở đây).",
            "[ĐÚNG - Cặp phạm vi thời gian chuyển giao から～にかけて]: 今夜から明日の朝にかけて.",
            "[SAI - Sai nghĩa tỷ lệ thuận]: につれて chỉ sự biến đổi tăng giảm song hành.",
            "[SAI - Sai nghĩa tác nhân/tùy theo]: によって không nối 2 mốc thời gian sau から.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-062-A",
        "grammar_code": "GP-N3-062",
        "drill_type": "application",
        "prompt_jp": "この果物は毎年9月から10月（　　）収穫の時期を迎える。",
        "options": ["にかけて", "に対して", "において", "にとって"],
        "correct_index": 0,
        "translation_vi": "Loại trái cây này hằng năm bước vào mùa thu hoạch từ khoảng tháng 9 sang tháng 10.",
        "explanation_vi": "Nối 2 mốc thời gian mùa vụ ước chừng từ tháng 9 sang tháng 10 dùng から～にかけて.",
        "option_diagnostics": [
            "[ĐÚNG - Khoảng thời gian chuyển tiếp から～にかけて]: 9月から10月にかけて.",
            "[SAI - Sai nghĩa đối tượng/tương phản]: に対して không nối 2 mốc thời gian sau から.",
            "[SAI - Sai cấu trúc]: において chỉ địa điểm/bối cảnh, không nối với から phía trước.",
            "[SAI - Sai nghĩa lập trường]: にとって không nối khoảng thời gian.",
        ],
    },
    # --- GP-N3-063 (formation + application) ---
    {
        "drill_key": "DR-GP-N3-063-F",
        "grammar_code": "GP-N3-063",
        "drill_type": "formation",
        "prompt_jp": "「どうして宿題をやってこないの？」「だって時間が（　　）もん。」",
        "options": ["ないだ", "なかったんだ", "ないの", "なくて"],
        "correct_index": 1,
        "translation_vi": "'Sao cậu không làm bài tập mang tới?' — 'Tại vì tớ không có thời gian mà.'",
        "explanation_vi": "Thể thông thường quá khứ giải thích lý do khẩu ngữ với だって～もん dùng [なかった + ん + だ + もん] -> なかったんだもん.",
        "option_diagnostics": [
            "[SAI - Thừa だ sau tính từ ない]: ない tự nó kết thúc ở thể thông thường, cấm viết *ないだ.",
            "[ĐÚNG - Giải thích lý do khẩu ngữ ～んだもん]: なかったんだもん.",
            "[SAI - Thiếu だ trước もん]: Khi giải thích bằng の trong câu này phải là のだ/んだ trước もん.",
            "[SAI - Thể て sai vị trí cuối câu]: なくてもん không phải cấu trúc ngữ pháp.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-063-A",
        "grammar_code": "GP-N3-063",
        "drill_type": "application",
        "prompt_jp": "「またケーキ食べてるの？」「だって、とてもおいしそうなんだ（　　）。」",
        "options": ["もん", "ものか", "べきだ", "おそれがある"],
        "correct_index": 0,
        "translation_vi": "'Lại đang ăn bánh ngọt nữa à?' — 'Thì tại nó trông ngon quá đi mất mà.'",
        "explanation_vi": "Hô ứng với だって để thanh minh vui vẻ thân mật ở cuối câu dùng もん (rút gọn của もの).",
        "option_diagnostics": [
            "[ĐÚNG - Thanh minh thân mật だって～もん]: Đáp lại câu hỏi bắt bẻ nhẹ.",
            "[SAI - Ngược nghĩa thành phản bác 'làm gì có chuyện']: ものか nghĩa là 'không đời nào ngon được', mâu thuẫn với だって.",
            "[SAI - Sai văn phong]: べきだ là khuyên nhủ đạo đức cứng nhắc.",
            "[SAI - Sai văn phong y khoa/thời sự]: おそれがある dùng cảnh báo rủi ro.",
        ],
    },
    # --- GP-N3-064 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-064-C",
        "grammar_code": "GP-N3-064",
        "drill_type": "contrast",
        "prompt_jp": "使用回数を守らないと、皮膚の症状が悪くなる（　　）。（薬の説明書）",
        "options": ["にきまっています", "おそれがあります", "ずにはいられません", "ばかりいます"],
        "correct_index": 1,
        "translation_vi": "Nếu không tuân thủ số lần sử dụng, triệu chứng ngoài da có nguy cơ trở nên nặng hơn. (Hướng dẫn thuốc)",
        "explanation_vi": "Văn bản hướng dẫn thuốc trang trọng cảnh báo rủi ro có thể xảy ra phải dùng おそれがあります (loại suy đoán cảm tính にきまっています) (Q#147).",
        "option_diagnostics": [
            "[SAI - Quả quyết chủ quan sai văn phong y khoa]: にきまっています là khẩu khí quả quyết cảm tính cá nhân, không dùng trong hướng dẫn sử dụng thuốc.",
            "[ĐÚNG - Cảnh báo rủi ro y khoa おそれがあります]: Trang trọng, khách quan (Q#147).",
            "[SAI - Sai chủ thể cảm xúc con người]: ずにはいられません chỉ dùng cho cảm xúc/hành vi không nhịn được của con người, không dùng cho 'triệu chứng'.",
            "[SAI - Sai dạng kết hợp]: ばかりいます gắn sau Vて chứ không gắn sau Vる 悪くなる.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-064-A",
        "grammar_code": "GP-N3-064",
        "drill_type": "application",
        "prompt_jp": "あんなに毎日遅くまで練習していたんだから、彼は次の試合に（　　）。",
        "options": ["勝つに決まっている", "勝つわけにはいかない", "勝つおそれがある", "勝つにすぎない"],
        "correct_index": 0,
        "translation_vi": "Anh ấy tập luyện tới khuya mỗi ngày như thế kia cơ mà, trận tới chắc chắn là thắng rồi.",
        "explanation_vi": "Niềm tin chủ quan chắc nịch của bạn bè khi cổ vũ ('tập thế kia thì thắng chắc rồi!') dùng Vる + に決まっている.",
        "option_diagnostics": [
            "[ĐÚNG - Quả quyết chủ quan mạnh mẽ に決まっている]: 勝つに決まっている.",
            "[SAI - Ngược nghĩa]: わけにはいかない là 'không thể thắng vì đạo lý cấm'.",
            "[SAI - Sai sắc thái tiêu cực]: おそれがある chỉ dùng cho chuyện xấu/rủi ro, không dùng cho việc thắng trận.",
            "[SAI - Sai nghĩa hạ thấp]: にすぎない là 'chẳng qua chỉ thắng thôi'.",
        ],
    },
    # --- GP-N3-065 (formation + contrast + application) ---
    {
        "drill_key": "DR-GP-N3-065-F",
        "grammar_code": "GP-N3-065",
        "drill_type": "formation",
        "prompt_jp": "玄関に彼の靴がない。もう出かけた（　　）。",
        "options": ["に違いない", "だに違いない", "のに違いない", "なにちがいない"],
        "correct_index": 0,
        "translation_vi": "Ở lối vào không thấy giày của anh ấy. Chắc chắn là anh ấy đã ra ngoài rồi.",
        "explanation_vi": "Động từ quá khứ thông thường 出かけた gắn trực tiếp vào に違いない (không thêm だ hay の).",
        "option_diagnostics": [
            "[ĐÚNG - V普通形 + に違いない]: 出かけた + に違いない.",
            "[SAI - Thừa だ sau động từ]: Không bao giờ thêm だ vào sau động từ chia thì (*出かけた + だ).",
            "[SAI - Thừa trợ từ の]: Không chèn の vào giữa Vた và に違いない.",
            "[SAI - Thừa な sau động từ]: Không dùng な sau động từ 出かけた.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-065-C",
        "grammar_code": "GP-N3-065",
        "drill_type": "contrast",
        "prompt_jp": "その国の言葉ができないことは、おそらく大きなストレスに（　　）。",
        "options": ["なるにすぎない", "なるに違いない", "なってばかりいる", "なろうとする"],
        "correct_index": 1,
        "translation_vi": "Việc không nói được ngôn ngữ nước đó có lẽ chắc chắn sẽ trở thành áp lực lớn.",
        "explanation_vi": "Phó từ おそらく hô ứng trực tiếp với phỏng đoán tin cậy cao ～に違いない (Q#153).",
        "option_diagnostics": [
            "[SAI - Ngược nghĩa hạ thấp]: にすぎない là 'chỉ là áp lực nhỏ thôi', mâu thuẫn với 大きなストレス.",
            "[ĐÚNG - Cặp hô ứng おそらく ～ に違いない]: Phỏng đoán chắc chắn trong văn nghị luận (Q#153).",
            "[SAI - Sai nghĩa lặp lại]: なってばかりいる nghĩa là 'suốt ngày chỉ toàn biến thành stress'.",
            "[SAI - Gắn ý chí cho danh từ vô tri]: Stress không tự 'cố định trở thành' bằng なろうとする.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-065-A",
        "grammar_code": "GP-N3-065",
        "drill_type": "application",
        "prompt_jp": "犯人は（　　）に違いない。鍵のかかった部屋の中から盗まれたのだから。",
        "options": ["内部の人間", "内部の人間だ", "内部の人間の", "内部の人間な"],
        "correct_index": 0,
        "translation_vi": "Thủ phạm chắc chắn là người nội bộ rồi. Vì đồ bị trộm từ bên trong căn phòng khóa kín cơ mà.",
        "explanation_vi": "Trước ～に違いない, danh từ và tính từ な BẮT BUỘC bỏ だ (nhận danh từ trần 内部の人間 + に違いない).",
        "option_diagnostics": [
            "[ĐÚNG - Danh từ trần (bỏ だ) + に違いない]: 内部の人間に違いない.",
            "[SAI - Lỗi giữ だ trước に違いない]: Danh từ/tính từ な phải lược bỏ だ trước に違いない.",
            "[SAI - Thừa の]: Không thêm の giữa danh từ và に違いない.",
            "[SAI - Thừa な]: Danh từ trước に違いない không thêm な.",
        ],
    },
    # --- GP-N3-066 (formation + contrast + application) ---
    {
        "drill_key": "DR-GP-N3-066-F",
        "grammar_code": "GP-N3-066",
        "drill_type": "formation",
        "prompt_jp": "この古い橋は老朽化が進んでいるため、大雨が降ると（　　）おそれがある。",
        "options": ["崩れる", "崩れた", "崩れて", "崩れの"],
        "correct_index": 0,
        "translation_vi": "Cây cầu cũ này đang xuống cấp nên hễ mưa lớn là có nguy cơ bị sập.",
        "explanation_vi": "Trước ～おそれがある, động từ BẮT BUỘC chia về thể từ điển nguyên thể Vる (tuyệt đối không chia Vた hay Vて).",
        "option_diagnostics": [
            "[ĐÚNG - Vる + おそれがある]: 崩れるおそれがある.",
            "[SAI - Sai thì quá khứ]: Dự báo nguy cơ tương lai không chia quá khứ Vた (*崩れたおそれがある).",
            "[SAI - Thể て sai hình thái]: Không gắn おそれがある sau thể て.",
            "[SAI - Cắt cụt động từ]: 崩れ không đứng làm danh từ tự do với の ở đây; phải dùng nguyên thể Vる 崩れる.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-066-C",
        "grammar_code": "GP-N3-066",
        "drill_type": "contrast",
        "prompt_jp": "この薬を飲んだあとで車を運転すると、強い眠気から事故を（　　）。",
        "options": ["起こすおかげがある", "起こすおそれがある", "起こすはずがない", "起こすにちがいないと喜んだ"],
        "correct_index": 1,
        "translation_vi": "Nếu lái xe sau khi uống thuốc này, cơn buồn ngủ mạnh có nguy cơ gây ra tai nạn.",
        "explanation_vi": "Cảnh báo tác dụng phụ rủi ro y tế gây tai nạn -> Vる + おそれがある.",
        "option_diagnostics": [
            "[SAI - Lỗi chế cụm & sai sắc thái]: Không có mẫu *おかげがある và không dùng おかげ cho tai nạn.",
            "[ĐÚNG - Cảnh báo nguy cơ xấu おそれがある]: 事故を起こすおそれがある.",
            "[SAI - Ngược nghĩa nguy hiểm]: 'Làm sao có chuyện gây tai nạn' trái hoàn toàn mục đích cảnh báo thuốc.",
            "[SAI - Ngược cảm xúc nghiêm trọng]: Không ai 'vui mừng' vì có nguy cơ tai nạn.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-066-A",
        "grammar_code": "GP-N3-066",
        "drill_type": "application",
        "prompt_jp": "個人情報が外部に（　　）おそれがあるため、パスワードを変更してください。",
        "options": ["漏れる", "守られる", "増える", "成功する"],
        "correct_index": 0,
        "translation_vi": "Do có nguy cơ thông tin cá nhân bị rò rỉ ra ngoài, xin hãy đổi mật khẩu.",
        "explanation_vi": "～おそれがある chỉ đi với động từ mang kết quả XẤU/NGUY HIỂM ('rò rỉ thông tin' 漏れる).",
        "option_diagnostics": [
            "[ĐÚNG - Động từ kết quả xấu + おそれがある]: 個人情報が漏れる (bị rò rỉ).",
            "[SAI - Kết quả tốt không đi với おそれがある]: 'Được bảo vệ' là kết quả tốt, không dùng おそれがある.",
            "[SAI - Không khớp logic với đổi mật khẩu]: 'Thông tin tăng lên' không phải nguyên nhân bảo mật bắt đổi mật khẩu.",
            "[SAI - Kết quả tốt không đi với おそれがある]: 'Thành công' không bao giờ ghép với おそれがある.",
        ],
    },
    # --- GP-N3-067 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-067-C",
        "grammar_code": "GP-N3-067",
        "drill_type": "contrast",
        "prompt_jp": "それはまだ確認されていないただの噂（　　）から、慌てる必要はない。",
        "options": ["にほかならない", "にすぎない", "に違いない", "に限る"],
        "correct_index": 1,
        "translation_vi": "Đó chẳng qua chỉ là tin đồn chưa được xác thực thôi nên không cần phải hoảng hốt.",
        "explanation_vi": "Hô ứng với phó từ ただ ('chỉ đơn thuần là...') để hạ nhẹ tầm quan trọng của tin đồn dùng [N + にすぎない].",
        "option_diagnostics": [
            "[SAI - Ngược sắc thái nhấn mạnh]: にほかならない (N2) khẳng định tầm quan trọng tuyệt đối 'chính là...', trái với 慌てる必要はない.",
            "[ĐÚNG - Hạ thấp mức độ ただ～にすぎない]: Chẳng qua chỉ là tin đồn thôi.",
            "[SAI - Ngược nghĩa]: に違いない khẳng định tin đồn chắc chắn là sự thật.",
            "[SAI - Sai nghĩa]: に限る là 'là nhất'.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-067-A",
        "grammar_code": "GP-N3-067",
        "drill_type": "application",
        "prompt_jp": "彼はまだ経験の浅い新人（　　）のに、とても落ち着いて仕事をしている。",
        "options": ["にすぎない", "に決まっている", "ばかりいる", "おかげだ"],
        "correct_index": 0,
        "translation_vi": "Anh ấy chẳng qua mới chỉ là nhân viên mới ít kinh nghiệm vậy mà làm việc rất điềm tĩnh.",
        "explanation_vi": "Hạ thấp nền tảng hiện có (mới chỉ là người mới) để làm nổi bật kết quả đáng nể sau のに dùng N + にすぎない.",
        "option_diagnostics": [
            "[ĐÚNG - N + にすぎない + のに]: Mới chỉ là người mới thôi mà...",
            "[SAI - Sai nghĩa]: 'Chắc chắn là người mới vậy mà...' không tự nhiên bằng にすぎない.",
            "[SAI - Sai cấu trúc với danh từ 新人]: ばかりいる đi sau Vて, không đi sau danh từ 新人.",
            "[SAI - Sai cấu trúc và nghĩa]: 新人おかげだ là sai ngữ pháp.",
        ],
    },
    # --- GP-N3-068 (formation + application) ---
    {
        "drill_key": "DR-GP-N3-068-F",
        "grammar_code": "GP-N3-068",
        "drill_type": "formation",
        "prompt_jp": "長い間入院していた祖母が退院できて、家族みんながどんなに（　　）ことか。",
        "options": ["喜んだ", "喜んで", "喜ぼう", "喜ぶに"],
        "correct_index": 0,
        "translation_vi": "Bà tôi nằm viện suốt thời gian dài nay đã xuất viện được, cả gia đình đã vui mừng biết bao nhiêu.",
        "explanation_vi": "Cấu trúc cảm thán [どんなに + 普通形 + ことか]: vì sự việc đã diễn ra (退院できて) nên động từ chia quá khứ thông thường -> 喜んだことか.",
        "option_diagnostics": [
            "[ĐÚNG - どんなに + V普通形(quá khứ) + ことか]: 喜んだことか.",
            "[SAI - Thể て không đứng trước ことか]: Không dùng *喜んでことか.",
            "[SAI - Thể ý chí sai cấu trúc]: Không dùng thể ý chí trước ことか.",
            "[SAI - Thừa に]: Không chèn に trước ことか.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-068-A",
        "grammar_code": "GP-N3-068",
        "drill_type": "application",
        "prompt_jp": "こんな簡単なミスで負けてしまって、悔しくてたまらない。二度と同じ失敗を（　　）ものか。",
        "options": ["する", "しない", "した", "しよう"],
        "correct_index": 0,
        "translation_vi": "Thua chỉ vì một lỗi ngớ ngẩn thế này, ấm ức không chịu nổi. Không đời nào tôi mắc lại sai lầm tương tự lần thứ hai nữa đâu!",
        "explanation_vi": "～ものか đặt cuối câu với động từ KHẲNG ĐỊNH Vる mang nghĩa PHỦ ĐỊNH QUYẾT LIỆT ('không đời nào làm thế nữa!') -> するものか.",
        "option_diagnostics": [
            "[ĐÚNG - Vる + ものか = Quyết không đời nào làm V]: 二度と同じ失敗をするものか.",
            "[SAI - Lỗi phủ định kép ngược nghĩa]: *しないものか lại thành 'không đời nào không làm (= nhất định sẽ mắc lỗi lại)'!",
            "[SAI - Sai thì tương lai quyết tâm]: 二度と (lần nữa ở tương lai) không đi với thì quá khứ した.",
            "[SAI - Sai hình thái]: Thể ý chí しよう không gắn trước ものか.",
        ],
    },
    # --- GP-N3-069 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-069-C",
        "grammar_code": "GP-N3-069",
        "drill_type": "contrast",
        "prompt_jp": "もし100万円自由に使える（　　）、あなたは何に使いますか。",
        "options": ["としたら", "うちに", "とたんに", "せいで"],
        "correct_index": 0,
        "translation_vi": "Giả sử như bạn có thể tự do tiêu 1 triệu yên thì bạn sẽ dùng vào việc gì?",
        "explanation_vi": "Đặt giả thiết tưởng tượng hoàn toàn chưa có thật (もし100万円使える...) để hỏi ý kiến dùng [Vる + としたら].",
        "option_diagnostics": [
            "[ĐÚNG - Giả thiết tưởng tượng としたら]: もし ～ としたら.",
            "[SAI - Sai nghĩa 'trong lúc đang']: うちに chỉ hành động tranh thủ trong trạng thái hiện hữu thực tế, không đi với もし giả tưởng.",
            "[SAI - Sai thì và nghĩa tức thì]: とたんに đi sau Vた kể biến cố bất ngờ đã xảy ra.",
            "[SAI - Sai nghĩa đổ lỗi]: せいで không dùng đặt giả thiết tưởng tượng.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-069-A",
        "grammar_code": "GP-N3-069",
        "drill_type": "application",
        "prompt_jp": "ニュースの内容がすべて本当（　　）、来年から税金が大きく上がることになる。",
        "options": ["だとしたら", "なとしたら", "のとすれば", "だとたんに"],
        "correct_index": 0,
        "translation_vi": "Nếu giả sử toàn bộ nội dung bản tin đó là sự thật thì từ năm sau thuế sẽ tăng mạnh.",
        "explanation_vi": "Trước ～としたら / ～とすれば, danh từ/tính từ な phải giữ だ -> 本当だとしたら.",
        "option_diagnostics": [
            "[ĐÚNG - N/Aな + だ + としたら]: 本当だとしたら.",
            "[SAI - Nhầm sang な]: Trước としたら giữ dạng khẳng định ngắn だ, không dùng な.",
            "[SAI - Thừa の]: Không dùng *本当のとすれば.",
            "[SAI - Sai mẫu]: とたんに chỉ đi sau động từ quá khứ Vた.",
        ],
    },
    # --- GP-N3-070 (formation + application) ---
    {
        "drill_key": "DR-GP-N3-070-F",
        "grammar_code": "GP-N3-070",
        "drill_type": "formation",
        "prompt_jp": "子どもたちはスポーツ（　　）、協力することの大切さを学ぶことができる。",
        "options": ["を通して", "に通して", "を通じる", "に通じて"],
        "correct_index": 0,
        "translation_vi": "Thông qua thể thao, trẻ em có thể học được tầm quan trọng của sự hợp tác.",
        "explanation_vi": "Cấu trúc 'thông qua hoạt động/phương tiện N' cố định trợ từ を -> [N + を通して / を通じて].",
        "option_diagnostics": [
            "[ĐÚNG - Trợ từ を cố định + 通して]: スポーツを通して.",
            "[SAI - Sai trợ từ に]: 通す là tha động từ nên dùng trợ từ を, cấm dùng *に通して.",
            "[SAI - Dạng kết thúc câu nguyên thể]: Không dùng dạng nguyên thể *を通じる làm trạng ngữ giữa câu.",
            "[SAI - Sai trợ từ に]: Không dùng *に通じて thay cho を通じて.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-070-A",
        "grammar_code": "GP-N3-070",
        "drill_type": "application",
        "prompt_jp": "この地域は夏も冬も気温差が小さく、一年（　　）とても暮らしやすい。",
        "options": ["を通じて", "にとって", "に対して", "をめぐって"],
        "correct_index": 0,
        "translation_vi": "Khu vực này mùa hè lẫn mùa đông chênh lệch nhiệt độ nhỏ, rất dễ sống suốt cả một năm.",
        "explanation_vi": "Chỉ sự duy trì liên tục xuyên suốt chu kỳ thời gian trọn vẹn (一年) dùng N + を通じて.",
        "option_diagnostics": [
            "[ĐÚNG - Suốt khoảng thời gian trọn vẹn を通じて]: 一年を通じて = suốt cả năm.",
            "[SAI - Sai nghĩa lập trường]: 'Đối với một năm' không hợp nghĩa.",
            "[SAI - Sai nghĩa đối lập]: 'Trái ngược với một năm' vô nghĩa.",
            "[SAI - Sai nghĩa tranh cãi]: 'Xoay quanh một năm' không hợp câu mô tả khí hậu.",
        ],
    },
    # --- GP-N3-071 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-071-C",
        "grammar_code": "GP-N3-071",
        "drill_type": "contrast",
        "prompt_jp": "終電に乗り遅れてしまったし、タクシーもつかまらないので、歩いて帰る（　　）。",
        "options": ["ほかはない", "にすぎない", "わけではない", "ことがある"],
        "correct_index": 0,
        "translation_vi": "Lỡ chuyến tàu cuối rồi mà taxi cũng không bắt được nên đành phải đi bộ về chứ không còn cách nào khác.",
        "explanation_vi": "Bế tắc mọi phương án khác nên chỉ còn duy nhất một cách giải quyết dùng [Vる + ほかはない / しかない].",
        "option_diagnostics": [
            "[ĐÚNG - Giải pháp bất đắc dĩ duy nhất ほかはない]: 歩いて帰るほかはない.",
            "[SAI - Sai nghĩa 'chỉ là']: にすぎない hạ thấp mức độ chứ không nói 'không còn lựa chọn nào khác'.",
            "[SAI - Ngược nghĩa]: わけではない nghĩa là 'không hẳn là phải đi bộ về'.",
            "[SAI - Sai sắc thái tần suất]: ことがある chỉ việc thỉnh thoảng xảy ra, không thể hiện sự bất đắc dĩ ngay lúc lỡ tàu.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-071-A",
        "grammar_code": "GP-N3-071",
        "drill_type": "application",
        "prompt_jp": "どうしても修理できないほど壊れてしまったから、新しいパソコンを（　　）しかない。",
        "options": ["買う", "買わない", "買った", "買って"],
        "correct_index": 0,
        "translation_vi": "Vì hỏng nặng tới mức không tài nào sửa được nên chẳng còn cách nào khác là phải mua máy tính mới.",
        "explanation_vi": "Trước ～しかない luôn dùng động từ thể từ điển Vる (tuyệt đối không chia phủ định Vない như ～わけにはいかない).",
        "option_diagnostics": [
            "[ĐÚNG - Vる + しかない]: 買うしかない = đành phải mua mới.",
            "[SAI - Nhầm với ～ないわけにはいかない]: Vない + しかない tạo nghĩa phủ định kép sai ('đành phải không mua').",
            "[SAI - Sai thì quá khứ]: Không dùng quá khứ Vた trước しかない.",
            "[SAI - Sai dạng thể て]: Không dùng Vて trước しかない.",
        ],
    },
    # --- GP-N3-072 (formation + application) ---
    {
        "drill_key": "DR-GP-N3-072-F",
        "grammar_code": "GP-N3-072",
        "drill_type": "formation",
        "prompt_jp": "お世話になった先生に、感謝の気持ち（　　）手紙を書いた。",
        "options": ["をこめて", "をこめた", "にこめて", "でこめて"],
        "correct_index": 0,
        "translation_vi": "Tôi đã viết thư gửi gắm trọn vẹn lòng biết ơn tới người thầy đã giúp đỡ mình.",
        "explanation_vi": "Nối sang động từ 書いた (đã viết với tâm tình...) phải dùng dạng thể て -> をこめて (còn bổ nghĩa trực tiếp cho danh từ mới dùng をこめた).",
        "option_diagnostics": [
            "[ĐÚNG - N(tình cảm) + をこめて + Động từ]: 感謝の気持ちをこめて書いた.",
            "[SAI - Sai vị trí bổ nghĩa]: Nếu đặt trước 手紙 theo kiểu [感謝の気持ちをこめた手紙] thì câu thiếu trợ từ hoặc nối trực tiếp vào 手紙, không đứng tách như trạng ngữ chỉ cách thức ở đây (hoặc cẩn thận: 手紙 ở đây là tân ngữ đứng ngay sau chỗ trống? Khoan: 感謝の気持ちをこめて + 手紙を書いた dùng をこめて tự nhiên hơn nhiều vì 手紙を書いた là cụm hành động).",
            "[SAI - Sai trợ từ に]: Động từ 込める nhận tình cảm bằng tân ngữ を, không dùng *にこめて.",
            "[SAI - Sai trợ từ で]: Không dùng *でこめて.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-072-A",
        "grammar_code": "GP-N3-072",
        "drill_type": "application",
        "prompt_jp": "母の日に、日頃の（　　）をこめた花束を贈った。",
        "options": ["感謝", "値段", "病院", "道具"],
        "correct_index": 0,
        "translation_vi": "Vào Ngày của Mẹ, tôi đã tặng bó hoa chứa đựng trọn vẹn lòng biết ơn hằng ngày.",
        "explanation_vi": "～をこめる chỉ kết hợp với danh từ biểu thị TÌNH CẢM, TÂM NGUYỆN (感謝, 愛, 願い, 心).",
        "option_diagnostics": [
            "[ĐÚNG - Danh từ tâm tình + をこめた]: 感謝をこめた花束.",
            "[SAI - Danh từ vật chất/con số]: Không nói 'gửi gắm giá tiền' (*値段をこめた).",
            "[SAI - Danh từ địa điểm]: Không gửi gắm 'bệnh viện' vào bó hoa.",
            "[SAI - Danh từ đồ vật cụ thể]: Không gửi gắm 'dụng cụ' vào bó hoa.",
        ],
    },
    # --- GP-N3-073 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-073-C",
        "grammar_code": "GP-N3-073",
        "drill_type": "contrast",
        "prompt_jp": "昨夜は疲れていて、部屋の電気を（　　）眠ってしまった。",
        "options": ["つけたてで", "つけっぱなしで", "つけかけで", "つけておいて"],
        "correct_index": 1,
        "translation_vi": "Tối qua mệt quá nên tôi cứ để nguyên đèn phòng bật sáng như vậy rồi ngủ thiếp đi mất.",
        "explanation_vi": "Bỏ mặc trạng thái không tắt đèn (sự sơ suất gây lãng phí/bất ổn) dùng [Vます + っぱなしで].",
        "option_diagnostics": [
            "[SAI - Dùng たて sai vật thể và nghĩa]: たて chỉ dùng cho đồ ăn/sản phẩm vừa làm ra còn mới (như 炊きたてのごはん), không gắn với bật đèn.",
            "[ĐÚNG - Để nguyên trạng thái sơ suất Vます+っぱなし]: つける -> つけっぱなしで.",
            "[SAI - Sai nghĩa 'đang bật dở']: Bật công tắc là hành động tức thời, không dùng つけかけ.",
            "[SAI - Sai chủ ý tích cực]: ておいて là cố tình bật sẵn đèn để chuẩn bị cho việc gì, mâu thuẫn với ngữ cảnh ngủ thiếp đi do mệt (眠ってしまった).",
        ],
    },
    {
        "drill_key": "DR-GP-N3-073-A",
        "grammar_code": "GP-N3-073",
        "drill_type": "application",
        "prompt_jp": "寒いから、玄関のドアを（　　）にしないで、ちゃんと閉めてください。",
        "options": ["開けっぱなし", "開けたて", "開けきり", "開けがち"],
        "correct_index": 0,
        "translation_vi": "Trời lạnh nên đừng có để cửa ra vào mở toang nguyên như thế, hãy đóng đàng hoàng lại đi.",
        "explanation_vi": "Trách móc việc mở cửa xong không chịu đóng dùng 開ける -> 開けっぱなしにする.",
        "option_diagnostics": [
            "[ĐÚNG - 開けっぱなしにする]: Để nguyên trạng thái mở không đóng.",
            "[SAI - Sai mẫu]: たて không dùng cho hành động mở cửa bỏ mặc.",
            "[SAI - Sai nghĩa 'mở hết sạch']: きり không ghép với しないで thành mẫu trách móc giữ nguyên trạng thái.",
            "[SAI - Sai nghĩa xu hướng]: がち là hay có xu hướng xấu, không hợp cụm 'mở toang cửa không đóng'.",
        ],
    },
    # --- GP-N3-074 (formation + application) ---
    {
        "drill_key": "DR-GP-N3-074-F",
        "grammar_code": "GP-N3-074",
        "drill_type": "formation",
        "prompt_jp": "弟は朝「ちょっとコンビニへ行ってくる」と（　　）、夕方になっても帰ってこない。",
        "options": ["行くきり", "行ったきり", "行ってきり", "行っきりで"],
        "correct_index": 1,
        "translation_vi": "Em trai tôi từ sáng nói 'đi cửa hàng tiện lợi một chút' rồi đi biệt từ lúc đó tới chiều tối vẫn chưa thấy về.",
        "explanation_vi": "Diễn tả 'kể từ khi làm V lần đó thì bặt tin không quay lại / không có biến chuyển gì thêm' dùng [Vた + きり] -> 行ったきり.",
        "option_diagnostics": [
            "[SAI - Sai thì nguyên thể Vる]: Không dùng Vる trước きり trong nghĩa 'kể từ lúc đó... vẫn chưa'.",
            "[ĐÚNG - Vた + きり]: 行ったきり + 帰ってこない.",
            "[SAI - Sai dạng thể て]: Thể て không đứng trước きり.",
            "[SAI - Lỗi ghép xúc âm sai]: っきりで chỉ dùng sau danh từ số lượng (như 2人っきりで), không cắt động từ thành *行っきりで.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-074-A",
        "grammar_code": "GP-N3-074",
        "drill_type": "application",
        "prompt_jp": "普段は忙しいので、今日は久しぶりに家族（　　）でゆっくり食事をしたい。",
        "options": ["っきり", "ながら", "ばかりに", "なりに"],
        "correct_index": 0,
        "translation_vi": "Bình thường bận rộn nên hôm nay lâu lắm rồi tôi muốn ăn uống thong thả chỉ riêng với gia đình thôi.",
        "explanation_vi": "Giới hạn 'chỉ riêng bao nhiêu đó thôi' sau danh từ/số người dùng N + っきり + で.",
        "option_diagnostics": [
            "[ĐÚNG - Giới hạn chỉ riêng っきり]: 家族っきりで = chỉ riêng gia đình với nhau.",
            "[SAI - Sai nghĩa 'tuy rằng']: ながら nối Vます hoặc tính từ nhượng bộ, không gắn với 家族.",
            "[SAI - Sai sắc thái đổ lỗi]: ばかりに là 'chỉ tại vì...'.",
            "[SAI - Sai nghĩa 'theo cách riêng của']: なりに không khớp ngữ cảnh quây quần riêng tư.",
        ],
    },
    # --- GP-N3-075 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-075-F",
        "grammar_code": "GP-N3-075",
        "drill_type": "formation",
        "prompt_jp": "彼は本当は答えを知っているのに、（　　）ふりをしている。",
        "options": ["知らない", "知らなくて", "知らないな", "知らぬの"],
        "correct_index": 0,
        "translation_vi": "Anh ta thực ra biết câu trả lời nhưng cứ giả vờ như không biết.",
        "explanation_vi": "Trước ～ふりをする, động từ chia thể thông thường 普通形 trực tiếp -> 知らないふりをしている.",
        "option_diagnostics": [
            "[ĐÚNG - V普通形 + ふりをする]: 知らないふり.",
            "[SAI - Sai dạng thể て]: Thể て không bổ nghĩa cho danh từ ふり.",
            "[SAI - Lỗi thêm な sau động từ phủ định ない]: ない là đuôi phủ định của động từ nên không thêm な trước danh từ ふり.",
            "[SAI - Thừa の cổ ngữ]: Không viết *知らぬのふり.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-075-C",
        "grammar_code": "GP-N3-075",
        "drill_type": "contrast",
        "prompt_jp": "廊下で嫌いな先輩とすれ違ったとき、気づかない（　　）通り過ぎた。",
        "options": ["ふりをして", "せいにして", "つもりになって", "とおりにして"],
        "correct_index": 0,
        "translation_vi": "Khi lướt qua người đàn anh mình ghét ở hành lang, tôi đã giả vờ như không nhận ra rồi đi thẳng qua.",
        "explanation_vi": "Cố tình làm ra vẻ không thấy dù thực tế biết rõ -> Vない + ふりをして.",
        "option_diagnostics": [
            "[ĐÚNG - Giả bộ có chủ ý ふりをして]: 気づかないふりをして.",
            "[SAI - Sai nghĩa 'đổ lỗi cho']: せいにして nghĩa là 'đổ tội cho việc không nhận ra'.",
            "[SAI - Sai nghĩa 'cứ đinh ninh / nhập tâm thành']: つもりになって là tự tưởng tượng mình là ai đó, không hợp hành vi giả vờ né mặt.",
            "[SAI - Sai nghĩa]: とおりにして là 'làm đúng theo như không nhận ra', vô nghĩa.",
        ],
    },
    # --- GP-N3-076 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-076-C",
        "grammar_code": "GP-N3-076",
        "drill_type": "contrast",
        "prompt_jp": "彼はまだ一度も自分で料理を作ったことがない（　　）、人の料理に文句ばかり言う。",
        "options": ["おかげで", "くせに", "ために", "とおりに"],
        "correct_index": 1,
        "translation_vi": "Anh ta chưa tự mình nấu ăn lấy một lần nào, vậy mà suốt ngày chỉ biết chê bai món ăn của người khác.",
        "explanation_vi": "Chỉ trích, bực mình trước hành vi mâu thuẫn đáng chê của một người dùng 普通形 + くせに.",
        "option_diagnostics": [
            "[SAI - Sai nghĩa biết ơn]: Không thể cảm ơn việc anh ta suốt ngày càm ràm bằng おかげで.",
            "[ĐÚNG - Mâu thuẫn đáng chê trách của con người くせに]: 作っったことがないくせに + 文句ばかり言う.",
            "[SAI - Sai quan hệ mục đích/nguyên nhân]: Không dùng ために để bày tỏ sự bất mãn kiểu 'vậy mà lại...'.",
            "[SAI - Sai nghĩa 'theo đúng như']: Không hợp mạch đối lập.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-076-A",
        "grammar_code": "GP-N3-076",
        "drill_type": "application",
        "prompt_jp": "お父さんは医者から禁煙しろと言われている（　　）、隠れてタバコを吸っている。",
        "options": ["くせに", "ためか", "はずで", "うちに"],
        "correct_index": 0,
        "translation_vi": "Bố bị bác sĩ bảo bỏ thuốc rồi, vậy mà vẫn lén lút hút thuốc.",
        "explanation_vi": "Nhắc nhở mỉa mai/trách nhẹ hành động lén hút thuốc trái lời bác sĩ dùng Vている + くせに.",
        "option_diagnostics": [
            "[ĐÚNG - Phê phán hành vi trái ngược くせに]: 言われているくせに + 隠れて吸っている.",
            "[SAI - Sai nghĩa suy đoán nguyên nhân]: ためか nghĩa là 'có lẽ vì...'.",
            "[SAI - Sai nghĩa và cấu trúc]: *はずで không nối 2 vế đối lập.",
            "[SAI - Sai nghĩa 'trong lúc đang']: Không hợp hành vi lén lút trái lời khuyên.",
        ],
    },
    # --- GP-N3-077 (formation + application) ---
    {
        "drill_key": "DR-GP-N3-077-F",
        "grammar_code": "GP-N3-077",
        "drill_type": "formation",
        "prompt_jp": "このお店はランチ（　　）、夜のコース料理もとても評判がいい。",
        "options": ["はもちろん", "のもちろん", "がもちろん", "に물론"],
        "correct_index": 0,
        "translation_vi": "Quán này bữa trưa thì đương nhiên ngon rồi, mà thực đơn tối cũng rất được khen ngợi.",
        "explanation_vi": "Cấu trúc 'N1 là hiển nhiên rồi, mà N2 cũng...' cố định là [N1 + はもちろん、N2 + も].",
        "option_diagnostics": [
            "[ĐÚNG - N1 + はもちろん、N2 + も]: ランチはもちろん.",
            "[SAI - Sai trợ từ の]: Không dùng *のもちろん.",
            "[SAI - Sai trợ từ が]: Chủ đề so sánh mở rộng phải dùng trợ từ は -> はもちろん.",
            "[SAI - Ký tự không hợp lệ]: Không dùng chữ ngoài tiếng Nhật trong cấu trúc.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-077-A",
        "grammar_code": "GP-N3-077",
        "drill_type": "application",
        "prompt_jp": "同じところに続けて使用しないでください。（　　）、顔は2週間以内にしてください。",
        "options": ["もちろん", "たとえば", "つまり", "それとも"],
        "correct_index": 1,
        "translation_vi": "Đừng sử dụng liên tục ở cùng một vị trí. Ví dụ như, vùng mặt hãy dùng trong vòng 2 tuần trở lại.",
        "explanation_vi": "Câu sau nêu con số minh họa cụ thể (vùng mặt 2 tuần) cho quy tắc chung ở câu trước -> chọn たとえば (loại もちろん vì đó không phải điều hiển nhiên ai cũng tự biết) (Q#146).",
        "option_diagnostics": [
            "[SAI - Nhầm điều hiển nhiên với ví dụ minh họa]: Con số '2 tuần cho mặt' là quy định cụ thể của loại thuốc chứ không phải chân lý hiển nhiên (もちろん).",
            "[ĐÚNG - Liên từ đưa ví dụ minh họa たとえば]: Khớp hoàn toàn câu sau (Q#146).",
            "[SAI - Nhầm sang đúc kết/tóm tắt]: つまり dùng để định nghĩa lại ý chung, không dùng khi chuyển từ tổng quát sang chi tiết 1 bộ phận.",
            "[SAI - Sai loại câu]: それとも chỉ dùng trong câu hỏi lựa chọn 'A hay là B'.",
        ],
    },
    # --- GP-N3-078 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-078-F",
        "grammar_code": "GP-N3-078",
        "drill_type": "formation",
        "prompt_jp": "最近は夏の暑さ対策として、新しく「緑のカーテン」が（　　）始めている。",
        "options": ["使われて", "使われ", "使う", "使われる"],
        "correct_index": 1,
        "translation_vi": "Gần đây như một biện pháp chống nóng mùa hè, 'rèm xanh' đang bắt đầu được sử dụng.",
        "explanation_vi": "Chủ ngữ là '緑のカーテンが' -> chia Bị động 使われる -> bỏ る thành gốc Vます là 使われ + 始めている (Passage 18).",
        "option_diagnostics": [
            "[SAI - Lỗi gắn 始める sau thể て]: Hậu tố 始める phải gắn vào Vます bỏ ます, cấm gắn sau thể て (*使われて始めている).",
            "[ĐÚNG - Bị động Vます + 始める]: 使われる -> 使われ + 始めている.",
            "[SAI - Dùng nguyên thể chủ động Vる]: Không gắn 始める sau Vる và rèm xanh không tự mình sử dụng cái gì.",
            "[SAI - Dùng nguyên thể Vる bị động]: Không giữ る của 使われる trước 始める.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-078-C",
        "grammar_code": "GP-N3-078",
        "drill_type": "contrast",
        "prompt_jp": "「外国人に負けないようにしよう」と思って無理に努力（　　）、つらくなることもあるだろう。",
        "options": ["し続けたら", "して続けたら", "し始めたら", "し終わったら"],
        "correct_index": 0,
        "translation_vi": "Nếu cứ gồng mình tiếp tục nỗ lực với suy nghĩ 'không được thua người nước ngoài' thì cũng có lúc mệt mỏi đấy.",
        "explanation_vi": "Tiếp tục gồng mình suốt thời gian dài dùng Vます + 続ける -> 努力し続けたら (Passage 19).",
        "option_diagnostics": [
            "[ĐÚNG - Vます + 続ける + たら]: 努力する -> 努力し + 続けたら.",
            "[SAI - Lỗi ghép 続ける sau thể て]: Tuyệt đối không gắn 続ける sau thể て (*して続けたら).",
            "[SAI - Sai nghĩa vừa mới bắt đầu]: Mới bắt đầu nỗ lực thì chưa dẫn ngay tới kiệt sức như gồng mình kéo dài (続ける).",
            "[SAI - Sai nghĩa hoàn tất]: 終わったら nghĩa là 'sau khi nỗ lực xong rồi'.",
        ],
    },
    # --- GP-N3-079 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-079-C",
        "grammar_code": "GP-N3-079",
        "drill_type": "contrast",
        "prompt_jp": "親元を離れて一人暮らしを（　　）、両親のありがたさが身にしみてわかった。",
        "options": ["してからでないと", "して初めて", "するうちに", "するたびに"],
        "correct_index": 1,
        "translation_vi": "Chỉ từ khi rời xa bố mẹ sống một mình rồi, tôi mới thấm thía nhận ra công ơn của bố mẹ.",
        "explanation_vi": "Kể lại bước ngoặt trải nghiệm trong quá khứ lần đầu giúp mình nhận ra giá trị -> Vて + 初めて.",
        "option_diagnostics": [
            "[SAI - Vế sau khẳng định quá khứ]: てからでないと dùng cho điều kiện tương lai với vế sau phủ định/không thể, không đi với わかった (đã hiểu ra).",
            "[ĐÚNG - Trải nghiệm dẫn tới nhận thức mới Vて + 初めて]: 一人暮らしをして初めてわかった.",
            "[SAI - Sai nghĩa 'trong lúc đang']: うちに chỉ sự việc nảy sinh ngẫu nhiên trong lúc đang làm A, không nhấn mạnh mốc 'lần đầu mới vỡ lẽ sau khi trải qua'.",
            "[SAI - Sai nghĩa lặp lại nhiều lần]: Tự lập sống một mình là bước ngoặt chuyển giai đoạn chứ không phải hành động lặp đi lặp lại nhiều lần.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-079-A",
        "grammar_code": "GP-N3-079",
        "drill_type": "application",
        "prompt_jp": "実際に大きな病気を（　　）、毎日の健康管理の大切さに気がついた。",
        "options": ["してみて初めて", "するばかりで", "したせいで", "してばかりいて"],
        "correct_index": 0,
        "translation_vi": "Chỉ sau khi thực sự mắc bệnh nặng một lần rồi tôi mới nhận ra tầm quan trọng của việc giữ gìn sức khỏe hằng ngày.",
        "explanation_vi": "Nhận ra bài học quý giá sau khi trải qua biến cố dùng Vて + 初めて.",
        "option_diagnostics": [
            "[ĐÚNG - Vて + 初めて + 気がついた]: Trải nghiệm -> giác ngộ.",
            "[SAI - Sai nghĩa nguyên nhân than vãn]: ばかりで không diễn tả ý 'chỉ sau khi trải qua mới lần đầu nhận ra'.",
            "[SAI - Sai sắc thái kết quả tích cực]: Nhận ra tầm quan trọng của sức khỏe là bài học tốt, không dùng せいで.",
            "[SAI - Sai logic 'suốt ngày chỉ toàn bị bệnh']: Không tự nhiên trong ngữ cảnh bước ngoặt nhận thức.",
        ],
    },
    # --- GP-N3-080 (formation + application) ---
    {
        "drill_key": "DR-GP-N3-080-F",
        "grammar_code": "GP-N3-080",
        "drill_type": "formation",
        "prompt_jp": "この動物園には、パンダ（　　）、世界中の珍しい動物がたくさんいる。",
        "options": ["をはじめ", "をはじめに", "がはじめ", "にはじめ"],
        "correct_index": 0,
        "translation_vi": "Ở sở thú này có rất nhiều loài động vật quý hiếm trên thế giới, mà trước tiên phải kể đến là gấu trúc.",
        "explanation_vi": "Đưa một đại diện nổi bật nhất đứng đầu tập hợp dùng [N + をはじめ / をはじめとして] (không dùng *をはじめに).",
        "option_diagnostics": [
            "[ĐÚNG - N(đại diện #1) + をはじめ]: パンダをはじめ.",
            "[SAI - Lỗi ghép に]: *をはじめに nghĩa là 'để mở đầu lời phát biểu (lời nói đầu)', không dùng nối ví dụ đại diện.",
            "[SAI - Sai trợ từ が]: Bắt buộc dùng trợ từ を trước はじめ.",
            "[SAI - Sai trợ từ に]: Bắt buộc dùng を, không dùng *にはじめ.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-080-A",
        "grammar_code": "GP-N3-080",
        "drill_type": "application",
        "prompt_jp": "日本の春は、（　　）をはじめとする美しい花や新緑の季節だ。",
        "options": ["桜", "桜や梅や桃", "雑草", "枯れ葉"],
        "correct_index": 0,
        "translation_vi": "Mùa xuân Nhật Bản là mùa của các loài hoa đẹp và chồi non, mà trước tiên phải kể đến là hoa anh đào.",
        "explanation_vi": "～をはじめとする chọn MỘT đại diện tiêu biểu, nổi tiếng nhất của mùa xuân Nhật Bản (桜) đứng đầu.",
        "option_diagnostics": [
            "[ĐÚNG - Một đại diện tiêu biểu hàng đầu + をはじめとする]: 桜 là biểu tượng số 1 của mùa xuân Nhật Bản.",
            "[SAI - Liệt kê hàng loạt thay vì chọn 1 đầu tàu]: Nhóm nhiều ví dụ ngang hàng dùng といった; をはじめ chọn 1 đại diện số 1.",
            "[SAI - Sai nghĩa 'cỏ dại']: Cỏ dại không phải đại diện cho 'hoa đẹp'.",
            "[SAI - Sai mùa và nghĩa 'lá khô rụng']: Lá khô là đặc trưng mùa thu/đông, không phải mùa xuân.",
        ],
    },
    # --- GP-N3-081 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-081-F",
        "grammar_code": "GP-N3-081",
        "drill_type": "formation",
        "prompt_jp": "テーブルの上に（　　）のコーヒーが置いてあるから、捨てないでね。",
        "options": ["飲みかけ", "飲むかけ", "飲んでかけ", "飲んだかけ"],
        "correct_index": 0,
        "translation_vi": "Trên bàn có ly cà phê đang uống dở đấy, đừng đổ đi nhé.",
        "explanation_vi": "Hậu tố ～かけ (đang làm dở) BẮT BUỘC gắn vào Vます bỏ ます -> 飲む -> 飲みかけ.",
        "option_diagnostics": [
            "[ĐÚNG - Vます(bỏ ます) + かけ + の + N]: 飲みかけのコーヒー.",
            "[SAI - Gắn sau Vる]: Không gắn かけ vào nguyên thể *飲むかけ.",
            "[SAI - Gắn sau thể て]: Không gắn かけ vào thể て *飲んでかけ.",
            "[SAI - Gắn sau thể た]: Không gắn かけ vào quá khứ *飲んだかけ.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-081-C",
        "grammar_code": "GP-N3-081",
        "drill_type": "contrast",
        "prompt_jp": "まだ半分しか読んでいない（　　）の本をカバンにしまった。",
        "options": ["読みたて", "読みかけ", "読みきり", "読みっぱなし"],
        "correct_index": 1,
        "translation_vi": "Tôi cất cuốn sách đang đọc dở (mới đọc được có một nửa) vào trong cặp.",
        "explanation_vi": "Thông tin gợi ý 'mới đọc được có một nửa' (半分しか読んでいない) -> đang đọc dở dang -> 読みかけ.",
        "option_diagnostics": [
            "[SAI - Sai nghĩa]: 読みたて không dùng rộng rãi và mang nghĩa 'vừa mới đọc xong hết tức thì', trái với 'mới đọc được một nửa'.",
            "[ĐÚNG - Đang làm dở nửa chừng 読みかけ]: Khớp hoàn toàn với 半分しか読んでいない.",
            "[SAI - Ngược nghĩa 'đọc hết sạch']: 読みきり là đã đọc hết trọn vẹn.",
            "[SAI - Sai nghĩa bỏ mặc]: 読みっぱなし là đọc xong vứt bừa không dọn, mâu thuẫn với việc cất vào cặp.",
        ],
    },
    # --- GP-N3-082 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-082-C",
        "grammar_code": "GP-N3-082",
        "drill_type": "contrast",
        "prompt_jp": "母はいつも家族には、今まさに炊き上がった（　　）のごはんを食べさせたいと言っている。",
        "options": ["炊きかけ", "炊きたて", "炊きっぱなし", "炊いたとたん"],
        "correct_index": 1,
        "translation_vi": "Mẹ lúc nào cũng muốn cho gia đình ăn cơm vừa mới nấu chín xong tức thì.",
        "explanation_vi": "Gợi ý '今まさに炊き上がった' (vừa mới nấu xong ngay lúc này) -> chốt tính tươi mới/nóng hổi bằng Vます + たて -> 炊きたて (Q#51).",
        "option_diagnostics": [
            "[SAI - Ngược nghĩa chưa chín]: 炊きかけ nghĩa là đang nấu dở chưa chín.",
            "[ĐÚNG - Vừa làm xong nóng hổi 炊きたて]: 炊きたてのごはん (Q#51).",
            "[SAI - Chê cẩu thả]: 炊きっぱなし là nấu xong bỏ mặc đó không dọn.",
            "[SAI - Sai cấu trúc bổ nghĩa danh từ]: Không đặt *炊いたとたん trực tiếp trước のごはん.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-082-A",
        "grammar_code": "GP-N3-082",
        "drill_type": "application",
        "prompt_jp": "このパン屋では、毎朝7時に（　　）のクロワッサンを買うことができる。",
        "options": ["焼きたて", "焼きかけ", "焼きっぱなし", "焼きがち"],
        "correct_index": 0,
        "translation_vi": "Ở tiệm bánh này, mỗi sáng lúc 7 giờ bạn có thể mua được bánh sừng bò vừa mới nướng xong nóng hổi.",
        "explanation_vi": "Bánh vừa mới ra lò còn nóng giòn -> 焼きたてのクロワッサン.",
        "option_diagnostics": [
            "[ĐÚNG - Sản phẩm mới ra lò 焼きたて]: 焼く -> 焼き + たて.",
            "[SAI - Ngược nghĩa]: 焼きかけ là bánh đang nướng dở còn sống bột.",
            "[SAI - Sai nghĩa chê trách]: 焼きっぱなし là nướng bỏ quên.",
            "[SAI - Sai ngữ nghĩa]: 焼きがち là 'hay có xu hướng nướng (xấu)'.",
        ],
    },
    # --- GP-N3-083 (formation + application) ---
    {
        "drill_key": "DR-GP-N3-083-F",
        "grammar_code": "GP-N3-083",
        "drill_type": "formation",
        "prompt_jp": "おいしい料理が（　　）ので、冷めないうちにみんなで食べましょう。",
        "options": ["できあがった", "できあげた", "できかけ", "でききった"],
        "correct_index": 0,
        "translation_vi": "Món ăn ngon đã nấu xong xuôi rồi, chúng ta cùng ăn trong lúc còn chưa nguội nhé.",
        "explanation_vi": "Chủ ngữ là 料理が (tự động từ) nên dùng 出来上がる -> できあがった (Q#138).",
        "option_diagnostics": [
            "[ĐÚNG - Tự động từ hoàn thành 出来上がる]: 料理が + できあがった.",
            "[SAI - Dùng tha động từ với trợ từ が]: 上げる là tha động từ (cần tân ngữ を), sai với chủ ngữ 料理が.",
            "[SAI - Ngược nghĩa chưa nấu xong]: できかけ là làm dở dang, mâu thuẫn với 'mời cùng ăn'.",
            "[SAI - Sai kết hợp từ]: Không ghép *でききった thay cho できあがった.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-083-A",
        "grammar_code": "GP-N3-083",
        "drill_type": "application",
        "prompt_jp": "一週間かかって、ようやく卒業論文を（　　）ことができた。",
        "options": ["書き上げる", "書き上がる", "書きかける", "書き出す"],
        "correct_index": 0,
        "translation_vi": "Mất suốt một tuần, cuối cùng tôi cũng đã hoàn thành viết xong xuôi luận văn tốt nghiệp.",
        "explanation_vi": "Tân ngữ đi với trợ từ を (卒業論文を) nên phải chọn Tha động từ 書き上げる.",
        "option_diagnostics": [
            "[ĐÚNG - Tha động từ hoàn thiện sản phẩm 書き上げる]: 卒業論文を + 書き上げる.",
            "[SAI - Dùng tự động từ với tân ngữ を]: 書き上がる đi với 論文が, không đi với 論文を.",
            "[SAI - Ngược nghĩa với 'ようやく']: Mới bắt đầu viết dở thì không dùng 'cuối cùng mất 1 tuần cũng...'.",
            "[SAI - Sai nghĩa 'mới bắt đầu viết']: 書き出す là bắt đầu viết, trái với hoàn tất luận văn sau 1 tuần.",
        ],
    },
    # --- GP-N3-084 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-084-C",
        "grammar_code": "GP-N3-084",
        "drill_type": "contrast",
        "prompt_jp": "こんなにたくさんのごちそう、とても一人では（　　）。",
        "options": ["食べきれません", "食べかけません", "食べにくいです", "食べがちです"],
        "correct_index": 0,
        "translation_vi": "Nhiều món ngon thế này thì một mình tôi tuyệt đối không thể ăn hết xuể được.",
        "explanation_vi": "Không đủ sức hoàn thành hết toàn bộ số lượng thức ăn quá lớn dùng [Vます + きれない] -> 食べきれません.",
        "option_diagnostics": [
            "[ĐÚNG - Không hoàn thành hết số lượng 食べきれません]: 食べる -> 食べきれない.",
            "[SAI - Không chia phủ định *かけません]: Không dùng *食べかけません cho nghĩa không ăn hết.",
            "[SAI - Sai sắc thái]: 食べにくい là 'khó ăn' (do vị cay/cứng/xương), không nói về khối lượng quá nhiều ăn không hết.",
            "[SAI - Sai nghĩa]: 食べがち là 'hay có thói quen ăn (xấu)'.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-084-A",
        "grammar_code": "GP-N3-084",
        "drill_type": "application",
        "prompt_jp": "500ページもある分厚い小説を、彼はたった一日で（　　）。",
        "options": ["読みきった", "読みかけた", "読み出した", "読みっぽかった"],
        "correct_index": 0,
        "translation_vi": "Cuốn tiểu thuyết dày tận 500 trang mà anh ấy đã đọc hết sạch chỉ trong vỏn vẹn một ngày.",
        "explanation_vi": "Hoàn thành triệt để toàn bộ khối lượng lớn (500 trang) dùng Vます + きる -> 読みきった.",
        "option_diagnostics": [
            "[ĐÚNG - Hoàn thành trọn vẹn khối lượng lớn 読みきった]: Đọc hết sạch 500 trang.",
            "[SAI - Sai nghĩa]: 読みかけた nghĩa là mới đọc dở chưa xong.",
            "[SAI - Sai nghĩa]: 読み出した nghĩa là mới bắt đầu đọc.",
            "[SAI - Không tồn tại hình thái]: Không ghép *読みっぽかった.",
        ],
    },
    # --- GP-N3-085 (formation + application) ---
    {
        "drill_key": "DR-GP-N3-085-F",
        "grammar_code": "GP-N3-085",
        "drill_type": "formation",
        "prompt_jp": "家を出ようとしたとき、突然空が暗くなって大雨が（　　）。",
        "options": ["降り出した", "降る出した", "降り始めた", "降って出した"],
        "correct_index": 0,
        "translation_vi": "Đúng lúc định ra khỏi nhà, bầu trời đột ngột tối sầm lại rồi mưa lớn ập xuống.",
        "explanation_vi": "Hành động thiên nhiên bộc phát đột ngột ('突然') gắn vào Vます bỏ ます + 出す -> 降り出した.",
        "option_diagnostics": [
            "[ĐÚNG - Vます + 出す (Đột ngột phát sinh)]: 突然 + 降り出した.",
            "[SAI - Gắn sau Vる]: Không gắn 出す vào nguyên thể *降る出した.",
            "[SAI - Thiếu sắc thái đột ngột của 突然]: 降り始めた diễn tả quá trình tự nhiên từ từ, còn với phó từ đột ngột 突然 chuẩn xác nhất là 降り出した.",
            "[SAI - Gắn sau thể て]: Không gắn 出す vào sau thể て (*降って出した).",
        ],
    },
    {
        "drill_key": "DR-GP-N3-085-A",
        "grammar_code": "GP-N3-085",
        "drill_type": "application",
        "prompt_jp": "新しい旅行の計画を最初に（　　）のは、井上くんです。",
        "options": ["言い出した", "言い終わった", "言い通した", "言いきった"],
        "correct_index": 0,
        "translation_vi": "Người đầu tiên mở lời đề xuất kế hoạch du lịch mới là cậu Inoue.",
        "explanation_vi": "Khởi xướng ý kiến trước tiên (最初に) dùng 言い出す -> 言い出した (Q#97: 言い出した ＝ 一番先に言った).",
        "option_diagnostics": [
            "[ĐÚNG - Khởi xướng ý tưởng 言い出した]: Đứng cùng 最初に.",
            "[SAI - Ngược nghĩa]: 言い終わった nghĩa là 'nói xong xuôi', trái với người đề xuất đầu tiên.",
            "[SAI - Sai nghĩa]: 言い通した nghĩa là 'khăng khăng nói suốt không đổi ý'.",
            "[SAI - Sai nghĩa]: 言いきった nghĩa là 'khẳng định chắc nịch không chút do dự'.",
        ],
    },
    # --- GP-N3-086 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-086-C",
        "grammar_code": "GP-N3-086",
        "drill_type": "contrast",
        "prompt_jp": "どんなに厳しい質問をされても、彼は最後まで（　　）。",
        "options": ["黙り通した", "黙りかけた", "黙りがちだった", "黙りたてだった"],
        "correct_index": 0,
        "translation_vi": "Dù bị hỏi những câu hỏi gay gắt thế nào đi nữa, anh ta cũng giữ im lặng suốt từ đầu đến cuối.",
        "explanation_vi": "Duy trì một trạng thái không đổi xuyên suốt đến tận cuối (最後まで) dùng Vます + 通す -> 黙り通した.",
        "option_diagnostics": [
            "[ĐÚNG - Giữ nguyên suốt từ đầu đến cuối 黙り通した]: Đứng cùng 最後まで.",
            "[SAI - Sai nghĩa 'định im lặng nửa chừng']: 黙りかけた là suýt im hoặc mới im dở dang.",
            "[SAI - Sai nghĩa 'hay có xu hướng im']: 黙りがち chỉ thói quen lặp lại chung, không hợp một cuộc tra hỏi cụ thể tới 最後まで.",
            "[SAI - Sai mẫu]: たて không ghép với 黙る.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-086-A",
        "grammar_code": "GP-N3-086",
        "drill_type": "application",
        "prompt_jp": "途中で何度も諦めそうになったが、最後まで42キロのマラソンを（　　）。",
        "options": ["走り抜いた", "走りかけた", "走り出した", "走りっぱなしだ"],
        "correct_index": 0,
        "translation_vi": "Giữa chừng có lúc tưởng chừng muốn bỏ cuộc mấy lần, nhưng cuối cùng tôi đã kiên trì chạy xuyên suốt 42km marathon.",
        "explanation_vi": "Vượt qua thử thách gian nan để hoàn thành đến tận vạch đích dùng Vます + 抜く -> 走り抜いた.",
        "option_diagnostics": [
            "[ĐÚNG - Kiên trì vượt khó tới cùng 走り抜いた]: 最後まで + 走り抜いた.",
            "[SAI - Ngược kết quả bỏ dở]: 走りかけた nghĩa là mới chạy được một nửa rồi bỏ.",
            "[SAI - Ngược thời điểm]: 走り出した là mới xuất phát chạy, trái với 'đến cuối cùng'.",
            "[SAI - Sai nghĩa]: っぱなし mang ý chê trách bỏ mặc.",
        ],
    },
    # --- GP-N3-087 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-087-F",
        "grammar_code": "GP-N3-087",
        "drill_type": "formation",
        "prompt_jp": "忙しい毎日を送っていると、どうしても栄養が（　　）。",
        "options": ["不足しがちだ", "不足するがちだ", "不足してがちだ", "不足しただちだ"],
        "correct_index": 0,
        "translation_vi": "Khi sống những ngày bận rộn, chúng ta rất hay có xu hướng bị thiếu chất dinh dưỡng.",
        "explanation_vi": "Hậu tố ～がち gắn trực tiếp vào Danh từ (病気・留守) hoặc gốc Vます bỏ ます (する -> しがちだ) -> 不足しがちだ.",
        "option_diagnostics": [
            "[ĐÚNG - N/Vます + がちだ]: 不足する -> 不足し + がちだ (hoặc danh từ 不足がちだ).",
            "[SAI - Gắn sau Vる]: Không gắn がち vào sau Vる (*不足するがち).",
            "[SAI - Gắn sau thể て]: Không gắn がち vào sau thể て (*不足してがち).",
            "[SAI - Lỗi hình thái]: Không có mẫu *しただちだ.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-087-C",
        "grammar_code": "GP-N3-087",
        "drill_type": "contrast",
        "prompt_jp": "最近の天気は（　　）で、洗濯物がなかなか乾かない。",
        "options": ["曇りがち", "曇りたて", "曇りっぱなし", "曇りかけ"],
        "correct_index": 0,
        "translation_vi": "Thời tiết dạo này thường hay âm u nhiều mây nên đồ giặt mãi chẳng khô được.",
        "explanation_vi": "Xu hướng thời tiết hay lặp lại tình trạng tiêu cực (âm u, hay mưa) dùng [曇り + がち] (tính từ な -> 曇りがちで).",
        "option_diagnostics": [
            "[ĐÚNG - Xu hướng thời tiết xấu hay lặp lại 曇りがち]: 曇りがちで.",
            "[SAI - Sai mẫu]: たて chỉ dùng cho đồ ăn/vật phẩm mới làm ra.",
            "[SAI - Sai chủ thể hành động]: っぱなし chỉ gắn với hành động có chủ ý của người (quên đóng/quên tắt), không dùng cho mây trời.",
            "[SAI - Sai nghĩa]: 曇りかけ chỉ trạng thái bắt đầu chớm âm u ngay lúc này, không hợp 'dạo này mãi quần áo không khô'.",
        ],
    },
    # --- GP-N3-088 (formation + contrast + application) ---
    {
        "drill_key": "DR-GP-N3-088-F",
        "grammar_code": "GP-N3-088",
        "drill_type": "formation",
        "prompt_jp": "急いで書いたので、このレポートは漢字の（　　）だ。",
        "options": ["間違いだらけ", "間違ってだらけ", "間違えるだらけ", "間違いがち"],
        "correct_index": 0,
        "translation_vi": "Vì viết vội nên bản báo cáo này toàn là lỗi sai chữ Hán.",
        "explanation_vi": "～だらけ CHỈ gắn trực tiếp vào DANH TỪ chỉ thứ tiêu cực, dơ bẩn hoặc lỗi sai -> 間違い (danh từ) + だらけだ.",
        "option_diagnostics": [
            "[ĐÚNG - Danh từ lỗi sai + だらけ]: 間違いだらけだ.",
            "[SAI - Lỗi gắn だらけ sau thể て]: Tuyệt đối không gắn だらけ vào sau động từ thể て.",
            "[SAI - Lỗi gắn だらけ sau Vる]: Tuyệt đối không gắn だらけ vào sau động từ nguyên thể.",
            "[SAI - Nhầm hậu tố xu hướng]: Báo cáo trên giấy đang chứa đầy lỗi sai chứ không nói bản báo cáo có 'xu hướng hay mắc lỗi' (がち).",
        ],
    },
    {
        "drill_key": "DR-GP-N3-088-C",
        "grammar_code": "GP-N3-088",
        "drill_type": "contrast",
        "prompt_jp": "毎日サボって遊んで（　　）と、テストでいい点は取れませんよ。",
        "options": ["だらけだ", "ばかりいる", "のみだ", "続けている"],
        "correct_index": 1,
        "translation_vi": "Nếu ngày nào cũng trốn học suốt ngày chỉ toàn đi chơi thì không đạt điểm cao trong bài kiểm tra được đâu.",
        "explanation_vi": "Sau động từ chia thể て (遊んで) để phàn nàn thói quen lặp đi lặp lại dùng ばかりいる (loại だらけ vì だらけ chỉ đi với Danh từ) (Q#55).",
        "option_diagnostics": [
            "[SAI - Lỗi ghép だらけ sau Vて]: Sau 遊んで (động từ thể て) cấm tuyệt đối dùng だらけ!",
            "[ĐÚNG - Vて + ばかりいる]: 遊んでばかりいると.",
            "[SAI - Sai hình thái với Vて]: のみ chỉ đi với Vる hoặc danh từ.",
            "[SAI - Sai hình thái với Vて]: 続ける phải gắn vào Vます (遊び続けている), không gắn sau thể て.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-088-A",
        "grammar_code": "GP-N3-088",
        "drill_type": "application",
        "prompt_jp": "雨の中を走ったので、靴もズボンも（　　）になってしまった。",
        "options": ["泥だらけ", "笑顔だらけ", "お金だらけ", "親切だらけ"],
        "correct_index": 0,
        "translation_vi": "Vì chạy trong mưa nên cả giày lẫn quần đều dính đầy bùn đất mất rồi.",
        "explanation_vi": "～だらけ chỉ dùng cho các thứ DƠ BẨN, LỘN XỘN, GÂY KHÓ CHỊU (泥: bùn, ゴミ: rác, 傷: vết thương, ほこり: bụi).",
        "option_diagnostics": [
            "[ĐÚNG - Danh từ bẩn thỉu/tiêu cực + だらけ]: 泥だらけ = đầy bùn đất.",
            "[SAI - Sai sắc thái tích cực]: Không dùng だらけ cho những thứ vui vẻ/tốt đẹp như nụ cười (笑顔) hay tiền bạc.",
            "[SAI - Sai sắc thái tích cực]: Không nói *お金だらけ để khen giàu có.",
            "[SAI - Sai từ loại và sắc thái]: Không dùng *親切だらけ.",
        ],
    },
    # --- GP-N3-089 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-089-F",
        "grammar_code": "GP-N3-089",
        "drill_type": "formation",
        "prompt_jp": "月の表面にある（　　）模様が、ウサギのような形に見える。",
        "options": ["黒的な", "黒っぽい", "黒らしい", "黒みたいな"],
        "correct_index": 1,
        "translation_vi": "Những hoa văn hơi đen trên bề mặt mặt trăng trông giống hình dáng con thỏ.",
        "explanation_vi": "Khi diễn đạt 'hơi ngả sang màu đen', cắt đuôi い của 黒い thành gốc 黒 rồi gắn っぽい -> 黒っぽい模様 (Q#61).",
        "option_diagnostics": [
            "[SAI - Gắn 的 vào tính từ thuần Nhật]: 的な chỉ gắn vào danh từ Hán-Nhật, cấm gắn vào gốc tính từ *黒的な.",
            "[ĐÚNG - Aい(bỏ い) + っぽい]: 黒い -> 黒 + っぽい (Q#61).",
            "[SAI - Cắt đuôi い trước らしい]: らしい phải gắn sau tính từ đầy đủ (黒いらしい) hoặc danh từ (春らしい), không viết *黒らしい.",
            "[SAI - Cắt đuôi い trước みたい]: みたいな phải đi sau mệnh đề hoàn chỉnh (黒いみたいな), không ghép *黒みたいな.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-089-C",
        "grammar_code": "GP-N3-089",
        "drill_type": "contrast",
        "prompt_jp": "このスープは味が薄くて、少し（　　）からあまり美味しくない。",
        "options": ["水っぽい", "水らしい", "水だらけ", "水気味"],
        "correct_index": 0,
        "translation_vi": "Món súp này vị nhạt, hơi loãng nhiều nước quá nên chẳng ngon mấy.",
        "explanation_vi": "Chê món súp lỏng bỏng toàn nước dùng N + っぽい -> 水っぽい.",
        "option_diagnostics": [
            "[ĐÚNG - Chê mang tính chất nổi trội 水っぽい]: 水っぽい = loãng toẹt, toàn nước.",
            "[SAI - Ngược sắc thái khen đúng chất]: 水らしい nghĩa là 'ra dáng nước / đúng chất nước', không dùng để chê súp loãng.",
            "[SAI - Sai ngữ nghĩa bề mặt]: だらけ chỉ bề mặt bị phủ kín bởi vật thể rời (bùn/rác), không dùng cho súp loãng.",
            "[SAI - Sai cách dùng của 気味]: 気味 dùng cho triệu chứng sức khỏe/cảm giác cơ thể hoặc xu hướng tiến độ, không tả vị súp nhạt.",
        ],
    },
    # --- GP-N3-090 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-090-C",
        "grammar_code": "GP-N3-090",
        "drill_type": "contrast",
        "prompt_jp": "安全上の理由から、機内（　　）携帯電話の使用は禁止されています。",
        "options": ["に対して", "における", "にとって", "について"],
        "correct_index": 1,
        "translation_vi": "Vì lý do an toàn, việc sử dụng điện thoại di động trên khoang máy bay bị nghiêm cấm.",
        "explanation_vi": "Chỉ địa điểm/không gian trang trọng bổ nghĩa cho danh từ phía sau (機内 + ___ + 使用) dùng N1 + における + N2 (Q#56).",
        "option_diagnostics": [
            "[SAI - Sai dạng và nghĩa]: に対して là 'đối với' và không đứng trực tiếp bổ nghĩa danh từ thay に対する.",
            "[ĐÚNG - Địa điểm trang trọng bổ nghĩa danh từ における]: 機内における使用 (Q#56).",
            "[SAI - Sai dạng và nghĩa]: にとって là lập trường đánh giá, không chỉ nơi chốn thực hiện hành động.",
            "[SAI - Sai dạng và nghĩa]: について nghĩa là 'về chủ đề khoang máy bay' và thiếu の.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-090-A",
        "grammar_code": "GP-N3-090",
        "drill_type": "application",
        "prompt_jp": "日本の伝統文化（　　）、お茶や生け花は非常に重要な役割を果たしている。",
        "options": ["において", "によって", "にかけて", "を問わず"],
        "correct_index": 0,
        "translation_vi": "Trong văn hóa truyền thống Nhật Bản, trà đạo và nghệ thuật cắm hoa đóng vai trò vô cùng quan trọng.",
        "explanation_vi": "Chỉ phạm vi, lĩnh vực trang trọng trong văn viết ('trong lĩnh vực N') dùng N + において.",
        "option_diagnostics": [
            "[ĐÚNG - Lĩnh vực/Bối cảnh văn viết において]: 伝統文化において.",
            "[SAI - Sai nghĩa 'tùy theo/bởi']: Không diễn đạt được ý 'trong phạm vi nền văn hóa'.",
            "[SAI - Sai nghĩa thời gian/không gian từ A đến B]: にかけて đòi hỏi cặp から～にかけて.",
            "[SAI - Ngược nghĩa]: 'Bất kể văn hóa truyền thống' làm hỏng hoàn toàn ý câu.",
        ],
    },
    # --- GP-N3-091 (formation + application) ---
    {
        "drill_key": "DR-GP-N3-091-F",
        "grammar_code": "GP-N3-091",
        "drill_type": "formation",
        "prompt_jp": "どちらもいいホテルですが、駅の近さや便利さ（　　）Aホテルがおすすめです。",
        "options": ["からいうと", "と思えば", "によれば", "に対して"],
        "correct_index": 0,
        "translation_vi": "Cả hai đều là khách sạn tốt, nhưng xét về độ gần ga và tiện lợi thì khách sạn A đáng gợi ý hơn.",
        "explanation_vi": "Lấy một tiêu chí cụ thể làm cơ sở nhận xét gợi ý ở vế sau dùng [N + からいうと] (Q#54).",
        "option_diagnostics": [
            "[ĐÚNG - Tiêu chí đánh giá からいうと]: 便利さからいうと (Q#54).",
            "[SAI - Sai hình thái và nghĩa]: と思えば đi sau mệnh đề hoàn chỉnh ('vừa mới tưởng là...') để tả sự thay đổi bất ngờ.",
            "[SAI - Nhầm nguồn tin nghe nói]: 'Độ tiện lợi' không phải nguồn tin báo đài, và vế sau là gợi ý chủ quan chứ không phải truyền đạt そうだ.",
            "[SAI - Sai nghĩa đối lập/đối tượng]: に対して không mang nghĩa 'xét từ tiêu chí này thì chọn cái kia'.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-091-A",
        "grammar_code": "GP-N3-091",
        "drill_type": "application",
        "prompt_jp": "空の暗さや風の冷たさ（　　）、これからかなり強い雨が降りそうだ。",
        "options": ["からすると", "のおかげで", "のかわりに", "をはじめ"],
        "correct_index": 0,
        "translation_vi": "Xét từ vẻ tối sầm của bầu trời và cái lạnh của gió, có vẻ sắp mưa khá to rồi.",
        "explanation_vi": "Căn cứ vào dấu hiệu quan sát (空の暗さや風の冷たさ) để phán đoán ở vế sau dùng [N + からすると].",
        "option_diagnostics": [
            "[ĐÚNG - Phán đoán từ dấu hiệu N + からすると]: 暗さや冷たさからすると.",
            "[SAI - Sai nghĩa 'nhờ có']: Bầu trời tối không phải nguyên nhân đáng biết ơn để tạo ra mưa.",
            "[SAI - Sai nghĩa 'thay cho']: Không thể 'thay cho trời tối'.",
            "[SAI - Sai cấu trúc liệt kê]: Không nối ví dụ ở đây.",
        ],
    },
    # --- GP-N3-092 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-092-F",
        "grammar_code": "GP-N3-092",
        "drill_type": "formation",
        "prompt_jp": "このアルバイトは、年齢や性別（　　）やる気があれば誰でも応募できます。",
        "options": ["を問わず", "に問わず", "が問わず", "を問わずに"],
        "correct_index": 0,
        "translation_vi": "Công việc làm thêm này bất kể tuổi tác hay giới tính, hễ có nhiệt huyết là ai cũng ứng tuyển được.",
        "explanation_vi": "Động từ 問う (hỏi đến) nhận tân ngữ bằng trợ từ を và chia thể ず trang trọng thành [N + を問わず] (không thêm に).",
        "option_diagnostics": [
            "[ĐÚNG - Trợ từ を cố định + 問わず]: 年齢や性別を問わず.",
            "[SAI - Sai trợ từ に]: 問う đi với を, không dùng *に問わず.",
            "[SAI - Sai trợ từ が]: Chủ ngữ ở đây là người ứng tuyển chứ không dùng *が問わず.",
            "[SAI - Thừa に]: Mẫu chuẩn mực văn viết bỏ に để dùng trực tiếp を問わず (dù dạng ～を問わずに ít dùng và đề chuẩn dùng を問わず).",
        ],
    },
    {
        "drill_key": "DR-GP-N3-092-C",
        "grammar_code": "GP-N3-092",
        "drill_type": "contrast",
        "prompt_jp": "この救急相談窓口は、昼夜（　　）24時間いつでも電話を受け付けている。",
        "options": ["を問わず", "によって", "に限って", "に際して"],
        "correct_index": 0,
        "translation_vi": "Quầy tư vấn cấp cứu này bất kể ngày đêm đều tiếp nhận điện thoại 24/24 bất cứ lúc nào.",
        "explanation_vi": "Cặp đối lập 昼夜 (ngày đêm) + 24時間いつでも ('bất kể lúc nào') dùng を問わず.",
        "option_diagnostics": [
            "[ĐÚNG - Không phân biệt cặp đối lập 昼夜を問わず]: Hoạt động suốt 24 giờ.",
            "[SAI - Ngược nghĩa thành 'tùy theo ngày hay đêm']: によって là thay đổi tùy lúc, mâu thuẫn với 24時間いつでも.",
            "[SAI - Ngược nghĩa thành 'chỉ riêng ngày đêm']: に限って thu hẹp phạm vi.",
            "[SAI - Sai ngữ cảnh sự kiện]: に際して chỉ sự kiện một lần như khai trương/đăng ký.",
        ],
    },
    # --- GP-N3-093 (formation + contrast + application) ---
    {
        "drill_key": "DR-GP-N3-093-F",
        "grammar_code": "GP-N3-093",
        "drill_type": "formation",
        "prompt_jp": "いすに座る生活が増えたため、日本の家では畳の部屋が（　　）。",
        "options": ["減るつつあります", "減りつつあります", "減ってつつあります", "減ったつつあります"],
        "correct_index": 1,
        "translation_vi": "Vì lối sống ngồi ghế tăng lên nên phòng trải chiếu tatami trong nhà Nhật đang ngày càng giảm dần.",
        "explanation_vi": "Hậu tố ～つつある BẮT BUỘC gắn vào Vます bỏ ます -> 減る -> 減りつつあります (Q#150).",
        "option_diagnostics": [
            "[SAI - Gắn sau Vる]: Không gắn つつある vào thể từ điển *減るつつ.",
            "[ĐÚNG - Vます(bỏ ます) + つつある]: 減りつつあります (Q#150).",
            "[SAI - Gắn sau thể て]: Không gắn つつある vào thể て *減ってつつ.",
            "[SAI - Gắn sau quá khứ Vた]: Không gắn つつある vào thể た *減ったつつ.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-093-C",
        "grammar_code": "GP-N3-093",
        "drill_type": "contrast",
        "prompt_jp": "最近、日本人のライフスタイルの変化により、昔ながらの和室が（　　）。",
        "options": ["減りつつあります", "減るだけです", "減りやすいです", "減ってもかまいません"],
        "correct_index": 0,
        "translation_vi": "Gần đây, do sự thay đổi lối sống của người Nhật, những căn phòng kiểu Nhật truyền thống đang dần giảm đi.",
        "explanation_vi": "Diễn tả một xu hướng đang thực sự chuyển biến dần ở thời điểm hiện tại dùng 減りつつあります (Q#150).",
        "option_diagnostics": [
            "[ĐÚNG - Xu hướng thực tế đang diễn biến dần つつあります]: Khớp mạch thời gian 最近.",
            "[SAI - Sắc thái cực đoan tiêu cực]: 減るだけです nghĩa là 'chỉ có giảm thôi (không làm gì khác)', sai mạch thông tin mô tả.",
            "[SAI - Tính chất chứ không phải xu hướng thực tế]: 減りやすい chỉ tính chất dễ bị giảm, không diễn tả việc nó đang diễn ra dần.",
            "[SAI - Ngược logic]: 減ってもかまいません nghĩa là 'có giảm đi cũng chẳng sao', vô lý trong câu kể thực trạng.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-093-A",
        "grammar_code": "GP-N3-093",
        "drill_type": "application",
        "prompt_jp": "新しい治療法が広まったことで、この病気の患者数は少しずつ（　　）。",
        "options": ["回復しつつある", "回復しにくい", "回復するおそれがある", "回復しかねない"],
        "correct_index": 0,
        "translation_vi": "Nhờ phương pháp điều trị mới phổ biến mà tình trạng bệnh nhân căn bệnh này đang dần hồi phục từng chút một.",
        "explanation_vi": "Diễn biến tích cực đang cải thiện dần dần từng chút một ('少しずつ') dùng 回復しつつある.",
        "option_diagnostics": [
            "[ĐÚNG - Tiến triển dần dần 回復しつつある]: Khớp với 少しずつ.",
            "[SAI - Ngược nghĩa]: 'Phương pháp mới phổ biến -> khó hồi phục' là mâu thuẫn.",
            "[SAI - Sai sắc thái tiêu cực]: おそれがある chỉ dùng cho hậu quả XẤU, không dùng cho 'hồi phục'.",
            "[SAI - Sai sắc thái tiêu cực]: かねない cũng chỉ cảnh báo rủi ro xấu.",
        ],
    },
    # --- GP-N3-094 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-094-C",
        "grammar_code": "GP-N3-094",
        "drill_type": "contrast",
        "prompt_jp": "「球技」というのは、ボールを使うスポーツ（　　）。",
        "options": ["のことだ", "というものだ", "というのだ", "のことか"],
        "correct_index": 0,
        "translation_vi": "Thuật ngữ 'Kyuugi' có nghĩa là các môn thể thao sử dụng quả bóng.",
        "explanation_vi": "Định nghĩa ý nghĩa danh từ/thuật ngữ dùng [Aというのは Bのことだ] (Q#21).",
        "option_diagnostics": [
            "[ĐÚNG - Định nghĩa từ ngữ AというのはBのことだ]: スポーツのことだ (Q#21).",
            "[SAI - Nhầm chân lý cuộc sống]: というものだ nêu quy luật/bản chất hiển nhiên (như 'đời vốn thế'), không dùng định nghĩa từ điển.",
            "[SAI - Sai sắc thái giải thích lý do]: というのだ mang nghĩa nhấn mạnh giải thích/khẳng định nguyên nhân, không định nghĩa danh từ.",
            "[SAI - Sai ngữ khí cảm thán]: ことか là câu cảm thán 'biết bao nhiêu'.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-094-A",
        "grammar_code": "GP-N3-094",
        "drill_type": "application",
        "prompt_jp": "案内状にある「出欠（しゅっけつ）」というのは、出席するか欠席するか（　　）。",
        "options": ["ということだ", "ということか", "というものだ", "にすぎない"],
        "correct_index": 0,
        "translation_vi": "Từ 'Shukketsu' trên giấy mời có nghĩa là việc có tham dự hay vắng mặt.",
        "explanation_vi": "Khi vế định nghĩa B kết thúc bằng một câu hỏi gián tiếp / mệnh đề (出席するか欠席するか), kết thúc bằng ということだ.",
        "option_diagnostics": [
            "[ĐÚNG - Giải thích ý nghĩa mệnh đề ということだ]: Xというのは ～ということだ.",
            "[SAI - Sai ngữ khí]: ことか là cảm thán, không phải câu định nghĩa.",
            "[SAI - Sai chức năng]: というものだ không dùng định nghĩa nghĩa từ.",
            "[SAI - Sai nghĩa hạ thấp]: にすぎない không định nghĩa thuật ngữ.",
        ],
    },
    # --- GP-N3-095 (formation + application) ---
    {
        "drill_key": "DR-GP-N3-095-F",
        "grammar_code": "GP-N3-095",
        "drill_type": "formation",
        "prompt_jp": "日本の秋は涼しくて、（　　）とてもいい季節だと言われている。",
        "options": ["読書するのに", "読書することで", "読書できるうちに", "読書してのに"],
        "correct_index": 0,
        "translation_vi": "Mùa thu ở Nhật mát mẻ, được cho là mùa rất thích hợp cho việc đọc sách.",
        "explanation_vi": "Đánh giá sự thích hợp/tiện lợi [いい / 便利だ / 役に立つ] đối với hoạt động V dùng [Vる + のに] (Q#18).",
        "option_diagnostics": [
            "[ĐÚNG - Vる + のに + いい]: 読書するのにとてもいい季節 (Q#18).",
            "[SAI - Sai quan hệ phương tiện]: 読書することで nghĩa là 'bằng phương tiện đọc sách', mùa thu không sinh ra bởi việc đọc sách.",
            "[SAI - Sai sắc thái tranh thủ]: うちに là 'tranh thủ lúc còn đọc được thì...', không khớp đánh giá 'là mùa rất tốt'.",
            "[SAI - Sai hình thái]: Thể て không gắn trực tiếp với のに.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-095-A",
        "grammar_code": "GP-N3-095",
        "drill_type": "application",
        "prompt_jp": "この電子辞書は軽くて画面も見やすいので、旅行へ（　　）とても便利だ。",
        "options": ["持って行くのに", "持って行ったのに", "持って行くと", "持って行くばかりに"],
        "correct_index": 0,
        "translation_vi": "Cuốn kim từ điển này nhẹ và màn hình dễ nhìn nên rất tiện lợi cho việc mang theo đi du lịch.",
        "explanation_vi": "Trước ～のに + 便利だ luôn dùng động từ thể từ điển Vる (không chia quá khứ Vた).",
        "option_diagnostics": [
            "[ĐÚNG - Vる + のに + 便利だ]: 持って行くのに便利だ.",
            "[SAI - Biến nghĩa sang 'mặc dù đã mang đi']: Vた + のに thành nhượng bộ 'mặc dù đã mang đi thế mà lại tiện', mâu thuẫn ngữ nghĩa.",
            "[SAI - Sai nghĩa điều kiện]: と không nối trực tiếp đánh giá công dụng đồ vật kiểu này.",
            "[SAI - Sai sắc thái đổ lỗi]: ばかりに chỉ dùng cho nguyên nhân gây hậu quả xấu.",
        ],
    },
    # --- GP-N3-096 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-096-F",
        "grammar_code": "GP-N3-096",
        "drill_type": "formation",
        "prompt_jp": "毎日少しずつでも復習を（　　）、語彙力は着実に伸びていく。",
        "options": ["続けることで", "続けてことで", "続けたのに", "続けるばかりに"],
        "correct_index": 0,
        "translation_vi": "Bằng việc tiếp tục ôn tập dù mỗi ngày một chút, vốn từ vựng sẽ tăng lên vững chắc.",
        "explanation_vi": "Chỉ phương thức/cách thức đạt kết quả mong muốn dùng động từ thể từ điển Vる + ことで.",
        "option_diagnostics": [
            "[ĐÚNG - Vる + ことで]: 続けることで diễn tả phương tiện 'bằng cách kiên trì làm V'.",
            "[SAI - Lỗi kết hợp]: Thể て không gắn trực tiếp với ことで.",
            "[SAI - Sai nghĩa nhượng bộ]: のに mang nghĩa 'mặc dù... nhưng', trái nghĩa nhân quả tích cực của câu.",
            "[SAI - Sai sắc thái kết quả xấu]: ばかりに chỉ nguyên nhân gây hậu quả đáng tiếc.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-096-C",
        "grammar_code": "GP-N3-096",
        "drill_type": "contrast",
        "prompt_jp": "この町は、きれいな水と空気（　　）昔からよく知られている。",
        "options": ["があることで", "があるのに", "があるわりに", "があっては"],
        "correct_index": 0,
        "translation_vi": "Thị trấn này từ xưa đã được biết đến rộng rãi nhờ có nguồn nước và không khí trong lành.",
        "explanation_vi": "～ことで còn chỉ nguyên nhân/đặc điểm tích cực tạo nên danh tiếng hoặc tình trạng tích cực ở vế sau.",
        "option_diagnostics": [
            "[ĐÚNG - Vる + ことで]: きれいな水と空気があることで (nhờ đặc điểm có nước và không khí sạch).",
            "[SAI - Sai logic nhượng bộ]: のに nghĩa là 'mặc dù có nước sạch nhưng vẫn...', ngược hoàn toàn.",
            "[SAI - Sai logic đối chiếu]: わりに nghĩa là 'so với tiêu chuẩn... thì bất ngờ là...', không hợp.",
            "[SAI - Sai sắc thái điều kiện xấu]: ては dùng cho điều kiện lặp đi lặp lại dẫn đến hậu quả không hay.",
        ],
    },
    # --- GP-N3-097 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-097-F",
        "grammar_code": "GP-N3-097",
        "drill_type": "formation",
        "prompt_jp": "人の失敗を陰で（　　）。誰でもミスをすることはあるのだから。",
        "options": ["笑うものではない", "笑ったものだ", "笑うことではない", "笑わないものだ"],
        "correct_index": 0,
        "translation_vi": "Không nên cười nhạo sau lưng thất bại của người khác. Bởi vì ai cũng có lúc mắc lỗi.",
        "explanation_vi": "Khuyên răn chuẩn mực đạo đức chung ('không nên làm V') dùng Vる + ものではない.",
        "option_diagnostics": [
            "[ĐÚNG - Vる + ものではない]: 笑うものではない diễn tả quy chuẩn ứng xử 'chớ nên cười'.",
            "[SAI - Sai thời và nghĩa]: Vた + ものだ là hoài niệm thói quen trong quá khứ.",
            "[SAI - Sai mẫu câu]: ことではない mang nghĩa 'không phải chuyện cần/đến mức...', không diễn đạt lời khuyên đạo đức phổ quát.",
            "[SAI - Sai cấu trúc phủ định]: Quy chuẩn cấm đoán đặt ない sau もので (Vる + ものではない), không đặt vào động từ (Vない + ものだ).",
        ],
    },
    {
        "drill_key": "DR-GP-N3-097-C",
        "grammar_code": "GP-N3-097",
        "drill_type": "contrast",
        "prompt_jp": "子どものころ、夏休みになるとよく川で泳いで（　　）。",
        "options": ["遊んだものだ", "遊ぶものだ", "遊ぶことだ", "遊ぶべきだ"],
        "correct_index": 0,
        "translation_vi": "Hồi nhỏ, cứ đến kỳ nghỉ hè là tôi thường hay bơi và chơi ở sông.",
        "explanation_vi": "Hồi tưởng kỷ niệm lặp đi lặp lại trong quá khứ đi kèm よく / 昔 / 子どものころ dùng Vた + ものだ.",
        "option_diagnostics": [
            "[ĐÚNG - Vた + ものだ]: 遊んだものだ diễn tả hồi ức thời thơ ấu.",
            "[SAI - Sai thì]: Vる + ものだ nêu chân lý hiển nhiên ở hiện tại, không khớp 子どものころ.",
            "[SAI - Sai chức năng]: Vる + ことだ là lời khuyên trực tiếp, không dùng hồi tưởng.",
            "[SAI - Sai sắc thái]: べきだ là nghĩa vụ đạo đức 'phải làm', không khớp ngữ cảnh kỷ niệm.",
        ],
    },
    # --- GP-N3-098 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-098-C",
        "grammar_code": "GP-N3-098",
        "drill_type": "contrast",
        "prompt_jp": "電車が事故で遅れた（　　）、会議の開始に間に合わなかったんです。申し訳ありません。",
        "options": ["ものだから", "ものの", "ものなら", "ことだから"],
        "correct_index": 0,
        "translation_vi": "Tại vì tàu bị trễ do tai nạn nên tôi đã không kịp giờ bắt đầu cuộc họp. Thành thật xin lỗi.",
        "explanation_vi": "Giải thích/thanh minh lý do cá nhân dẫn tới kết quả ngoài ý muốn (thường kèm xin lỗi) dùng ～ものだから.",
        "option_diagnostics": [
            "[ĐÚNG - Vた + ものだから]: Chỉ lý do biện minh nhẹ nhàng, mềm mỏng cho sự chậm trễ.",
            "[SAI - Ngược quan hệ nhân quả]: ものの nghĩa là 'mặc dù...', làm câu phi logic ('mặc dù tàu trễ nhưng không kịp').",
            "[SAI - Sai mẫu giả định]: Vる + ものなら nghĩa là 'nếu giả sử có thể... thì...', không phù hợp quá khứ đã xảy ra.",
            "[SAI - Sai đối tượng]: N + のことだから chỉ dùng suy đoán tính cách quen thuộc của một người ('vì là người ấy nên chắc chắn...').",
        ],
    },
    {
        "drill_key": "DR-GP-N3-098-A",
        "grammar_code": "GP-N3-098",
        "drill_type": "application",
        "prompt_jp": "新しいパソコンを買った（　　）、機能が多すぎてまだ十分に使えていない。",
        "options": ["ものの", "ものだから", "ものだ", "せいで"],
        "correct_index": 0,
        "translation_vi": "Tuy đã mua máy tính mới rồi nhưng vì nhiều chức năng quá nên tôi vẫn chưa dùng hết được.",
        "explanation_vi": "Thừa nhận sự thật ở vế trước nhưng kết quả vế sau chưa trọn vẹn/khác kỳ vọng dùng Vた + ものの.",
        "option_diagnostics": [
            "[ĐÚNG - Vた + ものの]: Diễn đạt ý nhượng bộ văn viết 'tuy đã mua nhưng...'.",
            "[SAI - Sai quan hệ]: ものだから biến vế trước thành nguyên nhân ('tại vì lỡ mua máy mới nên mới không dùng được' -> sai trọng tâm ý).",
            "[SAI - Sai cấu trúc nối câu]: ものだ dùng ở cuối câu nêu chân lý/hồi niệm, không nối hai mệnh đề tương phản.",
            "[SAI - Lệch quan hệ nguyên nhân]: Mua máy mới không phải thủ phạm trực tiếp gây ra việc không dùng hết, 機能の多さ mới là nguyên nhân.",
        ],
    },
    # --- GP-N3-099 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-099-F",
        "grammar_code": "GP-N3-099",
        "drill_type": "formation",
        "prompt_jp": "季節が秋から冬へと（　　）、朝晩の冷え込みが厳しくなってきた。",
        "options": ["進むにつれて", "進んでにつれて", "進んだにつれて", "進むにわたって"],
        "correct_index": 0,
        "translation_vi": "Theo đà chuyển giao từ thu sang đông, cái lạnh buổi sáng và tối càng trở nên khắc nghiệt hơn.",
        "explanation_vi": "Mẫu ～につれて nối sau danh từ hoặc động từ thể từ điển (Vる) chỉ hai xu hướng biến đổi song hành.",
        "option_diagnostics": [
            "[ĐÚNG - Vる + につれて]: 進むにつれて chuẩn kết hợp Vる diễn tả sự chuyển biến dần.",
            "[SAI - Sai chia thể]: Thể て không gắn trực tiếp trước につれて.",
            "[SAI - Sai thì]: につれて đòi hỏi Vる biểu thị quá trình đang dịch chuyển, không dùng Vた.",
            "[SAI - Sai nghĩa mẫu]: にわたって chỉ phạm vi không gian/thời gian trải rộng và không gắn sau Vる.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-099-C",
        "grammar_code": "GP-N3-099",
        "drill_type": "contrast",
        "prompt_jp": "都市の人口増加（　　）、住宅不足や交通渋滞が深刻になっている。",
        "options": ["に伴って", "にとって", "に比べて", "にわたって"],
        "correct_index": 0,
        "translation_vi": "Cùng với sự gia tăng dân số đô thị, tình trạng thiếu nhà ở và ùn tắc giao thông ngày càng trở nên nghiêm trọng.",
        "explanation_vi": "N + に伴って（にともなって） diễn tả sự biến đổi kéo theo hàng loạt hệ quả tương ứng (rất hay đi với danh từ Hán-Nhật chỉ xu hướng như 増加, 発展).",
        "option_diagnostics": [
            "[ĐÚNG - N + に伴って]: 人口増加に伴って diễn đạt biến đổi kéo theo các vấn đề xã hội.",
            "[SAI - Sai nghĩa]: にとって nghĩa là 'đối với lập trường của...', không đi với 増加.",
            "[SAI - Sai nghĩa so sánh]: に比べて là 'so với...' để đối chiếu tĩnh, không chỉ biến đổi kéo theo.",
            "[SAI - Sai nghĩa phạm vi]: にわたって là 'kéo dài suốt trong phạm vi thời gian/địa điểm'.",
        ],
    },
    # --- GP-N3-100 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-100-F",
        "grammar_code": "GP-N3-100",
        "drill_type": "formation",
        "prompt_jp": "この地域では、先週の土曜日から一週間（　　）伝統的な祭りが行われている。",
        "options": ["にわたって", "につれて", "によって", "にかけて"],
        "correct_index": 0,
        "translation_vi": "Tại khu vực này, lễ hội truyền thống đang được tổ chức xuyên suốt một tuần lễ kể từ thứ Bảy tuần trước.",
        "explanation_vi": "N (khoảng thời gian/diện tích/số lượng toàn bộ) + にわたって nhấn mạnh sự liên tục trải dài suốt cả khoảng đó.",
        "option_diagnostics": [
            "[ĐÚNG - Khoảng thời gian + にわたって]: 一週間にわたって (kéo dài xuyên suốt 1 tuần).",
            "[SAI - Sai đối tượng]: につれて chỉ sự biến đổi tỷ lệ thuận, không đi với khoảng thời gian 一週間.",
            "[SAI - Sai nghĩa]: によって chỉ nguyên nhân, phương tiện hoặc tác nhân bị động.",
            "[SAI - Sai khung mốc]: ～から～にかけて phải đi cùng cặp điểm đầu-điểm cuối (từ A đến B), không đứng sau một khoảng độ dài đơn lẻ 一週間.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-100-C",
        "grammar_code": "GP-N3-100",
        "drill_type": "contrast",
        "prompt_jp": "10年（　　）研究の結果、ついに新しいワクチンが開発された。",
        "options": ["にわたる", "につれての", "をめぐって", "に基づく"],
        "correct_index": 0,
        "translation_vi": "Kết quả của công trình nghiên cứu kéo dài suốt 10 năm trời, cuối cùng vắc-xin mới đã được phát triển.",
        "explanation_vi": "Bổ nghĩa trực tiếp cho danh từ đứng sau (研究) dùng dạng định ngữ N + にわたる + N.",
        "option_diagnostics": [
            "[ĐÚNG - N + にわたる + N]: 10年にわたる研究 (nghiên cứu kéo dài suốt 10 năm).",
            "[SAI - Sai mẫu]: につれて không nối sau khoảng thời gian tĩnh 10年 để bổ nghĩa kiểu này.",
            "[SAI - Sai chức năng định ngữ và nghĩa]: をめぐって không đứng trực tiếp bổ nghĩa cho danh từ (phải là をめぐる) và mang nghĩa tranh cãi.",
            "[SAI - Sai nghĩa]: に基づく nghĩa là 'căn cứ vào...', 10年 không phải quy tắc hay số liệu làm căn cứ.",
        ],
    },
    # --- GP-N3-101 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-101-C",
        "grammar_code": "GP-N3-101",
        "drill_type": "contrast",
        "prompt_jp": "新しい支店を開設する（　　）、地元の企業の皆様にご挨拶申し上げます。",
        "options": ["にあたり", "につれて", "にわたり", "にくらべ"],
        "correct_index": 0,
        "translation_vi": "Nhân dịp khai trương chi nhánh mới, chúng tôi xin gửi lời chào trân trọng tới quý doanh nghiệp địa phương.",
        "explanation_vi": "Mẫu trang trọng ～にあたり / ～にあたって đánh dấu một cột mốc sự kiện trọng đại sắp hoặc vừa mở ra.",
        "option_diagnostics": [
            "[ĐÚNG - Vる + にあたり]: 開設するにあたり là văn phong trang trọng chuẩn xác khi phát biểu khai trương.",
            "[SAI - Sai ý nghĩa]: につれて chỉ hai yếu tố cùng biến đổi dần dần.",
            "[SAI - Sai nghĩa và kết hợp]: にわたり chỉ sự trải rộng quy mô lớn, không gắn trực tiếp sau Vる.",
            "[SAI - Sai kết hợp và nghĩa]: にくらべ dùng cho so sánh danh từ, không nối Vる.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-101-A",
        "grammar_code": "GP-N3-101",
        "drill_type": "application",
        "prompt_jp": "個人情報保護方針の改定（　　）、以下の事項をご確認ください。",
        "options": ["に際して", "のせいで", "のおかげで", "のわりに"],
        "correct_index": 0,
        "translation_vi": "Nhân dịp sửa đổi chính sách bảo mật thông tin cá nhân, xin vui lòng xác nhận các hạng mục dưới đây.",
        "explanation_vi": "Trong thông báo hành chính/quy trình chính thức, trước sự kiện 改定 dùng N + に際して.",
        "option_diagnostics": [
            "[ĐÚNG - N + に際して]: 改定に際して thông báo thủ tục cần làm nhân dịp thay đổi chính sách.",
            "[SAI - Sai sắc thái đổ lỗi]: のせいで mang nghĩa đổ lỗi tiêu cực, cấm dùng trong thông báo chính thức với khách.",
            "[SAI - Sai logic]: Việc xác nhận điều khoản là thủ tục đi kèm sự kiện chứ không phải 'nhờ ơn'.",
            "[SAI - Sai quan hệ đối lập]: のわりに nghĩa là 'tuy vậy nhưng trái kỳ vọng'.",
        ],
    },
    # --- GP-N3-102 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-102-F",
        "grammar_code": "GP-N3-102",
        "drill_type": "formation",
        "prompt_jp": "新しい空港の建設計画（　　）、住民と行政の間で激しい議論が続いている。",
        "options": ["をめぐって", "をめぐる", "にわたって", "にもとづいて"],
        "correct_index": 0,
        "translation_vi": "Xoay quanh kế hoạch xây dựng sân bay mới, cuộc tranh luận gay gắt giữa người dân và chính quyền vẫn đang tiếp diễn.",
        "explanation_vi": "Bổ nghĩa cho cụm động từ phía sau (議論が続いている) dùng N + をめぐって (trạng ngữ). Chỉ dùng をめぐる khi đứng ngay trước danh từ.",
        "option_diagnostics": [
            "[ĐÚNG - N + をめぐって]: Nối với mệnh đề tranh luận 議論が続いている ở vế sau.",
            "[SAI - Sai vị trí cú pháp]: をめぐる là dạng định ngữ phải đứng trực tiếp trước một danh từ (ví dụ をめぐる議論), không ngăn cách bởi dấu phẩy và 住民と行政.",
            "[SAI - Sai nghĩa]: にわたって chỉ sự trải dài về thời gian/địa lý, không biểu đạt tâm điểm tranh cãi.",
            "[SAI - Sai nghĩa]: にもとづいて nghĩa là 'dựa trên căn cứ tiêu chuẩn', không phù hợp 激しい議論.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-102-C",
        "grammar_code": "GP-N3-102",
        "drill_type": "contrast",
        "prompt_jp": "遺産（　　）兄弟の対立が、長い間解決しないままになっている。",
        "options": ["をめぐる", "についての", "にもとづく", "にともなう"],
        "correct_index": 0,
        "translation_vi": "Sự đối lập giữa anh em xoay quanh chuyện tài sản thừa kế vẫn chưa được giải quyết suốt thời gian dài.",
        "explanation_vi": "Vế sau có từ khóa tranh chấp/đối lập (対立) và đứng ngay trước cụm danh từ 兄弟の対立 nên dùng N + をめぐる.",
        "option_diagnostics": [
            "[ĐÚNG - N + をめぐる + N]: Nhấn mạnh nhiều bên giằng co, đối lập nhau xoay quanh vấn đề thừa kế.",
            "[SAI - Mất sắc thái tranh chấp]: についての quá trung tính, thường dùng cho bài viết/câu hỏi thông thường chứ không đặc tả sự đối đầu 対立.",
            "[SAI - Sai nghĩa]: にもとづく nghĩa là 'căn cứ theo quy chuẩn'.",
            "[SAI - Sai nghĩa]: にともなう chỉ biến đổi kéo theo tỷ lệ thuận.",
        ],
    },
    # --- GP-N3-103 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-103-F",
        "grammar_code": "GP-N3-103",
        "drill_type": "formation",
        "prompt_jp": "このマニュアルは、長年の現場経験と実験データ（　　）作成された。",
        "options": ["に基づいて", "に基づく", "を込めて", "をめぐって"],
        "correct_index": 0,
        "translation_vi": "Cuốn sổ tay hướng dẫn này đã được biên soạn dựa trên kinh nghiệm thực tế nhiều năm và dữ liệu thực nghiệm.",
        "explanation_vi": "Bổ nghĩa cho động từ đứng sau (作成された) dùng dạng trạng ngữ N + に基づいて.",
        "option_diagnostics": [
            "[ĐÚNG - N + に基づいて + V]: Dựa trên dữ liệu để biên soạn tài liệu.",
            "[SAI - Sai vị trí bổ nghĩa]: に基づく phải đi trực tiếp trước Danh từ (ví dụ に基づくマニュアル), không đi trực tiếp trước động từ 作成された.",
            "[SAI - Sai kết hợp từ]: を込めて đi với tâm tình/cảm xúc (心を込めて), không đi với dữ liệu thí nghiệm.",
            "[SAI - Sai nghĩa]: をめぐって nghĩa là tranh cãi xoay quanh vấn đề.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-103-C",
        "grammar_code": "GP-N3-103",
        "drill_type": "contrast",
        "prompt_jp": "実話（　　）映画だが、登場人物の名前や時代設定は一部変更されている。",
        "options": ["をもとにした", "にもとづく", "にかわって", "にくらべて"],
        "correct_index": 0,
        "translation_vi": "Đây là bộ phim lấy chất liệu từ câu chuyện có thật, nhưng tên nhân vật và bối cảnh thời đại đã được thay đổi một phần.",
        "explanation_vi": "Khi cải biên tác phẩm nghệ thuật/phim ảnh từ câu chuyện gốc và có biến tấu dùng ～をもとにした; còn に基づく mang tính tuân thủ chặt chẽ quy định/dữ liệu khoa học.",
        "option_diagnostics": [
            "[ĐÚNG - N + をもとにした]: Phù hợp việc chuyển thể sáng tạo từ 実話 (có chỉnh sửa chi tiết).",
            "[SAI - Lệch sắc thái quy phạm]: に基づく nhấn mạnh tuân thủ chuẩn xác dữ liệu/luật pháp, mâu thuẫn với việc 'đã sửa đổi tên và thời đại'.",
            "[SAI - Sai nghĩa]: にかわって là 'thay mặt cho / thay thế vị trí của'.",
            "[SAI - Sai nghĩa]: にくらべて là 'so với'.",
        ],
    },
    # --- GP-N3-104 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-104-F",
        "grammar_code": "GP-N3-104",
        "drill_type": "formation",
        "prompt_jp": "連日の残業が続いて少し（　　）ので、今週末は家でゆっくり休もうと思う。",
        "options": ["疲れ気味だ", "疲れる気味だ", "疲れた気味だ", "疲れっぽい"],
        "correct_index": 0,
        "translation_vi": "Vì tăng ca liên tục nhiều ngày nên tôi cảm thấy hơi có dấu hiệu mệt, cuối tuần này tôi định nghỉ ngơi thư thả ở nhà.",
        "explanation_vi": "Mẫu ～気味（ぎみ） gắn sau Vます (bỏ ます: 疲れ) hoặc Danh từ (風邪) để diễn đạt cảm giác/triệu chứng nhẹ đang xuất hiện.",
        "option_diagnostics": [
            "[ĐÚNG - Vます(bỏ ます) + 気味だ]: 疲れ気味だ diễn tả trạng thái hơi thấm mệt.",
            "[SAI - Sai chia thể]: Động từ nguyên dạng 疲れる không gắn với 気味.",
            "[SAI - Sai chia thể]: Thể quá khứ 疲れた không gắn với 気味.",
            "[SAI - Sai hậu tố]: っぽい không ghép với gốc động từ 疲れ để diễn đạt triệu chứng sức khỏe hiện thời.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-104-C",
        "grammar_code": "GP-N3-104",
        "drill_type": "contrast",
        "prompt_jp": "最近、物事を（　　）ので、メモ帳をいつも持ち歩くことにしている。",
        "options": ["忘れがちな", "忘れ気味な", "忘れっぽいだ", "忘れるような"],
        "correct_index": 0,
        "translation_vi": "Gần đây tôi rất hay quên mọi việc nên luôn giữ thói quen mang theo sổ ghi chép bên mình.",
        "explanation_vi": "Thói quen/khuynh hướng xấu lặp lại thường xuyên dẫn đến phải có biện pháp đối phó (luôn mang sổ ghi chú) dùng Vます + がち.",
        "option_diagnostics": [
            "[ĐÚNG - Vます + がちな]: 忘れがち chỉ khuynh hướng lặp lại 'thường hay quên'.",
            "[SAI - Sai sắc thái triệu chứng tức thời]: 気味 chỉ dấu hiệu nhất thời vừa nhen nhóm (hơi mệt, hơi cảm), không tự nhiên cho khuynh hướng cố hữu phải lập thói quen mang sổ.",
            "[SAI - Sai ngữ pháp]: っぽい là tính từ đuôi い nên không bao giờ đi với だ hay な trước ので.",
            "[SAI - Sai nghĩa]: 忘れるような nghĩa là 'như thể sẽ quên', không biểu đạt tần suất hay gặp.",
        ],
    },
    # --- GP-N3-105 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-105-F",
        "grammar_code": "GP-N3-105",
        "drill_type": "formation",
        "prompt_jp": "このお店は駅のすぐ近くにある（　　）、料理の値段がとても安い。",
        "options": ["わりに", "にして", "ものだから", "おかげで"],
        "correct_index": 0,
        "translation_vi": "So với việc quán này nằm ngay sát nhà ga thì giá món ăn rất rẻ.",
        "explanation_vi": "Đối chiếu thực tế trái ngược với kỳ vọng thông thường (gần ga lẽ ra đắt nhưng thực tế lại rẻ) dùng V普通形 + わりに.",
        "option_diagnostics": [
            "[ĐÚNG - Mệnh đề thường + わりに]: 駅のすぐ近くにあるわりに (so với vị trí đắc địa gần ga thì giá lại rẻ bất ngờ).",
            "[SAI - Thiếu trợ từ は]: Cụm cố định là にしては (không dùng にして để so sánh trái kỳ vọng) và thường đi sau danh từ hoặc thể thường, không tự đứng làm にして.",
            "[SAI - Ngược quan hệ nhân quả]: ものだから biến việc gần ga thành nguyên nhân thanh minh tại sao giá rẻ.",
            "[SAI - Ngược nghĩa]: Quán gần ga không phải 'nhờ ơn' làm món ăn rẻ đi.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-105-C",
        "grammar_code": "GP-N3-105",
        "drill_type": "contrast",
        "prompt_jp": "田中さんは日本にまだ半年しか住んでいない（　　）、敬語がとても上手だ。",
        "options": ["にしては", "に比べて", "からいうと", "につれて"],
        "correct_index": 0,
        "translation_vi": "So với việc mới chỉ sống ở Nhật nửa năm thì anh Tanaka dùng kính ngữ rất giỏi.",
        "explanation_vi": "Sau mốc chuẩn cá nhân cụ thể (mới ở 6 tháng) mà kết quả vượt ngoài dự đoán dùng ～にしては.",
        "option_diagnostics": [
            "[ĐÚNG - Mệnh đề + にしては]: Đánh giá bất ngờ vượt mong đợi so với mốc nửa năm.",
            "[SAI - Sai kết hợp]: に比べて gắn sau Danh từ (không gắn thẳng sau động từ 住んでいない) và chỉ so sánh hai đối tượng bình thường.",
            "[SAI - Sai nghĩa và kết hợp]: からいうと gắn danh từ để nhận định từ một góc độ ('xét về mặt... thì').",
            "[SAI - Sai nghĩa]: につれて chỉ sự biến đổi tỷ lệ thuận theo thời gian.",
        ],
    },
    # --- GP-N3-106 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-106-C",
        "grammar_code": "GP-N3-106",
        "drill_type": "contrast",
        "prompt_jp": "電車は車（　　）時間が正確なので、大切な用事があるときはいつも電車を使う。",
        "options": ["に比べて", "に対して", "によって", "にかけて"],
        "correct_index": 0,
        "translation_vi": "Tàu điện so với ô tô thì giờ giấc chuẩn xác hơn nên khi có việc quan trọng tôi luôn đi tàu.",
        "explanation_vi": "Đặt hai đối tượng cụ thể (電車 vs 車) lên bàn cân so sánh về mặt tính chất (時間が正確だ) dùng N + に比べて.",
        "option_diagnostics": [
            "[ĐÚNG - N + に比べて]: 車に比べて so sánh ưu thế đúng giờ của tàu điện so với ô tô.",
            "[SAI - Sai sắc thái]: に対して nhấn mạnh thái độ hướng vào đối tượng hoặc tương phản hai chiều, không chuyên dùng cho phép so sánh hơn kém giữa phương tiện.",
            "[SAI - Sai nghĩa]: によって nghĩa là 'tùy thuộc vào' hoặc 'bởi vì'.",
            "[SAI - Sai nghĩa]: にかけて chỉ phạm vi từ điểm này tới điểm kia hoặc lĩnh vực sở trường.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-106-A",
        "grammar_code": "GP-N3-106",
        "drill_type": "application",
        "prompt_jp": "去年のデータ（　　）、今年の夏の平均気温は1.5度も高くなっている。",
        "options": ["と比べると", "から見ると", "にすると", "をめぐると"],
        "correct_index": 0,
        "translation_vi": "Nếu so sánh với số liệu năm ngoái thì nhiệt độ trung bình mùa hè năm nay đã tăng tới 1,5 độ.",
        "explanation_vi": "Khi đối chiếu số liệu cụ thể giữa hai mốc năm trước - năm nay dùng N + と比べると (hoặc に比べて).",
        "option_diagnostics": [
            "[ĐÚNG - N + と比べると]: Đặt số liệu năm ngoái cạnh năm nay để đối chiếu mức chênh lệch.",
            "[SAI - Lệch nghĩa góc nhìn]: から見ると là 'nhìn từ góc độ đánh giá chủ quan của...', không khớp phép trừ chênh lệch 1,5 độ.",
            "[SAI - Sai nghĩa]: にすると dùng khi đặt giả thiết đứng vào vị trí ai đó hoặc đổi đơn vị.",
            "[SAI - Sai ngữ pháp]: Động từ めぐる dùng ở thể て (をめぐって), không chia と để đối chiếu số liệu.",
        ],
    },
    # --- GP-N3-107 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-107-F",
        "grammar_code": "GP-N3-107",
        "drill_type": "formation",
        "prompt_jp": "今日は大切な面接があるので、朝食を（　　）家を出た。",
        "options": ["食べずに", "食べないに", "食べないでいて", "食べてずに"],
        "correct_index": 0,
        "translation_vi": "Vì hôm nay có buổi phỏng vấn quan trọng nên tôi đã ra khỏi nhà mà không ăn sáng.",
        "explanation_vi": "Dạng trang trọng của Vないで ('làm V2 mà không làm V1') dùng V(thể ない bỏ ない) + ずに.",
        "option_diagnostics": [
            "[ĐÚNG - Vない(bỏ ない) + ずに]: 食べずに là dạng chuẩn của 'mà không ăn'.",
            "[SAI - Lỗi cấu tạo]: Không gắn trực tiếp に vào sau ない.",
            "[SAI - Lệch nghĩa]: ないでいる chỉ trạng thái kéo dài chưa làm gì trong suốt thời gian qua, không tự nhiên khi nối với hành động ra khỏi nhà.",
            "[SAI - Sai chia thể]: Không gắn ずに vào sau thể て.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-107-C",
        "grammar_code": "GP-N3-107",
        "drill_type": "contrast",
        "prompt_jp": "あのコメディアンのおかしな動きを見たら、誰でも（　　）。",
        "options": ["笑わずにはいられない", "笑うおそれがある", "笑わなくてもすむ", "笑うわけがない"],
        "correct_index": 0,
        "translation_vi": "Hễ nhìn thấy động tác hài hước của diễn viên hài đó thì ai cũng không thể nhịn được cười.",
        "explanation_vi": "Cảm xúc/phản ứng tự nhiên bộc phát không kìm nén được ở người dùng V(thể ない bỏ ない) + ずにはいられない.",
        "option_diagnostics": [
            "[ĐÚNG - Vずにはいられない]: Không thể kiềm chế phản ứng bật cười.",
            "[SAI - Sai ngữ cảnh và nghĩa]: おそれがある dùng cảnh báo rủi ro/tai họa tiêu cực (thiên tai, sự cố), không dùng cho việc bật cười.",
            "[SAI - Sai nghĩa]: なくてもすむ nghĩa là 'không cần phải làm cũng ổn thỏa'.",
            "[SAI - Ngược nghĩa]: わけがない nghĩa là 'không đời nào cười'.",
        ],
    },
    # --- GP-N3-108 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-108-F",
        "grammar_code": "GP-N3-108",
        "drill_type": "formation",
        "prompt_jp": "今できる準備はすべてやり終えた。あとは本番の結果を（　　）。",
        "options": ["待つのみだ", "待つのみならず", "待ってのみだ", "待つばかりいる"],
        "correct_index": 0,
        "translation_vi": "Những khâu chuẩn bị có thể làm lúc này đều đã xong xuôi hết. Việc còn lại chỉ là chờ kết quả thi thật thôi.",
        "explanation_vi": "Văn viết trang trọng tương đương ～だけだ ('chỉ còn mỗi việc V thôi') dùng Vる + のみだ.",
        "option_diagnostics": [
            "[ĐÚNG - Vる + のみだ]: 待つのみだ diễn tả 'chỉ còn mỗi việc chờ đợi'.",
            "[SAI - Sai cấu trúc kết câu]: のみならず là vế mở đầu 'không chỉ... mà còn...', không thể kết thúc câu.",
            "[SAI - Sai chia thể]: のみだ gắn sau Vる hoặc Danh từ, không gắn sau thể て.",
            "[SAI - Sai hình thái và nghĩa]: Phải là Vて + ばかりいる ('suốt ngày chỉ làm'), hơn nữa không diễn đạt nghĩa 'chỉ còn lại mỗi việc này' sau bước chuẩn bị.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-108-C",
        "grammar_code": "GP-N3-108",
        "drill_type": "contrast",
        "prompt_jp": "この政策は国内の経済（　　）、周辺諸国の貿易にも大きな影響を与えた。",
        "options": ["のみならず", "のみで", "ばかりで", "だけしか"],
        "correct_index": 0,
        "translation_vi": "Chính sách này không chỉ tác động lớn tới kinh tế trong nước mà còn cả hoạt động thương mại của các nước lân cận.",
        "explanation_vi": "Vế sau có ～にも mở rộng phạm vi ('không chỉ A mà còn cả B') dùng N + のみならず.",
        "option_diagnostics": [
            "[ĐÚNG - N + のみならず ... ～にも]: Không chỉ ảnh hưởng A mà còn ảnh hưởng cả B.",
            "[SAI - Ngược nghĩa giới hạn]: のみで nghĩa là 'chỉ trong phạm vi A thôi', mâu thuẫn với にも.",
            "[SAI - Sai nghĩa và văn phong]: ばかりで dùng liệt kê hoặc chỉ lý do toàn yếu tố xấu, không khớp cặp mở rộng にも.",
            "[SAI - Sai ngữ pháp]: しか luôn đòi hỏi động từ phủ định ở cuối câu, không đi với 与えた.",
        ],
    },
    # --- GP-N3-109 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-109-C",
        "grammar_code": "GP-N3-109",
        "drill_type": "contrast",
        "prompt_jp": "私はただ自分の感想を正直に言った（　　）。相手を怒らせるつもりはなかった。",
        "options": ["だけです", "つつあります", "どころか", "ものの"],
        "correct_index": 0,
        "translation_vi": "Tôi chỉ đơn thuần nói thật cảm nghĩ của mình thôi. Tôi không hề có ý định chọc giận đối phương.",
        "explanation_vi": "Đi kèm phó từ ただ để nhấn mạnh phạm vi giới hạn 'chỉ thế thôi' dùng 普通形 + だけです.",
        "option_diagnostics": [
            "[ĐÚNG - Vた + だけです]: Phối hợp với ただ để giới hạn hành động ở mức đơn thuần.",
            "[SAI - Sai chia thể và nghĩa]: つつあります gắn với Vます chỉ sự đang biến đổi dần dần.",
            "[SAI - Sai vị trí và nghĩa]: どころか nối hai vế tương phản tăng tiến, không kết thúc câu kiểu phủ định chủ đích.",
            "[SAI - Sai cú pháp]: ものの nối hai mệnh đề tương phản, không kết câu.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-109-A",
        "grammar_code": "GP-N3-109",
        "drill_type": "application",
        "prompt_jp": "このアプリは無料で使える（　　）、広告もまったく表示されないので快適だ。",
        "options": ["だけでなく", "だけしか", "ばかりに", "こそ"],
        "correct_index": 0,
        "translation_vi": "Ứng dụng này không những dùng miễn phí mà còn hoàn toàn không hiện quảng cáo nên rất thoải mái.",
        "explanation_vi": "Bổ sung ưu điểm thứ hai cùng chiều (có trợ từ も ở vế sau) dùng 普通形 + だけでなく.",
        "option_diagnostics": [
            "[ĐÚNG - Vる + だけでなく ... ～も]: Không chỉ miễn phí mà còn không có quảng cáo.",
            "[SAI - Sai ngữ pháp]: だけしか đòi hỏi động từ phủ định và mang nghĩa giới hạn hẹp, trái ý liệt kê cộng thêm.",
            "[SAI - Sai nghĩa tiêu cực]: ばかりに chỉ dùng cho nguyên nhân dẫn đến hậu quả đáng tiếc.",
            "[SAI - Sai chức năng nối vế]: こそ nhấn mạnh danh từ hoặc mệnh đề nguyên nhân, không liệt kê A không chỉ có thế mà B cũng vậy.",
        ],
    },
    # --- GP-N3-110 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-110-F",
        "grammar_code": "GP-N3-110",
        "drill_type": "formation",
        "prompt_jp": "質問用紙に名前を書かなくて（　　）ので、率直なご意見をお聞かせください。",
        "options": ["もかまいません", "もつつあります", "こそかまいません", "てかまいません"],
        "correct_index": 0,
        "translation_vi": "Không cần ghi tên vào phiếu khảo sát cũng không sao, nên xin hãy cho chúng tôi nghe ý kiến thẳng thắn của bạn.",
        "explanation_vi": "Cho phép ở thể phủ định ('không cần làm V cũng không vấn đề gì') dùng Vなくて + もかまいません.",
        "option_diagnostics": [
            "[ĐÚNG - Vなくて + もかまいません]: Không cần viết tên cũng không sao.",
            "[SAI - Lỗi ghép cấu trúc vô nghĩa]: つつあります gắn sau Vます, không gắn vào なくて.",
            "[SAI - Sai trợ từ nhấn mạnh]: Phải dùng trợ từ nhượng bộ も trong mẫu てもかまわない.",
            "[SAI - Sai hình thái]: Sau なくて phải có も (phủ định nhượng bộ なくても), không dùng てかまいません.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-110-C",
        "grammar_code": "GP-N3-110",
        "drill_type": "contrast",
        "prompt_jp": "お急ぎでしたら、明日以降の提出（　　）。",
        "options": ["でもかまいません", "とはかぎりません", "にすぎません", "べきではありません"],
        "correct_index": 0,
        "translation_vi": "Nếu anh/chị đang bận thì nộp từ ngày mai trở đi cũng không vấn đề gì ạ.",
        "explanation_vi": "Chấp nhận phương án thay thế với danh từ ('cho dù là N cũng không sao') dùng N + でもかまいません.",
        "option_diagnostics": [
            "[ĐÚNG - N + でもかまいません]: Chấp nhận linh hoạt hạn nộp vào ngày hôm sau.",
            "[SAI - Sai nghĩa]: とはかぎりません nghĩa là 'chưa chắc đã là...', không phải lời cho phép.",
            "[SAI - Sai nghĩa]: にすぎません là 'chỉ là... tầm thường thôi'.",
            "[SAI - Ngược ý lịch sự]: べきではありません là lời khuyên ngăn cấm 'không nên nộp từ ngày mai'.",
        ],
    },
    # --- GP-N3-111 (formation + contrast + application) ---
    {
        "drill_key": "DR-GP-N3-111-F",
        "grammar_code": "GP-N3-111",
        "drill_type": "formation",
        "prompt_jp": "この古い木造の橋は、地元の人々によって何百年も大切に（　　）。",
        "options": ["守られてきた", "守ってきた", "守っていく", "守られていた"],
        "correct_index": 0,
        "translation_vi": "Cây cầu gỗ cổ này đã và đang được người dân địa phương gìn giữ trân trọng suốt hàng trăm năm qua.",
        "explanation_vi": "Chủ ngữ là 橋 (vật được người dân bảo vệ, có tác nhân によって) và trạng ngữ kéo dài tới hiện tại 何百年も -> phải kết hợp bị động + てきた = 守られてきた.",
        "option_diagnostics": [
            "[ĐÚNG - Bị động + てきた]: 守られてきた kết hợp đúng hướng tác động vào cây cầu và chiều thời gian suốt hàng trăm năm đến nay.",
            "[SAI - Sai thể chủ động]: Chủ ngữ là 橋 không thể tự 'bảo vệ', đã có tác nhân 地元の人々によって.",
            "[SAI - Sai cả thể và hướng thời gian]: 守っていく là chủ động và hướng từ hiện tại tới tương lai.",
            "[SAI - Thiếu sắc thái nối tiếp xuyên suốt]: 守られていた chỉ diễn tả trạng thái ở một mốc quá khứ đã dứt, kém tự nhiên so với 守られてきた khi nhấn mạnh truyền thống hàng trăm năm tới hiện tại.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-111-C",
        "grammar_code": "GP-N3-111",
        "drill_type": "contrast",
        "prompt_jp": "昔からこの地域では、新年の朝に特別な料理を食べる習慣が（　　）。",
        "options": ["続けられてきた", "続けられていく", "続けられたばかりだ", "続けるはずだった"],
        "correct_index": 0,
        "translation_vi": "Từ xưa tại vùng này, tập tục ăn món đặc biệt vào sáng năm mới đã luôn được duy trì cho đến nay.",
        "explanation_vi": "Có mốc 昔から (từ xưa tới hiện tại) nên dùng Vられてきた chứ không dùng ていく.",
        "option_diagnostics": [
            "[ĐÚNG - Từ quá khứ 昔から -> hiện tại]: 続けられてきた diễn tả tập tục truyền lại xuyên suốt đến nay.",
            "[SAI - Sai trục thời gian]: ていく hướng từ hiện tại đi vào tương lai, mâu thuẫn với 昔から.",
            "[SAI - Mâu thuẫn thời gian]: たばかりだ nghĩa là 'vừa mới chấm dứt cách đây không lâu', trái nghĩa 'từ xưa duy trì đến nay'.",
            "[SAI - Sai nghĩa]: はずだった là suy đoán trong quá khứ đã không thành sự thật.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-111-A",
        "grammar_code": "GP-N3-111",
        "drill_type": "application",
        "prompt_jp": "気温が急に下がって、ようやく秋らしい涼しさが（　　）。",
        "options": ["感じられるようになってきた", "感じられるようになっていく", "感じられるに違いない", "感じられたままだった"],
        "correct_index": 0,
        "translation_vi": "Nhiệt độ giảm đột ngột, cuối cùng sự mát mẻ đặc trưng của mùa thu đã dần bắt đầu cảm nhận được rõ.",
        "explanation_vi": "Quá trình biến chuyển vừa mới bắt đầu xuất hiện hướng tới người nói ở hiện tại (ようやく...) dùng ～てきた.",
        "option_diagnostics": [
            "[ĐÚNG - Biến chuyển hướng tới hiện tại]: 感じられるようになってきた mô tả thay đổi vừa diễn ra rõ rệt ngay lúc này.",
            "[SAI - Sai góc nhìn]: ようになっていく dùng dự báo xu hướng tiếp diễn ra xa về tương lai chứ không gắn với ようやく (cuối cùng thì đã...).",
            "[SAI - Sai ngữ khí]: に違いない là phỏng đoán chủ quan sự việc người khác, không hợp mô tả cảm giác thời tiết ngay lúc này.",
            "[SAI - Mâu thuẫn nội dung]: ままだった là 'giữ nguyên không đổi', trái ngược với 気温が急に下がって.",
        ],
    },
    # --- GP-N3-112 (formation + contrast + application) ---
    {
        "drill_key": "DR-GP-N3-112-F",
        "grammar_code": "GP-N3-112",
        "drill_type": "formation",
        "prompt_jp": "これからの時代は、AIと人間が協力しながら新しい仕事を（　　）だろう。",
        "options": ["作っていくだろう", "作ってきただろう", "作ってあったろう", "作ってしまうだろう"],
        "correct_index": 0,
        "translation_vi": "Trong thời đại sắp tới, có lẽ AI và con người sẽ vừa hợp tác vừa tiếp tục tạo ra những công việc mới.",
        "explanation_vi": "Có chỉ dấu tương lai これからの時代 và phỏng đoán だろう -> dùng Vて + いく.",
        "option_diagnostics": [
            "[ĐÚNG - Vて + いく + だろう]: Diễn tả xu hướng tiếp tục phát triển hướng về tương lai.",
            "[SAI - Sai trục thời gian]: てきた là từ quá khứ tới hiện tại, không khớp これからの時代.",
            "[SAI - Sai mẫu kết quả tĩnh]: てある chỉ kết quả hành động có chủ đích đã làm sẵn.",
            "[SAI - Lệch sắc thái]: てしまう thường nhấn mạnh hoàn tất dứt điểm hoặc sự cố lỡ làng, không mang nghĩa phát triển tiếp nối vào tương lai.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-112-C",
        "grammar_code": "GP-N3-112",
        "drill_type": "contrast",
        "prompt_jp": "日本の伝統工芸は、若い職人たちの手によって次の世代へも（　　）。",
        "options": ["受け継がれていく", "受け継がれてきた", "受け継ぐばかりだ", "受け継がざるを得ない"],
        "correct_index": 0,
        "translation_vi": "Nghề thủ công truyền thống của Nhật Bản sẽ tiếp tục được truyền lại cho thế hệ sau nhờ bàn tay của các nghệ nhân trẻ.",
        "explanation_vi": "Từ khóa hướng tương lai 次の世代へも (tới thế hệ tiếp theo) đòi hỏi chiều hướng ～ていく.",
        "option_diagnostics": [
            "[ĐÚNG - 次の世代へ + ていく]: Bị động + ていく diễn tả sự kế thừa hướng tới tương lai.",
            "[SAI - Sai hướng thời gian]: てきた chỉ từ quá khứ đến hiện tại, không khớp đích tương lai 次の世代へ.",
            "[SAI - Sai sắc thái]: ばかりだ là chiều hướng suy giảm tệ dần (chỉ toàn xấu đi).",
            "[SAI - Sai sắc thái cưỡng ép]: ざるを得ない nghĩa là 'đành buộc phải làm dù không muốn'.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-112-A",
        "grammar_code": "GP-N3-112",
        "drill_type": "application",
        "prompt_jp": "少子高齢化が進むにつれて、地方の人口は今後さらに（　　）見込みだ。",
        "options": ["減っていく", "減ってきた", "減ってある", "減りかけた"],
        "correct_index": 0,
        "translation_vi": "Theo đà già hóa dân số, dân số ở các địa phương dự kiến sẽ còn tiếp tục giảm thêm trong thời gian tới.",
        "explanation_vi": "Có từ 今後 (từ nay về sau) + 見込みだ (dự báo) -> dùng xu hướng tương lai Vて + いく.",
        "option_diagnostics": [
            "[ĐÚNG - 今後 + Vていく + 見込みだ]: Xu hướng tiếp tục giảm dần trong tương lai.",
            "[SAI - Sai trục thời gian]: てきた phản ánh thực trạng quá khứ tới nay, không khớp 今後...見込みだ.",
            "[SAI - Sai loại động từ]: 減る là tự động từ, không chia Vてある.",
            "[SAI - Sai thì và nghĩa]: 減りかけた nghĩa là 'đã suýt giảm trong quá khứ'.",
        ],
    },
    # --- GP-N3-113 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-113-F",
        "grammar_code": "GP-N3-113",
        "drill_type": "formation",
        "prompt_jp": "強い日差しが部屋に入る（　　）、窓の外に植物を育てている。",
        "options": ["のを防ぐため", "ことを防ぐため", "ものが防ぐため", "のが防ぐため"],
        "correct_index": 0,
        "translation_vi": "Để ngăn ánh nắng gắt chiếu vào phòng, tôi đang trồng cây bên ngoài cửa sổ.",
        "explanation_vi": "Danh từ hóa mệnh đề làm tân ngữ trực tiếp cho tha động từ 防ぐ (ngăn chặn việc gì) dùng Vる + の + を + 防ぐ.",
        "option_diagnostics": [
            "[ĐÚNG - Vる + のを + Tha động từ 防ぐ]: Chuẩn cú pháp ngăn chặn hành động ánh nắng chiếu vào.",
            "[SAI - Sai tự nhiên danh từ hóa]: Với động từ tác động trực giác/ngăn chặn hành động đang diễn ra như 防ぐ・止める・待つ, tiếng Nhật ưu tiên のを hơn ことを.",
            "[SAI - Sai nghĩa và trợ từ]: もの chỉ vật hữu hình và が không làm tân ngữ cho tha động từ 防ぐ.",
            "[SAI - Sai trợ từ]: 防ぐ là tha động từ đòi hỏi trợ từ tân ngữ を, không dùng が.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-113-C",
        "grammar_code": "GP-N3-113",
        "drill_type": "contrast",
        "prompt_jp": "試合に勝つこと以上に、最後まであきらめずに戦う（　　）大切だ。",
        "options": ["ことが", "のを", "ものが", "のに"],
        "correct_index": 0,
        "translation_vi": "Hơn cả việc thắng trận, việc chiến đấu không bỏ cuộc đến phút cuối cùng mới là điều quan trọng.",
        "explanation_vi": "Làm chủ ngữ cho tính từ đánh giá mệnh đề khái quát (大切だ / 必要だ) dùng Vる + こと + が.",
        "option_diagnostics": [
            "[ĐÚNG - Vる + ことが + 大切だ]: Danh từ hóa mệnh đề làm chủ ngữ cho tính từ.",
            "[SAI - Sai trợ từ]: 大切だ là tính từ, không nhận tân ngữ を.",
            "[SAI - Sai loại danh từ]: もの chỉ vật cụ thể, không danh từ hóa hành động chiến đấu.",
            "[SAI - Lỗi cấu trúc]: のに là 'cho việc... thì tiện/mặc dù', không làm chủ ngữ trực tiếp cho 大切だ ở đây.",
        ],
    },
    # --- GP-N3-114 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-114-C",
        "grammar_code": "GP-N3-114",
        "drill_type": "contrast",
        "prompt_jp": "家族と何度も話し合いを重ねた（　　）、東京の大学へ進学しないことに決めた。",
        "options": ["末に", "ばかりに", "たびに", "さいちゅうに"],
        "correct_index": 0,
        "translation_vi": "Sau rất nhiều lần bàn bạc trăn trở cùng gia đình, cuối cùng tôi quyết định không lên học đại học ở Tokyo.",
        "explanation_vi": "Quyết định cuối cùng sau một quá trình kéo dài nhiều cân nhắc, vất vả (何度も話し合いを重ねた) dùng Vた + 末に.",
        "option_diagnostics": [
            "[ĐÚNG - Vた + 末に]: Nhấn mạnh kết cục sau quá trình bàn bạc nhiều lần.",
            "[SAI - Sai nghĩa]: ばかりに mang nghĩa đổ lỗi 'chỉ tại vì... mà ra nông nỗi'.",
            "[SAI - Sai thời và nghĩa]: たびに gắn Vる nghĩa là 'mỗi lần hễ làm... thì lại...'.",
            "[SAI - Sai thời điểm]: さいちゅうに là 'ngay giữa lúc đang làm' (chưa kết thúc).",
        ],
    },
    {
        "drill_key": "DR-GP-N3-114-A",
        "grammar_code": "GP-N3-114",
        "drill_type": "application",
        "prompt_jp": "アンケートの集計（　　）、約8割の利用者が新しいサービスに満足していることがわかった。",
        "options": ["の結果", "の末に", "のせいで", "のかわりに"],
        "correct_index": 0,
        "translation_vi": "Kết quả tổng hợp phiếu khảo sát cho thấy khoảng 80% người dùng hài lòng với dịch vụ mới.",
        "explanation_vi": "Trình bày kết quả khách quan rút ra từ cuộc điều tra/khảo sát dùng N + の結果 (không mang sắc thái vất vả trăn trở như の末に).",
        "option_diagnostics": [
            "[ĐÚNG - N + の結果]: アンケート集計の結果 là cụm cố định báo cáo kết quả khảo sát.",
            "[SAI - Sai sắc thái]: の末に hàm ý trải qua gian nan trăn trở lâu dài, không dùng cho thống kê khảo sát trung tính.",
            "[SAI - Sai sắc thái tiêu cực]: のせいで chỉ dùng đổ lỗi kết quả xấu.",
            "[SAI - Sai nghĩa]: のかわりに nghĩa là 'thay cho'.",
        ],
    },
    # --- GP-N3-115 (formation + contrast + application) ---
    {
        "drill_key": "DR-GP-N3-115-F",
        "grammar_code": "GP-N3-115",
        "drill_type": "formation",
        "prompt_jp": "この植物は乾燥にとても強い。（　　）、砂漠のような厳しい環境でも育つことができる。",
        "options": ["そのため", "それとも", "なぜなら", "たとえば"],
        "correct_index": 0,
        "translation_vi": "Loài thực vật này rất chịu hạn. Do đó, nó có thể sinh trưởng ngay cả trong môi trường khắc nghiệt như sa mạc.",
        "explanation_vi": "Câu 1 nêu đặc tính nguyên nhân (chịu hạn tốt), câu 2 nêu kết quả hệ quả (sống được ở sa mạc) -> liên từ nhân quả そのため.",
        "option_diagnostics": [
            "[ĐÚNG - Liên từ nhân quả そのため]: Nối nguyên nhân (chịu hạn) sang kết quả (sống được ở sa mạc).",
            "[SAI - Sai chức năng lựa chọn]: それとも là 'hay là' (nối hai phương án lựa chọn trong câu hỏi).",
            "[SAI - Ngược chiều nhân quả]: なぜなら đứng đầu câu giải thích nguyên nhân ('bởi vì...'), trong khi câu 2 là kết quả.",
            "[SAI - Lệch quan hệ]: Câu 2 không phải ví dụ minh họa cho từ cụ thể mà là hệ quả logic từ câu 1.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-115-C",
        "grammar_code": "GP-N3-115",
        "drill_type": "contrast",
        "prompt_jp": "日本語の敬語は覚えるのが大変だ。（　　）、丁寧な印象を与えるために身につけておきたい。",
        "options": ["それでも", "つまり", "なぜなら", "それゆえに"],
        "correct_index": 0,
        "translation_vi": "Kính ngữ tiếng Nhật rất vất vả để ghi nhớ. Dù vậy, để tạo ấn tượng lịch sự tôi vẫn muốn nắm vững.",
        "explanation_vi": "Hai câu ngược chiều thái độ (tuy khó nhớ nhưng vẫn muốn học) -> liên từ nhượng bộ それでも.",
        "option_diagnostics": [
            "[ĐÚNG - Liên từ nhượng bộ それでも]: 'Dù là khó nhớ nhưng vẫn muốn trau dồi'.",
            "[SAI - Sai logic diễn giải]: つまり nghĩa là 'nói cách khác / tóm lại là' (hai câu đồng nghĩa).",
            "[SAI - Sai logic giải thích]: なぜなら đặt ra lý do cho việc 'rất khó nhớ', mâu thuẫn với mục tiêu muốn học.",
            "[SAI - Sai logic nhân quả]: それゆえに nghĩa là 'vì lý do đó nên...', không khớp hai vế đối lập.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-115-A",
        "grammar_code": "GP-N3-115",
        "drill_type": "application",
        "prompt_jp": "食品ロスとは、まだ食べられるのに捨てられてしまう食べ物のことだ。（　　）、賞味期限切れで廃棄される弁当などが当てはまる。",
        "options": ["たとえば", "つまり", "それでも", "ところが"],
        "correct_index": 0,
        "translation_vi": "Thất thoát thực phẩm là những đồ ăn vẫn còn ăn được nhưng bị vứt bỏ. Ví dụ như cơm hộp bị tiêu hủy vì quá hạn sử dụng.",
        "explanation_vi": "Câu 1 đưa khái niệm khái quát, câu 2 đưa trường hợp cụ thể minh họa kết thúc bằng ～などが当てはまる -> dùng たとえば.",
        "option_diagnostics": [
            "[ĐÚNG - Liên từ nêu ví dụ たとえば]: Khớp hoàn toàn với ～など ở cuối câu 2.",
            "[SAI - Sai chức năng]: つまり tóm lược/nói cách khác toàn bộ khái niệm, không liệt kê mảnh ví dụ với ～など.",
            "[SAI - Sai quan hệ đối lập]: それでも nghĩa là 'dù vậy vẫn'.",
            "[SAI - Sai quan hệ bất ngờ]: ところが nghĩa là 'thế nhưng trái lại'.",
        ],
    },
    # --- GP-N3-116 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-116-F",
        "grammar_code": "GP-N3-116",
        "drill_type": "formation",
        "prompt_jp": "このプロジェクトを成功させるためには、（　　）協力体制が不可欠だ。",
        "options": ["国際的な", "国際っぽい", "国際での", "国際がる"],
        "correct_index": 0,
        "translation_vi": "Để dự án này thành công, hệ thống hợp tác mang tính quốc tế là điều không thể thiếu.",
        "explanation_vi": "Danh từ Hán-Nhật 2 chữ (国際) + hậu tố 的 -> biến thành tính từ đuôi な nên bổ nghĩa cho danh từ 協力体制 dùng 的な.",
        "option_diagnostics": [
            "[ĐÚNG - N(Hán-Nhật) + 的な + N]: 国際的な協力体制 (cơ chế hợp tác mang tính quốc tế).",
            "[SAI - Lỗi kết hợp]: っぽい không ghép vào danh từ Hán-Nhật trừu tượng 国際.",
            "[SAI - Lỗi cú pháp]: 国際 là tính chất bổ nghĩa, không dùng trợ từ で.",
            "[SAI - Sai loại hậu tố]: がる chỉ gắn vào tính từ cảm xúc chủ quan ngôi thứ ba (怖がる, 欲しがる).",
        ],
    },
    {
        "drill_key": "DR-GP-N3-116-C",
        "grammar_code": "GP-N3-116",
        "drill_type": "contrast",
        "prompt_jp": "彼はまだ子ども（　　）、とても冷静で大人らしい判断をすることができる。",
        "options": ["っぽいのに", "的なのに", "らしいのに", "べきなのに"],
        "correct_index": 0,
        "translation_vi": "Cậu ấy nhìn vẫn còn vẻ trẻ con vậy mà có thể đưa ra phán đoán rất bình tĩnh như người lớn.",
        "explanation_vi": "N + っぽい mang nghĩa 'có tính chất/vẻ giống như N' (thường hơi tiêu cực hoặc tính cách trẻ con 子どもっぽい), khác với ～らしい (đúng chất đáng khen) và ～的 (gắn Hán-Nhật).",
        "option_diagnostics": [
            "[ĐÚNG - 子どもっぽいのに]: Nhấn mạnh vẻ bề ngoài còn trẻ con nhưng cách xử sự lại chín chắn.",
            "[SAI - Sai kết hợp thuần Nhật]: Hậu tố 的 hiếm khi gắn với danh từ thuần Nhật 子ども để tả nét tính cách.",
            "[SAI - Sai sắc thái]: 子どもらしい nghĩa là 'đúng chất trẻ thơ hồn nhiên' (khen ngợi), không hợp đối lập với 'phán đoán bình tĩnh như người lớn'.",
            "[SAI - Sai mẫu câu]: べき phải nối sau động từ, không nối trực tiếp sau 子ども.",
        ],
    },
    # --- GP-N3-117 (contrast + application) ---
    {
        "drill_key": "DR-GP-N3-117-C",
        "grammar_code": "GP-N3-117",
        "drill_type": "contrast",
        "prompt_jp": "さっきまで雨が強く降っていた（　　）、今は嘘のように青空が広がっている。",
        "options": ["と思ったら", "からいうと", "につれて", "にしたがって"],
        "correct_index": 0,
        "translation_vi": "Vừa mới thấy trời mưa to ban nãy thế mà bây giờ bầu trời xanh đã trải rộng như chưa từng có mưa.",
        "explanation_vi": "Chuyển biến bất ngờ trái ngược ngay sau một trạng thái vừa quan sát (さっきまで... 今は...) dùng 普通形 + と思ったら.",
        "option_diagnostics": [
            "[ĐÚNG - Vていた + と思ったら]: Diễn đạt sự thay đổi bất ngờ ngay sau đó.",
            "[SAI - Sai hình thức và nghĩa]: からいうと gắn sau danh từ tiêu chí ('xét từ...').",
            "[SAI - Sai logic]: Thời tiết thay đổi đột ngột trái ngược không phải biến đổi tỷ lệ thuận từ từ (につれて).",
            "[SAI - Sai logic]: にしたがって cũng diễn tả xu hướng biến đổi dần dần cùng chiều, không hợp trạng thái đảo ngược tức thì.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-117-A",
        "grammar_code": "GP-N3-117",
        "drill_type": "application",
        "prompt_jp": "玄関で誰かの話し声が聞こえた（　　）、友人がサプライズで遊びに来てくれていた。",
        "options": ["と思って出てみたら", "と思えば出てみない", "とすれば出てみる", "というほど出てみた"],
        "correct_index": 0,
        "translation_vi": "Vừa nghe thấy tiếng ai nói chuyện ngoài cửa, nghĩ bụng thế rồi bước ra xem thì hóa ra bạn tôi đến chơi bất ngờ.",
        "explanation_vi": "Nhận thấy tín hiệu ngoài cửa và hành động tiếp theo phát hiện sự việc bất ngờ dùng ～と思って Vてみたら (dạng nền tảng cùng họ ～と思ったら).",
        "option_diagnostics": [
            "[ĐÚNG - Vた + と思って + Vてみたら]: Phát hiện bất ngờ khi mở cửa kiểm tra.",
            "[SAI - Vô nghĩa]: 出てみない phủ định mâu thuẫn với việc thấy bạn đến chơi.",
            "[SAI - Sai giả định]: とすれば đặt giả thiết điều kiện, không kể lại sự việc đã xảy ra.",
            "[SAI - Sai nghĩa mức độ]: というほど là 'đến mức độ...', không gắn giữa hai sự việc nối tiếp.",
        ],
    },
    # --- GP-N3-118 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N3-118-F",
        "grammar_code": "GP-N3-118",
        "drill_type": "formation",
        "prompt_jp": "日頃は当店をご愛顧いただき、誠にありがとう（　　）。またのご来店をお待ちしております。",
        "options": ["ございます", "いただきます", "くださいます", "おります"],
        "correct_index": 0,
        "translation_vi": "Xin chân thành cảm ơn quý khách đã luôn tin tưởng ủng hộ cửa hàng chúng tôi. Rất hân hạnh được đón tiếp quý khách lần tới.",
        "explanation_vi": "Trong cụm cảm ơn lịch sự cố định đầu/cuối thông báo khách hàng dùng ありがとうございます -> văn trang trọng ありがとうございます / 誠にありがとうございます (ございます).",
        "option_diagnostics": [
            "[ĐÚNG - 誠にありがとうございます]: Thành ngữ kính ngữ cảm ơn chuẩn mực trong thông báo bán hàng.",
            "[SAI - Sai thành ngữ]: Không có cách nói ありがとういただきます.",
            "[SAI - Sai thành ngữ]: Không có cách nói ありがとうくださいます.",
            "[SAI - Sai trợ động từ]: おります là khiêm nhường của いる, không đi với ありがとう.",
        ],
    },
    {
        "drill_key": "DR-GP-N3-118-C",
        "grammar_code": "GP-N3-118",
        "drill_type": "contrast",
        "prompt_jp": "ご不明な点がございましたら、下記の窓口までご連絡（　　）。",
        "options": ["くださいますようお願い申し上げます", "になってくださります", "して参ります", "いたしましょう"],
        "correct_index": 0,
        "translation_vi": "Nếu có điểm nào chưa rõ, kính mong quý khách vui lòng liên hệ tới quầy tiếp nhận dưới đây.",
        "explanation_vi": "Đề nghị khách hàng thực hiện hành động liên hệ tới công ty mình dùng ご + Danh động từ Hán-Nhật + くださいますよう (hoặc ください).",
        "option_diagnostics": [
            "[ĐÚNG - ご連絡 + くださいますよう]: Tôn kính ngữ lịch sự cao độ đề nghị khách hàng liên hệ.",
            "[SAI - Lỗi trùng kính ngữ]: Không gắn になって với くださります sau danh từ Hán-Nhật ご連絡.",
            "[SAI - Nhầm chủ ngữ]: して参ります là khiêm nhường ngữ của mình ('tôi sẽ đi làm...'), biến thành nhân viên tự liên hệ chứ không phải mời khách.",
            "[SAI - Sai chủ ngữ]: いたしましょう là lời mời bản thân làm hộ, sai ngôi người liên hệ.",
        ],
    },

    # --- GP-N2-01 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N2-01-F",
        "grammar_code": "GP-N2-01",
        "drill_type": "formation",
        "prompt_jp": "台風で電車がすべて止まってしまったので、歩いて帰ら（　　）。",
        "options": ["ざるを得ない", "ないざるを得ない", "ずを得ない", "ざるはいない"],
        "correct_index": 0,
        "translation_vi": "Vì bão khiến toàn bộ tàu điện ngừng chạy nên tôi đành buộc phải đi bộ về.",
        "explanation_vi": "Mẫu N2 ～ざるを得ない gắn sau V(thể ない bỏ ない -> 帰ら + ざるを得ない). Riêng する chia thành せざるを得ない.",
        "option_diagnostics": [
            "[ĐÚNG - V(cột あ) + ざるを得ない]: 帰らざるを得ない ('đành buộc phải về').",
            "[SAI - Thừa ない]: ざる bản thân đã là trợ động từ phủ định cổ, không giữ lại ない.",
            "[SAI - Nhầm với ～ずにはいられない]: Không dùng ずを得ない.",
            "[SAI - Lỗi cấu tạo mẫu]: Sai trợ từ và động từ phụ (đúng phải là ざるを得ない).",
        ],
    },
    {
        "drill_key": "DR-GP-N2-01-C",
        "grammar_code": "GP-N2-01",
        "drill_type": "contrast",
        "prompt_jp": "経営赤字が3年連続で続いているため、不採算店舗を閉鎖（　　）。",
        "options": ["せざるを得ない", "するざるを得ない", "しざるを得ない", "してたまらない"],
        "correct_index": 0,
        "translation_vi": "Do thua lỗ kinh doanh kéo dài 3 năm liên tiếp nên buộc phải đóng cửa các cửa hàng không sinh lời.",
        "explanation_vi": "Ngoại lệ bắt buộc của nhóm 3 する với ～ざるを得ない là せざるを得ない (từ 閉鎖する -> 閉鎖せざるを得ない).",
        "option_diagnostics": [
            "[ĐÚNG - Ngoại lệ する -> せざるを得ない]: Biện pháp bắt buộc trong thông báo doanh nghiệp.",
            "[SAI - Sai chia động từ]: Không giữ nguyên する trước ざるを得ない.",
            "[SAI - Sai gốc chia]: Không dùng thân Vます (し) mà dùng dạng 未然 cổ (せ).",
            "[SAI - Sai ý nghĩa]: てたまらない diễn tả cảm giác/cảm xúc không chịu nổi của cá nhân, không dùng cho quyết sách đóng cửa hàng.",
        ],
    },
    # --- GP-N2-02 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N2-02-F",
        "grammar_code": "GP-N2-02",
        "drill_type": "formation",
        "prompt_jp": "睡眠不足のまま車の運転を続けると、重大な事故を起こし（　　）。",
        "options": ["かねない", "かねる", "うる", "ざるを得ない"],
        "correct_index": 0,
        "translation_vi": "Nếu tiếp tục lái xe trong tình trạng thiếu ngủ thì rất có nguy cơ gây ra tai nạn nghiêm trọng.",
        "explanation_vi": "Cảnh báo khả năng phát sinh hậu quả xấu dùng Vます(bỏ ます) + かねない ('không khéo sẽ...', đồng nghĩa mức N2 của ～おそれがある).",
        "option_diagnostics": [
            "[ĐÚNG - Vます + かねない]: 起こしかねない cảnh báo nguy cơ gây tai nạn.",
            "[SAI - Ngược nghĩa hoàn toàn]: かねる nghĩa là 'khó lòng mà làm được', ở đây lại thành 'khó lòng gây tai nạn'!",
            "[SAI - Sai sắc thái trung tính]: 得る chỉ khả năng lý thuyết trung tính, trong khi câu đang cảnh báo rủi ro tiêu cực cụ thể.",
            "[SAI - Lệch nghĩa]: ざるを得ない là 'đành buộc phải làm' dù không muốn.",
        ],
    },
    {
        "drill_key": "DR-GP-N2-02-C",
        "grammar_code": "GP-N2-02",
        "drill_type": "contrast",
        "prompt_jp": "そのような不用意な発言を続ければ、取引先の信頼を（　　）。",
        "options": ["失いかねない", "失いかねる", "失うものだ", "失うまい"],
        "correct_index": 0,
        "translation_vi": "Nếu tiếp tục phát ngôn thiếu thận trọng như vậy, rất có thể sẽ đánh mất lòng tin của đối tác.",
        "explanation_vi": "Phân biệt cặp cặp cực hay nhầm ở N2: Vます+かねない (có nguy cơ xảy ra chuyện xấu) vs Vます+かねる (khó mà làm nổi).",
        "option_diagnostics": [
            "[ĐÚNG - Vます + かねない]: Nguy cơ rất dễ làm mất lòng tin khách hàng.",
            "[SAI - Ngược nghĩa]: 失いかねる mang nghĩa 'khó có thể làm mất' (sai hoàn toàn).",
            "[SAI - Sai nghĩa]: ものだ dùng nêu chân lý chung hoặc hồi niệm.",
            "[SAI - Ngược nghĩa]: まい là ý chí/phỏng đoán phủ định ('chắc sẽ không mất').",
        ],
    },
    # --- GP-N2-03 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N2-03-F",
        "grammar_code": "GP-N2-03",
        "drill_type": "formation",
        "prompt_jp": "誠に恐れ入りますが、個人情報に関わる質問にはお答え（　　）。",
        "options": ["しかねます", "しかねません", "し得ません", "せざるを得ません"],
        "correct_index": 0,
        "translation_vi": "Thành thật xin lỗi quý khách, nhưng chúng tôi khó có thể trả lời các câu hỏi liên quan đến thông tin cá nhân.",
        "explanation_vi": "Từ chối khéo léo trong công sở/CSKH dùng kính ngữ khiêm nhường お + Vます + しかねます (gốc Vます + かねる).",
        "option_diagnostics": [
            "[ĐÚNG - お + Vます + しかねます]: Cách từ chối lịch sự chuẩn mực nhất trong doanh nghiệp Nhật.",
            "[SAI - Ngược nghĩa thành rủi ro]: かねません nghĩa là 'e rằng có nguy cơ sẽ lỡ trả lời mất'.",
            "[SAI - Lệch sắc thái công sở]: 得ません chỉ tính bất khả thi logic ('không thể tồn tại khả năng'), quá cứng và không mang ý từ chối khéo.",
            "[SAI - Ngược nghĩa]: せざるを得ません nghĩa là 'đành buộc phải trả lời'.",
        ],
    },
    {
        "drill_key": "DR-GP-N2-03-C",
        "grammar_code": "GP-N2-03",
        "drill_type": "contrast",
        "prompt_jp": "これほど重要な契約を、責任者の確認なしに私一人の判断では（　　）。",
        "options": ["引き受けかねます", "引き受けかねない", "引き受けがちだ", "引き受けておく"],
        "correct_index": 0,
        "translation_vi": "Một bản hợp đồng quan trọng thế này, nếu thiếu xác nhận của người phụ trách thì riêng phán đoán của mình tôi khó mà nhận được.",
        "explanation_vi": "Từ chối nhận trách nhiệm vượt thẩm quyền một cách lịch sự dùng Vます + かねます.",
        "option_diagnostics": [
            "[ĐÚNG - Vます + かねます]: Thể hiện sự khó xử/không thể tự ý đảm nhận.",
            "[SAI - Ngược nghĩa]: 引き受けかねない nghĩa là 'có nguy cơ lỡ nhận bừa mất'.",
            "[SAI - Sai nghĩa]: がちだ là khuynh hướng xấu lặp đi lặp lại.",
            "[SAI - Sai nghĩa]: ておく là chuẩn bị trước cho tương lai.",
        ],
    },
    # --- GP-N2-04 (contrast + application) ---
    {
        "drill_key": "DR-GP-N2-04-C",
        "grammar_code": "GP-N2-04",
        "drill_type": "contrast",
        "prompt_jp": "今回のプロジェクトの成功は、チーム全員が力を合わせた努力の結果（　　）。",
        "options": ["にほかならない", "にすぎない", "とはかぎらない", "だけのことだ"],
        "correct_index": 0,
        "translation_vi": "Thành công của dự án lần này chính là thành quả từ sự nỗ lực chung sức của toàn đội chứ không gì khác.",
        "explanation_vi": "Khẳng định dứt khoát nguyên nhân/bản chất duy nhất mang sắc thái trang trọng đề cao dùng N + にほかならない.",
        "option_diagnostics": [
            "[ĐÚNG - N + にほかならない]: Nhấn mạnh thành công 'chính xác là kết quả nỗ lực chung chứ không do đâu khác'.",
            "[SAI - Sắc thái hạ thấp ngược chiều]: にすぎない là 'chẳng qua chỉ là... tầm thường thôi'.",
            "[SAI - Sắc thái nghi ngờ]: とはかぎらない nghĩa là 'chưa chắc là...'.",
            "[SAI - Mất lực khẳng định]: だけのことだ chỉ có nghĩa 'chỉ là chuyện thế thôi'.",
        ],
    },
    {
        "drill_key": "DR-GP-N2-04-A",
        "grammar_code": "GP-N2-04",
        "drill_type": "application",
        "prompt_jp": "ルールを厳しくしたのは、利用者の安全を第一に考えている（　　）。",
        "options": ["からにほかならない", "からといって", "からには", "せいにほかならない"],
        "correct_index": 0,
        "translation_vi": "Việc siết chặt quy tắc chính là vì chúng tôi đặt sự an toàn của người dùng lên hàng đầu, chứ không phải vì lý do nào khác.",
        "explanation_vi": "Khi nêu nguyên nhân bằng mệnh đề ～から mà muốn khẳng định 'chính là vì lẽ đó không gì khác', dùng ～からにほかならない.",
        "option_diagnostics": [
            "[ĐÚNG - ～からにほかならない]: Khẳng định lý do duy nhất đằng sau quyết định siết quy tắc.",
            "[SAI - Sai cấu trúc kết câu]: からといって dùng ở giữa câu ('dù nói là... nhưng chưa chắc...'), không kết câu khẳng định.",
            "[SAI - Sai vị trí và chức năng]: からには là 'một khi đã... thì phải...', đứng ở vế 1.",
            "[SAI - Sai sắc thái]: せい mang ý đổ lỗi tiêu cực, không đi với mục tiêu an toàn tốt đẹp.",
        ],
    },
    # --- GP-N2-05 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N2-05-F",
        "grammar_code": "GP-N2-05",
        "drill_type": "formation",
        "prompt_jp": "カレンダーの上ではもう（　　）、朝晩はまだまだ冬の寒さが残っている。",
        "options": ["春とはいえ", "春といえどもない", "春ながらだ", "春ものの"],
        "correct_index": 0,
        "translation_vi": "Tuy trên lịch nói là đã sang xuân rồi, nhưng sáng tối vẫn còn vương lại cái lạnh của mùa đông.",
        "explanation_vi": "Mẫu N2 ～とはいえ nối thẳng sau Danh từ trần (春とはいえ) hoặc thể thường, thừa nhận danh nghĩa ở vế 1 nhưng thực tế vế 2 vẫn chưa tương xứng.",
        "option_diagnostics": [
            "[ĐÚNG - N + とはいえ]: 春とはいえ đối chiếu rất tự nhiên với まだまだ寒さが残っている.",
            "[SAI - Sai mẫu câu]: Không tồn tại dạngといえどもない.",
            "[SAI - Sai chia thể và trợ từ]: ながら gắn sau Vます, không gắn trực tiếp với N + だ.",
            "[SAI - Lỗi kết hợp]: Danh từ trước ものの phải chia N + な hoặc N + である (春であるものの).",
        ],
    },
    {
        "drill_key": "DR-GP-N2-05-C",
        "grammar_code": "GP-N2-05",
        "drill_type": "contrast",
        "prompt_jp": "AI技術が進歩した（　　）、最終的な倫理判断はやはり人間が行うべきだ。",
        "options": ["とはいえ", "からには", "にわたって", "のみならず"],
        "correct_index": 0,
        "translation_vi": "Tuy nói rằng công nghệ AI đã tiến bộ rồi, nhưng phán đoán đạo đức cuối cùng vẫn nên do con người thực hiện.",
        "explanation_vi": "Thừa nhận tiền đề tích cực (AI đã tiến bộ) rồi giới hạn/đối lập lại bằng vai trò không thể thay thế của con người ở vế sau dùng Vた + とはいえ.",
        "option_diagnostics": [
            "[ĐÚNG - Vた + とはいえ]: Nhượng bộ trang trọng 'tuy nói là... nhưng vẫn...'.",
            "[SAI - Sai quan hệ nhân quả ý chí]: からには là 'một khi đã tiến bộ thì phải...'.",
            "[SAI - Sai mẫu và nghĩa]: にわたって gắn danh từ chỉ phạm vi.",
            "[SAI - Ngược nghĩa mở rộng]: のみならず là 'không chỉ... mà còn...', không tạo tương phản.",
        ],
    },
    # --- GP-N2-06 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N2-06-F",
        "grammar_code": "GP-N2-06",
        "drill_type": "formation",
        "prompt_jp": "激しい大雨と強風（　　）、屋外のコンサートは予定どおり開催された。",
        "options": ["にもかかわらず", "なにもかかわらず", "のにかかわらず", "をにもかかわらず"],
        "correct_index": 0,
        "translation_vi": "Bất chấp mưa lớn xối xả và gió mạnh, buổi hòa nhạc ngoài trời vẫn được tổ chức đúng kế hoạch.",
        "explanation_vi": "N + にもかかわらず gắn trực tiếp sau Danh từ trần (không thêm な, の hay を).",
        "option_diagnostics": [
            "[ĐÚNG - N(trần) + にもかかわらず]: Chuẩn kết hợp danh từ với mẫu bất chấp N2.",
            "[SAI - Thừa な]: Không thêm な sau danh từ trước にもかかわらず (khác với のに phải dùng 大雨なのに).",
            "[SAI - Thừa の]: Không dùng の giữa Danh từ và にもかかわらず.",
            "[SAI - Sai trợ từ]: Không chèn を trước にもかかわらず.",
        ],
    },
    {
        "drill_key": "DR-GP-N2-06-C",
        "grammar_code": "GP-N2-06",
        "drill_type": "contrast",
        "prompt_jp": "何度も注意を受けていた（　　）、彼はまた同じミスを繰り返した。",
        "options": ["にもかかわらず", "おかげで", "にしたがって", "だけあって"],
        "correct_index": 0,
        "translation_vi": "Mặc dù đã nhiều lần bị nhắc nhở rồi, thế mà cậu ta vẫn lặp lại đúng sai lầm đó.",
        "explanation_vi": "Nhấn mạnh thái độ hoặc kết quả trái ngược bất chấp cảnh báo trước đó dùng 普通形 + にもかかわらず.",
        "option_diagnostics": [
            "[ĐÚNG - Vていた + にもかかわらず]: Thể hiện sự bất chấp lời nhắc nhở đáng trách.",
            "[SAI - Ngược nghĩa biết ơn]: おかげで là 'nhờ ơn'.",
            "[SAI - Sai logic]: にしたがって là 'càng bị nhắc càng lặp lỗi' (tăng tiến theo hướng đó thì vô lý ở đây nếu dùng cho cùng hành vi bình thường, trọng tâm bài là bất chấp cảnh báo).",
            "[SAI - Sai sắc thái khen ngợi]: だけあって mang nghĩa tích cực ('xứng danh với... nên quả nhiên...').",
        ],
    },
    # --- GP-N2-07 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N2-07-F",
        "grammar_code": "GP-N2-07",
        "drill_type": "formation",
        "prompt_jp": "新しい日程が（　　）、関係者の皆様へメールでお知らせいたします。",
        "options": ["決まり次第", "決まる次第", "決まったとたんに", "決まることにして"],
        "correct_index": 0,
        "translation_vi": "Ngay sau khi lịch trình mới được quyết định, chúng tôi sẽ thông báo qua email tới toàn thể quý vị liên quan.",
        "explanation_vi": "Mẫu công sở N2 'ngay sau khi xong V1 thì sẽ thực hiện V2' dùng Vます(bỏ ます) + 次第 (không dùng Vる hay Vた).",
        "option_diagnostics": [
            "[ĐÚNG - Vます(bỏ ます) + 次第]: 決まり次第 là mẫu chuẩn thông báo quy trình.",
            "[SAI - Sai chia thể]: 次第 không gắn sau Vる (決まる).",
            "[SAI - Sai thì]: とたんに dùng kể lại biến cố bất ngờ ĐÃ xảy ra ở quá khứ, không dùng hứa hẹn kế hoạch tương lai ～いたします.",
            "[SAI - Sai nghĩa và ngữ pháp]: 決まることにして không hợp ngữ cảnh chờ lịch quyết định rồi thông báo.",
        ],
    },
    {
        "drill_key": "DR-GP-N2-07-C",
        "grammar_code": "GP-N2-07",
        "drill_type": "contrast",
        "prompt_jp": "この計画が成功するかどうかは、リーダーの判断力（　　）。",
        "options": ["次第だ", "ばかりだ", "にちがいない", "ものだ"],
        "correct_index": 0,
        "translation_vi": "Kế hoạch này có thành công hay không hoàn toàn tùy thuộc vào năng lực phán đoán của người dẫn dắt.",
        "explanation_vi": "Khác với Vます+次第 ('ngay sau khi...'), khi gắn sau Danh từ ở cuối câu, N + 次第だ mang nghĩa 'tùy thuộc hoàn toàn vào N'.",
        "option_diagnostics": [
            "[ĐÚNG - N + 次第だ]: Khẳng định sự thành bại phụ thuộc vào năng lực phán đoán.",
            "[SAI - Sai nghĩa]: ばかりだ là 'càng ngày càng tệ' (sau Vる).",
            "[SAI - Sai ngữ pháp]: にちがいない không gắn trực tiếp sau danh từ 判断力 để diễn đạt sự phụ thuộc 'có thành công hay không'.",
            "[SAI - Sai nghĩa]: ものだ không có nghĩa 'tùy thuộc vào'.",
        ],
    },
    # --- GP-N2-08 (contrast + application) ---
    {
        "drill_key": "DR-GP-N2-08-C",
        "grammar_code": "GP-N2-08",
        "drill_type": "contrast",
        "prompt_jp": "経済のグローバル化（　　）、外国語能力を重視する企業が急増している。",
        "options": ["に伴って", "に限って", "にほかならず", "をめぐって"],
        "correct_index": 0,
        "translation_vi": "Cùng với quá trình toàn cầu hóa kinh tế, số doanh nghiệp coi trọng năng lực ngoại ngữ đang tăng nhanh.",
        "explanation_vi": "Hai xu hướng vĩ mô biến đổi kéo theo nhau cùng chiều (toàn cầu hóa -> số công ty cần ngoại ngữ tăng) dùng N + に伴って (trang trọng hơn につれて).",
        "option_diagnostics": [
            "[ĐÚNG - N + に伴って]: Biến đổi xã hội kéo theo sự gia tăng tương ứng.",
            "[SAI - Sai nghĩa]: に限って nghĩa là 'chính đúng vào lúc/riêng đối tượng N lại xui xẻo/đặc biệt'.",
            "[SAI - Sai nghĩa]: にほかならず nghĩa là 'chính là do không gì khác'.",
            "[SAI - Sai nghĩa]: をめぐって là tranh cãi xoay quanh vấn đề.",
        ],
    },
    {
        "drill_key": "DR-GP-N2-08-A",
        "grammar_code": "GP-N2-08",
        "drill_type": "application",
        "prompt_jp": "駅前の大規模な再開発に（　　）交通規制について、市民へ説明会が開かれた。",
        "options": ["伴う", "伴ったの", "つれての", "かわっての"],
        "correct_index": 0,
        "translation_vi": "Buổi giải trình cho người dân đã được mở ra về việc phân luồng giao thông đi kèm với đợt tái quy hoạch quy mô lớn trước nhà ga.",
        "explanation_vi": "Bổ nghĩa trực tiếp cho danh từ đứng sau (交通規制) dùng dạng định ngữ N + に伴う + N.",
        "option_diagnostics": [
            "[ĐÚNG - N + に伴う + N]: 再開発に伴う交通規制 (quy định giao thông phát sinh kèm theo tái quy hoạch).",
            "[SAI - Thừa の]: Động từ ở định ngữ nối trực tiếp danh từ, không chèn の sau 伴った.",
            "[SAI - Sai dạng định ngữ]: につれて không có dạng につれる + N; người ta dùng に伴う + N.",
            "[SAI - Sai nghĩa]: かわって nghĩa là 'thay mặt cho'.",
        ],
    },
    # --- GP-N2-09 (contrast + application) ---
    {
        "drill_key": "DR-GP-N2-09-C",
        "grammar_code": "GP-N2-09",
        "drill_type": "contrast",
        "prompt_jp": "この博物館は子ども（　　）、大人の訪問客も十分楽しめる工夫がされている。",
        "options": ["に限らず", "とは限らず", "に限って", "にしたがって"],
        "correct_index": 0,
        "translation_vi": "Bảo tàng này không chỉ giới hạn cho trẻ em mà còn có nhiều thiết kế khéo léo để cả du khách người lớn cũng thưởng thức trọn vẹn.",
        "explanation_vi": "Mở rộng đối tượng ('không chỉ A mà cả B cũng...') dùng N + に限らず + ～も.",
        "option_diagnostics": [
            "[ĐÚNG - N + に限らず ... ～も]: Phá bỏ giới hạn 'trẻ em' để mở rộng sang 'người lớn'.",
            "[SAI - Nhầm cặp N3 とは限らない]: とは限らない nghĩa là 'chưa chắc 100% là...' (phủ định sự tuyệt đối), không ghép danh từ để liệt kê 'không chỉ A mà cả B'.",
            "[SAI - Sai nghĩa]: に限って là 'riêng chỉ...'.",
            "[SAI - Sai nghĩa]: にしたがって là 'tuân theo / càng... càng...'.",
        ],
    },
    {
        "drill_key": "DR-GP-N2-09-A",
        "grammar_code": "GP-N2-09",
        "drill_type": "application",
        "prompt_jp": "災害は昼夜（　　）いつ発生するかわからないため、事前の備えが大切だ。",
        "options": ["を問わず", "に限らずだけ", "というものでなく", "にもかかわらずに"],
        "correct_index": 0,
        "translation_vi": "Thảm họa thì bất kể ngày hay đêm có thể xảy ra bất cứ lúc nào nên việc chuẩn bị trước là rất quan trọng.",
        "explanation_vi": "Dùng với cặp đối lập cố định như 昼夜 / 男女 / 年齢 / 国籍: ～に限らず hoặc ～を問わず ('không phân biệt/không giới hạn').",
        "option_diagnostics": [
            "[ĐÚNG - Cặp từ đối lập + を問わず / に限らず]: 昼夜を問わず không kể ngày đêm.",
            "[SAI - Ghép sai mẫu]: Không kết hợp に限らず với だけ.",
            "[SAI - Sai nghĩa]: というものではない phủ nhận quan điểm chung kiểu triết lý.",
            "[SAI - Lỗi trợ từ]: Không thêm に sau にもかかわらず.",
        ],
    },
    # --- GP-N2-10 (contrast + application) ---
    {
        "drill_key": "DR-GP-N2-10-C",
        "grammar_code": "GP-N2-10",
        "drill_type": "contrast",
        "prompt_jp": "祖父の病気入院（　　）、家族全員で食生活や健康管理を見直すようになった。",
        "options": ["を契機に", "を機会にすれば", "をめぐって", "に基づいて"],
        "correct_index": 0,
        "translation_vi": "Lấy sự kiện ông nội nhập viện vì bệnh làm bước ngoặt, cả gia đình đã bắt đầu nhìn nhận lại chế độ ăn uống và giữ gìn sức khỏe.",
        "explanation_vi": "Sự kiện bước ngoặt gây tác động dẫn đến sự thay đổi lớn từ đó về sau (kể cả sự kiện không vui như bệnh tật) dùng N + を契機に / をきっかけに.",
        "option_diagnostics": [
            "[ĐÚNG - N + を契機に]: Rất tự nhiên cho bước ngoặt thay đổi thói quen sau biến cố sức khỏe.",
            "[SAI - Lệch sắc thái và sai chia thể]: を機会に thường dùng cho cơ hội tích cực sắp tới để đưa ra quyết tâm chủ động, hơn nữa không chia すれば ở đây.",
            "[SAI - Sai nghĩa]: をめぐって nghĩa là tranh luận xoay quanh.",
            "[SAI - Sai nghĩa]: に基づいて nghĩa là dựa trên quy định/dữ liệu.",
        ],
    },
    {
        "drill_key": "DR-GP-N2-10-A",
        "grammar_code": "GP-N2-10",
        "drill_type": "application",
        "prompt_jp": "高校時代に読んだ一冊の小説（　　）、日本文学の研究者を目指すようになった。",
        "options": ["をきっかけに", "を問わずに", "をかぎりに", "をこめて"],
        "correct_index": 0,
        "translation_vi": "Lấy một cuốn tiểu thuyết đọc hồi cấp ba làm động lực khởi đầu, tôi đã hướng tới trở thành nhà nghiên cứu văn học Nhật Bản.",
        "explanation_vi": "N + をきっかけに diễn tả sự kiện/tác phẩm mang tính cơ duyên khởi phát con đường dài về sau.",
        "option_diagnostics": [
            "[ĐÚNG - N + をきっかけに]: Cơ duyên khởi đầu lý tưởng sống từ cuốn tiểu thuyết.",
            "[SAI - Sai nghĩa]: を問わず là 'bất kể, không phân biệt'.",
            "[SAI - Sai nghĩa]: をかぎりに là 'kể từ mốc này là lần cuối cùng/chấm dứt'.",
            "[SAI - Sai kết hợp]: を込めて là 'gửi gắm trọn vẹn (tình cảm)'.",
        ],
    },
    # --- GP-N2-11 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N2-11-F",
        "grammar_code": "GP-N2-11",
        "drill_type": "formation",
        "prompt_jp": "本番の試験を開始する（　　）、受験番号と氏名の記入漏れがないか確認します。",
        "options": ["に先立って", "に先立った", "を先立って", "から先立って"],
        "correct_index": 0,
        "translation_vi": "Trước khi bắt đầu kỳ thi chính thức, chúng tôi sẽ kiểm tra xem có ghi thiếu số báo danh và họ tên hay không.",
        "explanation_vi": "Thao tác chuẩn bị thực hiện TRƯỚC khi sự kiện chính diễn ra dùng Vる / N + に先立って.",
        "option_diagnostics": [
            "[ĐÚNG - Vる + に先立って]: Trình tự thao tác diễn ra trước thềm sự kiện chính.",
            "[SAI - Sai cấu trúc]: Trước 確認します cần dạng nối trạng ngữ ～に先立って.",
            "[SAI - Sai trợ từ]: Mẫu cố định dùng trợ từ に (に先立って), không dùng を.",
            "[SAI - Sai trợ từ]: Không dùng から先立って.",
        ],
    },
    {
        "drill_key": "DR-GP-N2-11-C",
        "grammar_code": "GP-N2-11",
        "drill_type": "contrast",
        "prompt_jp": "新店舗のオープン（　　）、先着100名様に記念品を配布いたします。",
        "options": ["にあたり", "に先立って", "のすえに", "ばかりに"],
        "correct_index": 0,
        "translation_vi": "Nhân dịp khai trương cửa hàng mới, chúng tôi sẽ phát quà lưu niệm cho 100 quý khách đến sớm đầu tiên.",
        "explanation_vi": "Quà tặng cho 100 khách đầu tiên đến vào dịp khai trương (ngay thời điểm sự kiện mở cửa diễn ra) dùng ～にあたり / ～にあたって; khác với ～に先立って (làm trước ngày mở cửa).",
        "option_diagnostics": [
            "[ĐÚNG - Sự kiện + にあたり]: Phát quà cho 100 khách đầu tiên đến đúng dịp khai trương.",
            "[SAI - Lệch thời điểm]: に先立って nghĩa là phát quà TRƯỚC khi cửa hàng khai trương/mở cửa, không hợp 先着100名様 khi khai trương.",
            "[SAI - Sai sắc thái]: の末に diễn tả kết cục sau quá trình trăn trở vất vả.",
            "[SAI - Sai nghĩa]: ばかりに là 'chỉ tại vì... mà ra hậu quả xấu'.",
        ],
    },
    # --- GP-N2-12 (formation + contrast) ---
    {
        "drill_key": "DR-GP-N2-12-F",
        "grammar_code": "GP-N2-12",
        "drill_type": "formation",
        "prompt_jp": "どんなに頑丈なシステムでも、想定外のエラーは常に（　　）。",
        "options": ["起こり得る", "起こられる得る", "起こる得る", "起きない得る"],
        "correct_index": 0,
        "translation_vi": "Cho dù hệ thống có vững chắc đến đâu, lỗi ngoài dự kiến vẫn luôn có thể xảy ra.",
        "explanation_vi": "Mẫu N2 đánh giá tính khả thi lý thuyết dùng gốc Vます (bỏ ます: 起こり) + 得る（うる / える）.",
        "option_diagnostics": [
            "[ĐÚNG - Vます(bỏ ます) + 得る]: 起こり得る mang nghĩa 'hoàn toàn có khả năng phát sinh'.",
            "[SAI - Lỗi ghép dư bị động]: Không lồng られる vào trước 得る.",
            "[SAI - Sai chia thể]: 得る gắn sau thân Vます (起こり), không gắn sau Vる (起こる).",
            "[SAI - Lỗi cấu tạo phủ định]: Phủ định là thân Vます + 得ない (起こり得ない), không đặt ない trước 得る.",
        ],
    },
    {
        "drill_key": "DR-GP-N2-12-C",
        "grammar_code": "GP-N2-12",
        "drill_type": "contrast",
        "prompt_jp": "厳重に管理されているこの金庫から、外部の人間が書類を持ち出すなど（　　）。",
        "options": ["あり得ない", "ありかねない", "あることができる", "あるまいとしない"],
        "correct_index": 0,
        "translation_vi": "Việc người bên ngoài tuồn tài liệu ra khỏi chiếc két được quản lý nghiêm ngặt này là chuyện tuyệt đối không thể nào xảy ra.",
        "explanation_vi": "Bác bỏ tuyệt đối tính khả thi theo logic ('chuyện đó không thể tồn tại / không đời nào xảy ra') dùng あり得ない.",
        "option_diagnostics": [
            "[ĐÚNG - あり得ない]: Cụm cố định phủ định 100% tính khả thi.",
            "[SAI - Ngược nghĩa]: ありかねない nghĩa là 'e rằng có nguy cơ xảy ra đấy' (mâu thuẫn với từ nghi ngờ mạnh ～など).",
            "[SAI - Sai chủ thể và mẫu]: ことができる chỉ năng lực của người, không đi với chủ ngữ là sự việc 持ち出すなど.",
            "[SAI - Lỗi cấu tạo]: Không dùng cấu trúc あるまいとしない.",
        ],
    },
    # --- GP-N2-13 (contrast + application) ---
    {
        "drill_key": "DR-GP-N2-13-C",
        "grammar_code": "GP-N2-13",
        "drill_type": "contrast",
        "prompt_jp": "忙しすぎて、海外旅行（　　）、週末にゆっくり昼寝をする時間さえない。",
        "options": ["どころか", "ばかりか", "ものの", "だけあって"],
        "correct_index": 0,
        "translation_vi": "Bận rộn quá mức nên đừng nói tới du lịch nước ngoài, đến cả thời gian ngủ trưa thư thả cuối tuần cũng chẳng có.",
        "explanation_vi": "Phủ định hẳn A (du lịch nước ngoài) để nêu thực tế còn tệ hơn ở B (đến cả ngủ trưa cũng không có -> dùng ～どころか... ～さえない).",
        "option_diagnostics": [
            "[ĐÚNG - A + どころか + Bさえない]: Bác bỏ hoàn toàn mức A để nhấn mạnh thực tế B khắc nghiệt hơn nhiều.",
            "[SAI - Nhầm cặp ばかりか]: ばかりか dùng khi A ĐÃ XẢY RA thật rồi cộng thêm B ('không những đã đi du lịch nước ngoài mà còn...'), phi logic với thời gian ngủ còn không có.",
            "[SAI - Sai nghĩa]: ものの là 'tuy nhưng'.",
            "[SAI - Sai nghĩa]: だけあって là 'xứng danh với...'.",
        ],
    },
    {
        "drill_key": "DR-GP-N2-13-A",
        "grammar_code": "GP-N2-13",
        "drill_type": "application",
        "prompt_jp": "彼は謝る（　　）、逆にこちらのやり方が悪いと文句を言ってきた。",
        "options": ["どころか", "ばかりに", "ことに", "ものだから"],
        "correct_index": 0,
        "translation_vi": "Anh ta chẳng những không xin lỗi, mà trái lại còn phàn nàn ngược rằng cách làm của bên mình sai.",
        "explanation_vi": "Diễn đạt kết quả thực tế ở vế sau hoàn toàn trái ngược (lên giọng/tấn công ngược lại thay vì xin lỗi) dùng Vる + どころか.",
        "option_diagnostics": [
            "[ĐÚNG - Vる + どころか + 逆に]: Phủ định việc xin lỗi và nhấn mạnh thái độ ngược hẳn ở vế sau.",
            "[SAI - Sai nghĩa]: ばかりに nghĩa là 'chỉ tại vì xin lỗi mà ra hậu quả xấu'.",
            "[SAI - Sai nghĩa và ngữ pháp]: ことに đứng sau tính từ cảm xúc (残念なことに).",
            "[SAI - Sai quan hệ]: ものだから nghĩa là 'tại vì... nên' (thanh minh).",
        ],
    },
    # --- GP-N2-14 (contrast + application) ---
    {
        "drill_key": "DR-GP-N2-14-C",
        "grammar_code": "GP-N2-14",
        "drill_type": "contrast",
        "prompt_jp": "高価な道具を買いそろえさえすれば、誰でも上達する（　　）。",
        "options": ["というものではない", "にほかならない", "ざるを得ない", "に限らない"],
        "correct_index": 0,
        "translation_vi": "Không phải cứ sắm sửa đủ dụng cụ đắt tiền là ai cũng tiến bộ được đâu.",
        "explanation_vi": "Phản bác nhận định phiến diện ('không phải cứ hễ A là đương nhiên B đâu') bằng nhận xét tổng quát sâu sắc ở N2 dùng 普通形 + というものではない.",
        "option_diagnostics": [
            "[ĐÚNG - Vる + というものではない]: Phản bác suy nghĩ đơn giản hóa quá mức.",
            "[SAI - Ngược nghĩa khẳng định tuyệt đối]: にほかならない nghĩa là 'chính là do điều đó không sai'.",
            "[SAI - Sai ý nghĩa]: ざるを得ない nghĩa là 'đành buộc phải'.",
            "[SAI - Sai kết hợp và sắc thái]: に限らない nghĩa là 'không giới hạn ở một đối tượng', khác mẫu phản bác điều kiện さえ～れば.",
        ],
    },
    {
        "drill_key": "DR-GP-N2-14-A",
        "grammar_code": "GP-N2-14",
        "drill_type": "application",
        "prompt_jp": "健康のために運動が大切だと言っても、毎日何時間も走らなければならない（　　）。",
        "options": ["というわけでもない", "にかかわらない", "にきまっている", "べきものだ"],
        "correct_index": 0,
        "translation_vi": "Tuy nói vận động tốt cho sức khỏe, nhưng cũng không hẳn là ngày nào cũng phải chạy hàng tiếng đồng hồ.",
        "explanation_vi": "Làm dịu và phản bác một mức độ thái quá ('không hẳn đến mức phải...') dùng 普通形 + というわけでもない (thân cận ～というものではない).",
        "option_diagnostics": [
            "[ĐÚNG - 普通形 + というわけでもない]: Giảm nhẹ sự cực đoan của câu khẳng định trước đó.",
            "[SAI - Sai nghĩa]: にかかわらない nghĩa là 'không liên quan tới'.",
            "[SAI - Ngược nghĩa hoàn toàn]: にきまっている khẳng định 'chắc chắn bắt buộc thế'.",
            "[SAI - Ngược nghĩa]: べきものだ khẳng định 'là điều đương nhiên phải làm'.",
        ],
    },
]


# ==============================================================================
# CURATED VOCABULARY & KANJI FOUNDATION (VOCAB_FOUNDATION_CURATED)
# Tổng hợp có hệ thống từ:
# - Từ-vựng-Mimikara-Oboeru-N3.pdf (Units 1-12)
# - N3-Somatome-Kanji-List-VN.pdf (Tuần 1-6)
# - 214-Bo-Thu.pdf (Chiết tự Bộ thủ Khang Hy chuẩn)
# ==============================================================================

VOCAB_FOUNDATION_CURATED: List[Dict[str, Any]] = [
    {
        "vocab_key": "VC-N3-001",
        "word": "申し込む",
        "reading": "もうしこむ",
        "han_viet": "THÂN NHẬP",
        "radical_note": "申 (Bộ Điền 田 mở rộng: thưa, trình) + 込 (Bộ Sước 辶: bước vào)",
        "meaning_vi": "Đăng ký, nộp đơn tham gia",
        "collocation_tip": "試験に申し込む / 申込書 (もうしこみしょ) に記入する [tha động từ V1t]",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.11 + Somatome Tuần 4 Ngày 4",
    },
    {
        "vocab_key": "VC-N3-002",
        "word": "断る",
        "reading": "ことわる",
        "han_viet": "ĐOẠN",
        "radical_note": "Bộ Cân 斤 (cái rìu) + Bộ Yêu 幺 (sợi tơ) -> cắt đứt, từ chối dứt khoát",
        "meaning_vi": "Từ chối, khước từ, báo trước",
        "collocation_tip": "誘いを断る (từ chối lời mời) / 断りなく (mà không xin phép trước)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.12",
    },
    {
        "vocab_key": "VC-N3-003",
        "word": "見つかる・見つける",
        "reading": "みつかる・みつける",
        "han_viet": "KIẾN",
        "radical_note": "Bộ Kiến 見 (bộ 147: nhìn thấy)",
        "meaning_vi": "Được tìm thấy (tự V1i) / Tìm thấy (tha V2t)",
        "collocation_tip": "財布が見つかった (cái ví tự được thấy) vs 財布を見つけた (tôi tìm thấy ví)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.12",
    },
    {
        "vocab_key": "VC-N3-004",
        "word": "直る・直す",
        "reading": "なおる・なおす",
        "han_viet": "TRỰC",
        "radical_note": "Bộ Mục 目 (mắt) + Bộ Thập 十 -> nhìn thẳng chỉnh lại cho ngay ngắn",
        "meaning_vi": "Được sửa xong (tự) / Sửa chữa, điều chỉnh, làm lại (tha)",
        "collocation_tip": "故障が直る / 文章を直す / Vます + 直す (làm lại: かけ直す gọi lại)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.12-13 + Somatome Tuần 5 Ngày 3",
    },
    {
        "vocab_key": "VC-N3-005",
        "word": "治る・治す",
        "reading": "なおる・なおす",
        "han_viet": "TRỊ",
        "radical_note": "Bộ Thủy 氵 (85: nước) + 台 -> trị thủy, chữa lành bệnh tật",
        "meaning_vi": "Khỏi bệnh (tự) / Chữa khỏi bệnh, điều trị (tha)",
        "collocation_tip": "病気が治る / 風邪を治す (Phân biệt 直す sửa đồ vs 治す chữa bệnh)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.13 + Somatome Tuần 5 Ngày 5",
    },
    {
        "vocab_key": "VC-N3-006",
        "word": "流行る",
        "reading": "はやる",
        "han_viet": "LƯU HÀNH",
        "radical_note": "流 (Bộ Thủy 氵: dòng chảy) + 行 (Bộ Hành 行: đi) -> lan truyền rộng",
        "meaning_vi": "Thịnh hành, phổ biến, bùng phát dịch",
        "collocation_tip": "インフルエンザが流行っている / Hán-Nhật: 流行 (りゅうこう) する",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.14",
    },
    {
        "vocab_key": "VC-N3-007",
        "word": "通う",
        "reading": "かよう",
        "han_viet": "THÔNG",
        "radical_note": "Bộ Sước 辶 (162: bước đi) + 甬 -> đi đi về về lặp lại trên một tuyến",
        "meaning_vi": "Đi lại thường xuyên (đến trường, chỗ làm, bệnh viện)",
        "collocation_tip": "大学に通う / 通勤 (つうきん đi làm) / 通学 (つうがく đi học)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.14",
    },
    {
        "vocab_key": "VC-N3-008",
        "word": "片付く・片付ける",
        "reading": "かたづく・かたづける",
        "han_viet": "PHIẾN PHÓ",
        "radical_note": "片 (Bộ Phiến 91: mảnh, phía) + 付 (Bộ Nhân 亻 + Thốn 寸: gắn vào)",
        "meaning_vi": "Được thu dọn gọn gàng, ổn thỏa (tự) / Dọn dẹp, giải quyết (tha)",
        "collocation_tip": "部屋が片付く / 仕事を片付ける (giải quyết xong công việc)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.16 + Somatome Tuần 2 Ngày 5",
    },
    {
        "vocab_key": "VC-N3-009",
        "word": "足りる・欠ける",
        "reading": "たりる・かける",
        "han_viet": "TÚC / KHIẾM",
        "radical_note": "足 (Bộ Túc 157: chân, đầy đủ) vs 欠 (Bộ Khiếm 76: há miệng, thiếu hụt)",
        "meaning_vi": "Đủ (vật chất/số lượng) vs Thiếu sót (trừu tượng)",
        "collocation_tip": "お金が足りない (thiếu tiền) vs 経験が欠けている (thiếu kinh nghiệm)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.17",
    },
    {
        "vocab_key": "VC-N3-010",
        "word": "積もる・積む",
        "reading": "つもる・つむ",
        "han_viet": "TÍCH",
        "radical_note": "Bộ Hòa 禾 (115: lúa) + 責 (Bộ Bối 貝) -> tích trữ, chất đống",
        "meaning_vi": "Tích tụ, phủ dày (tuyết/bụi - tự) / Chất xếp, tích lũy (kinh nghiệm - tha)",
        "collocation_tip": "雪が積もっている / 経験を積む (tích lũy kinh nghiệm)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.17-18",
    },
    {
        "vocab_key": "VC-N3-011",
        "word": "冷える・冷やす",
        "reading": "ひえる・ひやす",
        "han_viet": "LÃNH",
        "radical_note": "Bộ Băng 冫 (15: hai chấm băng) + 令 -> làm lạnh, ướp lạnh",
        "meaning_vi": "Lạnh đi (nhiệt độ cơ thể/phòng/đồ uống - tự) / Làm lạnh, ướp lạnh (tha)",
        "collocation_tip": "ビールをよく冷やす / 体が冷える (Phân biệt 冷める/冷ます: nguội đồ nóng)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.18 + Somatome Tuần 3 Ngày 1",
    },
    {
        "vocab_key": "VC-N3-012",
        "word": "冷める・冷ます",
        "reading": "さめる・さます",
        "han_viet": "LÃNH",
        "radical_note": "Bộ Băng 冫 (15: băng lạnh) -> hạ nhiệt từ trạng thái nóng/nhiệt huyết",
        "meaning_vi": "Nguội đi, mất nhiệt huyết (tự) / Để nguội, làm hạ nhiệt (tha)",
        "collocation_tip": "スープが冷める / 熱い気持ちが冷める (nhiệt huyết nguội lạnh)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.18 + Somatome Tuần 3 Ngày 1",
    },
    {
        "vocab_key": "VC-N3-013",
        "word": "役立つ・役に立つ",
        "reading": "やくだつ・やくにたつ",
        "han_viet": "DỊCH LẬP",
        "radical_note": "役 (Bộ Sách 彳: bước đi + 殳: nhiệm vụ) + 立 (Bộ Lập 117: đứng)",
        "meaning_vi": "Có ích, phát huy tác dụng (tự V1i)",
        "collocation_tip": "勉強に役立つ / の役に立つ / Tha động từ: 情報を役立てる",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.19 + Somatome Tuần 2 Ngày 4",
    },
    {
        "vocab_key": "VC-N3-014",
        "word": "替える・代える・換える",
        "reading": "かえる",
        "han_viet": "THẾ / ĐẠI / HOÁN",
        "radical_note": "替 (thay mới hoàn toàn) / 代 (亻 người thay thế vai trò) / 換 (扌 tay trao đổi)",
        "meaning_vi": "Thay mới / Thay thế vai trò / Trao đổi tương đương",
        "collocation_tip": "席を替える (đổi chỗ) / 命に代える / 円をドルに換える (đổi tiền)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.40",
    },
    {
        "vocab_key": "VC-N3-015",
        "word": "譲る",
        "reading": "ゆずる",
        "han_viet": "NHƯỢNG",
        "radical_note": "Bộ Ngôn 言 (149: lời nói) + 襄 -> dùng lời nhã nhặn nhường quyền lợi",
        "meaning_vi": "Nhường chỗ, nhượng lại tài sản, nhượng bộ",
        "collocation_tip": "お年寄りに席を譲る / 家具を安く譲ってもらう",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.41",
    },
    {
        "vocab_key": "VC-N3-016",
        "word": "隠れる・隠す",
        "reading": "かくれる・かくす",
        "han_viet": "ẨN",
        "radical_note": "Bộ Phụ 阝(170 trái: gò đất che khuất) + 急/心 -> ẩn nấp, che giấu",
        "meaning_vi": "Trốn, khuất sau (tự) / Giấu giếm, che đậy (tha)",
        "collocation_tip": "月が雲に隠れる / 事実を隠す",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.42",
    },
    {
        "vocab_key": "VC-N3-017",
        "word": "詰まる・詰める",
        "reading": "つまる・つめる",
        "han_viet": "CẬT",
        "radical_note": "Bộ Ngôn 言 (149) + 吉 -> dồn chặt, nghẽn lại",
        "meaning_vi": "Bị tắc nghẽn, chật cứng (tự) / Nhét chặt, rút ngắn (tha)",
        "collocation_tip": "鼻が詰まる / 予定が詰まっている / 詰めて座る (ngồi dịch sát vào)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.43",
    },
    {
        "vocab_key": "VC-N3-018",
        "word": "開く・閉じる",
        "reading": "ひらく・とじる",
        "han_viet": "KHAI / BẾ",
        "radical_note": "Bộ Môn 門 (169: cánh cửa) + 開 / 才 -> mở ra hoặc đóng khép cửa",
        "meaning_vi": "Mở (sách/hội nghị/cửa hàng) / Đóng, gấp sách, nhắm mắt",
        "collocation_tip": "会議を開く (tổ chức họp) / 本・目・ふた を閉じる",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.43",
    },
    {
        "vocab_key": "VC-N3-019",
        "word": "確かめる・試す",
        "reading": "たしかめる・ためす",
        "han_viet": "XÁC / THÍ",
        "radical_note": "確 (Bộ Thạch 石: đá chắc) / 試 (Bộ Ngôn 言: lời + 式: thử nghiệm)",
        "meaning_vi": "Xác nhận cho rõ ràng / Thử nghiệm giới hạn hoặc trải nghiệm",
        "collocation_tip": "事実を確かめる / 新しい方法を試してみる",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.44",
    },
    {
        "vocab_key": "VC-N3-020",
        "word": "慣れる・慣らす",
        "reading": "なれる・ならす",
        "han_viet": "QUÁN",
        "radical_note": "Bộ Tâm 忄(61: tinh thần) + 貫 -> quen thuộc trong tâm",
        "meaning_vi": "Quen với, thích ứng (tự) / Rèn cho quen (tha)",
        "collocation_tip": "日本の生活に慣れる / 体を寒さに慣らす",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.45",
    },
    {
        "vocab_key": "VC-N3-021",
        "word": "育つ・育てる",
        "reading": "そだつ・そだてる",
        "han_viet": "DỤC",
        "radical_note": "Bộ Nhục 月(130) + 亠ム -> nuôi dưỡng cơ thể lớn lên",
        "meaning_vi": "Lớn lên, phát triển (tự) / Nuôi nấng, trồng trọt, đào tạo (tha)",
        "collocation_tip": "子どもが元気に育つ / 植物・後輩 を育てる",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.45",
    },
    {
        "vocab_key": "VC-N3-022",
        "word": "汚れる・汚す",
        "reading": "よごれる・よごす",
        "han_viet": "Ô",
        "radical_note": "Bộ Thủy 氵(85: nước) + 于 -> nước vẩn đục, làm bẩn",
        "meaning_vi": "Bị bẩn, vấy bẩn (tự) / Làm bẩn, gây ô nhiễm (tha)",
        "collocation_tip": "シャツが汚れる / 川を汚す (Tính từ: 汚い きたない bẩn thỉu)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.45 + Somatome Tuần 5 Ngày 5",
    },
    {
        "vocab_key": "VC-N3-023",
        "word": "壊れる・壊す",
        "reading": "こわれる・こわす",
        "han_viet": "HOẠI",
        "radical_note": "Bộ Thổ 土 (32: đất) -> sụp đổ, hư hỏng cấu trúc",
        "meaning_vi": "Bị hỏng, đổ vỡ (tự) / Làm hỏng, phá hủy (tha)",
        "collocation_tip": "パソコンが壊れる / お腹を壊す (đau bụng) / 健康を壊す",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.46",
    },
    {
        "vocab_key": "VC-N3-024",
        "word": "割れる・割る",
        "reading": "われる・わる",
        "han_viet": "CÁT",
        "radical_note": "Bộ Đao 刂 (18: dao) + 害 -> dùng dao cắt chia tách làm nhiều mảnh",
        "meaning_vi": "Bị vỡ, nứt (tự) / Làm vỡ, đập trứng, chia tỷ lệ (tha)",
        "collocation_tip": "ガラスが割れる / 100を4で割る / 割合 (わりあい tỷ lệ) / 割引 (chiết khấu)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.46 + Somatome Tuần 4 Ngày 2",
    },
    {
        "vocab_key": "VC-N3-025",
        "word": "折れる・折る",
        "reading": "おれる・おる",
        "han_viet": "CHIẾT",
        "radical_note": "Bộ Thủ 扌(64: tay) + Bộ Cân 斤(69: rìu) -> chặt, bẻ gãy",
        "meaning_vi": "Bị gãy, rẽ (tự) / Bẻ gãy, gấp giấy (tha)",
        "collocation_tip": "骨が折れる (gãy xương / tốn công sức) / 折り紙 / 右折・左折 (rẽ phải/trái)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.46 + Somatome Tuần 2 Ngày 5",
    },
    {
        "vocab_key": "VC-N3-026",
        "word": "迷う・悩む",
        "reading": "まよう・なやむ",
        "han_viet": "MÊ / NÃO",
        "radical_note": "迷 (Bộ Sước 辶: lạc lối) vs 悩 (Bộ Tâm 忄: phiền muộn trong lòng)",
        "meaning_vi": "Lạc đường, lưỡng lự chọn lựa / Lo âu, trăn trở, băn khoăn",
        "collocation_tip": "道に迷う / どちらを買うか迷う vs 将来のことで悩む",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.47",
    },
    {
        "vocab_key": "VC-N3-027",
        "word": "慌てる・焦る",
        "reading": "あわてる・あせる",
        "han_viet": "HOẢNG / TIÊU",
        "radical_note": "慌 (Bộ Tâm 忄: hoảng hốt) vs 焦 (Bộ Hỏa 灬: nóng ruột như lửa đốt)",
        "meaning_vi": "Hấp tấp, cuống cuồng (hành động) / Sốt ruột, nôn nóng (tâm trạng)",
        "collocation_tip": "慌てて家を出た / 結果が出なくて焦る",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.48",
    },
    {
        "vocab_key": "VC-N3-028",
        "word": "移る・移す",
        "reading": "うつる・うつす",
        "han_viet": "DI",
        "radical_note": "Bộ Hòa 禾 (115: lúa) + 多 -> di chuyển mùa vụ sang chỗ khác",
        "meaning_vi": "Chuyển chỗ, lây bệnh, lan lửa (tự) / Di dời, lây sang, đưa vào thực tế (tha)",
        "collocation_tip": "風邪が移る / 考えを実行に移す (biến ý tưởng thành hành động)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.68 + Somatome Tuần 5 Ngày 2",
    },
    {
        "vocab_key": "VC-N3-029",
        "word": "伸ばす・延ばす",
        "reading": "のばす",
        "han_viet": "THÂN / DUYÊN",
        "radical_note": "伸 (亻 người duỗi thẳng) vs 延 (廴 bước dài kéo giãn thời gian)",
        "meaning_vi": "Duỗi thẳng, phát triển năng lực / Gia hạn thời gian, trì hoãn",
        "collocation_tip": "能力を伸ばす・手を伸ばす vs 締切を延ばす (hoãn hạn chót)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.72",
    },
    {
        "vocab_key": "VC-N3-030",
        "word": "重なる・重ねる",
        "reading": "かさなる・かさねる",
        "han_viet": "TRỌNG",
        "radical_note": "Bộ Lý 里 (166) biến thể -> chồng lớp lên nhau",
        "meaning_vi": "Trùng lịch, chồng chất (tự) / Xếp chồng, lặp đi lặp lại nỗ lực (tha)",
        "collocation_tip": "予定が重なる / 失敗を何度も重ねる / 重要 (じゅうよう) / 貴重 (きちょう)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.73",
    },
    {
        "vocab_key": "VC-N3-031",
        "word": "解ける・溶ける",
        "reading": "とける",
        "han_viet": "GIẢI / DUNG",
        "radical_note": "解 (Bộ Giác 角 + 刀: tháo gỡ) vs 溶 (Bộ Thủy 氵: tan chảy trong nước)",
        "meaning_vi": "Được cởi trói, hóa giải hiểu lầm, tuyết tan / Tan chảy (đường, băng)",
        "collocation_tip": "誤解が解ける (xóa tan hiểu nhầm) vs 砂糖が水に溶ける (đường tan)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.75 + Somatome Tuần 2 Ngày 2",
    },
    {
        "vocab_key": "VC-N3-032",
        "word": "現れる・表れる",
        "reading": "あらわれる",
        "han_viet": "HIỆN / BIỂU",
        "radical_note": "現 (Bộ Ngọc 王: ánh ngọc lộ ra) vs 表 (Bộ Y 衣: bề mặt lộ ra)",
        "meaning_vi": "Xuất hiện (người/triệu chứng/kết quả) / Bộc lộ ra ngoài (cảm xúc/chỉ dấu)",
        "collocation_tip": "効果・症状が現れる vs 顔に喜びが表れる",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.75-76",
    },
    {
        "vocab_key": "VC-N3-033",
        "word": "散る・散らす",
        "reading": "ちる・ちらす",
        "han_viet": "TÁN",
        "radical_note": "Bộ Phộc 攵 (66: đánh nhẹ) -> rụng tản mát ra xung quanh",
        "meaning_vi": "Hoa rụng, mây tan, mất tập trung (tự) / Phân tán, rải (tờ rơi) (tha)",
        "collocation_tip": "桜が散る / 気を散らす (làm xao nhãng) / 散らかす (bày bừa bãi)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.76",
    },
    {
        "vocab_key": "VC-N3-034",
        "word": "済む・済ませる",
        "reading": "すむ・すませる",
        "han_viet": "TẾ",
        "radical_note": "Bộ Thủy 氵 (85: nước) + 斉 -> qua sông, hoàn tất công việc",
        "meaning_vi": "Xong xuôi, kết thúc ổn thỏa (tự) / Giải quyết cho xong (tha)",
        "collocation_tip": "用事が済む / ～なくて済む (không cần làm cũng ổn) / 経済 (けいざい)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.71 + Somatome Tuần 6 Ngày 4",
    },
    {
        "vocab_key": "VC-N3-035",
        "word": "炊く・煮る・焼く",
        "reading": "たく・にる・やく",
        "han_viet": "XUY / CHỬ / THIÊU",
        "radical_note": "Đều mang Bộ Hỏa 火/灬 (86: lửa dùng chế biến món ăn)",
        "meaning_vi": "Nấu cơm (không nêm) / Kho, ninh (có nêm) / Nướng, rán",
        "collocation_tip": "ご飯を炊く / 野菜を煮る / パン・肉 を焼く",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.78",
    },
    {
        "vocab_key": "VC-N3-036",
        "word": "得意・苦手",
        "reading": "とくい・にがて",
        "han_viet": "ĐẮC Ý / KHỔ THỦ",
        "radical_note": "得 (彳: bước đi + 寸) + 意 (心: ý); 苦 (艹: đắng) + 手 (tay)",
        "meaning_vi": "Giỏi, sở trường (tính từ な) vs Kém, ngại làm (tính từ な)",
        "collocation_tip": "料理が得意だ / 人前で話すのが苦手だ (trợ từ が)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.23",
    },
    {
        "vocab_key": "VC-N3-037",
        "word": "熱心・夢中",
        "reading": "ねっしん・むちゅう",
        "han_viet": "NHIỆT TÂM / MỘNG TRUNG",
        "radical_note": "熱 (灬 lửa) + 心 (tâm); 夢 (艹 + 夕: giấc mơ) + 中",
        "meaning_vi": "Nhiệt tâm, tận tụy / Say mê quên hết xung quanh",
        "collocation_tip": "仕事に熱心だ / ゲームに夢中になる (đi kèm trợ từ に)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.23 + Somatome Tuần 5 Ngày 5",
    },
    {
        "vocab_key": "VC-N3-038",
        "word": "退屈・苦しい",
        "reading": "たいくつ・くるしい",
        "han_viet": "THỐI KHUẤT / KHỔ",
        "radical_note": "退 (辶: lùi) + 屈 (尸: uốn cong); 苦 (艹: vị đắng)",
        "meaning_vi": "Buồn chán, tẻ nhạt / Khổ sở, khó nhọc (thể chất lẫn tinh thần)",
        "collocation_tip": "退屈な映画 / 息が苦しい (khó thở) / 苦しむ (đau khổ vì ~に)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.23",
    },
    {
        "vocab_key": "VC-N3-039",
        "word": "悔しい・後悔する",
        "reading": "くやしい・こうかいする",
        "han_viet": "HỐI / HẬU HỐI",
        "radical_note": "悔 mang Bộ Tâm 忄(61: nỗi day dứt trong lòng) + 毎",
        "meaning_vi": "Cay cú, ấm ức tiếc nuối / Hối hận vì chuyện đã qua",
        "collocation_tip": "負けて悔しい / あの時の選択を後悔している",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.23",
    },
    {
        "vocab_key": "VC-N3-040",
        "word": "正直",
        "reading": "しょうじき",
        "han_viet": "CHÍNH TRỰC",
        "radical_note": "正 (止 dừng đúng mực) + 直 (ngay thẳng)",
        "meaning_vi": "Trung thực, thẳng thắn; thực tình mà nói",
        "collocation_tip": "正直な人 / 正直に言うと (thành thực mà nói thì)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.24",
    },
    {
        "vocab_key": "VC-N3-041",
        "word": "濃い・薄い",
        "reading": "こい・うすい",
        "han_viet": "NÙNG / BẠC",
        "radical_note": "濃 (Bộ Thủy 氵: đặc quánh) vs 薄 (Bộ Thảo 艹 + 氵: mỏng, nhạt)",
        "meaning_vi": "Đậm đặc, màu sẫm / Mỏng, nhạt vị, thưa thớt",
        "collocation_tip": "味が濃い・霧が濃い vs 本が薄い・色が薄い",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.51",
    },
    {
        "vocab_key": "VC-N3-042",
        "word": "詳しい・細かい",
        "reading": "くわしい・こまかい",
        "han_viet": "TƯỜNG / TẾ",
        "radical_note": "詳 (Bộ Ngôn 言: lời nói rõ ràng) vs 細 (Bộ Mịch 糸: sợi tơ mảnh nhỏ)",
        "meaning_vi": "Am hiểu tường tận, chi tiết / Nhỏ nhặt, chi li, tiền lẻ",
        "collocation_tip": "歴史に詳しい (rành về lịch sử) / 細かいお金 (tiền lẻ)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.52",
    },
    {
        "vocab_key": "VC-N3-043",
        "word": "固い・硬い",
        "reading": "かたい",
        "han_viet": "CỐ / NGẠNH",
        "radical_note": "固 (Bộ Vi 囗: rào kín vững chắc) vs 硬 (Bộ Thạch 石: cứng như đá)",
        "meaning_vi": "Bền chặt, kiên quyết / Cứng rắn (vật lý, biểu cảm cứng đờ)",
        "collocation_tip": "固い約束・固く信じる vs 硬いパン・硬い表情",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.52",
    },
    {
        "vocab_key": "VC-N3-044",
        "word": "清潔・新鮮",
        "reading": "せいけつ・しんせん",
        "han_viet": "THANH KHIẾT / TÂN TIÊN",
        "radical_note": "清・潔 đều có Bộ Thủy 氵(85: nước rửa sạch); 鮮 (Bộ Ngư 魚 + Dương 羊: cá thịt tươi)",
        "meaning_vi": "Sạch sẽ, hợp vệ sinh / Tươi ngon, mới mẻ",
        "collocation_tip": "手を清潔に保つ / 新鮮な野菜・新鮮な空気",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.52",
    },
    {
        "vocab_key": "VC-N3-045",
        "word": "豊か・裕福",
        "reading": "ゆたか・ゆうふく",
        "han_viet": "PHONG / DỤ PHÚC",
        "radical_note": "裕・福 đều có Bộ Y 衤 / Bộ Thị 礻(áo ấm cơm no, phúc lộc)",
        "meaning_vi": "Phong phú, dồi dào (tài nguyên, kinh nghiệm) / Giàu có (tiền bạc)",
        "collocation_tip": "自然・経験が豊かだ vs 裕福な家庭 (không dùng 豊か chỉ nhiều tiền)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.52-53",
    },
    {
        "vocab_key": "VC-N3-046",
        "word": "正確・確か",
        "reading": "せいかく・たしか",
        "han_viet": "CHÍNH XÁC / XÁC",
        "radical_note": "確 (Bộ Thạch 石: đá tảng chắc chắn, đáng tin)",
        "meaning_vi": "Chính xác tuyệt đối (số liệu, máy móc) / Chắc chắn; nếu nhớ không nhầm thì...",
        "collocation_tip": "正確な時間・情報 vs 確か明日は休みだったはずだ",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.53",
    },
    {
        "vocab_key": "VC-N3-047",
        "word": "激しい・ひどい",
        "reading": "はげしい・ひどい",
        "han_viet": "KÍCH / KHỐC",
        "radical_note": "激 (Bộ Thủy 氵: sóng trào + 攵) vs 酷 (Bộ Dậu 酉: rượu nồng -> cay nghiệt)",
        "meaning_vi": "Dữ dội, mãnh liệt (mưa gió, cạnh tranh) / Quá đáng, tồi tệ",
        "collocation_tip": "激しい雨・激しい運動 / ひどい言葉 (lời nói quá đáng)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.53",
    },
    {
        "vocab_key": "VC-N3-048",
        "word": "適当",
        "reading": "てきとう",
        "han_viet": "THÍCH ĐƯƠNG",
        "radical_note": "適 (Bộ Sước 辶: phù hợp bước đi) + 当 (đúng khớp)",
        "meaning_vi": "1) Phù hợp, vừa phải; 2) Làm qua loa, thiếu trách nhiệm (2 nghĩa trái ngược!)",
        "collocation_tip": "適当なサイズ (cỡ vừa) vs 適当に答える (trả lời bừa cho xong)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.54 + Somatome Tuần 5 Ngày 3",
    },
    {
        "vocab_key": "VC-N3-049",
        "word": "非常に・ほとんど",
        "reading": "ひじょうに・ほとんど",
        "han_viet": "PHI THƯỜNG",
        "radical_note": "非 (Bộ Phi 175: khác thường) + 常 (Bộ Cân 巾: bình thường)",
        "meaning_vi": "Cực kỳ, vô cùng / Hầu hết, gần như toàn bộ (đi cả khẳng & phủ định)",
        "collocation_tip": "非常に重要だ / ほとんど毎日 / お金がほとんどない",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.55",
    },
    {
        "vocab_key": "VC-N3-050",
        "word": "かなり・ずいぶん",
        "reading": "かなり・ずいぶん",
        "han_viet": "TÙY PHÂN",
        "radical_note": "随 (Bộ Phụ 阝 + 辶) + 分 (Bộ Đao 刀: phần)",
        "meaning_vi": "Khá là, đáng kể (trên mức kỳ vọng một chút) / Rất nhiều (gây ngạc nhiên)",
        "collocation_tip": "かなり時間がかかった / ずいぶん涼しくなりましたね",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.55",
    },
    {
        "vocab_key": "VC-N3-051",
        "word": "ぴったり・ぎりぎり",
        "reading": "ぴったり・ぎりぎり",
        "han_viet": "Tượng hình - phó từ",
        "radical_note": "Phó từ mô phỏng trạng thái (gọi là 擬態語 gitaigo hay thi N3)",
        "meaning_vi": "Vừa khít, đúng y, rất hợp / Sát nút, cận kề giới hạn cuối",
        "collocation_tip": "サイズがぴったりだ / 締切ぎりぎりに提出する",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.55-56",
    },
    {
        "vocab_key": "VC-N3-052",
        "word": "あらかじめ・前もって",
        "reading": "あらかじめ・まえもって",
        "han_viet": "TIỀN",
        "radical_note": "前 (Bộ Đao 刂: phía trước về thời gian)",
        "meaning_vi": "Chuẩn bị sẵn từ trước để đón sự kiện sắp tới / Làm trước",
        "collocation_tip": "会議室をあらかじめ予約する / 欠席の場合は前もって連絡する",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.56",
    },
    {
        "vocab_key": "VC-N3-053",
        "word": "必ず・決して",
        "reading": "かならず・けっして",
        "han_viet": "TẤT / QUYẾT",
        "radical_note": "必 (Bộ Tâm 心: kiên quyết trong tâm) vs 決 (Bộ Thủy 氵 + 夬: quyết đoán)",
        "meaning_vi": "Chắc chắn, nhất định luôn luôn / Quyết không bao giờ (+ ～ない)",
        "collocation_tip": "必ず確認してください vs 決して忘れません (bắt buộc đi với phủ định)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.79-80 + Somatome Tuần 3 Ngày 1",
    },
    {
        "vocab_key": "VC-N3-054",
        "word": "少なくとも",
        "reading": "すくなくとも",
        "han_viet": "THIỂU",
        "radical_note": "少 (Bộ Tiểu 小: ít) + động từ dạng cổ とも",
        "meaning_vi": "Ít nhất thì, tối thiểu là (đối nghĩa với 多くとも nhiều nhất)",
        "collocation_tip": "少なくとも1日30分は勉強する",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.80",
    },
    {
        "vocab_key": "VC-N3-055",
        "word": "どうしても・とても",
        "reading": "どうしても・とても",
        "han_viet": "Phó từ N3",
        "radical_note": "Khi đi với thể phủ định ～ない sẽ mang sắc thái bất khả kháng cực mạnh",
        "meaning_vi": "Dù thế nào cũng; (+ ～ない: không tài nào nổi) / Rất; (+ ～ない: tuyệt đối không thể)",
        "collocation_tip": "どうしても思い出せない / 私にはとてもできない",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.80-81",
    },
    {
        "vocab_key": "VC-N3-056",
        "word": "まるで・一体",
        "reading": "まるで・いったい",
        "han_viet": "NHẤT THỂ",
        "radical_note": "体 (Bộ Nhân 亻: người + 本: gốc)",
        "meaning_vi": "Cứ như thể là (+ ようだ/みたいだ) / Rốt cuộc thì (+ Nghi vấn từ)",
        "collocation_tip": "まるで夢のようだ / 一体何が起こったのだろう",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.81",
    },
    {
        "vocab_key": "VC-N3-057",
        "word": "費用・消費",
        "reading": "ひよう・しょうひ",
        "han_viet": "PHÍ DỤNG / TIÊU PHÍ",
        "radical_note": "費 (Bộ Bối 貝 154: tiền tài + 弗: phân tán chi tiêu) + 用 / 消",
        "meaning_vi": "Chi phí nói chung / Sự tiêu dùng, tiêu thụ",
        "collocation_tip": "消費者 (しょうひしゃ người tiêu dùng) / 消費税 (thuế tiêu dùng) / 旅費",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 3 Ngày 2 & Tuần 4 Ngày 3",
    },
    {
        "vocab_key": "VC-N3-058",
        "word": "期限・限定",
        "reading": "きげん・げんてい",
        "han_viet": "KỲ HẠN / HẠN ĐỊNH",
        "radical_note": "期 (Bộ Nguyệt 月: chu kỳ trăng) + 限 (Bộ Phụ 阝: ranh giới + 艮)",
        "meaning_vi": "Thời hạn, hạn chót / Giới hạn phạm vi, phiên bản giới hạn",
        "collocation_tip": "賞味期限 (hạn dùng ngon nhất) / 期間 (khoảng thời gian) / 限度",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 3 Ngày 2",
    },
    {
        "vocab_key": "VC-N3-059",
        "word": "製造・製品",
        "reading": "せいぞう・せいひん",
        "han_viet": "CHẾ TẠO / CHẾ PHẨM",
        "radical_note": "製 (Bộ Y 衣: cắt may -> chế tác) + 造 (Bộ Sước 辶) / 品 (Bộ Khẩu 口 x3)",
        "meaning_vi": "Sản xuất, chế tạo / Sản phẩm hoàn thiện",
        "collocation_tip": "日本製の製品 / 自動車を製造する",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 3 Ngày 2",
    },
    {
        "vocab_key": "VC-N3-060",
        "word": "価格・定価",
        "reading": "かかく・ていか",
        "han_viet": "GIÁ CÁCH / ĐỊNH GIÁ",
        "radical_note": "価 (Bộ Nhân 亻 + 西/覀) + 格 (Bộ Mộc 木: khuôn mẫu); 定 (Bộ Miên 宀)",
        "meaning_vi": "Giá cả thị trường / Giá niêm yết cố định",
        "collocation_tip": "価格が上がる / 定価の半額 (giảm nửa giá niêm yết) / 格安 (giá hời)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 4 Ngày 3",
    },
    {
        "vocab_key": "VC-N3-061",
        "word": "広告・割引",
        "reading": "こうこく・わりびき",
        "han_viet": "QUẢNG CÁO / CÁT DẪN",
        "radical_note": "広 (Bộ Nghiễm 广: mái nhà rộng) + 告 (Bộ Khẩu 口); 引 (Bộ Cung 弓: kéo giảm)",
        "meaning_vi": "Quảng cáo / Chiết khấu, giảm giá",
        "collocation_tip": "広告を出す / 3割引 (giảm 30%) / 値上げ・値下げ (tăng/giảm giá)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 4 Ngày 2",
    },
    {
        "vocab_key": "VC-N3-062",
        "word": "登録・記録",
        "reading": "とうろく・きろく",
        "han_viet": "ĐĂNG LỤC / KÝ LỤC",
        "radical_note": "録 mang Bộ Kim 釒(167: khắc lên kim loại để lưu giữ); 記 mang Bộ Ngôn 言",
        "meaning_vi": "Đăng ký tài khoản/thông tin / Ghi chép, kỷ lục",
        "collocation_tip": "会員登録する / 記録を残す / 録音・録画 (ghi âm / ghi hình)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 3 Ngày 6",
    },
    {
        "vocab_key": "VC-N3-063",
        "word": "予報・予防・予約",
        "reading": "よほう・よぼう・よやく",
        "han_viet": "DỰ BÁO / DỰ PHÒNG / DỰ ƯỚC",
        "radical_note": "予 (Bộ Quyết 亅: biết trước) + 報 (báo) / 防 (阝 ngăn) / 約 (糸 ước hẹn)",
        "meaning_vi": "Dự báo / Phòng ngừa / Đặt chỗ trước",
        "collocation_tip": "天気予報 / 病気を予防する / レストランを予約する",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 2 Ngày 6 & Tuần 6 Ngày 1",
    },
    {
        "vocab_key": "VC-N3-064",
        "word": "保存・存在",
        "reading": "ほぞん・そんざい",
        "han_viet": "BẢO TỒN / TỒN TẠI",
        "radical_note": "保 (Bộ Nhân 亻: người giữ đứa trẻ) + 存 (Bộ Tử 子: tồn tại)",
        "meaning_vi": "Bảo quản, lưu trữ / Sự tồn tại",
        "collocation_tip": "データを保存する / 常温で保存 / ご存じですか (kính ngữ 'biết')",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 3 Ngày 1",
    },
    {
        "vocab_key": "VC-N3-065",
        "word": "冷凍庫・冷蔵庫",
        "reading": "れいとうこ・れいぞうこ",
        "han_viet": "LÃNH ĐÔNG KHỐ / LÃNH TÀNG KHỐ",
        "radical_note": "冷・凍 (Bộ Băng 冫) + 蔵 (Bộ Thảo 艹: cất giấu) + 庫 (Bộ Nghiễm 广: kho)",
        "meaning_vi": "Ngăn/Tủ đông đá vs Tủ lạnh bảo quản",
        "collocation_tip": "冷凍食品 / 冷蔵庫に入れる / 車庫 (しゃこ nhà để xe)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 3 Ngày 1",
    },
    {
        "vocab_key": "VC-N3-066",
        "word": "調査・強調",
        "reading": "ちょうさ・きょうちょう",
        "han_viet": "ĐIỀU TRA / CƯỜNG ĐIỀU",
        "radical_note": "調 (Bộ Ngôn 言: lời + 周: chu đáo -> kiểm tra điều phối) + 査 (Bộ Mộc 木)",
        "meaning_vi": "Điều tra, khảo sát / Nhấn mạnh, cường điệu",
        "collocation_tip": "原因を調査する / 調子 (ちょうし tình trạng) / 重要性を強調する",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 5 Ngày 2",
    },
    {
        "vocab_key": "VC-N3-067",
        "word": "困難・簡単",
        "reading": "こんなん・かんたん",
        "han_viet": "KHỐN NAN / GIẢN ĐƠN",
        "radical_note": "困 (Bộ Vi 囗: bao vây + 木: cây bị nhốt -> khốn khó); 簡 (Bộ Trúc 竹: thẻ tre)",
        "meaning_vi": "Khó khăn, trở ngại / Đơn giản, dễ hiểu",
        "collocation_tip": "解決が困難だ / 簡単な説明 / 単語 (たんご) / 単位 (たんい)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 5 Ngày 2",
    },
    {
        "vocab_key": "VC-N3-068",
        "word": "回復・復習",
        "reading": "かいふく・ふくしゅう",
        "han_viet": "HỒI PHỤC / PHỤC TẬP",
        "radical_note": "復 (Bộ Sách 彳: quay trở lại bước cũ) + 習 (Bộ Vũ 羽: chim non tập bay)",
        "meaning_vi": "Bình phục, khôi phục / Ôn tập lại bài cũ",
        "collocation_tip": "体力が回復する / 往復 (おうふく khứ hồi) / 予習と復習",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 5 Ngày 3",
    },
    {
        "vocab_key": "VC-N3-069",
        "word": "連絡・交通",
        "reading": "れんらく・こうつう",
        "han_viet": "LIÊN LẠC / GIAO THÔNG",
        "radical_note": "連 (辶 + 車: xe nối nhau) + 絡 (糸: sợi dây nối) + 通 (辶: thông suốt)",
        "meaning_vi": "Liên lạc, báo tin / Giao thông, đi lại",
        "collocation_tip": "連休 (れんきゅう kỳ nghỉ dài) / 交差点 (ngã tư) / 交通が便利だ",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 2 Ngày 4 & Tuần 4 Ngày 4",
    },
    {
        "vocab_key": "VC-N3-070",
        "word": "配達・荷物",
        "reading": "はいたつ・にもつ",
        "han_viet": "PHỐI ĐẠT / HÀ VẬT",
        "radical_note": "配 (Bộ Dậu 酉) + 達 (Bộ Sước 辶); 荷 (Bộ Thảo 艹 + 何: gánh hàng hóa)",
        "meaning_vi": "Giao hàng, phân phát / Hành lý, bưu kiện",
        "collocation_tip": "宅配便 (chuyển phát tận nhà) / 配送料 / 入荷・出荷 (nhập/xuất hàng)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 4 Ngày 5",
    },
    {
        "vocab_key": "VC-N3-071",
        "word": "預金・預ける",
        "reading": "よきん・あずける",
        "han_viet": "DỰ KIM / DỰ",
        "radical_note": "預 (Bộ Hiệt 頁: đầu, mặt) + 予 -> gửi gắm tin cậy; đối cặp 預かる (nhận giữ hộ)",
        "meaning_vi": "Tiền gửi ngân hàng / Gửi nhờ, giao phó",
        "collocation_tip": "荷物を預ける (gửi hành lý) vs 荷物を預かる (giữ hộ hành lý cho khách)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 4 Ngày 6",
    },
    {
        "vocab_key": "VC-N3-072",
        "word": "参加・参考書",
        "reading": "さんか・さんこうしょ",
        "han_viet": "THAM GIA / THAM KHẢO THƯ",
        "radical_note": "参 (Bộ Tư 厶 + 彡) + 加 (Bộ Lực 力 + Khẩu 口: thêm sức vào)",
        "meaning_vi": "Tham gia sự kiện / Sách tham khảo",
        "collocation_tip": "会議に参加する / 参る (khiêm nhường của 行く・来る)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 4 Ngày 6",
    },
    {
        "vocab_key": "VC-N3-073",
        "word": "通勤・携帯",
        "reading": "つうきん・けいたい",
        "han_viet": "THÔNG CẦN / HUỀ ĐỚI",
        "radical_note": "勤 (Bộ Lực 力: dốc sức làm việc); 携 (Bộ Thủ 扌: mang theo bên tay)",
        "meaning_vi": "Đi làm hằng ngày / Mang theo bên mình (điện thoại di động)",
        "collocation_tip": "会社に勤める / 携帯電話 / 時間帯 (khung giờ)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 4 Ngày 6",
    },
    {
        "vocab_key": "VC-N3-074",
        "word": "遅刻・失礼",
        "reading": "ちこく・しつれい",
        "han_viet": "TRÌ KHẮC / THẤT LỄ",
        "radical_note": "遅 (Bộ Sước 辶: bước chậm) + 刻 (刂); 失 (Bộ Đại 大: để tuột mất) + 礼 (礻)",
        "meaning_vi": "Đi muộn giờ hẹn / Thất lễ; câu xin phép lịch sự 'Xin thất lễ'",
        "collocation_tip": "授業に遅刻する / 遅れる (đến trễ) / お先に失礼します",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 5 Ngày 1",
    },
    {
        "vocab_key": "VC-N3-075",
        "word": "残念・記念",
        "reading": "ざんねん・きねん",
        "han_viet": "TÀN NIỆM / KỶ NIỆM",
        "radical_note": "念 (Bộ Tâm 心: giữ mãi trong lòng) + 今",
        "meaning_vi": "Đáng tiếc / Kỷ niệm, vật/sự kiện ghi dấu ấn",
        "collocation_tip": "残念ながら (rất tiếc là...) / 記念写真を撮る",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 5 Ngày 1",
    },
    {
        "vocab_key": "VC-N3-076",
        "word": "笑顔・涙",
        "reading": "えがお・なみだ",
        "han_viet": "TIẾU NHAN / LỆ",
        "radical_note": "笑 (Bộ Trúc 竹 + 夭: cười rộ); 涙 (Bộ Thủy 氵: nước từ mắt + 戻)",
        "meaning_vi": "Khuôn mặt tươi cười / Nước mắt",
        "collocation_tip": "笑顔であいさつする / 涙を流す (rơi nước mắt)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 5 Ngày 1",
    },
    {
        "vocab_key": "VC-N3-077",
        "word": "感動・感想・予想",
        "reading": "かんどう・かんそう・よそう",
        "han_viet": "CẢM ĐỘNG / CẢM TƯỞNG / DỰ TƯỞNG",
        "radical_note": "感 và 想 đều mang Bộ Tâm 心 (61: rung động tâm trí)",
        "meaning_vi": "Cảm động, xúc động / Cảm nghĩ, cảm tưởng / Dự đoán trước",
        "collocation_tip": "映画に感動する / 感想を述べる / 予想どおり (đúng như dự đoán)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 5 Ngày 2",
    },
    {
        "vocab_key": "VC-N3-078",
        "word": "快適・選択",
        "reading": "かいてき・せんたく",
        "han_viet": "KHOÁI THÍCH / TUYỂN TRẠCH",
        "radical_note": "快 (Bộ Tâm 忄: dễ chịu trong lòng); 選 (辶 + 巽: chọn lựa bước đi)",
        "meaning_vi": "Thoải mái, dễ chịu / Lựa chọn",
        "collocation_tip": "快適な生活 / 選挙 (bầu cử) / 選手 (tuyển thủ) / 選ぶ (lựa chọn)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 5 Ngày 3",
    },
    {
        "vocab_key": "VC-N3-079",
        "word": "結婚・お祝い",
        "reading": "けっこん・おいわい",
        "han_viet": "KẾT HÔN / CHÚC",
        "radical_note": "結 (糸 nối) + 婚 (女 phụ nữ lấy chồng); 祝 (Bộ Thị 礻: tế lễ cầu phúc)",
        "meaning_vi": "Kết hôn / Lời chúc mừng, quà mừng",
        "collocation_tip": "婚約 (đính hôn) / 祝日 (ngày lễ quốc gia) / 結局 (kết cục thì)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 5 Ngày 4",
    },
    {
        "vocab_key": "VC-N3-080",
        "word": "頭痛・腹痛",
        "reading": "ずつう・ふくつう",
        "han_viet": "ĐẦU THỐNG / PHÚC THỐNG",
        "radical_note": "痛 mang Bộ Nạch 疒(104: bệnh tật đau đớn); 腹 mang Bộ Nhục 月(130: bộ phận cơ thể)",
        "meaning_vi": "Đau đầu / Đau bụng",
        "collocation_tip": "頭が痛い / 歯医者・歯科 (nha khoa) / 虫歯 (răng sâu)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 5 Ngày 5",
    },
    {
        "vocab_key": "VC-N3-081",
        "word": "治療・健康",
        "reading": "ちりょう・けんこう",
        "han_viet": "TRỊ LIỆU / KIỆN KHANG",
        "radical_note": "療 mang Bộ Nạch 疒(104: bệnh); 健 mang Bộ Nhân 亻(9: người khỏe mạnh)",
        "meaning_vi": "Điều trị y tế / Sức khỏe, khỏe mạnh",
        "collocation_tip": "歯の治療を受ける / 健康管理 (quản lý sức khỏe)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 5 Ngày 5 + Mimikara p.23",
    },
    {
        "vocab_key": "VC-N3-082",
        "word": "身長・独身",
        "reading": "しんちょう・どくしん",
        "han_viet": "THÂN TRƯỞNG / ĐỘC THÂN",
        "radical_note": "身 (Bộ Thân 158: thân thể con người); 独 (Bộ Khuyển 犭)",
        "meaning_vi": "Chiều cao cơ thể / Độc thân",
        "collocation_tip": "身長が伸びる / 身分 (vị thế) / 刺身 (さしみ)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 5 Ngày 6",
    },
    {
        "vocab_key": "VC-N3-083",
        "word": "呼吸・睡眠",
        "reading": "こきゅう・すいみん",
        "han_viet": "HÔ HẤP / THỤY MIÊN",
        "radical_note": "呼・吸 (Bộ Khẩu 口: miệng thở hút); 睡・眠 (Bộ Mục 目: mắt nhắm ngủ)",
        "meaning_vi": "Hô hấp, hít thở / Giấc ngủ",
        "collocation_tip": "深呼吸する / 睡眠不足 (thiếu ngủ) / 息切れ (hụt hơi) / 息子 (con trai)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 5 Ngày 6",
    },
    {
        "vocab_key": "VC-N3-084",
        "word": "地震・津波",
        "reading": "じしん・つなみ",
        "han_viet": "ĐỊA CHẤN / TÂN BA",
        "radical_note": "震 (Bộ Vũ 雨 173: mưa gió rung chuyển); 波 (Bộ Thủy 氵: sóng nước)",
        "meaning_vi": "Động đất / Sóng thần",
        "collocation_tip": "地震が起きる / 津波に注意する / 電波 (sóng điện từ)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 6 Ngày 1",
    },
    {
        "vocab_key": "VC-N3-085",
        "word": "募集・職業",
        "reading": "ぼしゅう・しょくぎょう",
        "han_viet": "MỘ TẬP / CHỨC NGHIỆP",
        "radical_note": "募 (Bộ Lực 力: kêu gọi lực lượng); 職 (Bộ Nhĩ 耳: lắng nghe đảm trách)",
        "meaning_vi": "Tuyển dụng, chiêu mộ / Nghề nghiệp",
        "collocation_tip": "アルバイトを募集する / 職場 (nơi làm việc) / 転職 (chuyển việc)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 6 Ngày 2",
    },
    {
        "vocab_key": "VC-N3-086",
        "word": "技術・美術",
        "reading": "ぎじゅつ・びじゅつ",
        "han_viet": "KỸ THUẬT / MỸ THUẬT",
        "radical_note": "技 (Bộ Thủ 扌: khéo tay); 術 (Bộ Hành 行: phương pháp) + 美 (Bộ Dương 羊)",
        "meaning_vi": "Kỹ thuật, công nghệ / Mỹ thuật, nghệ thuật",
        "collocation_tip": "技術者 (kỹ sư) / 美術館 (bảo tàng mỹ thuật) / 手術 (phẫu thuật)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 2 Ngày 3 & Tuần 6 Ngày 2",
    },
    {
        "vocab_key": "VC-N3-087",
        "word": "地球・優勝・決勝",
        "reading": "ちきゅう・ゆうしょう・けっしょう",
        "han_viet": "ĐỊA CẦU / ƯU THẮNG / QUYẾT THẮNG",
        "radical_note": "球 (Bộ Ngọc 王: viên bi tròn); 勝 (Bộ Lực 力: sức mạnh chiến thắng)",
        "meaning_vi": "Trái đất / Vô địch, giành giải nhất / Trận chung kết",
        "collocation_tip": "大会で優勝する / 野球 (bóng chày) / 反対 (phản đối) / 勝負 (thắng bại)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 6 Ngày 3",
    },
    {
        "vocab_key": "VC-N3-088",
        "word": "経験・経営",
        "reading": "けいけん・けいえい",
        "han_viet": "KINH NGHIỆM / KINH DOANH",
        "radical_note": "経 (Bộ Mịch 糸: sợi dọc trải qua) + 験 (Bộ Mã 馬: kiểm nghiệm)",
        "meaning_vi": "Kinh nghiệm bản thân / Quản trị kinh doanh",
        "collocation_tip": "豊かな経験 / 会社を経営する / 成長 (trưởng thành) / 完成 (hoàn thành)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 6 Ngày 4",
    },
    {
        "vocab_key": "VC-N3-089",
        "word": "貿易・輸出・輸入",
        "reading": "ぼうえき・ゆしゅつ・ゆにゅう",
        "han_viet": "MẬU DỊCH / THÂU XUẤT / THÂU NHẬP",
        "radical_note": "輸 (Bộ Xa 車 159: xe chuyên chở hàng hóa) + 貿 (Bộ Bối 貝: tiền hàng)",
        "meaning_vi": "Ngoại thương / Xuất khẩu / Nhập khẩu",
        "collocation_tip": "外国と貿易をする / 車を輸出する / 食料を輸入する",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 6 Ngày 4",
    },
    {
        "vocab_key": "VC-N3-090",
        "word": "相談・相手",
        "reading": "そうだん・あいて",
        "han_viet": "TƯƠNG ĐÀM / TƯƠNG THỦ",
        "radical_note": "相 (Bộ Mộc 木 + Mục 目: quan sát lẫn nhau) + 談 (Bộ Ngôn 言: nói chuyện)",
        "meaning_vi": "Bàn bạc, tham vấn / Đối phương, bạn đồng hành",
        "collocation_tip": "先生に相談する / 相手の気持ちを考える / 首相 (Thủ tướng)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 6 Ngày 4",
    },
    {
        "vocab_key": "VC-N3-091",
        "word": "原因・原料",
        "reading": "げんいん・げんりょう",
        "han_viet": "NGUYÊN NHÂN / NGUYÊN LIỆU",
        "radical_note": "原 (Bộ Hán 厂: vách núi + suối nguồn -> khởi nguồn); 因 (Bộ Vi 囗 + Đại 大)",
        "meaning_vi": "Nguyên nhân (thường của sự cố) / Nguyên liệu thô",
        "collocation_tip": "事故の原因を調べる / パンの原料は小麦だ",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 6 Ngày 5",
    },
    {
        "vocab_key": "VC-N3-092",
        "word": "会議・議論",
        "reading": "かいぎ・ぎろん",
        "han_viet": "HỘI NGHỊ / NGHỊ LUẬN",
        "radical_note": "議 và 論 đều mang Bộ Ngôn 言 (149: lời bàn luận)",
        "meaning_vi": "Cuộc họp, hội nghị / Cuộc thảo luận, tranh luận",
        "collocation_tip": "会議を開く / 問題について議論する / 議員 (nghị sĩ)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 6 Ngày 5",
    },
    {
        "vocab_key": "VC-N3-093",
        "word": "生活・活動",
        "reading": "せいかつ・かつどう",
        "han_viet": "SINH HOẠT / HOẠT ĐỘNG",
        "radical_note": "活 (Bộ Thủy 氵: nước chảy sinh sôi); 動 (Bộ Lực 力: chuyển động)",
        "meaning_vi": "Đời sống sinh hoạt / Hoạt động (tình nguyện, câu lạc bộ)",
        "collocation_tip": "規則正しい生活 / ボランティア活動 / 変化 (biến đổi)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 6 Ngày 5",
    },
    {
        "vocab_key": "VC-N3-094",
        "word": "政治・政府",
        "reading": "せいじ・せいふ",
        "han_viet": "CHÍNH TRỊ / CHÍNH PHỦ",
        "radical_note": "政 (Bộ Phộc 攵: chỉnh đốn cho ngay chính); 府 (Bộ Nghiễm 广: công đường)",
        "meaning_vi": "Chính trị / Chính phủ",
        "collocation_tip": "政治家 (chính trị gia) / 都道府県 (đơn vị hành chính Nhật)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 6 Ngày 6",
    },
    {
        "vocab_key": "VC-N3-095",
        "word": "改正・改札口",
        "reading": "かいせい・かいさつぐち",
        "han_viet": "CẢI CHÍNH / CẢI TRÁT KHẨU",
        "radical_note": "改 (Bộ Kỷ 己 + Phộc 攵: sửa đổi cải cách); 札 (Bộ Mộc 木: thẻ vé gỗ)",
        "meaning_vi": "Sửa đổi luật/quy định / Cửa soát vé nhà ga",
        "collocation_tip": "法律を改正する / 改札口を出る / 改めて (một lần nữa nghiêm chỉnh)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 6 Ngày 6",
    },
    {
        "vocab_key": "VC-N3-096",
        "word": "否定・肯定",
        "reading": "ひてい・こうてい",
        "han_viet": "PHỦ ĐỊNH / KHẲNG ĐỊNH",
        "radical_note": "否 (不 + 口: miệng nói không); 肯 (Bộ Nhục 月: gật đầu đồng ý)",
        "meaning_vi": "Phủ định, bác bỏ / Khẳng định, tán thành",
        "collocation_tip": "意見を否定する / 肯定的な評価 (đánh giá tích cực/khẳng định)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 6 Ngày 6",
    },
    {
        "vocab_key": "VC-N3-097",
        "word": "目的・国際的",
        "reading": "もくてき・こくさいてき",
        "han_viet": "MỤC ĐÍCH / QUỐC TẾ ĐÍCH",
        "radical_note": "目 (Bộ Mục 109: mắt) + 的 (Bộ Bạch 白: tâm bia); 際 (Bộ Phụ 阝: ranh giới)",
        "meaning_vi": "Mục đích, đích đến / Mang tính quốc tế",
        "collocation_tip": "旅行の目的 / 個人的 (mang tính cá nhân) / 基本的 (cơ bản)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 6 Ngày 6",
    },
    {
        "vocab_key": "VC-N3-098",
        "word": "実際・実験",
        "reading": "じっさい・じっけん",
        "han_viet": "THỰC TẾ / THỰC NGHIỆM",
        "radical_note": "実 (Bộ Miên 宀: mái nhà + quả đầy -> thực chất); 験 (Bộ Mã 馬)",
        "meaning_vi": "Thực tế (trên thực tế) / Thí nghiệm, thực nghiệm",
        "collocation_tip": "実際に使ってみる / 実は (thật ra thì...) / 実験を行う",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 6 Ngày 6",
    },
    {
        "vocab_key": "VC-N3-099",
        "word": "欠点・欠席",
        "reading": "けってん・けっせき",
        "han_viet": "KHIẾM ĐIỂM / KHIẾM TỊCH",
        "radical_note": "欠 (Bộ Khiếm 76: thiếu hụt); 席 (Bộ Nghiễm 广: chiếu ngồi)",
        "meaning_vi": "Khuyết điểm, điểm yếu / Vắng mặt (học, họp)",
        "collocation_tip": "誰にでも欠点がある / 授業を欠席する (trái với 出席 có mặt)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 6 Ngày 6",
    },
    {
        "vocab_key": "VC-N3-100",
        "word": "専門・専門家",
        "reading": "せんもん・せんもんか",
        "han_viet": "CHUYÊN MÔN / CHUYÊN MÔN GIA",
        "radical_note": "専 (Bộ Thốn 寸: chuyên tâm); 門 (Bộ Môn 169: cánh cửa ngành)",
        "meaning_vi": "Chuyên ngành, chuyên môn / Chuyên gia",
        "collocation_tip": "大学での専門 / 専門家に相談する",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 6 Ngày 6",
    },
    {
        "vocab_key": "VC-N3-101",
        "word": "警察・事故・故障",
        "reading": "けいさつ・じこ・こしょう",
        "han_viet": "CẢNH SÁT / SỰ CỐ / CỐ CHƯỚNG",
        "radical_note": "警 (敬 + 言: lời cảnh báo); 察 (宀: soi xét); 障 (阝: cản trở)",
        "meaning_vi": "Cảnh sát / Tai nạn, sự cố / Hỏng hóc máy móc",
        "collocation_tip": "警察署 (sở cảnh sát) / 交通事故 / パソコンが故障する",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 2 Ngày 6",
    },
    {
        "vocab_key": "VC-N3-102",
        "word": "伝言・伝える",
        "reading": "でんごん・つたえる",
        "han_viet": "TRUYỀN NGÔN / TRUYỀN",
        "radical_note": "伝 (Bộ Nhân 亻: người truyền đạt) + 言 (Bộ Ngôn 149: lời nói)",
        "meaning_vi": "Lời nhắn / Truyền đạt lại, lan truyền (tự: 伝わる)",
        "collocation_tip": "伝言を残す / 気持ちを伝える / 手伝う (giúp đỡ)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 2 Ngày 6 + Mimikara p.71",
    },
    {
        "vocab_key": "VC-N3-103",
        "word": "理解・解説",
        "reading": "りかい・かいせつ",
        "han_viet": "LÝ GIẢI / GIẢI THUYẾT",
        "radical_note": "理 (Bộ Ngọc 王: mạch ngọc -> hợp lý); 説 (Bộ Ngôn 言: giảng giải)",
        "meaning_vi": "Sự thông hiểu / Lời giải thích cặn kẽ",
        "collocation_tip": "内容を深く理解する / わかりやすい解説 / 解答 (đáp án)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 2 Ngày 2",
    },
    {
        "vocab_key": "VC-N3-104",
        "word": "協力・願う",
        "reading": "きょうりょく・ねがう",
        "han_viet": "HIỆP LỰC / NGUYỆN",
        "radical_note": "協 (Bộ Thập 十 + Lực 力 x3: ba sức chung lại); 願 (Bộ Hiệt 頁: cúi đầu mong)",
        "meaning_vi": "Hợp tác, chung sức / Mong muốn, cầu nguyện, nhờ cậy",
        "collocation_tip": "ご協力をお願いいたします / 合格を願う",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 2 Ngày 2",
    },
    {
        "vocab_key": "VC-N3-105",
        "word": "観光・観客",
        "reading": "かんこう・かんきゃく",
        "han_viet": "QUAN QUANG / QUAN KHÁCH",
        "radical_note": "観 (Bộ Kiến 見 147: nhìn ngắm kỹ); 客 (Bộ Miên 宀: khách tới mái nhà)",
        "meaning_vi": "Tham quan du lịch / Khán giả, khách tham quan",
        "collocation_tip": "京都を観光する / お客様 (quý khách) / 様子 (dáng vẻ, tình hình)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 2 Ngày 2-3",
    },
    {
        "vocab_key": "VC-N3-106",
        "word": "種類・共通",
        "reading": "しゅるい・きょうつう",
        "han_viet": "CHỦNG LOẠI / CỘNG THÔNG",
        "radical_note": "種 (Bộ Hòa 禾: giống lúa); 類 (Bộ Hiệt 頁); 共 (Bộ Bát 八)",
        "meaning_vi": "Chủng loại, loại hình / Điểm chung, dùng chung",
        "collocation_tip": "様々な種類 / 共通の趣味 (sở thích chung) / 共通点",
        "jlpt_level": "N3",
        "source_ref": "Kho từ vựng đề thi JLPT N3",
    },
    {
        "vocab_key": "VC-N3-107",
        "word": "影響・効果",
        "reading": "えいきょう・こうか",
        "han_viet": "ẢNH HƯỞNG / HIỆU QUẢ",
        "radical_note": "響 (Bộ Âm 音: âm thanh vang dội); 効 (Bộ Lực 力: sức tạo kết quả)",
        "meaning_vi": "Sự ảnh hưởng / Hiệu quả, tác dụng",
        "collocation_tip": "影響を与える・受ける / 効果がある・効く (có tác dụng)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.69 + Đề thi N3",
    },
    {
        "vocab_key": "VC-N3-108",
        "word": "責任・義務",
        "reading": "せきにん・ぎむ",
        "han_viet": "TRÁCH NHIỆM / NGHĨA VỤ",
        "radical_note": "責 (Bộ Bối 貝); 任 (Bộ Nhân 亻: gánh vác); 務 (Bộ Lực 力: việc phải làm)",
        "meaning_vi": "Trách nhiệm / Nghĩa vụ, bổn phận",
        "collocation_tip": "責任を持つ・感じる / 義務教育 (giáo dục bắt buộc)",
        "jlpt_level": "N3",
        "source_ref": "Kho từ vựng Đọc hiểu N3",
    },
    {
        "vocab_key": "VC-N3-109",
        "word": "態度・雰囲気",
        "reading": "たいど・ふんいき",
        "han_viet": "THÁI ĐỘ / PHÂN VI KHÍ",
        "radical_note": "態 (能 + 心: biểu hiện trong tâm); 雰 (Bộ Vũ 雨: bầu khí quanh ta)",
        "meaning_vi": "Thái độ ứng xử / Bầu không khí (lưu ý đọc ふんいき, không đọc ふいんき!)",
        "collocation_tip": "態度が悪い・丁寧だ / 明るい雰囲気の職場",
        "jlpt_level": "N3",
        "source_ref": "Kho từ vựng JLPT N3 + Đề đọc hiểu",
    },
    {
        "vocab_key": "VC-N3-110",
        "word": "環境・伝統",
        "reading": "かんきょう・でんとう",
        "han_viet": "HOÀN CẢNH / TRUYỀN THỐNG",
        "radical_note": "環 (Bộ Ngọc 王: vòng tròn bao quanh); 統 (Bộ Mịch 糸: sợi nối xuyên suốt)",
        "meaning_vi": "Môi trường (tự nhiên, làm việc) / Truyền thống lâu đời",
        "collocation_tip": "環境問題 / 伝統文化を守る / 伝統的な料理",
        "jlpt_level": "N3",
        "source_ref": "Đề N3 (緑のカーテン / 月のウサギ) + Somatome",
    },
    {
        "vocab_key": "VC-N3-111",
        "word": "防ぐ・守る",
        "reading": "ふせぐ・まもる",
        "han_viet": "PHÒNG / THỦ",
        "radical_note": "防 (Bộ Phụ 阝: đắp đê ngăn nước); 守 (Bộ Miên 宀 + Thốn 寸: canh giữ)",
        "meaning_vi": "Ngăn chặn, phòng chống / Bảo vệ, tuân thủ (quy tắc, lời hứa)",
        "collocation_tip": "日差しが入るのを防ぐ / ルールを守る / 消防 (cứu hỏa)",
        "jlpt_level": "N3",
        "source_ref": "Somatome Tuần 2 Ngày 6 + Đề N3 Q#52 (緑のカーテン)",
    },
    {
        "vocab_key": "VC-N3-112",
        "word": "確認・承認",
        "reading": "かくにん・しょうにん",
        "han_viet": "XÁC NHẬN / THỪA NHẬN",
        "radical_note": "認 (Bộ Ngôn 言 + 忍: nhận biết bằng lời nói xác thực)",
        "meaning_vi": "Kiểm tra xác nhận lại / Phê duyệt, công nhận",
        "collocation_tip": "内容を確認する / 承認を得る / 確認が取れる",
        "jlpt_level": "N3",
        "source_ref": "Đề N3 + Từ vựng công sở",
    },
    {
        "vocab_key": "VC-N3-113",
        "word": "常識・知識",
        "reading": "じょうしき・ちしき",
        "han_viet": "THƯỜNG THỨC / TRI THỨC",
        "radical_note": "識 (Bộ Ngôn 言 149: lời phân biệt nhận thức rõ ràng)",
        "meaning_vi": "Kiến thức phổ thông, lẽ thường / Tri thức chuyên sâu",
        "collocation_tip": "社会の常識 / 専門的な知識を身につける",
        "jlpt_level": "N3",
        "source_ref": "Kho từ vựng Đọc hiểu N3",
    },
    {
        "vocab_key": "VC-N3-114",
        "word": "対象・傾向",
        "reading": "たいしょう・けいこう",
        "han_viet": "ĐỐI TƯỢNG / KHUYNH HƯỚNG",
        "radical_note": "傾 (Bộ Nhân 亻: nghiêng mình về một phía); 向 (hướng)",
        "meaning_vi": "Đối tượng nhắm tới / Xu hướng, khuynh hướng",
        "collocation_tip": "学生を対象としたアンケート / ～という傾向がある",
        "jlpt_level": "N3",
        "source_ref": "Đọc hiểu Kosei + Đề N3",
    },
    {
        "vocab_key": "VC-N3-115",
        "word": "整理・整える",
        "reading": "せいり・ととのえる",
        "han_viet": "CHỈNH LÝ / CHỈNH",
        "radical_note": "整 (Bộ Phộc 攵 + 正: chỉnh sửa lại cho ngay ngắn trật tự)",
        "meaning_vi": "Sắp xếp ngăn nắp, phân loại / Điều chỉnh, chuẩn bị sẵn sàng",
        "collocation_tip": "書類を整理する / 生活リズムを整える",
        "jlpt_level": "N3",
        "source_ref": "Đề N3 + Mimikara N3",
    },
    {
        "vocab_key": "VC-N3-116",
        "word": "判断・決定",
        "reading": "はんだん・けってい",
        "han_viet": "PHÁN ĐOÁN / QUYẾT ĐỊNH",
        "radical_note": "判 (Bộ Đao 刂: phân tách); 断 (Bộ Cân 斤: cắt dứt khoát)",
        "meaning_vi": "Phán đoán, đánh giá / Quyết định chính thức",
        "collocation_tip": "状況を見て判断する / 日程を決定する / 決まる・決める",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 6 Ngày 3 + Đọc hiểu N3",
    },
    {
        "vocab_key": "VC-N3-117",
        "word": "比較・比例",
        "reading": "ひかく・ひれい",
        "han_viet": "TỶ GIÁC / TỶ LỆ",
        "radical_note": "比 (Bộ Tỷ 81: hai người đứng cạnh so sánh nhau); 較 (Bộ Xa 車)",
        "meaning_vi": "So sánh đối chiếu / Tỷ lệ thuận",
        "collocation_tip": "昨年と比較する / 比較的 (ひかくてき: tương đối) / 比べる",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 6 Ngày 5 + GP-N3-106",
    },
    {
        "vocab_key": "VC-N3-118",
        "word": "将来・未来・過去",
        "reading": "しょうらい・みらい・かこ",
        "han_viet": "TƯƠNG LAI / VỊ LAI / QUÁ KHỨ",
        "radical_note": "過 (Bộ Sước 辶: đã bước đi qua); 去 (Bộ Tư 厶: rời đi)",
        "meaning_vi": "Tương lai gần (đời người/nghề nghiệp) / Tương lai xa (nhân loại) / Quá khứ",
        "collocation_tip": "将来の夢 (ước mơ tương lai) / 未来の世界 / 過去の記憶",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 + Đọc hiểu Kosei",
    },
    {
        "vocab_key": "VC-N3-119",
        "word": "結果・理由・原因",
        "reading": "けっか・りゆう・げんいん",
        "han_viet": "KẾT QUẢ / LÝ DO / NGUYÊN NHÂN",
        "radical_note": "果 (Bộ Mộc 木 + Điền 田: trái chín trên cây); 結 (Bộ Mịch 糸)",
        "meaning_vi": "Kết quả / Lý do giải thích / Nguyên nhân gốc rễ",
        "collocation_tip": "調査の結果 / 遅刻の理由 / 果物 (くだもの - đọc đặc biệt!)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 6 Ngày 3 & 5",
    },
    {
        "vocab_key": "VC-N3-120",
        "word": "表現・表示",
        "reading": "ひょうげん・ひょうじ",
        "han_viet": "BIỂU HIỆN / BIỂU THỊ",
        "radical_note": "表 (Bộ Y 衣); 示 (Bộ Thị 示 113: bày tỏ cho thấy rõ)",
        "meaning_vi": "Diễn đạt, biểu hiện (ngôn ngữ, cảm xúc) / Hiển thị trên màn hình/biển",
        "collocation_tip": "言葉で表現する / 画面に表示される",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 + Đề N3",
    },
    {
        "vocab_key": "VC-N3-121",
        "word": "集中・緊張",
        "reading": "しゅうちゅう・きんちょう",
        "han_viet": "TẬP TRUNG / KHẨN TRƯƠNG",
        "radical_note": "集 (Bộ Truy 隹 + Mộc 木: chim đậu chung cây); 緊・張 (糸 / 弓: dây căng)",
        "meaning_vi": "Tập trung tinh thần / Căng thẳng, hồi hộp",
        "collocation_tip": "勉強に集中する / 面接の前で緊張する",
        "jlpt_level": "N3",
        "source_ref": "Kho từ vựng Đề N3",
    },
    {
        "vocab_key": "VC-N3-122",
        "word": "安心・心配・不安",
        "reading": "あんしん・しんぱい・ふあん",
        "han_viet": "AN TÂM / TÂM PHỐI / BẤT AN",
        "radical_note": "安 (Bộ Miên 宀 + Nữ 女: bình yên dưới mái nhà); 心 (Bộ Tâm 61)",
        "meaning_vi": "Yên tâm / Lo lắng (cho ai/việc gì) / Bất an, thấp thỏm",
        "collocation_tip": "試験に受かって安心した / 親に心配をかける / 将来が不安だ",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 + Somatome Tuần 4 Ngày 5",
    },
    {
        "vocab_key": "VC-N3-123",
        "word": "応援・援助",
        "reading": "おうえん・えんじょ",
        "han_viet": "ỨNG VIỆN / VIỆN TRỢ",
        "radical_note": "援 (Bộ Thủ 扌 64: chìa tay kéo giúp); 助 (Bộ Lực 力: trợ sức)",
        "meaning_vi": "Cổ vũ, ủng hộ / Viện trợ, giúp đỡ vật chất/tài chính",
        "collocation_tip": "選手を応援する / 発展途上国を援助する",
        "jlpt_level": "N3",
        "source_ref": "Đề N3 (日本人スポーツ選手) + Somatome",
    },
    {
        "vocab_key": "VC-N3-124",
        "word": "努力・工夫",
        "reading": "どりょく・くふう",
        "han_viet": "NỖ LỰC / CÔNG PHU",
        "radical_note": "努・力 (Bộ Lực 力 19: gắng sức); 工 (Bộ Công 48: khéo léo chế tác)",
        "meaning_vi": "Nỗ lực, cố gắng / Sáng kiến, khéo léo nghĩ cách cải tiến",
        "collocation_tip": "合格に向けて努力する / 使いやすく工夫する",
        "jlpt_level": "N3",
        "source_ref": "Kho từ vựng Đọc hiểu N3",
    },
    {
        "vocab_key": "VC-N3-125",
        "word": "特徴・特長",
        "reading": "とくちょう・とくちょう",
        "han_viet": "ĐẶC TRƯNG / ĐẶC TRƯỜNG",
        "radical_note": "特 (Bộ Ngưu 牛: trâu nổi bật); 徴 (Bộ Sách 彳: dấu hiệu riêng)",
        "meaning_vi": "Đặc trưng, nét riêng (trung tính) / Ưu điểm nổi trội (tích cực)",
        "collocation_tip": "日本の文化の特徴 / この製品の特長 (điểm mạnh của sản phẩm)",
        "jlpt_level": "N3",
        "source_ref": "Phân biệt đồng âm kinh điển N3",
    },
    {
        "vocab_key": "VC-N3-126",
        "word": "許可・禁止",
        "reading": "きょか・きんし",
        "han_viet": "HỨA KHẢ / CẤM CHỈ",
        "radical_note": "許 (Bộ Ngôn 言: lời cho phép); 禁 (Bộ Lâm 林 + Thị 示: cấm đoán)",
        "meaning_vi": "Cho phép, cấp phép / Cấm đoán",
        "collocation_tip": "許可を得る・求める / 禁煙 (cấm hút thuốc) / 撮影禁止",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 + Somatome",
    },
    {
        "vocab_key": "VC-N3-127",
        "word": "増加・減少",
        "reading": "ぞうか・げんしょう",
        "han_viet": "TĂNG GIA / GIẢM THIỂU",
        "radical_note": "増 (Bộ Thổ 土: đắp thêm đất); 減 (Bộ Thủy 氵: nước vơi bớt đi)",
        "meaning_vi": "Tăng lên / Giảm xuống (cặp trái nghĩa trọng tâm N3-N2)",
        "collocation_tip": "人口の増加に伴って / ゴミの量を減少させる",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 + GP-N3-099",
    },
    {
        "vocab_key": "VC-N3-128",
        "word": "出発・到着",
        "reading": "しゅっぱつ・とうちゃく",
        "han_viet": "XUẤT PHÁT / ĐÁO TRƯỚC",
        "radical_note": "発 (Bộ Bát 癶: bước ra); 到 (Bộ Đao 刂 + Chí 至: đi tới đích)",
        "meaning_vi": "Khởi hành, xuất phát / Tới nơi, cập bến",
        "collocation_tip": "定刻に出発する / 空港に到着する (trợ từ に)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 + Đề N3",
    },
    {
        "vocab_key": "VC-N3-129",
        "word": "習慣・癖",
        "reading": "しゅうかん・くせ",
        "han_viet": "TẬP QUÁN / PHÍCH",
        "radical_note": "習 (Bộ Vũ 羽); 癖 (Bộ Nạch 疒: tật quen khó bỏ của cá nhân)",
        "meaning_vi": "Tập quán, thói quen (tốt hoặc văn hóa) / Tật riêng khó sửa",
        "collocation_tip": "早起きの習慣 / 貧乏ゆすりの癖 (tật rung chân)",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.47 + Đề N3",
    },
    {
        "vocab_key": "VC-N3-130",
        "word": "記録・記憶",
        "reading": "きろく・きおく",
        "han_viet": "KÝ LỤC / KÝ ỨC",
        "radical_note": "記 (Bộ Ngôn 言); 憶 (Bộ Tâm 忄: ghi giữ trong lòng/não)",
        "meaning_vi": "Ghi chép ra văn bản, kỷ lục / Ký ức, trí nhớ trong đầu",
        "collocation_tip": "ノートに記録する / 記憶に残る・記憶が薄れる",
        "jlpt_level": "N3",
        "source_ref": "Somatome Tuần 3 Ngày 6 + Đồng âm N3",
    },
    {
        "vocab_key": "VC-N3-131",
        "word": "発見・発明",
        "reading": "はっけん・はつめい",
        "han_viet": "PHÁT KIẾN / PHÁT MINH",
        "radical_note": "見 (nhìn thấy cái vốn có) vs 明 (làm sáng tỏ cái mới chưa từng có)",
        "meaning_vi": "Phát hiện (cái có sẵn) / Phát minh (sáng chế cái mới)",
        "collocation_tip": "新しい星を発見する / 電球を発明する",
        "jlpt_level": "N3",
        "source_ref": "Từ vựng phân biệt cốt lõi N3",
    },
    {
        "vocab_key": "VC-N3-132",
        "word": "説明・納得",
        "reading": "せつめい・なっとく",
        "han_viet": "THUYẾT MINH / NẠP ĐẮC",
        "radical_note": "説 (Bộ Ngôn 言: giảng giải); 納 (Bộ Mịch 糸: thu nhận vào lòng)",
        "meaning_vi": "Giải thích / Hiểu thấu và đồng tình hoàn toàn",
        "collocation_tip": "理由を説明する / 説明を聞いて納得する",
        "jlpt_level": "N3",
        "source_ref": "Đọc hiểu Kosei + Đề N3",
    },
    {
        "vocab_key": "VC-N3-133",
        "word": "注意・警戒",
        "reading": "ちゅうい・けいかい",
        "han_viet": "CHÚ Ý / CẢNH GIỚI",
        "radical_note": "注 (Bộ Thủy 氵: rót dồn vào một điểm); 警 (Bộ Ngôn 言)",
        "meaning_vi": "Lưu ý, chú ý / Đề phòng cảnh giác cao độ",
        "collocation_tip": "説明書に注意書きがある / 台風に警戒する",
        "jlpt_level": "N3",
        "source_ref": "Đề N3 + Mimikara N3",
    },
    {
        "vocab_key": "VC-N3-134",
        "word": "利用・活用",
        "reading": "りよう・かつよう",
        "han_viet": "LỢI DỤNG / HOẠT DỤNG",
        "radical_note": "利 (Bộ Hòa 禾 + Đao 刂: gặt lúa thu lợi); 活 (Bộ Thủy 氵: sinh động)",
        "meaning_vi": "Sử dụng (dịch vụ, công cụ) / Vận dụng linh hoạt hiệu quả",
        "collocation_tip": "図書館を利用する / 知識を仕事に活用する",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 4 Ngày 2 & Tuần 6 Ngày 5",
    },
    {
        "vocab_key": "VC-N3-135",
        "word": "都合・予定",
        "reading": "つごう・よてい",
        "han_viet": "ĐÔ HỢP / DỰ ĐỊNH",
        "radical_note": "都 (Bộ Ấp 阝); 合 (Bộ Nhân 人 + 口); 定 (Bộ Miên 宀)",
        "meaning_vi": "Sự thuận tiện (thời gian/hoàn cảnh) / Lịch trình, dự định",
        "collocation_tip": "都合がいい・悪い / 仕事の都合で (vì lý do công việc) / 予定を立てる",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 + Đề giao tiếp N3",
    },
    {
        "vocab_key": "VC-N3-136",
        "word": "満足・不満",
        "reading": "まんぞく・ふまん",
        "han_viet": "MÃN TÚC / BẤT MÃN",
        "radical_note": "満 (Bộ Thủy 氵: nước tràn đầy); 足 (Bộ Túc: đủ đầy)",
        "meaning_vi": "Hài lòng, thỏa mãn / Bất mãn, không hài lòng",
        "collocation_tip": "結果に満足する / サービスに対する不満 (trợ từ に対する)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 + Mimikara N3",
    },
    {
        "vocab_key": "VC-N3-137",
        "word": "誤解・理解",
        "reading": "ごかい・りかい",
        "han_viet": "NGỘ GIẢI / LÝ GIẢI",
        "radical_note": "誤 (Bộ Ngôn 言: lời nói sai lầm); 解 (Bộ Giác 角 + 刀: phân tích gỡ rối)",
        "meaning_vi": "Hiểu nhầm / Hiểu đúng thấu đáo",
        "collocation_tip": "誤解を招く・誤解を解く / お互いの立場を理解する",
        "jlpt_level": "N3",
        "source_ref": "Mimikara N3 p.75 + Somatome Tuần 2 Ngày 2",
    },
    {
        "vocab_key": "VC-N3-138",
        "word": "成長・成功",
        "reading": "せいちょう・せいこう",
        "han_viet": "THÀNH TRƯỞNG / THÀNH CÔNG",
        "radical_note": "成 (Bộ Qua 戈: hoàn thành); 長 (Bộ Trường 168: lớn dài); 功 (Bộ Lực 力)",
        "meaning_vi": "Trưởng thành, phát triển / Thành công",
        "collocation_tip": "子どもが成長する / 実験に成功する (trợ từ に)",
        "jlpt_level": "N3",
        "source_ref": "Somatome N3 Tuần 6 Ngày 4",
    },
]
