"""Exact Content-Hash Question Grammar Map (163/163 Exam Questions) & Dynamic Analyzer.

Maps every unique question from the 7 JLPT N3 exam workbooks (by immutable
compute_question_hash SHA-256) to:
- Validated grammar links (primary_target, distractor_trap, sentence_structure, discourse_marker)
- Vietnamese syntactic/discourse structure dissection (including 4-slot ★ assembly chains)
- Pedagogical recognition & trap-avoidance takeaway
- Exact per-option grammar/collocation notes

Also provides analyze_question_grammar(question_dict, passage_dict) to fall back
on GRAMMAR_POINTS_DATA match_patterns when future .xlsx exam files are uploaded.
"""

import json
import re
from typing import Any, Dict, List, Optional

from n3_mastery.grammar_corpus import GRAMMAR_POINTS_DATA
from n3_mastery.importer import compute_question_hash


QUESTION_GRAMMAR_MAP: Dict[str, Dict[str, Any]] = {
    # =========================================================================
    # SECTION 1: GRAMMAR (42 QUESTIONS: IDs 15-29, 49-63, 146-157)
    # =========================================================================
    # ID=15
    "467c0e24ec847b662c005029c40c488762a491085596a80b54ad7df71cd9b6b3": {
        "links": [
            {"grammar_code": "GP-N3-043", "role": "primary_target", "note_vi": "Số từ tối thiểu + でも + ば/たら: dù chỉ một lần thôi mà..."},
            {"grammar_code": "GP-N3-044", "role": "distractor_trap", "note_vi": "Bẫy 一度も: bắt buộc đi với câu phủ định (~ない), không đi với điều kiện khẳng định あれば."},
            {"grammar_code": "GP-N3-023", "role": "distractor_trap", "note_vi": "Bẫy さえ: 一度さえ会えば thường dùng ở cặp さえ～ば mà không tự nhiên bằng 一度でも sau 一度 trong văn nói."},
            {"grammar_code": "GP-N3-042", "role": "distractor_trap", "note_vi": "Bẫy こそ: nhấn mạnh 'chính là', không ghép vào số lượng tối thiểu 一度 trước ば."},
            {"grammar_code": "GP-N4-16", "role": "sentence_structure", "note_vi": "Mệnh đề điều kiện ことがあれば (nếu có việc từng gặp...) phối hợp cùng Số từ + でも."},
        ],
        "structure_parse_vi": (
            "[一度 + でも] (dù chỉ 1 lần) + [会ったことがあれば] (nếu đã từng gặp - GP-N5-09 + điều kiện ば) "
            "-> [友だちだと考える] (mệnh đề định ngữ trích dẫn với と) + [人もいる] (cũng có người cho rằng...)."
        ),
        "pedagogical_takeaway_vi": "Thấy [Số lượng tối thiểu: 一度 / 少し / 1分] + [Chỗ trống] + [～ば / ～たら] trong câu khẳng định -> chọn ngay でも.",
        "option_grammar_notes": [
            "も: Lượng từ + も trong câu này đòi hỏi phủ định (~一度も会ったことがない), mâu thuẫn với あれば.",
            "でも: ĐÚNG. 一度でも会ったことがあれば = dù chỉ từng gặp mặt một lần thôi mà...",
            "さえ: Sắc thái điều kiện tối thiểu trong cặp さえ～ば không kết hợp tự nhiên ở đây bằng 一度でも.",
            "こそ: Trợ từ nhấn mạnh đối tượng ('chính là...'), sai chức năng với số từ tối thiểu.",
        ],
    },
    # ID=16
    "19bc06832e3f187d9eaffe95413f335816d84236ff3e68fd252eba2b8c08ce9d": {
        "links": [
            {"grammar_code": "GP-N3-005", "role": "primary_target", "note_vi": "N + によって + Phân loại: phân chia tùy theo tiêu chí kích thước."},
            {"grammar_code": "GP-N3-106", "role": "distractor_trap", "note_vi": "Bẫy に比べて: so sánh 2 đối tượng (AはBに比べて), không chỉ tiêu chí phân loại thành 3 nhóm."},
            {"grammar_code": "GP-N3-047", "role": "distractor_trap", "note_vi": "Bẫy について: nghĩa là 'nói/viết về chủ đề N'."},
            {"grammar_code": "GP-N3-013", "role": "distractor_trap", "note_vi": "Bẫy に対して: nghĩa là 'đối với (thái độ)' hoặc 'trái lại'."},
        ],
        "structure_parse_vi": (
            "Câu 1 giới thiệu vật tồn tại [ここにたくさんのびんがあります] (GP-N5-03 địa điểm tồn tại に). "
            "Câu 2 [大きさ + によって] (tùy theo kích cỡ) + [三つに + 分けてください] (hãy chia làm 3 phần - kết quả biến đổi に + てください GP-N5-10)."
        ),
        "pedagogical_takeaway_vi": "Khi động từ phía sau là 分ける (phân loại), 違う (khác nhau), 変わる (thay đổi) -> gắn danh từ tiêu chí với によって.",
        "option_grammar_notes": [
            "に比べて: So sánh hơn kém giữa hai vật, không dùng trước 'hãy chia thành ba nhóm'.",
            "について: 'Về chủ đề...', chỉ đi với động từ nói/viết/tìm hiểu (話す, 書く, 調べる).",
            "によって: ĐÚNG. 大きさによって三つに分ける = phân chia thành 3 nhóm tùy theo kích thước.",
            "に対して: Chỉ hướng thái độ/ứng xử hoặc tương phản, không chỉ tiêu chí phân loại.",
        ],
    },
    # ID=17
    "a1c14224a6e164e6b6278040e4e4001e1793d9e3067cfb5f0446c2a3d8fc3f02": {
        "links": [
            {"grammar_code": "GP-N3-036", "role": "primary_target", "note_vi": "V(sai khiến)て + ほしい: muốn đối phương cho phép mình (わたしにも) được đọc."},
            {"grammar_code": "GP-N5-11", "role": "distractor_trap", "note_vi": "Bẫy 読んでほしい: nghĩa là muốn BẠN đọc hộ cho tôi (sai vai chủ thể so với わたしにも + お借りしてもいいですか)."},
            {"grammar_code": "GP-N4-03", "role": "distractor_trap", "note_vi": "Bẫy bị động 読まれてほしい: vô nghĩa vì ほしい không gắn sau bị động để xin phép."},
            {"grammar_code": "GP-N5-07", "role": "distractor_trap", "note_vi": "Bẫy danh từ hóa 読むのがほしい: ほしい nhận danh từ với が, không gắn trực tiếp sau mệnh đề Vる + の."},
            {"grammar_code": "GP-N4-02", "role": "sentence_structure", "note_vi": "Chia thể sai khiến chuẩn cho nhóm 1: 読む -> 読ませる -> 読ませて."},
        ],
        "structure_parse_vi": (
            "Thoại B: [じゃ、わたしにも] (vậy thì tôi cũng - đối tượng được cho phép に) + [読ませてほしいです] (muốn bạn cho phép tôi đọc - sai khiến + ほしい). "
            "Câu sau xác nhận lại quyền mượn: [お借りしてもいいですか] (khiêm nhường + てもいいですか)."
        ),
        "pedagogical_takeaway_vi": "Thấy cụm [わたしに / 私にも] + [___ほしい] kèm ý xin phép làm -> 100% chia V(sai khiến)て + ほしい.",
        "option_grammar_notes": [
            "読んで: 読んでほしい nghĩa là 'muốn bạn đọc (cho tôi nghe)', mâu thuẫn với câu xin mượn sách お借りしてもいいですか.",
            "読まれて: Thể bị động không kết hợp với ほしい để xin phép làm hành động.",
            "読ませて: ĐÚNG. V(sai khiến)て + ほしい = muốn bạn cho phép tôi được đọc.",
            "読むのが: Sai ngữ pháp vì tính từ ほしい mong muốn đồ vật (Nがほしい), không gắn mệnh đề hành động + ほしい.",
        ],
    },
    # ID=18
    "f713367a063d0e08bd70aa00a308b7752011f0288d3f35e7542e8080c47fcc4f": {
        "links": [
            {"grammar_code": "GP-N3-095", "role": "primary_target", "note_vi": "Vる + のに + いい: rất thích hợp cho việc đọc sách."},
            {"grammar_code": "GP-N3-096", "role": "distractor_trap", "note_vi": "Bẫy ことで: chỉ phương tiện đạt kết quả ('bằng cách đọc sách'), không ghép với đánh giá 'là mùa tốt'."},
            {"grammar_code": "GP-N4-11", "role": "distractor_trap", "note_vi": "Bẫy できるように: 'để có thể đọc sách', diễn tả nỗ lực đạt khả năng chứ không đánh giá sự phù hợp của mùa."},
            {"grammar_code": "GP-N3-001", "role": "distractor_trap", "note_vi": "Bẫy できるうちに: 'tranh thủ lúc còn đọc được thì...', sai sắc thái câu chân lý văn hóa."},
            {"grammar_code": "GP-N3-026", "role": "discourse_marker", "note_vi": "Đuôi と言われている truyền đạt nhận định phổ biến của người Nhật về mùa thu."},
        ],
        "structure_parse_vi": (
            "[日本では] (tại Nhật) [秋は] (mùa thu là) -> cụm đánh giá công dụng/thích hợp: [読書する + のに + とてもいい季節だ] "
            "-> đóng khung trích dẫn truyền đạt [と言われている] (người ta nói rằng - GP-N3-026)."
        ),
        "pedagogical_takeaway_vi": "Công thức [Nは + Vる + のに + いい / 便利だ / 役に立つ] dùng đánh giá thời điểm hoặc vật dụng thích hợp cho việc V.",
        "option_grammar_notes": [
            "読書するのに: ĐÚNG. Vる + のに + いい季節だ (mùa thích hợp để đọc sách).",
            "読書することで: 'Bằng cách đọc sách', sai quan hệ phương tiện - mục đích.",
            "読書できるように: 'Để có thể đọc sách', chỉ mục tiêu hành động chủ ý thay vì đánh giá đặc tính của mùa thu.",
            "読書できるうちに: 'Tranh thủ khi còn có thể đọc sách', mang ý vội vã trước khi biến đổi.",
        ],
    },
    # ID=19
    "8d11f509f8a8d5cd56d855ce34f9ed2c7ea6eb37da62f7760ac59c0256194517": {
        "links": [
            {"grammar_code": "GP-N3-041", "role": "primary_target", "note_vi": "Vた + つもりだった: cứ đinh ninh là đã viết đúng (nhưng thực tế sai)."},
            {"grammar_code": "GP-N4-14", "role": "distractor_trap", "note_vi": "Bẫy 書くことになった: nghĩa là 'được quyết định sẽ viết' (khách quan), trái nghĩa 'tự tin mình viết đúng'."},
            {"grammar_code": "GP-N4-13", "role": "distractor_trap", "note_vi": "Bẫy 書くつもりになった: 'đã chuyển sang ý định sẽ viết', dùng thể Vる không khớp quá khứ trong bài thi hôm qua."},
            {"grammar_code": "GP-N5-07", "role": "distractor_trap", "note_vi": "Bẫy 書いたことだった: không có mẫu Vた + ことだった để diễn tả niềm tin chủ quan."},
            {"grammar_code": "GP-N5-15", "role": "discourse_marker", "note_vi": "Liên từ đối lập が nối giữa nhận thức chủ quan (つもりだった) và sự thật (間違いだった)."},
        ],
        "structure_parse_vi": (
            "Bối cảnh [きのうの試験で] (địa điểm sự kiện で) + chủ thể nhấn mạnh [自分では] (tự bản thân mình thì) + "
            "[正しい答えを + 書いたつもりだった] (đinh ninh là đã viết đáp án đúng - GP-N3-041) "
            "+ [が、わたしの答えは間違いだった] (nhưng thực tế lại sai)."
        ),
        "pedagogical_takeaway_vi": "Thấy [自分では...] + [Vた___] + [～が、実は / 実際は...] -> 100% là Vた + つもりだ (cứ tưởng mình đã làm chuẩn).",
        "option_grammar_notes": [
            "書くつもりになった: Vる + つもりになる nghĩa là 'bắt đầu nảy sinh ý định sẽ viết', không phải 'đinh ninh đã viết đúng'.",
            "書いたつもりだった: ĐÚNG. Vた + つもりだった = cứ tưởng chắc là đã viết đúng rồi.",
            "書くことになった: 'Đã được quyết định sẽ viết', nói về quyết định khách quan.",
            "書いたことだった: Không mang nghĩa 'tự cho rằng/tưởng rằng'.",
        ],
    },
    # ID=20
    "4f6862b78d71a7e4bce65d62c317da4ba896635afe661eb8379c8be8dc96611c": {
        "links": [
            {"grammar_code": "GP-N3-053", "role": "primary_target", "note_vi": "Vて + ばかりいる + と: nếu cứ suốt ngày chỉ toàn làm việc như thế thì sẽ đổ bệnh."},
            {"grammar_code": "GP-N4-22", "role": "distractor_trap", "note_vi": "Bẫy したばかりだと: Vたばかり là 'vừa mới làm xong', mâu thuẫn với thói quen lặp lại quá mức gây đổ bệnh."},
            {"grammar_code": "GP-N4-21", "role": "distractor_trap", "note_vi": "Bẫy したところでは / したところだと: Vたところ là 'vừa dứt hành động tức thì', sai về mặt tích lũy kiệt sức."},
            {"grammar_code": "GP-N4-16", "role": "sentence_structure", "note_vi": "Cấu trúc điều kiện と dẫn đến hệ quả tiêu cực tất yếu (体をこわしますよ)."},
        ],
        "structure_parse_vi": (
            "[そんなに + 仕事を + してばかりいる] (cứ suốt ngày chỉ toàn làm việc nhiều đến mức đó - GP-N3-053) "
            "+ điều kiện tất yếu [と] (GP-N4-16) -> hậu quả cảnh báo [体をこわしますよ]."
        ),
        "pedagogical_takeaway_vi": "Ghi nhớ cặp bẫy sát thủ của JLPT N3: Vて + ばかりいる (lặp đi lặp lại đến phát mệt) khác hẳn Vた + ばかりだ (vừa mới làm xong).",
        "option_grammar_notes": [
            "したばかりだと: Vた + ばかりだ là 'vừa mới làm xong', không phải nguyên nhân kiệt sức do làm quá nhiều.",
            "してばかりいると: ĐÚNG. Vて + ばかりいる = suốt ngày chỉ toàn làm việc (phàn nàn tần suất).",
            "したところでは: Vたところ là 'vừa mới xong tức thì', và では không dẫn tới hệ quả như vậy.",
            "したところだと: 'Nếu bảo là vừa mới làm xong thì...', sai cả thì lẫn nghĩa.",
        ],
    },
    # ID=21
    "e0ecfaaadc69002a60f27af7a04cc9a8830ab37d2748cf956785e17ea6749138": {
        "links": [
            {"grammar_code": "GP-N3-094", "role": "primary_target", "note_vi": "AというのはBのことだ: định nghĩa khái niệm/thuật ngữ '球技' là các môn thể thao dùng bóng."},
            {"grammar_code": "GP-N3-097", "role": "distractor_trap", "note_vi": "Bẫy というものだ: nêu bản chất/chân lý tự nhiên hoặc quy chuẩn chung, không dùng giải thích từ điển."},
            {"grammar_code": "GP-N3-028", "role": "distractor_trap", "note_vi": "Bẫy というのだ / という: chỉ ý giải thích nhấn mạnh của người nói hoặc thiếu danh từ hóa kết câu."},
            {"grammar_code": "GP-N5-06", "role": "sentence_structure", "note_vi": "Mệnh đề định ngữ [ボールを使う] bổ nghĩa cho danh từ [スポーツ]."},
        ],
        "structure_parse_vi": (
            "Chủ đề cần định nghĩa [球技 + というのは] + định ngữ mô tả [ボールを使う + スポーツ] + kết cấu định nghĩa danh từ [のことだ]."
        ),
        "pedagogical_takeaway_vi": "Gặp khung [Từ vựng X + というのは + Cụm giải thích N + ___] -> chọn ngay のことだ (hoặc ということだ nếu phía trước là mệnh đề).",
        "option_grammar_notes": [
            "というのだ: Thường dùng nhấn mạnh lý do/nhận xét của người nói ('ý là... đấy'), không phải mẫu chuẩn định nghĩa danh từ.",
            "というものだ: Nêu chân lý, bản chất đời thường (例: 人生とはそういうものだ), sai khi giải nghĩa thuật ngữ.",
            "という: Kết câu bỏ lửng dạng văn nói thiếu danh từ trung tâm.",
            "のことだ: ĐÚNG. Khung chuẩn N1というのは N2のことだ (A có nghĩa là B).",
        ],
    },
    # ID=22
    "6b54f04291331021fe6f60f019326342785b43bde2972e4b7f04c40de1453beb": {
        "links": [
            {"grammar_code": "GP-N3-038", "role": "primary_target", "note_vi": "Vる + ように言われる / と言われてきた: được dặn dò phải hành động như vậy."},
            {"grammar_code": "GP-N4-07", "role": "sentence_structure", "note_vi": "Bị động + てきた (われてきた): lời dặn dò lặp đi lặp lại suốt từ hồi nhỏ (子どものころから) tới nay."},
            {"grammar_code": "GP-N5-01", "role": "distractor_trap", "note_vi": "Bẫy nhầm thứ tự 考えて -> 行動する hay đảo vị trí trợ từ ように trước động từ."},
        ],
        "structure_parse_vi": (
            "Chuỗi lắp ghép 4 mảnh: [3. 周りのことを] (tân ngữ của 考えて) -> [1. 考えて] (thể て chỉ trình tự: nghĩ rồi mới...) "
            "-> [★ 2. 行動する] (động từ chính ở thể từ điển đứng ngay trước ように) -> [4. ように] + と言われてきた (GP-N3-038). "
            "Câu hoàn chỉnh: 子どものころから、周りのことを 考えて ★行動する ように と言われてきた。"
        ),
        "pedagogical_takeaway_vi": "Trong bài ★, cụm Nを luôn kéo động từ tha tương ứng (周りのことを考えて), còn ように luôn đứng ngay sau Vる để nối vào と言われてきた.",
        "option_grammar_notes": [
            "考えて (Slot 2): Theo sau tân ngữ 周りのことを ở Slot 1 để tạo thành cụm hành động nền rồi mới đến động từ chính.",
            "行動する (Slot 3 ★): ĐÚNG. Đứng ngay sau 考えて và ngay trước ように để hoàn chỉnh cấu trúc 行動するように.",
            "周りのことを (Slot 1): Tân ngữ mở đầu đi với trợ từ を cho động từ 考えて.",
            "ように (Slot 4): Nối động từ 行動する ở thể từ điển vào cụm trích dẫn gián tiếp と言われてきた.",
        ],
    },
    # ID=23
    "5ad45c0f335d3f22f797b24e7b18c90953860593a4237eb671f8bba8c4af345e": {
        "links": [
            {"grammar_code": "GP-N3-024", "role": "primary_target", "note_vi": "Cặp hô ứng nhượng bộ: たとえ + どんなに + Aい + Nでも."},
            {"grammar_code": "GP-N5-05", "role": "sentence_structure", "note_vi": "Tính từ đuôi い (難しい) giữ nguyên い bổ nghĩa trực tiếp cho danh từ (問題)."},
            {"grammar_code": "GP-N5-06", "role": "distractor_trap", "note_vi": "Bẫy đảo nhầm thứ tự どんなに trước たとえ hoặc đặt 問題でも vào giữa."},
        ],
        "structure_parse_vi": (
            "Chuỗi lắp ghép 4 mảnh: [3. たとえ] (mở đầu mệnh đề giả thiết nhượng bộ) -> [2. どんなに] (phó từ mức độ bổ cho tính từ) "
            "-> [★ 1. 難しい] (tính từ đuôi い bổ nghĩa trực tiếp cho danh từ sau) -> [4. 問題でも] (danh từ + でも kết cụm nhượng bộ). "
            "Câu hoàn chỉnh: わたしは たとえ どんなに ★難しい 問題でも 必ず答えはあると思う。"
        ),
        "pedagogical_takeaway_vi": "Thứ tự bất di bất dịch của cấu trúc nhượng bộ mạnh: [たとえ] -> [どんなに] -> [Tính từ] -> [Danh từ + でも].",
        "option_grammar_notes": [
            "難しい (Slot 3 ★): ĐÚNG. Đứng sau phó từ mức độ どんなに và bổ nghĩa trực tiếp cho danh từ 問題 đứng cuối.",
            "どんなに (Slot 2): Phó từ chỉ mức độ ('đến đâu đi nữa'), đứng sau たとえ và trước tính từ.",
            "たとえ (Slot 1): Liên từ mở đầu cụm nhượng bộ ('cho dù'), luôn đứng đầu vế câu.",
            "問題でも (Slot 4): Danh từ mang tiểu từ nhượng bộ でも, bắt buộc đứng ở vị trí cuối cụm trước mệnh đề chính.",
        ],
    },
    # ID=24
    "c8a07c258501c3904b9be687ceeeb39952c69e0f627be7c54e46b2296f952501": {
        "links": [
            {"grammar_code": "GP-N3-028", "role": "primary_target", "note_vi": "Mệnh đề hoàn chỉnh + という + メール (email có nội dung rằng...)."},
            {"grammar_code": "GP-N5-06", "role": "sentence_structure", "note_vi": "Định ngữ lồng 2 tầng: [乗っている] bổ nghĩa [電車], và [乗っている電車が止まっている] bổ nghĩa [メール]."},
            {"grammar_code": "GP-N5-08", "role": "distractor_trap", "note_vi": "Bẫy hoán đổi hai động từ 乗っている và 止まっている làm sai logic vật lý."},
        ],
        "structure_parse_vi": (
            "Chuỗi lắp ghép 4 mảnh: [2. 乗っている] (định ngữ: đang ngồi trên) -> [1. 電車が] (chủ thể: tàu điện) "
            "-> [★ 4. 止まっている] (vị ngữ của mệnh đề nội dung email) -> [3. という] (nối vào danh từ メール). "
            "Câu hoàn chỉnh: ...友だちから 乗っている 電車が ★止まっている という メールが来た。"
        ),
        "pedagogical_takeaway_vi": "Khi cuối câu là [...という + Danh từ thông tin (メール/話/ニュース)], hãy xác định cặp [Động từ vị ngữ -> という] đứng ở cuối cụm và ghép ngược định ngữ ra phía trước.",
        "option_grammar_notes": [
            "電車が (Slot 2): Chủ ngữ của hành động 止まっている, được bổ nghĩa bởi 乗っている đứng ngay trước nó.",
            "乗っている (Slot 1): Mệnh đề định ngữ ngắn ('mà bạn đang đi') đứng trước 電車が.",
            "という (Slot 4): Luôn gắn ngay trước danh từ メール ở cuối dãy trống để báo nội dung bức thư.",
            "止まっている (Slot 3 ★): ĐÚNG. Vị ngữ của '電車が' đứng ngay trước 'という メール'.",
        ],
    },
    # ID=25
    "5cb6b7ec88962b42bd34b1ead7f6b8435b087863e428cc663e95e7e3a38a2c2a": {
        "links": [
            {"grammar_code": "GP-N3-049", "role": "primary_target", "note_vi": "N (掃除用具) + として: với tư cách / tận dụng làm dụng cụ vệ sinh."},
            {"grammar_code": "GP-N4-13", "role": "primary_target", "note_vi": "Vる + こと + に + した: quyết định làm gì (chú ý した nằm ngoài khung!)."},
            {"grammar_code": "GP-N5-03", "role": "distractor_trap", "note_vi": "Bẫy đặt に vào giữa 掃除用具 và として hoặc đặt sai cặp こと + に trước した."},
        ],
        "structure_parse_vi": (
            "Chuỗi lắp ghép 4 mảnh: 掃除用具 + [2. として] (gắn trực tiếp danh từ chỉ vai trò GP-N3-049) "
            "-> [1. 使う] (động từ thể từ điển) -> [★ 4. こと] -> [3. に] + した (kết thúc mẫu Vることにした GP-N4-13). "
            "Câu hoàn chỉnh: 古くなった歯ブラシを掃除用具 として 使う ★こと に した。"
        ),
        "pedagogical_takeaway_vi": "Thấy danh từ công cụ ngay trước 4 ô trống và chữ した ở tận cuối -> tách thành hai khớp cố định [N + として] ở đầu và [Vる + こと + に + した] ở cuối.",
        "option_grammar_notes": [
            "使う (Slot 2): Động từ thể từ điển theo sau 掃除用具として và đứng trước こと.",
            "として (Slot 1): Gắn trực tiếp vào danh từ 掃除用具 phía trước ('dùng làm dụng cụ vệ sinh').",
            "に (Slot 4): Đi kèm với した ở cuối câu hoàn chỉnh để tạo thành ことにした.",
            "こと (Slot 3 ★): ĐÚNG. Danh từ hóa động từ 使う, nằm giữa 使う và にした.",
        ],
    },
    # ID=26
    "c77459afffa2872f2bf3de83593e0dbe887551b3125e92b670b81a90ea1b1062": {
        "links": [
            {"grammar_code": "GP-N3-031", "role": "primary_target", "note_vi": "～というわけではなく: không phải cứ là cái gì cũng được mà..."},
            {"grammar_code": "GP-N3-047", "role": "primary_target", "note_vi": "N (日本文化) + に関する + こと: những điều liên quan tới văn hóa Nhật Bản."},
            {"grammar_code": "GP-N5-17", "role": "sentence_structure", "note_vi": "ことだけです giới hạn phạm vi ở cuối câu ('chỉ là chuyện liên quan tới... thôi')."},
            {"grammar_code": "GP-N5-06", "role": "distractor_trap", "note_vi": "Bẫy chia nhầm thứ tự danh từ 日本文化 với に関する hay ghép いいという sau わけではなく."},
        ],
        "structure_parse_vi": (
            "Chuỗi lắp ghép 4 mảnh: 何でも + [4. いいという] -> [1. わけではなく] (kết nối phủ định một phần ở dạng て: không hẳn là cái gì cũng được mà...) "
            "-> [★ 3. 日本文化] -> [2. に関する] + ことだけです (định ngữ chỉ phạm vi: liên quan đến văn hóa Nhật). "
            "Câu hoàn chỉnh: スピーチのテーマは何でも いいという わけではなく ★日本文化 に関する ことだけです。"
        ),
        "pedagogical_takeaway_vi": "Khi cuối câu là [～ことだけです], mảnh đứng ngay trước nó thường là động từ/liên ngữ định ngữ dạng [～に関する].",
        "option_grammar_notes": [
            "わけではなく (Slot 2): Đi ngay sau いいという để hoàn tất mệnh đề nhượng bộ 'không phải là gì cũng được mà...'.",
            "に関する (Slot 4): Cụm định ngữ bổ nghĩa trực tiếp cho ことだけです ở sau dấu trống.",
            "日本文化 (Slot 3 ★): ĐÚNG. Danh từ đứng ngay trước に関する (日本文化に関する = liên quan đến văn hóa Nhật).",
            "いいという (Slot 1): Khớp với đại từ nghi vấn 何でも phía trước (何でもいいという = nói là cái gì cũng được).",
        ],
    },
    # ID=27
    "56004b7c2ef4cb83dc9097a03bd634718bb5723013ca53872081959d590a2323": {
        "links": [
            {"grammar_code": "GP-N4-11", "role": "primary_target", "note_vi": "Thể khả năng 読める + ように: mục đích 'để có thể đọc được' khi cần thiết."},
            {"grammar_code": "GP-N4-01", "role": "sentence_structure", "note_vi": "Chia thể khả năng nhóm 1 読む -> 読める (chú ý không gắn thêm られる!)."},
            {"grammar_code": "GP-N4-12", "role": "distractor_trap", "note_vi": "Bẫy 読むために / 読めるために: ために chỉ đi với Vる ý chí, CẤM ghép với thể khả năng 読める và sai sắc thái 'lúc cần thiết'."},
            {"grammar_code": "GP-N4-05", "role": "sentence_structure", "note_vi": "Vế chính しまっておいてください (Vておく: hãy cất giữ sẵn) khớp hoàn hảo với mục đích phòng khi cần."},
        ],
        "structure_parse_vi": (
            "Mạch văn Đục lỗ (PID=1 この薬の使い方): Sau phần hướng dẫn bôi, đoạn nhắc giữ tờ hướng dẫn: "
            "[また、必要なときに] (trạng ngữ thời điểm không cố định) + [読めるように] (mục đích khả năng GP-N4-11) "
            "-> [大切にしまっておいてください] (hãy cất sẵn cẩn thận GP-N4-05)."
        ),
        "pedagogical_takeaway_vi": "Nhớ luật sắt N4-N3: Thể khả năng (読める) CHỈ đi với ように, TUYỆT ĐỐI KHÔNG bao giờ đi với ために.",
        "option_grammar_notes": [
            "読むために: Sai sắc thái vì hành động 'đọc khi cần' là trạng thái dự phòng chứ không phải mục đích trực tiếp đang làm ngay.",
            "読めるために: SAI ngữ pháp cứng — ために không bao giờ gắn sau động từ thể khả năng.",
            "読むように: Động từ ý chí 読む đứng trần không có thể khả năng sẽ biến thành câu mệnh lệnh/mong muốn thay vì 'để có thể đọc'.",
            "読めるように: ĐÚNG. Thể khả năng 読める + ように = để có thể đọc được lúc cần thiết.",
        ],
    },
    # ID=28
    "511c8a3f7edc55458d9b048ceff1a4b3889d78194cc0a3cd372c346ec720fee8": {
        "links": [
            {"grammar_code": "GP-N4-10", "role": "primary_target", "note_vi": "Vます + やすい + く + なっています: trở nên dễ thoa (tính chất sản phẩm)."},
            {"grammar_code": "GP-N5-05", "role": "primary_target", "note_vi": "Quy tắc chia tính từ đuôi い trước なる: bỏ い thêm く (つけやすい -> つけやすく)."},
            {"grammar_code": "GP-N4-03", "role": "distractor_trap", "note_vi": "Bẫy つけられやすく: thừa thể bị động られ khi câu giải thích thiết kế công dụng của đầu mút xốp."},
            {"grammar_code": "GP-N4-11", "role": "distractor_trap", "note_vi": "Bẫy つけるように: không ghép trực tiếp つけるようなっています để tả sự dễ dùng của thiết kế."},
            {"grammar_code": "GP-N5-13", "role": "sentence_structure", "note_vi": "Mệnh đề nguyên nhân ~ので giải thích lý do dẫn tới tính tiện dụng dễ bôi."},
        ],
        "structure_parse_vi": (
            "Mạch văn Đục lỗ (PID=1 この薬の使い方): Đoạn 2 chuyển sang mô tả cấu tạo lọ thuốc: "
            "[容器の先にスポンジがついている + ので] (vì đầu lọ có gắn miếng mút - tự động từ + ている + ので) "
            "-> [つけやすくなっています] (được thiết kế để trở nên dễ bôi - つけやすい chia く + なる GP-N5-05)."
        ),
        "pedagogical_takeaway_vi": "Mọi đuôi ～やすい / ～にくい đều là tính từ đuôi い -> khi đứng trước なる / する luôn biến thành ～やすく / ～にくく.",
        "option_grammar_notes": [
            "つけやすく: ĐÚNG. Vます (つけ) + やすい bỏ い thêm く -> つけやすくなっています.",
            "つけやすいに: SAI quy tắc chia — tính từ đuôi い không dùng に trước なる.",
            "つけるように: Không diễn đạt tính chất 'dễ bôi hơn nhờ miếng mút' trước なっています.",
            "つけられやすく: Dư thừa hình thái bị động trước やすい.",
        ],
    },
    # ID=29
    "a4799c436f6a2b64e4f4f97221655af978cd3687b8a337afe9fe6ad1fe7eb2a8": {
        "links": [
            {"grammar_code": "GP-N3-115", "role": "primary_target", "note_vi": "Liên kết mở đoạn với まず、～しないでください (chủ đề cảnh báo chú ý dùng thuốc)."},
            {"grammar_code": "GP-N5-10", "role": "sentence_structure", "note_vi": "Câu cấm đoán ～ないでください liệt kê ngay sau câu mở đoạn."},
            {"grammar_code": "GP-N5-06", "role": "sentence_structure", "note_vi": "Định ngữ động từ bổ nghĩa cho danh từ 点 (注意する点)."},
            {"grammar_code": "GP-N5-05", "role": "distractor_trap", "note_vi": "Bẫy 悪い点 / すごい点 / いい点: sai logic văn bản hướng dẫn an toàn y khoa dù chia đúng tính từ bổ nghĩa danh từ."},
        ],
        "structure_parse_vi": (
            "Mạch văn Đục lỗ (PID=1 この薬の使い方): Sau phần cách bôi ở đoạn trước, đoạn 3 chuyển sang loạt điều cấm kỵ nối bằng まず... それから... (~しないでください). "
            "Do đó câu chủ đề mở đoạn [3] phải khái quát được tính chất cảnh báo: [注意する点があります]."
        ),
        "pedagogical_takeaway_vi": "Trong 問題3, câu đứng đầu đoạn trống [3] luôn phải khái quát đúng mạch các câu liệt kê ngay phía sau (thấy まず～しないで -> 注意する点).",
        "option_grammar_notes": [
            "注意する点があります: ĐÚNG. Mở đầu chuẩn xác cho loạt chỉ dẫn phòng tránh まず～しないでください.",
            "いい点があります: 'Có điểm tốt', mâu thuẫn hoàn toàn với chuỗi điều cấm sử dụng ở vết thương/mắt.",
            "悪い点があります: Hướng dẫn sản phẩm không tự giới thiệu 'có nhược điểm' để liệt kê cảnh báo dùng thuốc.",
            "すごい点があります: Văn phong cảm thán 'điểm tuyệt vời', lạc tông hoàn toàn so với hướng dẫn y tế.",
        ],
    },
    # ID=49
    "538e2667615c2991482196e217d9ec158df3e9c5f143dd31e8f2545250145c4d": {
        "links": [
            {"grammar_code": "GP-N3-115", "role": "primary_target", "note_vi": "Liên từ diễn giải tương đương つまり ('tức là, nói cách khác là'), phân biệt với bẫy なぜなら."},
            {"grammar_code": "GP-N5-13", "role": "distractor_trap", "note_vi": "Bẫy それで / ですから: biểu thị quan hệ nguyên nhân -> kết quả, không dùng giải thích từ đồng nghĩa."},
            {"grammar_code": "GP-N5-15", "role": "distractor_trap", "note_vi": "Bẫy liên từ giải thích nguyên nhân なぜなら: dùng nêu lý do cho vế trước, sai quan hệ đồng nhất."},
        ],
        "structure_parse_vi": (
            "[今日はおおみそか] (danh từ văn hóa cụ thể) -> liên từ giải nghĩa [つまり] -> [一年の最後の日です] (cụm từ giải thích tương đương cho khái niệm trên)."
        ),
        "pedagogical_takeaway_vi": "Khi vế 1 đưa từ vựng/khái niệm chuyên biệt (A) và vế 2 giải nghĩa tương đương (B) cùng quy chiếu 1 sự vật -> chọn つまり.",
        "option_grammar_notes": [
            "それで: Liên từ chỉ kết quả kéo theo ('vì thế mà'), sai vì 'đêm giao thừa' không sinh ra 'ngày cuối năm'.",
            "つまり: ĐÚNG. Diễn giải lại khái niệm 'おおみそか' thành '一年の最後の日'.",
            "なぜなら: Liên từ giải thích lý do ('bởi vì là...'), đặt ở đây làm gãy quan hệ đồng nhất.",
            "ですから: Liên từ nhân quả lịch sự ('vì vậy nên'), không dùng giải nghĩa từ vựng.",
        ],
    },
    # ID=50
    "cfb53f21622cb319524b273e6e055a5e4ebe13f18cf0e89e2aa7720ab3f8e51b": {
        "links": [
            {"grammar_code": "GP-N4-11", "role": "primary_target", "note_vi": "Vない + ように + 気をつける: chú ý để không bị cảm lạnh."},
            {"grammar_code": "GP-N4-12", "role": "distractor_trap", "note_vi": "Bẫy ために / ための: ために không đi sau Vない và không dùng cho động từ không ý chí như かぜをひかない."},
            {"grammar_code": "GP-N4-20", "role": "distractor_trap", "note_vi": "Bẫy ようで: nghĩa là 'có vẻ như là', sai cấu trúc trước 気をつけてください."},
            {"grammar_code": "GP-N4-07", "role": "sentence_structure", "note_vi": "Mệnh đề nguyên nhân 寒くなってきたので sử dụng てくる chỉ biến đổi hướng tới hiện tại."},
        ],
        "structure_parse_vi": (
            "Nguyên nhân biến đổi thời tiết [寒くなってきた + ので] (GP-N4-07 + GP-N5-13) -> mục tiêu phòng ngừa trạng thái không ý chí "
            "[かぜをひかない + ように] (GP-N4-11) + yêu cầu cẩn trọng [気をつけてください]."
        ),
        "pedagogical_takeaway_vi": "Động từ có phủ định Vない hoặc không ý chí (không bị ốm, không quên, không muộn) + 気をつける -> bắt buộc dùng ように.",
        "option_grammar_notes": [
            "ために: Sai quy tắc — ために chỉ đi với động từ ý chí khẳng định Vる hoặc Danh từ + の.",
            "ための: Dạng định ngữ đứng trước danh từ, không đứng trực tiếp trước động từ 気をつけてください.",
            "ように: ĐÚNG. かぜをひかないように気をつけてください (chú ý để không bị cảm).",
            "ようで: Dạng nối của ようだ ('hình như'), không biểu đạt mục đích phòng ngừa.",
        ],
    },
    # ID=51
    "52675942dcb9be4b289acda4862855938650bb57748ba70b9230e7a9dc6161c4": {
        "links": [
            {"grammar_code": "GP-N3-082", "role": "primary_target", "note_vi": "Vます + たて + の + N: cơm vừa mới nấu xong nóng hổi (炊きたてのごはん)."},
            {"grammar_code": "GP-N3-081", "role": "distractor_trap", "note_vi": "Bẫy 炊きかけ: đang nấu dở dang chưa chín, không thể ăn ngay."},
            {"grammar_code": "GP-N3-073", "role": "distractor_trap", "note_vi": "Bẫy 炊きっぱなし: cứ cắm điện/để nguyên cơm bỏ mặc không dọn (mang nghĩa chê trách)."},
            {"grammar_code": "GP-N3-061", "role": "distractor_trap", "note_vi": "Bẫy 炊いたとたん: vừa nấu xong thì đột ngột có biến cố, không đi trực tiếp với のごはん."},
            {"grammar_code": "GP-N4-18", "role": "sentence_structure", "note_vi": "Cụm cho nhận 食べてもらいたい (muốn gia đình ăn cho mình) trích dẫn qua と言っている."},
        ],
        "structure_parse_vi": (
            "[母はいつも]、[家族には + (炊きたて + の + ごはん)を + 食べてもらいたい] (định ngữ Vますたて + の + N làm tân ngữ cho 食べてもらいたい) "
            "-> trích dẫn thói quen [と言っている]."
        ),
        "pedagogical_takeaway_vi": "Đồ ăn tươi mới/nóng hổi vừa nấu nướng ra lò (ごはん, パン, コーヒー) luôn ghép Vます + たて + の + N.",
        "option_grammar_notes": [
            "炊きかけ: Đang nấu dở chưa chín, sai nghĩa trong bữa ăn.",
            "炊きたて: ĐÚNG. Vます + たて + の + ごはん = cơm vừa mới thổi chín nóng hổi.",
            "炊きっぱなし: Để nguyên trạng thái bỏ mặc thiếu trách nhiệm, sắc thái chê trách.",
            "炊いたとたん: Mẫu câu sự cố tức thì ở mệnh đề, không đứng trước trợ từ の để bổ nghĩa danh từ.",
        ],
    },
    # ID=52
    "6eaa62555fdbe04e036363c8f18dbdf04773b0dfc029fdcc4e1ef7e6d8ce566b": {
        "links": [
            {"grammar_code": "GP-N3-042", "role": "primary_target", "note_vi": "N + こそ: chính cuốn sách ảnh này chứ không phải cuốn nào khác."},
            {"grammar_code": "GP-N5-17", "role": "distractor_trap", "note_vi": "Bẫy しか / だけ: しか bắt buộc đi với phủ định ~ない; だけ nghĩa 'chỉ có', yếu sắc thái khẳng định đích danh."},
            {"grammar_code": "GP-N3-053", "role": "distractor_trap", "note_vi": "Bẫy ばかり: 'toàn là', không hợp với danh từ số ít この写真集 và định ngữ ずっと探していたものだ."},
            {"grammar_code": "GP-N5-06", "role": "sentence_structure", "note_vi": "Mệnh đề định ngữ [ぼくがずっと探していた] (GP-N5-08 tiếp diễn quá khứ) bổ nghĩa cho [ものだ]."},
        ],
        "structure_parse_vi": (
            "[この写真集 + こそ] (chủ ngữ nhấn mạnh tuyệt đối GP-N3-042) -> phần vị ngữ danh từ [ぼくがずっと探していた + ものだ] (thứ mà tôi luôn tìm bấy lâu)."
        ),
        "pedagogical_takeaway_vi": "Khung khẳng định tuyệt đối danh từ duy nhất vừa tìm ra hoặc đề cao giá trị dùng [N + こそ (+ ずっと探していたものだ)].",
        "option_grammar_notes": [
            "こそ: ĐÚNG. Trợ từ nhấn mạnh đích danh ('chính cuốn này').",
            "しか: Bắt buộc đi với vị ngữ phủ định (~ではない), không đi với ものだ.",
            "だけ: Giới hạn số lượng 'chỉ có', không mang lực nhấn mạnh nhận diện đích danh.",
            "ばかり: Biểu thị 'toàn là / chỉ toàn' số lượng nhiều hoặc lặp lại, sai nghĩa với 1 cuốn sách.",
        ],
    },
    # ID=53
    "cc17dc454ffebbcbe5fde5ea99a7584fbed869c72e381c7a4f0be68a7a6dc2af": {
        "links": [
            {"grammar_code": "GP-N3-013", "role": "primary_target", "note_vi": "Mệnh đề thường + のに対して: đối lập tương phản giữa quán bên này (rẻ) và quán bên kia (nhiều món)."},
            {"grammar_code": "GP-N3-090", "role": "distractor_trap", "note_vi": "Bẫy において: chỉ địa điểm/phạm vi trang trọng ('tại...'), không gắn sau tính từ + の để tương phản."},
            {"grammar_code": "GP-N3-047", "role": "distractor_trap", "note_vi": "Bẫy に関して: nghĩa là 'liên quan đến', sai logic đối chiếu hai quán ăn."},
            {"grammar_code": "GP-N3-096", "role": "sentence_structure", "note_vi": "Đuôi câu 量が多い + ことで評判だ (nổi tiếng nhờ/vì đặc điểm lượng nhiều - gần với GP-N3-096)."},
        ],
        "structure_parse_vi": (
            "Vế đối chiếu 1 [こちらの店が安い + のに対して] (trong khi quán bên này giá rẻ thì ngược lại - GP-N3-013) "
            "-> vế đối chiếu 2 [あちらの店は量が多いことで評判だ] (quán kia nổi tiếng nhờ khẩu phần nhiều)."
        ),
        "pedagogical_takeaway_vi": "Thấy 2 vế đối xứng cặp [こちら...はA] vs [あちら...はB] -> kiểm tra ngay cấu trúc tương phản ～のに対して.",
        "option_grammar_notes": [
            "において: Dùng cho N + において ('tại/trong lĩnh vực N'), không gắn sau mệnh đề の để tương phản.",
            "において (trùng lặp từ đề gốc): Sai ngữ nghĩa và cách kết hợp tương tự phương án 1.",
            "に対して: ĐÚNG. Tính từ 安い + のに対して = trái ngược với việc giá rẻ.",
            "に関して: Nghĩa là 'liên quan đến', không đối chiếu hai vế tương phản.",
        ],
    },
    # ID=54
    "00b28a3920e98cb6ffef0c4b126bfc2f7e82e3a32425db1189aebcd4dcf6b523": {
        "links": [
            {"grammar_code": "GP-N3-091", "role": "primary_target", "note_vi": "N + からいうと: xét về tiêu chí độ tiện lợi vị trí thì khách sạn A đáng gợi ý hơn."},
            {"grammar_code": "GP-N3-117", "role": "distractor_trap", "note_vi": "Bẫy と思えば: gắn sau mệnh đề để diễn tả thay đổi bất ngờ ('vừa mới tưởng...')."},
            {"grammar_code": "GP-N3-025", "role": "distractor_trap", "note_vi": "Bẫy によれば: trích dẫn nguồn tin truyền đạt (đòi hỏi đuôi そうだ / ということだ)."},
            {"grammar_code": "GP-N3-013", "role": "distractor_trap", "note_vi": "Bẫy に対して: thái độ đối với đối tượng hoặc tương phản hai vế, không chọn một tiêu chí so sánh."},
            {"grammar_code": "GP-N5-04", "role": "sentence_structure", "note_vi": "Câu kết sử dụng mẫu so sánh N + のほうが + おすすめです (GP-N5-04)."},
        ],
        "structure_parse_vi": (
            "Nhượng bộ mở [どちらもいいホテルですが] -> chọn tiêu chí đánh giá [場所の便利さ + からいうと] (xét về mặt tiện lợi địa điểm - GP-N3-091) "
            "-> đưa ra gợi ý [Aホテルのほうがおすすめです]."
        ),
        "pedagogical_takeaway_vi": "Thấy danh từ tiêu chí trừu tượng (便利さ / 値段 / 結果 / 見た目) + [___] + đánh giá cá nhân (~のほうが / ~ほうがいい) -> chọn からいうと / からすると.",
        "option_grammar_notes": [
            "と思えば: Gắn sau mệnh đề thể thường diễn tả chuyển biến bất ngờ, không gắn danh từ tiêu chí.",
            "によれば: Dùng dẫn nguồn tin khách quan (phải kết thúc câu bằng そうだ/ということだ), không hợp おすすめです.",
            "に対して: Chỉ hướng đối tượng hoặc đối lập, không đưa ra tiêu chí lập luận.",
            "からいうと: ĐÚNG. 便利さからいうと = xét từ góc độ độ tiện lợi.",
        ],
    },
    # ID=55
    "8a0024018331e84c82723aea0df5419fc5585eebd9d385da47731e7aae4078d5": {
        "links": [
            {"grammar_code": "GP-N3-053", "role": "primary_target", "note_vi": "Vて + ばかりいる: ngày nào cũng chỉ toàn ngủ (lặp lại mang sắc thái than phiền)."},
            {"grammar_code": "GP-N3-088", "role": "distractor_trap", "note_vi": "Bẫy cực độc だらけだ: だらけ CHỈ gắn sau DANH TỪ (例: ほこりだらけ), tuyệt đối không gắn sau thể て (寝て)."},
            {"grammar_code": "GP-N3-108", "role": "distractor_trap", "note_vi": "Bẫy のみだ: gắn sau Vる hoặc Danh từ, không gắn sau thể て (寝て)."},
            {"grammar_code": "GP-N3-078", "role": "distractor_trap", "note_vi": "Bẫy 続けている: liên tục không nghỉ gắn sau gốc Vます (寝続けている), không gắn sau thể て."},
            {"grammar_code": "GP-N5-05", "role": "sentence_structure", "note_vi": "Biến đổi thời điểm 夏休みになって (đã bước sang kỳ nghỉ hè - Vて + なる)."},
        ],
        "structure_parse_vi": (
            "Mốc bắt đầu [夏休みになって] + tần suất [毎日] + hành động lặp lại dạng thể て [寝て + ばかりいる] (cả ngày chỉ toàn ngủ - GP-N3-053)."
        ),
        "pedagogical_takeaway_vi": "Nhìn hình thái động từ ngay trước chỗ trống là thể て (寝て) -> loại thẳng cánh だらけ (cần N), のみ (cần Vる), 続ける (cần Vます).",
        "option_grammar_notes": [
            "のみだ: Gắn sau Vる hoặc N, sai kết hợp sau thể て (寝て).",
            "だらけだ: Bẫy kinh điển — だらけ chỉ gắn sau Danh từ (ごみだらけ), cấm gắn sau Vて.",
            "ばかりいる: ĐÚNG. Vて (寝て) + ばかりいる = suốt ngày chỉ toàn ngủ.",
            "続けている: Đòi hỏi Vます (寝続けている), không nối sau thể て (寝て).",
        ],
    },
    # ID=56
    "ed6caa613e142ec7b9a68815d55c2117287c42c41b7dcad6abc9628c4e604841": {
        "links": [
            {"grammar_code": "GP-N3-090", "role": "primary_target", "note_vi": "N1 (機内) + における + N2 (携帯電話の使用): nối 2 danh từ chỉ địa điểm/phạm vi trang trọng."},
            {"grammar_code": "GP-N4-03", "role": "sentence_structure", "note_vi": "Bị động xã hội 禁止されています (việc sử dụng bị nghiêm cấm trên máy bay)."},
            {"grammar_code": "GP-N5-02", "role": "distractor_trap", "note_vi": "Bẫy đặt 携帯電話の trước における làm đảo chủ thể địa điểm 'trên máy bay'."},
        ],
        "structure_parse_vi": (
            "Chuỗi lắp ghép 4 mảnh: 機内 (địa điểm) -> [3. における] (giới từ nối danh từ định ngữ GP-N3-090) "
            "-> [4. 携帯電話の] (N bổ ngữ) -> [★ 2. 使用は] (chủ ngữ với は) -> [1. 禁止] + されています (bị động). "
            "Câu hoàn chỉnh: 機内 における 携帯電話の ★使用は 禁止 されています。"
        ),
        "pedagogical_takeaway_vi": "Gặp における (dạng định ngữ của において): luôn kẹp giữa [N địa điểm/lĩnh vực] và [N sự việc chịu tác động].",
        "option_grammar_notes": [
            "禁止 (Slot 4): Danh động từ ghép với されています tạo bị động 禁止されています.",
            "使用は (Slot 3 ★): ĐÚNG. Trung tâm của cụm danh từ 携帯電話の使用 + trợ từ chủ đề は trước 禁止されています.",
            "における (Slot 1): Gắn ngay sau danh từ địa điểm 機内 ('tại trong khoang máy bay').",
            "携帯電話の (Slot 2): Bổ nghĩa sở hữu cho danh từ 使用 đứng ngay sau.",
        ],
    },
    # ID=57
    "593840abdd57403cee62f130a43718cf9d6c781938b16b07517fff0d55be568f": {
        "links": [
            {"grammar_code": "GP-N3-017", "role": "primary_target", "note_vi": "N1 (先輩) + のかわりに: thay thế cho người đàn anh bị chấn thương."},
            {"grammar_code": "GP-N3-049", "role": "primary_target", "note_vi": "N2 (チームの代表) + として: với tư cách là đại diện đội tuyển."},
            {"grammar_code": "GP-N4-14", "role": "sentence_structure", "note_vi": "Kết câu 試合に出ることになった (được quyết định/sắp xếp sẽ ra sân thi đấu)."},
            {"grammar_code": "GP-N5-02", "role": "distractor_trap", "note_vi": "Bẫy đổi chỗ に và として hoặc tách rời cặp のかわり + に."},
        ],
        "structure_parse_vi": (
            "Chuỗi lắp ghép 4 mảnh: けがをした先輩 + [3. のかわり] + [1. に] (cụm GP-N3-017: thay cho đàn anh) "
            "-> [★ 4. チームの代表] + [2. として] (cụm GP-N3-049: với tư cách đại diện đội) + 試合に出ることになった. "
            "Câu hoàn chỉnh: ...先輩 のかわり に ★チームの代表 として 試合に出ることになった。"
        ),
        "pedagogical_takeaway_vi": "Trong câu có mảnh のかわり và mảnh に đơn lẻ -> ghép chúng thành のかわりに ở đầu trước, rồi đặt vai trò mới [N + として] ở ngay sau.",
        "option_grammar_notes": [
            "に (Slot 2): Đi liền sau のかわり để tạo thành cấu trúc のかわりに ('thay cho...').",
            "として (Slot 4): Đứng sau チームの代表 và ngay trước động từ 試合に出る ('với tư cách là...').",
            "のかわり (Slot 1): Nối trực tiếp sau danh từ 先輩 ('thay thế cho đàn anh').",
            "チームの代表 (Slot 3 ★): ĐÚNG. Danh từ chỉ tư cách đứng giữa のかわりに và として.",
        ],
    },
    # ID=58
    "b8b0382d8e37125873d1f50b933190c8b6b7123562a5b99d06c97eb15077d4cd": {
        "links": [
            {"grammar_code": "GP-N3-023", "role": "primary_target", "note_vi": "N (やる気) + さえ + あれば: chỉ cần có tinh thần hăng hái là đủ."},
            {"grammar_code": "GP-N3-092", "role": "primary_target", "note_vi": "N (経験) + を問わず: bất kể kinh nghiệm, không đòi hỏi kinh nghiệm."},
            {"grammar_code": "GP-N4-01", "role": "sentence_structure", "note_vi": "Kết câu khả năng 応募することができます (có thể ứng tuyển)."},
            {"grammar_code": "GP-N4-16", "role": "distractor_trap", "note_vi": "Bẫy đặt 経験 trước さえあれば (mất logic tuyển dụng vì đề yêu cầu bất kể kinh nghiệm, chỉ cần nhiệt huyết)."},
        ],
        "structure_parse_vi": (
            "Chuỗi lắp ghép 4 mảnh: やる気 + [1. さえ] + [3. あれば] (điều kiện tối thiểu GP-N3-023: chỉ cần có nhiệt huyết) "
            "-> [★ 2. 経験] + [4. を問わず] (miễn trừ điều kiện GP-N3-092: bất kể kinh nghiệm) + 応募することができます. "
            "Câu hoàn chỉnh: ...やる気 さえ あれば ★経験 を問わず 応募することができます。"
        ),
        "pedagogical_takeaway_vi": "Gặp cặp [さえ] + [あれば] và [を問わず] -> さえあれば là cặp điều kiện tối thiểu, và 経験 luôn đi trước を問わず.",
        "option_grammar_notes": [
            "さえ (Slot 1): Gắn sau やる気 để mở cặp điều kiện tối thiểu さえ～ば.",
            "経験 (Slot 3 ★): ĐÚNG. Danh từ làm đối tượng cho cụm cố định 経験 + を問わず ('bất kể kinh nghiệm').",
            "あれば (Slot 2): Động từ điều kiện hoàn tất cụm やる気さえあれば.",
            "を問わず (Slot 4): Nối danh từ 経験 vào động từ chính 応募することができます.",
        ],
    },
    # ID=59
    "0cecb9003fc4fe84a3a1908c122b98efb17ef80fbbe284481f0d2ddeac10c024": {
        "links": [
            {"grammar_code": "GP-N3-091", "role": "primary_target", "note_vi": "N (女性の平均) + からすると: xét từ mức trung bình của phụ nữ."},
            {"grammar_code": "GP-N3-031", "role": "primary_target", "note_vi": "Cặp hô ứng 決して + 小さい + わけではない ('hoàn toàn không phải là nhỏ')."},
            {"grammar_code": "GP-N5-05", "role": "sentence_structure", "note_vi": "Tính từ đuôi い (小さい) giữ nguyên bổ nghĩa trực tiếp cho danh từ わけ."},
            {"grammar_code": "GP-N5-15", "role": "distractor_trap", "note_vi": "Bẫy đặt わけ sau からすると hoặc tách phó từ 決して khỏi tính từ 小さい."},
        ],
        "structure_parse_vi": (
            "Chuỗi lắp ghép 4 mảnh: 女性の平均 + [4. からすると] (góc độ đối chiếu GP-N3-091) "
            "-> [2. 決して] (phó từ nhấn mạnh phủ định đứng đầu mệnh đề sau) -> [★ 3. 小さい] (tính từ bổ cho わけ) -> [1. わけ] + ではない (GP-N3-031). "
            "Câu hoàn chỉnh: ...女性の平均 からすると 決して ★小さい わけ ではない。"
        ),
        "pedagogical_takeaway_vi": "Phó từ 決して luôn đứng đầu mệnh đề phủ định (sau からすると) để kéo xuống cụm [Tính từ + わけではない] ở cuối.",
        "option_grammar_notes": [
            "わけ (Slot 4): Đứng ngay trước ではない ngoài dấu trống để tạo thành mẫu わけではない.",
            "決して (Slot 2): Phó từ nhấn mạnh phủ định, đứng sau からすると và trước tính từ 小さい.",
            "小さい (Slot 3 ★): ĐÚNG. Tính từ bị phó từ 決して bổ nghĩa, đứng trực tiếp trước わけではない.",
            "からすると (Slot 1): Gắn sau danh từ tiêu chuẩn 女性の平均 ('xét từ mức trung bình nữ giới').",
        ],
    },
    # ID=60
    "6c36bf512dc851db571738a812c8c729b6d95b19b15a0f32bec9e8a868da6b0e": {
        "links": [
            {"grammar_code": "GP-N3-054", "role": "primary_target", "note_vi": "N1 ばかりでなく N2 も: không chỉ piano mà cả violin cũng chơi được."},
            {"grammar_code": "GP-N4-01", "role": "sentence_structure", "note_vi": "Động từ khả năng ひける (có thể chơi đàn) + cảm thán なんて、すごいですね (GP-N3-046)."},
            {"grammar_code": "GP-N3-053", "role": "distractor_trap", "note_vi": "Bẫy nhầm với ばかり (chỉ toàn) hoặc đặt も vào trước バイオリン."},
        ],
        "structure_parse_vi": (
            "Chuỗi lắp ghép 4 mảnh: ピアノ (N1) -> [3. ばかり] -> [2. でなく] (liên kết GP-N3-054: không chỉ N1) "
            "-> [★ 4. バイオリン] (N2) -> [1. も] (trợ từ mở rộng đi trước động từ ひける). "
            "Câu hoàn chỉnh: ピアノ ばかり でなく ★バイオリン も ひけるなんて、すごいですね。"
        ),
        "pedagogical_takeaway_vi": "Khung cố định liệt kê tăng tiến song hành 2 danh từ: [N1] + [ばかり] + [でなく] + [N2] + [も].",
        "option_grammar_notes": [
            "も (Slot 4): Trợ từ đi sau danh từ N2 (バイオリン) để nối vào động từ ひける.",
            "でなく (Slot 2): Nối sau ばかり tạo cụm liên kết ばかりでなく.",
            "ばかり (Slot 1): Nối trực tiếp sau danh từ N1 (ピアノ) ở đầu dãy trống.",
            "バイオリン (Slot 3 ★): ĐÚNG. Danh từ N2 được giới thiệu thêm sau ばかりでなく và trước も.",
        ],
    },
    # ID=61
    "ea141497f0fb36fee19d8540f3546e858e041d0e5e126a763b9018403833e0cc": {
        "links": [
            {"grammar_code": "GP-N3-089", "role": "primary_target", "note_vi": "Aい(bỏ い) + っぽい: 黒っぽい = hơi đen, ngả màu đen."},
            {"grammar_code": "GP-N3-116", "role": "distractor_trap", "note_vi": "Bẫy 的な: hậu tố 的 chỉ gắn vào Danh từ Hán-Nhật 2 chữ (国際的), cấm gắn vào gốc tính từ thuần Nhật 黒."},
            {"grammar_code": "GP-N4-20", "role": "distractor_trap", "note_vi": "Bẫy らしい / みたいな: gắn vào Danh từ nguyên dạng hoặc mệnh đề, không gắn trực tiếp vào gốc bỏ い của tính từ (黒)."},
            {"grammar_code": "GP-N3-052", "role": "sentence_structure", "note_vi": "Câu chứa cấu trúc ví von ような形に見える (trông giống hình dáng như thể...)."},
        ],
        "structure_parse_vi": (
            "Mạch văn Đục lỗ (PID=5 月のウサギ): Câu mở giới thiệu văn hóa Nhật về thỏ trên mặt trăng, câu [1] giải thích cơ sở thị giác: "
            "[これは、月にある + (黒っぽい + 模様) + が] (chủ thể là hoa văn ngả đen - GP-N3-089) "
            "-> [ウサギがもちをついているような形に + 見えるからです] (vì trông giống dáng vẻ thỏ đang giã bánh - GP-N3-052)."
        ),
        "pedagogical_takeaway_vi": "Khi chữ đứng ngay trước chỗ trống là gốc tính từ màu sắc mất đuôi い (黒 / 白 / 赤) -> 100% chọn っぽい (黒っぽい).",
        "option_grammar_notes": [
            "的な: Chỉ gắn sau Danh từ (đa số từ Hán-Nhật), sai ngữ pháp khi gắn trực tiếp sau gốc tính từ 黒.",
            "っぽい: ĐÚNG. Aい(bỏ い) + っぽい -> 黒っぽい = ngả màu đen / hơi đen.",
            "らしい: Chỉ gắn sau danh từ hoàn chỉnh hoặc thể thông thường, không gắn gốc tính từ bỏ い (黒).",
            "みたいな: Phải gắn sau danh từ hoàn chỉnh hoặc mệnh đề thể thông thường, không dùng *黒みたいな.",
        ],
    },
    # ID=62
    "9525b5e95ed5c52b5e03c5ead2b5264e217bd57ed4c8e5267ebe9f49c9778560": {
        "links": [
            {"grammar_code": "GP-N3-115", "role": "primary_target", "note_vi": "Liên từ nhân quả trực tiếp そのため ('vì vậy, do đó')."},
            {"grammar_code": "GP-N3-105", "role": "distractor_trap", "note_vi": "Bẫy そのわりに: nghĩa tương phản trái kỳ vọng ('tuy vậy mà lại'), ngược logic khoa học trong đoạn."},
            {"grammar_code": "GP-N5-15", "role": "distractor_trap", "note_vi": "Bẫy それでも / それから: それでも mang nghĩa nhượng bộ ('dù vậy vẫn'); それから chỉ trình tự thời gian/liệt kê thêm."},
            {"grammar_code": "GP-N3-024", "role": "sentence_structure", "note_vi": "Cụm nhượng bộ どこから見ても (nhìn từ bất cứ đâu cũng đều giống nhau - nghi vấn từ + ても)."},
        ],
        "structure_parse_vi": (
            "Mạch văn Đục lỗ (PID=5 月のウサギ): Câu trước nêu nguyên lý thiên văn [月は、いつも地球に同じ面を向けています]. "
            "Chỗ trống [2] dùng liên từ nhân quả [そのため] (do đó) để suy ra hệ quả tất yếu ở câu sau [月の模様は地球のどこから見ても同じです]."
        ),
        "pedagogical_takeaway_vi": "Trong 問題3 điền liên từ đầu câu: so quan hệ giữa câu ngay trước và câu ngay sau — nếu câu trước là nguyên nhân khoa học trực tiếp dẫn ra câu sau thì chọn そのため.",
        "option_grammar_notes": [
            "そのため: ĐÚNG. Nối nguyên nhân (mặt trăng luôn quay một mặt về Trái Đất) sang hệ quả (nhìn từ đâu cũng giống nhau).",
            "それでも: Liên từ nhượng bộ ('dù vậy vẫn'), sai quan hệ nhân quả thuận chiều.",
            "それから: Liên từ nối tiếp thời gian hoặc liệt kê thêm ('sau đó / ngoài ra'), không thể hiện quan hệ nguyên nhân - kết quả.",
            "そのわりに: Liên từ đối lập trái kỳ vọng ('tuy vậy mà'), ngược với logic tất yếu của đoạn.",
        ],
    },
    # ID=63
    "033f2bdfe2994343c7e3a18f9261c688a05eb40f16ba43bae66e0bd3a7d612d6": {
        "links": [
            {"grammar_code": "GP-N3-031", "role": "primary_target", "note_vi": "けれども + みんな + ～わけではありません: không phải tất cả đều ví với con thỏ."},
            {"grammar_code": "GP-N3-029", "role": "distractor_trap", "note_vi": "Bẫy わけです: khẳng định kết luận tất yếu, mâu thuẫn với liên từ đối lập けれども và thực tế các vùng khác ví với cua/lừa."},
            {"grammar_code": "GP-N3-032", "role": "distractor_trap", "note_vi": "Bẫy わけにはいきません / わけにもいきません: chỉ sự không thể làm vì lý do đạo đức/quy tắc cá nhân, không khớp ngôi thứ 3 みんな."},
            {"grammar_code": "GP-N5-15", "role": "discourse_marker", "note_vi": "Liên từ đối lập けれども ở đầu câu báo hiệu bác bỏ nhận định tổng quát 'tất cả đều giống Nhật'."},
        ],
        "structure_parse_vi": (
            "Mạch văn Đục lỗ (PID=5 月のウサギ): Câu trước nói về Nhật Bản ví với thỏ; câu [3] chuyển hướng bằng [けれども] + lượng từ toàn thể [世界中の人がみんな... たとえている] "
            "-> kết câu bắt buộc là phủ định bộ phận [わけではありません] (GP-N3-031) để mở đường cho câu sau kể Nam Âu thấy hình cua, Nam Mỹ thấy con lừa."
        ),
        "pedagogical_takeaway_vi": "Cặp nhận diện kinh điển ở Đọc hiểu & Ngữ pháp N3: [けれども / しかし] + [みんな / すべて / いつも] + [～わけではありません].",
        "option_grammar_notes": [
            "わけです: Khẳng định tất yếu ('thế nên là...'), mâu thuẫn hoàn toàn với câu chuyển ý けれども và ví dụ Nam Âu/Nam Mỹ sau đó.",
            "わけではありません: ĐÚNG. Phủ định một phần ('không hẳn tất cả mọi người đều ví như vậy').",
            "わけにはいきません: Nghĩa là 'không thể làm (dù muốn) vì vướng quy tắc/lương tâm', sai ngữ cảnh miêu tả cách nhìn văn hóa.",
            "わけにもいきません: Nghĩa là 'cũng không thể làm vì lý do tương tự', sai mẫu ngữ pháp.",
        ],
    },
    # ID=146
    "4b1b98d18237f1b1caf549b77eb8301a855dbb93003c0819da0a920e7d889f24": {
        "links": [
            {"grammar_code": "GP-N3-115", "role": "primary_target", "note_vi": "Liên từ đưa ví dụ cụ thể たとえば (minh họa cho 'ở cùng một chỗ quá lâu')."},
            {"grammar_code": "GP-N3-115", "role": "distractor_trap", "note_vi": "Bẫy つまり / それとも: つまり đúc kết/tóm gọn lại; それとも hỏi lựa chọn ('hay là')."},
            {"grammar_code": "GP-N3-077", "role": "distractor_trap", "note_vi": "Bẫy もちろん: nghĩa là 'tất nhiên rồi', dùng nhấn mạnh điều hiển nhiên chứ không nêu thông số cụ thể 2 tuần / 4 tuần."},
            {"grammar_code": "GP-N5-10", "role": "sentence_structure", "note_vi": "Hai câu liền kề cùng kết bằng mệnh lệnh lịch sự ～ないでください và ～にしてください."},
        ],
        "structure_parse_vi": (
            "Mạch văn Đục lỗ (PID=1 この薬の使い方): Câu trước nêu nguyên tắc chung [同じところに続けて長く使用しないでください]. "
            "Chỗ trống [4] cần liên từ [たとえば] để đưa ra thông số giới hạn minh họa cụ thể cho hai vùng da [顔は2週間以内、その他のところは4週間以内にしてください]."
        ),
        "pedagogical_takeaway_vi": "Khi câu trước nói quy tắc tổng quát ('đừng dùng lâu', 'đừng ăn nhiều') và câu sau tách ra con số cụ thể từng trường hợp -> chọn たとえば.",
        "option_grammar_notes": [
            "つまり: Dùng tóm tắt/nói cách khác toàn bộ ý, không dùng liệt kê thông số minh họa riêng lẻ cho từng bộ phận.",
            "もちろん: 'Đương nhiên là', không thể coi giới hạn '2 tuần cho mặt, 4 tuần cho chỗ khác' là lẽ hiển nhiên ai cũng biết sẵn.",
            "たとえば: ĐÚNG. Đưa ra ví dụ cụ thể hóa cho quy định chung ở câu trước.",
            "それとも: 'Hay là...', chỉ dùng nối hai vế câu hỏi lựa chọn.",
        ],
    },
    # ID=147
    "fdd298223f5f8fb37e4add7688959b5581d59cfae7b64fdad2626b11b7665d8d": {
        "links": [
            {"grammar_code": "GP-N3-066", "role": "primary_target", "note_vi": "Vる + おそれがあります: có nguy cơ triệu chứng xấu đi (văn bản y khoa/cảnh báo)."},
            {"grammar_code": "GP-N3-107", "role": "distractor_trap", "note_vi": "Bẫy ずにはいられません: chỉ cảm xúc/phản ứng tâm lý tự phát của người, không dùng cho 'triệu chứng bệnh' (症状)."},
            {"grammar_code": "GP-N4-14", "role": "distractor_trap", "note_vi": "Bẫy ことになっています: 'theo quy định được định sẵn', vô lý nếu quy định bắt triệu chứng phải nặng hơn."},
            {"grammar_code": "GP-N3-064", "role": "distractor_trap", "note_vi": "Bẫy にきまっています: suy đoán chủ quan cảm tính cá nhân, không dùng trong hướng dẫn sử dụng thuốc trang trọng."},
            {"grammar_code": "GP-N4-16", "role": "sentence_structure", "note_vi": "Mệnh đề điều kiện phủ định 気をつけないと dẫn vào cảnh báo rủi ro ở cuối đoạn."},
        ],
        "structure_parse_vi": (
            "Mạch văn Đục lỗ (PID=1 この薬の使い方): Câu kết toàn bài hướng dẫn tổng hợp mọi cảnh báo phía trên bằng [以上のことに気をつけないと] "
            "(nếu không chú ý các điều nêu trên thì - điều kiện と) -> cảnh báo rủi ro y khoa trang trọng [症状が + 悪くなるおそれがあります] (GP-N3-066)."
        ),
        "pedagogical_takeaway_vi": "Thấy danh từ rủi ro (症状 / 事故 / 病気 / 地震) + Vる + cảnh báo trong văn bản thông báo/y tế -> chọn ～おそれがある.",
        "option_grammar_notes": [
            "悪くならずにはいられません: Chỉ dùng cho cảm xúc không kìm được của người, sai chủ ngữ vô tri 症状.",
            "悪くなることになっています: 'Theo quy định/lịch trình thì bệnh sẽ nặng lên', phi lý hoàn toàn.",
            "悪くなるにきまっています: Phỏng đoán chủ quan khẩu ngữ, sai văn phong y tế và mang tính khẳng định thái quá.",
            "悪くなるおそれがあります: ĐÚNG. Cảnh báo trang trọng nguy cơ triệu chứng trở nặng.",
        ],
    },
    # ID=148
    "b75b79f74ea167992faf9422d806aa3491148ccb51acf72d0b9f867dbf65fd62": {
        "links": [
            {"grammar_code": "GP-N3-111", "role": "primary_target", "note_vi": "Bị động + てきました (つくられてきました): ngôi nhà đã và đang được xây dựng từ xưa tới nay."},
            {"grammar_code": "GP-N4-03", "role": "sentence_structure", "note_vi": "Chủ ngữ là Nhà (家が) nên động từ つくる phải chia thể bị động つくられる."},
            {"grammar_code": "GP-N4-06", "role": "distractor_trap", "note_vi": "Bẫy つくってあります: dùng tha động từ chia てある nên không nhận chủ ngữの家 với が theo kiểu có mốc 昔から ở đây dễ nhầm hành động tác nhân."},
            {"grammar_code": "GP-N4-05", "role": "distractor_trap", "note_vi": "Bẫy つくっておきました: 'đã làm sẵn trước', dùng tha động từ và không diễn tả tiến trình lịch sử từ 昔から tới hiện tại."},
            {"grammar_code": "GP-N3-005", "role": "sentence_structure", "note_vi": "Câu mang trạng ngữ chuyển tiếp nguyên nhân ですから và mốc 昔から khớp thì quá khứ tiếp diễn tới hiện tại."},
        ],
        "structure_parse_vi": (
            "Mạch văn Đục lỗ (PID=18 緑のカーテン): Câu trước nêu đặc điểm khí hậu nóng ẩm của Nhật, câu [1] mở đầu lịch sử kiến trúc bằng [ですから、日本では昔から] "
            "(mốc từ xa xưa đến hiện tại) + chủ ngữ vật [この気候に合わせた家が] -> động từ bắt buộc phải vừa là bị động vừa tiếp diễn đến nay: [つくられてきました] (GP-N3-111)."
        ),
        "pedagogical_takeaway_vi": "Kiểm tra song song 2 trục ở Đọc hiểu Đục lỗ: (1) Chủ ngữ là đồ vật/truyền thống + が -> chọn BỊ ĐỘNG; (2) Có từ 昔から -> chọn ～てきた.",
        "option_grammar_notes": [
            "つくられました: Đúng thể bị động nhưng là hành động đã chấm dứt trong quá khứ, thiếu mạch kéo dài tới hiện tại từ 昔から.",
            "つくってあります: Cấu trúc tha động từ chỉ trạng thái bày biện có chủ ý hiện thời, không hợp dòng lịch sử 昔から.",
            "つくられてきました: ĐÚNG. Thể bị động + てきました = đã và đang được xây dựng truyền nối từ xưa đến nay.",
            "つくっておきました: Tha động từ 'đã làm chuẩn bị sẵn', sai cả chủ thể và trục thời gian.",
        ],
    },
    # ID=149
    "cdb892c0600bf948663f5b5a41cb0312fbc2feb81174f6febbb7d62b4d046467": {
        "links": [
            {"grammar_code": "GP-N3-113", "role": "primary_target", "note_vi": "Vる + のを + 防ぐ: danh từ hóa mệnh đề 'không khí lạnh tràn vào phòng' làm tân ngữ cho tha động từ 防ぎます."},
            {"grammar_code": "GP-N5-07", "role": "distractor_trap", "note_vi": "Bẫy ことが: 防ぎます là tha động từ đòi hỏi trợ từ を, không dùng が."},
            {"grammar_code": "GP-N3-027", "role": "distractor_trap", "note_vi": "Bẫy とか: dùng liệt kê ví dụ ('những thứ như là'), sai ngữ pháp sau động từ vào trong câu này."},
            {"grammar_code": "GP-N5-02", "role": "distractor_trap", "note_vi": "Bẫy ものを: もの chỉ đồ vật hữu hình, không danh từ hóa sự việc 'hành động không khí lạnh lọt vào'."},
        ],
        "structure_parse_vi": (
            "Mạch văn Đục lỗ (PID=18 緑のカーテン): Đoạn giải thích công dụng của nhà truyền thống Nhật vào mùa đông: "
            "[冬には] + mệnh đề sự việc [冷たい空気が部屋の中に入る] + danh từ hóa làm tân ngữ [のを] (GP-N3-113) + tha động từ [防ぎます]."
        ),
        "pedagogical_takeaway_vi": "Khi động từ cuối câu là tha động từ trực giác/can thiệp sự việc đang diễn ra (防ぐ ngăn, 止める dừng, 待つ đợi, 見る nhìn) -> danh từ hóa luôn dùng のを.",
        "option_grammar_notes": [
            "ことが: Sai trợ từ — động từ 防ぎます (ngăn chặn) là tha động từ đi với を, không đi với が.",
            "のを: ĐÚNG. Danh từ hóa mệnh đề sự việc đang diễn ra + を làm tân ngữ cho 防ぎます.",
            "とか: Dùng liệt kê ví dụ, không nối mệnh đề làm tân ngữ trực tiếp cho 防ぐ.",
            "ものを: Danh từ もの chỉ đồ vật hữu hình, không dùng thay thế sự kiện 'không khí tràn vào'.",
        ],
    },
    # ID=150
    "e22ad2ff2b6c3dacaede3f9180329e1f01570702ec8e4bb063693181090b6bdd": {
        "links": [
            {"grammar_code": "GP-N3-093", "role": "primary_target", "note_vi": "Vます + つつあります (減りつつあります): phòng kiểu Nhật đang dần dần giảm đi."},
            {"grammar_code": "GP-N3-109", "role": "distractor_trap", "note_vi": "Bẫy 減るだけです: mang nghĩa giới hạn 'chỉ có giảm thôi', sai sắc thái phân tích xu hướng xã hội."},
            {"grammar_code": "GP-N4-10", "role": "distractor_trap", "note_vi": "Bẫy 減りやすいです: diễn tả tính chất 'dễ bị giảm', không phải xu hướng thay đổi thực tế do 多くなりましたから."},
            {"grammar_code": "GP-N3-110", "role": "distractor_trap", "note_vi": "Bẫy 減ってもかまいません: nghĩa là 'dù có giảm cũng chẳng sao', hoàn toàn sai logic nguyên nhân - kết quả."},
            {"grammar_code": "GP-N5-13", "role": "sentence_structure", "note_vi": "Mệnh đề nguyên nhân lối sống hiện đại (いすに座ることが多くなりましたから) dẫn ra xu hướng biến đổi hiện tại."},
        ],
        "structure_parse_vi": (
            "Mạch văn Đục lỗ (PID=18 緑のカーテン): Đoạn chuyển từ kiến trúc xưa sang hiện đại bằng nguyên nhân [いすに座ることが多くなりましたから] "
            "(vì việc ngồi ghế trở nên nhiều hơn - GP-N4-15 + GP-N5-13) -> dẫn đến xu hướng biến đổi dần dần hiện nay [和室が + 減りつつあります] (GP-N3-093)."
        ),
        "pedagogical_takeaway_vi": "Gặp văn viết/báo chí mô tả một xu hướng tăng hoặc giảm dần (増える / 減る / 変わる / 進む) do đổi thay lối sống -> nhớ ngay Vます + つつある.",
        "option_grammar_notes": [
            "減るだけです: Nghĩa 'chỉ có giảm thôi', không diễn tả tiến trình biến chuyển đang diễn ra từng bước.",
            "減りやすいです: Chỉ tính chất dễ tổn thương/dễ sụt giảm, không miêu tả thực trạng đang diễn ra do ngồi ghế nhiều.",
            "減ってもかまいません: 'Có giảm cũng không sao', lạc đề hoàn toàn so với ngữ cảnh.",
            "減りつつあります: ĐÚNG. Vます + つつあります = đang trên đà giảm dần trong văn viết.",
        ],
    },
    # ID=151
    "3d3bebc63a9df62c43f56046ce76df27aebcb6612bedeaff04296ad5e8ce95b4": {
        "links": [
            {"grammar_code": "GP-N3-005", "role": "primary_target", "note_vi": "N + によって + Bị động (水分によって冷やされている): gió được làm mát nhờ hơi nước từ cây."},
            {"grammar_code": "GP-N3-048", "role": "distractor_trap", "note_vi": "Bẫy にとって: đánh giá từ lập trường của một người/tập thể, không đứng sau 水分 để làm tác nhân làm mát."},
            {"grammar_code": "GP-N3-099", "role": "distractor_trap", "note_vi": "Bẫy につれて / にともなって: chỉ hai biến đổi song hành tỷ lệ thuận ('cùng với A thì B biến đổi'), không chỉ phương tiện vật lý trong câu bị động."},
            {"grammar_code": "GP-N4-03", "role": "sentence_structure", "note_vi": "Vị ngữ bị động tiếp diễn 冷やされている xác định ngay nhu cầu tác nhân/phương tiện đứng trước là によって."},
        ],
        "structure_parse_vi": (
            "Mạch văn Đục lỗ (PID=18 緑のカーテン): Giải thích cơ chế làm mát tự nhiên của rèm cây xanh: "
            "chủ ngữ [窓から入ってくる風は] (GP-N4-07) + cụm định ngữ nguồn hơi ẩm [窓の外側の植物が出す水分] "
            "+ tác nhân phương tiện [によって] (GP-N3-005) + bị động trạng thái [冷やされている] + nguyên nhân ので."
        ),
        "pedagogical_takeaway_vi": "Nhìn động từ ngay sau chỗ trống ở thể Bị động (冷やされる / 作られる / 支えられる) -> chọn ngay によって chỉ tác nhân hoặc phương tiện.",
        "option_grammar_notes": [
            "にとって: Chỉ lập trường đánh giá ('đối với...'), không ghép với vô tri 水分 làm tác nhân làm mát.",
            "につれて: Diễn tả biến đổi song hành theo thời gian/quy mô, sai quan hệ phương tiện bị động.",
            "にともなって: Diễn tả hai biến cố/xu hướng biến đổi cùng lúc, không nối tác nhân bị động 冷やされている.",
            "によって: ĐÚNG. Chỉ tác nhân/phương tiện làm mát gió trong cấu trúc bị động.",
        ],
    },
    # ID=152
    "3e98d8bb5face849b6579967bd6e1e6e480d2c8067c6d51d9df4bb8034391238": {
        "links": [
            {"grammar_code": "GP-N3-112", "role": "primary_target", "note_vi": "Bị động + ていくでしょう (使われていくでしょう): sẽ tiếp tục được sử dụng trong nhà Nhật tương lai."},
            {"grammar_code": "GP-N3-111", "role": "distractor_trap", "note_vi": "Bẫy 増えてきました: chiều てきた hướng từ quá khứ tới hiện tại, mâu thuẫn với trạng ngữ これからの."},
            {"grammar_code": "GP-N4-19", "role": "distractor_trap", "note_vi": "Bẫy 見られなくなるはずです: dự báo tiêu cực 'chắc sẽ biến mất', ngược hoàn toàn với vế nguyên nhân よく合っていますから."},
            {"grammar_code": "GP-N4-08", "role": "distractor_trap", "note_vi": "Bẫy 減っていきそうです: đúng hướng ていく nhưng sai nghĩa ngược hoàn toàn ('có vẻ sẽ giảm đi')."},
            {"grammar_code": "GP-N5-13", "role": "sentence_structure", "note_vi": "Câu kết nối lý do tích cực よく合っていますから với dự báo tương lai でしょう."},
        ],
        "structure_parse_vi": (
            "Mạch văn Đục lỗ (PID=18 緑のカーテン): Câu kết đoạn tóm lược ưu điểm của rèm cây: "
            "[暮らし方によく合っていますから] (vì rất hợp lối sống hiện đại - mệnh đề thuận) + cụm thời gian tương lai [これからの日本の家に] "
            "-> vị ngữ bị động tiếp diễn về tương lai + dự đoán: [使われていくでしょう] (GP-N3-112)."
        ),
        "pedagogical_takeaway_vi": "Chốt đoạn Đục lỗ: kiểm tra hai chốt 'trục thời gian' (これからの -> chọn ていく) và 'cực tính luận điểm' (hợp lối sống -> chọn được tiếp tục dùng tích cực).",
        "option_grammar_notes": [
            "増えてきました: Dùng chiều quá khứ-hiện tại てきた, mâu thuẫn trực tiếp với これからの (từ nay về sau).",
            "見られなくなるはずです: Đảo ngược logic tích cực ('chắc sẽ không còn thấy nữa' sau lý do 'rất hợp').",
            "使われていくでしょう: ĐÚNG. Thể bị động + ていく + でしょう = có lẽ sẽ tiếp tục được sử dụng trong tương lai.",
            "減っていきそうです: Đúng chiều ていく nhưng sai ngược hoàn toàn cực tính nghĩa ('có vẻ sẽ giảm đi').",
        ],
    },
    # ID=153
    "211c4366a1d9eec08e92ebb4ab8b8f458d33c3a58e011a8566ee4bf7cc9d5d82": {
        "links": [
            {"grammar_code": "GP-N3-065", "role": "primary_target", "note_vi": "Cặp hô ứng cố định おそらく ～ に違いない: chắc hẳn việc bất đồng ngôn ngữ sẽ thành stress lớn."},
            {"grammar_code": "GP-N3-053", "role": "distractor_trap", "note_vi": "Bẫy なってばかりいる: diễn tả hành động lặp đi lặp lại hoặc trạng thái tiêu cực cứ tái diễn liên tục, không hô ứng với phó từ おそらく."},
            {"grammar_code": "GP-N3-067", "role": "distractor_trap", "note_vi": "Bẫy なるにすぎない: mang sắc thái hạ thấp 'chẳng qua chỉ là... mà thôi', mâu thuẫn với 大きなストレス."},
            {"grammar_code": "GP-N4-17", "role": "distractor_trap", "note_vi": "Bẫy なろうとする: chỉ ý chí cố gắng biến thành của chủ thể có ý thức, sai chủ ngữ vô tri '言葉ができないこと'."},
            {"grammar_code": "GP-N5-07", "role": "sentence_structure", "note_vi": "Danh từ hóa [その国の言葉ができない + こと + は] làm chủ ngữ cho suy đoán."},
        ],
        "structure_parse_vi": (
            "Mạch văn Đục lỗ (PID=19 日本人スポーツ選手): Mở đầu đặt ra khó khăn của vận động viên Nhật ra nước ngoài: "
            "[その国の言葉ができないことは] (việc không biết ngôn ngữ nước đó - GP-N5-07) + phó từ dự đoán [おそらく] "
            "+ [大きなストレスになるに違いない] (hô ứng chắc chắn với おそらく - GP-N3-065)."
        ),
        "pedagogical_takeaway_vi": "Gặp phó từ おそらく (có lẽ, chắc hẳn) ở đầu vế suy đoán -> ưu tiên cặp hô ứng に違いない (hoặc だろう / はずだ).",
        "option_grammar_notes": [
            "なるに違いない: ĐÚNG. Hô ứng hoàn chỉnh với phó từ suy đoán おそらく.",
            "なってばかりいる: Không có chức năng suy đoán, không đi với おそらく.",
            "なるにすぎない: Hạ thấp mức độ ('chỉ là thôi'), mâu thuẫn với tính chất 大きなストレス.",
            "なろうとする: Diễn tả ý chí chủ động muốn biến thành, vô nghĩa với chủ ngữ trừu tượng 'việc không biết tiếng'.",
        ],
    },
    # ID=154
    "2885be797e04601931f8308f2f9423c505b33f6d843e46d1387695551a057cc1": {
        "links": [
            {"grammar_code": "GP-N3-023", "role": "primary_target", "note_vi": "N + さえ + Vなくても: đến cả ngôn ngữ không biết cũng vẫn xoay xở được."},
            {"grammar_code": "GP-N3-053", "role": "distractor_trap", "note_vi": "Bẫy ばかり: diễn tả 'chỉ toàn', làm câu mất nghĩa nhấn mạnh ví dụ tối thiểu."},
            {"grammar_code": "GP-N5-17", "role": "distractor_trap", "note_vi": "Bẫy しか: gắn sau 言葉 + phủ định できなくても thành 'chỉ mỗi không nói được tiếng' hoặc lệch sắc thái giới hạn."},
            {"grammar_code": "GP-N3-046", "role": "distractor_trap", "note_vi": "Bẫy なんか: mang sắc thái coi nhẹ khẩu ngữ kiểu 'ba cái thứ tiếng tăm', không phù hợp thông điệp tôn trọng tích cực."},
            {"grammar_code": "GP-N4-16", "role": "sentence_structure", "note_vi": "Nhấn mạnh nhượng bộ だって ('kể cả trong sinh hoạt hằng ngày đi nữa thì...') phối hợp với さえ... できなくても."},
        ],
        "structure_parse_vi": (
            "Mạch văn Đục lỗ (PID=19 日本人スポーツ選手): Tác giả phản biện giả định ở câu 1 (câu 1 bảo stress vì ngôn ngữ, câu 2 bảo thậm chí thiếu ngôn ngữ vẫn ổn): "
            "[日常生活だって] -> yếu tố tối thiểu [言葉 + さえ] (GP-N3-023) + nhượng bộ [できなくても] -> kết quả lạc quan [なんとかなりますよ]."
        ),
        "pedagogical_takeaway_vi": "Thấy danh từ cơ bản + [___] + phủ định nhượng bộ (~なくても / ~なければ) + kết quả vẫn ổn -> chọn trợ từ さえ ('ngay cả không có N đi nữa cũng...').",
        "option_grammar_notes": [
            "ばかり: 'Chỉ toàn là...', không khớp vế nhượng bộ できなくてもなんとかなる.",
            "しか: Giới hạn phạm vi ('chỉ mỗi'), làm biến đổi thành 'chỉ mỗi không nói được ngôn ngữ chứ cái khác được' — sai ý tác giả.",
            "さえ: ĐÚNG. Ngay cả điều cơ bản nhất là ngôn ngữ không biết đi nữa cũng xoay xở được.",
            "なんか: Mang sắc thái coi nhẹ cảm tính ('mấy thứ như là'), lạc tông văn phong.",
        ],
    },
    # ID=155
    "57231d9acf6cc7cf02d2abb227ecab1a6e77da83a94bb6362b30385c3ca01949": {
        "links": [
            {"grammar_code": "GP-N3-020", "role": "primary_target", "note_vi": "Vない + せいで: tại vì không hiểu câu đùa nên mỗi mình không cười được và thấy cay cú."},
            {"grammar_code": "GP-N4-20", "role": "distractor_trap", "note_vi": "Bẫy むずかしそうで: 'trông có vẻ khó', thiếu quan hệ nguyên nhân dẫn tới kết quả không cười được."},
            {"grammar_code": "GP-N4-16", "role": "distractor_trap", "note_vi": "Bẫy 理解できないなら: điều kiện giả định 'nếu không hiểu thì...', mâu thuẫn với trải nghiệm quá khứ くやしかった."},
            {"grammar_code": "GP-N4-12", "role": "distractor_trap", "note_vi": "Bẫy 聞こえなかったために: bẫy đọc hiểu — VĐV vẫn nghe âm thanh câu đùa nhưng KHÔNG HIỂU nghĩa tiếng Anh (わからない) nên không cười được."},
            {"grammar_code": "GP-N5-13", "role": "sentence_structure", "note_vi": "Liên kết giải thích nguyên nhân (～せいで) trong câu tường thuật tâm trạng quá khứ (くやしかったからですよ)."},
        ],
        "structure_parse_vi": (
            "Mạch văn Đục lỗ (PID=19 日本人スポーツ選手): Giải thích động lực thật khiến cầu thủ quyết tâm học tiếng Anh: "
            "chủ thể định ngữ [外国人が言った冗談が] + nguyên nhân đáng tiếc [わからないせいで] (GP-N3-020) "
            "-> hậu quả [自分だけ笑えないのがくやしかったからですよ] (việc chỉ mình không cười được khiến cậu ấy ấm ức)."
        ),
        "pedagogical_takeaway_vi": "Đừng chỉ nhìn ngữ pháp đúng ở Đục lỗ mà quên đối chiếu ĐÚNG NGHĨA với bài đọc (わからない khác hẳn 聞こえなかった!).",
        "option_grammar_notes": [
            "むずかしそうで: Nghĩa là 'trông có vẻ khó', không diễn tả nguyên nhân cụ thể làm mất cơ hội cười.",
            "理解できないなら: Câu điều kiện giả định, không hợp thì quá khứ xác thực くやしかった.",
            "わからないせいで: ĐÚNG. Tại vì không hiểu trò đùa nên không cười được và thấy ấm ức.",
            "聞こえなかったために: Ngữ pháp đúng nhưng SAI nội dung bài đọc (vấn đề là hiểu nghĩa, không phải thính giác bị điếc hay ồn).",
        ],
    },
    # ID=156
    "af088d33d5e8563e7fb38221f0cc1d40263734fdb02faff0a68492bcc15301b0": {
        "links": [
            {"grammar_code": "GP-N3-050", "role": "primary_target", "note_vi": "Vる + こともある: cũng có lúc sẽ cảm thấy mệt mỏi/đau khổ."},
            {"grammar_code": "GP-N4-14", "role": "distractor_trap", "note_vi": "Bẫy ことになる: chỉ quyết định khách quan hoặc kết cục chắc chắn hoàn toàn, không hợp ý dự phòng 'thỉnh thoảng cũng có lúc'."},
            {"grammar_code": "GP-N3-005", "role": "distractor_trap", "note_vi": "Bẫy ことによる: nghĩa là 'tùy thuộc vào việc...', sai cấu trúc kết câu dự đoán だろう."},
            {"grammar_code": "GP-N3-051", "role": "distractor_trap", "note_vi": "Bẫy ことはない: 'không cần thiết phải / không đời nào', trái ngược hoàn toàn thông điệp tác giả."},
            {"grammar_code": "GP-N4-15", "role": "sentence_structure", "note_vi": "Mệnh đề trích dẫn ý chí tự nhủ [負けないようにしよう] + điều kiện tiếp diễn [努力し続けたら] (GP-N4-16 + GP-N3-078)."},
        ],
        "structure_parse_vi": (
            "Mạch văn Đục lỗ (PID=19 日本人スポーツ選手): Tác giả cảnh báo mặt trái của việc gồng mình quá sức: "
            "[「外国人に負けないようにしよう」と思って + 努力し続けたら] (nếu cứ cố gắng với tâm lý không được thua kém - điều kiện たら) "
            "-> hệ quả có khả năng phát sinh từng lúc [つらくなる + こともあるだろう] (GP-N3-050 + GP-N5-16)."
        ),
        "pedagogical_takeaway_vi": "Phân biệt bộ 3 [Vる + こと] cuối câu: Vることもある (đôi khi có lúc xảy ra) vs Vることはない (không cần phải/không bao giờ) vs Vることになる (được quyết định là).",
        "option_grammar_notes": [
            "ことになる: Nghĩa 'được quy định / kết cục là', quá cứng so với phỏng đoán mềm mại つらくなる...だろう.",
            "ことによる: Nghĩa 'phụ thuộc vào việc...', không kết thúc câu bằng だろう như vị ngữ.",
            "ことはない: Ngược hoàn toàn logic ('sẽ không cần phải/không bao giờ thấy khổ').",
            "こともある: ĐÚNG. Vる + こともあるだろう = cũng có lúc sẽ cảm thấy vất vả, đau khổ.",
        ],
    },
    # ID=157
    "aee38b37a3a5d53ad25e6af59aa67c5be8fbe3a1fe5522c0b1d0c28cacc8eaa2": {
        "links": [
            {"grammar_code": "GP-N3-042", "role": "primary_target", "note_vi": "N + こそ + が: chính tinh thần thoải mái và suy nghĩ tích cực mới là điều cần thiết."},
            {"grammar_code": "GP-N3-010", "role": "distractor_trap", "note_vi": "Bẫy ほど: diễn tả mức độ ('đến mức...'), không ghép trực tiếp giữa chủ ngữ N và が trước 必要なのだろう."},
            {"grammar_code": "GP-N5-17", "role": "distractor_trap", "note_vi": "Bẫy だけ: giới hạn 'chỉ có mỗi', làm giảm sức nặng khẳng định chủ trương ở câu kết bài."},
            {"grammar_code": "GP-N3-009", "role": "distractor_trap", "note_vi": "Bẫy くらい: mang nghĩa ước lượng ('khoảng/cỡ như'), sai chức năng nhấn mạnh chủ thể."},
            {"grammar_code": "GP-N3-048", "role": "sentence_structure", "note_vi": "Cụm lập trường [外国で活躍するスポーツ選手にとって] đánh giá tầm quan trọng đối với vận động viên."},
        ],
        "structure_parse_vi": (
            "Mạch văn Đục lỗ (PID=19 日本人スポーツ選手): Câu kết toàn bài thâu tóm thông điệp chính: "
            "chủ thể [このような心の余裕や前向きな考え方 + こそ + が] (nhấn mạnh tuyệt đối bằng こそ - GP-N3-042) "
            "+ đối tượng đánh giá [スポーツ選手にとって] (GP-N3-048) -> [必要なのだろう]."
        ),
        "pedagogical_takeaway_vi": "Khi danh từ trừu tượng ở câu kết bài đứng ngay trước [___が + 必要なのだろう / 大切だ], trợ từ đứng chen giữa danh từ và が để nhấn mạnh chủ thể luôn là こそ (こそが).",
        "option_grammar_notes": [
            "ほど: Trợ từ so sánh mức độ, không tạo cụm nhấn mạnh chủ ngữ [N + ほど + が] trong khẳng định chủ trương.",
            "こそ: ĐÚNG. 考え方こそが = chính tư duy này mới thực sự là điều cần thiết.",
            "だけ: Giới hạn phạm vi 'chỉ có', mâu thuẫn với thông điệp nhấn mạnh tích cực mở rộng.",
            "くらい: Nghĩa 'cỡ khoảng', hạ nhẹ tầm quan trọng của luận điểm chính.",
        ],
    },
    # =========================================================================
    # SECTION 2: VOCABULARY BATCH 1 (49 QUESTIONS: IDs 1-14, 35-48, 69-89)
    # =========================================================================
    # ID=1
    "d64a8882c98a2210e74682a501c0feb557269c6aaea00c712d2d8c45526f6958": {
        "links": [
            {"grammar_code": "GP-N5-14", "role": "sentence_structure", "note_vi": "Liệt kê song song 気温も湿度も (cả nhiệt độ lẫn độ ẩm đều...)."},
            {"grammar_code": "GP-N4-10", "role": "sentence_structure", "note_vi": "Đuôi 過ごしにくい (Vます + にくい): khó chịu/khó sống."},
            {"grammar_code": "GP-N5-05", "role": "sentence_structure", "note_vi": "Tính từ đuôi い chia thể て (高くて) nêu nguyên nhân dẫn đến tính từ 過ごしにくい."},
        ],
        "structure_parse_vi": (
            "[日本の夏は] (chủ đề) + song hành [気温も + 湿度も + 高くて] (tính từ chia て nguyên nhân GP-N5-05) "
            "-> vị ngữ đánh giá mức độ khó sinh hoạt [過ごしにくい] (Vます + にくい GP-N4-10)."
        ),
        "pedagogical_takeaway_vi": "Trong câu có dạng AもBも + 高くて + Vますにくい, vế sau luôn khái quát cảm nhận chịu ảnh hưởng từ cả hai yếu tố song song.",
        "option_grammar_notes": [
            "しつけ (躾): Danh từ, nghĩa 'sự dạy dỗ lễ nghi', sai ngữ nghĩa thời tiết.",
            "しつど (湿度): ĐÚNG. Danh từ song hành với 気温 (nhiệt độ).",
            "しっき (湿気): Bẫy âm đọc chữ 気 thành き ('hơi ẩm'), không phải từ chỉ số đo 'độ ẩm' đi cặp với 気温.",
            "しめど: Bẫy ghép sai âm Kun của 湿 (しめる) với âm On của 度 (ど).",
        ],
    },
    # ID=2
    "4eda31077a75b3cb87e8bc73ba9b78734e0508913c742448d565db10079f8434": {
        "links": [
            {"grammar_code": "GP-N5-03", "role": "sentence_structure", "note_vi": "Trợ từ で sau これで đánh dấu phạm vi/mức lượng công cụ ('với chừng này thì...')."},
            {"grammar_code": "GP-N5-18", "role": "sentence_structure", "note_vi": "Tự động từ 足りる (đủ dùng) không nhận tân ngữ を."},
        ],
        "structure_parse_vi": (
            "[これで] (với mức lượng này - phạm vi công cụ/số lượng で) + câu hỏi xác nhận [足りますか。] -> hỏi ý kiến [どうですか。]."
        ),
        "pedagogical_takeaway_vi": "Cả 足りる (đủ) và 余る (dư thừa) đều là tự động từ, hay đi kèm lượng từ + で (これで足りますか = chừng này đủ chưa?).",
        "option_grammar_notes": [
            "たります (足ります): ĐÚNG. Tự động từ nhóm 2 'đủ dùng', khớp ngữ cảnh これで.",
            "かります (借ります): Tha động từ 'đi mượn', thường đòi hỏi tân ngữ với を.",
            "あまります (余ります): Tự động từ trái nghĩa ('còn thừa lại').",
            "かわります (変わります): Tự động từ 'thay đổi', không hợp hỏi số lượng.",
        ],
    },
    # ID=3
    "71f587a94ea9a890146d19afb9e7114a65620d93cdbbab657dd379961f1d98b0": {
        "links": [
            {"grammar_code": "GP-N5-02", "role": "sentence_structure", "note_vi": "Khung chủ vị chuẩn SVO: [Chủ ngữ は] + [Danh từ の Danh từ を] + [Danh động từ する]."},
        ],
        "structure_parse_vi": (
            "[その歌手は] (chủ ngữ は) + tân ngữ [離婚の + うわさを] (tin đồn về chuyện ly hôn - NのN + を) + vị ngữ hành động [否定した] (V3 quá khứ)."
        ),
        "pedagogical_takeaway_vi": "Danh động từ Hán-Nhật hai chữ (否定する, 肯定する) đứng cuối câu làm tha động từ trực tiếp cho cụm NのNを.",
        "option_grammar_notes": [
            "ひて: Lỗi rơi trường âm い ở âm tiết thứ hai (定 đọc là てい).",
            "ふってい: Lỗi đọc 否 thành ふ thêm xúc âm っ.",
            "ひてい (否定): ĐÚNG. Phủ nhận hoàn toàn tin đồn.",
            "ふてい: Bẫy ghép nhầm âm của 不 (ふ) cho chữ 否 (ひ).",
        ],
    },
    # ID=4
    "b84dc432d2e0d764d6c46ec0bc1382029df65770f3ee5d3a321e489dc5599d42": {
        "links": [
            {"grammar_code": "GP-N5-05", "role": "sentence_structure", "note_vi": "Tính từ đuôi な giữ nguyên な khi bổ nghĩa trực tiếp cho danh từ ところ (不便なところ)."},
            {"grammar_code": "GP-N5-03", "role": "sentence_structure", "note_vi": "Trợ từ に đánh dấu vị trí tồn tại tĩnh đi với động từ ある."},
        ],
        "structure_parse_vi": (
            "[母の家は]、(chủ đề) + phó từ mức độ [とても] + cụm danh từ có định ngữ tính từ な [不便な + ところ] + vị trí tồn tại [に + ある] (GP-N5-03)."
        ),
        "pedagogical_takeaway_vi": "Nhận diện ngay đuôi ～なところにある phía sau chỗ trống để chắc chắn từ cần điền là một Tính từ đuôi な miêu tả tính chất địa điểm.",
        "option_grammar_notes": [
            "非便: Sai tiền tố phủ định — chữ 便 ghép với 不 (ふ), không dùng 非 (ひ).",
            "非勉: Sai cả hai chữ Hán (勉 là cố gắng trong 勉強).",
            "不便 (ふべん): ĐÚNG. Tính từ đuôi な nối vào なところ.",
            "不勉: Sai chữ thứ hai (nhầm 便 với 勉).",
        ],
    },
    # ID=5
    "f6df469b91c27a04eeb5dc5011d36820d926e3ab576e98fd618f83eb34c04b07": {
        "links": [
            {"grammar_code": "GP-N5-03", "role": "sentence_structure", "note_vi": "Cấu trúc mục đích di chuyển [Vます (食べ) + に + 来る]: bay đến ĐỂ ăn."},
            {"grammar_code": "GP-N5-02", "role": "sentence_structure", "note_vi": "Chủ ngữ động vật 小鳥が đứng đầu, tân ngữ 木の実を gắn động từ ăn."},
        ],
        "structure_parse_vi": (
            "[ことりが] (chủ thể hành động) + địa điểm [庭の木の実を] (tân ngữ của 食べる nằm trong cụm mục đích) "
            "+ mục đích di chuyển [食べ + に + 来る] (GP-N5-03)."
        ),
        "pedagogical_takeaway_vi": "Khi thấy động từ ở dạng bỏ ます + に + 行く / 来る, tân ngữ gắn với を đứng trước đó thuộc về động từ mục đích.",
        "option_grammar_notes": [
            "子島: Sai cả hai chữ (子 con + 島 hòn đảo), không hợp ngữ cảnh bay tới ăn quả.",
            "小島 (こじま): Đảo nhỏ — làm chủ ngữ cho hành động bay tới ăn là phi lý.",
            "子鳥: Tiếng Nhật viết 'chim nhỏ' là 小鳥 (ことり), không viết 子鳥 dù thú 4 chân dùng 子犬/子猫.",
            "小鳥 (ことり): ĐÚNG. Chủ thể hành động bay đến vườn ăn quả.",
        ],
    },
    # ID=6
    "704bca392a074ec15282618ceebcca36b8ad37e785c30eb305e76156b7da57c2": {
        "links": [
            {"grammar_code": "GP-N4-18", "role": "sentence_structure", "note_vi": "Vて + くれた (来てくれた): bạn đã làm giúp cho mình (sắc thái biết ơn)."},
            {"grammar_code": "GP-N5-04", "role": "sentence_structure", "note_vi": "Trợ từ giới hạn điểm đến 空港まで (ra tận sân bay) + mục đích 迎えに + 来る."},
        ],
        "structure_parse_vi": (
            "[友だちが] (người thực hiện ân huệ) + giới hạn địa điểm [空港まで] (GP-N5-04) "
            "+ mục đích [迎え + に] (danh từ hóa từ Vます của 迎える) + [来てくれた] (ân huệ hướng về người nói GP-N4-18)."
        ),
        "pedagogical_takeaway_vi": "Cụm [空港 / 駅 + まで] + [迎えに + 来る / 行く] + [てくれた] là mẫu giao tiếp chuẩn về việc ra đón ai đó.",
        "option_grammar_notes": [
            "通え: Chữ 通 chia thành 通う (かよう: đi lại) hoặc 通る (とおる), không đọc là むかえる.",
            "送え: Chữ 送 đọc là おくる ('tiễn/gửi'), âm cũng sai và nghĩa ngược hoàn toàn với 'ra đón'.",
            "追え: Chữ 追 đọc là おう ('đuổi theo'), không ghép đuôi え cho むかえ.",
            "迎え (むかえ): ĐÚNG. Danh từ từ Vます của 迎える, đứng trước に来てくれた.",
        ],
    },
    # ID=7
    "032c9817af81af397e45e3f3a55596dd49cc57e37180f16c3f4cac642165403e": {
        "links": [
            {"grammar_code": "GP-N5-03", "role": "sentence_structure", "note_vi": "Trợ từ に đánh dấu nơi lưu dấu kết quả của tha động từ 残す (để lại ở đâu)."},
            {"grammar_code": "GP-N5-18", "role": "sentence_structure", "note_vi": "Tha động từ 残す (để lại thứ gì vào đâu: N1にN2を残す) đối cặp với tự động từ 残る."},
        ],
        "structure_parse_vi": (
            "[留守番電話に] (đích lưu kết quả hành động với に - GP-N5-03) + tân ngữ [メッセージを] + tha động từ quá khứ [残した]."
        ),
        "pedagogical_takeaway_vi": "Tha động từ kết quả như 残す (để lại), 書く (viết lên), 置く (đặt lên) đánh dấu điểm tiếp nhận bằng trợ từ に.",
        "option_grammar_notes": [
            "インタビュー: Cuộc phỏng vấn — không kết hợp tự nhiên với việc để lại trên hộp thư thoại.",
            "マッサージ: Xoa bóp — vật lý không thể để lại trong hộp thư thoại.",
            "アナウンス: Thông báo phát thanh — thường dùng với 流す/聞く/する chứ không 'để lại' trên máy trả lời.",
            "メッセージ: ĐÚNG. Kết hợp tự nhiên cố định: 留守番電話にメッセージを残す.",
        ],
    },
    # ID=8
    "18bf1210a4e1c524b97f28d24cfc2795e6a809db83435283186119510fbed7d2": {
        "links": [
            {"grammar_code": "GP-N5-10", "role": "sentence_structure", "note_vi": "Câu yêu cầu lịch sự tại cửa hàng dùng Vて + ください (つつんでください)."},
            {"grammar_code": "GP-N5-02", "role": "sentence_structure", "note_vi": "Trợ từ は thay thế を để nhấn mạnh và đối chiếu hai món hàng [チョコレートとクッキーは]."},
        ],
        "structure_parse_vi": (
            "Lời đề nghị trực tiếp: [チョコレートとクッキーは] (đối tượng được nâng làm chủ đề bằng は) "
            "+ phó từ cách thức [べつべつに] + yêu cầu [つつんでください] (GP-N5-10)."
        ),
        "pedagogical_takeaway_vi": "Các phó từ cách thức như 別々に (tách riêng), 一緒に (cùng nhau), 丁寧に (cẩn thận) bổ nghĩa ngay trước động từ yêu cầu.",
        "option_grammar_notes": [
            "べつべつに: ĐÚNG. Phó từ chỉ cách thức tách riêng bổ nghĩa trực tiếp cho động từ 包む (gói).",
            "たがいに: Nghĩa 'lẫn nhau' đòi hỏi chủ thể đối ứng hai người, không hợp hành động nhân viên gói bánh.",
            "ただ: Mang nghĩa 'chỉ' hoặc 'miễn phí', không ăn khớp cấu trúc yêu cầu gói riêng 2 loại.",
            "どんなに: Phó từ nghi vấn đòi hỏi hô ứng ～ても / ～だろう, vô nghĩa trước つつんでください.",
        ],
    },
    # ID=9
    "0398e489df185d30458e4ba8983a98a35dd7ee9c7ee55e078d41ef5033754f8e": {
        "links": [
            {"grammar_code": "GP-N3-024", "role": "sentence_structure", "note_vi": "Khung hô ứng [どんなに + Vても]: dù có cố gắng đến mức độ nào đi nữa."},
            {"grammar_code": "GP-N4-01", "role": "sentence_structure", "note_vi": "Thể khả năng phủ định 勝てない (không thể thắng nổi người đó - Nには + V khả năng)."},
        ],
        "structure_parse_vi": (
            "Vế nhượng bộ mức độ [どんなに + 頑張っても] (dù cố đến mấy - GP-N3-024) "
            "-> vế kết quả bất lực [あの人には + 勝てない] (không thể thắng nổi người đó - GP-N4-01)."
        ),
        "pedagogical_takeaway_vi": "Hễ thấy Vても phía sau và kết quả phủ định bất lực ở cuối câu -> chọn phó từ hô ứng どんなに (hoặc いくら).",
        "option_grammar_notes": [
            "どんなに: ĐÚNG. Hô ứng trực tiếp với thể nhượng bộ 頑張っても để nhấn mạnh mức độ cao nhất.",
            "どうしても: Nghĩa 'dù thế nào cũng' thường ghép thẳng với phủ định (どうしても勝てない), không ghép trực tiếp trước 頑張っても.",
            "べつに: Phó từ phủ định ('chẳng có gì đặc biệt'), buộc đi liền phủ định nhẹ (~ない).",
            "たった: Chỉ số lượng ít ('chỉ vỏn vẹn 1 phút'), sai hoàn toàn với 頑張っても.",
        ],
    },
    # ID=10
    "aaf045c1a11911ebbcaa1b782fee8291e914aa24be180fc662a937618a37fc21": {
        "links": [
            {"grammar_code": "GP-N5-02", "role": "sentence_structure", "note_vi": "Khung tha động từ truyền tin: [N1(nội dung)を] + [N2(đối tượng tiếp nhận)に] + 知らせる."},
            {"grammar_code": "GP-N5-03", "role": "sentence_structure", "note_vi": "Trợ từ に đánh dấu đối tượng nhận thông báo."},
        ],
        "structure_parse_vi": (
            "Tân ngữ thông tin [新しいスケジュールを] + đối tượng tiếp nhận [会のメンバーに] (GP-N5-03) + động từ truyền đạt quá khứ [知らせた]."
        ),
        "pedagogical_takeaway_vi": "Động từ 知らせる (thông báo cho ai việc gì) nhận cặp trợ từ kép: [Người nhận に] + [Nội dung を].",
        "option_grammar_notes": [
            "会員 (かいいん): ĐÚNG. Đồng nghĩa với メンバー (thành viên trong hội).",
            "会長 (かいちょう): Chỉ 1 người đứng đầu hội ('hội trưởng'), không đồng nghĩa tập thể メンバー.",
            "新会員: Thu hẹp sai đối tượng thành 'thành viên mới'.",
            "リーダー: Chỉ trưởng nhóm/người dẫn dắt, sai nghĩa メンバー.",
        ],
    },
    # ID=11
    "3db5b6dee06efaac2e003a8ceb3118691a8414b12ddc09064bbf23843e168576": {
        "links": [
            {"grammar_code": "GP-N5-15", "role": "discourse_marker", "note_vi": "Liên kết cảm thán tiếc nuối ～のに kết thúc câu một (もうちょっとだったのに)."},
            {"grammar_code": "GP-N5-05", "role": "sentence_structure", "note_vi": "Tính từ đuôi な + だ + ね thể hiện sự đồng cảm."},
        ],
        "structure_parse_vi": (
            "Câu cảm thán bỏ lửng với のに [もうちょっとだったのに] (chỉ thêm chút nữa thôi mà...) -> nhận xét tiếc nuối [おしかったね] (= 残念だったね)."
        ),
        "pedagogical_takeaway_vi": "Đuôi ～のに đứng cuối câu cảm thán luôn kéo theo tâm trạng tiếc nuối hoặc bất mãn.",
        "option_grammar_notes": [
            "びっくりした: Diễn tả giật mình bất ngờ, không đồng nghĩa sát với 'tiếc nuối vì thiếu một chút nữa'.",
            "あぶなかった: Nghĩa 'suýt nguy hiểm', lệch hẳn sắc thái tiếc nuối.",
            "残念だ: ĐÚNG. Đồng nghĩa chính xác với 惜しい (đáng tiếc khi vuột mất sát nút).",
            "だめだ: Nghĩa 'hỏng rồi/không được rồi', không mang cảm xúc nuối tiếc cụ thể của 惜しい.",
        ],
    },
    # ID=12
    "7f9d69f8c32baf46ee2a2b6a634137e3844bdc789f4a1fb024ccf6ff53efc978": {
        "links": [
            {"grammar_code": "GP-N3-107", "role": "sentence_structure", "note_vi": "Dạng phủ định trạng ngữ cổ V(ない) + ず (残らず = 残らないで: không chừa lại chút nào)."},
            {"grammar_code": "GP-N5-18", "role": "sentence_structure", "note_vi": "Tha động từ 片付けた đi với chủ đề tân ngữ 今日の仕事は."},
        ],
        "structure_parse_vi": (
            "[今日の仕事は] (tân ngữ được đưa làm chủ đề) + phó từ phủ định triệt để [残らず] (không để sót lại chút nào - GP-N3-107) + tha động từ [片付けた]."
        ),
        "pedagogical_takeaway_vi": "Đuôi ～ず ở giữa câu bổ nghĩa cho động từ sau mang nghĩa 'mà không làm V' (残らず = không chừa lại = toàn bộ 100%).",
        "option_grammar_notes": [
            "全部 (ぜんぶ): ĐÚNG. Tương đương tuyệt đối 100% với 残らず ('không sót chút nào').",
            "大部分: Chỉ 'phần lớn' (< 100%), không tương đương 残らず.",
            "だいたい: Chỉ 'đại khái/khoảng chừng', thiếu tính triệt để.",
            "一部: Chỉ 'một phần', trái hoàn toàn mức độ trọn vẹn.",
        ],
    },
    # ID=13
    "46632a6be0a75651a40b44c2f3798bec82b29536649b83948cf0703b0902cb99": {
        "links": [
            {"grammar_code": "GP-N4-20", "role": "sentence_structure", "note_vi": "Thể khả năng 眠れる + そうだ (眠れそうだ): có vẻ sẽ ngủ được ngon."},
            {"grammar_code": "GP-N5-13", "role": "sentence_structure", "note_vi": "Mệnh đề nguyên nhân 今日は疲れているので (vì hôm nay mệt) giải thích lý do dẫn tới giấc ngủ sâu."},
            {"grammar_code": "GP-N5-04", "role": "sentence_structure", "note_vi": "Trợ từ giới hạn thời gian 朝まで (cho đến tận sáng)."},
        ],
        "structure_parse_vi": (
            "Ở câu đúng (Option 3): nguyên nhân trạng thái [今日は疲れているので] (GP-N5-08 + GP-N5-13) "
            "-> giới hạn thời gian [朝まで] (GP-N5-04) + trạng thái [ぐっすり] + dự đoán [眠れそうだ] (GP-N4-01 + GP-N4-20)."
        ),
        "pedagogical_takeaway_vi": "Phó từ tượng hình ぐっすり bị ràng buộc chọn lựa động từ cực chặt: chỉ đi với 眠る / 寝る (ngủ say).",
        "option_grammar_notes": [
            "Sentence 1: Đưa ぐっすり vào trước 食べてください sai ngữ nghĩa (cần たっぷり / たくさん).",
            "Sentence 2: Đưa ぐっすり vào trước 練習した sai kết hợp động từ (cần しっかり).",
            "Sentence 3: ĐÚNG. Kết hợp chuẩn ぐっすり + 眠れそうだ sau mệnh đề nguyên nhân 疲れているので.",
            "Sentence 4: Đưa ぐっすり vào trước おしゃべりした sai động từ (chỉ dùng cho ngủ).",
        ],
    },
    # ID=14
    "07af48e27447c3a844ab2ce5af797fc535dc156bafa2c4076db8ac2b0c498438": {
        "links": [
            {"grammar_code": "GP-N5-08", "role": "sentence_structure", "note_vi": "Trạng thái sở hữu hiện tại 持っている kết hợp chủ thể 家族それぞれが."},
            {"grammar_code": "GP-N5-02", "role": "sentence_structure", "note_vi": "Trợ từ が sau 家族それぞれ đánh dấu từng thành viên đều sở hữu laptop riêng."},
        ],
        "structure_parse_vi": (
            "Ở câu đúng (Option 4): [家は] (đại diện phạm vi gia đình) + [家族それぞれが] (mỗi thành viên trong gia đình) "
            "+ [ノートパソコンを持っている] (trạng thái sở hữu - GP-N5-08)."
        ),
        "pedagogical_takeaway_vi": "それぞれ có chức năng đại từ/phó từ chỉ 'mỗi cá nhân riêng biệt' (không làm tính từ な ở *それぞれな気持ち).",
        "option_grammar_notes": [
            "Sentence 1: Ép それぞれ làm tính từ đuôi な (*それぞれな気持ち) — sai loại từ (cần 複雑な).",
            "Sentence 2: Thiếu hình thái bổ nghĩa phủ định hợp lý cho 感じない (cần そうは感じない).",
            "Sentence 3: Bẫy âm tương tự giữa それぞれ và そろそろ ('sắp sửa/đã đến lúc bắt đầu họp').",
            "Sentence 4: ĐÚNG. 家族それぞれが làm chủ ngữ tự nhiên cho 持っている.",
        ],
    },
    # ID=35
    "031e8ef432e375f3ebc885f83c1be6c1074345ca85b5281715a8f8c4ae653379": {
        "links": [
            {"grammar_code": "GP-N5-06", "role": "sentence_structure", "note_vi": "Chuỗi định ngữ ghép hai danh từ [新しい型] + の + [パソコン]."},
        ],
        "structure_parse_vi": (
            "Định ngữ [新しい型の] (tính từ い + danh từ + の bổ cho danh từ sau) + tân ngữ [パソコンを] + hành động quá khứ [買った]."
        ),
        "pedagogical_takeaway_vi": "Khi đứng một mình làm danh từ độc lập sau 新しい～の, chữ 型 đọc thuần là かた (không biến âm thành がた như hậu tố 最新型).",
        "option_grammar_notes": [
            "かたち: Cách đọc của chữ 形 (hình dáng), không dùng cho chữ 型 (kiểu mẫu/đời máy).",
            "けい: Âm On chỉ dùng trong từ ghép Hán-Nhật (例: 模型 もけい, 小型 こがた).",
            "かた: ĐÚNG. Cách đọc độc lập chuẩn của 型 (đời/mẫu mới).",
            "がた: Chỉ biến âm sang đục âm khi gắn làm hậu tố sau chữ khác (例: 最新型).",
        ],
    },
    # ID=36
    "cadb97caa5815655bb29c0f22ddacdf55dd33fa885a4539334115dccfd8c164a": {
        "links": [
            {"grammar_code": "GP-N5-02", "role": "sentence_structure", "note_vi": "Khung kinh điển [N1 は] + [N2 が] + [Tính từ]: Chủ đề Tokyo có thuộc tính Vật giá đắt."},
        ],
        "structure_parse_vi": (
            "[東京は] (chủ đề địa điểm tổng thể は) + [物価が] (chủ thể hẹp mang tính chất が) + [高いです] (tính từ đuôi い lịch sự)."
        ),
        "pedagogical_takeaway_vi": "Mô hình [Địa điểm は + Thuộc tính が + Tính từ] giúp phân định rõ chủ đề rộng (Tokyo) và yếu tố được đánh giá (Vật giá).",
        "option_grammar_notes": [
            "ぶつか: Bẫy không biến âm xúc âm っ khi chữ ghép bắt đầu bằng hàng か.",
            "ぶっか (物価): ĐÚNG. ぶつ + か -> biến âm ぶっか.",
            "ものか: Bẫy ghép âm Kun của 物 (もの) với âm On của 価.",
            "ものが: Đọc sai cả hai chữ, không tồn tại từ vựng ものが chỉ vật giá.",
        ],
    },
    # ID=37
    "1c55c22afcc6fe19e2448619ac01793d96de74ab1f55d1a643303cc829303025": {
        "links": [
            {"grammar_code": "GP-N3-026", "role": "sentence_structure", "note_vi": "Cụm kết câu ～と言われている (được cho rằng, người ta nói rằng...)."},
            {"grammar_code": "GP-N5-02", "role": "sentence_structure", "note_vi": "Chủ đề 現代は + vị ngữ danh từ 情報の時代だ trích dẫn trước と."},
        ],
        "structure_parse_vi": (
            "[現代は] (chủ đề thời đại) + vị ngữ danh từ [情報の時代だ] -> trích dẫn khách quan chung [と言われている] (GP-N3-026)."
        ),
        "pedagogical_takeaway_vi": "Cấu trúc Mệnh đề + と言われている luôn giữ dạng thể thường (ví dụ 時代だ) ngay trước trợ từ と.",
        "option_grammar_notes": [
            "じだい (時代): ĐÚNG. Nghĩa 'thời đại' khớp với cụm 情報の時代だ.",
            "しだい (次第): Bẫy thiếu âm đục; 次第 đọc là しだい mang nghĩa 'tùy thuộc' hoặc 'ngay sau khi'.",
            "げんだい (現代): Bẫy đọc nhầm chữ 現代 ở đầu câu thay vì chữ 時代 trong ngoặc.",
            "げんたい: Đọc nhầm chữ đầu câu và sai âm đục chữ 代.",
        ],
    },
    # ID=38
    "667b035ecf4fa8e91d656eddb140d606e0563aea3363346c9c64569fd89d5db9": {
        "links": [
            {"grammar_code": "GP-N5-02", "role": "sentence_structure", "note_vi": "Khung [N1は] + [N2の + N3が] + [悪い]: học sinh kia có thái độ trong giờ học kém."},
        ],
        "structure_parse_vi": (
            "[あの学生は]、(chủ đề người) + cụm thuộc tính [授業の + たいどが] + tính từ đánh giá [悪い]."
        ),
        "pedagogical_takeaway_vi": "Nhận diện bộ phận trong câu [N1は + N2のN3が + 良い/悪い] giúp khoanh vùng danh từ chỉ tính chất/tác phong của N1.",
        "option_grammar_notes": [
            "態度 (たいど): ĐÚNG. Chữ 態 (có bộ Tâm 心) + 度 (bộ Nghiễm 广) = thái độ.",
            "能度: Nhầm 態 với 能 (năng lực 能力).",
            "態渡: Nhầm 度 với 渡 (băng qua 渡る).",
            "能渡: Sai cả hai chữ Hán.",
        ],
    },
    # ID=39
    "e9d98aaf75fc2d7373254768c43219448ac4fc59944028776eb23a785117ce21": {
        "links": [
            {"grammar_code": "GP-N5-08", "role": "sentence_structure", "note_vi": "Lưu ý phủ định đặc biệt của 知る: luôn là 知らない (tuyệt đối không chia *知っていない!)."},
            {"grammar_code": "GP-N5-02", "role": "sentence_structure", "note_vi": "Cấu trúc Nは + Nを + 知らない."},
        ],
        "structure_parse_vi": (
            "[あの人は] (chủ ngữ) + tân ngữ [れいぎを] + phủ định hiểu biết [知らない] (không biết phép tắc lịch sự)."
        ),
        "pedagogical_takeaway_vi": "Động từ 知る (biết): khẳng định chia 知っている, nhưng phủ định ở hiện tại bắt buộc chia 知らない (luật N5 hay bẫy ở N4-N3).",
        "option_grammar_notes": [
            "礼義: Nhầm chữ 儀 (nghi thức, có bộ Nhân 亻) với chữ 義 (chính nghĩa).",
            "祈義: Nhầm cả hai chữ Hán (祈 là cầu nguyện).",
            "礼儀 (れいぎ): ĐÚNG. Lễ nghi, phép lịch sự.",
            "祈儀: Nhầm chữ 礼 (lễ) với 祈 (kỳ - cầu nguyện).",
        ],
    },
    # ID=40
    "830347e2fd141307f596a5d293414d09c6e6ad2626f3605a60139cf7a497ae06": {
        "links": [
            {"grammar_code": "GP-N5-02", "role": "sentence_structure", "note_vi": "Cấu trúc sở hữu/tồn tại vấn đề: [N1の + N2が + ある] (có lời phàn nàn về...)."},
        ],
        "structure_parse_vi": (
            "[給料の] (bổ ngữ chỉ nội dung đối tượng về tiền lương) + [もんくが + ある] (tồn tại sự phàn nàn - GP-N5-02)."
        ),
        "pedagogical_takeaway_vi": "Cụm từ cố định 文句がある / 文句を言う dùng để diễn đạt sự than phiền đối với đối tượng gắn trước bởi trợ từ の hoặc に.",
        "option_grammar_notes": [
            "文化 (ぶんか): Nghĩa 'văn hóa', không đọc là もんく và sai nghĩa câu.",
            "文勺: Bẫy tự dạng cực hiểm — 勺 (thược) thiếu nét chữ 口 ở trong so với 句 (cú).",
            "交句: Nhầm chữ 文 với chữ 交 (giao lưu).",
            "文句 (もんく): ĐÚNG. Lời phàn nàn về tiền lương.",
        ],
    },
    # ID=41
    "57de04dd67b23fac636deb297c0f1cba20e9285bfce11f32cd440a7832dfd00b": {
        "links": [
            {"grammar_code": "GP-N5-18", "role": "sentence_structure", "note_vi": "Phân biệt Tự động từ (男女が + 混ざる) vs Tha động từ (～を + 混ぜる)."},
            {"grammar_code": "GP-N5-01", "role": "sentence_structure", "note_vi": "Chia thể て nối hành động (混ざって + サッカーをした): cùng hòa chung chơi bóng đá."},
        ],
        "structure_parse_vi": (
            "[男女が] (chủ ngữ gắn trợ từ が) + tự động từ thể て [まざって] (hòa lẫn vào nhau - GP-N5-18) + hành động chính [サッカーをした]."
        ),
        "pedagogical_takeaway_vi": "Chỉ cần nhìn chữ が ngay trước chỗ trống (男女が) là loại ngay tha động từ まぜて (đòi hỏi を) và つけて.",
        "option_grammar_notes": [
            "まぜて: Tha động từ (混ぜる) bắt buộc đi với を (例: AとBを混ぜる), sai trợ từ khi đứng sau 男女が.",
            "まざって: ĐÚNG. Tự động từ (混ざる) hợp khớp hoàn toàn với trợ từ chủ ngữ が.",
            "ついて: Không diễn đạt nghĩa nam nữ cùng hòa chung chơi bóng.",
            "つけて: Tha động từ ('gắn vào/bật lên'), sai cả nghĩa lẫn trợ từ.",
        ],
    },
    # ID=42
    "d92c869d0e208e9df9b0484a9c6e7ee674ab339614f51d87ddc4ec29a577913e": {
        "links": [
            {"grammar_code": "GP-N4-21", "role": "sentence_structure", "note_vi": "Cụm Vた + ところを (ngay khoảnh khắc vừa mới... thì bị bắt quả tang)."},
            {"grammar_code": "GP-N4-03", "role": "sentence_structure", "note_vi": "Thể bị động 逮捕された (bị cảnh sát bắt giữ)."},
            {"grammar_code": "GP-N5-03", "role": "sentence_structure", "note_vi": "Mục đích di chuyển 金を取りに (đến để lấy tiền - Vます + に)."},
        ],
        "structure_parse_vi": (
            "[犯人は] + mục đích [金を取りに] (GP-N5-03) + thời điểm tức thì bị phát giác [現れた + ところを] (GP-N4-21) + bị động [逮捕された] (GP-N4-03)."
        ),
        "pedagogical_takeaway_vi": "Cấu trúc [Vた + ところを + 逮捕される / 見つかる] diễn tả việc bị bắt quả tang đúng lúc vừa hành động, đi cùng trợ từ を.",
        "option_grammar_notes": [
            "表れた: Đồng âm あらわれる nhưng dùng cho sự bộc lộ cảm xúc/thái độ trừu tượng.",
            "現れた: ĐÚNG. Chữ 現 dùng cho người hoặc vật hữu hình xuất hiện trước mặt.",
            "抜けた: Tự động từ 'rút ra/thoát ra', không khớp bối cảnh bắt quả tang lúc tới lấy tiền.",
            "解けた: Tự động từ 'được giải tỏa/tan ra', vô nghĩa với phạm nhân.",
        ],
    },
    # ID=43
    "c8fb7a91ad0de61335800b601ee2cda53d6da6f38a5f4c434793348069f4d7a6": {
        "links": [
            {"grammar_code": "GP-N5-05", "role": "sentence_structure", "note_vi": "Trạng ngữ tính từ đuôi な (簡単に + 話す) và liên kết thể て của する (省略して)."},
            {"grammar_code": "GP-N5-02", "role": "sentence_structure", "note_vi": "Tân ngữ 詳しい説明を nhận danh động từ nhóm 3 (～して)."},
        ],
        "structure_parse_vi": (
            "Vế hành động 1 [詳しい説明を + 省略して] (tân ngữ を + danh động từ chia thể て chỉ cách thức) "
            "-> vế 2 [簡単に + 話す] (nói một cách ngắn gọn - GP-N5-05)."
        ),
        "pedagogical_takeaway_vi": "Đứng giữa Nを và ～して chắc chắn là danh động từ nhóm 3 (する) tác động trực tiếp vào danh từ 'giải thích chi tiết'.",
        "option_grammar_notes": [
            "省略 (しょうりゃく): ĐÚNG. Kết hợp tự nhiên: 説明を省略する (lược bỏ giải thích).",
            "挑戦 (ちょうせん): Nghĩa 'thử thách', đi với trợ từ に (～に挑戦する), không nhận 説明を.",
            "合図 (あいず): 'Ra hiệu', thường đi với ～に合図する.",
            "勇気 (ゆうき): Danh từ 'dũng khí', không chia với して sau 説明を.",
        ],
    },
    # ID=44
    "7fdd4cd64b79ea7ceb619ce1795f66c4037fd5d77aa8311a739d73c54acd7d45": {
        "links": [
            {"grammar_code": "GP-N5-02", "role": "sentence_structure", "note_vi": "Mệnh đề nguyên nhân tồn tại sự việc わけがあって (vì có lý do nên...)."},
            {"grammar_code": "GP-N5-01", "role": "sentence_structure", "note_vi": "Thể て của ある (あって) nối lý do sang mệnh đề kết quả 日本へ来た."},
        ],
        "structure_parse_vi": (
            "Nguyên nhân [わけが + あって] (GP-N5-02 + GP-N5-01) -> hành động di chuyển hướng đích [日本へ + 来た] (GP-N5-03)."
        ),
        "pedagogical_takeaway_vi": "Cụm [わけがあって] / [事情があって] dùng thể て của ある để giải thích khéo nguyên nhân mà không muốn nêu chi tiết.",
        "option_grammar_notes": [
            "手段: 'Phương tiện/biện pháp', không đồng nghĩa với わけ (lý do).",
            "理由: ĐÚNG. Đồng nghĩa với danh từ わけ trong ngữ cảnh わけがあって.",
            "目的: 'Mục đích', khác với わけ (lý do gốc rễ).",
            "目標: 'Mục tiêu cần đạt', không thay thế わけ.",
        ],
    },
    # ID=45
    "ab20f56f82bdf25a76db837df3a8f65b649328a6f96e5523a1b9bccec9abb428": {
        "links": [
            {"grammar_code": "GP-N5-13", "role": "sentence_structure", "note_vi": "Mệnh đề nguyên nhân ～ので: giải thích lý do khách quan cho hành động thay đổi lịch trình."},
            {"grammar_code": "GP-N5-02", "role": "sentence_structure", "note_vi": "Tân ngữ 旅行の日程を đi kèm tha động từ 変更した."},
        ],
        "structure_parse_vi": (
            "Nguyên nhân khách quan [急な仕事が入った + ので] (GP-N5-13) -> hành động điều chỉnh [旅行の日程を + 変更した] (GP-N5-02)."
        ),
        "pedagogical_takeaway_vi": "Thấy khung [日程を変更する] trong câu giải thích bằng ので -> nghĩa chuẩn là dời lịch (ずらす), tránh nhầm với hủy hoàn toàn.",
        "option_grammar_notes": [
            "ずらした: ĐÚNG. 'Làm xê dịch/dời lịch trình', tương đương sát nghĩa nhất với 日程を変更する ở ngữ cảnh này.",
            "ひかえた: 'Kiềm chế, hạn chế làm gì', không khớp với 日程 (lịch trình).",
            "取り消した: 'Hủy bỏ hoàn toàn' (= 中止・キャンセル), quá mạnh so với 変更 (thay đổi/điều chỉnh).",
            "申し込んだ: 'Đăng ký', sai nghĩa thay đổi.",
        ],
    },
    # ID=46
    "9c7218708b0d8c483d0ec9ca7cf0e8d82f2cc4467b1c2dc2f197145be2a64f06": {
        "links": [
            {"grammar_code": "GP-N4-16", "role": "sentence_structure", "note_vi": "Điều kiện hoàn tất tuần tự Vたら (済んだら): sau khi việc xong thì hãy..."},
            {"grammar_code": "GP-N5-18", "role": "sentence_structure", "note_vi": "Tự động từ 済む đi kèm chủ ngữ 用事が."},
            {"grammar_code": "GP-N5-10", "role": "sentence_structure", "note_vi": "Yêu cầu 連絡してください nối ở vế sau của điều kiện たら."},
        ],
        "structure_parse_vi": (
            "Điều kiện thời điểm hoàn tất [用事が + 済んだら] (GP-N5-18 + GP-N4-16) -> yêu cầu hành động kế tiếp [連絡してください] (GP-N5-10)."
        ),
        "pedagogical_takeaway_vi": "Vế 1 có Nが済んだら và vế 2 là mệnh lệnh lịch sự てください -> điều kiện たら bắt buộc hoàn thành V1 rồi mới làm V2.",
        "option_grammar_notes": [
            "あったら: 'Nếu có việc' — không diễn tả việc đã xử lý xong.",
            "決まったら: 'Nếu được quyết định' — sai nghĩa hoàn tất công việc của 済む.",
            "終わったら: ĐÚNG. Đồng nghĩa trực tiếp với tự động từ 済む (kết thúc xong việc).",
            "始まったら: Trái nghĩa hoàn toàn ('nếu bắt đầu').",
        ],
    },
    # ID=47
    "edaed5a31b1f94d742ab89c5f88f136cf527e75795e53b5f36503502a8a9983b": {
        "links": [
            {"grammar_code": "GP-N5-08", "role": "sentence_structure", "note_vi": "Ở Option 1 có dạng tính trạng thái kết quả 似ている, trong khi Option 4 là yêu cầu tức thì てください."},
            {"grammar_code": "GP-N5-03", "role": "sentence_structure", "note_vi": "Trong Option 4: 会社に行く前に (trước khi đi làm) + 私の家に寄ってください (đích tạt qua + に)."},
            {"grammar_code": "GP-N5-10", "role": "sentence_structure", "note_vi": "Đề nghị lịch sự 寄ってください trên đường tới công ty."},
        ],
        "structure_parse_vi": (
            "Câu đúng (Option 4): mệnh đề thời điểm [会社に行く + 前に] (Vる + 前に) -> địa điểm ghé qua [私の家に + 寄ってください] (GP-N5-03 + GP-N5-10)."
        ),
        "pedagogical_takeaway_vi": "Động từ di chuyển ghé qua 寄る nhận trợ từ đích に (家に寄る) và khác hoàn toàn với 偏る (かたよる: thiên lệch) hay 似る (にる: giống).",
        "option_grammar_notes": [
            "Sentence 1: Dùng 寄っている thay cho 似ている ('giống bố mẹ') — sai động từ trạng thái.",
            "Sentence 2: Dùng 寄った trước 荷物 thay cho 送った ('bưu kiện đã gửi').",
            "Sentence 3: Bẫy âm gần giống giữa 寄る và 偏る (かたよった食事: ăn uống thiên lệch).",
            "Sentence 4: ĐÚNG. 私の家に寄ってください (hãy ghé qua nhà tôi).",
        ],
    },
    # ID=48
    "c2e088f7da0445297877c7a81ab6537aca7a554a3280b9fb0cc51f1b4196150f": {
        "links": [
            {"grammar_code": "GP-N5-05", "role": "sentence_structure", "note_vi": "Ở Option 1: ぴったりだ hoạt động như vị ngữ tính từ đuôi な đi cùng đối tượng に (私にぴったりだ)."},
            {"grammar_code": "GP-N4-16", "role": "sentence_structure", "note_vi": "Option 3 dùng điều kiện なら (nếu định học lên thì...) nhưng ghép sai phó từ."},
        ],
        "structure_parse_vi": (
            "Câu đúng (Option 1): chủ ngữ cụ thể [この黄色のセーターは] -> đối tượng phù hợp [私に] -> vị ngữ tính chất [ぴったりだ]."
        ),
        "pedagogical_takeaway_vi": "Phân biệt bộ 3 phó từ âm cuối ったり: ぴったり (vừa khít/hợp), ばったり (tình cờ đụng mặt), ぐったり (mệt lử).",
        "option_grammar_notes": [
            "Sentence 1: ĐÚNG. Nは + Người + にぴったりだ = vừa vặn/hợp với ai.",
            "Sentence 2: Tình cờ gặp bạn phải dùng ばったり会った.",
            "Sentence 3: Học hành nghiêm túc phải dùng しっかり勉強しなさい.",
            "Sentence 4: Nằm mệt rũ vì nóng phải dùng ぐったりしていた.",
        ],
    },
    # ID=69
    "34fdb0862a667928d647b129bb36ad8941a385945988a96f5aef29254f9789a3": {
        "links": [
            {"grammar_code": "GP-N5-08", "role": "sentence_structure", "note_vi": "Tự động từ + ている (並んでいる) diễn tả trạng thái tĩnh hiện tại (những quả táo đang xếp ngay ngắn)."},
            {"grammar_code": "GP-N5-18", "role": "sentence_structure", "note_vi": "Tự động từ 並ぶ đi với chủ ngữ が (りんごが), phân biệt với tha động từ 並べる."},
            {"grammar_code": "GP-N5-03", "role": "sentence_structure", "note_vi": "Vị trí tồn tại tĩnh 箱の中に nhận trợ từ に."},
        ],
        "structure_parse_vi": (
            "[りんごが] (chủ ngữ tự động từ GP-N5-18) + vị trí tĩnh [箱の中に] (GP-N5-03) + trạng thái kết quả [並んでいる] (GP-N5-08)."
        ),
        "pedagogical_takeaway_vi": "Khi vật đứng trước が đang ở trạng thái tĩnh trong hộp/trên bàn với vị trí に -> dùng Tự động từ + ている.",
        "option_grammar_notes": [
            "つんで: Chữ 積 chia tự động từ là 積もる (つもる), còn つんで (積んで) là tha động từ nên không đi sau りんごが.",
            "ならんで (並んで): ĐÚNG. Tự động từ 並ぶ đi với りんごが + 箱の中に.",
            "つつんで: Tha động từ 包む (gói), sai trợ từ khi đứng sau りんごが.",
            "しずんで: Tự động từ 沈む (chìm), vô nghĩa với táo trong hộp.",
        ],
    },
    # ID=70
    "bb61b183c8d546f024904bbc49afc6c70ccc14ef4403d35e15db3e989b118aec": {
        "links": [
            {"grammar_code": "GP-N5-05", "role": "sentence_structure", "note_vi": "Tính từ đuôi な chia thể て (無事で) nối nguyên nhân trực tiếp tới cảm xúc an tâm (安心しました)."},
            {"grammar_code": "GP-N5-02", "role": "sentence_structure", "note_vi": "Chủ ngữ trong mệnh đề nguyên nhân nhận trợ từ が (あの人が)."},
        ],
        "structure_parse_vi": (
            "Mệnh đề nguyên nhân [あの人が + 無事で] (chủ ngữ が + Aな thể て - GP-N5-05) -> trạng thái tâm lý kết quả [本当に安心しました]."
        ),
        "pedagogical_takeaway_vi": "Thể て của danh từ/tính từ な (N/Aな + で) đứng giữa câu trước động từ cảm xúc (安心する / よかった) luôn chỉ nguyên nhân.",
        "option_grammar_notes": [
            "むし: Đọc nhầm chữ 無 thành む (chữ này đọc む trong 無理 hay 無視, không ghép với 事).",
            "むじ: Sai âm đầu chữ 無 (ở đây không đọc là む; đọc là ぶ mới đúng).",
            "ぶし: Sai âm đục ở chữ 事 (đọc ぶし dễ nhầm với 武士 - võ sĩ).",
            "ぶじ (無事): ĐÚNG. Chữ 無 đọc biến thành ぶ + 事 (じ).",
        ],
    },
    # ID=71
    "0d3d9fce05e0fe6488cca8c0cdebbedb7bc0cf3e02183e6b405597ddfebc2da6": {
        "links": [
            {"grammar_code": "GP-N5-03", "role": "sentence_structure", "note_vi": "Trợ từ に đánh dấu thời điểm hoặc cách thức thời gian (同時に) đi kèm tự động từ 起こった."},
            {"grammar_code": "GP-N5-18", "role": "sentence_structure", "note_vi": "Tự động từ 起こる đi với chủ ngữ 事件が."},
        ],
        "structure_parse_vi": (
            "[2つの事件が] (chủ ngữ tự động từ) + thời điểm đồng nhất [同時に] (GP-N5-03) + động từ xảy ra [起こった]."
        ),
        "pedagogical_takeaway_vi": "Phân biệt chắc chắn cặp đồng âm/gần âm thời gian: 同時 (どうじ: cùng lúc) vs 当時 (とうじ: vào thời đó).",
        "option_grammar_notes": [
            "とうじ: Bẫy thiếu tenten — 当時 đọc là とうじ ('vào hồi đó'), không phải 同時.",
            "どうじ (同時): ĐÚNG. 同 đọc là どう + 時 là じ.",
            "とうき: Âm đọc của 冬季 (mùa đông) hoặc 陶器 (đồ gốm).",
            "どうき: Âm đọc của 動機 (động cơ) hoặc 同期 (cùng khóa).",
        ],
    },
    # ID=72
    "01478c528c78b91be73bb4667f85cf1365a44b40f7d3f679deccdf4fa2fe40e7": {
        "links": [
            {"grammar_code": "GP-N5-08", "role": "sentence_structure", "note_vi": "Động từ trạng thái cố hữu bắt buộc chia ている ở hiện tại: 似ている (giống với ai)."},
            {"grammar_code": "GP-N5-03", "role": "sentence_structure", "note_vi": "Đối tượng so sánh/tương đồng nhận trợ từ に (父に似ている)."},
        ],
        "structure_parse_vi": (
            "[彼は]、(chủ đề) + đối tượng so sánh [私の父に] (GP-N5-03) + động từ trạng thái ngoại hình/tính cách [似ています] (GP-N5-08)."
        ),
        "pedagogical_takeaway_vi": "Động từ nhóm trạng thái (似ている giống, 優れている vượt trội, 変わっている kỳ lạ) hầu như luôn dùng dạng Vている với trợ từ に.",
        "option_grammar_notes": [
            "にて (似て): ĐÚNG. Thể て của động từ nhóm 2 似る (にる).",
            "みて: Chữ 見 (nhìn), không đi với mẫu AはBに～ている.",
            "して: Thể て của する, không ghép Kanji 似.",
            "きて: Thể て của 来る/着る, sai mặt chữ 似.",
        ],
    },
    # ID=73
    "8fe5b63b3378c068435560bde093c3c02ef7198df26a623695cc77f3a6841157": {
        "links": [
            {"grammar_code": "GP-N5-12", "role": "sentence_structure", "note_vi": "Cấu trúc cho nhận cơ bản [Người nói は] + [Người tặng から/に] + [Vật を] + もらう."},
        ],
        "structure_parse_vi": (
            "Nguồn cho [友だちから] (GP-N5-12) + tân ngữ quà tặng [コンサートの + 券を] + động từ tiếp nhận [もらいました]."
        ),
        "pedagogical_takeaway_vi": "Khi nhận vật cụ thể từ bạn bè với từ khóa ～からもらいました, vị trí trống đứng trước を là danh từ đồ vật (券 = けん).",
        "option_grammar_notes": [
            "かん: Bẫy chữ 巻 (cuộn/tập) hoặc 缶 (lon) đọc かん; chữ 券 có bộ Đao 刀 bên dưới phải đọc là けん.",
            "がん: Đọc sai thanh đục.",
            "けん (券): ĐÚNG. Vé, phiếu (乗車券, 商品券).",
            "げん: Bẫy thanh đục.",
        ],
    },
    # ID=74
    "090803d0e17475f827fbd2fe42a55ef378dc87085730750fc7047efffa9c5118": {
        "links": [
            {"grammar_code": "GP-N5-05", "role": "sentence_structure", "note_vi": "Tính từ đuôi な giữ nguyên な bổ nghĩa cho danh từ 性格 (素直な性格だ)."},
        ],
        "structure_parse_vi": (
            "[彼女は] (chủ đề) + định ngữ tính từ な [素直な] + danh từ vị ngữ [性格だ] (GP-N5-05)."
        ),
        "pedagogical_takeaway_vi": "Chữ 素直 vừa đọc đặc biệt (すなお) vừa là tính từ đuôi な (bổ nghĩa danh từ bằng な).",
        "option_grammar_notes": [
            "そっちょく: Bẫy đồng nghĩa 率直 (thẳng thắn), không phải âm của 素直.",
            "しょうじき: Bẫy đồng nghĩa 正直 (thật thà), sai Kanji.",
            "すなお (素直): ĐÚNG. Tính từ な mang nghĩa ngoan ngoãn, hiền lành.",
            "まっすぐ: Bẫy từ gần nghĩa 真っ直ぐ (thẳng tắp).",
        ],
    },
    # ID=75
    "d10e2785896e58dd5988e34b98250a9b2ed748982d341d22824b0de68d7856b8": {
        "links": [
            {"grammar_code": "GP-N4-07", "role": "sentence_structure", "note_vi": "Động từ ghép hướng về người nói 持ってくる (mang lại đây)."},
            {"grammar_code": "GP-N5-10", "role": "sentence_structure", "note_vi": "Câu cầu khiến lịch sự Vてください (持ってきてください)."},
            {"grammar_code": "GP-N5-03", "role": "sentence_structure", "note_vi": "Đích di chuyển ここに gắn với trợ từ に."},
        ],
        "structure_parse_vi": (
            "Đích đến [ここに] (GP-N5-03) + tân ngữ [机を] + động từ ghép hướng về phía người nói ở dạng yêu cầu [持ってきてください] (GP-N4-07 + GP-N5-10)."
        ),
        "pedagogical_takeaway_vi": "Phân biệt từ đơn thuần Nhật chỉ đồ nội thất: 机 (つくえ bàn) vs 棚 (たな kệ) vs 台 (だい bệ).",
        "option_grammar_notes": [
            "だい: Cách đọc của chữ 台 (cái bệ/đài).",
            "つくえ (机): ĐÚNG. Cái bàn học/bàn làm việc.",
            "たな: Cách đọc của chữ 棚 (cái kệ/giá).",
            "はこ: Cách đọc của chữ 箱 (cái hộp).",
        ],
    },
    # ID=76
    "a0ae64af2ed84054799aa579de0f7a71bbaa297944cfc0902380c00fbe37598a": {
        "links": [
            {"grammar_code": "GP-N5-10", "role": "sentence_structure", "note_vi": "Cụm 休まないで (Vないで: mà không nghỉ) diễn tả trạng thái kèm theo hành động chính."},
            {"grammar_code": "GP-N5-08", "role": "sentence_structure", "note_vi": "Thể tiếp diễn lặp lại thói quen/vận hành 営業している."},
        ],
        "structure_parse_vi": (
            "[この店は]、+ khoảng thời gian liên tục [1年中] + trạng thái kèm theo [休まないで] (GP-N5-10) + thói quen vận hành [営業している] (GP-N5-08)."
        ),
        "pedagogical_takeaway_vi": "Khung [～ないで + Vている] chỉ việc duy trì một hoạt động kinh doanh mà không thực hiện V1 (mở cửa suốt năm không nghỉ).",
        "option_grammar_notes": [
            "こうぎょう: Âm đọc của 工業 (công nghiệp), không hợp bối cảnh cửa hàng mở bán.",
            "えいぎょう (営業): ĐÚNG. Mở cửa kinh doanh phục vụ khách hàng.",
            "そうぎょう: Âm đọc của 創業 (khởi nghiệp) / 操業 (vận hành máy móc nhà máy).",
            "かいぎょう: Âm đọc của 開業 (khai trương mới), mâu thuẫn với 1年中休まないで.",
        ],
    },
    # ID=77
    "b9cc725539248b280db613276835407f5a8d4b36eebe9a082b202692021909a1": {
        "links": [
            {"grammar_code": "GP-N5-05", "role": "sentence_structure", "note_vi": "Tính từ đuôi な thêm に làm trạng ngữ bổ nghĩa cho động từ (幸福に生活する)."},
            {"grammar_code": "GP-N5-08", "role": "sentence_structure", "note_vi": "Quá khứ tiếp diễn 生活していた miêu tả quãng đời sinh sống êm đềm."},
        ],
        "structure_parse_vi": (
            "[彼女は]、(chủ đề) + trạng ngữ tính chất [幸福 + に] (GP-N5-05) + động từ quá khứ tiếp diễn [生活していた] (GP-N5-08)."
        ),
        "pedagogical_takeaway_vi": "Vị trí ngay trước động từ nối bằng に (～に生活する) yêu cầu Tính từ đuôi な (như 幸福, 幸せ) làm trạng từ.",
        "option_grammar_notes": [
            "幸復: Nhầm chữ 福 (phúc lành, bộ Thị 礻) với chữ 復 (khôi phục, bộ Sách 彳).",
            "広復: Sai cả hai chữ Hán (広 là rộng, 復 là lặp lại).",
            "幸福 (こうふく): ĐÚNG. Chữ 幸 + chữ 福 có bộ Thị 礻.",
            "広福: Nhầm chữ 幸 (hạnh) với chữ 広 (quảng - rộng).",
        ],
    },
    # ID=78
    "999fa34eb5920aabc457fd3869ab8206b1ed7f590f18e4b20481f91d9256905a": {
        "links": [
            {"grammar_code": "GP-N5-02", "role": "sentence_structure", "note_vi": "Cấu trúc trực tiếp [Tân ngữ を + Danh động từ する]: 生活を改善する."},
        ],
        "structure_parse_vi": (
            "Tân ngữ chịu tác động cải thiện [生活を] (GP-N5-02) + động từ nhóm 3 [かいぜんする]."
        ),
        "pedagogical_takeaway_vi": "Phân biệt 4 từ ghép với 改 dựa vào tân ngữ đứng trước を: 生活を改善する (cải thiện) vs 法律を改正する (sửa luật) vs 家を改造する.",
        "option_grammar_notes": [
            "改正 (かいせい): Sửa đổi quy định, luật lệ, lịch tàu, không dùng cho 'đời sống'.",
            "改造 (かいぞう): Cải tạo kết cấu vật lý nhà cửa/xe cộ.",
            "改良 (かいりょう): Cải tiến chất lượng sản phẩm/giống cây.",
            "改善 (かいぜん): ĐÚNG. Khắc phục làm cho tốt hơn (dùng với 生活, 環境, 条件).",
        ],
    },
    # ID=79
    "b0137420afaf06ffd807f26d280a2c69fa03e5a91a2ad72626ee75c17250a7a0": {
        "links": [
            {"grammar_code": "GP-N5-03", "role": "sentence_structure", "note_vi": "Cụm định hướng không gian N + に + 沿って (đi dọc theo tuyến vật lý con sông)."},
            {"grammar_code": "GP-N5-01", "role": "sentence_structure", "note_vi": "Động từ nhóm 1 đuôi う biến âm thành って ở thể て (沿う -> 沿って)."},
        ],
        "structure_parse_vi": (
            "Tuyến địa lý [大きな川に] + động từ thể て chỉ phương hướng di chuyển [沿って] + hành động chính [歩く]."
        ),
        "pedagogical_takeaway_vi": "Gặp cặp [川 / 道 / 線路 + にそって], bắt buộc chọn chữ 沿 (bộ Thủy 氵: ven sông/dọc theo tuyến vật lý), tránh nhầm với 添 (kề bên/đáp ứng).",
        "option_grammar_notes": [
            "添って: Đồng âm そって nhưng dùng cho nghĩa trừu tượng ('đáp ứng kỳ vọng', 'nương tựa bên cạnh').",
            "沢って: Chữ 沢 (trạch - đầm) đọc là さわ, không chia với って.",
            "沿って: ĐÚNG. 沿う (そって) = đi dọc theo đường/sông.",
            "沼って: Chữ 沼 (chiểu - đầm lầy) đọc là ぬま, sai hoàn toàn.",
        ],
    },
    # ID=80
    "5ced0af3bc94261bb9469bac3448840207355ad55d5a2e50161509bae9989a42": {
        "links": [
            {"grammar_code": "GP-N5-06", "role": "sentence_structure", "note_vi": "Định ngữ ý muốn [家を買いたい] bổ nghĩa cho danh từ chỉ người [人]."},
            {"grammar_code": "GP-N5-11", "role": "sentence_structure", "note_vi": "Đuôi たい biểu đạt mong muốn thực hiện hành động (買いたい)."},
            {"grammar_code": "GP-N5-03", "role": "sentence_structure", "note_vi": "Đối tượng tiếp nhận tiền vay nhận trợ từ に (人に金を貸す)."},
        ],
        "structure_parse_vi": (
            "Định ngữ [家を買いたい + 人に] (người muốn mua nhà - GP-N5-06 + GP-N5-11 + GP-N5-03) "
            "+ tân ngữ [金を] + hành động cung cấp vay [かす]."
        ),
        "pedagogical_takeaway_vi": "Cụm [人に金を貸す] (cho ai vay tiền) ngược chiều trợ từ với [人にお金を借りる] (mượn tiền từ ai).",
        "option_grammar_notes": [
            "買す: Chữ 買 đọc là かう ('mua'), không có biến thể かす.",
            "貸す (かす): ĐÚNG. Cho vay, cho mượn.",
            "借す: Chữ 借 đọc là かりる ('đi vay'), không đi với đuôi す.",
            "課す: Đồng âm かす nhưng nghĩa 'giao nhiệm vụ/áp đặt thuế', không hợp cho người muốn mua nhà vay tiền.",
        ],
    },
    # ID=81
    "09c42bf7a383c25950928145ff02396b76879d35c8ebd3894490da5fd922fbcb": {
        "links": [
            {"grammar_code": "GP-N5-03", "role": "sentence_structure", "note_vi": "Cụm mốc khởi đầu ～を機会に (nhân dịp/lấy việc này làm cơ hội để thay đổi thói quen; mở rộng lên N2 là ～を契機に)."},
            {"grammar_code": "GP-N4-17", "role": "sentence_structure", "note_vi": "Ý chí dự định đang cân nhắc Vよう + と思う (やめようと思う)."},
        ],
        "structure_parse_vi": (
            "[これを + 機会に] (lấy việc này làm dịp khởi đầu - GP-N2-10) -> quyết tâm cá nhân [たばこを + やめようと思う] (GP-N4-17)."
        ),
        "pedagogical_takeaway_vi": "Nhớ liền tay mẫu [これを機会に + Vようと思う]: dùng 機 (cơ hội) + 会 (gặp dịp), đừng nhầm 期 (thời kỳ) hay 回 (số lần).",
        "option_grammar_notes": [
            "期回: Nhầm cả hai chữ Hán.",
            "期会: Nhầm chữ 機 (cơ hội) thành 期 (kỳ hạn).",
            "機回: Nhầm chữ 会 thành chữ 回 (lần).",
            "機会 (きかい): ĐÚNG. これを機会に = nhân cơ hội này.",
        ],
    },
    # ID=82
    "6480be20c3e2ea3bd2f255d10cdd4f5457c6336199bdc7e045f373cd77b54284": {
        "links": [
            {"grammar_code": "GP-N5-07", "role": "sentence_structure", "note_vi": "Danh từ hóa hành động Vること làm chủ ngữ đánh giá: [深く考える + こと + は大切だ]."},
            {"grammar_code": "GP-N5-05", "role": "sentence_structure", "note_vi": "Tính từ đuôi い chuyển dạng trạng từ く (深く + 考える): suy nghĩ một cách sâu sắc."},
        ],
        "structure_parse_vi": (
            "Cụm danh từ hóa chủ ngữ [物事を + 深く + 考えること + は] (GP-N5-05 + GP-N5-07) + vị ngữ đánh giá [大切だ]."
        ),
        "pedagogical_takeaway_vi": "Chủ ngữ kết thúc bằng Vる + ことは + 大切だ giúp tách tân ngữ đứng ngay đầu cụm là danh từ trừu tượng chỉ 'mọi sự vật, sự việc'.",
        "option_grammar_notes": [
            "物事 (ものごと): ĐÚNG. Mọi sự vật, sự việc trong đời sống.",
            "物言: Từ ghép là 物言い (ものいい: cách ăn nói/lời phản đối), không khớp 深く考える.",
            "物語 (ものがたり): Câu chuyện cổ tích/tiểu thuyết, đọc là ものがたり.",
            "物毎: Từ ghép không tồn tại.",
        ],
    },
    # ID=83
    "41c3b371d09d738a592bab6c627166284d642361ee6035627cc5445fc330e7c8": {
        "links": [
            {"grammar_code": "GP-N4-12", "role": "sentence_structure", "note_vi": "Cấu trúc mục đích N + のために (vì công việc mới nên mọi người cùng...)."},
            {"grammar_code": "GP-N5-02", "role": "sentence_structure", "note_vi": "Động từ ghép tương hỗ ～を出し合う (cùng nhau đưa ra/đóng góp lẫn nhau)."},
        ],
        "structure_parse_vi": (
            "Mục đích [新しい仕事のために] (GP-N4-12) -> chủ thể tập thể [みんなで] (cách thức nhóm で) + tân ngữ và động từ tương hỗ [アイデアを + 出し合った]."
        ),
        "pedagogical_takeaway_vi": "Động từ ghép Vます + 合う (出し合う, 話し合う, 助け合う) mang nghĩa 'cùng nhau trao đổi/tác động lẫn nhau', luôn đi kèm みんなで.",
        "option_grammar_notes": [
            "アプローチ: Sự tiếp cận (gần nghĩa phương thức) — không kết hợp tự nhiên với cụm 出し合う (cùng nhau đề xuất).",
            "シフト: Ca làm việc — không cùng nhau 'đưa ra' bằng 出し合う.",
            "アイデア: ĐÚNG. Cụm cố định: アイデアを出す / 出し合う (cùng nhau góp ý tưởng).",
            "カルチャー: Văn hóa — không phải thứ có thể 出し合う.",
        ],
    },
    # ID=84
    "75fe7eaf6ac00f3fce14f7cf60168ff4dd7840ebf1f9b18640ffda4d6e6e9c8e": {
        "links": [
            {"grammar_code": "GP-N4-12", "role": "sentence_structure", "note_vi": "Nguyên nhân trang trọng N + のため (vì mưa lớn nên đã quyết định hủy...)."},
            {"grammar_code": "GP-N5-18", "role": "sentence_structure", "note_vi": "Tự động từ 決まる gắn với chủ ngữ kết quả (～の中止が決まった)."},
        ],
        "structure_parse_vi": (
            "Nguyên nhân khách quan [大雨のため] (GP-N4-12) -> chủ ngữ sự kiện [大会の + 中止が] + tự động từ [決まった] (GP-N5-18)."
        ),
        "pedagogical_takeaway_vi": "Khung [Nのため + Nの___が決まった]: sau từ chỉ thiên tai/thời tiết xấu như 大雨, phương án hợp logic là hủy bỏ hoàn toàn sự kiện (中止).",
        "option_grammar_notes": [
            "静止: Đứng yên bất động (của hình ảnh/người), không dùng cho đại hội bị hủy vì mưa.",
            "禁止: Cấm đoán hành vi, không dùng với thiên tai 'đại hội bị cấm'.",
            "停止: Tạm ngưng vận hành máy móc/giao thông/hệ thống.",
            "中止 (ちゅうし): ĐÚNG. Hủy bỏ sự kiện, giải đấu đã lên lịch.",
        ],
    },
    # ID=85
    "ba46a14f879b5f39e4479855c28919ee63e8b6fe9a2b953efe5f9bc7d4d24937": {
        "links": [
            {"grammar_code": "GP-N5-07", "role": "sentence_structure", "note_vi": "Danh từ hóa cụm động từ Vる + のは + 大変だ (việc quản lý ngôi nhà lớn thì rất vất vả)."},
            {"grammar_code": "GP-N5-02", "role": "sentence_structure", "note_vi": "Tân ngữ 大きな家を đi kèm trực tiếp danh động từ nhóm 3 する."},
        ],
        "structure_parse_vi": (
            "Cụm danh từ hóa [大きな家を + 管理する + のは] (tân ngữ + danh động từ nhóm 3 + のは GP-N5-07) -> đánh giá [大変だ]."
        ),
        "pedagogical_takeaway_vi": "Thấy khung [大きな家を + ___するのは、大変だ], danh động từ cần tìm phải nhận nhà cửa làm tân ngữ quản trị.",
        "option_grammar_notes": [
            "故障: Hỏng hóc (đi với tự động từ/danh từ máy móc 家が/車が故障する), không nhận tân ngữ を ở đây.",
            "管理 (かんり): ĐÚNG. Quản lý, trông coi tài sản/tòa nhà lớn.",
            "指図: Sai bảo/chỉ đạo con người, không dùng với ngôi nhà.",
            "構成: Cấu thành nội dung/văn bản, không khớp đánh giá 'vất vả để giữ nhà'.",
        ],
    },
    # ID=86
    "d8d1e10a051e2e4885bb58bd0b5312ac00ff0dabc8fc2eb0eeca865dcf114050": {
        "links": [
            {"grammar_code": "GP-N5-01", "role": "sentence_structure", "note_vi": "Chia động từ nhóm 1 sang thể て nối tuần tự hai hành động (焼く -> 焼いて -> 料理を作った)."},
            {"grammar_code": "GP-N5-02", "role": "sentence_structure", "note_vi": "Hai vế cùng dùng tân ngữ trực tiếp với を."},
        ],
        "structure_parse_vi": (
            "Hành động bước 1 [魚を + 焼いて] (động từ nhóm 1 chia thể て GP-N5-01) -> bước 2 [料理を作った]."
        ),
        "pedagogical_takeaway_vi": "Phân biệt chia thể て của động từ nhóm 1 có đuôi tương đồng âm vị: 焼く (やいて) vs 沸かす (わかして) vs 破る (やぶって).",
        "option_grammar_notes": [
            "わかして: Đun sôi nước (お湯を沸かす), không dùng để nướng cá.",
            "やぶって: Xé rách giấy hoặc phá lời hứa, sai với 魚を.",
            "やいて (焼いて): ĐÚNG. Nướng/rán cá làm món ăn.",
            "こいで: Đạp xe hoặc chèo thuyền, vô nghĩa với 魚を.",
        ],
    },
    # ID=87
    "ba04ba732338da6ec32ef6b4f1b6ea771698b53c856539b273221e8d05b1e6b1": {
        "links": [
            {"grammar_code": "GP-N5-13", "role": "sentence_structure", "note_vi": "Mệnh đề nguyên nhân hiện tại ～ので (vì hôm nay không có ở nhà)."},
            {"grammar_code": "GP-N4-23", "role": "sentence_structure", "note_vi": "Kính ngữ đề nghị lịch sự ～にお願いします."},
            {"grammar_code": "GP-N5-04", "role": "sentence_structure", "note_vi": "Mốc thời gian bắt đầu hướng về tương lai (明日以降に)."},
        ],
        "structure_parse_vi": (
            "Nguyên nhân hiện tại [今日は家にいない + ので] (GP-N5-13) -> yêu cầu đặt lịch vào mốc tương lai [連絡は + 明日以降に + お願いします] (GP-N4-23)."
        ),
        "pedagogical_takeaway_vi": "Kiểm tra trục thời gian ngay trước chỗ trống: từ mốc TƯƠNG LAI (明日, 来週) trở đi BẮT BUỘC dùng 以降, tuyệt đối không dùng 以来 (chỉ mốc quá khứ).",
        "option_grammar_notes": [
            "以来: Chỉ mốc từ QUÁ KHỨ tới nay (例: 卒業して以来), không gắn sau mốc tương lai 明日.",
            "以上: Dùng cho số lượng hoặc cấp độ trở lên (5人以上), không dùng cho mốc ngày mai.",
            "以下: Dùng cho số lượng/mức trở xuống.",
            "以降 (いこう): ĐÚNG. Kể từ một mốc (hiện tại hoặc tương lai) trở về sau.",
        ],
    },
    # ID=88
    "554aa8a99c21992c500a33cd10740b201c4886ce1871682f9de2774acf5eef0f": {
        "links": [
            {"grammar_code": "GP-N4-11", "role": "sentence_structure", "note_vi": "Mục đích/lời chúc không ý chí [Vる + よう（に） + 祈っています] (lược bỏ に trong văn viết lịch sự)."},
            {"grammar_code": "GP-N5-08", "role": "sentence_structure", "note_vi": "Thể tiếp diễn trạng thái tâm lý 祈っています (đang cầu chúc)."},
        ],
        "structure_parse_vi": (
            "Nội dung cầu mong không ý chí [早く病気がなおるよう（に）] (GP-N4-11 + tự động từ 治る) -> hành động cầu nguyện tiếp diễn [祈っています] (GP-N5-08)."
        ),
        "pedagogical_takeaway_vi": "Khi vế trước kết bằng ～よう（に） (hoặc ～ようにと) thì động từ sau luôn là động từ cầu nguyện/nhắn nhủ (祈る, 願う).",
        "option_grammar_notes": [
            "祈って (いのって): ĐÚNG. Cầu nguyện, cầu chúc bệnh mau khỏi (~ように祈る).",
            "信じて: 'Tin tưởng', đi với Nを hoặc ～と信じる, không hợp cầu mong ~ように.",
            "困って: 'Gặp rắc rối', sai nghĩa lời chúc sức khỏe.",
            "返って: 'Trả lại', vô nghĩa với ngữ cảnh chúc mau lành bệnh.",
        ],
    },
    # ID=89
    "150ccd5e67d4f835467b9cce829a10beff11ce6ee0f4d0958b2467d3df6cca38": {
        "links": [
            {"grammar_code": "GP-N5-07", "role": "sentence_structure", "note_vi": "Danh từ hóa cụm động từ Vる + ことは + 大切だ (việc giao tiếp giữa cha mẹ và con cái rất quan trọng)."},
            {"grammar_code": "GP-N5-02", "role": "sentence_structure", "note_vi": "Kết hợp động từ cố định [Nをとる]: コミュニケーションをとる."},
        ],
        "structure_parse_vi": (
            "Cụm danh từ hóa chủ ngữ [親子の + コミュニケーションを + とること + は] (GP-N5-07) -> đánh giá [大切だ]."
        ),
        "pedagogical_takeaway_vi": "Chú ý động từ đi kèm sau chỗ trống là をとる: コミュニケーションをとる (giao tiếp), メモをとる (ghi chú), バランスをとる (cân bằng).",
        "option_grammar_notes": [
            "コントロール: Kiểm soát (コントロールする), ít tự nhiên với 'lấy kiểm soát giữa cha mẹ và con' trong câu này.",
            "レクリエーション: Giải trí tập thể, không kết hợp với をとる.",
            "サークル: Câu lạc bộ, không ghép với をとる.",
            "コミュニケーション: ĐÚNG. Cụm từ cố định: コミュニケーションをとる (giao tiếp).",
        ],
    },
    # =========================================================================
    # SECTION 2: VOCABULARY BATCH 2 (49 QUESTIONS: IDs 90-138)
    # =========================================================================
    # ID=90
    "a046cfbfac41d0611a0e3cae8dfb7e7a9014d70b682f4526e7e593da64eb2a47": {
        "links": [
            {"grammar_code": "GP-N5-01", "role": "sentence_structure", "note_vi": "Thể て của động từ nhận thức 読んで biểu thị nguyên nhân cảm xúc (đọc xong thì giật mình)."},
            {"grammar_code": "GP-N5-02", "role": "sentence_structure", "note_vi": "Cụm sở hữu 新聞の + N làm tân ngữ với を."},
        ],
        "structure_parse_vi": (
            "[新聞の + 見出しを + 読んで]、(thể て nối nguyên nhân trực tiếp - GP-N5-01) -> kết quả cảm xúc [びっくりした]."
        ),
        "pedagogical_takeaway_vi": "Cấu tạo danh từ ghép dạng [Vます gốc + 出し] (見出し tiêu đề, 思い出 hồi ức) luôn giữ cấu trúc bổ nghĩa NのN trước を.",
        "option_grammar_notes": [
            "見回し: Hành động nhìn xung quanh (見回す), không dùng làm thứ 'đọc' trên báo.",
            "見落とし: Sự nhìn sót lỗi/thông tin, không hợp cấu trúc 新聞の...を読んで.",
            "見出し (みだし): ĐÚNG. Tiêu đề, tít bài báo.",
            "見返し: Sự xem lại hoặc tờ gác bìa sách.",
        ],
    },
    # ID=91
    "253ed9ca87092a6815be884a24dbf249256a53b3dd933653ad8e18649787d7f4": {
        "links": [
            {"grammar_code": "GP-N5-10", "role": "sentence_structure", "note_vi": "Yêu cầu phủ định nhẹ Vないで nối vào lời mời kính ngữ."},
            {"grammar_code": "GP-N4-23", "role": "sentence_structure", "note_vi": "Tôn kính ngữ tiếp khách lịch sự お召し上がりください (từ 食べる)."},
        ],
        "structure_parse_vi": (
            "Vế nhượng bộ khuyến khích [遠慮 + しないで] (GP-N5-10) -> lời mời tôn kính bữa ăn [たくさん + お召し上がりください] (GP-N4-23)."
        ),
        "pedagogical_takeaway_vi": "Gặp tôn kính ngữ bàn ăn お召し上がりください đứng cuối câu, cụm mở đầu lịch sự gần như luôn là 遠慮しないで (xin đừng khách sáo).",
        "option_grammar_notes": [
            "辞退 (じたい): Từ chối lời mời/chức vụ trang trọng, không hợp 'đừng từ chối mà hãy ăn nhiều' theo ngữ dụng mời khách.",
            "失礼 (しつれい): Thất lễ — nói 'đừng thất lễ rồi ăn nhiều' là vô lý trong tiếp khách.",
            "先導 (せんどう): Dẫn đường đi đầu, lạc ngữ cảnh bữa ăn.",
            "遠慮 (えんりょ): ĐÚNG. Cụm lịch sự cố định: 遠慮しないで召し上がる.",
        ],
    },
    # ID=92
    "4e4ebcda58f56a47645345d65b1aba18071b11bf1fb95f4736e6f359ca0d5abe": {
        "links": [
            {"grammar_code": "GP-N4-16", "role": "sentence_structure", "note_vi": "Điều kiện thời gian quá khứ Vていたら (trong lúc đang làm thì bất ngờ đã...)."},
            {"grammar_code": "GP-N4-09", "role": "sentence_structure", "note_vi": "Thể Vてしまった ở cuối câu nhấn mạnh sự trôi thời gian ngoài ý thức (đã trưa mất rồi)."},
        ],
        "structure_parse_vi": (
            "Bối cảnh hành động kéo dài [一生けん命 + 仕事をしていたら] (GP-N5-08 + GP-N4-16) "
            "-> phó từ [いつのまにか] -> biến chuyển thời gian hoàn tất [昼になってしまった] (GP-N4-09)."
        ),
        "pedagogical_takeaway_vi": "Khung [～ていたら + ___ + Vてしまった / になってしまった] thường đòi hỏi phó từ chỉ sự diễn biến vô thức いつのまにか ('lúc nào không hay').",
        "option_grammar_notes": [
            "いつまでも: Nghĩa 'mãi mãi đến tận bao giờ', không khớp sự việc bất ngờ đã tới trưa.",
            "いつのまにか: ĐÚNG. Diễn tả thời gian trôi mà người nói mải làm không để ý.",
            "どこまでも: Chỉ không gian/mức độ 'đến cùng', sai ngữ nghĩa thời gian.",
            "どこか: Đại từ bất định 'ở đâu đó', không khớp danh từ thời gian 昼.",
        ],
    },
    # ID=93
    "8b95906f18d862f374d5dc916bfa3e72d422bd506128d4835fddd4c85ad7a380": {
        "links": [
            {"grammar_code": "GP-N3-098", "role": "sentence_structure", "note_vi": "Liên kết nhượng bộ văn viết N + であった / あった + ものの (tuy gặp tai nạn lớn nhưng may sao...)."},
            {"grammar_code": "GP-N5-03", "role": "sentence_structure", "note_vi": "Trợ từ に đi với 遭う (あう): gặp phải sự cố ngoài ý muốn (事故にあう)."},
        ],
        "structure_parse_vi": (
            "Mệnh đề nhượng bộ [大きな + 事故に + あった + ものの] (GP-N5-03 + GP-N3-098) -> kết quả may mắn [なんとか助かった]."
        ),
        "pedagogical_takeaway_vi": "Chú ý kết hợp động từ riêng cho tai họa: 事故にあう (gặp tai nạn) khác với 怪我をする (bị thương) và 病気になる (bị ốm).",
        "option_grammar_notes": [
            "怪我 (けが): Phải đi với động từ 怪我をする (không đi với 怪我にあう).",
            "病気 (びょうき): Phải đi với 病気になる hoặc 病気にかかる.",
            "事故 (じこ): ĐÚNG. Kết hợp chuẩn 事故にあう ('gặp tai nạn') khớp với 助かった (thoát chết).",
            "殺人 (さつじん): 'Vụ sát nhân' — không kết hợp tự nhiên kiểu nạn nhân kể 殺人にあう ở đây.",
        ],
    },
    # ID=94
    "fe566b323104b24344c5ed2fbac813a744211cafcc403a84532244efb3322090": {
        "links": [
            {"grammar_code": "GP-N5-03", "role": "sentence_structure", "note_vi": "Trợ từ に + は (女の人には) chỉ đối tượng hướng tới của tính cách dễ dãi (～に甘い)."},
            {"grammar_code": "GP-N5-05", "role": "sentence_structure", "note_vi": "Tính từ đuôi い (甘い = やさしい) làm vị ngữ đánh giá tính cách."},
        ],
        "structure_parse_vi": (
            "[彼は]、(chủ đề) + trạng ngữ tần suất [いつも] + đối tượng hướng tới [女の人には] (GP-N5-03) + tính từ vị ngữ [あまい]."
        ),
        "pedagogical_takeaway_vi": "Khi tính từ 甘い (ngọt) đi cùng cấu trúc [Người + には + 甘い], nghĩa chuyển từ vị giác sang 'dễ dãi, nuông chiều' (= やさしい).",
        "option_grammar_notes": [
            "消極的だ: Nghĩa 'tiêu cực/thụ động', không khớp nét nghĩa nuông chiều đối phương.",
            "積極的だ: Nghĩa 'tích cực/năng nổ', sai nghĩa.",
            "きびしい: Bẫy trái nghĩa ('nghiêm khắc'), trái ngược hẳn thái độ 甘い.",
            "やさしい: ĐÚNG. Đồng nghĩa với あまい khi đi trong mẫu 人には甘い.",
        ],
    },
    # ID=95
    "815f732595cf01c7836836fc82a9277879d6482d706bad0162cff5926ca45f8f": {
        "links": [
            {"grammar_code": "GP-N5-13", "role": "sentence_structure", "note_vi": "Mệnh đề nguyên nhân ～ので (vì đã vận động nhiều nên...)."},
            {"grammar_code": "GP-N5-05", "role": "sentence_structure", "note_vi": "Tính từ danh từ tượng hình からから + だ làm vị ngữ miêu tả trạng thái cổ họng."},
        ],
        "structure_parse_vi": (
            "Nguyên nhân quá khứ [たくさん運動した + ので] (GP-N5-13) -> chủ thể cơ thể [のどが] + trạng thái khô khốc [からからだ]."
        ),
        "pedagogical_takeaway_vi": "Từ tượng thanh/tượng hình からからだ gắn với danh từ のど (họng) luôn quy về tính chất khát khô (乾いている).",
        "option_grammar_notes": [
            "ぬれている: Bẫy trái nghĩa ('đang bị ướt'), ngược với từ tượng hình からから.",
            "乾いている (かわいている): ĐÚNG. Trạng thái khô cạn, khát nước.",
            "楽だ: 'Thoải mái/dễ dàng', sai ngữ nghĩa cổ họng sau vận động mạnh.",
            "痛い: 'Đau', không đồng nghĩa với trạng thái khô ráo からから.",
        ],
    },
    # ID=96
    "a868c7117ef40d1378bbd58757798f075af91623134168596b763e82ba904fa4": {
        "links": [
            {"grammar_code": "GP-N5-05", "role": "sentence_structure", "note_vi": "Phó từ mức độ 結構 đứng trực tiếp trước tính từ đuôi な (便利だ) làm giảm hoặc đánh giá mức 'khá là'."},
        ],
        "structure_parse_vi": (
            "[この辞書は] (chủ đề) + phó từ chỉ mức độ [結構] + tính từ đuôi な [便利だ]."
        ),
        "pedagogical_takeaway_vi": "Phó từ 結構 khi bổ nghĩa cho tính từ (結構便利だ / 結構高い) mang mức độ 'khá, tương đối' (= ある程度は), khác với nghĩa từ chối trong hội thoại.",
        "option_grammar_notes": [
            "おどろくほど: 'Đến mức đáng kinh ngạc' — mức độ quá cực đoan so với 結構.",
            "ちょうどよく: 'Vừa vặn đúng chuẩn', không khớp với đánh giá mức độ tiện lợi của 結構.",
            "ある程度は: ĐÚNG. Mức 'khá là, ở một chừng mực đáng kể'.",
            "前よりもっと: 'Hơn trước đây', thêm yếu tố so sánh thời gian không có trong 結構.",
        ],
    },
    # ID=97
    "aebc9f45da3d748664329bceeb2da96780de8c7873b4bfd2cef4ce0b9b7cb60c": {
        "links": [
            {"grammar_code": "GP-N3-085", "role": "sentence_structure", "note_vi": "Động từ ghép Vます + 出す (言い出す = bất ngờ/tiên phong nói ra đầu tiên)."},
            {"grammar_code": "GP-N5-07", "role": "sentence_structure", "note_vi": "Danh từ hóa nhấn mạnh [Vた + のは + Người + だ] (câu chẻ làm nổi bật chủ thể 井上くん)."},
        ],
        "structure_parse_vi": (
            "Cấu trúc nhấn mạnh câu chẻ [計画を + 言い出した + のは]、(việc khởi xướng kế hoạch - GP-N3-085 + GP-N5-07) + chủ thể [井上くんだ]."
        ),
        "pedagogical_takeaway_vi": "Hậu tố ghép ～出す sau động từ phát ngôn (言い出す, 切り出す) mang nghĩa 'mở lời khởi xướng trước tiên'.",
        "option_grammar_notes": [
            "一番先に言った: ĐÚNG. Giải nghĩa chính xác sắc thái khởi xướng của 言い出す.",
            "一番最後に言った: Bẫy trái nghĩa ('nói sau cùng').",
            "人から聞いて伝えた: Sai nguồn gốc thông tin ('nghe từ người khác rồi nói lại').",
            "考えて発表した: Không nhấn mạnh ý khởi xướng đầu tiên như 言い出す.",
        ],
    },
    # ID=98
    "6bb88e62c1493163520515996e5109df791ca0cf272442ff9c880529e73a701f": {
        "links": [
            {"grammar_code": "GP-N5-10", "role": "sentence_structure", "note_vi": "Câu cấm đoán nhẹ nhàng ～ないでください (xin đừng nói những lời thừa thãi)."},
            {"grammar_code": "GP-N5-05", "role": "sentence_structure", "note_vi": "Tính từ đuôi な (余計な) bổ nghĩa cho danh từ trừu tượng こと."},
        ],
        "structure_parse_vi": (
            "Cụm danh từ có định ngữ tính từ な [よけいな + ことを] (GP-N5-05) + yêu cầu không thực hiện [言わないでください] (GP-N5-10)."
        ),
        "pedagogical_takeaway_vi": "Nghĩa lõi của tính từ 余計な (dư thừa không cần thiết) khi chuyển sang phân tích ngữ dụng câu là '言わなくてもよい' (không nói cũng được).",
        "option_grammar_notes": [
            "言ったことがある: Thể trải nghiệm quá khứ ('đã từng nói'), sai ngữ nghĩa.",
            "言ったことがない: Phủ định trải nghiệm ('chưa từng nói').",
            "言ったほうがよい: Lời khuyên khẳng định ('nên nói'), trái ngược lời răn ngăn cản.",
            "言わなくてもよい: ĐÚNG. 'Điều không cần thiết phải nói' = よけいなこと.",
        ],
    },
    # ID=99
    "eb809b93114faabc4b924d3fdbf6927f5e036f5aef6a798910c7851fcf8a7935": {
        "links": [
            {"grammar_code": "GP-N4-12", "role": "sentence_structure", "note_vi": "Ở Option 4 đúng: 練習のために (vì mục đích luyện tập) bổ nghĩa cho việc lặp lại."},
            {"grammar_code": "GP-N5-06", "role": "sentence_structure", "note_vi": "Mệnh đề danh từ hóa 先生が言ったこと làm tân ngữ với を cho 繰り返した."},
        ],
        "structure_parse_vi": (
            "Câu đúng (Option 4): Mục đích [練習のために] (GP-N4-12) + tân ngữ [先生が言ったことを] (GP-N5-06) + tần suất và hành động [何度も + 繰り返した]."
        ),
        "pedagogical_takeaway_vi": "Phân biệt 3 động từ chữ 返/反 cực hay nhầm: 繰り返す (lặp lại hành động/lời nói) vs ひっくり返す (lật úp đồ vật) vs 振り返る (ngoái nhìn/hồi tưởng).",
        "option_grammar_notes": [
            "Sentence 1: Làm đổ bàn ghế phải dùng ひっくり返してしまった.",
            "Sentence 2: Ngoái đầu nhìn lại phía sau phải dùng 振り返った.",
            "Sentence 3: Nghĩ nhớ về một người dùng 思い出した hoặc 振り返った.",
            "Sentence 4: ĐÚNG. 練習のために先生の言葉をくり返す (lặp lại nhiều lần).",
        ],
    },
    # ID=100
    "69440d953e871052ce22fbd9ab4c3e2d4847b6b329c55d0af0ea808f9b4d826d": {
        "links": [
            {"grammar_code": "GP-N5-18", "role": "sentence_structure", "note_vi": "Tự động từ hữu cơ 生える đi với chủ ngữ thực vật với が (草木が地面から生えた)."},
            {"grammar_code": "GP-N5-04", "role": "sentence_structure", "note_vi": "Trợ từ xuất phát điểm không gian 地面から (mọc lên từ mặt đất)."},
        ],
        "structure_parse_vi": (
            "Câu đúng (Option 1): chủ ngữ tự nhiên [新しい草木が] (GP-N5-18) + điểm xuất phát [地面から] (GP-N5-04) + tự động từ [生えた]."
        ),
        "pedagogical_takeaway_vi": "Động từ 生える (はえる) chuyên dùng cho cây cối, tóc, râu, răng mọc từ bề mặt vật chất — không dùng cho ý tưởng hay nhà cửa.",
        "option_grammar_notes": [
            "Sentence 1: ĐÚNG. 草木が地面から生えた (cây cỏ mọc lên từ mặt đất).",
            "Sentence 2: Ý tưởng nảy ra phải dùng 浮かぶ hoặc 生まれる.",
            "Sentence 3: Nhà cửa được xây mọc lên phải dùng 建つ (たつ).",
            "Sentence 4: Phát bệnh phải dùng 病気になる hoặc かかる.",
        ],
    },
    # ID=101
    "6d1dadc02435e204f02df786f13b6bc49e780bf4d2272428e497ffa84881032a": {
        "links": [
            {"grammar_code": "GP-N4-12", "role": "sentence_structure", "note_vi": "Cụm mục đích 体のために (vì sức khỏe thể chất) đi trước thói quen tập luyện."},
            {"grammar_code": "GP-N5-08", "role": "sentence_structure", "note_vi": "Thói quen lặp lại hằng ngày かならず + トレーニングしている."},
        ],
        "structure_parse_vi": (
            "Câu đúng (Option 3): khung thời gian [朝と夜]、+ mục đích [体のために] (GP-N4-12) + tần suất [かならず] + thói quen [トレーニングしている] (GP-N5-08)."
        ),
        "pedagogical_takeaway_vi": "Đừng nhầm âm Katakana giữa トレーニング (training: rèn luyện thể lực) và トレーディング (trading: giao dịch thương mại).",
        "option_grammar_notes": [
            "Sentence 1: Giao thương giữa các quốc gia phải dùng 貿易 (hoặc トレーディング).",
            "Sentence 2: Thử sức với kỳ thi dùng 挑戦 hoặc チャレンジ (トレーニング không đi kiểu 試験に~).",
            "Sentence 3: ĐÚNG. 体のためにトレーニングしている (luyện tập vì sức khỏe).",
            "Sentence 4: Tính năng/hiệu suất của ô tô dùng 性能 hoặc 機能.",
        ],
    },
    # ID=102
    "68df359536226eed430dc7fe334b5303e6e7be8dc733434864683ee0d3f45a06": {
        "links": [
            {"grammar_code": "GP-N5-01", "role": "sentence_structure", "note_vi": "Thể て nguyên nhân/phương tiện của danh động từ (努力して) dẫn đến kết quả khả năng đỗ đạt."},
            {"grammar_code": "GP-N4-01", "role": "sentence_structure", "note_vi": "Động từ khả năng quá khứ 合格できた (đã thi đỗ được)."},
        ],
        "structure_parse_vi": (
            "Câu đúng (Option 2): hành động phương tiện [努力して]、(GP-N5-01) -> kết quả đạt được [希望の大学に + 合格できた] (GP-N4-01)."
        ),
        "pedagogical_takeaway_vi": "Khác với 能力 (năng lực sẵn có/được đánh giá: 能力がある), 努力 là hành động cố gắng (努力する / 努力を重ねる).",
        "option_grammar_notes": [
            "Sentence 1: Năng khiếu/tài năng có sẵn dùng 能力 hoặc 才能 (~がある).",
            "Sentence 2: ĐÚNG. 努力して合格できた (nhờ nỗ lực mà thi đỗ được).",
            "Sentence 3: Hồi phục thể lực/sức khỏe phải dùng 体力を回復した.",
            "Sentence 4: Năng lực làm việc của nhân viên phải dùng 能力 của nhân viên (能力のよい).",
        ],
    },
    # ID=103
    "cc6578a6f744e5c4316de3562b5f55d2fe4b413d94c9fbbd4ef199b9ac18023b": {
        "links": [
            {"grammar_code": "GP-N3-097", "role": "sentence_structure", "note_vi": "Đuôi ものだ đi sau tính từ cảm xúc (なつかしいものだ) bộc lộ chân lý cảm động tự nhiên."},
            {"grammar_code": "GP-N4-16", "role": "sentence_structure", "note_vi": "Cụm nhượng bộ nghi vấn [何年たっても]: cho dù bao nhiêu năm trôi qua đi nữa."},
        ],
        "structure_parse_vi": (
            "Câu đúng (Option 2): nhượng bộ thời gian [日本へ来て + 何年たっても]、(GP-N4-16) "
            "-> chủ đề cảm xúc [やはり + 国の家族は] + cảm thán chân lý [なつかしいものだ] (GP-N3-097)."
        ),
        "pedagogical_takeaway_vi": "Chữ 懐かしい (なつかしい) dùng cho ký ức xưa cũ, quê nhà; tránh nhầm với 懐く (なつく: thú cưng quấn chủ) và 恥ずかしい (xấu hổ).",
        "option_grammar_notes": [
            "Sentence 1: Chó mèo quấn quýt chủ phải dùng động từ 懐いている (なついている).",
            "Sentence 2: ĐÚNG. 何年たっても家族は懐かしいものだ (luôn thấy nhớ thương gia đình).",
            "Sentence 3: Ghen tị với người nhiều bạn phải dùng 羨ましい (うらやましい).",
            "Sentence 4: Ngượng ngùng xấu hổ khi thất bại trước đám đông dùng 恥ずかしかった.",
        ],
    },
    # ID=104
    "38d0e01534f7a3bc4ed6be45e06073cb57dc5d48d73e2c707137434e20c5cc83": {
        "links": [
            {"grammar_code": "GP-N4-09", "role": "sentence_structure", "note_vi": "Thể hoàn tất tiếc nuối Vて + しまった (散ってしまった): hoa đã rụng tàn mất rồi."},
            {"grammar_code": "GP-N5-01", "role": "sentence_structure", "note_vi": "Biến âm nhóm 1 đuôi る: 散る (ちる) chia thể て thành 散って (ちって)."},
        ],
        "structure_parse_vi": (
            "[桜の花は]、(chủ đề tương phản は) + phó từ đã qua [もう] + biến đổi tiếc nuối hoàn tất [散ってしまった] (GP-N5-01 + GP-N4-09)."
        ),
        "pedagogical_takeaway_vi": "Phân biệt chia thể て 4 động từ nhóm 1 đuôi る dễ nhầm trong câu hoa lá rụng: 散る -> ちって (khác với 行く/言う いって).",
        "option_grammar_notes": [
            "いって: Thể て của 行く (đi) hoặc 言う (nói), sai nghĩa và mặt chữ 散.",
            "まって: Thể て của 待つ (đợi), sai chữ Hán.",
            "さって: Thể て của 去る (rời đi/trôi qua — dùng cho thời gian/người, không dùng cho hoa rụng).",
            "ちって (散って): ĐÚNG. 散る chia thể て + しまった = hoa đã rụng tàn mất rồi.",
        ],
    },
    # ID=105
    "8a084e169a0e97e398595f7310eb8671366df04c9640dc46ed418a221a4c45df": {
        "links": [
            {"grammar_code": "GP-N5-03", "role": "sentence_structure", "note_vi": "Tính từ な / Danh động từ 満足 nhận đối tượng hướng tới bằng trợ từ に (今の生活に満足ですか)."},
        ],
        "structure_parse_vi": (
            "Đối tượng đánh giá [今の生活に] (GP-N5-03) + vị ngữ câu hỏi tính từ な [満足ですか]."
        ),
        "pedagogical_takeaway_vi": "Nhớ quy tắc biến âm đục của chữ 足: 満足 đọc まんぞく (có tenten) trong khi 不足 đọc ふそく (không có tenten).",
        "option_grammar_notes": [
            "まんそく: Bẫy quên thanh đục ở chữ 足 trong từ 満足.",
            "まんぞく (満足): ĐÚNG. Hài lòng với cuộc sống hiện tại.",
            "まんそぐ: Sai thanh đục ở âm tiết cuối く.",
            "まんぞぐ: Thừa thanh đục ở chữ cuối.",
        ],
    },
    # ID=106
    "b575babb163ae0a47d30525c2a1ccb0e4b5094d147fa4b5bc89141482a10b48c": {
        "links": [
            {"grammar_code": "GP-N5-03", "role": "sentence_structure", "note_vi": "Trợ từ xuất phát điểm từ ga この駅から + đích lên tàu 急行に + 乗る."},
            {"grammar_code": "GP-N3-041", "role": "sentence_structure", "note_vi": "Dự định chủ quan trong câu khẳng định Vる + つもりだ (乗るつもりだ)."},
        ],
        "structure_parse_vi": (
            "[この駅から] (điểm xuất phát) + phương tiện lên [急行に] (GP-N5-03) + động từ + dự định [乗るつもりだ] (GP-N3-041)."
        ),
        "pedagogical_takeaway_vi": "Phân biệt trường âm hai từ giao thông cực dễ nhầm: 急行 (きゅうこう - tàu tốc hành) vs 空港 (くうこう - sân bay).",
        "option_grammar_notes": [
            "くこう: Thiếu trường âm cả 急 lẫn 港.",
            "くうこう: Âm của 空港 (sân bay), không dùng sau 駅から...に乗る.",
            "きゅこう: Thiếu trường âm ở 急 (きゅう).",
            "きゅうこう (急行): ĐÚNG. Tàu tốc hành.",
        ],
    },
    # ID=107
    "323494c792cf70c2f42a46da1431657da353688b9c2244dd037f01717e336067": {
        "links": [
            {"grammar_code": "GP-N5-01", "role": "sentence_structure", "note_vi": "Dạng nối câu văn viết dùng gốc Vます (川に落ち、) thay cho thể て (落ちて) nối nguyên nhân tai nạn."},
            {"grammar_code": "GP-N5-18", "role": "sentence_structure", "note_vi": "Tự động từ 落ちる và tự động từ なくなる (意識がなくなる: mất ý thức)."},
        ],
        "structure_parse_vi": (
            "[彼女は] + sự cố nguyên nhân dạng liên dụng văn viết [川に落ち、] (GP-N5-01) -> kết quả [意識がなくなった] (GP-N5-18)."
        ),
        "pedagogical_takeaway_vi": "Vế câu kết thúc bằng gốc động từ bỏ ます + dấu phẩy (落ち、) là cách nối trình tự/nguyên nhân phổ biến trong báo chí N3.",
        "option_grammar_notes": [
            "ちしき: Âm đọc của 知識 (tri thức/kiến thức), không ghép với chữ 意.",
            "にんしき: Âm đọc của 認識 (nhận thức).",
            "けんしき: Âm đọc của 見識 (kiến giải sâu rộng).",
            "いしき (意識): ĐÚNG. Cụm y tế cố định: 意識がなくなる (bất tỉnh).",
        ],
    },
    # ID=108
    "f3ac4fdfab830c7ae034fd8366518e2364191b30f9e2bf72f5867fac08dbd139": {
        "links": [
            {"grammar_code": "GP-N5-02", "role": "sentence_structure", "note_vi": "Chủ ngữ ghép [AとBの + 能力の差 + は] + vị ngữ tính từ 大きい."},
        ],
        "structure_parse_vi": (
            "[あの人と私の] + [能力の + 差は] (chủ đề có hai tầng sở hữu の) + tính từ đánh giá mức độ [大きい]."
        ),
        "pedagogical_takeaway_vi": "Chữ 差 khi đứng độc lập trước trợ từ (差がある / 差は大きい) đọc đơn âm さ; chỉ khi ghép 2 chữ mới đọc さい (差異, 誤差).",
        "option_grammar_notes": [
            "さ (差): ĐÚNG. Cách đọc độc lập chuẩn xác chỉ sự chênh lệch.",
            "ざ: Bẫy đọc âm đục.",
            "さい: Âm On ghép từ 差異 (sự khác biệt), không đọc một chữ trần sau 能力の.",
            "ざい: Sai thanh đục và âm đọc.",
        ],
    },
    # ID=109
    "8eb316aefee14c82bc3afa2b24233aa5ddbbb0a675f4183203d8f4f692765ec0": {
        "links": [
            {"grammar_code": "GP-N5-03", "role": "sentence_structure", "note_vi": "Trợ từ に chỉ bề mặt/nơi đăng tải (新聞に) đi với tha động từ 載せる (đăng lên)."},
            {"grammar_code": "GP-N5-18", "role": "sentence_structure", "note_vi": "Tha động từ のせる (載せる: đăng báo) nhận tân ngữ を."},
        ],
        "structure_parse_vi": (
            "Phương tiện đăng tải [新聞に] (GP-N5-03) + tân ngữ [広告を] + tha động từ [のせる] (GP-N5-18)."
        ),
        "pedagogical_takeaway_vi": "Cụm [新聞に広告をのせる] giúp nhớ cặp trường âm 広告 (こうこく) khác hẳn 航空 (こうくう - hàng không).",
        "option_grammar_notes": [
            "ここく: Thiếu trường âm う ở chữ 広 (こう).",
            "こうく: Thiếu âm đọc ở chữ 告 (こく).",
            "こうこく (広告): ĐÚNG. Quảng cáo trên báo.",
            "こうくう: Âm đọc của 航空 (hàng không), sai với 新聞.",
        ],
    },
    # ID=110
    "4604912704da6fc6973d8bf9df468f2a4688adf26385c83ff5b34ba10c2bef6b": {
        "links": [
            {"grammar_code": "GP-N5-01", "role": "sentence_structure", "note_vi": "Thể て nối hành động trước sau (運動をして) dẫn tới kết quả đổ mồ hôi (汗をかいた)."},
            {"grammar_code": "GP-N5-02", "role": "sentence_structure", "note_vi": "Kết hợp động từ đặc biệt N + を + かく (汗をかく)."},
        ],
        "structure_parse_vi": (
            "Hành động tạo tác [運動をして]、(GP-N5-01) -> kết quả sinh lý [汗を + たくさん + かいた] (GP-N5-02)."
        ),
        "pedagogical_takeaway_vi": "Động từ かく đi sau tân ngữ ở đây chỉ kết hợp với 汗 (汗をかく: đổ mồ hôi); nước mắt dùng 流す, hơi thở dùng する/つく.",
        "option_grammar_notes": [
            "なみだ: Cách đọc của 涙 (nước mắt), không đi với かく (mà đi với 涙を流す).",
            "あせ (汗): ĐÚNG. Cụm cố định 汗をかく (đổ mồ hôi).",
            "いき: Cách đọc của 息 (hơi thở — dùng 息をする/吐く).",
            "みず: Cách đọc của 水 (nước).",
        ],
    },
    # ID=111
    "579d221b3023a166b34a384b49b50afbbc036df1341c6c60e643c0a4b30b8b72": {
        "links": [
            {"grammar_code": "GP-N5-02", "role": "sentence_structure", "note_vi": "Khung trực tiếp [NのNを + 禁止する]: nghiêm cấm việc ra ngoài ban đêm."},
        ],
        "structure_parse_vi": (
            "Cụm danh từ hành vi [夜中の + 外出を] (GP-N5-02) + tha động từ nhóm 3 [禁止する]."
        ),
        "pedagogical_takeaway_vi": "Chú ý hai âm dễ nhầm ở 禁止: danh động từ nhóm 3 nguyên mẫu luôn đọc thanh trong きんし (chỉ động từ 禁じる mới có âm đục じ).",
        "option_grammar_notes": [
            "きんし (禁止): ĐÚNG. Thanh trong ở cả hai chữ (nghiêm cấm).",
            "きんじ: Bẫy nhầm với động từ 禁じる (きんじる).",
            "ぎんし: Đọc sai âm đục chữ 禁.",
            "ぎんじ: Sai âm đục cả hai chữ.",
        ],
    },
    # ID=112
    "9d5676832381bfa0cf9cc1d9984d46a0af6b153a95af16147fe2fd1d587ff74e": {
        "links": [
            {"grammar_code": "GP-N5-05", "role": "sentence_structure", "note_vi": "Tính từ đuôi な kết câu dạng khẳng định hiện tại với chủ ngữ phụ (Nは + Nが + 豊富だ)."},
            {"grammar_code": "GP-N5-02", "role": "sentence_structure", "note_vi": "Cặp trợ từ chủ đề - thuộc tính [この国は + 天然資源が]."},
        ],
        "structure_parse_vi": (
            "[この国は]、(chủ đề tổng thể は) + thuộc tính được đánh giá [天然資源が] (GP-N5-02) + tính từ な vị ngữ [豊富だ] (GP-N5-05)."
        ),
        "pedagogical_takeaway_vi": "Khung [N1は + N2が + 豊富だ] (dồi dào về tài nguyên/kinh nghiệm) luôn kết hợp 豊 (Phong) + 富 (Phú).",
        "option_grammar_notes": [
            "盛富: Chữ 盛 (thịnh) không đọc là ほう.",
            "宝富: Chữ 宝 (bảo) đọc là ほう nhưng không ghép với 富 để nghĩa là phong phú.",
            "豊富 (ほうふ): ĐÚNG. Tài nguyên phong phú, dồi dào.",
            "広富: Chữ 広 đọc là こう (không phải ほう).",
        ],
    },
    # ID=113
    "dd0ab46092ed3b21956c05de0270187956aab6add37aaf7ae7d1418b56fece8f": {
        "links": [
            {"grammar_code": "GP-N5-03", "role": "sentence_structure", "note_vi": "Trạng ngữ mốc trước sự kiện [テストの前に] + tha động từ 暗記した (GP-N5-02)."},
        ],
        "structure_parse_vi": (
            "Thời điểm [テストの + 前に] (trước kỳ thi) + tân ngữ [単語を] + hành động quá khứ [あんきした] (GP-N5-02)."
        ),
        "pedagogical_takeaway_vi": "Phân biệt mặt chữ đồng âm あん trong học tập: 暗記 (ám ký - học thuộc lòng) vs 案内 (hướng dẫn) vs 安心 (an tâm).",
        "option_grammar_notes": [
            "案記: Nhầm 暗 (tối/thuộc lòng trong đầu) với 案 (phương án).",
            "明記: Nghĩa 'ghi rõ ra', nhưng đọc là めいき (không phải あんき).",
            "安記: Nhầm với 安 (an tâm/rẻ tiền).",
            "暗記 (あんき): ĐÚNG. Học thuộc lòng từ vựng.",
        ],
    },
    # ID=114
    "ddca3839bdf8d9ebbbf89d44622696f7201049361f8b420ea3a37702009e1aa5": {
        "links": [
            {"grammar_code": "GP-N5-03", "role": "sentence_structure", "note_vi": "Đích phòng ngừa hướng vào thảm họa nhận trợ từ に (地震に備えて)."},
            {"grammar_code": "GP-N5-01", "role": "sentence_structure", "note_vi": "Thể て của 備える nối hành động mục đích dự phòng dẫn vào vế mua sắm 水と食べ物を買う."},
        ],
        "structure_parse_vi": (
            "Đích phòng bị [地震に + 備えて]、(GP-N5-03 + GP-N5-01) -> hành động chuẩn bị [水と + 食べ物を + 買う]."
        ),
        "pedagogical_takeaway_vi": "Cặp đồng âm そなえる cực dễ bẫy: 備える (chuẩn bị phòng ngừa cho thiên tai với に) vs 供える (dâng cúng đồ lễ với を).",
        "option_grammar_notes": [
            "準えて: Chữ 準 đọc là じゅん (準備), không chia thành そなえて.",
            "備えて (そなえて): ĐÚNG. Dự phòng cho tình huống rủi ro/động đất.",
            "供えて: Đồng âm そなえて nhưng nghĩa 'dâng lễ lên bàn thờ', không đi với 地震に.",
            "背えて: Sai chữ Hán (背 là lưng).",
        ],
    },
    # ID=115
    "9374934f216efd7888cc75e826efe8aaa1753d4156bc0d6a51c4c22dede7d716": {
        "links": [
            {"grammar_code": "GP-N4-14", "role": "sentence_structure", "note_vi": "Đuôi câu ～ことになった diễn tả kết cục khách quan ngoài ý muốn (cuối cùng bị mất việc)."},
            {"grammar_code": "GP-N5-01", "role": "sentence_structure", "note_vi": "Thể て nguyên nhân (大きなミスをして) dẫn tới hậu quả ở vế 2."},
        ],
        "structure_parse_vi": (
            "Nguyên nhân sai sót [大きなミスをして]、(GP-N5-01) -> hậu quả khách quan [仕事を + 失う + ことになった] (GP-N4-14)."
        ),
        "pedagogical_takeaway_vi": "Động từ 失う (うしなう - Thất) có hình dáng rất giống 夫, 矢, 央 nhưng nét đầu nhô sang trái trên nét ngang dài.",
        "option_grammar_notes": [
            "失う (うしなう): ĐÚNG. Đánh mất công việc/uy tín/ý thức.",
            "夫う: Chữ 夫 (chồng) đọc là おっと, thiếu nét phẩy trên đầu.",
            "矢う: Chữ 矢 (mũi tên) đọc là や, nét đầu khác vị trí.",
            "央う: Chữ 央 (trung ương) đọc là おう, sai nét dọc.",
        ],
    },
    # ID=116
    "ab5984e0241a9512464d270a31e842c6cb96ceb24f24fd6939cd6b97e6547977": {
        "links": [
            {"grammar_code": "GP-N5-03", "role": "sentence_structure", "note_vi": "Mẫu sở thích/quan tâm cố định: [Đối tượng + に + 興味がある] (có hứng thú với...)."},
        ],
        "structure_parse_vi": (
            "Đối tượng quan tâm [日本のマンガに] (GP-N5-03) + chủ thể danh từ [興味が + あります] (GP-N5-02)."
        ),
        "pedagogical_takeaway_vi": "Gặp khung [Nに + きょうみがある / を持つ], xác nhận cặp Kanji 興 (hứng) + 味 (vị) chứ không phải 教 (giáo) + 見 (kiến).",
        "option_grammar_notes": [
            "教味: Nhầm 興 (hứng) với 教 (dạy học).",
            "教見: Sai cả hai chữ Hán.",
            "興味 (きょうみ): ĐÚNG. Hứng thú, sự quan tâm.",
            "興見: Nhầm chữ 味 (vị trong 意味) với chữ 見 (nhìn).",
        ],
    },
    # ID=117
    "50485eefe817cf607afc5a183cde1dba532b2dcbd68882679ab0e9a70d54f81d": {
        "links": [
            {"grammar_code": "GP-N5-01", "role": "sentence_structure", "note_vi": "Thể て nối trình tự thời gian (結婚して -> sau khi kết hôn thì...)."},
            {"grammar_code": "GP-N5-05", "role": "sentence_structure", "note_vi": "Biến đổi trạng thái danh từ N + になる (夫婦になった)."},
        ],
        "structure_parse_vi": (
            "Hành động mốc [結婚して]、(GP-N5-01) -> chủ ngữ [2人は] + kết quả trạng thái [夫婦に + なった] (GP-N5-05)."
        ),
        "pedagogical_takeaway_vi": "Phân biệt hai từ đồng nghĩa nhưng khác cách đọc: 夫婦 đọc ふうふ (vợ chồng đời thường) vs 夫妻 đọc ふさい (vợ chồng trang trọng).",
        "option_grammar_notes": [
            "夫妻: Nghĩa giống nhưng đọc là ふさい, không đọc là ふうふ.",
            "妻夫: Đảo ngược sai trật tự Kanji.",
            "夫婦 (ふうふ): ĐÚNG. Cặp vợ chồng (ふうふ).",
            "婦夫: Đảo ngược sai trật tự Kanji.",
        ],
    },
    # ID=118
    "c173a867ee8e391e5f0d2acefa35d253f5e65b5d626364e778c5aa31dff1f6d0": {
        "links": [
            {"grammar_code": "GP-N5-03", "role": "sentence_structure", "note_vi": "Trạng ngữ thời điểm quá khứ [高校生のとき] + địa điểm hành động 海外で (tại nước ngoài)."},
        ],
        "structure_parse_vi": (
            "Mốc thời gian [高校生のとき]、(Nの + とき) + tần suất [初めて] + địa điểm hành động [海外で] (GP-N5-03) + hành động [ホームステイした]."
        ),
        "pedagogical_takeaway_vi": "Trợ từ chỉ nơi diễn ra hành động で (海外で) đi với động từ nhóm 3 ghép danh từ Katakana chỉ trải nghiệm lưu trú.",
        "option_grammar_notes": [
            "パスポート: Danh từ đồ vật ('hộ chiếu'), không ghép làm động từ ～した tại nước ngoài.",
            "クラスメート: Danh từ chỉ người ('bạn cùng lớp'), không dùng thành động từ する.",
            "ホームページ: Danh từ ('trang chủ web'), không ghép làm hành động ở nước ngoài kiểu này.",
            "ホームステイ: ĐÚNG. Ở trọ nhà dân bản xứ (ホームステイする).",
        ],
    },
    # ID=119
    "fd51d568994ea3415f93263bc47bf6a90e1588b8d0185344f8c57dc420e181a7": {
        "links": [
            {"grammar_code": "GP-N5-01", "role": "sentence_structure", "note_vi": "Thể て nguyên nhân (晴れて -> vì trời nắng nên không khí khô ráo)."},
            {"grammar_code": "GP-N5-08", "role": "sentence_structure", "note_vi": "Trạng thái kết quả tiếp diễn ～している (乾燥している)."},
        ],
        "structure_parse_vi": (
            "[今日は]、+ nguyên nhân thời tiết [晴れて] (GP-N5-01) + chủ ngữ trạng thái [空気が] + trạng thái hiện tại [乾燥している] (GP-N5-08)."
        ),
        "pedagogical_takeaway_vi": "Trong thời tiết học, danh động từ ghép 乾燥する (khô ráo) thường dùng ở thể ている khi đi với 空気が.",
        "option_grammar_notes": [
            "燃焼: Sự đốt cháy nhiên liệu, không đi với 空気が trong ngày nắng.",
            "点火: Sự đánh lửa/châm lửa, vô nghĩa với không khí.",
            "乾燥 (かんそう): ĐÚNG. Trạng thái hanh khô của không khí/da.",
            "熱中: Say mê làm gì (đi với ～に熱中する), sai chủ ngữ 空気が.",
        ],
    },
    # ID=120
    "36e232a6ed6d656138327653d319396513145c0c75194549875e8afe6806e3ae": {
        "links": [
            {"grammar_code": "GP-N5-08", "role": "sentence_structure", "note_vi": "Quá khứ tiếp diễn miêu tả hiện tượng thiên nhiên đang diễn ra [～ていました] (吹いていました)."},
            {"grammar_code": "GP-N5-05", "role": "sentence_structure", "note_vi": "Tính từ đuôi い đổi sang phó từ trạng thái く bổ cho động từ (強く + 吹く)."},
        ],
        "structure_parse_vi": (
            "[その日は]、+ chủ thể thiên nhiên [風が] + trạng từ bổ nghĩa [強く] (GP-N5-05) + tiếp diễn quá khứ [吹いていました] (GP-N5-08)."
        ),
        "pedagogical_takeaway_vi": "Kết hợp từ cố định thời tiết: 風が強く吹く (gió thổi mạnh), tránh nhầm mặt chữ giữa 吹く (xúy - thổi) và 空く / 巻く / 開く.",
        "option_grammar_notes": [
            "空いて: Trống chỗ / đói bụng (空く), không đi với 風が.",
            "巻いて: Cuộn/quấn (tha động từ 巻く), không đứng sau 風が.",
            "開いて: Mở ra (開く), không đi với 風が強く.",
            "吹いて (ふいて): ĐÚNG. Tự động từ 吹く (gió thổi).",
        ],
    },
    # ID=121
    "f8af7490d565da2ef18e6ff1d70db967f244ef63a711cb2a3fe9f4a3b30ec386": {
        "links": [
            {"grammar_code": "GP-N5-03", "role": "sentence_structure", "note_vi": "Trợ từ で sau エンジニアの仕事 chỉ phương tiện/nghề nghiệp kiếm sống."},
            {"grammar_code": "GP-N5-08", "role": "sentence_structure", "note_vi": "Thể tiếp diễn nghề nghiệp ổn định ở hiện tại Vて + いる (かせいでいる)."},
        ],
        "structure_parse_vi": (
            "[彼は]、+ phương tiện nghề nghiệp [エンジニアの仕事で] (GP-N5-03) + lượng từ [たくさん] + thói quen hiện tại [かせいでいる] (GP-N5-08)."
        ),
        "pedagogical_takeaway_vi": "Khi không có tân ngữ trực tiếp với を đứng ngay trước động từ và có たくさん -> 稼ぐ (かせぐ: kiếm tiền/thu nhập) dùng độc lập được, khác với 得る (đòi hỏi Nを).",
        "option_grammar_notes": [
            "かせいで: ĐÚNG. 仕事でたくさん稼いでいる (kiếm nhiều thu nhập từ công việc).",
            "得て: Động từ 得る bắt buộc phải có tân ngữ rõ ràng gắn を (例: 収入を得る).",
            "あげて: Nghĩa 'tặng' hoặc 'nâng lên', thiếu tân ngữ cụ thể và lệch nghĩa.",
            "受けて: 'Nhận/tham dự thi', đòi hỏi tân ngữ với を.",
        ],
    },
    # ID=122
    "719a830aef3734ed1b633fd1233aee50ec3a0dbf4c99da4981fd94a7a9019220": {
        "links": [
            {"grammar_code": "GP-N3-107", "role": "sentence_structure", "note_vi": "Cấu trúc trạng ngữ trang trọng V(ない) + ず [言わず] (= 言わないで: mà không nói dối)."},
            {"grammar_code": "GP-N5-03", "role": "sentence_structure", "note_vi": "Trợ từ で sau 本音 chỉ phương tiện/cách thức giao tiếp (trò chuyện bằng lời thật lòng)."},
            {"grammar_code": "GP-N5-11", "role": "sentence_structure", "note_vi": "Đuôi たい biểu đạt mong muốn thực hiện hành động 話し合いたい."},
        ],
        "structure_parse_vi": (
            "Điều kiện cách thức phủ định [うそを言わず]、(GP-N3-107) -> phương thức trao đổi [本音で] (GP-N5-03) + ý muốn tương hỗ [話し合いたい] (GP-N5-11)."
        ),
        "pedagogical_takeaway_vi": "Thấy khung [うそを言わず + ___で話し合う] -> chữ đứng trước で phải là 'tấm lòng thật / sự chân thực' (本音 đối lập với 建前).",
        "option_grammar_notes": [
            "意見: Thường đi với 意見を言う/交換する, không tự nhiên thành 意見で話し合う để đối chiếu với うそを言わず.",
            "本音 (ほんね): ĐÚNG. Lời thật đáy lòng (本音で話し合う).",
            "解答: Đáp án giải bài thi, lạc ngữ cảnh nói dối/nói thật.",
            "正解: Câu trả lời đúng bài trắc nghiệm.",
        ],
    },
    # ID=123
    "016d1192e7dd9a3115df675513e383574d94454ce854f80ef21e3c738e180eba": {
        "links": [
            {"grammar_code": "GP-N5-13", "role": "sentence_structure", "note_vi": "Mệnh đề nguyên nhân ～ので (vì vẫn còn mới nên...)."},
            {"grammar_code": "GP-N5-05", "role": "sentence_structure", "note_vi": "Phó từ mô tả tính chất ぴかぴか kết cấu vị ngữ danh từ/tính từ な với だ."},
        ],
        "structure_parse_vi": (
            "Nguyên nhân [この車は、まだ新しい + ので] (GP-N5-13) -> kết quả trạng thái [ぴかぴかだ] (GP-N5-05)."
        ),
        "pedagogical_takeaway_vi": "Kiểm tra sự tương thích ngữ nghĩa sau ～ので: 新しいので dẫn thẳng đến tính từ trạng thái bóng loáng mới tinh (ぴかぴか).",
        "option_grammar_notes": [
            "ぴかぴか: ĐÚNG. Sáng bóng, mới tinh (khớp với まだ新しいので).",
            "ふらふら: Chóng mặt loạng choạng/lang thang, sai chủ ngữ xe mới.",
            "ぺこぺこ: Đói meo bụng hoặc cúi rạp nịnh bợ.",
            "くるくる: Xoay tít mù liên tục, không phù hợp đặc tính 'vẫn còn mới'.",
        ],
    },
    # ID=124
    "fbea73fe0a01c29a971073d99527d79418b33b7506d6bd7884bc84a5377b4be0": {
        "links": [
            {"grammar_code": "GP-N3-047", "role": "sentence_structure", "note_vi": "Cấu trúc chủ đề trang trọng [その問題については] (về vấn đề đó thì...)."},
            {"grammar_code": "GP-N5-13", "role": "sentence_structure", "note_vi": "Nguyên nhân よくわからないので nối sang kết quả bất khả thi できません (GP-N4-01)."},
        ],
        "structure_parse_vi": (
            "Phạm vi chủ đề [その問題については]、(GP-N3-047) + lý do [よくわからないので] (GP-N5-13) -> khả năng phủ định [コメント + できません] (GP-N4-01)."
        ),
        "pedagogical_takeaway_vi": "Cặp [～についてはよくわからないので] luôn dẫn tới động từ phát ngôn/nhận xét dạng khả năng phủ định như コメントできません / 答えられません.",
        "option_grammar_notes": [
            "コート: Áo khoác / sân tennis (không chia thành コートできません).",
            "コンセント: Ổ cắm điện (danh từ đồ vật, không đi với できません ở đây).",
            "コンクール: Cuộc thi âm nhạc/nghệ thuật (sai với 問題 về ý kiến).",
            "コメント: ĐÚNG. Danh động từ Katakana: コメントする -> コメントできません.",
        ],
    },
    # ID=125
    "cc70ca6d597d46a0f117a143280ad23bb0130e24688b46bcbd8034a1ffdd4332": {
        "links": [
            {"grammar_code": "GP-N5-07", "role": "sentence_structure", "note_vi": "Danh từ hóa động từ [校庭の木の手入れを + する + のは] làm chủ ngữ cho tính từ 大変だ."},
            {"grammar_code": "GP-N5-02", "role": "sentence_structure", "note_vi": "Chuỗi bổ ngữ sở hữu 3 tầng [校庭の + 木の + 手入れ] + をする."},
        ],
        "structure_parse_vi": (
            "[毎日]、+ cụm danh từ hóa chủ ngữ [校庭の木の + 手入れをする + のは]、(GP-N5-07) + đánh giá [大変だ]."
        ),
        "pedagogical_takeaway_vi": "Bộ 4 từ ghép với 手 (Thủ): 手入れ (chăm sóc/bảo dưỡng cây, da, giày) vs 手引き (sách chỉ dẫn) vs 手出し (xen vào) vs 手抜き (làm ẩu).",
        "option_grammar_notes": [
            "手入れ (ていれ): ĐÚNG. Chăm sóc tỉa tót bảo dưỡng hằng ngày (木の手入れをする).",
            "手引き: Sách hướng dẫn, không phù hợp việc chăm sóc hàng ngày với cây.",
            "手出し: Can thiệp/động tay chân vào chuyện người khác.",
            "手抜き: Ăn bớt công đoạn/làm ẩu — mâu thuẫn với 毎日...大変だ.",
        ],
    },
    # ID=126
    "ca84ade578596af77eaf4f57b711a15fd2358957f27c07627acd5da9b08b9e2b": {
        "links": [
            {"grammar_code": "GP-N4-18", "role": "sentence_structure", "note_vi": "Cấu trúc sai khiến + cho nhận trong định ngữ [留学させてくれた + 両親]: bố mẹ đã cho phép tôi đi du học."},
            {"grammar_code": "GP-N5-03", "role": "sentence_structure", "note_vi": "Trợ từ に đánh dấu đối tượng tri ân [両親に + 感謝しています]."},
            {"grammar_code": "GP-N5-08", "role": "sentence_structure", "note_vi": "Trạng thái tâm lý liên tục hiện tại 感謝しています."},
        ],
        "structure_parse_vi": (
            "Cụm định ngữ sai khiến ân huệ [留学させてくれた] (GP-N4-02 + GP-N4-18 + GP-N5-06) + đối tượng tri ân [両親に] (GP-N5-03) "
            "+ vị ngữ tiếp diễn [感謝しています] (GP-N5-08)."
        ),
        "pedagogical_takeaway_vi": "Nhìn cụm định ngữ [～てくれた] (ân huệ cho mình) kết hợp với trợ từ に phía sau -> động từ tri ân phù hợp nhất là 感謝する.",
        "option_grammar_notes": [
            "成功: 'Thành công', đi với trợ từ に của việc gì (試験に成功する), không nhận đối tượng người 両親に.",
            "要望: 'Yêu cầu/đề nghị', không hợp tâm trạng biết ơn bố mẹ cho đi du học.",
            "救助: 'Giải cứu sinh mạng', sai ngữ cảnh gia đình du học.",
            "感謝 (かんしゃ): ĐÚNG. Biết ơn bố mẹ đã cho đi du học (両親に感謝する).",
        ],
    },
    # ID=127
    "0877ae6d82e0c76e822baca0573a57e9fa865a5bbfa855ba4ede7fcc26304d02": {
        "links": [
            {"grammar_code": "GP-N3-118", "role": "sentence_structure", "note_vi": "Khiêm nhường ngữ nhận quà ở định ngữ いただいた + 本 (cuốn sách đã được tặng)."},
            {"grammar_code": "GP-N4-17", "role": "sentence_structure", "note_vi": "Ý chí dự định đang tính [読もうと思います] (thể ý hướng Vよう + と思う)."},
        ],
        "structure_parse_vi": (
            "Định ngữ khiêm nhường [いただいた + 本を] (GP-N3-118 + GP-N5-06) + phó từ háo hức ngay [さっそく] + dự định [読もうと思います] (GP-N4-17)."
        ),
        "pedagogical_takeaway_vi": "Khi vừa nhận quà/thông tin lịch sự (いただいた本) đi kèm ý định bắt tay làm ngay (Vようと思う), phó từ chuẩn lịch sự là さっそく ('ngay lập tức/tranh thủ ngay').",
        "option_grammar_notes": [
            "やがて: 'Chẳng bao lâu nữa (tự nhiên biến chuyển)', không hợp dự định chủ động ngay lúc này.",
            "いきなり: 'Bỗng nhiên/đột ngột' (mang tính bất ngờ/thiếu báo trước), không dùng cho dự định cá nhân đọc sách vừa nhận.",
            "さっそく: ĐÚNG. Thể hiện sự háo hức bắt tay vào làm ngay sau khi nhận quà/tin.",
            "はっきり: 'Rõ ràng mạch lạc', không hợp bổ nghĩa thời điểm bắt đầu đọc.",
        ],
    },
    # ID=128
    "38493f77322ecfb91247715be06c3e379708dfa9a5aa677a1826756408daa76b": {
        "links": [
            {"grammar_code": "GP-N3-046", "role": "sentence_structure", "note_vi": "Liệt kê ví dụ điển hình 散歩やジョギング + など."},
            {"grammar_code": "GP-N5-03", "role": "sentence_structure", "note_vi": "Mẫu đánh giá tác dụng có lợi [Nに + よい] (tốt cho sức khỏe)."},
        ],
        "structure_parse_vi": (
            "Ví dụ liệt kê [散歩やジョギングなど]、(GP-N3-046) + chủ đề [軽い運動は] + đối tượng hưởng lợi [健康に + よい] (GP-N5-03)."
        ),
        "pedagogical_takeaway_vi": "Mẫu [Nによい / Nにいい] đánh giá lợi ích sức khỏe chỉ nhận danh từ trừu tượng 健康 (không ghép với 元気 hay 体重 trong ngữ cảnh chung).",
        "option_grammar_notes": [
            "体重: 'Cân nặng', không nói chung là 軽い運動は体重によい.",
            "元気: Tính từ な chỉ trạng thái sung sức, không tự nhiên bằng 健康によい.",
            "体温: 'Thân nhiệt', sai kết hợp.",
            "健康 (けんこう): ĐÚNG. Cụm cố định 健康によい / 健康にいい.",
        ],
    },
    # ID=129
    "3f6bf19d7de5f74e23790d24414b7187051cefc1e832ab9487003f7bdae3eba5": {
        "links": [
            {"grammar_code": "GP-N3-116", "role": "sentence_structure", "note_vi": "Hậu tố ～的 trong phương án đúng 否定的 (biến danh từ Hán-Nhật 否定 thành tính từ な)."},
            {"grammar_code": "GP-N5-05", "role": "sentence_structure", "note_vi": "Tính từ đuôi な kết thúc câu bằng だ (ネガティブだ = 否定的だ)."},
        ],
        "structure_parse_vi": (
            "[彼の考え方は]、(chủ đề) + trạng từ tần suất [いつも] + vị ngữ tính từ な [ネガティブだ] (= 否定的だ GP-N3-116)."
        ),
        "pedagogical_takeaway_vi": "Gặp cặp từ mượn đối lập ネガティブ (negative) vs ポジティブ (positive) nhớ ngay quy đổi Hán-Nhật đuôi 的: 否定的 vs 肯定的.",
        "option_grammar_notes": [
            "まじめ: Nghĩa 'nghiêm túc chăm chỉ', khác nghĩa tiêu cực bi quan.",
            "ふまじめ: Nghĩa 'thiếu nghiêm túc/lười nhác', sai nghĩa.",
            "肯定的 (こうていてき): Bẫy trái nghĩa ('tích cực/khẳng định' = positive).",
            "否定的 (ひていてき): ĐÚNG. Tương đương với ネガティブ (tiêu cực/phủ định).",
        ],
    },
    # ID=130
    "7f6619384d91090ee4c31da6efa6c835adb655efa0cd130559a0e7229e98dd09": {
        "links": [
            {"grammar_code": "GP-N5-10", "role": "sentence_structure", "note_vi": "Yêu cầu lịch sự Vてください (つないでください)."},
            {"grammar_code": "GP-N5-01", "role": "sentence_structure", "note_vi": "Nhóm 1 đuôi ぐ chia thể て biến âm thành いで (つなぐ -> つないで)."},
        ],
        "structure_parse_vi": (
            "Tân ngữ số đếm [2本の + ロープを] + tha động từ yêu cầu [つないでください] (GP-N5-01 + GP-N5-10)."
        ),
        "pedagogical_takeaway_vi": "Động từ つなぐ (nối dây, kết nối thiết bị) đồng nghĩa với danh động từ Hán-Nhật 接続する (tiếp tục/kết nối).",
        "option_grammar_notes": [
            "関係して: 'Liên quan tới', thường là tự động từ đi với に/と, không nối hai sợi dây.",
            "接続して: ĐÚNG. Đồng nghĩa chuẩn với つなぐ (kết nối hai vật/đoạn).",
            "注意して: 'Chú ý', sai nghĩa.",
            "切断して: Bẫy trái nghĩa hoàn toàn ('cắt đứt').",
        ],
    },
    # ID=131
    "78b32b6e0217b44bfdce7ffb696a01eba65fc4438e62123d9a95385b6c154dc3": {
        "links": [
            {"grammar_code": "GP-N5-06", "role": "sentence_structure", "note_vi": "Mệnh đề định ngữ 自分の言った bổ nghĩa cho danh từ trừu tượng こと làm tân ngữ với を."},
        ],
        "structure_parse_vi": (
            "[彼は]、(chủ ngữ) + tân ngữ định ngữ [自分の言った + ことを] (điều chính mình đã nói - GP-N5-06) + tha động từ kép quá khứ [打ち消した]."
        ),
        "pedagogical_takeaway_vi": "Động từ ghép tiền tố 打ち～ như 打ち消す (dập tắt, phủ nhận hoàn toàn) đồng nghĩa trực tiếp với 否定する.",
        "option_grammar_notes": [
            "忘れた: 'Đã quên', không mang hành động chủ động phủ bác lời nói.",
            "途中でやめた: 'Bỏ dở giữa chừng', sai nghĩa.",
            "否定した: ĐÚNG. Phủ nhận hoàn toàn điều vừa phát ngôn.",
            "そのままにした: 'Cứ để nguyên như thế', trái nghĩa bác bỏ.",
        ],
    },
    # ID=132
    "d54f9d1921f6e6ae68daeb12412bd20e2922bff305af22ca8864d4276b8de328": {
        "links": [
            {"grammar_code": "GP-N4-02", "role": "sentence_structure", "note_vi": "Thể sai khiến của tự động từ 終わる -> 終わらせる (làm cho công việc kết thúc)."},
            {"grammar_code": "GP-N5-02", "role": "sentence_structure", "note_vi": "Chuyển đổi từ tự động từ 仕事が終わる sang tha hóa bằng sai khiến 仕事を終わらせる."},
        ],
        "structure_parse_vi": (
            "Phó từ tác phong [さっさと] + tân ngữ [仕事を] + động từ sai khiến mang nghĩa hoàn thành chủ động [終わらせた] (GP-N4-02)."
        ),
        "pedagogical_takeaway_vi": "Khi muốn nói 'tự mình giải quyết xong một việc gì đó', tự động từ 終わる chuyển sang dạng 終わらせる (được nhận vào tân ngữ を).",
        "option_grammar_notes": [
            "早く (はやく): ĐÚNG. Đồng nghĩa với tác phong nhanh thoăn thoắt, dứt khoát của さっさと.",
            "ゆっくりと: Bẫy trái nghĩa ('chậm rãi thư thả').",
            "正確に: 'Chính xác', nói về chất lượng chứ không phải tốc độ nhanh gọn.",
            "だいたい: 'Đại khái', sai sắc thái dứt khoát.",
        ],
    },
    # ID=133
    "dd686e6e93fae6e039268b4579d8202b543f48ea39a2aff682ff87120ea0ec26": {
        "links": [
            {"grammar_code": "GP-N5-08", "role": "sentence_structure", "note_vi": "Vて + いる ở động từ tâm lý (落ち着いている) chỉ tính cách/trạng thái ổn định thường trực (luôn điềm tĩnh)."},
        ],
        "structure_parse_vi": (
            "[彼女は]、(chủ đề) + phó từ tần suất [いつも] + tính từ hóa trạng thái bằng ている [落ち着いている] (GP-N5-08)."
        ),
        "pedagogical_takeaway_vi": "Động từ trạng thái tâm lý 落ち着いている ('bình tĩnh, vững vàng') tương đương trực tiếp với tính từ な 冷静だ.",
        "option_grammar_notes": [
            "優秀だ: 'Ưu tú, xuất sắc (về năng lực/thành tích)', không đồng nghĩa 'bình tĩnh'.",
            "有能だ: 'Có tài năng/giỏi việc', lệch nét nghĩa tâm lý.",
            "冷静だ: ĐÚNG. Điềm tĩnh, không hoảng loạn.",
            "温厚だ: 'Ôn hòa hiền hậu', thiên về tính nết hiền lành hơn sự điềm tĩnh xử lý việc.",
        ],
    },
    # ID=134
    "31ea3d1502ba16616c40403d581212e05d6201de3368861b0c0b8433a6f252e6": {
        "links": [
            {"grammar_code": "GP-N4-13", "role": "sentence_structure", "note_vi": "Trong Option 2 đúng: mệnh đề nguyên nhân ～ので dẫn vào quyết định chủ quan 買うことにした (Vることにする)."},
            {"grammar_code": "GP-N5-02", "role": "sentence_structure", "note_vi": "Cấu trúc đánh giá ưng ý nhận chủ thể đối tượng với が: Nが + 気に入った."},
        ],
        "structure_parse_vi": (
            "Câu đúng (Option 2): chủ thể đánh giá [その店の服が] + phó từ [とても] + động từ tâm lý [気に入った + ので] (GP-N5-13) "
            "-> quyết định hành động [買うことにした] (GP-N4-13)."
        ),
        "pedagogical_takeaway_vi": "Thuộc lòng bộ 4 thành ngữ với 気: 気に入る (ưng ý với が) / 気になる (bận tâm) / 気がする (có linh cảm) / 気がつく (nhận ra với に).",
        "option_grammar_notes": [
            "Sentence 1: Lo lắng bận tâm phải dùng 気になって (không dùng 気に入って).",
            "Sentence 2: ĐÚNG. その店の服が気に入ったので買うことにした (ưng ý bộ đồ nên quyết định mua).",
            "Sentence 3: Linh cảm về thời tiết phải dùng 気がする (bắt buộc ~ような気がする).",
            "Sentence 4: Nhận ra sự việc quên ví phải dùng 気がついた.",
        ],
    },
    # ID=135
    "7dca90943ba35c41c45f98813492a66b62851d417b00933eac8e6f160d6f04cc": {
        "links": [
            {"grammar_code": "GP-N5-18", "role": "sentence_structure", "note_vi": "Tha động từ 混ぜる (まぜる) nhận hai danh từ nối bằng と làm tân ngữ với を (たまごと牛乳を混ぜる)."},
            {"grammar_code": "GP-N5-10", "role": "sentence_structure", "note_vi": "Động từ nhóm 2 混ぜる chia yêu cầu lịch sự 混ぜてください."},
        ],
        "structure_parse_vi": (
            "Câu đúng (Option 3): tân ngữ song hành [たまごと + 牛乳を] + phó từ mức độ [よく] + yêu cầu tha động từ [まぜてください] (GP-N5-18 + GP-N5-10)."
        ),
        "pedagogical_takeaway_vi": "Tha động từ 混ぜる bắt buộc nối ít nhất 2 vật liệu có thể hòa trộn bằng trợ từ と + を (không dùng để cắm hoa hay rửa mặt).",
        "option_grammar_notes": [
            "Sentence 1: Cắm hoa vào bình dùng 生ける hoặc 飾る.",
            "Sentence 2: Đính khâu cúc vào áo dùng つける hoặc 縫いつける.",
            "Sentence 3: ĐÚNG. たまごと牛乳をよく混ぜてください (trộn đều trứng và sữa).",
            "Sentence 4: Rửa mặt phải dùng 洗う (顔を洗う).",
        ],
    },
    # ID=136
    "d3a00806b0697b231b72e77509e4e87aaa46c2c497820f5e8673eb9ab3976fc9": {
        "links": [
            {"grammar_code": "GP-N4-01", "role": "sentence_structure", "note_vi": "Thể khả năng phủ định 思えない (không thể nghĩ/tin nổi) gắn sau trích dẫn とは."},
            {"grammar_code": "GP-N5-06", "role": "sentence_structure", "note_vi": "Mệnh đề định ngữ dài [とても現実とは思えない] bổ nghĩa trực tiếp cho danh từ ニュース."},
        ],
        "structure_parse_vi": (
            "Câu đúng (Option 4): cụm định ngữ mức độ bất ngờ [とても + 現実とは + 思えない] (GP-N4-01 + GP-N5-06) + tân ngữ [ニュースを] + [聞いた]."
        ),
        "pedagogical_takeaway_vi": "Phân biệt từ gốc 現: 現実 (thực tế khách quan, hay đi trong cụm 現実とは思えない) vs 実感 (cảm giác thực sự じっかんがわく) vs 現在 (thời hiện tại).",
        "option_grammar_notes": [
            "Sentence 1: Giỏi thực thi hơn suy nghĩ dùng 実行 hoặc 行動.",
            "Sentence 2: Chưa thấy cảm giác thật là đã đỗ dùng cụm cố định 実感 (じっかん) がわかない.",
            "Sentence 3: Thời đại hiện nay (đối chiếu 昔) dùng 現在 hoặc 現代.",
            "Sentence 4: ĐÚNG. とても現実とは思えないニュース (tin tức khó tin là sự thật).",
        ],
    },
    # ID=137
    "dda6b2b988230287570210c4f6ced612b7693e5325669255374a52240015d312": {
        "links": [
            {"grammar_code": "GP-N5-02", "role": "sentence_structure", "note_vi": "Khung định nghĩa chủ ngữ [今日の晩ごはんの + おかずは]、+ vị ngữ liệt kê [肉と野菜の料理です]."},
            {"grammar_code": "GP-N3-002", "role": "sentence_structure", "note_vi": "Phương án 1 chứa cấu trúc khoảng thời gian 昼食と夕食のあいだの (trong khoảng giữa bữa trưa và bữa tối)."},
        ],
        "structure_parse_vi": (
            "Câu đúng (Option 2): chủ đề danh từ 2 lớp sở hữu [今日の晩ごはんの + おかずは]、-> giải thích món ăn [肉と野菜の + 料理です]."
        ),
        "pedagogical_takeaway_vi": "おかず chỉ thức ăn mặn/rau dùng kèm cơm (đối lập với 主食 như cơm/bánh mì và bữa xế おやつ).",
        "option_grammar_notes": [
            "Sentence 1: Đồ ăn vặt buổi chiều giữa trưa và tối phải dùng おやつ.",
            "Sentence 2: ĐÚNG. 晩ごはんのおかずは肉と野菜の料理です.",
            "Sentence 3: Đun sôi nước pha trà dùng お湯 (お湯を沸かす).",
            "Sentence 4: Cơm và bánh mì là lương thực chính (主食), không phải món kèm おかず.",
        ],
    },
    # ID=138
    "f8d8c878259b4a48a3fd30b4a5d13959fc903023481e586b7dd6ff53223e49ed": {
        "links": [
            {"grammar_code": "GP-N3-083", "role": "sentence_structure", "note_vi": "Tự động từ ghép Vます + 上がる (出来上がる): món ăn/tác phẩm đã hoàn thành xong xuôi."},
            {"grammar_code": "GP-N5-13", "role": "sentence_structure", "note_vi": "Mệnh đề nguyên nhân hoàn tất できあがったので dẫn vào lời mời lịch sự 食べてください (GP-N5-10)."},
        ],
        "structure_parse_vi": (
            "Câu đúng (Option 4): [料理が + できあがった + ので]、(chủ ngữ tự động từ GP-N3-083 + GP-N5-13) -> lời mời [食べてください] (GP-N5-10)."
        ),
        "pedagogical_takeaway_vi": "Động từ ghép 出来上がる (hoàn thiện sản phẩm/món ăn/công trình) là tự động từ đi với trợ từ が, KHÔNG dùng thay cho 'trở thành' (になる) hay 'đi lên' (上がる).",
        "option_grammar_notes": [
            "Sentence 1: Trở thành giáo viên phải dùng 先生になる.",
            "Sentence 2: Đi thang máy lên tầng 10 phải dùng 上がる (あがる).",
            "Sentence 3: Đi hết cầu thang phải dùng 上がる / 登る.",
            "Sentence 4: ĐÚNG. 料理ができあがったので、食べてください.",
        ],
    },
    # =========================================================================
    # SECTION 3: READING (23 QUESTIONS: IDs 30-34, 64-68, 139-145, 158-163)
    # =========================================================================
    # ID=30
    "cd0fd32432ed79a55fadf53de25be66ad11b737efd2deffb50dc2daf29715711": {
        "links": [
            {"grammar_code": "GP-N5-15", "role": "discourse_marker", "note_vi": "Liên từ đối lập 「しかし」 trong bài đọc đảo hướng từ ý kiến xã hội sang chủ trương của tác giả."},
            {"grammar_code": "GP-N3-015", "role": "discourse_marker", "note_vi": "Bài đọc (PID=2) sử dụng cấu trúc đối chiếu 一方で nêu chiều ngược lại của hai nhóm môn học."},
            {"grammar_code": "GP-N4-20", "role": "sentence_structure", "note_vi": "Đuôi truyền đạt ～そうだ (増えているそうだ) đánh dấu ý kiến của một số người mà tác giả không đồng tình hoàn toàn."},
            {"grammar_code": "GP-N3-052", "role": "sentence_structure", "note_vi": "Cấu trúc so sánh tương đồng 同じように (Option 3) diễn đạt sự cân bằng giá trị giữa các môn học."},
        ],
        "structure_parse_vi": (
            "Cấu trúc mạch văn nghị luận (PID=2): [～と言う人も増えているそうだ] (trích dẫn dư luận - GP-N4-20) "
            "-> bước ngoặt đối lập [しかし] (GP-N5-15) -> mệnh đề chủ chốt [他の科目も重要であることは変わらない] (danh từ hóa こと + は). "
            "Câu hỏi sử dụng cấu trúc [Nと + 合っているものはどれか]."
        ),
        "pedagogical_takeaway_vi": "Khi thấy mẫu trích dẫn dư luận (～そうだ / ～と言われている) rồi theo sau bởi 「しかし」, câu chốt ý kiến thật của tác giả luôn nằm NGAY SAU 「しかし」.",
        "option_grammar_notes": [
            "Option 1: Dùng trợ từ so sánh ～より (hơn là), xuyên tạc chủ trương cân bằng của tác giả.",
            "Option 2: Đảo ngược phép so sánh ～より ở Option 1, vẫn sai tinh thần cân bằng mọi môn học.",
            "Option 3: ĐÚNG. Dùng ～と同じように (giống như) diễn tả đúng giá trị bình đẳng của các môn học.",
            "Option 4: Lấy phần ý kiến dư luận bị tác giả bác bỏ trước しかし làm kết luận toàn bài.",
        ],
    },
    # ID=31
    "150f95e96c07860d96e0bec736983d01cff54cb0b2f2fbca8820167db63ecf18": {
        "links": [
            {"grammar_code": "GP-N5-15", "role": "discourse_marker", "note_vi": "Liên từ bổ sung 「それに」 (thêm vào đó) nối đủ 2 luận cứ cho đáp án."},
            {"grammar_code": "GP-N5-14", "role": "sentence_structure", "note_vi": "Cấu trúc liệt kê nguyên nhân song song trong Option 3: Aい + し、Vる + から (危ないし、耳が悪くなるから)."},
            {"grammar_code": "GP-N4-04", "role": "sentence_structure", "note_vi": "Bài đọc (PID=3) sử dụng thể sai khiến bị động 思わせられることがある ('khiến mình bị ép phải nghĩ rằng')."},
            {"grammar_code": "GP-N4-10", "role": "sentence_structure", "note_vi": "Đuôi 聞こえにくくなる trong bài đọc chuyển nghĩa thành 耳が悪くなる ở phương án đúng."},
            {"grammar_code": "GP-N3-114", "role": "sentence_structure", "note_vi": "Bài đọc (PID=3) nhắc hệ quả nhận biết 結果 khi đánh giá thói quen nghe nhạc lớn."},
        ],
        "structure_parse_vi": (
            "Cấu trúc bài đọc (PID=3): Đặt vấn đề tu từ [～はどうだろうか] -> Luận cứ 1 [後ろから車が来てもわからない] (nhượng bộ ても -> nguy hiểm) "
            "+ liên từ cộng thêm [それに] (GP-N5-15) -> Luận cứ 2 [小さい音が聞こえにくくなる] (Vます + にくくなる GP-N4-10 + GP-N5-05). "
            "Đáp án tóm tắt bằng cấu trúc liệt kê song song ～し～し + から (GP-N5-14)."
        ),
        "pedagogical_takeaway_vi": "Thấy từ nối それに nối 2 câu nhược điểm trong bài đọc, đáp án đúng thường dùng mẫu Aし、Bから gom đủ cả 2 ý chứ không lấy một nửa.",
        "option_grammar_notes": [
            "Option 1: Dùng 迷惑になるから — suy diễn ý chưa được tác giả kết luận.",
            "Option 2: Dùng sai khiến 心配させるから (làm người khác lo), lệch khỏi nội dung bài.",
            "Option 3: ĐÚNG. Cặp ～し...から khớp hoàn toàn cả 2 lý do trước và sau それに.",
            "Option 4: Sai ngữ pháp đọc hiểu vì chỉ trích xuất phiến diện ý cuối, bỏ sót yếu tố 危ない.",
        ],
    },
    # ID=32
    "fa87a41efd4ed5c1d9f8abeac6f0115384c963da52a67732ed40313e0a9240ea": {
        "links": [
            {"grammar_code": "GP-N4-15", "role": "sentence_structure", "note_vi": "Cụm chuyển biến khả năng Vえる + ようになった (捕れるようになった = trở nên đánh bắt dễ dàng được)."},
            {"grammar_code": "GP-N4-03", "role": "sentence_structure", "note_vi": "Thể bị động 大量に捕られるようになった diễn tả lượng cá bị đánh bắt hàng loạt."},
            {"grammar_code": "GP-N3-048", "role": "sentence_structure", "note_vi": "Mẫu danh từ lập trường Nにとって (マグロにとって) dùng trong bẫy số 2."},
            {"grammar_code": "GP-N3-114", "role": "discourse_marker", "note_vi": "Bài đọc (PID=4) dùng cấu trúc その結果 / の結果 nối diễn biến công nghệ đánh bắt sang suy giảm số lượng cá."},
        ],
        "structure_parse_vi": (
            "Câu hỏi chẻ [最も大きな原因は + 何か] (nguyên nhân lớn nhất). "
            "Trong bài đọc (PID=4): [一番の原因は、魚を捕る技術が発達したことだ] (danh từ hóa ことだ) -> hệ quả [大量に捕られるようになった] (bị động + ようになる GP-N4-03 + GP-N4-15)."
        ),
        "pedagogical_takeaway_vi": "Cảnh giác bẫy so sánh cấp bậc: đề hỏi 最も大きな原因 (tương ứng 一番の原因) khác hoàn toàn với 原因の一つ (một trong các nguyên nhân phụ).",
        "option_grammar_notes": [
            "Option 1: Danh từ hóa ～こと kết nối nguyên nhân giá rẻ (trái thực tế khan hiếm).",
            "Option 2: Bẫy dùng ～にとって ('đối với cá ngừ') gắn vào nguyên nhân phụ 原因の一つ.",
            "Option 3: ĐÚNG. Cụm 捕れるようになったこと khớp chuẩn bị động/khả năng trong câu 一番の原因は.",
            "Option 4: Nêu nguyên nhân phụ thiếu trọng tâm từ sự phổ biến.",
        ],
    },
    # ID=33
    "e40e85639f7198f516294348f8f8ce3d274516154d5af6141a07cb9c1a03cc24": {
        "links": [
            {"grammar_code": "GP-N5-06", "role": "sentence_structure", "note_vi": "Mệnh đề định ngữ dài [マグロを捕る + ことができる + 量を + 決めた] bổ nghĩa cho danh từ [ルール]."},
            {"grammar_code": "GP-N4-03", "role": "sentence_structure", "note_vi": "Bị động tiếp diễn 守られていない (quy tắc đang không được tuân thủ) nối với ～とあるが."},
            {"grammar_code": "GP-N3-005", "role": "sentence_structure", "note_vi": "Cách chia nhóm danh từ Quốc gia trong bài đọc 国ごとに ('từng quốc gia một')."},
        ],
        "structure_parse_vi": (
            "Câu hỏi [守られていない + とあるが、何が + 守られていないのか] (GP-N4-03 + GP-N3-028 trích dẫn đề bài). "
            "Truy vết cụm [このルール] -> định ngữ bài đọc [マグロを捕ってもいい量を国ごとに定めた国際的な決まり]."
        ),
        "pedagogical_takeaway_vi": "Định ngữ đứng ngay trước từ trung tâm (決まり / ルール) chính là nội dung định nghĩa cho đại từ chỉ thị (このルール).",
        "option_grammar_notes": [
            "Option 1: ĐÚNG. Định ngữ 量を決めたルール dịch đúng từ 量を定めた決まり trong bài.",
            "Option 2: Đổi sai danh từ trung tâm định ngữ từ 'sản lượng' (量) sang 'người' (人).",
            "Option 3: Gài bẫy cấm đoán ～てはいけない (không có quy định cấm bắt cá con).",
            "Option 4: Gài bẫy nghĩa vụ ～なければならない về môi trường chung.",
        ],
    },
    # ID=34
    "8dc9356e84fb8ecca2e8495dcb93b65b3e747180a56ab7c1732207b9cc81f508": {
        "links": [
            {"grammar_code": "GP-N4-24", "role": "discourse_marker", "note_vi": "Câu hỏi tu từ cuối bài ～ではないだろうか khẳng định chủ trương mềm mại của tác giả."},
            {"grammar_code": "GP-N5-09", "role": "sentence_structure", "note_vi": "Lời khuyên Vたほうがいい ở đáp án đúng (捕るのをやめたほうがいい) truyền đạt đề xuất tác giả."},
            {"grammar_code": "GP-N3-040", "role": "distractor_trap", "note_vi": "Bẫy べきだ trong Option 4 dùng nghĩa vụ mạnh cho nội dung đảo ngược hoàn toàn ý tác giả."},
            {"grammar_code": "GP-N4-19", "role": "sentence_structure", "note_vi": "Câu lập luận nền trong bài dùng ～少なくないはずだ (chắc chắn lượng vứt bỏ không hề ít)."},
        ],
        "structure_parse_vi": (
            "Cấu trúc lập luận kết bài (PID=4): Suy luận logic [少なくないはずだ] (GP-N4-19) "
            "-> chủ trương chính ở câu kết [消費に合った量のマグロを捕るようにすることも + 重要ではないだろうか] (GP-N4-15 + GP-N4-24). "
            "Câu hỏi dùng mẫu [～について + どう考えているか] (GP-N3-047)."
        ),
        "pedagogical_takeaway_vi": "Ở đoạn kết bài nghị luận, mẫu ～ではないだろうか chính là khẳng định quan điểm của tác giả (tương đương ～たほうがいい / 重要だ).",
        "option_grammar_notes": [
            "Option 1: Đánh giá sai phủ định 'không ngon', trái miêu tả sự phổ biến trong bài.",
            "Option 2: ĐÚNG. Cụm 必要以上に...やめたほうがいい (GP-N5-09) diễn giải đúng 消費に合った量...重要ではないだろうか.",
            "Option 3: Dùng sai mẫu 必要以上に...特別なものだと考えている (ngược với từ khóa 気軽に trong bài).",
            "Option 4: Dùng nghĩa vụ べきだ (GP-N3-040) cổ súy đánh bắt nhiều hơn, ngược lập luận bài.",
        ],
    },
    # ID=64
    "508ec4b8eb49864549ccbde62f4f28d25994ab0e2e8c92d8bc9b4ad1722cf5b1": {
        "links": [
            {"grammar_code": "GP-N3-040", "role": "sentence_structure", "note_vi": "Cấu trúc câu hỏi [～なければならないか] hỏi về hành động bắt buộc phải thực hiện."},
            {"grammar_code": "GP-N5-04", "role": "sentence_structure", "note_vi": "Phân biệt chuẩn mốc hạn chót 4月6日までに (hoàn thành trước 6/4)."},
            {"grammar_code": "GP-N3-002", "role": "sentence_structure", "note_vi": "Khoảng thời gian chọn ngày thay thế dùng 17日から19日の間で (GP-N3-002 ～間 / ～間に)."},
            {"grammar_code": "GP-N3-004", "role": "sentence_structure", "note_vi": "Bài đọc (PID=6) dẫn nội dung chi tiết bên dưới bằng cụm ～のとおり (theo như dưới đây)."},
            {"grammar_code": "GP-N4-23", "role": "sentence_structure", "note_vi": "Kính ngữ hành động email trong bài: お返事ください / お知らせください."},
            {"grammar_code": "GP-N5-15", "role": "discourse_marker", "note_vi": "Từ nối bổ sung điều kiện 「また」 tách riêng yêu cầu dành cho người vắng mặt (出席できない人)."},
        ],
        "structure_parse_vi": (
            "Cấu trúc Email (PID=6): Yêu cầu chung [出席できるかどうか、4月6日までにお返事ください] (nhấn mạnh hạn chót までに GP-N5-04) "
            "+ bổ sung [また、出席できない人は、...参加できる日をあわせてお知らせください] (GP-N4-23). "
            "Câu hỏi định ngữ [4月20日の会議に出席できない人は] (GP-N4-01 + GP-N5-06)."
        ),
        "pedagogical_takeaway_vi": "Trong email công việc, đừng bỏ sót câu bắt đầu bằng 「また、～できない人は」 vì đây thường là nơi cài điều kiện riêng cho câu hỏi đọc hiểu.",
        "option_grammar_notes": [
            "Option 1: Sai đối tượng định ngữ (đề hỏi người KHÔNG dự được ngày 20/4).",
            "Option 2: ĐÚNG. Hạn chót 4月6日までに + 伝える khớp hoàn toàn お返事ください / お知らせください.",
            "Option 3: Trộn lẫn khoảng ngày chọn lịch họp mới với hành động tự ý đến địa điểm.",
            "Option 4: Ghép sai phương thức gửi email cho ý tưởng thảo luận trực tiếp trong họp.",
        ],
    },
    # ID=65
    "6a62e07e73535e7e258f247224326e27ff38a4a3992e121ad819ee1162359a8c": {
        "links": [
            {"grammar_code": "GP-N3-049", "role": "sentence_structure", "note_vi": "Cấu trúc câu hỏi [～の行動として、正しいものはどれか]: xét hành động hợp lệ với tư cách người tham gia."},
            {"grammar_code": "GP-N3-004", "role": "sentence_structure", "note_vi": "Tờ rơi (PID=7) sử dụng mẫu 以下のとおり / ～の通り để dẫn danh mục quy định tiếp nhận sách."},
            {"grammar_code": "GP-N4-23", "role": "sentence_structure", "note_vi": "Kính ngữ hướng dẫn trong tờ rơi お持ちになり... お越しください (お + Vます + になる / くださる)."},
            {"grammar_code": "GP-N4-16", "role": "sentence_structure", "note_vi": "Các phương án dùng câu điều kiện ～ば / ～たら kiểm tra hai nhánh danh sách cho/không cho phép."},
        ],
        "structure_parse_vi": (
            "Tờ rơi thông tin (PID=7): Phân nhóm tiêu chí bằng cụm định ngữ đối lập [対象とする本] vs [対象としない本] "
            "-> yêu cầu hình thức mang trực tiếp bằng kính ngữ [お持ちになり... お越しください] (GP-N4-23). "
            "Đáp án dùng câu điều kiện [いらない絵本があれば、...持っていく] (GP-N4-16)."
        ),
        "pedagogical_takeaway_vi": "Tờ rơi tuyển quyên góp luôn bẫy ở 2 điểm: (1) Danh mục loại trừ (対象としない); (2) Phương thức tự mang đến (持参/お持ちになる) vs gửi bưu điện (送る).",
        "option_grammar_notes": [
            "Option 1: Sai chủ thể bán sách (Trung tâm tổ chức bán quyên góp chứ không phải cá nhân tự bán).",
            "Option 2: Chọn sách giáo khoa (教科書) thuộc danh mục loại trừ (対象としない本).",
            "Option 3: Thay đổi phương thức sang 送る (gửi bưu điện), trái với お持ちになり.",
            "Option 4: ĐÚNG. Đáp ứng đủ cả điều kiện loại sách (絵本) và hành động tự mang tới (持っていく).",
        ],
    },
    # ID=66
    "8a3cc36d3080e649d13f081f855fc7598613bf749d972574c2f16a3b5fe6f188": {
        "links": [
            {"grammar_code": "GP-N4-18", "role": "sentence_structure", "note_vi": "Cụm cho nhận cảm kích ～てくれた (包んでくれた / リボンをつけてくれた): tiệm hoa làm giúp cho mình."},
            {"grammar_code": "GP-N4-06", "role": "sentence_structure", "note_vi": "Thể trạng thái bị động phủ định ラッピングがされていなかった mô tả sự cố ban đầu."},
            {"grammar_code": "GP-N3-028", "role": "sentence_structure", "note_vi": "Câu hỏi trích dẫn cảm xúc [本当に助かったとあるが、何が助かったと言っているか]."},
        ],
        "structure_parse_vi": (
            "Mạch kể chuyện (PID=8): Sự cố phát hiện [ラッピングがされていなかった] (bị động trạng thái phủ định GP-N4-03 + GP-N5-08) "
            "-> giải pháp cứu nguy từ tiệm hoa [きれいな紙で箱を包み、リボンをつけてくれた] (GP-N4-18) -> cảm xúc kết [本当に助かった]."
        ),
        "pedagogical_takeaway_vi": "Câu hỏi truy nguyên từ cảm xúc [本当に助かった] luôn gắn với hành động mang cấu trúc ～てくれた của người giúp mình giải quyết đúng nút thắt trước đó.",
        "option_grammar_notes": [
            "Option 1: Đưa từ 'hoa' (花とリボン) ghép vào hộp bánh nhờ bị động つけられた (bịa chi tiết).",
            "Option 2: Đổi sai chủ thể thực hiện hành động ～てくれた từ tiệm hoa sang tiệm bánh.",
            "Option 3: ĐÚNG. Khớp chuẩn 100% với 花屋さんが + 包んでくれた.",
            "Option 4: Chỉ là bối cảnh đặt hàng mở đầu, không phải điểm cứu nguy tạo ra cảm giác 助かった.",
        ],
    },
    # ID=67
    "21a80a1694fab31d42282fec75af66b99eb32b4f3d4018a2bd888d124e467762": {
        "links": [
            {"grammar_code": "GP-N3-031", "role": "sentence_structure", "note_vi": "Phủ định một phần cuối bài: すべてが同じというわけではない (màu cảm nhận ở mỗi người không hoàn toàn giống nhau)."},
            {"grammar_code": "GP-N3-026", "role": "sentence_structure", "note_vi": "Trích dẫn kiến thức khoa học ～とも言われている và ～のだそうだ (GP-N4-20)."},
            {"grammar_code": "GP-N4-09", "role": "sentence_structure", "note_vi": "Vế đối lập trong bài dùng 残ってしまう (tuy mất dần khi lớn nhưng vẫn sót lại ở một số người)."},
            {"grammar_code": "GP-N4-16", "role": "sentence_structure", "note_vi": "Chuyển đổi mệnh đề tương đương giữa ～と失われる và ～てもなくなることが多い."},
        ],
        "structure_parse_vi": (
            "Đoạn văn giải thích hiện tượng (PID=9): [赤ちゃんのころは誰でも...と言われている] (GP-N3-026) "
            "-> quy luật chung [普通は + 成長すると + 失われていくものなのだ + が] (GP-N4-16 + GP-N4-08 + GP-N3-097) "
            "-> ngoại lệ [一部の大人には残ってしまうのだそうだ] (GP-N4-09 + GP-N4-20)."
        ),
        "pedagogical_takeaway_vi": "Paraphrase kinh điển ở N3: câu ghép đối lập [AするとBいくものなのだが、一部...] trong bài chuyển sang câu hỏi tổng quát thành [AてもBことが多い].",
        "option_grammar_notes": [
            "Option 1: Đánh tráo 一部の大人 thành すべての人 (lỗi lượng từ tuyệt đối).",
            "Option 2: Đảo ngược thái độ cảm nhận từ tích cực sang 嫌だと感じる.",
            "Option 3: ĐÚNG. Diễn đạt lại chuẩn xác câu 普通は成長すると失われていくものなのだ bằng てもなくなることが多い.",
            "Option 4: Khẳng định 皆同じである, trái ngược trực tiếp với すべてが同じというわけではない (GP-N3-031).",
        ],
    },
    # ID=68
    "bdad9f1ab96bacf698b74c620370d42e21daab80ea0d85568d25bb2716c330b8": {
        "links": [
            {"grammar_code": "GP-N3-038", "role": "sentence_structure", "note_vi": "Lời nhắn gián tiếp yêu cầu chuyển đạt: ～ように伝えてください (hãy nhắn với các bạn khác rằng...)."},
            {"grammar_code": "GP-N3-024", "role": "sentence_structure", "note_vi": "Điều kiện bất khả kháng nếu không thể đi: [もし、どうしても + 出席できない場合は] (GP-N4-01)."},
            {"grammar_code": "GP-N5-04", "role": "sentence_structure", "note_vi": "Thời hạn bắt buộc báo vắng trước ngày 19: 19日(月)までに."},
        ],
        "structure_parse_vi": (
            "Lời nhắn trong Memo (PID=10): Điều kiện giả thiết [もし、どうしても + 出席できない + 場合は] (GP-N4-01 + GP-N5-06) "
            "-> yêu cầu có hạn chót [19日までに + わたしに連絡する + ように] (GP-N5-04) + chuyển lời [伝えてください] (GP-N3-038)."
        ),
        "pedagogical_takeaway_vi": "Trong đề tin nhắn/memo có câu chốt 「～ように伝えてください」, nội dung ngay trước ように chính là đáp án câu hỏi 'nhắn lại điều gì'.",
        "option_grammar_notes": [
            "Option 1: Đưa hành động suy nghĩ trước (~ておく GP-N4-05) vào nội dung không được yêu cầu.",
            "Option 2: ĐÚNG. Tường thuật chuẩn xác [出席できない場合は、19日までに...知らせること].",
            "Option 3: Sai mục tiêu liên hệ (thầy đã ấn định nội dung chuẩn bị diễn thuyết).",
            "Option 4: Đánh tráo điều kiện sang cả người đi lẫn người vắng (～人も～人も), trái hẳn どうしても出席できない場合.",
        ],
    },
    # ID=139
    "eecd1e55ce7a4c0599d9a2539f9aad6dd567553d2d1903b0819ef38d7f08dda5": {
        "links": [
            {"grammar_code": "GP-N4-20", "role": "sentence_structure", "note_vi": "Truyền đạt tin nghe nói 入院したらしい (nghe nói anh/chị Ogawa đã nhập viện)."},
            {"grammar_code": "GP-N5-10", "role": "sentence_structure", "note_vi": "Lời chúc ở cuối thư 早くお元気になってください (mong sớm khỏe lại - GP-N4-23 + GP-N5-05)."},
            {"grammar_code": "GP-N4-12", "role": "sentence_structure", "note_vi": "Câu hỏi xác định người nhận và mục đích viết thư dùng [だれに + 何のために]."},
        ],
        "structure_parse_vi": (
            "Mạng lưới nhân vật trong thư (PID=11): Người gửi [小池一郎] (cuối thư) -> Người truyền tin gián tiếp [大木 -> 田中 -> 小池] "
            "-> Người được nhắc tin nhập viện & Người nhận thư [小川さんが入院したらしい] (GP-N4-20) -> lời chúc [早くお元気になってください] (GP-N4-23)."
        ),
        "pedagogical_takeaway_vi": "Trong bài thư có 3-4 tên riêng, hãy tách rõ: ai đứng cuối thư là người viết, ai được gọi bằng lời chúc trực tiếp ở cuối là người nhận.",
        "option_grammar_notes": [
            "Option 1: Nhầm người nhận sang Tanaka và nhầm mục đích sang lời chào mùa hè mở đầu thư.",
            "Option 2: Đúng người nhận Ogawa nhưng nhầm lý do phụ ('gọi về nhà không bắt máy') thành mục đích chính.",
            "Option 3: Nhầm người nhận sang Oki (chỉ là người truyền tin trung gian).",
            "Option 4: ĐÚNG. Người nhận là 小川さん và mục đích là thăm hỏi lo lắng vì bị ốm nhập viện.",
        ],
    },
    # ID=140
    "0a292c7d376c621dbfd170c9ab353253f7a43d484b9d2c1ecda4611a750de587": {
        "links": [
            {"grammar_code": "GP-N5-01", "role": "sentence_structure", "note_vi": "Trình tự thời gian hành động [帰ってから + すぐ] (ngay sau khi từ viện về nhà thì đã viết thư)."},
            {"grammar_code": "GP-N3-028", "role": "sentence_structure", "note_vi": "Đáp án đúng dùng mệnh đề bổ nghĩa nội dung bức thư [～が失礼だった + という + 手紙]."},
            {"grammar_code": "GP-N4-18", "role": "sentence_structure", "note_vi": "Bẫy Option 3 dựa trên cụm kính ngữ bối cảnh お世話になっている (đang được giúp đỡ)."},
        ],
        "structure_parse_vi": (
            "Chuỗi sự kiện tâm lý (PID=12): Bối cảnh [お世話になっている] -> mang hoa cúc tới thăm -> được anh Ishii giải thích -> nhận thức [意味がよくわかりました] "
            "-> phản ứng tức thì [帰ってからすぐ] (Vてから GP-N5-01) -> suy luận nội dung thư [お見舞いの花が失礼だったという手紙] (GP-N3-028)."
        ),
        "pedagogical_takeaway_vi": "Khi câu văn kết thúc ở hành động phản ứng [帰ってからすぐ書いた], phải nối với nhận thức vừa vỡ lẽ ở câu ngay trước đó chứ không quay về lời xã giao câu đầu.",
        "option_grammar_notes": [
            "Option 1: Bẫy hiểu sai trạng thái nhận thức ('hỏi lý do' dù tác giả đã hiểu ra ngay trước đó).",
            "Option 2: Bẫy thời gian — việc đi thăm bệnh đã làm trực tiếp ở bệnh viện rồi.",
            "Option 3: Bẫy lấy cụm bối cảnh đầu đoạn (お世話になっている) gán làm nội dung chính của bức thư sau cùng.",
            "Option 4: ĐÚNG. Định ngữ ～が失礼だったという phản ánh chính xác ý thức xin lỗi sau khi hiểu sự việc.",
        ],
    },
    # ID=141
    "6205e5de1619999796be430f7bfbefea6387b2acb67508b61adbba9c79f03706": {
        "links": [
            {"grammar_code": "GP-N5-15", "role": "discourse_marker", "note_vi": "Liên kết tương phản đánh giá [とても大変だけど、すばらしいと思っている] làm rõ động lực gốc rễ."},
            {"grammar_code": "GP-N3-112", "role": "sentence_structure", "note_vi": "Trong bài đọc: くだものを育てていくこと (tiếp tục vun trồng hướng về tương lai bằng Vていく)."},
            {"grammar_code": "GP-N4-13", "role": "sentence_structure", "note_vi": "Câu hỏi giải thích ý định dài hạn [～たいと思っているのは、どうしてか] (GP-N5-11 + GP-N5-08)."},
        ],
        "structure_parse_vi": (
            "Phân biệt 2 lớp nguyên nhân (PID=13): Lớp 1 — Động lực nền đã có sẵn [自然の中で...育てていくことはとても大変だけど、すばらしいと思っている] "
            "(danh từ hóa こと + GP-N3-112 + nhượng bộ けど). Lớp 2 — Tác nhân gia cường sau điện thoại của bố [今までより強く...思った]."
        ),
        "pedagogical_takeaway_vi": "Gặp từ so sánh cấp độ ở cuối đoạn như [今までより強く思った] (nghĩ mạnh mẽ HƠN trước) -> sự kiện vừa xảy ra chỉ là chất xúc tác tăng thêm, nguyên nhân gốc nằm ở quan điểm sẵn có trước đó.",
        "option_grammar_notes": [
            "Option 1: Nhầm tác nhân làm tăng quyết tâm (giọng buồn của bố) thành nguyên nhân khởi nguồn.",
            "Option 2: Lấy lập luận phản bác của người bố về nghề văn phòng (サラリーマン).",
            "Option 3: ĐÚNG. Trích chuẩn xác quan điểm nền tảng 大変だけど、すばらしいと思っている.",
            "Option 4: Chỉ là chi tiết bối cảnh mùa vụ năm nay, không phải lý do định hướng nghề nghiệp.",
        ],
    },
    # ID=142
    "ceb956d400e66c2aa9a80f6f1f0bcae8ea8c88f995008d90361c516dc5547f6c": {
        "links": [
            {"grammar_code": "GP-N3-028", "role": "sentence_structure", "note_vi": "Trích dẫn trực tiếp cảm xúc [『えっ？ 自分より若いお母さん？』と + 驚いて] chỉ thẳng đối tượng gây bất ngờ."},
            {"grammar_code": "GP-N5-04", "role": "sentence_structure", "note_vi": "Cấu trúc so sánh tuổi tác 自分より若い (trẻ hơn bản thân người đàn ông đó)."},
            {"grammar_code": "GP-N4-03", "role": "sentence_structure", "note_vi": "Bẫy Option 3 dùng bị động xưng hô お母さんから + お兄ちゃんと + 呼ばれている (ví dụ bạn kể thêm)."},
        ],
        "structure_parse_vi": (
            "Câu chốt trích dẫn (PID=14): Nội dung độc thoại trong ngoặc [『えっ？ 自分より若いお母さん？』] (so sánh より GP-N5-04) "
            "+ động từ cảm xúc thể て [と驚いて]. Câu hỏi chẻ danh từ hóa [驚いたことは、なにか]."
        ),
        "pedagogical_takeaway_vi": "Gặp câu hỏi [～が驚いたことは何か], tìm ngay cụm trích dẫn ngoặc kép 『...』 hoặc dấu ~と trước chữ 驚いて trong bài.",
        "option_grammar_notes": [
            "Option 1: ĐÚNG. Diễn giải đúng ý nghĩ gây sốc khi người đàn ông gọi người phụ nữ trẻ hơn là 'Mẹ'.",
            "Option 2: Nêu hành động mở đầu trên sân ga, chưa chạm vào nội dung điều gây ngạc nhiên.",
            "Option 3: Dùng sai bị động ví dụ phụ (～と呼ばれている) mà người bạn kể minh họa quy tắc xưng hô gia đình Nhật.",
            "Option 4: Bẫy hiểu sai đối tượng nhân vật (gộp bà mẹ 70 tuổi với người vợ 30 tuổi).",
        ],
    },
    # ID=143
    "172a930f06b287cc2031101e33853812b4b0c0aa5af57f26c3009258c2915bf8": {
        "links": [
            {"grammar_code": "GP-N4-14", "role": "sentence_structure", "note_vi": "Hệ quả logic khách quan trong bài: チャンスをなくすことになる (kết cục dẫn đến mất cơ hội)."},
            {"grammar_code": "GP-N4-01", "role": "sentence_structure", "note_vi": "Thể khả năng phủ định 信ず / 信じる + ことができない (không thể tin tưởng người không chào hỏi)."},
            {"grammar_code": "GP-N5-16", "role": "sentence_structure", "note_vi": "Suy đoán không chắc chắn 変わってしまうかもしれない ở luận điểm gạch chân."},
            {"grammar_code": "GP-N3-051", "role": "sentence_structure", "note_vi": "Trong đáp án đúng dùng dạng nối liên dụng văn viết 信じず (từ 信じない -> 信じず GP-N3-107)."},
        ],
        "structure_parse_vi": (
            "Cấu trúc 2 đoạn (PID=15): Đoạn 1 nêu luận điểm [あなたの一生が変ってしまうかもしれない] (GP-N4-09 + GP-N5-16). "
            "Đoạn 2 giải thích cơ chế nhân quả gồm 2 mắt xích: [信じることができない] (GP-N4-01) -> [チャンスをなくすことになる] (GP-N4-14). "
            "Đáp án đúng tóm tắt bằng dạng văn viết liên dụng [信じず、チャンスを与えないから]."
        ),
        "pedagogical_takeaway_vi": "Trong bài nghị luận giải thích luận điểm gạch chân, hãy ghép đủ cả 2 mắt xích nhân quả ở đoạn ngay sau và cảnh giác với phương án đảo ngược vai (上司 vs 部下).",
        "option_grammar_notes": [
            "Option 1: Trái dữ kiện bài ('năng lực làm việc của hai người ngang nhau').",
            "Option 2: ĐÚNG. Dùng dạng phủ định văn viết 信じず + 与えない phản ánh trọn vẹn lập luận đoạn 2.",
            "Option 3: Đảo ngược đối tượng và gài từ khẳng định tuyệt đối 必ず thành công.",
            "Option 4: Đảo ngược chiều nhân-quả giữa 'chào hỏi' và 'tin tưởng'.",
        ],
    },
    # ID=144
    "7038fe51ee75a40ca411255824bcbb10f66a48c4cd4f66cda9e5143fe0405c66": {
        "links": [
            {"grammar_code": "GP-N5-01", "role": "sentence_structure", "note_vi": "Cụm thời gian Vて + から (結婚してからいちども...いっていない): kể từ sau khi kết hôn chưa từng đi lần nào."},
            {"grammar_code": "GP-N3-044", "role": "sentence_structure", "note_vi": "Phó từ phủ định hoàn toàn いちども～ない tương đương 全然～ていない trong đáp án đúng."},
            {"grammar_code": "GP-N3-041", "role": "sentence_structure", "note_vi": "Ý định dự tính ở hiện tại 奈良へいくつもりだった (định đi Nara)."},
        ],
        "structure_parse_vi": (
            "Đối chiếu mốc thời gian tiểu thuyết (PID=16): Mốc đồng thời [結婚と学校につとめたのが一緒だった] -> khoảng từ mốc đó tới nay "
            "[結婚してからいちどもお寺にいっていない] (GP-N5-01 + GP-N3-044). "
            "Đáp án đúng paraphrase câu này thành [最近、...全然行っていない]."
        ),
        "pedagogical_takeaway_vi": "Cặp diễn đạt tương đương kinh điển trong Đọc hiểu N3: [～てから + いちども + Vていない] = [最近、全然 + Vていない].",
        "option_grammar_notes": [
            "Option 1: Dùng ～前から sai mốc thời gian (bài nói hai sự kiện diễn ra đồng thời 一緒だった).",
            "Option 2: Dùng phép so sánh ～より今のほうが ngược hoàn toàn thực tế (xưa đi nhiều, nay chưa đi).",
            "Option 3: ĐÚNG. Paraphrase chính xác từ いちども～いっていない sang 全然行っていない.",
            "Option 4: Khẳng định sai đã hết hứng thú, trái với chi tiết dự định đi Nara (つもりだった).",
        ],
    },
    # ID=145
    "f8d45e95443146ca898cb0628c30220ab52bc0d7893e1c4f7af7b2cdfdfa2156": {
        "links": [
            {"grammar_code": "GP-N3-118", "role": "sentence_structure", "note_vi": "Kính ngữ thông báo sản phẩm: お買い上げくださり (cảm ơn quý khách đã mua hàng)."},
            {"grammar_code": "GP-N4-16", "role": "sentence_structure", "note_vi": "Điều kiện sự cố trang trọng 故障した場合 (nếu trường hợp bị hỏng) -> tương đương với こわれたとき ở Option 1."},
            {"grammar_code": "GP-N5-14", "role": "sentence_structure", "note_vi": "Liên từ lựa chọn hoặc 電話かEメールで ('bằng điện thoại HOẶC email' — không phải 'VÀ')."},
            {"grammar_code": "GP-N4-01", "role": "sentence_structure", "note_vi": "Động từ khả năng trong đáp án đúng: 聞くことができる (có thể hỏi thăm cách xử lý)."},
        ],
        "structure_parse_vi": (
            "Văn bản thông báo bảo hành (PID=17): Lời cảm ơn kính ngữ [お買い上げくださり] (GP-N3-118) "
            "-> điều kiện [故障した場合] (khi hỏng hóc) -> phương thức liên hệ tách lựa chọn [電話かEメール] (dùng trợ từ か!). "
            "Kết hợp chú thích 注1 định nghĩa 問い合わせ thành câu tương đương [どうしたらいいか聞くことができる]."
        ),
        "pedagogical_takeaway_vi": "Trong thông báo dịch vụ, chú ý trợ từ か (hoặc) vs と (và), chú thích 注1 ở cuối trang và phân biệt hướng dẫn cho người ĐÃ mua vs người MUỐN mua.",
        "option_grammar_notes": [
            "Option 1: ĐÚNG. Giữ đúng liên kết lựa chọn か (hoặc) và nghĩa chú thích của 問い合わせ.",
            "Option 2: Bịa đặt thứ tự thời gian ～したあと (liên hệ mail xong mới gọi điện).",
            "Option 3: Đánh tráo trợ từ lựa chọn か thành と ('cả hai') và bịa thêm ～てくれる (đến tận nhà sửa).",
            "Option 4: Đánh tráo đối tượng sử dụng từ ĐÃ MUA (お買い上げくださり) sang MUỐN MUA (買いたいとき).",
        ],
    },
    # ID=158
    "28466a79d314e54d425fd642e2b8d5affafdd296970e050e6da0514f2b567920": {
        "links": [
            {"grammar_code": "GP-N4-16", "role": "sentence_structure", "note_vi": "Câu hỏi dùng điều kiện giả thiết lịch sự 利用すればいいか (nên sử dụng mục nào thì tốt)."},
            {"grammar_code": "GP-N5-10", "role": "sentence_structure", "note_vi": "Câu khuyến khích nhẹ nhàng trong mục ③: 一人で悩まないで相談に来てください."},
            {"grammar_code": "GP-N3-077", "role": "discourse_marker", "note_vi": "Bảng thông tin (PID=20) dùng cụm mở rộng đối tượng もちろん để nhấn mạnh phạm vi tiếp nhận."},
        ],
        "structure_parse_vi": (
            "Tra cứu thông tin bảng biểu (PID=20): Lọc 2 điều kiện hồ sơ cô Sato: (1) [15歳] khớp mục ③ [対象：0～18さいの子どもの親か関係者]; "
            "(2) [lo lắng nuôi dạy con] khớp mô tả [一人で悩まないで相談に来てください] (Vないで + ください GP-N5-10)."
        ),
        "pedagogical_takeaway_vi": "Với dạng 情報検索 16 điểm dễ lấy nhất nhưng hay mất điểm oan: luôn gạch chân đủ 2 cột [対象 (Đối tượng/Độ tuổi)] + [内容 (Nhu cầu cụ thể)].",
        "option_grammar_notes": [
            "子どもネットワーク: Sai mục đích — dành báo cáo khẩn khi hàng xóm/bản thân trẻ gặp nguy hiểm.",
            "わいわいひろば: Bị loại vì giới hạn độ tuổi 0-3 tuổi (con cô Sato 15 tuổi).",
            "子育て相談: ĐÚNG. Khớp cả dải tuổi 0-18 lẫn nhu cầu tư vấn lo âu phụ huynh.",
            "ボランティア相談: Sai hoàn toàn nhu cầu (đây là tư vấn hoạt động tình nguyện).",
        ],
    },
    # ID=159
    "c08a10c8e92c21f2d6744e789d480701b31164c2a543dfc90a54edbeed299a97": {
        "links": [
            {"grammar_code": "GP-N5-14", "role": "sentence_structure", "note_vi": "Mẫu Vたり～たり (情報を交換したり、子どもと一緒に楽しく遊びましょう) mô tả hoạt động giao lưu của mục ②."},
            {"grammar_code": "GP-N4-16", "role": "sentence_structure", "note_vi": "Câu hỏi lựa chọn điều kiện ～ばいいか cho hồ sơ thứ hai (cô Yamada)."},
        ],
        "structure_parse_vi": (
            "Tra cứu bảng biểu (PID=20): Hồ sơ cô Yamada gồm (1) con 2 tuổi -> khớp [0～3さいの子どもと親]; "
            "(2) muốn kết bạn vui chơi cùng phụ huynh khác -> khớp câu rủ rê [情報を交換したり、...遊びましょう] (GP-N5-14)."
        ),
        "pedagogical_takeaway_vi": "Khi 2 mục cùng thỏa điều kiện độ tuổi (ví dụ 0-3 tuổi đều lọt vào dải 0-18 tuổi), phải đối chiếu sâu hơn vào động từ mục đích ở phần nội dung.",
        "option_grammar_notes": [
            "子どもネットワーク: Mạng lưới bảo vệ/báo cáo khẩn cấp, sai mục đích giao lưu kết bạn.",
            "わいわいひろば: ĐÚNG. Chuyên giao lưu các mẹ có con nhỏ 0-3 tuổi.",
            "子育て相談: Đúng độ tuổi 0-18 nhưng là nơi tư vấn giải quyết nỗi lo, không phải kết bạn vui chơi.",
            "ボランティア相談: Tư vấn tình nguyện, sai nhu cầu.",
        ],
    },
    # ID=160
    "d530bb232853b0a04195a1f75a74597ee20e669570a03ab8fd96cd1fbaba83d1": {
        "links": [
            {"grammar_code": "GP-N5-09", "role": "sentence_structure", "note_vi": "Thể phủ định trải nghiệm 全然勉強したことがありません (chưa từng học bao giờ - Vたことがない) quyết định phân nhóm trình độ B."},
            {"grammar_code": "GP-N4-01", "role": "sentence_structure", "note_vi": "Định ngữ khả năng 参加できるのは (lớp mà anh Tanaka có thể tham gia)."},
        ],
        "structure_parse_vi": (
            "Lọc 3 tầng bảng biểu (PID=21): Tầng 1 Trình độ — [全然勉強したことがありません] (GP-N5-09) -> loại nhóm A [少し話せる], chọn nhóm B [初めての人]; "
            "Tầng 2 Ngôn ngữ -> lớp ③ tiếng Tây Ban Nha; Tầng 3 Lịch nghỉ Thứ 7-CN -> khớp lịch Thứ 7."
        ),
        "pedagogical_takeaway_vi": "Trong đề chọn lớp học, cụm [Vたことがありません] (chưa từng học) luôn loại ngay nhóm A sơ cấp (少し話せる) để chuyển sang nhóm B nhập môn (初めて).",
        "option_grammar_notes": [
            "Aの①のクラス: Sai trình độ (nhóm A yêu cầu đã nói được chút ít).",
            "Aの③のクラス: Sai cả trình độ lẫn ngôn ngữ/lịch học.",
            "Bの①のクラス: Đúng nhóm B nhập môn nhưng sai môn học tiếng Tây Ban Nha (③).",
            "Bの③のクラス: ĐÚNG. Thỏa cả 3 màng lọc: trình độ B, tiếng TBN ③, học Thứ 7.",
        ],
    },
    # ID=161
    "1f3d6fb1c86e00cc282294bf6d4b78b11b0aca8a1b73150ecd5b26cbf622de66": {
        "links": [
            {"grammar_code": "GP-N4-23", "role": "sentence_structure", "note_vi": "Khiêm nhường ngữ tiếp nhận tiền 1回目の日にいただきます quy định thời điểm đóng tiền vào buổi học đầu."},
            {"grammar_code": "GP-N3-039", "role": "sentence_structure", "note_vi": "Khung chú thích điều khoản cuối tờ rơi 注意 / テキスト代は別 cài ngoại lệ giảm 500 yên."},
        ],
        "structure_parse_vi": (
            "Bài toán tính phí có ngoại lệ (PID=21): Bước 1 đọc mục học phí gốc (5,000円) + mục riêng [テキスト代は別] (1,000円); "
            "Bước 2 ĐỌC BẮT BUỘC mục [注意] cuối bảng (lớp B-TBN nghỉ ngày 23/10 giảm còn 4,500円); "
            "Bước 3 chuyển kính ngữ [1回目の日にいただきます] (GP-N4-23) sang [授業の最初の日に]."
        ),
        "pedagogical_takeaway_vi": "Luật vàng làm bài Tìm kiếm thông tin (情報検索): KHÔNG BAO GIỜ cộng tiền trước khi đọc hết phần ※ / 注意 ở tận đáy trang!",
        "option_grammar_notes": [
            "Option 1: Bẫy quên đọc mục 注意 ở cuối tờ rơi nên tính nguyên 5,000 + 1,000 = 6,000 yên.",
            "Option 2: ĐÚNG. Áp dụng ngoại lệ giảm còn 4,500 + 1,000 giáo trình = 5,500 yên đóng ngày học đầu.",
            "Option 3: Sai cả số tiền (quên giảm) lẫn ngày đóng (nhầm ngày nghỉ 23/10).",
            "Option 4: Đúng số tiền 5,500 yên nhưng gài ngày hạn đăng ký qua điện thoại (9/25) làm ngày đóng tiền.",
        ],
    },
    # ID=162
    "a1ddac17bdaaa9fa604fc7e843eb705b84f2a843dfd3098c5cb1aca5510bd465": {
        "links": [
            {"grammar_code": "GP-N3-024", "role": "sentence_structure", "note_vi": "Câu ngoại lệ nhượng bộ mấu chốt: 病院が休みの日でも、電話で受付できます (dù ngày nghỉ khám vẫn nhận đặt hẹn qua ĐT)."},
            {"grammar_code": "GP-N4-16", "role": "sentence_structure", "note_vi": "Câu hỏi điều kiện khuyên hành động ～ばいいか (nên gọi điện vào lúc nào)."},
            {"grammar_code": "GP-N5-04", "role": "sentence_structure", "note_vi": "Cấu trúc khung thời gian hợp lệ từ 9h sáng hôm trước đến 11h sáng ngày khám (～から～まで)."},
        ],
        "structure_parse_vi": (
            "Chuỗi suy luận thời gian (PID=22): Bước 1 loại Thứ 5 vì [休診：木曜日] -> chốt đi khám Sáng Thứ 6; "
            "Bước 2 xác định khung gọi đặt [～から～まで] (GP-N5-04): từ 9h sáng Thứ 5 đến 11h sáng Thứ 6; "
            "Bước 3 kiểm tra câu nhượng bộ [病院が休みの日でも、電話で受付できます] (GP-N3-024) -> sáng Thứ 5 lúc 9h gọi hợp lệ."
        ),
        "pedagogical_takeaway_vi": "Đừng tự suy diễn 'ngày phòng khám nghỉ là tổng đài cũng nghỉ' — luôn tìm câu ngoại lệ có trợ từ ～でも (Ngay cả ngày nghỉ cũng...).",
        "option_grammar_notes": [
            "Option 1: Thứ 4 là 2 ngày trước Thứ 6 — nằm ngoài khung nhận đặt từ 9h sáng hôm trước.",
            "Option 2: ĐÚNG. Thỏa mãn cả khung 9h sáng hôm trước lẫn điều khoản ngoại lệ 休みの日でも受付可.",
            "Option 3: Quá 11h sáng Thứ 6 (khung nhận hẹn sáng Thứ 6 đã đóng lúc 11:00).",
            "Option 4: Bỏ qua toàn bộ khung giờ quy định 9:00 hôm trước ~ 11:00 hôm khám.",
        ],
    },
    # ID=163
    "ef93415e8ba30a25653bc49d978d74a24413b2092b0a94673ca0bc33e715d1a5": {
        "links": [
            {"grammar_code": "GP-N4-23", "role": "sentence_structure", "note_vi": "Kính ngữ bị động tôn kính trong hướng dẫn tổng đài: 受付をされる方 / 午前を希望される方 (Vれる tôn kính)."},
            {"grammar_code": "GP-N5-01", "role": "sentence_structure", "note_vi": "Trình tự hai hành động nối bằng thể て trong cột hướng dẫn: 番号を押して、〈#〉を押してください."},
        ],
        "structure_parse_vi": (
            "Quy trình thao tác tuần tự theo bảng (PID=22): Bước 2 [受付をされる方 -> <1>] (tôn kính ngữ される GP-N4-03/GP-N4-23) "
            "-> Bước 3 [午前を希望される方 -> <3>] -> Bước 4 [番号を押して、〈#〉を押してください] (trình tự V1て, V2 GP-N5-01: bấm mã số xong mới bấm #) "
            "-> Bước 5 [<5>か<6>]."
        ),
        "pedagogical_takeaway_vi": "Trong bảng hướng dẫn tổng đài bằng kính ngữ ～される方, đọc kỹ liên kết tuần tự Vて ở bước 4 (bấm số trước rồi mới bấm #) để không bị đảo phím.",
        "option_grammar_notes": [
            "Option 1: ĐÚNG. Đúng cả 4 bước (<1> đặt mới -> <3> buổi sáng -> <番号> rồi mới <#>).",
            "Option 2: Sai ngay bước đầu (bấm <2> hủy/đổi lịch) và đảo thứ tự phím <#> trước số thẻ.",
            "Option 3: Đúng bước 3-4 nhưng sai bước đầu (<2> thay vì <1>).",
            "Option 4: Sai cả buổi (<4> buổi chiều) lẫn thứ tự phím (<#> trước số thẻ).",
        ],
    },
}


