"""Sectional readiness calculator and score projection engine."""

from datetime import datetime, timezone
from typing import Dict, List, Optional, Any

from jlpt_study_system.config import (
    PASS_TOTAL_THRESHOLD,
    MAX_TOTAL_SCORE,
    SECTION_CUTOFF,
    SECTION_MAX_SCORE,
)
from jlpt_study_system.database import get_db
from jlpt_study_system.models import (
    SectionName,
    SectionReadiness,
    ReadinessReport,
)


def calculate_sectional_readiness(db_path=None) -> ReadinessReport:
    """Calculate projected scores for Language Knowledge, Reading, and Listening.

    Evaluates real performance against JLPT N3 passing thresholds:
    - Language Knowledge: >= 19/60 cutoff
    - Reading: >= 19/60 cutoff
    - Listening: >= 19/60 cutoff
    - Total: >= 95/180 passing threshold
    """
    now = datetime.now(timezone.utc)

    with get_db(db_path) as conn:
        # 1. Cards and FSRS retention
        total_cards = conn.execute("SELECT COUNT(*) AS c FROM cards").fetchone()["c"]
        reviewed_cards = conn.execute(
            "SELECT COUNT(*) AS c FROM fsrs_states WHERE reps > 0"
        ).fetchone()["c"]

        # Reviews accuracy
        review_acc_row = conn.execute(
            """
            SELECT
                COUNT(*) AS total,
                SUM(CASE WHEN rating >= 3 THEN 1 ELSE 0 END) AS good_easy
            FROM review_logs
            """
        ).fetchone()
        total_reviews = review_acc_row["total"] or 0
        good_reviews = review_acc_row["good_easy"] or 0
        review_acc = (good_reviews / total_reviews) if total_reviews > 0 else 0.0

        # Grammar & Vocab specific coverage
        grammar_reviewed = conn.execute(
            """
            SELECT COUNT(*) AS c FROM cards c
            JOIN fsrs_states f ON c.id = f.card_id
            WHERE c.category = 'grammar' AND f.reps > 0
            """
        ).fetchone()["c"]
        vocab_reviewed = conn.execute(
            """
            SELECT COUNT(*) AS c FROM cards c
            JOIN fsrs_states f ON c.id = f.card_id
            WHERE c.category = 'vocab' AND f.reps > 0
            """
        ).fetchone()["c"]

        # Average stability
        avg_stability_row = conn.execute(
            "SELECT AVG(stability) AS s FROM fsrs_states WHERE reps > 0"
        ).fetchone()
        avg_stability = avg_stability_row["s"] or 0.0

        # 2. Dokkai reading drill metrics
        dokkai_row = conn.execute(
            """
            SELECT
                COUNT(*) AS total,
                SUM(h.is_correct) AS correct
            FROM drill_history h
            JOIN drill_items d ON h.drill_item_id = d.id
            WHERE d.drill_type = 'dokkai_decoder'
            """
        ).fetchone()
        dokkai_total = dokkai_row["total"] or 0
        dokkai_correct = dokkai_row["correct"] or 0
        dokkai_acc = (dokkai_correct / dokkai_total) if dokkai_total > 0 else 0.0

        # 3. Choukai listening drill metrics
        choukai_row = conn.execute(
            """
            SELECT
                COUNT(*) AS total,
                SUM(h.is_correct) AS correct,
                AVG(h.response_time_sec) AS avg_speed
            FROM drill_history h
            JOIN drill_items d ON h.drill_item_id = d.id
            WHERE d.drill_type = 'choukai_reflex'
            """
        ).fetchone()
        choukai_total = choukai_row["total"] or 0
        choukai_correct = choukai_row["correct"] or 0
        choukai_speed = choukai_row["avg_speed"] or 0.0
        choukai_acc = (choukai_correct / choukai_total) if choukai_total > 0 else 0.0

    # Section 1: Language Knowledge (Gengo Chishiki)
    # Baseline from N5: 14.0 points. Max sprint bonus: 46.0 points.
    gengo_coverage = (grammar_reviewed + vocab_reviewed) / max(1, total_cards)
    cov_weight = min(1.0, (grammar_reviewed + vocab_reviewed) / max(1, total_cards * 0.4))
    stability_factor = min(1.0, (avg_stability or 0.0) / 4.0)
    gengo_performance = (0.70 * review_acc) + (0.30 * stability_factor) if total_reviews > 0 else 0.0
    gengo_score = round(min(60.0, max(12.0, 14.0 + (46.0 * cov_weight * gengo_performance))), 1)

    # Section 2: Reading (Dokkai)
    # Baseline from N5: 13.0 points. Max sprint bonus: 47.0 points.
    vocab_ratio = min(1.0, vocab_reviewed / 30.0)
    dokkai_vol = min(1.0, dokkai_total / 8.0)
    reading_factor = (0.35 * vocab_ratio) + (0.65 * dokkai_acc * dokkai_vol)
    reading_score = round(min(60.0, max(12.0, 13.0 + (47.0 * reading_factor))), 1)

    # Section 3: Listening (Choukai)
    # Baseline from N5: 14.0 points. Max sprint bonus: 46.0 points.
    if choukai_total > 0:
        choukai_vol = min(1.0, choukai_total / 12.0)
        speed_penalty = max(0.0, (choukai_speed - 2.5) * 0.08)
        choukai_perf = max(0.0, choukai_acc - speed_penalty)
        choukai_factor = choukai_perf * choukai_vol
    else:
        choukai_factor = 0.0
    listening_score = round(min(60.0, max(12.0, 14.0 + (46.0 * choukai_factor))), 1)

    total_score = round(gengo_score + reading_score + listening_score, 1)

    # Cutoff validations
    gengo_pass = (gengo_score >= SECTION_CUTOFF)
    reading_pass = (reading_score >= SECTION_CUTOFF)
    listening_pass = (listening_score >= SECTION_CUTOFF)
    total_pass = (total_score >= PASS_TOTAL_THRESHOLD)

    at_risk: List[str] = []
    if not gengo_pass:
        at_risk.append("Language Knowledge (DƯỚI SÀN LIỆT 19 ĐIỂM)")
    elif gengo_score < 23.0:
        at_risk.append("Language Knowledge (Sát ranh giới sàn liệt)")

    if not reading_pass:
        at_risk.append("Reading Dokkai (DƯỚI SÀN LIỆT 19 ĐIỂM)")
    elif reading_score < 23.0:
        at_risk.append("Reading Dokkai (Sát ranh giới sàn liệt)")

    if not listening_pass:
        at_risk.append("Listening Choukai (DƯỚI SÀN LIỆT 19 ĐIỂM)")
    elif listening_score < 23.0:
        at_risk.append("Listening Choukai (Sát ranh giới sàn liệt)")

    if total_pass and not at_risk:
        pass_status = "PASS"
    elif not gengo_pass or not reading_pass or not listening_pass or total_score < 85.0:
        pass_status = "FAIL"
    else:
        pass_status = "AT_RISK"

    # Actionable sprint recommendations
    recommendations = []
    if not gengo_pass:
        recommendations.append(
            "[BÁO ĐỘNG ĐỎ] Điểm Kiến thức ngôn ngữ ước tính chỉ đạt "
            f"{gengo_score}/60 (< sàn liệt 19). Hoàn thành khẩn cấp 150 lượt thẻ Ngữ pháp Tier 1."
        )
    if not reading_pass:
        recommendations.append(
            "[BÁO ĐỘNG ĐỎ] Điểm Đọc hiểu ước tính chỉ đạt "
            f"{reading_score}/60 (< sàn liệt 19). Luyện thuật toán quét từ nối 'しかし/つまり' và làm bài Tìm kiếm thông tin."
        )
    if not listening_pass:
        recommendations.append(
            "[BÁO ĐỘNG ĐỎ] Điểm Nghe hiểu ước tính chỉ đạt "
            f"{listening_score}/60 (< sàn liệt 19). Luyện ngay 25 mẫu phản xạ Mondai 5 để bảo vệ mốc an toàn 30 điểm."
        )
    if total_score < PASS_TOTAL_THRESHOLD and not recommendations:
        gap = round(PASS_TOTAL_THRESHOLD - total_score, 1)
        recommendations.append(
            f"[MỤC TIÊU TỔNG ĐIỂM] Tổng điểm ước tính {total_score}/180, còn thiếu {gap} điểm để đạt ngưỡng đỗ (95). Tăng tốc độ duyệt thẻ và cày Pomodoro."
        )
    if not recommendations:
        recommendations.append(
            f"[SẴN SÀNG VƯỢT NGƯỠNG] Điểm ước tính {total_score}/180 đã vượt ngưỡng đỗ an toàn (95/180) và cả 3 phân môn đều vượt xa sàn liệt. Duy trì phong độ phòng thi!"
        )

    gengo_readiness = SectionReadiness(
        section_name=SectionName.GENGO,
        score=gengo_score,
        max_score=60.0,
        cutoff=19.0,
        pass_cutoff=gengo_pass,
        mastery_ratio=round(gengo_coverage, 2),
        retention_rate=round(review_acc * 100, 1),
        sample_count=total_reviews,
        status_label="VƯỢT SÀN" if gengo_pass else "NGUY CƠ LIỆT",
    )

    reading_readiness = SectionReadiness(
        section_name=SectionName.READING,
        score=reading_score,
        max_score=60.0,
        cutoff=19.0,
        pass_cutoff=reading_pass,
        mastery_ratio=round(vocab_ratio, 2),
        retention_rate=round(dokkai_acc * 100, 1),
        sample_count=dokkai_total,
        status_label="VƯỢT SÀN" if reading_pass else "NGUY CƠ LIỆT",
    )

    listening_readiness = SectionReadiness(
        section_name=SectionName.LISTENING,
        score=listening_score,
        max_score=60.0,
        cutoff=19.0,
        pass_cutoff=listening_pass,
        mastery_ratio=round(choukai_acc, 2),
        retention_rate=round(choukai_acc * 100, 1),
        sample_count=choukai_total,
        status_label="VƯỢT SÀN" if listening_pass else "NGUY CƠ LIỆT",
    )

    return ReadinessReport(
        total_score=total_score,
        max_total_score=180.0,
        pass_total=total_pass,
        gengo=gengo_readiness,
        reading=reading_readiness,
        listening=listening_readiness,
        at_risk_sections=at_risk,
        pass_status=pass_status,
        critical_recommendations=recommendations,
        generated_at=now,
    )
