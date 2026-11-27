"""Dual 10-Point Calibration (Original Bank Score vs True Anti-Rote Mastery Score) & Mastery Gate."""

from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from n3_mastery.config import (
    MASTERY_PARTIAL_CREDIT_CLEAN,
    MASTERY_PARTIAL_CREDIT_HINTED,
    MASTERY_REQUIRED_SPACED_REPS,
    SECTION_WEIGHTS_JLPT,
    TOTAL_SCORE_10,
)
from n3_mastery.database import get_connection
from n3_mastery.fsrs_adaptive import compute_retrievability, get_pace_settings, parse_iso, utc_now
from n3_mastery.models import DualReadinessReport, ScoringMode, SectionReadiness

SECTION_LABELS = {
    "vocab": "Từ vựng & Kanji (文字・語彙)",
    "grammar": "Ngữ pháp (文法)",
    "reading": "Đọc hiểu (読解)",
}


def is_question_mastered(row: Dict[str, Any]) -> bool:
    """True iff question satisfies all 3 Mastery Gate conditions with 0 recent lapses."""
    return (
        int(row["clean_original_passed"]) == 1
        and int(row["variant_passed"]) >= 1
        and int(row["spaced_clean_sessions"]) >= MASTERY_REQUIRED_SPACED_REPS
        and str(row["state"]) != "relearning"
        and int(row["latest_overall_correct"] or 0) == 1
    )