# ==============================================================================
# DYNAMIC GRAMMAR ANALYZER (FOR NEWLY UPLOADED .XLSX WORKBOOKS)
# ==============================================================================

_POINT_BY_CODE: Dict[str, Dict[str, Any]] = {
    pt["code"]: pt for pt in GRAMMAR_POINTS_DATA
}


def _extract_options_list(question_dict: Dict[str, Any]) -> List[str]:
    """Normalize options from either `options` list or `options_json` string."""
    raw = question_dict.get("options")
    if isinstance(raw, list):
        return [str(x) for x in raw]
    raw_json = question_dict.get("options_json")
    if isinstance(raw_json, str) and raw_json.strip():
        try:
            parsed = json.loads(raw_json)
            if isinstance(parsed, list):
                return [str(x) for x in parsed]
        except json.JSONDecodeError:
            pass
    return []


def _match_pattern_score(pattern: str, text: str) -> int:
    """Return pattern character weight if pattern matches text cleanly, else 0."""
    if not pattern or not text:
        return 0
    # Avoid spurious hits from single-character kana particles unless they appear as full tokens
    if len(pattern) <= 1 and all("\u3040" <= ch <= "\u30ff" for ch in pattern):
        return 0
    if any(ch in pattern for ch in (".*", "\\", "[", "(", "+")):
        try:
            if re.search(pattern, text):
                return len(pattern)
        except re.error:
            pass
    if pattern in text:
        return len(pattern)
    return 0


