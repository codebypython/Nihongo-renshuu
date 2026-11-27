"""Anti-rote variant drill generator covering 100% of imported questions + condition shifts."""

import json
import re
import sqlite3
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from n3_mastery.database import get_connection, transaction


# Curated condition-shift variants for MU-12 (情報検索) so learners cannot memorize answers
CURATED_CONDITION_SHIFTS: Dict[str, List[Dict[str, Any]]] = {
    "佐藤（さとう）さんは、どこを利用すればいいか。": [
        {
            "prompt_jp": (
                "【Đảo điều kiện 情報検索】Giả sử con của cô 佐藤さん chỉ mới 2 tuổi và cô muốn cùng con chơi, "
                "đồng thời kết bạn trao đổi thông tin với các bà mẹ khác (từ thứ 2 đến thứ 7, 10:00–16:00). "
                "Lúc này cô 佐藤さん nên sử dụng mục nào?"
            ),
            "options": ["子どもネットワーク", "わいわいひろば", "子育て相談", "ボランティア相談"],
            "correct_index": 1,
            "evidence_hint": "対象：0～3さいの子どもと親 / 月曜日～土曜日 午前10時から午後4時",
            "explanation_vi": (
                "Đảo điều kiện tuổi con (15 -> 2 tuổi) và nhu cầu giao lưu: khớp mục ② わいわいひろば "
                "(dành riêng cho trẻ 0–3 tuổi và phụ huynh)."
            ),
        },
        {
            "prompt_jp": (
                "【Đảo điều kiện 情報検索】Giả sử một người hàng xóm nhìn thấy đứa trẻ cạnh nhà có dấu hiệu bị ngược đãi lúc 11 giờ đêm "
                "(không phải người trong gia đình đứa trẻ). Theo tờ rơi 「子どもセンター案内」, người hàng xóm phải liên hệ mục nào?"
            ),
            "options": ["子どもネットワーク", "わいわいひろば", "子育て相談", "ボランティア相談"],
            "correct_index": 0,
            "evidence_hint": "まわりの子どもが「ちょっと気になる」「心配だ」というとき…家族でなくても子どもたちを守りましょう。24時間電話で受け付けています。",
            "explanation_vi": (
                "Người ngoài gia đình ('家族でなくても') gọi khẩn cấp ban đêm (24/24) thuộc mục ① 子どもネットワーク."
            ),
        },
    ],
    "山田（やまだ）さんは、どこを利用すればいいか。": [
        {
            "prompt_jp": (
                "【Đảo điều kiện 情報検索】Giả sử con cô 山田さん đã lên 5 tuổi (vượt ngưỡng 0–3 tuổi) và cô muốn đến "
                "nhờ chuyên viên tư vấn nỗi lo nuôi dạy con vào Thứ 4 lúc 14:00. Cô 山田さん phải chọn mục nào?"
            ),
            "options": ["子どもネットワーク", "わいわいひろば", "子育て相談", "ボランティア相談"],
            "correct_index": 2,
            "evidence_hint": "子育ての心配や悩み…対象：0～18さいの子どもの親か関係者（月～金 9:00～17:00）",
            "explanation_vi": (
                "Trẻ 5 tuổi không còn thuộc わいわいひろば (0–3 tuổi) -> chuyển sang mục ③ 子育て相談 (0–18 tuổi, T2–T6)."
            ),
        }
    ],
    "田中（たなか）さんが参加できるのは、どのクラスか。": [
        {
            "prompt_jp": (
                "【Đảo điều kiện 情報検索】Giả sử anh 田中さん ĐÃ nói được tiếng Tây Ban Nha một chút (少し話せる) "
                "và vẫn chỉ nghỉ Thứ 7, Chủ nhật. Anh 田中さん phải đăng ký lớp nào?"
            ),
            "options": ["Aの①のクラス", "Aの③のクラス", "Bの①のクラス", "Bの③のクラス"],
            "correct_index": 0,
            "evidence_hint": "A 少し話せる人の初級クラス：① スペイン語 日 10:00～12:00",
            "explanation_vi": (
                "Khi đổi trình độ từ 'chưa từng học' sang '少し話せる', anh Tanaka chuyển sang nhóm A, "
                "lớp ① tiếng TBN học Chủ nhật 10:00–12:00 (khớp ngày nghỉ cuối tuần)."
            ),
        }
    ],
    "田中（たなか）さんはいつ、いくら払う（はらう）か。": [
        {
            "prompt_jp": (
                "【Đảo điều kiện 情報検索】Giả sử anh 田中さん đăng ký lớp B-② Tiếng Thái (タイ語, không có ghi chú giảm học phí ở mục 注意) "
                "và cần mua cả giáo trình. Ngày học đầu tiên anh phải nộp tổng cộng bao nhiêu tiền?"
            ),
            "options": ["授業の最初の日に 5,500円", "授業の最初の日に 5,700円", "授業の最初の日に 6,000円", "9月25日に 5,700円"],
            "correct_index": 1,
            "evidence_hint": "受講料：5,000円（1回目の日にいただきます）/ テキスト代は別：タイ語 700円",
            "explanation_vi": (
                "Lớp Tiếng Thái B-② không được giảm học phí (vẫn 5,000円) + giáo trình Tiếng Thái 700円 = 5,700円, "
                "nộp vào ngày học đầu tiên ('1回目の日にいただきます')."
            ),
        }
    ],
    "リーさんは、いつ予約の電話をかければいいか。": [
        {
            "prompt_jp": (
                "【Đảo điều kiện 情報検索】Giả sử ngày nghỉ của bạn リーさん đổi thành Thứ 4 (水曜日) và Thứ 5 (木曜日), "
                "và bạn ấy vẫn muốn khám BUỔI SÁNG (午前中). Biết bệnh viện nghỉ khám Thứ 5 (休診：木曜日). "
                "Bạn リーさん có thể gọi đặt lịch khám sớm nhất từ thời điểm nào?"
            ),
            "options": ["火曜日の午前9時", "水曜日の午前9時", "木曜日の午前9時", "火曜日の午後3時"],
            "correct_index": 0,
            "evidence_hint": "休診：木曜日 / 予約受付時間は前日の午前9時から / 午前の受付は午前11時まで",
            "explanation_vi": (
                "Vì bệnh viện nghỉ Thứ 5 nên Lee phải khám sáng Thứ 4. Lịch đặt cho sáng Thứ 4 mở từ 9:00 sáng hôm trước, "
                "tức là 火曜日の午前9時 (9 giờ sáng Thứ 3)!"
            ),
        }
    ],
    "リーさんが予約の電話をするとき、どの順番（じゅんばん）になるか。": [
        {
            "prompt_jp": (
                "【Đảo điều kiện 情報検索】Giả sử bạn リーさん đổi sang đặt lịch khám mới vào BUỔI CHIỀU (午後を希望). "
                "Thứ tự bấm phím chính xác là dãy nào?"
            ),
            "options": [
                "<1>→<4>→<診察券番号>→<#>→<5>か<6>",
                "<1>→<3>→<診察券番号>→<#>→<5>か<6>",
                "<2>→<4>→<診察券番号>→<#>→<5>か<6>",
                "<1>→<4>→<#>→<診察券番号>→<5>か<6>",
            ],
            "correct_index": 0,
            "evidence_hint": "受付をされる方は〈1〉 / 午後の方は〈4〉 / 番号を押して〈#〉を押してください",
            "explanation_vi": (
                "Đặt lịch mới bấm 〈1〉 -> Buổi chiều bấm 〈4〉 -> Nhập mã thẻ 〈診察券番号〉 rồi mới bấm 〈#〉 -> Xác nhận 〈5〉か〈6〉."
            ),
        }
    ],
}