def calculate_dual_readiness(
    scoring_mode: Optional[ScoringMode] = None,
    now: Optional[datetime] = None,
    db_path: Optional[Path] = None,
) -> DualReadinessReport:
    """Calculate honest Dual /10 scores adhering strictly to Zero-Sycophancy."""
    ts_now = now or utc_now()
    mode = scoring_mode or get_pace_settings(db_path=db_path).scoring_mode

    conn = get_connection(db_path)
    try:
        rows = conn.execute(
            """
            SELECT q.id, q.section, q.unit_code,
                   f.stability, f.reps, f.lapses, f.state,
                   f.clean_original_passed, f.variant_passed,
                   f.spaced_clean_sessions, f.last_review,
                   (SELECT a.is_correct FROM ATTEMPT_LOGS a
                    WHERE a.question_id = q.id AND a.variant_id IS NULL
                    ORDER BY a.id DESC LIMIT 1) AS latest_orig_correct,
                   (SELECT a.used_hint FROM ATTEMPT_LOGS a
                    WHERE a.question_id = q.id AND a.variant_id IS NULL
                    ORDER BY a.id DESC LIMIT 1) AS latest_orig_hint,
                   (SELECT a.is_correct FROM ATTEMPT_LOGS a
                    WHERE a.question_id = q.id
                    ORDER BY a.id DESC LIMIT 1) AS latest_overall_correct
            FROM QUESTIONS q
            JOIN FSRS_STATES f ON f.question_id = q.id
            ORDER BY q.id
            """
        ).fetchall()
    finally:
        conn.close()

    total_q = len(rows)
    if total_q == 0:
        return DualReadinessReport(
            scoring_mode=mode,
            original_score_10=0.0,
            mastery_score_10=0.0,
            rote_gap_10=0.0,
            total_questions=0,
            attempted_count=0,
            mastered_count=0,
            mastered_percent=0.0,
            sections=[],
            honest_verdict="0.00/10.00 — Chưa có dữ liệu câu hỏi hoặc chưa thực hiện lượt học nào.",
        )

    grouped: Dict[str, List[Dict[str, Any]]] = {"vocab": [], "grammar": [], "reading": []}
    for r in rows:
        sec = str(r["section"])
        if sec in grouped:
            grouped[sec].append(dict(r))

    # Determine section weights summing to 10.0
    if mode == ScoringMode.EQUAL_WEIGHTED:
        weights = {sec: TOTAL_SCORE_10 * len(items) / total_q for sec, items in grouped.items()}
    else:
        active_secs = [s for s, items in grouped.items() if len(items) > 0]
        raw_w_sum = sum(SECTION_WEIGHTS_JLPT[s] for s in active_secs) or 1.0
        weights = {
            s: (TOTAL_SCORE_10 * SECTION_WEIGHTS_JLPT[s] / raw_w_sum) if len(grouped[s]) > 0 else 0.0
            for s in ("vocab", "grammar", "reading")
        }

    section_reports: List[SectionReadiness] = []
    total_orig_10 = 0.0
    total_mastery_10 = 0.0
    total_attempted = 0
    total_mastered = 0

    for sec in ("vocab", "grammar", "reading"):
        items = grouped[sec]
        n = len(items)
        w = weights[sec]
        if n == 0:
            section_reports.append(
                SectionReadiness(
                    section=sec,
                    label_vi=SECTION_LABELS[sec],
                    weight_10=0.0,
                    total_questions=0,
                    attempted_original=0,
                    correct_original=0,
                    variant_passed_count=0,
                    mastered_count=0,
                    original_score_10=0.0,
                    mastery_score_10=0.0,
                )
            )
            continue

        orig_sum = 0.0
        mastery_sum = 0.0
        attempted_sec = 0
        correct_orig_sec = 0
        variant_sec = 0
        mastered_sec = 0

        for row in items:
            has_any_attempt = row["latest_overall_correct"] is not None
            if has_any_attempt:
                attempted_sec += 1

            last_rev = parse_iso(row["last_review"])
            elapsed_days = 0.0
            if last_rev is not None:
                elapsed_days = max(0.0, (ts_now - last_rev).total_seconds() / 86400.0)
            retrievability = compute_retrievability(float(row["stability"]), elapsed_days) if has_any_attempt else 0.0

            orig_ok = int(row["latest_orig_correct"] or 0) == 1
            if orig_ok:
                correct_orig_sec += 1
                orig_sum += retrievability

            if int(row["variant_passed"]) >= 1:
                variant_sec += 1

            if is_question_mastered(row):
                mastered_sec += 1
                mastery_sum += 1.0 * retrievability
            elif str(row["state"]) != "relearning" and (
                int(row["clean_original_passed"]) == 1 or int(row["variant_passed"]) >= 1
            ):
                mastery_sum += MASTERY_PARTIAL_CREDIT_CLEAN * retrievability
            elif str(row["state"]) != "relearning" and orig_ok and int(row["latest_orig_hint"] or 0) == 1:
                mastery_sum += MASTERY_PARTIAL_CREDIT_HINTED * retrievability

        sec_orig_10 = round(w * (orig_sum / n), 2)
        sec_mast_10 = round(w * (mastery_sum / n), 2)
        total_orig_10 += sec_orig_10
        total_mastery_10 += sec_mast_10
        total_attempted += attempted_sec
        total_mastered += mastered_sec

        section_reports.append(
            SectionReadiness(
                section=sec,
                label_vi=SECTION_LABELS[sec],
                weight_10=round(w, 2),
                total_questions=n,
                attempted_original=attempted_sec,
                correct_original=correct_orig_sec,
                variant_passed_count=variant_sec,
                mastered_count=mastered_sec,
                original_score_10=sec_orig_10,
                mastery_score_10=sec_mast_10,
            )
        )

    total_orig_10 = round(min(10.0, total_orig_10), 2)
    total_mastery_10 = round(min(10.0, total_mastery_10), 2)
    rote_gap = round(max(0.0, total_orig_10 - total_mastery_10), 2)
    mastered_pct = round((total_mastered / total_q) * 100.0, 1)

    if total_attempted == 0:
        verdict = "0.00/10.00 — Chưa làm bài nào. Bắt đầu từ Trạm Bắc cầu N4 (MU-01) để xây điểm thật."
    elif rote_gap >= 2.0:
        verdict = (
            f"[WARN] Cảnh báo học vẹt: Đề gốc đạt {total_orig_10:.2f}/10 nhưng Chống Biến Thể chỉ đạt "
            f"{total_mastery_10:.2f}/10 (chênh lệch {rote_gap:.2f} điểm). Cần vượt biến thể & ôn cách quãng >= 2 phiên."
        )
    elif total_mastered == total_q:
        verdict = (
            f"[MASTERED 10/10] Đạt chuẩn làm chủ toàn diện {total_q}/{total_q} câu qua biến thể chống học vẹt "
            f"và >= 2 phiên cách quãng."
        )
    else:
        verdict = (
            f"Tiến độ thực chất: {total_mastered}/{total_q} câu đạt [MASTERED 10/10] ({mastered_pct}%). "
            f"Tiếp tục giữ chuỗi 0 lỗi qua 2 phiên cách quãng."
        )

    return DualReadinessReport(
        scoring_mode=mode,
        original_score_10=total_orig_10,
        mastery_score_10=total_mastery_10,
        rote_gap_10=rote_gap,
        total_questions=total_q,
        attempted_count=total_attempted,
        mastered_count=total_mastered,
        mastered_percent=mastered_pct,
        sections=section_reports,
        honest_verdict=verdict,
    )
