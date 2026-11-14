"""Adaptive Pace FSRS scheduler with Horizon Scaling and Zero-Sycophancy capacity checks."""

import math
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from n3_mastery.config import (
    DEFAULT_DAILY_MINUTES,
    DEFAULT_DAYS_REMAINING,
    DEFAULT_SCORING_MODE,
    INITIAL_STABILITY_DAYS,
    MAX_DIFFICULTY,
    MIN_DIFFICULTY,
    MIN_SPACED_SESSION_HOURS,
    WORKLOAD_BRIDGE_MIN,
    WORKLOAD_ORIGINAL_MIN,
    WORKLOAD_REMEDIATION_MIN,
    WORKLOAD_VARIANT_MIN,
)
from n3_mastery.database import get_connection, transaction
from n3_mastery.models import PaceFeasibility, PaceSettings, Rating, ScoringMode
from n3_mastery.scaffolding import determine_scaffold_tier


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def parse_iso(ts: Optional[str]) -> Optional[datetime]:
    if not ts:
        return None
    dt = datetime.fromisoformat(ts)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def format_iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).isoformat()


def get_pace_settings(db_path: Optional[Path] = None) -> PaceSettings:
    conn = get_connection(db_path)
    try:
        rows = conn.execute("SELECT key, value FROM USER_SETTINGS").fetchall()
        kv = {r["key"]: r["value"] for r in rows}
        return PaceSettings(
            days_remaining=int(kv.get("days_remaining", DEFAULT_DAYS_REMAINING)),
            daily_minutes=int(kv.get("daily_minutes", DEFAULT_DAILY_MINUTES)),
            scoring_mode=ScoringMode(kv.get("scoring_mode", DEFAULT_SCORING_MODE)),
        )
    finally:
        conn.close()


def update_pace_settings(
    days_remaining: Optional[int] = None,
    daily_minutes: Optional[int] = None,
    scoring_mode: Optional[str] = None,
    db_path: Optional[Path] = None,
) -> PaceSettings:
    current = get_pace_settings(db_path=db_path)
    new_settings = PaceSettings(
        days_remaining=days_remaining if days_remaining is not None else current.days_remaining,
        daily_minutes=daily_minutes if daily_minutes is not None else current.daily_minutes,
        scoring_mode=ScoringMode(scoring_mode) if scoring_mode is not None else current.scoring_mode,
    )
    with transaction(db_path) as conn:
        for k, v in (
            ("days_remaining", str(new_settings.days_remaining)),
            ("daily_minutes", str(new_settings.daily_minutes)),
            ("scoring_mode", new_settings.scoring_mode.value),
        ):
            conn.execute(
                """
                INSERT INTO USER_SETTINGS (key, value) VALUES (?, ?)
                ON CONFLICT(key) DO UPDATE SET value=excluded.value
                """,
                (k, v),
            )
    return new_settings


def compute_retrievability(stability: float, elapsed_days: float) -> float:
    """Compute FSRS memory retrievability R(t) = exp(ln(0.9) * t / S)."""
    if stability <= 0:
        return 0.0
    if elapsed_days <= 0:
        return 1.0
    return float(math.exp((math.log(0.9) * elapsed_days) / max(0.1, stability)))


def compute_horizon_interval(raw_interval_days: float, days_remaining: int) -> float:
    """Compress FSRS interval to fit inside remaining exam horizon so weak cards return >= 2 times."""
    horizon_cap = max(0.25, 0.45 * max(1, days_remaining))
    return round(min(raw_interval_days, horizon_cap), 4)