# Curated replacement answers for 問題5 (Cách dùng từ) wrong-sentence diagnosis
# Format: focus_keyword -> (wrong_option_index_0based, clean_replacement_no_furigana, pos_matched_distractors, explanation)
CURATED_USAGE_REPLACEMENTS: Dict[str, Tuple[int, str, List[str], str]] = {
    "ぐっすり": (
        3,
        "たっぷり",
        ["ぐっすり", "しっかり", "ぴったり"],
        "Trò chuyện say sưa/thoải mái dùng たっぷり hoặc ゆっくり; ぐっすり chỉ đi với ngủ (眠る).",
    ),
    "それぞれ": (
        2,
        "そろそろ",
        ["それぞれ", "だんだん", "いよいよ"],
        "Bẫy âm gần giống: 会議を【そろそろ】始めましょう (sắp sửa bắt đầu), không dùng それぞれ.",
    ),
    "寄る": (
        2,
        "偏った",
        ["寄った", "揃った", "決まった"],
        "Ăn uống thiên lệch/kén ăn dùng 偏った（かたよった）食事, bẫy đồng âm gần với 寄った.",
    ),
    "ぴったり": (
        1,
        "ばったり",
        ["ぴったり", "ぐっすり", "しっかり"],
        "Tình cờ chạm mặt bạn cũ dùng 【ばったり】会った, không dùng ぴったり.",
    ),
    "くり返す": (
        1,
        "振り返った",
        ["くり返した", "見送った", "思い出した"],
        "Quay đầu nhìn lại khi nghe gọi tên dùng 【振り返る（ふりかえる）】, không dùng 繰り返す.",
    ),
    "生える": (
        2,
        "建った",
        ["生えた", "育った", "増えた"],
        "Ngôi nhà được xây lên dùng 【建つ（たつ）】; 生える chỉ dùng cho cây cỏ, tóc, râu, răng.",
    ),
    "トレーニング": (
        0,
        "貿易",
        ["トレーニング", "輸入", "観光"],
        "Giao thương buôn bán với nước khác dùng 貿易（ぼうえき） hoặc トレーディング, không dùng トレーニング.",
    ),
    "努力": (
        0,
        "能力",
        ["努力", "経験", "知識"],
        "Có năng lực/tài năng tuyệt vời dùng 【能力（のうりょく）】がある, không dùng 努力がある.",
    ),
    "なつかしい": (
        3,
        "恥ずかしい",
        ["なつかしい", "うらやましい", "めずらしい"],
        "Xấu hổ khi thất bại trước đám đông dùng 【恥ずかしい（はずかしい）】, bẫy âm gần với なつかしい.",
    ),
    "気に入る": (
        0,
        "気になって",
        ["気に入って", "気がついて", "気がして"],
        "Lo lắng, bận tâm về bài kiểm tra ngày mai dùng 【気になる（きになる）】, không dùng 気に入る (ưng ý).",
    ),
    "まぜる": (
        0,
        "生けよう",
        ["まぜよう", "育てよう", "並べよう"],
        "Cắm hoa vào bình dùng 【生ける（いける）】 hoặc 飾る, không dùng 混ぜる.",
    ),
    "現実": (
        1,
        "実感",
        ["現実", "意識", "印象"],
        "Cụm cố định: 'chưa có cảm giác thực sự là đã đỗ' dùng 【実感（じっかん）】がわかない.",
    ),
    "おかず": (
        0,
        "おやつ",
        ["おかず", "食事", "弁当"],
        "Bữa ăn nhẹ buổi chiều giữa trưa và tối dùng 【おやつ】, không dùng おかず.",
    ),
    "できあがる": (
        0,
        "なる",
        ["できあがる", "つとめる", "通う"],
        "Trở thành giáo viên dùng 先生に【なる】; 出来上がる dùng cho món ăn/tác phẩm hoàn tất.",
    ),
}


