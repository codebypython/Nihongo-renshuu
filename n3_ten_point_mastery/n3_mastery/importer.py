"""Smart .xlsx Importer supporting all 4 Excel layouts, deduplication, companion sheets, and Micro-Unit routing."""

import hashlib
import json
import re
import sqlite3
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple

import openpyxl

from n3_mastery.bridge_content import seed_micro_units_and_bridges
from n3_mastery.config import get_excel_dir
from n3_mastery.database import init_db, transaction

# Exact keyword routing for MU-03 (verbs / intransitive-transitive / particle collocations in 問題3)
MU03_KEYWORDS = {
    "まざって",
    "現れた",
    "やいて",
    "以降",
    "祈って",
    "事故",
    "乾燥",
    "吹いて",
    "かせいで",
    "感謝",
    "健康",
}

MU04_KEYWORDS = {
    "メッセージ",
    "べつべつに",
    "どんなに",
    "省略",
    "アイデア",
    "中止",
    "管理",
    "コミュニケーション",
    "見出し",
    "遠慮",
    "いつのまにか",
    "ホームステイ",
    "本音",
    "ぴかぴか",
    "コメント",
    "手入れ",
    "さっそく",
}

# Exact cloze questions routed to MU-08 (emphatic particles, partial negation, connectors)
MU08_CLOZE_KEYS = {
    ("月のウサギ", "【3】"),
    ("この薬の使い方", "Câu [4]"),
    ("日本人スポーツ選手", "Câu [2]"),
    ("日本人スポーツ選手", "Câu [5]"),
}

# Exact cloze questions routed to MU-07 (N4->N3 verb conjugation foundation)
MU07_CLOZE_KEYS = {
    ("この薬の使い方", "Câu [1]"),
    ("この薬の使い方", "【1】"),
    ("この薬の使い方", "Câu [2]"),
    ("この薬の使い方", "【2】"),
    ("緑のカーテン", "Câu [1]"),
}