def analyze_question_grammar(
    question_dict: Dict[str, Any],
    passage_dict: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Analyze grammar links & parse for a question dict (optional passage context).

    Checks exact immutable content_hash in QUESTION_GRAMMAR_MAP first; if the
    question comes from a newly uploaded .xlsx workbook, falls back dynamically
    to GRAMMAR_POINTS_DATA match_patterns detection.
    """
    prompt_jp = str(question_dict.get("prompt_jp") or "")
    options = _extract_options_list(question_dict)
    computed_hash = ""
    if prompt_jp and options:
        computed_hash = compute_question_hash(prompt_jp, options)
    provided_hash = str(question_dict.get("content_hash") or "")

    for key_hash in (computed_hash, provided_hash):
        if key_hash and key_hash in QUESTION_GRAMMAR_MAP:
            entry = QUESTION_GRAMMAR_MAP[key_hash]
            return {
                "source": "curated_map",
                "content_hash": key_hash,
                "links": [dict(lnk) for lnk in entry["links"]],
                "structure_parse_vi": entry["structure_parse_vi"],
                "pedagogical_takeaway_vi": entry["pedagogical_takeaway_vi"],
                "option_grammar_notes": list(entry["option_grammar_notes"]),
            }

    # Dynamic match_patterns fallback for future .xlsx imports
    section = str(question_dict.get("section") or "grammar").lower()
    correct_idx = question_dict.get("correct_index")
    p_dict = passage_dict or {}
    passage_body = str(p_dict.get("japanese_text") or p_dict.get("body_jp") or "")
    combined_context = f"{prompt_jp}\n{passage_body}"

    scored_links: List[Dict[str, Any]] = []
    seen_pairs = set()

    for pt in GRAMMAR_POINTS_DATA:
        code = pt["code"]
        patterns = pt.get("match_patterns", [])

        best_correct_score = 0
        best_trap_score = 0
        best_ctx_score = 0

        for idx, opt in enumerate(options):
            for pat in patterns:
                sc = _match_pattern_score(pat, opt)
                if sc > 0:
                    if correct_idx is not None and idx == correct_idx:
                        best_correct_score = max(best_correct_score, sc)
                    else:
                        best_trap_score = max(best_trap_score, sc)

        for pat in patterns:
            best_ctx_score = max(best_ctx_score, _match_pattern_score(pat, combined_context))

        if section == "grammar":
            if best_correct_score > 0 and (code, "primary_target") not in seen_pairs:
                seen_pairs.add((code, "primary_target"))
                scored_links.append({
                    "score": best_correct_score + 100,
                    "grammar_code": code,
                    "role": "primary_target",
                    "note_vi": f"Nhận diện tự động trọng điểm {pt['pattern']}: {pt['core_meaning_vi']}.",
                })
            if best_trap_score > 0 and (code, "distractor_trap") not in seen_pairs:
                seen_pairs.add((code, "distractor_trap"))
                scored_links.append({
                    "score": best_trap_score + 50,
                    "grammar_code": code,
                    "role": "distractor_trap",
                    "note_vi": f"Phương án nhiễu xuất hiện mẫu {pt['pattern']} ({pt['core_meaning_vi']}).",
                })

        if best_ctx_score > 0:
            ctx_role = "discourse_marker" if pt.get("category") == "discourse" else "sentence_structure"
            if (code, ctx_role) not in seen_pairs and (code, "primary_target") not in seen_pairs:
                seen_pairs.add((code, ctx_role))
                scored_links.append({
                    "score": best_ctx_score,
                    "grammar_code": code,
                    "role": ctx_role,
                    "note_vi": f"Cấu trúc ngữ cảnh phát hiện: {pt['pattern']} — {pt['core_meaning_vi']}.",
                })

    scored_links.sort(key=lambda item: item["score"], reverse=True)
    top_links = [
        {
            "grammar_code": item["grammar_code"],
            "role": item["role"],
            "note_vi": item["note_vi"],
        }
        for item in scored_links[:8]
    ]

    if not top_links:
        fallback_code = "GP-N5-02"
        pt_fb = _POINT_BY_CODE[fallback_code]
        top_links = [{
            "grammar_code": fallback_code,
            "role": "sentence_structure",
            "note_vi": f"Khung trợ từ và mệnh đề nền tảng: {pt_fb['pattern']}.",
        }]

    detected_labels = [
        f"{lnk['grammar_code']} ({_POINT_BY_CODE[lnk['grammar_code']]['pattern']})"
        for lnk in top_links[:3]
        if lnk["grammar_code"] in _POINT_BY_CODE
    ]
    structure_parse_vi = (
        f"Phân tích tự động câu đề ({question_dict.get('mondai_type') or section}): "
        f"Các mẫu ngữ pháp phát hiện trong ngữ cảnh gồm {'; '.join(detected_labels)}."
    )
    takeaway_vi = (
        "Đối chiếu trực tiếp cách chia thể (Vる / Vます / Vた / Vて / N) ngay trước chỗ trống và nghĩa mạch văn "
        "với bảng phân biệt cặp dễ nhầm của các mẫu vừa nhận diện."
    )

    option_notes: List[str] = []
    for idx, opt in enumerate(options):
        matched_pt = None
        best_len = 0
        for pt in GRAMMAR_POINTS_DATA:
            for pat in pt.get("match_patterns", []):
                sc = _match_pattern_score(pat, opt)
                if sc > best_len:
                    best_len = sc
                    matched_pt = pt
        if matched_pt is not None:
            tag = "ĐÁP ÁN" if (correct_idx is not None and idx == correct_idx) else "Phương án"
            option_notes.append(f"{tag} ({opt}): Liên quan mẫu {matched_pt['code']} {matched_pt['pattern']} — {matched_pt['core_meaning_vi']}.")
        else:
            option_notes.append(f"Phương án ({opt}): Kiểm tra sự tương hợp trợ từ, tự/tha động từ và ngữ nghĩa trong câu.")

    return {
        "source": "dynamic_match",
        "content_hash": computed_hash or provided_hash,
        "links": top_links,
        "structure_parse_vi": structure_parse_vi,
        "pedagogical_takeaway_vi": takeaway_vi,
        "option_grammar_notes": option_notes,
    }