def _strip_inline_furigana(text: str) -> str:
    return re.sub(r"（[^）]{1,12}）", "", str(text or "")).strip()


def _clean_unbalanced_parens(text: str) -> str:
    s = str(text or "").strip()
    while s.endswith(")") and s.count("(") < s.count(")"):
        s = s[:-1].strip()
    while s.endswith("）") and s.count("（") < s.count("）"):
        s = s[:-1].strip()
    while s.startswith("(") and s.count(")") < s.count("("):
        s = s[1:].strip()
    return s.strip(" .")


def _mask_answer_leaks_for_reading(text: str, options: List[str]) -> str:
    """Remove any hiragana/option text matching the 4 choices (including 1-char Japanese particles) from a prompt."""
    out = str(text or "")
    tokens: List[str] = []
    short_tokens: List[str] = []
    for opt in options:
        clean_o = _strip_inline_furigana(opt)
        for tok in (opt, clean_o):
            if not tok:
                continue
            if len(tok) >= 2 and tok not in tokens:
                tokens.append(tok)
            elif len(tok) == 1 and tok not in short_tokens:
                short_tokens.append(tok)
    for tok in sorted(tokens, key=len, reverse=True):
        out = out.replace(tok, "___")
    # Mask 1-char Japanese particle options when immediately attached to Japanese text (e.g., 一度も -> 一度___)
    for st in short_tokens:
        out = re.sub(rf"(?<=[\u4e00-\u9faf\u3040-\u309f\u30a0-\u30ff]){re.escape(st)}", "___", out)
    return out


def _clean_kanji_leak_in_meaning(text: str, options: List[str]) -> str:
    """Remove parentheticals or phrases that leak Kanji chars from the 4 choices without producing broken fragments."""
    kanji_chars = set("".join(re.findall(r"[\u4e00-\u9faf]", " ".join(options))))
    if not kanji_chars:
        return text

    def _clean_paren(m: re.Match) -> str:
        inner = m.group(1)
        if any(ch in kanji_chars for ch in inner):
            vi_only = re.sub(r"[\u4e00-\u9faf\u3040-\u30ff・]+", "", inner).strip(" :-–・,")
            if vi_only and len(vi_only) >= 5:
                return f"({vi_only})"
            return ""
        return m.group(0)

    out = re.sub(r"\(([^)]+)\)", _clean_paren, str(text or ""))
    out = re.sub(r"（([^）]+)）", _clean_paren, out)

    def _repl_jp(m: re.Match) -> str:
        tok = m.group(0)
        if any(ch in kanji_chars for ch in tok):
            return "＿＿"
        return tok

    out = re.sub(r"[\u4e00-\u9faf\u3040-\u309f・]+", _repl_jp, out)
    out = re.sub(r"\s{2,}", " ", out).strip(" ,.-")
    return _clean_unbalanced_parens(out)


def _split_top_level_colon(body: str) -> Tuple[str, str]:
    """Split on the first ':' or '：' outside parentheses so '(無視: phớt lờ)' stays intact."""
    depth = 0
    for idx, ch in enumerate(body):
        if ch in "(（":
            depth += 1
        elif ch in ")）":
            depth = max(0, depth - 1)
        elif ch in ":：" and depth == 0:
            return body[:idx].strip(), body[idx + 1 :].strip()
    return body.strip(), body.strip()


def _split_bullet_segments(explanation_vi: str) -> List[Tuple[int, str]]:
    """Split explanation_vi distractor lines, including inline '; 2. ...' or ', 3. ...' items."""
    items: List[Tuple[int, str]] = []
    if not explanation_vi:
        return items

    for raw_line in explanation_vi.splitlines():
        clean_line = raw_line.strip()
        m = re.match(r"^[-•]\s*(\d+)(?:\s*\(\d+\))?\.\s*(.+)$", clean_line)
        if not m:
            continue
        # Split inline chained items like "1. あったら: nếu có; 2. 決まったら: nếu quyết định; 4. 始まったら: ..."
        sub_parts = re.split(r"[;,]\s*(?=\d+(?:\s*\(\d+\))?\.\s*)", m.group(2).strip())
        first_idx = int(m.group(1)) - 1
        items.append((first_idx, sub_parts[0].strip()))
        for sp in sub_parts[1:]:
            m_sub = re.match(r"^(\d+)(?:\s*\(\d+\))?\.\s*(.+)$", sp.strip())
            if m_sub:
                items.append((int(m_sub.group(1)) - 1, m_sub.group(2).strip()))
    return items


