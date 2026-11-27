"""Offline curriculum of 12 Micro-Units and 12 N4->N3 Bridge Capsules."""

import json
import sqlite3
from typing import Any, Dict, List


MICRO_UNITS_SPEC: List[Dict[str, Any]] = [
    {
        "code": "MU-01",
        "order_index": 1,
        "title": "Kanji Âm On/Kun, Biến âm (Tenten) & Trường âm",
        "section": "vocab",
        "target_skill": "問題1 Cách đọc Kanji (Âm On/Kun, âm đục じ/ぞ/ぶ, xúc âm っ, trường âm う)",
        "estimated_minutes": 40,
        "bridge": {
            "grammar_focus": "Quy tắc đọc On/Kun N4->N3, âm đục Rendaku (じ/し, ぶ/む, ぞ/そ), xúc âm (っ) & trường âm (きゅう/くう)",
            "explanation_vi": (
                "Người học xuất phát từ N5 hay mất điểm ở 問題1 vì chỉ nhớ 1 âm đọc rời rạc mà không nắm 4 quy luật biến âm N4->N3:\n"
                "1. Đứng một mình thường đọc Kun (型 かた, 差 さ, 汗 あせ), ghép 2 chữ Hán đọc On (模型 もけい, 差異 さい).\n"
                "2. Biến âm đục (Tenten) thay đổi theo từ ghép: 無 đọc ぶ trong 無事(ぶじ)・無礼(ぶれい) nhưng đọc む trong 無理(むり)・無視(むし); 足 đọc ぞく trong 満足(まんぞく) nhưng そく trong 不足(ふそく).\n"
                "3. Xúc âm (っ): âm kết thúc つ/く trước hàng か/さ/た/ぱ hay biến thành っ (物 ぶつ + 価 か -> 物価 ぶっか).\n"
                "4. Trường âm: phân biệt きゅう (急行 きゅうこう) vs くう (空港 くうこう), てい (否定 ひてい) vs て."
            ),
            "examples": [
                {"jp": "型（かた） vs 模型（もけい） vs 最新型（さいしんがた）", "vi": "Độc lập đọc Kun かた; từ ghép Hán-Nhật đọc On けい; hậu tố biến âm がた."},
                {"jp": "無事（ぶじ） vs 無視（むし）", "vi": "Cùng chữ 無 nhưng ghép 事 đọc ぶじ, ghép 視 đọc むし (không tenten ở し)."},
                {"jp": "満足（まんぞく） vs 不足（ふそく）", "vi": "Bẫy kinh điển: 満足 có tenten (ぞく), 不足 không tenten (そく)."},
                {"jp": "物価（ぶっか） / 急行（きゅうこう）", "vi": "物 (ぶつ) + 価 (か) -> xúc âm ぶっか; 急 luôn có trường âm きゅう."},
            ],
            "quick_check": [
                {
                    "prompt": "Trong cặp từ ghép của chữ 無, từ nào đọc là 「ぶじ」?",
                    "options": ["無地", "無事", "無視", "無理"],
                    "correct_index": 1,
                    "note": "無事 (ぶじ: bình an vô sự); 無地 (むじ), 無視 (むし), 無理 (むり).",
                },
                {
                    "prompt": "Cách đọc đúng của 「物価」 khi áp dụng quy tắc xúc âm N4->N3 là gì?",
                    "options": ["ぶつか", "ものか", "ぶっか", "ものが"],
                    "correct_index": 2,
                    "note": "物 (ぶつ) đứng trước hàng か biến âm thành xúc âm っ -> ぶっか.",
                },
            ],
        },
    },
    {
        "code": "MU-02",
        "order_index": 2,
        "title": "Chữ Hán Viết (Phân biệt Bộ thủ & Đồng âm N4->N3)",
        "section": "vocab",
        "target_skill": "問題2 Viết Kanji (Soi bộ thủ gần giống 鳥/島, 礻/衤, 句/勺 và từ đồng âm 備える/供える)",
        "estimated_minutes": 35,
        "bridge": {
            "grammar_focus": "Bộ thủ quyết định nghĩa (礻 vs 彳, 亻 vs không bộ), nét tinh vi (句/勺, 失/夫/矢/央) & đồng âm khác chữ",
            "explanation_vi": (
                "Để không sập bẫy tự dạng ở 問題2, luôn tách chữ Hán thành 2 phần [Bộ chỉ nghĩa] + [Bộ chỉ âm] trước khi nhìn tổng thể:\n"
                "1. Soi nét chi tiết: 鳥 (chim, có 4 chấm) khác 島 (đảo, có 山); 句 (chứa 口) khác 勺 (chỉ 1 dấu chấm); 失 khác 夫・矢・央.\n"
                "2. Phân biệt bộ thủ: 福 (bộ Thị 礻 = phúc lành) vs 復 (bộ Xích 彳 = khôi phục); 儀 (có bộ Nhân 亻 trong 礼儀) vs 義 (正義); 態 (có Tâm 心) vs 能 (能力).\n"
                "3. Tiền tố phủ định: 不 (不便・不安) vs 非 (非常).\n"
                "4. Đồng âm khác chữ theo ngữ cảnh: 川に沿って (沿う = dọc theo không gian) vs 期待に添う (添う = đáp ứng); 地震に備える (phòng bị) vs 花を供える (dâng cúng)."
            ),
            "examples": [
                {"jp": "小鳥（ことり） vs 小島（こじま）", "vi": "鳥 có 4 chấm lửa ở chân (con chim), 島 có bộ 山 (núi giữa biển = hòn đảo)."},
                {"jp": "沿う（そって） vs 添う（そって）", "vi": "Đều đọc そって: 沿う (bộ Thủy 氵) đi với sông/đường; 添う đi với kỳ vọng/kề bên."},
                {"jp": "備える（そなえる） vs 供える（そなえる）", "vi": "Đều đọc そなえる: 備える (bộ Nhân 亻) = phòng bị thiên tai; 供える = dâng lễ."},
                {"jp": "文句（もんく） vs 文勺 / 夫婦（ふうふ） vs 夫妻（ふさい）", "vi": "句 có 口 bên trong, 勺 chỉ có chấm; 夫婦 đọc ふうふ còn 夫妻 đọc ふさい."},
            ],
            "quick_check": [
                {
                    "prompt": "Trong câu 「川に【そって】歩く」, chữ Kanji nào dùng đúng cho sông/đường?",
                    "options": ["添って", "沿って", "沢って", "沼って"],
                    "correct_index": 1,
                    "note": "沿う (bộ Thủy 氵) dùng cho không gian dọc theo sông, đường, bờ biển.",
                },
                {
                    "prompt": "Chữ Kanji nào viết đúng cho từ 「もんく」(lời phàn nàn)?",
                    "options": ["文勺", "交句", "文句", "文化"],
                    "correct_index": 2,
                    "note": "句 (Cú) có bộ 口 bên trong; 勺 (Thược) chỉ có một dấu chấm.",
                },
            ],
        },
    },
    {
        "code": "MU-03",
        "order_index": 3,
        "title": "Tự động từ vs Tha động từ & Trợ từ đi kèm",
        "section": "vocab",
        "target_skill": "Phân biệt cặp Tự/Tha động từ (が vs を), kết hợp trợ từ cố định (に遭う, に感謝する, によい)",
        "estimated_minutes": 26,
        "bridge": {
            "grammar_focus": "Hệ thống cặp tự/tha động từ N4 (開く/開ける, 混ざる/混ぜる, 並ぶ/並べる, 焼く/焼ける) & trợ từ に/が/を",
            "explanation_vi": (
                "Khoảng 35% câu điền từ 問題3 có thể chốt trong 5 giây chỉ bằng cách nhìn trợ từ ngay trước chỗ trống:\n"
                "1. [Chủ thể + が] -> chọn Tự động từ (không cần tác động trực tiếp bằng を): 男女が混ざる, 風が吹く, 空気が乾燥している.\n"
                "2. [Tân ngữ + を] -> chọn Tha động từ: 魚を焼く, たまごと牛乳を混ぜる, お湯を沸かす, 紙を破る.\n"
                "3. Kết hợp trợ từ cố định với động từ/tính từ: 事故にあう (遭う = gặp chuyện xấu — còn 怪我 thì đi với する), 両親に感謝する, 健康によい (tốt cho sức khỏe), 明日以降に."
            ),
            "examples": [
                {"jp": "男女が混ざる（まざる） ↔ 牛乳と卵を混ぜる（まぜる）", "vi": "Trợ từ が đi với tự động từ 混ざる; trợ từ を đi với tha động từ 混ぜる."},
                {"jp": "事故にあう（遭う） ↔ 怪我をする", "vi": "Tai nạn/thiên tai dùng にあう; bị thương dùng 怪我をする; mắc bệnh dùng 病気になる."},
                {"jp": "現れる（あらわれる） vs 表れる（あらわれる）", "vi": "現れる = người/vật xuất hiện hữu hình; 表れる = cảm xúc/kết quả bộc lộ."},
            ],
            "quick_check": [
                {
                    "prompt": "Chọn động từ khớp với trợ từ trong câu: 「男女が（　）サッカーをした。」",
                    "options": ["まぜて", "まざって", "つけて", "わかして"],
                    "correct_index": 1,
                    "note": "Chủ ngữ đi với trợ từ が (男女が) nên phải dùng tự động từ 混ざる -> まざって.",
                },
                {
                    "prompt": "Danh từ nào kết hợp đúng với 「～にあう」(gặp phải điều xui xẻo)?",
                    "options": ["怪我", "病気", "事故", "健康"],
                    "correct_index": 2,
                    "note": "Cụm cố định là 事故にあう; 怪我をする và 病気になる không dùng với にあう.",
                },
            ],
        },
    },
    {
        "code": "MU-04",
        "order_index": 4,
        "title": "Từ ghép Hán-Nhật 2 chữ, Động từ ghép & Katakana",
        "section": "vocab",
        "target_skill": "Phân biệt từ Hán-Nhật cùng gốc chữ (中止/停止/静止/禁止), danh từ ghép Vます (見出し/手入れ) & Katakana",
        "estimated_minutes": 34,
        "bridge": {
            "grammar_focus": "Cấu tạo từ ghép Hán-Nhật 2 chữ, danh từ ghép từ động từ (見〜, 手〜) & Katakana N4->N3",
            "explanation_vi": (
                "Trong đề N3, các từ ghép Hán-Nhật và Katakana luôn ra theo nhóm đối chiếu nghĩa hẹp:\n"
                "1. Nhóm đuôi 止 (Chỉ = dừng): 中止 (hủy hẳn sự kiện/đại hội), 停止 (tạm dừng xe/máy móc), 禁止 (nghiêm cấm), 静止 (đứng yên bất động).\n"
                "2. Danh từ ghép từ động từ 見/手: 見出し (tiêu đề báo), 見落とし (bỏ sót); 手入れ (chăm sóc/bảo dưỡng), 手抜き (làm ẩu), 手引き (hướng dẫn).\n"
                "3. Katakana hay thi kèm cụm động từ: メッセージを残す, アイデアを出し合う, コミュニケーションをとる, ホームステイする, コメントする.\n"
                "4. Phó từ hô ứng N4->N3: どんなに～ても (dù thế nào), いつのまにか (lúc nào không hay), さっそく (làm ngay háo hức)."
            ),
            "examples": [
                {"jp": "大会の中止 vs 電車の停止 vs 撮影の禁止", "vi": "Hủy sự kiện dùng 中止; tạm dừng máy/tàu dùng 停止; cấm làm dùng 禁止."},
                {"jp": "新聞の見出し vs 字の見落とし", "vi": "見出し = tít báo/đề mục; 見落とし = nhìn sót thông tin."},
                {"jp": "さっそく（早速） vs いきなり", "vi": "さっそく = bắt tay làm ngay khi nhận quà/tin (tích cực); いきなり = đột ngột thiếu chuẩn bị."},
            ],
            "quick_check": [
                {
                    "prompt": "Khi muốn nói 'Hủy bỏ giải đấu vì mưa lớn', dùng từ nào chuẩn nhất?",
                    "options": ["静止", "停止", "中止", "見返し"],
                    "correct_index": 2,
                    "note": "中止 dùng cho việc hủy bỏ hẳn sự kiện, cuộc họp, giải đấu.",
                },
                {
                    "prompt": "Động từ nào thường đi kèm cố định với 「コミュニケーション」?",
                    "options": ["とる", "あう", "つく", "のる"],
                    "correct_index": 0,
                    "note": "Cụm cố định N3: コミュニケーションをとる (giao tiếp, trao đổi).",
                },
            ],
        },
    },
    {
        "code": "MU-05",
        "order_index": 5,
        "title": "Từ đồng nghĩa (Paraphrase N4 <-> N3 & Nghĩa mở rộng)",
        "section": "vocab",
        "target_skill": "問題4 Quy đổi từ thuần Nhật <-> Hán-Nhật, nghĩa mở rộng (甘い＝やさしい) & lọc bẫy từ trái nghĩa",
        "estimated_minutes": 32,
        "bridge": {
            "grammar_focus": "Chuyển đổi Thuần Nhật <-> Hán-Nhật <-> Katakana và nhận diện bẫy từ trái nghĩa ở 問題4",
            "explanation_vi": (
                "Đề 問題4 luôn cài sẵn 1–2 phương án TRÁI NGHĨA (như あまい vs きびしい, からから vs ぬれている, ネガティブ vs 肯定的, つなぐ vs 切断する) để bẫy thí sinh đọc lướt:\n"
                "1. Quy đổi Thuần Nhật <-> Hán-Nhật: わけ＝理由, 済む＝終わる, 残らず＝全部, 変更する＝ずらす, つなぐ＝接続する, 打ち消す＝否定する, 落ち着いている＝冷静だ.\n"
                "2. Nghĩa mở rộng của từ N5/N4: 甘い (ngọt -> dễ dãi/chiều chuộng = やさしい), 結構 (tốt -> khá là = ある程度は), 惜しい (tiếc -> 残念だ).\n"
                "3. Động từ ghép Vます+出す: 言い出す = bắt đầu nói ra trước tiên = 一番先に言った."
            ),
            "examples": [
                {"jp": "ネガティブ ＝ 否定的（ひていてき） ↔ 肯定的（こうていてき）", "vi": "Cẩn thận bẫy trái nghĩa: 肯定的 là tích cực (Positive)."},
                {"jp": "用事が済む ＝ 終わる / 残らず ＝ 全部", "vi": "済む đồng nghĩa 終わる (không phải 始まる); 残らず = không sót chút nào = 全部."},
                {"jp": "女の人には甘い ＝ やさしい ↔ きびしい", "vi": "甘い chỉ thái độ với người nghĩa là dễ dãi, chiều chuộng (trái với きびしい)."},
            ],
            "quick_check": [
                {
                    "prompt": "Trong 問題4, từ đồng nghĩa với 「ネガティブ」 là từ nào (tránh bẫy trái nghĩa)?",
                    "options": ["肯定的", "積極的", "否定的", "冷静だ"],
                    "correct_index": 2,
                    "note": "ネガティブ (negative) = 否定的 (tiêu cực); 肯定的 là từ trái nghĩa (positive).",
                },
                {
                    "prompt": "Nghĩa mở rộng của 「計画を言い出した」 tương đương với cụm nào?",
                    "options": ["一番最後に言った", "一番先に言った", "忘れていた", "否定した"],
                    "correct_index": 1,
                    "note": "Vます + 出す diễn tả hành động bắt đầu phát sinh -> 言い出す = người đề xuất đầu tiên.",
                },
            ],
        },
    },
    {
        "code": "MU-06",
        "order_index": 6,
        "title": "Tượng thanh/Phó từ & Cách dùng từ tự nhiên",
        "section": "vocab",
        "target_skill": "問題5 Kiểm tra chủ ngữ/tân ngữ hợp lệ (生える vs 建つ, ぐっすり+眠る, ぴったり vs ばったり, 気に入る vs 気になる)",
        "estimated_minutes": 30,
        "bridge": {
            "grammar_focus": "Phân biệt từ tượng thanh đuôi ったり, cụm từ với 気 (Khí) & giới hạn kết hợp ngữ nghĩa của động từ",
            "explanation_vi": (
                "問題5 là phần dễ mất điểm nhất vì 3 câu sai thường được chế cực tự nhiên về ngữ pháp nhưng SAI kết hợp từ (Collocation):\n"
                "1. Bộ 4 từ tượng thanh đuôi ったり: ぴったり (vừa khít/khớp), ばったり (tình cờ chạm mặt), しっかり (chăm chỉ/chắc chắn), ぐったり (mệt lử).\n"
                "2. Phó từ giới hạn động từ: ぐっすり CHỈ đi với ngủ (眠る/寝る); それぞれ = mỗi cá nhân (khác そろそろ = sắp sửa).\n"
                "3. Bộ 4 cụm từ với 気: 気に入る (ưng ý vật/người), 気になる (lo lắng/bận tâm), 気がする (có linh cảm), 気がつく (chợt nhận ra).\n"
                "4. Giới hạn chủ/tân ngữ: 生える (cây/tóc/râu mọc — nhà phải dùng 建つ, ý tưởng dùng 浮かぶ); おかず (món ăn kèm cơm — bánh/cơm là 主食); 繰り返す (lặp lại lời/việc — quay đầu dùng 振り返る, đổ bàn dùng ひっくり返す)."
            ),
            "examples": [
                {"jp": "ぴったり合う vs ばったり会う vs ぐったりする", "vi": "Áo vừa khít = ぴったり; tình cờ gặp = ばったり; mệt rũ = ぐったり."},
                {"jp": "服が気に入る vs テストが気になる vs さいふに気がつく", "vi": "Ưng ý = 気に入る; lo lắng = 気になる; chợt nhớ/nhận ra = 気がつく."},
                {"jp": "草木が生える ↔ 家が建つ ↔ アイデアが浮かぶ", "vi": "Sinh vật hữu cơ mọc từ đất/da mới dùng 生える."},
            ],
            "quick_check": [
                {
                    "prompt": "Khi muốn diễn tả 'tình cờ gặp lại bạn cũ ở nước ngoài', dùng từ tượng thanh nào?",
                    "options": ["ぴったり", "ぐっすり", "ばったり", "しっかり"],
                    "correct_index": 2,
                    "note": "ばったり会う = tình cờ chạm mặt; ぴったり = vừa vặn.",
                },
                {
                    "prompt": "Câu 「明日のテストが【気に入って】心配だ」 sai vì dùng nhầm cụm 気 nào?",
                    "options": ["気がする", "気になる", "気がつく", "気に入る"],
                    "correct_index": 1,
                    "note": "Lo lắng, bận tâm về kỳ thi phải dùng 気になる (きになる), không dùng 気に入る (ưng ý).",
                },
            ],
        },
    },
    {
        "code": "MU-07",
        "order_index": 7,
        "title": "Nền tảng Chia động từ N4->N3 & Mẫu Ý chí/Trạng thái",
        "section": "grammar",
        "target_skill": "Ôn chắc 4 thể N4 (Vえる khả năng, Vさせる sai khiến, Vられる bị động, Vてくる/いく) & Vやすい/にくい, Vたばかり/つもり",
        "estimated_minutes": 28,
        "bridge": {
            "grammar_focus": "Kết nối trực tiếp 4 thể biến đổi động từ N4 (Khả năng/Sai khiến/Bị động/てくる) vào cấu trúc mục đích & trạng thái N3",
            "explanation_vi": (
                "Nếu chưa vững 4 biến đổi động từ N4, học viên N5 sẽ chọn nhầm hàng loạt câu Ngữ pháp câu đơn và Đục lỗ N3:\n"
                "1. Khả năng (Vえる) & Không ý chí (Vない): BẮT BUỘC đi với ように (読めるように = để có thể đọc, かぜをひかないように = để không bị cảm). CẤM dùng ために sau thể khả năng!\n"
                "2. Sai khiến (Vさせる): [V(sai khiến)て + ほしい] = muốn đối phương cho phép mình làm (わたしにも読ませてほしい).\n"
                "3. Tính từ hóa Vます+やすい/にくい/たて: [Vます+やすい] là tính từ đuôi い -> kết hợp なる phải đổi い->く (つけやすくなる); [Vます+たて] = vừa mới nấu/làm xong nóng hổi (炊きたてのごはん).\n"
                "4. Bị động tiếp diễn: [Vられる + てきた] = đã và đang được làm từ xưa (昔からつくられてきました); [Vた+つもりだ] = cứ đinh ninh là đã làm."
            ),
            "examples": [
                {"jp": "読めるように（○） vs 読めるために（×）", "vi": "Thể khả năng luôn đi với ように, không bao giờ kết hợp ために."},
                {"jp": "わたしにも読ませてほしい", "vi": "Sai khiến 読ませる + てほしい = muốn được phép đọc (khác 読んでほしい = muốn người khác đọc cho mình)."},
                {"jp": "つけやすい + なる -> つけやすくなる", "vi": "Đuôi やすい chia như tính từ い (bỏ い + く + なる)."},
            ],
            "quick_check": [
                {
                    "prompt": "Chọn đáp án đúng ngữ pháp với động từ thể khả năng 「読める」:",
                    "options": ["読めるために", "読めるように", "読むように", "読むための"],
                    "correct_index": 1,
                    "note": "Thể khả năng 読める chỉ kết hợp với ように (để có thể...), tuyệt đối không đi với ために.",
                },
                {
                    "prompt": "Mẫu nào có nghĩa 'vừa mới nấu xong nóng hổi' khi bổ nghĩa trực tiếp cho danh từ 「ごはん」?",
                    "options": ["炊きかけ", "炊きっぱなし", "炊きたて", "炊いたとたん"],
                    "correct_index": 2,
                    "note": "Vます + たて + の + N diễn tả sự vật vừa mới hoàn tất còn mới/nóng hổi.",
                },
            ],
        },
    },
    {
        "code": "MU-08",
        "order_index": 8,
        "title": "Trợ từ nhấn mạnh, Phủ định một phần & Từ nối N3",
        "section": "grammar",
        "target_skill": "Phân biệt trợ từ nâng cao (でも/さえ/こそ/しか/ばかり), nối câu (つまり/たとえば/のに対して) & phủ định một phần (わけではない)",
        "estimated_minutes": 30,
        "bridge": {
            "grammar_focus": "Nâng cấp trợ từ N4 (しか/だけ/ばかり) lên N3 (でも/さえ/こそ), cặp phủ định một phần & từ nối giải thích/ví dụ",
            "explanation_vi": (
                "Cụm câu hỏi N3 rất thích bẫy ranh giới giữa các trợ từ và mẫu có chữ わけ:\n"
                "1. Trợ từ N4->N3: [Số nhỏ + でも + ば/たら] = dù chỉ... thôi cũng; [N + さえ] = ngay cả/đến cả (dù thiếu mức tối thiểu); [N + こそ] = chính là (nhấn mạnh tuyệt đối); [N + しか + Phủ định] = chỉ.\n"
                "2. Phủ định một phần vs Cấm/Không thể: [～わけではない] = không hẳn là (dù có みんな/tất cả vẫn có ngoại lệ); khác hẳn [～わけにはいかない] = không thể làm vì lý do đạo lý/quy tắc.\n"
                "3. Cặp liên từ dễ nhầm: つまり (tức là, diễn giải lại khái niệm) vs たとえば (ví dụ minh họa cụ thể); ～のに対して (tương phản 2 vế) vs ～によって (tùy theo / bởi tác nhân)."
            ),
            "examples": [
                {"jp": "一度でも会えば vs 言葉さえできなくても vs この考え方こそ", "vi": "でも = dù chỉ 1 lần; さえ = ngay cả đến mức tối thiểu; こそ = chính là."},
                {"jp": "みんながそう思っているわけではない", "vi": "Không phải tất cả mọi người đều nghĩ vậy (phủ định một phần)."},
                {"jp": "Vてばかりいる vs Nだらけだ", "vi": "ばかりいる gắn sau Vて; だらけ chỉ gắn sau Danh từ (間違いだらけ)."},
            ],
            "quick_check": [
                {
                    "prompt": "Điền dạng nối đúng sau động từ chia thể て 「毎日寝て（　）」:",
                    "options": ["だらけだ", "ばかりいる", "のみだ", "続けている"],
                    "correct_index": 1,
                    "note": "Vて + ばかりいる = suốt ngày chỉ toàn làm V; だらけ chỉ đi với danh từ.",
                },
                {
                    "prompt": "Trong câu minh họa bằng con số cụ thể ('ví dụ mặt 2 tuần, chỗ khác 4 tuần'), dùng từ nối nào?",
                    "options": ["つまり", "それとも", "たとえば", "もちろん"],
                    "correct_index": 2,
                    "note": "たとえば đưa ví dụ cụ thể minh họa quy tắc chung; つまり dùng để đúc kết/giải thích lại.",
                },
            ],
        },
    },
    {
        "code": "MU-09",
        "order_index": 9,
        "title": "Ngữ pháp Mạch văn & Đọc hiểu Đục lỗ (4 Bài văn)",
        "section": "grammar",
        "target_skill": "Bài đọc đục lỗ 問題3 (文章の文法): bắt mạch thời gian (昔から/最近/これから), câu mở đoạn & cặp hô ứng (おそらく～に違いない)",
        "estimated_minutes": 30,
        "bridge": {
            "grammar_focus": "Xác định mạch thời gian đoạn văn, danh từ hóa mệnh đề (～のを防ぐ) & ngữ điệu văn phong y tế/nghị luận",
            "explanation_vi": (
                "Đừng dịch từng chữ trong bài đục lỗ 問題3 — hãy đọc theo 3 trục tín hiệu:\n"
                "1. Trục Thời gian & Thể động từ: 昔から (từ xưa -> Vてきた); 最近 (gần đây -> Vつつある = đang dần giảm/thay đổi); これからの (từ nay về sau -> Vていくでしょう).\n"
                "2. Trục Danh từ hóa & Trợ từ: Khi động từ chính là tha động từ như 防ぐ (ngăn chặn), mệnh đề đứng trước phải danh từ hóa bằng の + を (入るのを防ぐ).\n"
                "3. Trục Văn phong & Hô ứng: Hướng dẫn sử dụng/y khoa dùng cảnh báo trang trọng [～おそれがある] (có nguy cơ), KHÔNG dùng [～にきまっている]; câu mở đầu cho chuỗi まず…それから… chọn câu chủ đề [注意する点があります]; おそらく kéo theo [～に違いない]."
            ),
            "examples": [
                {"jp": "昔からつくられてきました -> 減りつつあります -> 使われていくでしょう", "vi": "Bắt 3 mốc thời gian là giải trúng 3 câu trong bài 緑のカーテン."},
                {"jp": "空気が入るのを防ぎます", "vi": "防ぐ là tha động từ đi với を -> dùng のを để danh từ hóa mệnh đề."},
                {"jp": "おそらく～に違いない / わからないせいで / つらくなることもある", "vi": "せいで chỉ nguyên nhân dẫn tới hậu quả đáng tiếc (くやしい)."},
            ],
            "quick_check": [
                {
                    "prompt": "Mốc thời gian 「これからの日本の家に…」 yêu cầu chọn đuôi câu nào?",
                    "options": ["増えてきました", "使われていくでしょう", "つくられました", "減りつつあります"],
                    "correct_index": 1,
                    "note": "これからの hướng về tương lai nên đi với Vていくでしょう; ～てきた chỉ từ quá khứ tới hiện tại.",
                },
                {
                    "prompt": "Để nối mệnh đề 「冷たい空気が入る」 làm tân ngữ cho động từ 「防ぎます」, dùng tiểu từ nào?",
                    "options": ["ことが", "とか", "のを", "ものを"],
                    "correct_index": 2,
                    "note": "防ぐ nhận tân ngữ với を nên danh từ hóa hành động bằng の + を.",
                },
            ],
        },
    },
    {
        "code": "MU-10",
        "order_index": 10,
        "title": "Thuật toán Ghép câu Sao ★ (4-Slot Assembly)",
        "section": "grammar",
        "target_skill": "問題2 Sắp xếp câu 4 ô [1][2][3][4]: ghép cụm định ngữ N4, vị trí trợ từ (における/にとって/を問わず) & cặp hô ứng",
        "estimated_minutes": 30,
        "bridge": {
            "grammar_focus": "Quy tắc ghép cụm 2 mảnh N4->N3 (Định ngữ + N, N1におけるN2, 決して～わけではない, ばかりでなく～も)",
            "explanation_vi": (
                "Tuyệt đối KHÔNG thử mò vị trí dấu ★. Hãy ghép đủ cả 4 ô theo thuật toán 3 bước:\n"
                "1. Khóa chặt điểm neo trước và sau 4 ô trống: nhìn chữ ngay trước ô 1 (như 機内, 掃除用具, 先輩) và chữ ngay sau ô 4 (như と言われてきた, されています, ではない).\n"
                "2. Ghép các cặp 2 mảnh cố định trước: [N + における + N], [N + として], [Vる + ことに + する], [決して + A + わけ + ではない], [N1 + ばかり + でなく + N2 + も], [さえ + あれば], [たとえ + どんなに + Aい + Nでも].\n"
                "3. Ráp đủ cả 4 ô rồi đọc trơn từ đầu đến cuối câu để kiểm tra mạch định ngữ N4 (Mệnh đề thể thông thường + Danh từ)."
            ),
            "examples": [
                {"jp": "機内 [における] [携帯電話の] [使用は] [禁止] されています。", "vi": "N1 + における + N2 + は + Danh động từ + されている."},
                {"jp": "女性の平均 [からすると] [決して] [小さい] [わけ] ではない。", "vi": "Khóa cặp hô ứng 決して…わけではない trước, đặt からすると làm vế đánh giá."},
                {"jp": "ピアノ [ばかり] [でなく] [バイオリン] [も] ひける。", "vi": "Cặp song hành kinh điển: N1 ばかりでなく N2 も."},
            ],
            "quick_check": [
                {
                    "prompt": "Trong cặp hô ứng 「決して ～ ではない」, từ nào bắt buộc đứng ngay trước 「ではない」?",
                    "options": ["からすると", "わけ", "ばかり", "こと"],
                    "correct_index": 1,
                    "note": "Cấu trúc hoàn chỉnh là 決して ～ わけではない (hoàn toàn không hẳn là).",
                },
                {
                    "prompt": "Thứ tự đúng của mẫu 'với tư cách là đại diện' là gì?",
                    "options": ["として + チームの代表", "チームの代表 + として", "に + のかわり", "でなく + ばかり"],
                    "correct_index": 1,
                    "note": "Danh từ luôn đứng trước として (Nとして = với tư cách là N).",
                },
            ],
        },
    },
    {
        "code": "MU-11",
        "order_index": 11,
        "title": "Dokkai Ngắn & Trung: Câu chốt, Paraphrase & Từ chỉ thị",
        "section": "reading",
        "target_skill": "Đọc hiểu đoạn ngắn/trung (短文・中文): tách mệnh đề chính, tìm câu chốt sau しかし/それに, truy vết từ chỉ thị (このルール) & chú thích (注1)",
        "estimated_minutes": 40,
        "bridge": {
            "grammar_focus": "Giải mã câu dài N4->N3 (tách chủ ngữ trước は/が), câu hỏi tu từ (～ではないだろうか) & 3 bẫy suy diễn",
            "explanation_vi": (
                "Kỷ luật vàng Dokkai ngắn & trung là **Evidence-First (Tìm đúng câu chốt trước khi đọc 4 đáp án)**:\n"
                "1. Tín hiệu kết luận của tác giả: Luận điểm thật nằm SAU 「しかし」/「けれども」; nguyên nhân tổng hợp liệt kê qua 「それに」 (phải gộp ĐỦ cả 2 ý, không chọn đáp án chỉ có 1 vế); ý kiến tác giả hay giấu trong câu hỏi tu từ 「～ではないだろうか」「～はどうだろうか」.\n"
                "2. Truy vết từ chỉ thị (このルール, それ, 意味がよくわかりました): Câu trả lời luôn nằm ở 1–2 câu NGAY LIỀN TRƯỚC.\n"
                "3. Đọc kỹ chú thích `(注1)` cuối bài (đáp án đúng thường paraphrase từ định nghĩa trong chú thích) và gạch bỏ các đáp án dùng từ tuyệt đối (必ず, すべて, より) khi bài chỉ nói cân bằng hoặc かもしれない."
            ),
            "examples": [
                {"jp": "一番の原因 (nguyên nhân #1) vs 原因の一つ (một trong các nguyên nhân)", "vi": "Bài マグロ hỏi 最も大きな原因 -> loại bẫy môi trường biển (chỉ là 原因の一つ)."},
                {"jp": "それに (hơn nữa) -> 危ないし、耳が悪くなるから", "vi": "Bài tai nghe có 2 ý nối bằng それに: vừa nguy hiểm xe phía sau vừa hỏng thính lực."},
                {"jp": "結婚してからいちどもお寺にいっていない ＝ 最近全然行っていない", "vi": "Paraphrase cốt lõi bài cô giáo Kotani."},
            ],
            "quick_check": [
                {
                    "prompt": "Khi đoạn văn dùng từ nối 「それに」 để liệt kê 2 lý do A và B, đáp án đúng phải thỏa điều kiện gì?",
                    "options": ["Chỉ cần nêu lý do A", "Nêu ngược lại lý do B", "Bao quát đủ cả 2 ý A và B", "Dùng từ tuyệt đối 必ず"],
                    "correct_index": 2,
                    "note": "Đề JLPT N3 luôn cài bẫy đáp án thiếu 1 nửa ý khi bài văn liệt kê 2 luận cứ bằng それに.",
                },
                {
                    "prompt": "Câu kết có dạng 「～重要ではないだろうか」 biểu đạt thái độ nào của tác giả?",
                    "options": ["Phản đối hoàn toàn", "Khẳng định là rất quan trọng (câu hỏi tu từ)", "Không rõ ý kiến", "Kể lại tin đồn"],
                    "correct_index": 1,
                    "note": "～ではないだろうか (chẳng phải là ... sao?) là câu hỏi tu từ khẳng định chủ trương của tác giả.",
                },
            ],
        },
    },
    {
        "code": "MU-12",
        "order_index": 12,
        "title": "Dokkai Tìm kiếm Thông tin: Ma trận Điều kiện & Ngoại lệ",
        "section": "reading",
        "target_skill": "情報検索: Đối chiếu ma trận [Nhân vật x Điều kiện 1,2] và soi mục ngoại lệ ẩn (注意, 休診, テキスト代は別, 対象)",
        "estimated_minutes": 25,
        "bridge": {
            "grammar_focus": "Từ vựng hành chính/tờ rơi N4->N3 (対象, 休診, 注意, 以内, 受講料, 別) & kỹ thuật đọc ngược từ câu hỏi",
            "explanation_vi": (
                "Bài 情報検索 (Tìm kiếm thông tin) là phần dễ đạt điểm tuyệt đối nhất NẾU không đọc lướt mục chữ nhỏ cuối tờ rơi:\n"
                "1. Không đọc từ đầu đến cuối tờ rơi! Đọc câu hỏi trước -> lập danh sách 3 điều kiện của nhân vật (Tuổi / Trình độ / Lịch rảnh / Nhu cầu).\n"
                "2. Soi 4 cụm từ khóa bẫy kinh điển: 対象 (đối tượng hợp lệ độ tuổi/trình độ), 休診 (ngày nghỉ khám), 注意 (ngoại lệ giảm học phí hoặc ngày nghỉ đột xuất), テキスト代は別 (tiền sách tính riêng cộng thêm).\n"
                "3. Đọc kỹ ngoại lệ tích cực: ví dụ 「病院が休みの日でも、電話で受付できます」 — bệnh viện nghỉ khám thứ 5 nhưng VẪN gọi đặt lịch cho sáng thứ 6 được!"
            ),
            "examples": [
                {"jp": "受講料 5,000円 + 注意(Bスペイン語 4,500円) + テキスト代別(1,000円)", "vi": "Tổng tiền phải nộp = 4,500 + 1,000 = 5,500 yên (không phải 6,000 yên!)."},
                {"jp": "休診：木曜日 + 病院が休みの日でも電話で受付できます", "vi": "Khám sáng Thứ 6 -> gọi từ 9:00 sáng hôm trước (chính là sáng Thứ 5)."},
                {"jp": "番号を押して、〈#〉を押してください", "vi": "Thứ tự bấm phím: <診察券番号> trước rồi mới đến <#>."},
            ],
            "quick_check": [
                {
                    "prompt": "Khi tờ rơi ghi 「受講料 5,000円」「テキスト代は別 1,000円」 và mục 「注意」 ghi lớp B giảm còn 4,500円, tổng tiền là bao nhiêu?",
                    "options": ["5,000円", "6,000円", "5,500円", "4,500円"],
                    "correct_index": 2,
                    "note": "Luôn áp dụng ngoại lệ ở mục 注意 (4,500円) rồi cộng tiền giáo trình tính riêng (1,000円) = 5,500円.",
                },
                {
                    "prompt": "Câu 「病院が休みの日でも、電話で受付できます」 cho phép làm gì vào ngày nghỉ khám (休診)?",
                    "options": ["Đến khám trực tiếp", "Không gọi điện được", "Gọi điện đặt lịch cho ngày hôm sau", "Chỉ hủy lịch"],
                    "correct_index": 2,
                    "note": "Dù ngày Thứ 5 bệnh viện nghỉ khám vẫn có thể gọi điện đặt lịch cho sáng Thứ 6 từ 9:00 sáng.",
                },
            ],
        },
    },
]