def compute_pace_feasibility(
    days_remaining: Optional[int] = None,
    daily_minutes: Optional[int] = None,
    db_path: Optional[Path] = None,
) -> PaceFeasibility:
    """Zero-Sycophancy capacity check comparing remaining workload against user's time budget."""
    settings = get_pace_settings(db_path=db_path)
    d_rem = max(1, days_remaining if days_remaining is not None else settings.days_remaining)
    d_min = max(5, daily_minutes if daily_minutes is not None else settings.daily_minutes)

    conn = get_connection(db_path)
    try:
        bridges_left = conn.execute(
            "SELECT COUNT(*) FROM N4_BRIDGE_CAPSULES WHERE completed=0"
        ).fetchone()[0]
        orig_left = conn.execute(
            "SELECT COUNT(*) FROM FSRS_STATES WHERE clean_original_passed=0"
        ).fetchone()[0]
        variant_left = conn.execute(
            "SELECT COUNT(*) FROM FSRS_STATES WHERE variant_passed=0 OR spaced_clean_sessions < 2"
        ).fetchone()[0]
        remed_left = conn.execute(
            "SELECT COUNT(*) FROM FSRS_STATES WHERE state='relearning'"
        ).fetchone()[0]
    finally:
        conn.close()

    remaining_workload = (
        bridges_left * WORKLOAD_BRIDGE_MIN
        + orig_left * WORKLOAD_ORIGINAL_MIN
        + variant_left * WORKLOAD_VARIANT_MIN
        + remed_left * WORKLOAD_REMEDIATION_MIN
    )
    available_budget = float(d_rem * d_min)
    required_per_day = remaining_workload / float(d_rem)
    is_feasible = d_min >= required_per_day
    shortfall = max(0.0, required_per_day - d_min)
    horizon_cap = max(0.25, 0.45 * d_rem)

    warning_msg: Optional[str] = None
    if not is_feasible:
        status_tag = "[WARN] CẦN THÊM THỜI GIAN"
        warning_msg = (
            f"[WARN] Quỹ thời gian hiện hơi ít: với {d_rem} ngày còn lại, bạn cần khoảng "
            f"{math.ceil(required_per_day)} phút/ngày để ôn kỹ toàn bộ bài (hiện đặt {d_min} phút/ngày, "
            f"thiếu khoảng {math.ceil(shortfall)} phút/ngày). Hãy tăng thêm phút học mỗi ngày hoặc tăng số ngày ôn."
        )
    else:
        status_tag = "[OK] LỊCH HỌC VỪA SỨC"

    return PaceFeasibility(
        days_remaining=d_rem,
        daily_minutes=d_min,
        available_budget_minutes=round(available_budget, 1),
        remaining_workload_minutes=round(remaining_workload, 1),
        required_minutes_per_day=round(required_per_day, 1),
        is_feasible=is_feasible,
        shortfall_minutes_per_day=round(shortfall, 1),
        new_units_per_day=round(bridges_left / float(d_rem), 2),
        questions_per_day=round(orig_left / float(d_rem), 1),
        variants_per_day=round(variant_left / float(d_rem), 1),
        horizon_cap_days=round(horizon_cap, 2),
        warning_message=warning_msg,
        status_tag=status_tag,
    )