def _extract_distractor_bullets(explanation_vi: str, options: List[str], correct_index: int) -> List[Dict[str, Any]]:
    """Parse distractor explanations cleanly into structured facts per distractor option."""
    results: List[Dict[str, Any]] = []
    seen_indices: set[int] = set()

    for opt_idx, body in _split_bullet_segments(explanation_vi):
        if not (0 <= opt_idx < len(options)) or opt_idx == correct_index or opt_idx in seen_indices:
            continue
        opt_val = options[opt_idx]
        lower_body = body.lower()
        # Skip non-word / purely invalid fabricated distractors or merged multi-item summary comments
        if any(
            bad in lower_body
            for bad in (
                "cách đọc sai",
                "sai mặt chữ",
                "không tồn tại",
                "bị đảo ngược",
                "không chia được",
                "không ghép thành",
                "đều không mang nghĩa",
            )
        ):
            continue
        if re.search(r"&\s*\d+\.", body):
            continue

        # Split head (before top-level ':') and meaning (after top-level ':')
        head, meaning_raw = _split_top_level_colon(body)
        if ":" in meaning_raw and not re.search(r"[a-zA-ZÀ-ỹ]", head):
            # e.g. 'むし (無視: phớt lờ / 虫: côn trùng)' with no top-level colon
            m_first_jp = re.search(r"[:：]\s*(.+)$", body)
            if m_first_jp:
                meaning_raw = m_first_jp.group(1)

        head = head.strip()
        meaning_vi = _clean_unbalanced_parens(meaning_raw)
        if not meaning_vi or len(meaning_vi) < 3:
            continue

        paren = ""
        m_paren = re.search(r"\(([^)]+)\)", head)
        if m_paren:
            paren = m_paren.group(1).strip()

        # Extract Kanji target from head or paren for 問題1
        head_no_paren = re.sub(r"\([^)]+\)", "", head).strip()
        kanji_candidates = re.findall(r"[\u4e00-\u9faf々〆ヶ]+(?:[\u3040-\u309f]+)?", f"{paren} {head_no_paren}")
        # Filter out option text itself if reading
        kanji_label = ""
        for kc in kanji_candidates:
            if re.search(r"[\u4e00-\u9faf]", kc) and kc != opt_val:
                kanji_label = kc
                break

        is_error_note = any(
            err_kw in meaning_vi.lower()
            for err_kw in (
                "(sai",
                "sai quy tắc",
                "sai cấu trúc",
                "sai trợ từ",
                "sai chủ thể",
                "sai về",
                "mâu thuẫn",
                "thiếu sắc thái",
                "không hợp",
                "không dùng cho",
                "không đi với",
                "không gắn",
            )
        )

        seen_indices.add(opt_idx)
        results.append(
            {
                "opt_index": opt_idx,
                "option_text": opt_val,
                "detail": _clean_unbalanced_parens(body),
                "paren": paren,
                "kanji_label": kanji_label,
                "meaning_vi": meaning_vi,
                "is_error_note": is_error_note,
            }
        )
    return results


def _build_star_shift_variants(q: sqlite3.Row) -> List[Dict[str, Any]]:
    meta = json.loads(q["notebook_meta_json"] or "{}")
    sa = meta.get("star_assembly")
    options = json.loads(q["options_json"])
    if not sa or len(sa.get("slots_order", [])) != 4:
        return []

    slots_order: List[int] = sa["slots_order"]
    orig_star_slot: int = int(sa.get("star_slot_index", 2))
    prefix: str = sa.get("prefix", "")
    suffix: str = sa.get("suffix", "")
    full_sentence: str = sa.get("full_sentence", "")

    # Shift ★ to different slot positions (e.g. slot index 1 and 3, avoiding orig_star_slot)
    candidate_slots = [s for s in (1, 3, 0, 2) if s != orig_star_slot][:2]
    variants: List[Dict[str, Any]] = []
    for new_star_slot in candidate_slots:
        slot_tokens = ["★" if i == new_star_slot else "＿＿＿" for i in range(4)]
        prompt_jp = f"【Biến thể Dời dấu ★ sang Ô {new_star_slot + 1}】{prefix} {' '.join(slot_tokens)} {suffix}".strip()
        new_correct_idx = int(slots_order[new_star_slot])
        v_meta = {
            "slots_order": slots_order,
            "star_slot_index": new_star_slot,
            "chunks": options,
            "prefix": prefix,
            "suffix": suffix,
            "full_sentence": full_sentence,
            "original_star_slot": orig_star_slot,
        }
        variants.append(
            {
                "variant_mode": "star_4slot_shift",
                "prompt_jp": prompt_jp,
                "options": options,
                "correct_index": new_correct_idx,
                "metadata": v_meta,
                "explanation_vi": (
                    f"Biến thể dời dấu ★ từ ô {orig_star_slot + 1} sang ô {new_star_slot + 1}: "
                    f"đáp án tại ô ★ mới là '{options[new_correct_idx]}'. "
                    f"Câu hoàn chỉnh: {full_sentence}."
                ),
            }
        )
    return variants