def seed_micro_units_and_bridges(conn: sqlite3.Connection) -> int:
    """Upsert all 12 Micro-Units and 12 N4->N3 Bridge Capsules into SQLite."""
    for unit in MICRO_UNITS_SPEC:
        conn.execute(
            """
            INSERT INTO MICRO_UNITS (code, order_index, title, section, target_skill, estimated_minutes)
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(code) DO UPDATE SET
                order_index=excluded.order_index,
                title=excluded.title,
                section=excluded.section,
                target_skill=excluded.target_skill,
                estimated_minutes=excluded.estimated_minutes
            """,
            (
                unit["code"],
                unit["order_index"],
                unit["title"],
                unit["section"],
                unit["target_skill"],
                unit["estimated_minutes"],
            ),
        )
        bridge = unit["bridge"]
        conn.execute(
            """
            INSERT INTO N4_BRIDGE_CAPSULES
                (unit_code, grammar_focus, explanation_vi, examples_json, quick_check_json)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(unit_code) DO UPDATE SET
                grammar_focus=excluded.grammar_focus,
                explanation_vi=excluded.explanation_vi,
                examples_json=excluded.examples_json,
                quick_check_json=excluded.quick_check_json
            """,
            (
                unit["code"],
                bridge["grammar_focus"],
                bridge["explanation_vi"],
                json.dumps(bridge["examples"], ensure_ascii=False),
                json.dumps(bridge["quick_check"], ensure_ascii=False),
            ),
        )
    return len(MICRO_UNITS_SPEC)