def apply_fsrs_update(
    question_id: int,
    rating: int,
    used_hint: bool = False,
    now: Optional[datetime] = None,
    days_remaining: Optional[int] = None,
    daily_minutes: Optional[int] = None,
    is_clean_pass_override: Optional[bool] = None,
    db_path: Optional[Path] = None,
) -> Dict[str, Any]:
    """Update FSRS state for a question with Horizon Scaling and same-day Relearning."""
    ts_now = now or utc_now()
    settings = get_pace_settings(db_path=db_path)
    d_rem = max(1, days_remaining if days_remaining is not None else settings.days_remaining)
    d_min = max(5, daily_minutes if daily_minutes is not None else settings.daily_minutes)

    effective_rating = int(rating)
    if used_hint and effective_rating in (Rating.GOOD.value, Rating.EASY.value):
        effective_rating = Rating.HARD.value

    with transaction(db_path) as conn:
        row = conn.execute(
            "SELECT * FROM FSRS_STATES WHERE question_id=?", (question_id,)
        ).fetchone()
        if not row:
            raise ValueError(f"Không tìm thấy trạng thái FSRS cho câu hỏi id={question_id}")

        old_stab = float(row["stability"])
        old_diff = float(row["difficulty"])
        old_reps = int(row["reps"])
        old_lapses = int(row["lapses"])
        old_state = str(row["state"])
        spaced_clean = int(row["spaced_clean_sessions"])
        last_clean_dt = parse_iso(row["last_clean_session_at"])
        last_rev_dt = parse_iso(row["last_review"])

        elapsed_days = 0.0
        if last_rev_dt is not None:
            elapsed_days = max(0.0, (ts_now - last_rev_dt).total_seconds() / 86400.0)

        if effective_rating == Rating.AGAIN.value:
            new_state = "relearning"
            new_lapses = old_lapses + 1
            new_reps = old_reps + 1
            new_stab = round(max(0.25, old_stab * 0.4), 4)
            new_diff = round(min(MAX_DIFFICULTY, old_diff + 0.85), 3)
            # Same-day remediation queue delay: 10 min for high daily budget, 2 hours otherwise
            delay_min = 10 if d_min >= 45 else 120
            due_dt = ts_now + timedelta(minutes=delay_min)
            raw_interval_days = delay_min / 1440.0
            effective_interval_days = raw_interval_days
            # Reset consecutive clean spaced streak upon lapse
            spaced_clean = 0
            last_clean_out = None
        else:
            r_now = compute_retrievability(old_stab, elapsed_days)
            if old_state in ("new", "relearning") or old_reps == 0:
                new_stab = INITIAL_STABILITY_DAYS[effective_rating]
            else:
                if effective_rating == Rating.HARD.value:
                    mult = 1.2 + max(0.05, (11.0 - old_diff) * 0.04)
                elif effective_rating == Rating.GOOD.value:
                    mult = 1.0 + 0.45 * ((11.0 - old_diff) / 5.0) * (1.0 + (1.0 - r_now))
                else:  # EASY
                    mult = 1.0 + 0.85 * ((11.0 - old_diff) / 5.0) * (1.0 + (1.0 - r_now))
                new_stab = round(min(180.0, max(old_stab + 0.2, old_stab * mult)), 4)

            diff_delta = {
                Rating.HARD.value: 0.25,
                Rating.GOOD.value: -0.10,
                Rating.EASY.value: -0.45,
            }[effective_rating]
            new_diff = round(min(MAX_DIFFICULTY, max(MIN_DIFFICULTY, old_diff + diff_delta)), 3)
            new_reps = old_reps + 1
            new_lapses = old_lapses
            new_state = "review"
            raw_interval_days = new_stab
            effective_interval_days = compute_horizon_interval(raw_interval_days, d_rem)
            due_dt = ts_now + timedelta(days=effective_interval_days)

            clean_pass = (not used_hint) if is_clean_pass_override is None else is_clean_pass_override
            if clean_pass:
                if last_clean_dt is None or (ts_now - last_clean_dt).total_seconds() >= MIN_SPACED_SESSION_HOURS * 3600.0:
                    spaced_clean += 1
                    last_clean_dt = ts_now
            last_clean_out = format_iso(last_clean_dt) if last_clean_dt is not None else None

        new_tier = determine_scaffold_tier(new_stab, exam_mode=False)
        conn.execute(
            """
            UPDATE FSRS_STATES
            SET stability=?, difficulty=?, reps=?, lapses=?, state=?,
                scaffold_tier=?, spaced_clean_sessions=?, last_clean_session_at=?,
                last_review=?, due_date=?
            WHERE question_id=?
            """,
            (
                new_stab,
                new_diff,
                new_reps,
                new_lapses,
                new_state,
                new_tier,
                spaced_clean,
                last_clean_out,
                format_iso(ts_now),
                format_iso(due_dt),
                question_id,
            ),
        )

    return {
        "question_id": question_id,
        "effective_rating": effective_rating,
        "downgraded_by_hint": used_hint and rating in (Rating.GOOD.value, Rating.EASY.value),
        "stability": new_stab,
        "difficulty": new_diff,
        "reps": new_reps,
        "lapses": new_lapses,
        "state": new_state,
        "scaffold_tier": new_tier,
        "spaced_clean_sessions": spaced_clean,
        "raw_interval_days": round(raw_interval_days, 4),
        "effective_interval_days": round(effective_interval_days, 4),
        "due_date": format_iso(due_dt),
    }


def get_due_question_ids(
    unit_code: Optional[str] = None,
    limit: int = 20,
    now: Optional[datetime] = None,
    db_path: Optional[Path] = None,
) -> List[int]:
    """Return due/relearning/new question IDs prioritized by Remediation -> Overdue -> New."""
    ts_now = format_iso(now or utc_now())
    conn = get_connection(db_path)
    try:
        where_clauses = ["(f.state='relearning' OR f.due_date IS NULL OR f.due_date <= ?)"]
        params: List[Any] = [ts_now]
        if unit_code:
            where_clauses.append("q.unit_code=?")
            params.append(unit_code)
        where_sql = " AND ".join(where_clauses)
        params.append(limit)
        rows = conn.execute(
            f"""
            SELECT q.id
            FROM QUESTIONS q
            JOIN FSRS_STATES f ON f.question_id = q.id
            WHERE {where_sql}
            ORDER BY
                CASE f.state
                    WHEN 'relearning' THEN 0
                    WHEN 'review' THEN 1
                    ELSE 2
                END ASC,
                COALESCE(f.due_date, '') ASC,
                q.id ASC
            LIMIT ?
            """,
            tuple(params),
        ).fetchall()
        return [int(r["id"]) for r in rows]
    finally:
        conn.close()