def _build_usage_error_diagnosis_variant(q: sqlite3.Row) -> List[Dict[str, Any]]:
    options = json.loads(q["options_json"])
    correct_idx = int(q["correct_index"])
    kw = str(q["focus_keyword"] or "").strip()
    explanation_vi = str(q["explanation_vi"] or "")

    # Try curated mapping first, then rule-based extraction from explanation_vi
    wrong_idx: Optional[int] = None
    replacement_word = ""
    pos_distractors: List[str] = []
    extra_note = ""

    if kw in CURATED_USAGE_REPLACEMENTS:
        wrong_idx, replacement_word, pos_distractors, extra_note = CURATED_USAGE_REPLACEMENTS[kw]
    else:
        # Rule-based extraction for newly uploaded 問題5 workbooks
        m_sai = re.search(r"Câu\s*(\d)\s*\(SAI[^)]*\):[^\n]*?(?:phải dùng|dùng)\s+([^\s(（.。\n]+)", explanation_vi)
        if m_sai:
            cand_idx = int(m_sai.group(1)) - 1
            if 0 <= cand_idx < 4 and cand_idx != correct_idx:
                wrong_idx = cand_idx
                replacement_word = _strip_inline_furigana(m_sai.group(2).split("/")[0].strip())
                extra_note = m_sai.group(0).strip()

    if wrong_idx is not None and replacement_word:
        wrong_sentence = options[wrong_idx]
        clean_rep = _strip_inline_furigana(replacement_word.split("/")[0].strip())
        choices = [clean_rep]
        for cand in pos_distractors + [kw, "しっかり", "ぴったり", "気になる"]:
            clean_c = _strip_inline_furigana(cand)
            if len(choices) >= 4:
                break
            if clean_c and clean_c != clean_rep and clean_c not in choices:
                choices.append(clean_c)
        return [
            {
                "variant_mode": "error_diagnosis",
                "prompt_jp": (
                    f"【Đảo nhiễu 問題5 — Chẩn đoán lỗi sai】Câu sau dùng từ trong 【...】 SAI ngữ cảnh:\n"
                    f"「{wrong_sentence}」\nTừ đúng để thay thế cho vị trí trong ngoặc là từ nào?"
                ),
                "options": choices,
                "correct_index": 0,
                "metadata": {
                    "target_keyword": kw,
                    "wrong_sentence": wrong_sentence,
                    "replacement_word": clean_rep,
                },
                "explanation_vi": f"{extra_note}\n(Trong câu gốc, từ 【{kw}】 chỉ đúng ở câu: {options[correct_idx]}).",
            }
        ]

    return [
        {
            "variant_mode": "error_diagnosis",
            "prompt_jp": (
                f"【Chẩn đoán 問題5】Xét cách dùng từ 【{kw}】 trong 4 câu dưới đây (đã xáo thứ tự). "
                f"Chọn câu DUY NHẤT kết hợp đúng cả chủ ngữ lẫn tân ngữ với 【{kw}】:"
            ),
            "options": options,
            "correct_index": correct_idx,
            "metadata": {"target_keyword": kw, "mode_fallback": True},
            "explanation_vi": explanation_vi,
        }
    ]


def _build_reading_variants(q: sqlite3.Row) -> List[Dict[str, Any]]:
    options = json.loads(q["options_json"])
    correct_idx = int(q["correct_index"])
    meta = json.loads(q["notebook_meta_json"] or "{}")
    ev_indices = meta.get("evidence_indices") or []
    prompt_jp = str(q["prompt_jp"])
    explanation_vi = str(q["explanation_vi"] or "")

    variants: List[Dict[str, Any]] = []
    if q["passage_id"] is not None and ev_indices:
        variants.append(
            {
                "variant_mode": "dokkai_evidence",
                "prompt_jp": f"【Evidence-First Dokkai】Chọn đúng câu chốt / dòng điều kiện trong bài trước khi trả lời:\n{prompt_jp}",
                "options": options,
                "correct_index": correct_idx,
                "metadata": {
                    "evidence_indices": ev_indices,
                    "require_evidence": True,
                    "dokkai_skill": meta.get("dokkai_skill", ""),
                    "condition_matrix": meta.get("condition_matrix"),
                    "trap_decoder": meta.get("trap_decoder"),
                },
                "explanation_vi": explanation_vi,
            }
        )

    # Add Condition-Shift variants for MU-12 (情報検索)
    if prompt_jp in CURATED_CONDITION_SHIFTS:
        for shift in CURATED_CONDITION_SHIFTS[prompt_jp]:
            variants.append(
                {
                    "variant_mode": "condition_shift",
                    "prompt_jp": shift["prompt_jp"],
                    "options": shift["options"],
                    "correct_index": shift["correct_index"],
                    "metadata": {
                        "evidence_indices": ev_indices,
                        "require_evidence": False,
                        "evidence_hint": shift["evidence_hint"],
                        "is_condition_shift": True,
                    },
                    "explanation_vi": shift["explanation_vi"],
                }
            )
    if not variants:
        return _build_distractor_invert_variants(q)
    return variants