def compute_file_hash(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def normalize_prompt_for_hash(prompt_jp: str) -> str:
    """Strip passage prefixes, normalize blank markers, and collapse whitespace for deduplication."""
    text = str(prompt_jp or "").strip()
    text = re.sub(r"^\s*【Bài đọc:\s*[^】]+】\s*", "", text)
    text = re.sub(r"^\s*【Bài\s*\d+\s*-\s*Câu\s*\d+】\s*", "", text)
    text = re.sub(r"\n*\(Lưu ý:\s*trên đề gốc[^)]*\)\s*", "", text)
    text = re.sub(r"【\s*(\d+)\s*】", r"[BLANK_\1]", text)
    text = re.sub(r"\[\s*(\d+)\s*\]", r"[BLANK_\1]", text)
    text = re.sub(r"[\s\u3000]+", "", text)
    return text.lower()


def clean_option_text(opt: Any) -> str:
    text = str(opt or "").strip()
    # Keep clean display text if raw option had historical numbering prefix like "5(1). 会員"
    cleaned = re.sub(r"^\d+\(\d+\)\.\s*", "", text)
    return cleaned


def compute_question_hash(prompt_jp: str, options: List[str]) -> str:
    norm_prompt = normalize_prompt_for_hash(prompt_jp)
    norm_opts = [re.sub(r"[\s\u3000]+", "", clean_option_text(o)).lower() for o in options]
    payload = f"{norm_prompt}||{'|'.join(norm_opts)}"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def compute_passage_hash(title: str, japanese_text: str) -> str:
    norm = re.sub(r"[\s\u3000]+", "", f"{title}||{japanese_text}")
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()


def normalize_mondai(raw_mondai: str, section: str) -> str:
    text = str(raw_mondai or "")
    m = re.search(r"(問題[1-5])", text)
    if m:
        return m.group(1)
    if section == "reading":
        if "情報検索" in text or "Tìm kiếm" in text or "案内" in text or "予約" in text or "楽しもう" in text:
            return "情報検索"
        if "3番" in text or "Đoạn trung" in text or "マグロ" in text:
            return "中文"
        return "短文"
    return text.strip() or "問題1"


def extract_star_assembly(col13_text: str, options: List[str], correct_index: int) -> Optional[Dict[str, Any]]:
    """Parse [3. 周りのことを] [1. 考えて] [★ 2. 行動する] [4. ように] or ordered sentence into 4-slot metadata."""
    raw = str(col13_text or "").strip()
    matches = list(re.finditer(r"\[(★?\s*(\d+))\.\s*([^\]]+)\]", raw))
    if len(matches) == 4:
        slots_order: List[int] = []
        star_slot_index: Optional[int] = None
        for idx, m in enumerate(matches):
            marker = m.group(1)
            opt_num = int(m.group(2)) - 1
            slots_order.append(opt_num)
            if "★" in marker:
                star_slot_index = idx
        if sorted(slots_order) == [0, 1, 2, 3]:
            if star_slot_index is None:
                star_slot_index = slots_order.index(correct_index) if 0 <= correct_index < 4 else 2
            # Extract clean assembled sentence
            sentence_line = raw.splitlines()[0]
            sentence_line = re.sub(r"^Câu hoàn chỉnh:\s*", "", sentence_line).strip()
            if "(Đề gốc:" in raw:
                m_orig = re.search(r"\(Đề gốc:\s*([^)]+)\)", raw)
                if m_orig:
                    sentence_line = m_orig.group(1).strip()
            # Build prefix/suffix relative to sentence_line
            first_chunk_token = matches[0].group(0)
            last_chunk_token = matches[-1].group(0)
            if first_chunk_token in sentence_line and last_chunk_token in sentence_line:
                prefix = sentence_line.split(first_chunk_token, 1)[0].strip()
                suffix = sentence_line.rsplit(last_chunk_token, 1)[-1].strip()
            else:
                prefix = ""
                suffix = ""
            full_sentence = re.sub(r"\[(★?\s*\d+)\.\s*([^\]]+)\]", r"\2", sentence_line)
            full_sentence = re.sub(r"\s+", "", full_sentence)
            return {
                "slots_order": slots_order,
                "star_slot_index": star_slot_index,
                "chunks": options,
                "prefix": prefix,
                "suffix": suffix,
                "full_sentence": full_sentence,
                "original_star_option_index": correct_index,
            }

    # Fallback: deduce 4-slot order when col 13 contains a complete sentence without [1. ...] brackets
    if not raw or len(options) != 4 or not (0 <= correct_index < 4):
        return None
    sentence_line = raw.splitlines()[0]
    sentence_line = re.sub(r"^Câu hoàn chỉnh:\s*", "", sentence_line).strip()
    if "(Đề gốc:" in raw:
        m_orig = re.search(r"\(Đề gốc:\s*([^)]+)\)", raw)
        if m_orig:
            sentence_line = m_orig.group(1).strip()
    compact_line = re.sub(r"[\s\u3000]+", "", sentence_line)
    if not compact_line:
        return None

    def _match_order(cand_opts: List[str]) -> Optional[Dict[int, Tuple[int, int]]]:
        if not all(cand_opts) or len(set(cand_opts)) != 4:
            return None
        used_ranges: List[Tuple[int, int]] = []
        found_spans: Dict[int, Tuple[int, int]] = {}
        for opt_idx in sorted(range(4), key=lambda i: -len(cand_opts[i])):
            tok = cand_opts[opt_idx]
            search_pos = 0
            matched_span: Optional[Tuple[int, int]] = None
            while True:
                pos = compact_line.find(tok, search_pos)
                if pos == -1:
                    break
                end = pos + len(tok)
                if not any(not (end <= s or pos >= e) for s, e in used_ranges):
                    matched_span = (pos, end)
                    break
                search_pos = pos + 1
            if matched_span is None:
                return None
            used_ranges.append(matched_span)
            found_spans[opt_idx] = matched_span
        return found_spans

    cleaned_opts = [re.sub(r"[\s\u3000]+", "", clean_option_text(o)) for o in options]
    found_spans = _match_order(cleaned_opts)
    if found_spans is None:
        # Retry stripping inline furigana （...） from options in case col 13 omitted furigana
        nofuri_opts = [re.sub(r"（[^）]{1,12}）", "", co) for co in cleaned_opts]
        found_spans = _match_order(nofuri_opts)
    if found_spans is None:
        return None
    slots_order = sorted(range(4), key=lambda i: found_spans[i][0])
    first_start = found_spans[slots_order[0]][0]
    last_end = found_spans[slots_order[-1]][1]
    return {
        "slots_order": slots_order,
        "star_slot_index": slots_order.index(correct_index),
        "chunks": options,
        "prefix": compact_line[:first_start],
        "suffix": compact_line[last_end:],
        "full_sentence": compact_line,
        "original_star_option_index": correct_index,
    }


def segment_japanese_sentences(japanese_text: str) -> List[str]:
    """Split a Dokkai passage into clean, selectable Japanese sentences/condition lines."""
    lines = [ln.strip() for ln in str(japanese_text or "").splitlines()]
    segments: List[str] = []
    for ln in lines:
        if not ln:
            continue
        if re.fullmatch(r"[-－─=＝]+", ln):
            continue
        if re.fullmatch(r"【[^】]+】", ln):
            continue
        # Remove leading 【...】 tag if inline? Keep content lines intact
        # Split line by Japanese period 。 keeping 。 attached
        parts = re.split(r"(?<=。)", ln)
        for p in parts:
            cleaned = p.strip().lstrip("\u3000").strip()
            if not cleaned:
                continue
            if re.fullmatch(r"[-－─=＝]+", cleaned):
                continue
            segments.append(cleaned)
    return segments


def _normalize_match_text(s: str) -> str:
    s = re.sub(r"（[^）]{1,30}）", "", s)  # remove inline furigana or (注1:...) notes
    s = re.sub(r"\([^)]{1,30}\)", "", s)
    s = re.sub(r"[「」『』【】\s\u3000・、。,:：…\.\-－\(\)（）●①②③④〈〉<>]+", "", s)
    return s.lower()


def _extract_gold_explanation_head(explanation_vi: str) -> str:
    """Keep only the affirmative evidence part of explanation_vi, excluding trap/elimination sections."""
    if not explanation_vi:
        return ""
    parts = re.split(
        r"(?m)^\s*[•\-]?\s*(?:Phân tích bẫy|Bẫy|Loại trừ|Vì sao các câu|Vì sao các đáp án|3 loại bẫy)\b",
        explanation_vi,
        maxsplit=1,
    )
    return parts[0]


def find_evidence_indices(
    sentences: List[str],
    explanation_vi: str,
    companion_evidence: Optional[str] = None,
    condition_info: Optional[Dict[str, Any]] = None,
) -> List[int]:
    """Find matching sentence indices in `sentences` based on gold Japanese evidence & conditions."""
    quotes: List[str] = []
    if companion_evidence:
        # Handle nested 『...』 inside 「...」 as well as whole companion sentence
        for m in re.findall(r"[「『']([^」』']{4,})[」』']", companion_evidence):
            quotes.append(m)
        quotes.append(companion_evidence)

    gold_expl = _extract_gold_explanation_head(explanation_vi)
    if gold_expl:
        for m in re.findall(r"['「『]([^'」』\n]{4,})['」』]", gold_expl):
            if re.search(r"[\u3040-\u30ff\u4e00-\u9faf]", m):
                quotes.append(m)

    if condition_info:
        for k in ("condition_1", "condition_2", "hidden_condition"):
            val = str(condition_info.get(k, "") or "")
            # Exclude negated trap comparisons after ≠
            affirmative_val = val.split("≠")[0]
            for m in re.findall(r"['「『]([^'」』\n]{3,})['」』]", affirmative_val):
                if re.search(r"[\u3040-\u30ff\u4e00-\u9faf]", m):
                    quotes.append(m)
        combined_cond = " ".join(
            str(condition_info.get(k, "") or "").split("≠")[0]
            for k in ("condition_1", "condition_2", "hidden_condition", "matched_answer")
        )
        # Explicit Japanese flyer/notice anchors (stored as (trigger_substring, jp_match_pattern, boost_weight))
        explicit_anchors = [
            ("休診", "休診", 12),
            ("注意", "注意", 12),
            ("テキスト代は別", "テキスト代は別", 12),
            ("受講料", "受講料", 10),
            ("4,500", "4500円", 14),
            ("4500", "4500円", 14),
            ("9:00 sáng", "前日の午前9時", 14),
            ("対象とする本", "対象とする本", 12),
            ("番号を押して", "番号を押して", 12),
            ("病院が休みの日でも", "病院が休みの日でも", 14),
            ("1回目の日にいただきます", "1回目の日にいただきます", 14),
            ("0～18さい", "0～18さい", 12),
            ("0～3さい", "0～3さい", 12),
        ]
        boosted_anchors: List[Tuple[str, int]] = []
        for trig, jp_pat, w in explicit_anchors:
            if trig in combined_cond or trig in gold_expl:
                boosted_anchors.append((jp_pat, w))
    else:
        boosted_anchors = []

    # Also check specific high-signal anchors inside gold_expl (e.g., Eメール, 電話, 注1)
    for anchor in ("Eメール", "電話でのお問い合わせ", "問い合わせ", "わからないことを聞くこと"):
        if anchor in gold_expl or (companion_evidence and anchor in companion_evidence):
            quotes.append(anchor)

    # Deduplicate quotes preserving order, preferring longer specific phrases over tiny tags
    norm_sentences = [_normalize_match_text(s) for s in sentences]
    scored_hits: Dict[int, int] = {}

    for jp_pat, w in boosted_anchors:
        np = _normalize_match_text(jp_pat)
        if np:
            for idx, ns in enumerate(norm_sentences):
                if ns and np in ns:
                    scored_hits[idx] = max(scored_hits.get(idx, 0), w)

    for q in quotes:
        subparts = [sp.strip() for sp in re.split(r"[…\.]{1,3}|／|。|●", q) if len(sp.strip()) >= 3]
        if not subparts:
            subparts = [q]
        for sp in subparts:
            nq = _normalize_match_text(sp)
            if len(nq) < 3:
                continue
            for idx, ns in enumerate(norm_sentences):
                if not ns:
                    continue
                if nq in ns or (len(ns) >= 6 and ns in nq):
                    # Weight by specificity so full clause matches outrank generic 4-char keywords
                    scored_hits[idx] = max(scored_hits.get(idx, 0), len(nq))

    if scored_hits:
        # Prefer sentences with specificity >= 5 if any exist; keep up to 5 best-matched indices
        strong = [idx for idx, w in scored_hits.items() if w >= 5]
        pool = strong if strong else list(scored_hits.keys())
        ranked = sorted(pool, key=lambda i: (-scored_hits[i], i))[:5]
        return sorted(ranked)

    # Fallback: score token overlap if nothing exact matched
    if sentences:
        jp_tokens = re.findall(r"[\u4e00-\u9faf\u3040-\u30ff]{3,}", f"{companion_evidence or ''} {gold_expl}")
        best_idx = 0
        best_score = -1
        for idx, ns in enumerate(norm_sentences):
            score = sum(1 for tok in jp_tokens if _normalize_match_text(tok) in ns)
            if score > best_score:
                best_score = score
                best_idx = idx
        return [best_idx]

    return []


def assign_micro_unit(
    section: str,
    mondai_type: str,
    focus_keyword: str,
    prompt_jp: str,
    passage_title: str = "",
    source_label: str = "",
) -> str:
    """Route a question deterministically to one of the 12 Micro-Units (MU-01..MU-12)."""
    if section == "vocab":
        if mondai_type == "問題1":
            return "MU-01"
        if mondai_type == "問題2":
            return "MU-02"
        if mondai_type == "問題4":
            return "MU-05"
        if mondai_type == "問題5":
            return "MU-06"
        # 問題3 splits cleanly into MU-03 (11 verb/particle collocation items) & MU-04 (17 compound/katakana/adverb items)
        kw = str(focus_keyword or "").strip()
        if kw in MU03_KEYWORDS:
            return "MU-03"
        if kw in MU04_KEYWORDS:
            return "MU-04"
        # Heuristic fallback for future uploaded workbooks
        if not re.search(r"[\u30a0-\u30ff]", kw) and not re.fullmatch(r"[\u4e00-\u9faf]{2,}", kw):
            if any(p in prompt_jp for p in ("が（", "を（", "にあう", "に感謝")):
                return "MU-03"
        return "MU-04"

    if section == "grammar":
        if mondai_type == "問題2":
            return "MU-10"
        if mondai_type == "問題3":
            key = (passage_title.strip(), source_label.strip())
            if key in MU07_CLOZE_KEYS:
                return "MU-07"
            if key in MU08_CLOZE_KEYS:
                return "MU-08"
            return "MU-09"
        # 問題1 grammar single sentence
        kw = str(focus_keyword or "")
        if any(marker in kw for marker in ("Vえる", "V(sai khiến)", "Vる + のに", "Vた + つもり", "Vて + ばかりいると", "Vない + ように", "Vます + たて")):
            return "MU-07"
        return "MU-08"

    # Reading section
    if mondai_type == "情報検索":
        return "MU-12"
    return "MU-11"


def detect_layout(wb: openpyxl.Workbook) -> str:
    """Detect workbook layout from primary question sheets (companion sheets are optional)."""
    names = set(wb.sheetnames)
    if "Tong_Hop_On_Thi" in names:
        return "vocab_35"
    if names & {"Phan_I_Tu_Vung_Kanji", "Phan_II_Ngu_Phap", "Phan_III_Doc_Hai"}:
        return "comprehensive_3_part"
    if "Bai_Doc_Va_Luyen_Tap" in names:
        return "grammar_cloze_3_passages"
    if "Dokkai_Doan_Van_Ngan" in names:
        return "dokkai_short"
    if "Tim_Kiem_Thong_Tin_Dokkai" in names:
        return "dokkai_info"
    raise ValueError(f"Không nhận diện được định dạng sheet từ danh sách: {sorted(names)}")


_BANNER_PREFIXES = (
    "ĐỀ THI",
    "ĐỀ MỞ",
    "ĐỀ TÙY",
    "ĐỀ UPLOAD",
    "LUYỆN THI",
    "Thiết kế chuyên biệt",
    "Hướng dẫn",
    "BẢNG TỔNG HỢP",
    "SỔ TAY",
    "MA TRẬN",
    "TOÀN VĂN",
    "Gói bài đọc",
    "Gói thể loại",
    "Gói câu hỏi",
    "Toàn bộ số liệu",
)


def _is_banner_or_header_line(text: str) -> bool:
    s = str(text or "").strip()
    return not s or s.startswith(_BANNER_PREFIXES)


def _is_passage_row(ws: Any, r: int, c1: str) -> bool:
    """Detect whether row r holds a reading/cloze passage (with or without leading 【...】)."""
    if not c1:
        return False
    if ws.cell(r, 4).value is not None or ws.cell(r, 5).value is not None:
        return False
    if c1.startswith("【"):
        return True
    if _is_banner_or_header_line(c1):
        return False
    if ws.cell(r, 2).value is not None or ws.cell(r, 10).value is not None:
        return False
    if c1.startswith(("III-", "Phần III", "Gói ", "Bài ")):
        return False
    jp_chars = re.findall(r"[\u3040-\u30ff\u4e00-\u9faf]", c1)
    has_translation = bool(str(ws.cell(r, 8).value or "").strip())
    return bool(jp_chars) and (has_translation or "。" in c1 or "\n" in c1 or len(jp_chars) >= 8)


def _is_header_options(raw_opts: List[Any]) -> bool:
    strs = [str(o or "").strip() for o in raw_opts]
    return strs == ["Đáp án 1", "Đáp án 2", "Đáp án 3", "Đáp án 4"] or strs == ["Đ1", "Đ2", "Đ3", "Đ4"]


def _parse_int_answer(val: Any) -> Optional[int]:
    if isinstance(val, (int, float)) and not isinstance(val, bool):
        iv = int(val)
        if 1 <= iv <= 4:
            return iv - 1
    if isinstance(val, str):
        s = val.strip().translate(str.maketrans("１２３４", "1234"))
        if s.isdigit():
            iv = int(s)
            if 1 <= iv <= 4:
                return iv - 1
        m = re.match(r"^([1-4])\s*[\.．\):：]\s*\S*", s)
        if m:
            return int(m.group(1)) - 1
    return None


def _upsert_passage(
    conn: sqlite3.Connection,
    title: str,
    genre: str,
    section: str,
    japanese_text: str,
    vietnamese_text: str,
    evidence_sentences: List[str],
    condition_matrix: List[Dict[str, Any]],
) -> int:
    """Insert or upgrade a passage (specifically upgrades 3-blank この薬の使い方 to full 5-blank version)."""
    # First check if a grammar cloze passage with the exact same title exists (case: この薬の使い方)
    if section == "grammar":
        existing = conn.execute(
            "SELECT id, japanese_text, vietnamese_text, evidence_sentences_json FROM PASSAGES WHERE section='grammar' AND title=?",
            (title,),
        ).fetchone()
        if existing:
            if len(japanese_text) > len(existing["japanese_text"]):
                new_hash = compute_passage_hash(title, japanese_text)
                conn.execute(
                    """
                    UPDATE PASSAGES
                    SET content_hash=?, japanese_text=?, vietnamese_text=?, evidence_sentences_json=?, condition_matrix_json=?
                    WHERE id=?
                    """,
                    (
                        new_hash,
                        japanese_text,
                        vietnamese_text,
                        json.dumps(evidence_sentences, ensure_ascii=False),
                        json.dumps(condition_matrix, ensure_ascii=False),
                        existing["id"],
                    ),
                )
            return int(existing["id"])

    p_hash = compute_passage_hash(title, japanese_text)
    existing_by_hash = conn.execute("SELECT id FROM PASSAGES WHERE content_hash=?", (p_hash,)).fetchone()
    if existing_by_hash:
        return int(existing_by_hash["id"])

    cur = conn.execute(
        """
        INSERT INTO PASSAGES
            (content_hash, title, genre, section, japanese_text, vietnamese_text, evidence_sentences_json, condition_matrix_json)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            p_hash,
            title,
            genre,
            section,
            japanese_text,
            vietnamese_text,
            json.dumps(evidence_sentences, ensure_ascii=False),
            json.dumps(condition_matrix, ensure_ascii=False),
        ),
    )
    return int(cur.lastrowid)


def _upsert_question(
    conn: sqlite3.Connection,
    workbook_id: int,
    q_data: Dict[str, Any],
) -> Tuple[int, bool]:
    """Insert question or merge richer metadata on duplicate hash. Returns (question_id, is_new)."""
    options = q_data["options"]
    options_json = json.dumps(options, ensure_ascii=False)
    q_hash = compute_question_hash(q_data["prompt_jp"], options)
    existing = conn.execute(
        "SELECT id, passage_id, notebook_meta_json, explanation_vi, unit_code, prompt_jp FROM QUESTIONS WHERE content_hash=?",
        (q_hash,),
    ).fetchone()

    # Also deduplicate grammar-cloze blanks on the same passage where one excerpt omits a leading conjunction (e.g. また、)
    if existing is None and q_data.get("passage_id") is not None and q_data.get("mondai_type") == "問題3":
        norm_in = normalize_prompt_for_hash(q_data["prompt_jp"])
        candidates = conn.execute(
            """
            SELECT id, passage_id, notebook_meta_json, explanation_vi, unit_code, prompt_jp
            FROM QUESTIONS
            WHERE passage_id=? AND options_json=?
            """,
            (q_data["passage_id"], options_json),
        ).fetchall()
        for cand in candidates:
            norm_ex = normalize_prompt_for_hash(cand["prompt_jp"])
            if norm_in in norm_ex or norm_ex in norm_in:
                existing = cand
                break

    if existing:
        q_id = int(existing["id"])
        old_meta = json.loads(existing["notebook_meta_json"] or "{}")
        new_meta = q_data.get("notebook_meta", {})
        merged_meta = {**old_meta, **new_meta}

        # Prefer richer explanation & full 5-blank passage link if applicable
        new_passage_id = existing["passage_id"]
        if q_data.get("passage_id") is not None:
            if new_passage_id is None:
                new_passage_id = q_data["passage_id"]
            else:
                old_p = conn.execute("SELECT japanese_text FROM PASSAGES WHERE id=?", (new_passage_id,)).fetchone()
                new_p = conn.execute("SELECT japanese_text FROM PASSAGES WHERE id=?", (q_data["passage_id"],)).fetchone()
                if new_p and (not old_p or len(new_p["japanese_text"]) >= len(old_p["japanese_text"])):
                    new_passage_id = q_data["passage_id"]

        new_expl = q_data["explanation_vi"]
        if len(existing["explanation_vi"] or "") > len(new_expl or ""):
            new_expl = existing["explanation_vi"]

        # Prefer canonical grammar_notebook source metadata (focus_keyword, unit_code) regardless of file import order
        prefer_incoming = "grammar_notebook" in new_meta and "grammar_notebook" not in old_meta
        row_extra = conn.execute(
            "SELECT focus_keyword, translation_vi, unit_code FROM QUESTIONS WHERE id=?",
            (q_id,),
        ).fetchone()
        new_focus = q_data.get("focus_keyword", "") if prefer_incoming else (row_extra["focus_keyword"] or q_data.get("focus_keyword", ""))
        new_trans = row_extra["translation_vi"] or q_data.get("translation_vi", "")
        new_unit = q_data["unit_code"] if prefer_incoming else row_extra["unit_code"]

        conn.execute(
            """
            UPDATE QUESTIONS
            SET passage_id=?, notebook_meta_json=?, explanation_vi=?, focus_keyword=?, translation_vi=?, unit_code=?
            WHERE id=?
            """,
            (
                new_passage_id,
                json.dumps(merged_meta, ensure_ascii=False),
                new_expl,
                new_focus,
                new_trans,
                new_unit,
                q_id,
            ),
        )
        conn.execute(
            "INSERT OR IGNORE INTO QUESTION_SOURCES (question_id, workbook_id, source_label) VALUES (?, ?, ?)",
            (q_id, workbook_id, q_data["source_label"]),
        )
        return q_id, False

    cur = conn.execute(
        """
        INSERT INTO QUESTIONS (
            content_hash, workbook_id, unit_code, passage_id, section,
            mondai_type, source_label, focus_keyword, prompt_jp,
            options_json, correct_index, translation_vi, explanation_vi, notebook_meta_json
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            q_hash,
            workbook_id,
            q_data["unit_code"],
            q_data.get("passage_id"),
            q_data["section"],
            q_data["mondai_type"],
            q_data["source_label"],
            q_data.get("focus_keyword", ""),
            q_data["prompt_jp"],
            options_json,
            q_data["correct_index"],
            q_data.get("translation_vi", ""),
            q_data.get("explanation_vi", ""),
            json.dumps(q_data.get("notebook_meta", {}), ensure_ascii=False),
        ),
    )
    q_id = int(cur.lastrowid)
    conn.execute("INSERT OR IGNORE INTO FSRS_STATES (question_id) VALUES (?)", (q_id,))
    conn.execute(
        "INSERT OR IGNORE INTO QUESTION_SOURCES (question_id, workbook_id, source_label) VALUES (?, ?, ?)",
        (q_id, workbook_id, q_data["source_label"]),
    )
    return q_id, True


def _parse_layout_vocab_35(wb: openpyxl.Workbook, conn: sqlite3.Connection, workbook_id: int) -> Tuple[int, int, List[int]]:
    ws = wb["Tong_Hop_On_Thi"]
    ws_nb = wb["So_Tay_Tu_Vung"] if "So_Tay_Tu_Vung" in wb.sheetnames else None
    ws_strat = wb["Thong_Ke_Chien_Thuat"] if "Thong_Ke_Chien_Thuat" in wb.sheetnames else None

    so_tay_map: Dict[str, Dict[str, str]] = {}
    if ws_nb is not None:
        for r in range(2, ws_nb.max_row + 1):
            src = str(ws_nb.cell(r, 2).value or "").strip()
            word = str(ws_nb.cell(r, 3).value or "").strip()
            if not src or not word or src in ("Nguồn câu", "Nguồn bài") or word in ("Từ vựng", "Từ vựng / Kanji"):
                continue
            so_tay_map[src] = {
                "source_ref": src,
                "word": word,
                "hiragana": str(ws_nb.cell(r, 4).value or "").strip(),
                "han_viet": str(ws_nb.cell(r, 5).value or "").strip(),
                "meaning_vi": str(ws_nb.cell(r, 6).value or "").strip(),
                "collocation_tip": str(ws_nb.cell(r, 7).value or "").strip(),
            }

    strat_map: Dict[str, Dict[str, str]] = {}
    if ws_strat is not None:
        for r in range(2, ws_strat.max_row + 1):
            m_name = str(ws_strat.cell(r, 1).value or "").strip()
            if not m_name or m_name.startswith(("TỔNG", "BẢNG", "Các cột", "Gói câu hỏi")):
                continue
            m = re.search(r"(問題[1-5])", m_name)
            if m:
                strat_map[m.group(1)] = {
                    "traps": str(ws_strat.cell(r, 8).value or "").strip(),
                    "tactics": str(ws_strat.cell(r, 9).value or "").strip(),
                }

    raw_count = 0
    imported_count = 0
    question_ids: List[int] = []
    for r in range(1, ws.max_row + 1):
        ans_idx = _parse_int_answer(ws.cell(r, 11).value)
        raw_opts = [ws.cell(r, c).value for c in range(5, 9)]
        if ans_idx is None or not all(o is not None for o in raw_opts) or _is_header_options(raw_opts):
            continue
        raw_count += 1
        mondai_raw = str(ws.cell(r, 1).value or "").strip()
        mondai_type = normalize_mondai(mondai_raw, "vocab")
        q_num = str(ws.cell(r, 2).value or "").strip()
        src_label = f"Câu {q_num}" if q_num.isdigit() else q_num
        focus_kw = str(ws.cell(r, 3).value or "").strip()
        prompt_jp = str(ws.cell(r, 4).value or "").strip()
        options = [clean_option_text(o) for o in raw_opts]
        translation_vi = str(ws.cell(r, 13).value or "").strip()
        explanation_vi = str(ws.cell(r, 14).value or "").strip()

        meta: Dict[str, Any] = {}
        if src_label in so_tay_map:
            meta["so_tay"] = so_tay_map[src_label]
        if mondai_type in strat_map:
            meta["strategy_tip"] = strat_map[mondai_type]

        unit_code = assign_micro_unit("vocab", mondai_type, focus_kw, prompt_jp, source_label=src_label)
        q_id, is_new = _upsert_question(
            conn,
            workbook_id,
            {
                "unit_code": unit_code,
                "passage_id": None,
                "section": "vocab",
                "mondai_type": mondai_type,
                "source_label": src_label,
                "focus_keyword": focus_kw,
                "prompt_jp": prompt_jp,
                "options": options,
                "correct_index": ans_idx,
                "translation_vi": translation_vi,
                "explanation_vi": explanation_vi,
                "notebook_meta": meta,
            },
        )
        question_ids.append(q_id)
        if is_new:
            imported_count += 1
    return raw_count, imported_count, question_ids


def _parse_layout_comprehensive(wb: openpyxl.Workbook, conn: sqlite3.Connection, workbook_id: int) -> Tuple[int, int, List[int]]:
    raw_count = 0
    imported_count = 0
    question_ids: List[int] = []

    # 1. Dashboard strategy notes per package (optional companion sheet)
    dash_tips: Dict[str, Dict[str, str]] = {}
    if "Dashboard_Tong_Quan" in wb.sheetnames:
        ws_dash = wb["Dashboard_Tong_Quan"]
        for r in range(2, ws_dash.max_row + 1):
            pkg = str(ws_dash.cell(r, 1).value or "").strip()
            if pkg and not pkg.startswith(("TỔNG", "BẢNG", "Toàn bộ", "Gói câu hỏi")):
                dash_tips[pkg] = {
                    "traps": str(ws_dash.cell(r, 8).value or "").strip(),
                    "tactics": str(ws_dash.cell(r, 9).value or "").strip(),
                }

    # 2. Phan I: Vocab & Kanji (optional sheet)
    if "Phan_I_Tu_Vung_Kanji" in wb.sheetnames:
        ws1 = wb["Phan_I_Tu_Vung_Kanji"]
        for r in range(1, ws1.max_row + 1):
            ans_idx = _parse_int_answer(ws1.cell(r, 11).value)
            raw_opts = [ws1.cell(r, c).value for c in range(5, 9)]
            if ans_idx is None or not all(o is not None for o in raw_opts) or _is_header_options(raw_opts):
                continue
            raw_count += 1
            pkg_raw = str(ws1.cell(r, 1).value or "").strip()
            mondai_type = normalize_mondai(pkg_raw, "vocab")
            src_label = str(ws1.cell(r, 2).value or "").strip()
            focus_kw = str(ws1.cell(r, 3).value or "").strip()
            prompt_jp = str(ws1.cell(r, 4).value or "").strip()
            options = [clean_option_text(o) for o in raw_opts]
            raw_opt_strings = [str(o).strip() for o in raw_opts]
            translation_vi = str(ws1.cell(r, 13).value or "").strip()
            explanation_vi = str(ws1.cell(r, 14).value or "").strip()
            meta: Dict[str, Any] = {}
            if options != raw_opt_strings:
                meta["raw_options"] = raw_opt_strings
            if pkg_raw in dash_tips:
                meta["strategy_tip"] = dash_tips[pkg_raw]
            unit_code = assign_micro_unit("vocab", mondai_type, focus_kw, prompt_jp, source_label=src_label)
            q_id, is_new = _upsert_question(
                conn,
                workbook_id,
                {
                    "unit_code": unit_code,
                    "passage_id": None,
                    "section": "vocab",
                    "mondai_type": mondai_type,
                    "source_label": src_label,
                    "focus_keyword": focus_kw,
                    "prompt_jp": prompt_jp,
                    "options": options,
                    "correct_index": ans_idx,
                    "translation_vi": translation_vi,
                    "explanation_vi": explanation_vi,
                    "notebook_meta": meta,
                },
            )
            question_ids.append(q_id)
            if is_new:
                imported_count += 1

    # 3. Phan II: Grammar (問題1, 問題2 ★, 問題3 cloze + 1 or more passages; optional sheet)
    if "Phan_II_Ngu_Phap" in wb.sheetnames:
        ws2 = wb["Phan_II_Ngu_Phap"]
        cloze_passages_by_title: Dict[str, int] = {}
        cloze_blocks: List[Tuple[int, str, int]] = []
        consumed_rows: set[int] = set()
        pending_p3_title = ""

        for r in range(1, ws2.max_row + 1):
            if r in consumed_rows:
                continue
            c1 = str(ws2.cell(r, 1).value or "").strip()
            if c1.startswith("TOÀN VĂN ĐOẠN ĐỌC"):
                m_title = re.search(r"「([^」]+)」", c1)
                c_title = m_title.group(1).strip() if m_title else (pending_p3_title or f"Cloze Passage {len(cloze_blocks) + 1}")
                pending_p3_title = ""
                for r2 in range(r + 1, ws2.max_row + 1):
                    jp_raw = str(ws2.cell(r2, 1).value or "").strip()
                    if jp_raw:
                        consumed_rows.add(r2)
                        vi_raw = str(ws2.cell(r2, 8).value or "").strip()
                        jp_clean = re.sub(r"^【Đoạn văn gốc tiếng Nhật】\s*", "", jp_raw).strip()
                        vi_clean = re.sub(r"^【Bản dịch tiếng Việt[^】]*】\s*", "", vi_raw).strip()
                        sents = segment_japanese_sentences(jp_clean)
                        cp_id = _upsert_passage(
                            conn,
                            title=c_title,
                            genre="文章の文法",
                            section="grammar",
                            japanese_text=jp_clean,
                            vietnamese_text=vi_clean,
                            evidence_sentences=sents,
                            condition_matrix=[],
                        )
                        cloze_passages_by_title[c_title] = cp_id
                        cloze_blocks.append((r, c_title, cp_id))
                        break
            elif c1.startswith(("II-3.", "Gói ", "Bài ")) and ws2.cell(r, 5).value is None and ws2.cell(r, 11).value is None:
                m_t = re.search(r"「([^」]+)」|\(([^)]+)\)", c1)
                if m_t:
                    pending_p3_title = (m_t.group(1) or m_t.group(2) or "").strip()
            elif _is_passage_row(ws2, r, c1) and ws2.cell(r, 11).value is None:
                vi_raw = str(ws2.cell(r, 8).value or "").strip()
                jp_clean = re.sub(r"^【Đoạn văn gốc tiếng Nhật】\s*", "", c1).strip()
                vi_clean = re.sub(r"^【Bản dịch tiếng Việt[^】]*】\s*", "", vi_raw).strip()
                c_title = pending_p3_title or (c1.splitlines()[0].strip("【】 ") if c1.startswith("【") else f"Cloze Passage {len(cloze_blocks) + 1}")
                pending_p3_title = ""
                sents = segment_japanese_sentences(jp_clean)
                cp_id = _upsert_passage(
                    conn,
                    title=c_title,
                    genre="文章の文法",
                    section="grammar",
                    japanese_text=jp_clean,
                    vietnamese_text=vi_clean,
                    evidence_sentences=sents,
                    condition_matrix=[],
                )
                cloze_passages_by_title[c_title] = cp_id
                cloze_blocks.append((r, c_title, cp_id))

        first_q3_row: Optional[int] = None
        for r in range(1, ws2.max_row + 1):
            a_idx = _parse_int_answer(ws2.cell(r, 11).value)
            r_opts = [ws2.cell(r, c).value for c in range(5, 9)]
            if a_idx is not None and all(o is not None for o in r_opts) and not _is_header_options(r_opts):
                if normalize_mondai(str(ws2.cell(r, 1).value or "").strip(), "grammar") == "問題3":
                    first_q3_row = r
                    break

        for r in range(1, ws2.max_row + 1):
            ans_idx = _parse_int_answer(ws2.cell(r, 11).value)
            raw_opts = [ws2.cell(r, c).value for c in range(5, 9)]
            if ans_idx is None or not all(o is not None for o in raw_opts) or _is_header_options(raw_opts):
                continue
            raw_count += 1
            pkg_raw = str(ws2.cell(r, 1).value or "").strip()
            mondai_type = normalize_mondai(pkg_raw, "grammar")
            src_label = str(ws2.cell(r, 2).value or "").strip()
            focus_kw = str(ws2.cell(r, 3).value or "").strip()
            prompt_jp = str(ws2.cell(r, 4).value or "").strip()
            options = [clean_option_text(o) for o in raw_opts]
            col13 = str(ws2.cell(r, 13).value or "").strip()
            explanation_vi = str(ws2.cell(r, 14).value or "").strip()
            meta = {}
            if pkg_raw in dash_tips:
                meta["strategy_tip"] = dash_tips[pkg_raw]

            p_id = None
            p_title = ""
            if mondai_type == "問題2":
                star_meta = extract_star_assembly(col13, options, ans_idx)
                if star_meta:
                    meta["star_assembly"] = star_meta
            elif mondai_type == "問題3":
                m_pt = re.search(r"\(([^)]+)\)|「([^」]+)」", pkg_raw)
                m_bt = re.search(r"【Bài đọc:\s*([^】]+)】", prompt_jp)
                extracted_pt = ""
                if m_pt:
                    extracted_pt = (m_pt.group(1) or m_pt.group(2) or "").strip()
                elif m_bt:
                    extracted_pt = m_bt.group(1).strip()
                if extracted_pt and extracted_pt in cloze_passages_by_title:
                    p_id = cloze_passages_by_title[extracted_pt]
                    p_title = extracted_pt
                elif cloze_blocks:
                    passages_precede = first_q3_row is not None and cloze_blocks[0][0] < first_q3_row
                    chosen_block = None
                    if passages_precede:
                        prior_blocks = [b for b in cloze_blocks if b[0] < r]
                        chosen_block = prior_blocks[-1] if prior_blocks else cloze_blocks[0]
                    else:
                        next_blocks = [b for b in cloze_blocks if b[0] > r]
                        chosen_block = next_blocks[0] if next_blocks else cloze_blocks[-1]
                    p_title = extracted_pt or chosen_block[1]
                    p_id = chosen_block[2]

            unit_code = assign_micro_unit(
                "grammar",
                mondai_type,
                focus_kw,
                prompt_jp,
                passage_title=p_title,
                source_label=src_label,
            )
            q_id, is_new = _upsert_question(
                conn,
                workbook_id,
                {
                    "unit_code": unit_code,
                    "passage_id": p_id,
                    "section": "grammar",
                    "mondai_type": mondai_type,
                    "source_label": src_label,
                    "focus_keyword": focus_kw,
                    "prompt_jp": prompt_jp,
                    "options": options,
                    "correct_index": ans_idx,
                    "translation_vi": col13,
                    "explanation_vi": explanation_vi,
                    "notebook_meta": meta,
                },
            )
            question_ids.append(q_id)
            if is_new:
                imported_count += 1

    # 4. Phan III: Reading (multi-block passages + questions; optional sheet)
    if "Phan_III_Doc_Hai" in wb.sheetnames:
        ws3 = wb["Phan_III_Doc_Hai"]
        cur_title = ""
        cur_genre = "短文"
        cur_passage_id: Optional[int] = None
        cur_sentences: List[str] = []

        for r in range(1, ws3.max_row + 1):
            c1 = str(ws3.cell(r, 1).value or "").strip()
            ans_idx = _parse_int_answer(ws3.cell(r, 10).value)
            raw_opts = [ws3.cell(r, c).value for c in range(4, 8)]

            if ans_idx is not None and all(o is not None for o in raw_opts) and not _is_header_options(raw_opts):
                raw_count += 1
                pkg_raw = c1
                src_label = str(ws3.cell(r, 2).value or "").strip()
                prompt_jp = str(ws3.cell(r, 3).value or "").strip()
                options = [clean_option_text(o) for o in raw_opts]
                skill = str(ws3.cell(r, 12).value or "").strip()
                explanation_vi = str(ws3.cell(r, 13).value or "").strip()
                mondai_type = cur_genre if cur_genre in ("短文", "中文", "情報検索") else normalize_mondai(pkg_raw, "reading")

                ev_indices = find_evidence_indices(cur_sentences, explanation_vi)
                meta = {
                    "dokkai_skill": skill,
                    "evidence_indices": ev_indices,
                }
                unit_code = assign_micro_unit("reading", mondai_type, skill, prompt_jp, passage_title=cur_title, source_label=src_label)
                q_id, is_new = _upsert_question(
                    conn,
                    workbook_id,
                    {
                        "unit_code": unit_code,
                        "passage_id": cur_passage_id,
                        "section": "reading",
                        "mondai_type": mondai_type,
                        "source_label": src_label,
                        "focus_keyword": skill,
                        "prompt_jp": prompt_jp,
                        "options": options,
                        "correct_index": ans_idx,
                        "translation_vi": "",
                        "explanation_vi": explanation_vi,
                        "notebook_meta": meta,
                    },
                )
                question_ids.append(q_id)
                if is_new:
                    imported_count += 1
            elif c1.startswith(("III-", "Phần III", "Gói ", "Bài ")) and not _is_banner_or_header_line(c1) and ws3.cell(r, 4).value is None:
                cur_title = c1
                if "情報検索" in c1 or "Tìm kiếm" in c1:
                    cur_genre = "情報検索"
                elif "3番" in c1 or "Đoạn trung" in c1 or "マグロ" in c1:
                    cur_genre = "中文"
                else:
                    cur_genre = "短文"
            elif _is_passage_row(ws3, r, c1):
                vi_text = str(ws3.cell(r, 8).value or "").strip()
                cur_sentences = segment_japanese_sentences(c1)
                cur_passage_id = _upsert_passage(
                    conn,
                    title=cur_title or c1.splitlines()[0],
                    genre=cur_genre,
                    section="reading",
                    japanese_text=c1,
                    vietnamese_text=vi_text,
                    evidence_sentences=cur_sentences,
                    condition_matrix=[],
                )

    return raw_count, imported_count, question_ids


def _parse_layout_grammar_cloze(wb: openpyxl.Workbook, conn: sqlite3.Connection, workbook_id: int) -> Tuple[int, int, List[int]]:
    ws = wb["Bai_Doc_Va_Luyen_Tap"]
    ws_nb = wb["So_Tay_Ngu_Phap_Dokkai"] if "So_Tay_Ngu_Phap_Dokkai" in wb.sheetnames else None
    ws_stat = wb["Thong_Ke_Tien_Do"] if "Thong_Ke_Tien_Do" in wb.sheetnames else None

    nb_map: Dict[str, Dict[str, str]] = {}
    if ws_nb is not None:
        for r in range(2, ws_nb.max_row + 1):
            src = str(ws_nb.cell(r, 2).value or "").strip()
            if not src or src in ("Nguồn bài", "Nguồn câu"):
                continue
            nb_map[src] = {
                "source_ref": src,
                "pattern": str(ws_nb.cell(r, 3).value or "").strip(),
                "structure": str(ws_nb.cell(r, 4).value or "").strip(),
                "meaning_vi": str(ws_nb.cell(r, 5).value or "").strip(),
                "distinction": str(ws_nb.cell(r, 6).value or "").strip(),
                "example": str(ws_nb.cell(r, 7).value or "").strip(),
            }

    stat_tips: Dict[str, Dict[str, str]] = {}
    if ws_stat is not None:
        for r in range(2, ws_stat.max_row + 1):
            pkg = str(ws_stat.cell(r, 1).value or "").strip()
            if pkg and not pkg.startswith(("TỔNG", "BẢNG", "Số liệu", "Gói bài đọc")):
                stat_tips[pkg] = {
                    "focus": str(ws_stat.cell(r, 8).value or "").strip(),
                    "tactics": str(ws_stat.cell(r, 9).value or "").strip(),
                }

    raw_count = 0
    imported_count = 0
    question_ids: List[int] = []
    cur_title = ""
    pending_title = ""
    cur_passage_id: Optional[int] = None
    cur_b_num = 1

    for r in range(1, ws.max_row + 1):
        c1 = str(ws.cell(r, 1).value or "").strip()
        ans_idx = _parse_int_answer(ws.cell(r, 10).value)
        raw_opts = [ws.cell(r, c).value for c in range(4, 8)]

        if ans_idx is not None and all(o is not None for o in raw_opts) and not _is_header_options(raw_opts):
            raw_count += 1
            src_label = str(ws.cell(r, 2).value or "").strip()
            prompt_jp = str(ws.cell(r, 3).value or "").strip()
            options = [clean_option_text(o) for o in raw_opts]
            focus_kw = str(ws.cell(r, 12).value or "").strip()
            explanation_vi = str(ws.cell(r, 13).value or "").strip()

            m_c = re.search(r"[\[\【]\s*(\d+)\s*[\]\】]", src_label)
            nb_key = f"Bài {cur_b_num} - [{m_c.group(1)}]" if m_c else ""
            meta: Dict[str, Any] = {}
            if nb_key in nb_map:
                meta["grammar_notebook"] = nb_map[nb_key]
            if c1 in stat_tips:
                meta["strategy_tip"] = stat_tips[c1]

            unit_code = assign_micro_unit(
                "grammar",
                "問題3",
                focus_kw,
                prompt_jp,
                passage_title=cur_title,
                source_label=src_label,
            )
            q_id, is_new = _upsert_question(
                conn,
                workbook_id,
                {
                    "unit_code": unit_code,
                    "passage_id": cur_passage_id,
                    "section": "grammar",
                    "mondai_type": "問題3",
                    "source_label": src_label,
                    "focus_keyword": focus_kw,
                    "prompt_jp": prompt_jp,
                    "options": options,
                    "correct_index": ans_idx,
                    "translation_vi": "",
                    "explanation_vi": explanation_vi,
                    "notebook_meta": meta,
                },
            )
            question_ids.append(q_id)
            if is_new:
                imported_count += 1
        elif (c1.startswith("Gói ") or c1.startswith("Bài ")) and not _is_banner_or_header_line(c1) and ws.cell(r, 4).value is None:
            m_t = re.search(r"「([^」]+)」", c1)
            raw_t = m_t.group(1).strip() if m_t else c1
            # Normalize short canonical title for この薬の使い方 / 緑のカーテン / 日本人スポーツ選手
            if "緑のカーテン" in raw_t:
                pending_title = "緑のカーテン"
            elif "日本人スポーツ選手" in raw_t:
                pending_title = "日本人スポーツ選手"
            else:
                pending_title = raw_t
            cur_title = pending_title
            m_b = re.search(r"(?:Gói|Bài)\s*(\d+)", c1)
            cur_b_num = int(m_b.group(1)) if m_b else 1
        elif _is_passage_row(ws, r, c1):
            vi_text = str(ws.cell(r, 8).value or "").strip()
            sents = segment_japanese_sentences(c1)
            passage_title = pending_title or c1.splitlines()[0].strip("【】 ") or f"Cloze Passage {cur_b_num}"
            cur_title = passage_title
            pending_title = ""
            cur_passage_id = _upsert_passage(
                conn,
                title=passage_title,
                genre="文章の文法",
                section="grammar",
                japanese_text=c1,
                vietnamese_text=vi_text,
                evidence_sentences=sents,
                condition_matrix=[],
            )

    return raw_count, imported_count, question_ids


def _parse_layout_dokkai_short(wb: openpyxl.Workbook, conn: sqlite3.Connection, workbook_id: int) -> Tuple[int, int, List[int]]:
    ws = wb["Dokkai_Doan_Van_Ngan"]
    ws_trap = wb["Bang_Giai_Ma_Bay_Dokkai"] if "Bang_Giai_Ma_Bay_Dokkai" in wb.sheetnames else None
    ws_stat = wb["Thong_Ke_Chien_Thuat"] if "Thong_Ke_Chien_Thuat" in wb.sheetnames else None

    trap_map: Dict[str, Dict[str, str]] = {}
    if ws_trap is not None:
        for r in range(2, ws_trap.max_row + 1):
            col1 = str(ws_trap.cell(r, 1).value or "").strip()
            m = re.search(r"(\[\d+\])", col1)
            if m:
                trap_map[m.group(1)] = {
                    "question_pattern": str(ws_trap.cell(r, 2).value or "").strip(),
                    "key_evidence_sentence": str(ws_trap.cell(r, 3).value or "").strip(),
                    "paraphrase": str(ws_trap.cell(r, 4).value or "").strip(),
                    "matched_answer": str(ws_trap.cell(r, 5).value or "").strip(),
                    "classic_traps": str(ws_trap.cell(r, 6).value or "").strip(),
                }

    stat_map: Dict[str, Dict[str, str]] = {}
    if ws_stat is not None:
        for r in range(2, ws_stat.max_row + 1):
            pkg = str(ws_stat.cell(r, 1).value or "").strip()
            if pkg and not pkg.startswith(("TỔNG", "BẢNG", "Số liệu", "Gói thể loại")):
                tip_obj = {
                    "traps": str(ws_stat.cell(r, 8).value or "").strip(),
                    "tactics": str(ws_stat.cell(r, 9).value or "").strip(),
                }
                stat_map[pkg] = tip_obj
                m_goi = re.match(r"^(Gói\s*\d+)", pkg)
                if m_goi:
                    stat_map[m_goi.group(1)] = tip_obj

    raw_count = 0
    imported_count = 0
    question_ids: List[int] = []
    cur_title = ""
    pending_title = ""
    cur_passage_id: Optional[int] = None
    cur_sentences: List[str] = []

    for r in range(1, ws.max_row + 1):
        c1 = str(ws.cell(r, 1).value or "").strip()
        ans_idx = _parse_int_answer(ws.cell(r, 10).value)
        raw_opts = [ws.cell(r, c).value for c in range(4, 8)]

        if ans_idx is not None and all(o is not None for o in raw_opts) and not _is_header_options(raw_opts):
            raw_count += 1
            src_label = str(ws.cell(r, 2).value or "").strip()
            prompt_jp = str(ws.cell(r, 3).value or "").strip()
            options = [clean_option_text(o) for o in raw_opts]
            skill = str(ws.cell(r, 12).value or "").strip()
            explanation_vi = str(ws.cell(r, 13).value or "").strip()

            m_lbl = re.search(r"(\[\d+\])", src_label)
            trap_info = trap_map.get(src_label) or (trap_map.get(m_lbl.group(1), {}) if m_lbl else {})
            ev_indices = find_evidence_indices(
                cur_sentences,
                explanation_vi,
                companion_evidence=trap_info.get("key_evidence_sentence"),
            )
            meta: Dict[str, Any] = {
                "dokkai_skill": skill,
                "evidence_indices": ev_indices,
            }
            if trap_info:
                meta["trap_decoder"] = trap_info
            m_goi = re.match(r"^(Gói\s*\d+)", c1)
            if c1 in stat_map:
                meta["strategy_tip"] = stat_map[c1]
            elif m_goi and m_goi.group(1) in stat_map:
                meta["strategy_tip"] = stat_map[m_goi.group(1)]

            unit_code = assign_micro_unit("reading", "短文", skill, prompt_jp, passage_title=cur_title, source_label=src_label)
            q_id, is_new = _upsert_question(
                conn,
                workbook_id,
                {
                    "unit_code": unit_code,
                    "passage_id": cur_passage_id,
                    "section": "reading",
                    "mondai_type": "短文",
                    "source_label": src_label,
                    "focus_keyword": skill,
                    "prompt_jp": prompt_jp,
                    "options": options,
                    "correct_index": ans_idx,
                    "translation_vi": "",
                    "explanation_vi": explanation_vi,
                    "notebook_meta": meta,
                },
            )
            question_ids.append(q_id)
            if is_new:
                imported_count += 1
        elif (c1.startswith("Gói ") or c1.startswith("Bài ")) and not _is_banner_or_header_line(c1) and ws.cell(r, 4).value is None:
            pending_title = c1
            cur_title = c1
        elif _is_passage_row(ws, r, c1):
            vi_text = str(ws.cell(r, 8).value or "").strip()
            cur_sentences = segment_japanese_sentences(c1)
            passage_title = pending_title or c1.splitlines()[0]
            cur_title = passage_title
            pending_title = ""
            cur_passage_id = _upsert_passage(
                conn,
                title=passage_title,
                genre="短文",
                section="reading",
                japanese_text=c1,
                vietnamese_text=vi_text,
                evidence_sentences=cur_sentences,
                condition_matrix=[],
            )

    return raw_count, imported_count, question_ids


def _parse_layout_dokkai_info(wb: openpyxl.Workbook, conn: sqlite3.Connection, workbook_id: int) -> Tuple[int, int, List[int]]:
    ws = wb["Tim_Kiem_Thong_Tin_Dokkai"]
    ws_mx = wb["Ma_Tran_Doi_Chieu_Dieu_Kien"] if "Ma_Tran_Doi_Chieu_Dieu_Kien" in wb.sheetnames else None
    ws_stat = wb["Thong_Ke_Chien_Thuat"] if "Thong_Ke_Chien_Thuat" in wb.sheetnames else None

    matrix_map: Dict[str, Dict[str, str]] = {}
    if ws_mx is not None:
        for r in range(2, ws_mx.max_row + 1):
            col1 = str(ws_mx.cell(r, 1).value or "").strip()
            m = re.search(r"(\[\d+\])", col1)
            if m:
                matrix_map[m.group(1)] = {
                    "character": str(ws_mx.cell(r, 2).value or "").strip(),
                    "condition_1": str(ws_mx.cell(r, 3).value or "").strip(),
                    "condition_2": str(ws_mx.cell(r, 4).value or "").strip(),
                    "hidden_condition": str(ws_mx.cell(r, 5).value or "").strip(),
                    "matched_answer": str(ws_mx.cell(r, 6).value or "").strip(),
                    "typical_trap": str(ws_mx.cell(r, 7).value or "").strip(),
                }

    stat_map: Dict[str, Dict[str, str]] = {}
    if ws_stat is not None:
        for r in range(2, ws_stat.max_row + 1):
            pkg = str(ws_stat.cell(r, 1).value or "").strip()
            if pkg and not pkg.startswith(("TỔNG", "BẢNG", "Số liệu", "Gói bài đọc")):
                tip_obj = {
                    "traps": str(ws_stat.cell(r, 8).value or "").strip(),
                    "tactics": str(ws_stat.cell(r, 9).value or "").strip(),
                }
                stat_map[pkg] = tip_obj
                m_goi = re.match(r"^(Gói\s*\d+)", pkg)
                if m_goi:
                    stat_map[m_goi.group(1)] = tip_obj

    raw_count = 0
    imported_count = 0
    question_ids: List[int] = []
    cur_title = ""
    pending_title = ""
    cur_passage_id: Optional[int] = None
    cur_sentences: List[str] = []

    for r in range(1, ws.max_row + 1):
        c1 = str(ws.cell(r, 1).value or "").strip()
        ans_idx = _parse_int_answer(ws.cell(r, 10).value)
        raw_opts = [ws.cell(r, c).value for c in range(4, 8)]

        if ans_idx is not None and all(o is not None for o in raw_opts) and not _is_header_options(raw_opts):
            raw_count += 1
            src_label = str(ws.cell(r, 2).value or "").strip()
            prompt_jp = str(ws.cell(r, 3).value or "").strip()
            options = [clean_option_text(o) for o in raw_opts]
            skill = str(ws.cell(r, 12).value or "").strip()
            explanation_vi = str(ws.cell(r, 13).value or "").strip()

            m_lbl = re.search(r"(\[\d+\])", src_label)
            cond_info = matrix_map.get(src_label) or (matrix_map.get(m_lbl.group(1), {}) if m_lbl else {})
            ev_indices = find_evidence_indices(
                cur_sentences,
                explanation_vi,
                condition_info=cond_info,
            )
            if cur_passage_id is not None and cond_info:
                p_row = conn.execute(
                    "SELECT condition_matrix_json FROM PASSAGES WHERE id=?", (cur_passage_id,)
                ).fetchone()
                cur_mx = json.loads(p_row["condition_matrix_json"] or "[]") if p_row else []
                cur_mx.append({"source_label": src_label, **cond_info})
                conn.execute(
                    "UPDATE PASSAGES SET condition_matrix_json=? WHERE id=?",
                    (json.dumps(cur_mx, ensure_ascii=False), cur_passage_id),
                )

            meta: Dict[str, Any] = {
                "dokkai_skill": skill,
                "evidence_indices": ev_indices,
            }
            if cond_info:
                meta["condition_matrix"] = cond_info
            m_goi = re.match(r"^(Gói\s*\d+)", c1)
            if c1 in stat_map:
                meta["strategy_tip"] = stat_map[c1]
            elif m_goi and m_goi.group(1) in stat_map:
                meta["strategy_tip"] = stat_map[m_goi.group(1)]

            unit_code = assign_micro_unit("reading", "情報検索", skill, prompt_jp, passage_title=cur_title, source_label=src_label)
            q_id, is_new = _upsert_question(
                conn,
                workbook_id,
                {
                    "unit_code": unit_code,
                    "passage_id": cur_passage_id,
                    "section": "reading",
                    "mondai_type": "情報検索",
                    "source_label": src_label,
                    "focus_keyword": skill,
                    "prompt_jp": prompt_jp,
                    "options": options,
                    "correct_index": ans_idx,
                    "translation_vi": "",
                    "explanation_vi": explanation_vi,
                    "notebook_meta": meta,
                },
            )
            question_ids.append(q_id)
            if is_new:
                imported_count += 1
        elif (c1.startswith("Gói ") or c1.startswith("Bài ")) and not _is_banner_or_header_line(c1) and ws.cell(r, 4).value is None:
            pending_title = c1
            cur_title = c1
        elif _is_passage_row(ws, r, c1):
            vi_text = str(ws.cell(r, 8).value or "").strip()
            cur_sentences = segment_japanese_sentences(c1)
            passage_title = pending_title or c1.splitlines()[0]
            cur_title = passage_title
            pending_title = ""
            cur_passage_id = _upsert_passage(
                conn,
                title=passage_title,
                genre="情報検索",
                section="reading",
                japanese_text=c1,
                vietnamese_text=vi_text,
                evidence_sentences=cur_sentences,
                condition_matrix=[],
            )

    return raw_count, imported_count, question_ids


LAYOUT_PARSERS: Dict[str, Callable[[openpyxl.Workbook, sqlite3.Connection, int], Tuple[int, int, List[int]]]] = {
    "vocab_35": _parse_layout_vocab_35,
    "comprehensive_3_part": _parse_layout_comprehensive,
    "grammar_cloze_3_passages": _parse_layout_grammar_cloze,
    "dokkai_short": _parse_layout_dokkai_short,
    "dokkai_info": _parse_layout_dokkai_info,
}


def import_excel_file(
    file_path: Path,
    db_path: Optional[Path] = None,
    generate_variants: bool = True,
) -> Dict[str, Any]:
    """Import a single .xlsx workbook idempotently and optionally auto-generate variants."""
    resolved = Path(file_path)
    if not resolved.exists():
        raise FileNotFoundError(f"Không tìm thấy tệp Excel: {resolved}")

    init_db(db_path)
    f_hash = compute_file_hash(resolved)
    wb = openpyxl.load_workbook(str(resolved), data_only=True)
    layout_type = detect_layout(wb)

    with transaction(db_path) as conn:
        seed_micro_units_and_bridges(conn)
        existing_wb = conn.execute(
            "SELECT id, raw_count, imported_count FROM SOURCE_WORKBOOKS WHERE file_hash=?",
            (f_hash,),
        ).fetchone()
        if existing_wb:
            return {
                "filename": resolved.name,
                "layout_type": layout_type,
                "raw_count": int(existing_wb["raw_count"]),
                "imported_count": int(existing_wb["imported_count"]),
                "newly_imported_count": 0,
                "deduplicated_skipped": int(existing_wb["raw_count"]) - int(existing_wb["imported_count"]),
                "already_imported": True,
                "variants_generated": 0,
            }

        cur = conn.execute(
            "INSERT INTO SOURCE_WORKBOOKS (filename, file_hash, layout_type) VALUES (?, ?, ?)",
            (resolved.name, f_hash, layout_type),
        )
        workbook_id = int(cur.lastrowid)

        parser = LAYOUT_PARSERS[layout_type]
        raw_count, imported_count, touched_qids = parser(wb, conn, workbook_id)
        if raw_count == 0:
            raise ValueError(
                f"Tệp Excel '{resolved.name}' khớp layout '{layout_type}' nhưng không có câu hỏi hợp lệ nào (cần 4 phương án và đáp án đúng 1–4)."
            )
        conn.execute(
            "UPDATE SOURCE_WORKBOOKS SET raw_count=?, imported_count=? WHERE id=?",
            (raw_count, imported_count, workbook_id),
        )

        variants_generated = 0
        if generate_variants:
            from n3_mastery.variant_generator import ensure_variants_for_questions

            variants_generated = ensure_variants_for_questions(conn, touched_qids)

    return {
        "filename": resolved.name,
        "layout_type": layout_type,
        "raw_count": raw_count,
        "imported_count": imported_count,
        "newly_imported_count": imported_count,
        "deduplicated_skipped": raw_count - imported_count,
        "already_imported": False,
        "variants_generated": variants_generated,
    }


def import_all_excel(
    excel_dir: Optional[Path] = None,
    db_path: Optional[Path] = None,
    generate_variants: bool = True,
) -> Dict[str, Any]:
    """Import all .xlsx workbooks in directory, returning aggregate statistics."""
    target_dir = Path(excel_dir) if excel_dir is not None else get_excel_dir()
    if not target_dir.exists():
        raise FileNotFoundError(f"Thư mục chứa tệp Excel không tồn tại: {target_dir}")

    init_db(db_path)
    files = sorted(target_dir.glob("*.xlsx"))
    reports = []
    total_raw = 0
    total_imported = 0
    total_variants = 0
    for f in files:
        res = import_excel_file(f, db_path=db_path, generate_variants=False)
        reports.append(res)
        total_raw += res["raw_count"]
        total_imported += res["newly_imported_count"]

    if generate_variants:
        from n3_mastery.variant_generator import ensure_variants_for_all

        total_variants = ensure_variants_for_all(db_path=db_path)

    with transaction(db_path) as conn:
        unique_questions = conn.execute("SELECT COUNT(*) FROM QUESTIONS").fetchone()[0]
        dokkai_passages = conn.execute("SELECT COUNT(*) FROM PASSAGES WHERE section='reading'").fetchone()[0]
        cloze_passages = conn.execute("SELECT COUNT(*) FROM PASSAGES WHERE section='grammar'").fetchone()[0]
        total_variants_db = conn.execute("SELECT COUNT(*) FROM VARIANT_DRILLS").fetchone()[0]

    return {
        "files_processed": len(files),
        "total_raw_rows": total_raw,
        "total_newly_imported": total_imported,
        "unique_questions": int(unique_questions),
        "dokkai_passages": int(dokkai_passages),
        "cloze_passages": int(cloze_passages),
        "variants_generated": total_variants,
        "total_variants_in_db": int(total_variants_db),
        "workbooks": reports,
    }