def _build_distractor_invert_variants(q: sqlite3.Row) -> List[Dict[str, Any]]:
    options = json.loads(q["options_json"])
    correct_idx = int(q["correct_index"])
    section = q["section"]
    mondai = q["mondai_type"]
    kw = str(q["focus_keyword"] or "")
    prompt_jp = str(q["prompt_jp"] or "")
    explanation_vi = str(q["explanation_vi"] or "")
    meta = json.loads(q["notebook_meta_json"] or "{}")

    facts = _extract_distractor_bullets(explanation_vi, options, correct_idx)
    variants: List[Dict[str, Any]] = []

    if section == "vocab" and mondai == "問題1":
        for fact in facts:
            if len(variants) >= 2:
                break
            d_opt = fact["option_text"]
            meaning = _mask_answer_leaks_for_reading(fact["meaning_vi"], options)
            kanji_label = fact.get("kanji_label", "")
            # Skip ambiguous cross-reference notes when label is missing or meaning leaks another Kanji clue like "Chữ 券..."
            if "___" in meaning and not kanji_label:
                continue
            if kanji_label and f"Chữ {kanji_label}" not in meaning and "Chữ " in meaning and "___" in meaning:
                continue
            if len(meaning) < 5 and not kanji_label:
                continue
            if kanji_label:
                q_text = f"【Đảo nhiễu 問題1】Từ 【{kanji_label}】 (nghĩa: {meaning}) có cách đọc đúng là phương án nào?"
            else:
                q_text = f"【Đảo nhiễu 問題1】Trong các cách đọc dưới đây, phương án nào ứng với nghĩa 「{meaning}」?"
            variants.append(
                {
                    "variant_mode": "distractor_invert",
                    "prompt_jp": q_text,
                    "options": options,
                    "correct_index": fact["opt_index"],
                    "metadata": {
                        "inverted_from_correct": options[correct_idx],
                        "target_distractor": d_opt,
                        "target_kanji": kanji_label,
                    },
                    "explanation_vi": f"Đảo chiều từ bẫy của câu gốc 【{kw}】: {fact['detail']}",
                }
            )
        if not variants:
            so_tay = meta.get("so_tay", {})
            meaning = so_tay.get("meaning_vi") or str(q["translation_vi"] or "")
            meaning = _mask_answer_leaks_for_reading(meaning, options).strip(" .-")
            kw_parts = [p.strip() for p in re.split(r"→|->", kw) if p.strip()]
            kanji_part = next((p for p in kw_parts if re.search(r"[\u4e00-\u9faf]", p)), kw_parts[0] if kw_parts else "")
            if not kanji_part:
                m_target = re.search(r"【([^】]+)】", prompt_jp)
                kanji_part = m_target.group(1).strip() if m_target else ""
            kanji_part = _mask_answer_leaks_for_reading(kanji_part, options).strip(" .-")
            meaning_clause = f" (nghĩa: {meaning})" if meaning and meaning != kanji_part and meaning != "___" else ""
            if kanji_part and kanji_part != "___":
                fallback_prompt = f"【Đảo nhiễu 問題1】Từ 【{kanji_part}】{meaning_clause} đọc đúng là phương án nào?"
            else:
                fallback_prompt = f"【Đảo nhiễu 問題1】Chọn cách đọc đúng cho từ trong 【...】:\n{prompt_jp}{meaning_clause}"
            variants.append(
                {
                    "variant_mode": "distractor_invert",
                    "prompt_jp": fallback_prompt,
                    "options": options,
                    "correct_index": correct_idx,
                    "metadata": {"reverse_meaning": True, "target_kanji": kanji_part},
                    "explanation_vi": explanation_vi,
                }
            )
        return variants

    if section == "vocab" and mondai == "問題2":
        for fact in facts:
            if len(variants) >= 2:
                break
            d_opt = fact["option_text"]
            # Only invert REAL Japanese words/compounds (skip fake fabricated forms like 通え/買す/夫う/準えて/物言)
            if not re.search(rf"(?<![\u4e00-\u9faf\u3040-\u309f]){re.escape(d_opt)}(?![\u4e00-\u9faf\u3040-\u309f])", fact["detail"]) or fact.get("is_error_note"):
                continue
            meaning = _clean_kanji_leak_in_meaning(fact["meaning_vi"], options)
            if len(meaning) < 8:
                continue
            variants.append(
                {
                    "variant_mode": "distractor_invert",
                    "prompt_jp": (
                        f"【Đảo nhiễu 問題2 — Tự dạng & Đồng âm】Chọn chữ Kanji viết ĐÚNG cho ngữ nghĩa / cách kết hợp sau:\n"
                        f"「{meaning}」"
                    ),
                    "options": options,
                    "correct_index": fact["opt_index"],
                    "metadata": {"inverted_from_correct": options[correct_idx], "target_distractor": d_opt},
                    "explanation_vi": f"Phân biệt với đáp án gốc ({options[correct_idx]}): {fact['detail']}",
                }
            )
        if not variants:
            # Extract ONLY hiragana reading (never include the Kanji!)
            m_hira = re.search(r"【([^】]+)】", prompt_jp)
            hira_cue = m_hira.group(1).strip() if m_hira else ""
            if not hira_cue or re.search(r"[\u4e00-\u9faf]", hira_cue):
                kw_parts = [p.strip() for p in re.split(r"→|->", kw) if p.strip()]
                hira_cue = next((p for p in kw_parts if not re.search(r"[\u4e00-\u9faf]", p)), hira_cue)
            hira_cue = _clean_kanji_leak_in_meaning(hira_cue, options).strip(" .-")
            trans_clean = _clean_kanji_leak_in_meaning(str(q["translation_vi"] or ""), options).strip(" .-")
            if trans_clean:
                prompt_m2 = (
                    f"【Đảo nhiễu 問題2 — Khớp Kanji theo nghĩa】Chọn chữ Kanji chuẩn cho từ 【{hira_cue or '...'}】 "
                    f"trong nghĩa câu: 「{trans_clean}」"
                )
            else:
                prompt_m2 = (
                    f"【Đảo nhiễu 問題2 — Khớp Kanji】Chọn chữ Kanji chuẩn cho phần 【{hira_cue or '...'}】 trong câu:\n"
                    f"{_clean_kanji_leak_in_meaning(prompt_jp, options)}"
                )
            variants.append(
                {
                    "variant_mode": "distractor_invert",
                    "prompt_jp": prompt_m2,
                    "options": options,
                    "correct_index": correct_idx,
                    "metadata": {"reverse_meaning": True},
                    "explanation_vi": explanation_vi,
                }
            )
        return variants

    if section == "vocab" and mondai == "問題4":
        antonym_fact = next(
            (f for f in facts if "TRÁI NGHĨA" in f["detail"].upper() or "trái nghĩa" in f["detail"].lower()),
            None,
        )
        if antonym_fact:
            variants.append(
                {
                    "variant_mode": "distractor_invert",
                    "prompt_jp": f"【Đảo nhiễu 問題4 — Phản xạ Trái nghĩa】Trong 4 lựa chọn sau, từ nào TRÁI NGHĨA với từ trong ngoặc: {prompt_jp}",
                    "options": options,
                    "correct_index": antonym_fact["opt_index"],
                    "metadata": {"antonym_probe": True},
                    "explanation_vi": (
                        f"Đáp án trái nghĩa là '{antonym_fact['option_text']}' ({antonym_fact['detail']}). "
                        f"Đáp án ĐỒNG NGHĨA ở câu gốc là '{options[correct_idx]}'."
                    ),
                }
            )
        # Pick a DIFFERENT distractor (not the antonym_fact) for meaning-reversal probe
        for f_other in facts:
            if antonym_fact and f_other["opt_index"] == antonym_fact["opt_index"]:
                continue
            clean_m = _mask_answer_leaks_for_reading(f_other["meaning_vi"], options)
            clean_m = re.sub(r"\s*\(từ trái nghĩa\)|là từ TRÁI NGHĨA[^.]*", "", clean_m, flags=re.IGNORECASE).strip(" .)")
            if len(clean_m) < 5 or "___" in clean_m:
                continue
            variants.append(
                {
                    "variant_mode": "distractor_invert",
                    "prompt_jp": f"【Đảo nhiễu 問題4】Trong 4 phương án dưới đây, từ/cụm nào mang nghĩa 「{clean_m}」?",
                    "options": options,
                    "correct_index": f_other["opt_index"],
                    "metadata": {"distractor_probe": True},
                    "explanation_vi": f"Đáp án bẫy trong câu gốc ({kw}): {f_other['detail']}.",
                }
            )
            break
        if not variants:
            trans_vi = _mask_answer_leaks_for_reading(str(q["translation_vi"] or ""), options).strip(" .-")
            trans_line = f"\n(Nghĩa câu: {trans_vi})" if trans_vi and trans_vi != "___" else ""
            variants.append(
                {
                    "variant_mode": "distractor_invert",
                    "prompt_jp": (
                        f"【Đảo chiều Đồng nghĩa】Từ nào có thể thay thế tương đương cho từ trong ngoặc của câu sau:\n"
                        f"{prompt_jp}{trans_line}"
                    ),
                    "options": options,
                    "correct_index": correct_idx,
                    "metadata": {"reverse_paraphrase": True},
                    "explanation_vi": explanation_vi,
                }
            )
        return variants

    # 問題3 Vocab, 問題1 Grammar, 問題3 Grammar Cloze
    # Prefer positive meaning/function bullets before error-note bullets
    ordered_facts = sorted(facts, key=lambda x: (1 if x.get("is_error_note") else 0))
    for fact in ordered_facts:
        if len(variants) >= 2:
            break
        d_opt = fact["option_text"]
        meaning = _mask_answer_leaks_for_reading(fact["meaning_vi"], options)
        if len(meaning) < 5:
            continue
        jp_ex = ""
        m_ex = re.search(r"ví dụ:\s*([^)）\n]+)", fact["detail"], re.IGNORECASE)
        if m_ex:
            jp_ex = m_ex.group(1).strip()
        if jp_ex and d_opt in jp_ex and not fact.get("is_error_note"):
            masked_ex = jp_ex.replace(d_opt, "（　　　）", 1)
            q_text = f"【Đảo nhiễu Ngữ cảnh】Điền từ/mẫu phù hợp vào câu ví dụ của phương án bẫy:\n{masked_ex}"
        elif fact.get("is_error_note"):
            # Skip ambiguous double-masked comparisons if clearer positive bullets exist
            if meaning.count("___") >= 2:
                continue
            q_text = (
                f"【Đảo nhiễu Nhận diện Bẫy】Phương án nào dưới đây ứng với nhận xét loại trừ sau khi xét vào câu gốc:\n"
                f"「{meaning}」\nCâu gốc: {prompt_jp}"
            )
        else:
            q_text = (
                f"【Đảo nhiễu Phân biệt】Phương án nào dưới đây diễn đạt đúng sắc thái/chức năng:\n"
                f"「{meaning}」?"
            )
        variants.append(
            {
                "variant_mode": "distractor_invert",
                "prompt_jp": q_text,
                "options": options,
                "correct_index": fact["opt_index"],
                "metadata": {"inverted_from_correct": options[correct_idx], "target_distractor": d_opt},
                "explanation_vi": f"Đảo chiều phương án nhiễu của câu gốc ({kw}): {fact['detail']}",
            }
        )

    if not variants:
        g_nb = meta.get("grammar_notebook", {})
        raw_dist = g_nb.get("distinction") or g_nb.get("meaning_vi") or str(q["translation_vi"] or kw)
        dist = _mask_answer_leaks_for_reading(raw_dist, options).strip(" .-")
        has_clue = bool(dist and re.sub(r"[～~\s_＿\-・]+", "", dist))
        if section == "reading":
            clue_line = f"\n(Kỹ năng trọng tâm: {dist})" if has_clue else ""
            fallback_prompt = f"【Đảo chiều Đọc hiểu】Chọn phương án trả lời chính xác cho câu hỏi sau (đã xáo thứ tự đáp án):{clue_line}\n{prompt_jp}"
        elif has_clue:
            fallback_prompt = f"【Đảo nhiễu Ngữ pháp】Dựa vào phân biệt sau, chọn cấu trúc đúng cho ngữ cảnh gốc:\n「{dist}」\nCâu gốc: {prompt_jp}"
        else:
            fallback_prompt = f"【Đảo nhiễu Ngữ pháp】Chọn từ/cấu trúc phù hợp nhất cho ngữ cảnh câu sau (đã xáo thứ tự đáp án):\n{prompt_jp}"
        variants.append(
            {
                "variant_mode": "distractor_invert",
                "prompt_jp": fallback_prompt,
                "options": options,
                "correct_index": correct_idx,
                "metadata": {"grammar_distinction": section != "reading"},
                "explanation_vi": explanation_vi,
            }
        )
    return variants


def generate_variants_for_question_row(q: sqlite3.Row) -> List[Dict[str, Any]]:
    """Generate >= 1 anti-rote variant drill for any question row."""
    section = q["section"]
    mondai = q["mondai_type"]

    if section == "grammar" and mondai == "問題2":
        variants = _build_star_shift_variants(q)
        if variants:
            return variants
    if section == "vocab" and mondai == "問題5":
        variants = _build_usage_error_diagnosis_variant(q)
        if variants:
            return variants
    if section == "reading":
        return _build_reading_variants(q)

    return _build_distractor_invert_variants(q)


def ensure_variants_for_questions(conn: sqlite3.Connection, question_ids: List[int]) -> int:
    """Idempotently generate anti-rote variants for specific question IDs inside a transaction."""
    if not question_ids:
        return 0
    created = 0
    placeholders = ",".join("?" for _ in question_ids)
    rows = conn.execute(
        f"SELECT * FROM QUESTIONS WHERE id IN ({placeholders})",
        tuple(question_ids),
    ).fetchall()
    for q in rows:
        existing_cnt = conn.execute(
            "SELECT COUNT(*) FROM VARIANT_DRILLS WHERE question_id=?", (q["id"],)
        ).fetchone()[0]
        if existing_cnt > 0:
            continue
        variants = generate_variants_for_question_row(q)
        for v in variants:
            conn.execute(
                """
                INSERT INTO VARIANT_DRILLS
                    (question_id, variant_mode, prompt_jp, options_json, correct_index, metadata_json, explanation_vi)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    q["id"],
                    v["variant_mode"],
                    v["prompt_jp"],
                    json.dumps(v["options"], ensure_ascii=False),
                    int(v["correct_index"]),
                    json.dumps(v.get("metadata", {}), ensure_ascii=False),
                    v.get("explanation_vi", ""),
                ),
            )
            created += 1
    return created


def ensure_variants_for_all(db_path: Optional[Path] = None) -> int:
    """Ensure 100% of questions in the database have >= 1 anti-rote variant drill."""
    with transaction(db_path) as conn:
        q_ids = [r[0] for r in conn.execute("SELECT id FROM QUESTIONS ORDER BY id").fetchall()]
        return ensure_variants_for_questions(conn, q_ids)
