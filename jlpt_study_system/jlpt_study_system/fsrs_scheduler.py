"""Spaced Repetition Scheduler (FSRS-inspired for JLPT N3 7-Day Sprint)."""

from datetime import datetime, timedelta, timezone
from typing import List, Optional, Tuple
import json

from jlpt_study_system.config import (
    DEFAULT_DIFFICULTY,
    DEFAULT_STABILITY,
    MIN_DIFFICULTY,
    MAX_DIFFICULTY,
    INITIAL_STABILITY,
    DESIRED_RETENTION_SPRINT,
)
from jlpt_study_system.models import (
    Card,
    CardCategory,
    CardState,
    FSRSState,
    Rating,
    CardWithState,
)
from jlpt_study_system.database import get_db
from jlpt_study_system.error_notebook import remediate_by_item


def calculate_next_fsrs_state(
    current_state: FSRSState,
    rating: Rating,
    review_time: Optional[datetime] = None,
) -> FSRSState:
    """Pure function calculating the next FSRS state after a review rating.

    Tuned for 7-day high-yield sprint:
    - Again (1): Immediate recycle (10 minutes), records lapse, resets stability.
    - Hard (2): 1 day interval, slightly decreases difficulty factor.
    - Good (3): 2-3 days interval based on stability and difficulty.
    - Easy (4): 4-6 days interval for instant recognition.
    """
    now = review_time or datetime.now(timezone.utc)

    stability = current_state.stability
    difficulty = current_state.difficulty
    reps = current_state.reps
    lapses = current_state.lapses
    state = current_state.state

    # First review (Card is NEW or 0 reps)
    if state == CardState.NEW or reps == 0:
        # Initial difficulty calculation
        difficulty = DEFAULT_DIFFICULTY - (rating.value - 3) * 0.8
        difficulty = max(MIN_DIFFICULTY, min(MAX_DIFFICULTY, round(difficulty, 2)))
        stability = INITIAL_STABILITY.get(rating.value, 2.0)

        if rating == Rating.AGAIN:
            new_state = CardState.LEARNING
            new_reps = 0
            new_lapses = lapses + 1
            scheduled_days = 0
            due_date = now + timedelta(minutes=10)
        else:
            new_state = CardState.REVIEW
            new_reps = 1
            new_lapses = lapses
            scheduled_days = max(1, min(7, round(stability)))
            due_date = now + timedelta(days=scheduled_days)

        return FSRSState(
            card_id=current_state.card_id,
            stability=round(stability, 2),
            difficulty=round(difficulty, 2),
            reps=new_reps,
            lapses=new_lapses,
            state=new_state,
            last_review=now,
            due_date=due_date,
            scheduled_days=scheduled_days,
        )

    # Subsequent reviews
    if rating == Rating.AGAIN:
        # Lapse event
        new_lapses = lapses + 1
        new_state = CardState.RELEARNING
        new_reps = reps
        stability = max(0.4, stability * 0.35)
        difficulty = min(MAX_DIFFICULTY, difficulty + 0.8)
        scheduled_days = 0
        due_date = now + timedelta(minutes=10)
    else:
        # Successful recall
        new_reps = reps + 1
        new_lapses = lapses
        new_state = CardState.REVIEW

        # Mean-reverting difficulty update
        delta_d = -0.4 * (rating.value - 3)
        difficulty = max(MIN_DIFFICULTY, min(MAX_DIFFICULTY, difficulty + delta_d))

        # Stability multiplier
        if rating == Rating.HARD:
            mult = 1.2
        elif rating == Rating.GOOD:
            mult = 2.1 * ((11.0 - difficulty) / 6.0)
        else:  # EASY
            mult = 3.2 * ((11.0 - difficulty) / 5.0)

        stability = max(0.6, stability * mult)

        # Sprint interval calculation (bounded to 7 days maximum)
        interval_val = stability * (1.0 / DESIRED_RETENTION_SPRINT)
        scheduled_days = max(1, min(7, round(interval_val)))
        due_date = now + timedelta(days=scheduled_days)

    return FSRSState(
        card_id=current_state.card_id,
        stability=round(stability, 2),
        difficulty=round(difficulty, 2),
        reps=new_reps,
        lapses=new_lapses,
        state=new_state,
        last_review=now,
        due_date=due_date,
        scheduled_days=scheduled_days,
    )


def get_due_cards(
    db_path=None,
    limit: Optional[int] = 50,
    category: Optional[CardCategory] = None,
) -> List[CardWithState]:
    """Retrieve cards that are due for review (or never reviewed), ordered by priority."""
    now_iso = datetime.now(timezone.utc).isoformat()
    query = """
        SELECT
            c.id AS c_id, c.category, c.front, c.back, c.trap, c.example, c.tags, c.created_at,
            f.card_id, f.stability, f.difficulty, f.reps, f.lapses, f.state, f.last_review, f.due_date, f.scheduled_days
        FROM cards c
        JOIN fsrs_states f ON c.id = f.card_id
        WHERE (f.due_date IS NULL OR f.due_date <= ?)
    """
    params = [now_iso]
    if category:
        cat_val = category.value if hasattr(category, "value") else str(category)
        query += " AND c.category = ?"
        params.append(cat_val)

    # Prioritize: Relearning & Learning cards first, then overdue Reviews, then New cards
    query += """
        ORDER BY
            CASE f.state
                WHEN 'Relearning' THEN 1
                WHEN 'Learning' THEN 2
                WHEN 'Review' THEN 3
                WHEN 'New' THEN 4
                ELSE 5
            END,
            f.due_date ASC
    """
    if limit:
        query += f" LIMIT {int(limit)}"

    results = []
    with get_db(db_path) as conn:
        rows = conn.execute(query, params).fetchall()
        for r in rows:
            card = Card(
                id=r["c_id"],
                category=CardCategory(r["category"]),
                front=r["front"],
                back=r["back"],
                trap=r["trap"] or "",
                example=r["example"] or "",
                tags=r["tags"] or "",
                created_at=datetime.fromisoformat(r["created_at"]) if r["created_at"] else None,
            )
            fsrs = FSRSState(
                card_id=r["card_id"],
                stability=r["stability"],
                difficulty=r["difficulty"],
                reps=r["reps"],
                lapses=r["lapses"],
                state=CardState(r["state"]),
                last_review=datetime.fromisoformat(r["last_review"]) if r["last_review"] else None,
                due_date=datetime.fromisoformat(r["due_date"]) if r["due_date"] else None,
                scheduled_days=r["scheduled_days"],
            )
            results.append(CardWithState(card=card, fsrs=fsrs))
    return results


def process_card_review(
    card_id: int,
    rating: Rating,
    elapsed_seconds: float = 0.0,
    db_path=None,
) -> Tuple[CardWithState, bool]:
    """Update card state with review rating and log history.

    Returns (updated_card_with_state, logged_to_error_notebook).
    """
    now = datetime.now(timezone.utc)
    now_iso = now.isoformat()
    logged_error = False

    with get_db(db_path) as conn:
        # 1. Fetch current card and FSRS state
        row = conn.execute(
            """
            SELECT
                c.id AS c_id, c.category, c.front, c.back, c.trap, c.example, c.tags, c.created_at,
                f.card_id, f.stability, f.difficulty, f.reps, f.lapses, f.state, f.last_review, f.due_date, f.scheduled_days
            FROM cards c
            JOIN fsrs_states f ON c.id = f.card_id
            WHERE c.id = ?
            """,
            (card_id,),
        ).fetchone()

        if not row:
            raise ValueError(f"Card with id {card_id} not found.")

        card = Card(
            id=row["c_id"],
            category=CardCategory(row["category"]),
            front=row["front"],
            back=row["back"],
            trap=row["trap"] or "",
            example=row["example"] or "",
            tags=row["tags"] or "",
            created_at=datetime.fromisoformat(row["created_at"]) if row["created_at"] else None,
        )
        current_fsrs = FSRSState(
            card_id=row["card_id"],
            stability=row["stability"],
            difficulty=row["difficulty"],
            reps=row["reps"],
            lapses=row["lapses"],
            state=CardState(row["state"]),
            last_review=datetime.fromisoformat(row["last_review"]) if row["last_review"] else None,
            due_date=datetime.fromisoformat(row["due_date"]) if row["due_date"] else None,
            scheduled_days=row["scheduled_days"],
        )

        # 2. Compute new state
        next_fsrs = calculate_next_fsrs_state(current_fsrs, rating, review_time=now)

        # 3. Persist new state
        conn.execute(
            """
            UPDATE fsrs_states
            SET stability = ?, difficulty = ?, reps = ?, lapses = ?, state = ?,
                last_review = ?, due_date = ?, scheduled_days = ?
            WHERE card_id = ?
            """,
            (
                next_fsrs.stability,
                next_fsrs.difficulty,
                next_fsrs.reps,
                next_fsrs.lapses,
                next_fsrs.state.value,
                next_fsrs.last_review.isoformat() if next_fsrs.last_review else None,
                next_fsrs.due_date.isoformat() if next_fsrs.due_date else None,
                next_fsrs.scheduled_days,
                card_id,
            ),
        )

        # 4. Insert review log
        conn.execute(
            """
            INSERT INTO review_logs (card_id, rating, review_time, elapsed_seconds, scheduled_days, stability_after, difficulty_after)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                card_id,
                rating.value,
                now_iso,
                elapsed_seconds,
                next_fsrs.scheduled_days,
                next_fsrs.stability,
                next_fsrs.difficulty,
            ),
        )

        # 5. If rating is AGAIN (1) or HARD (2), log or update error notebook
        if rating in (Rating.AGAIN, Rating.HARD):
            trap_note = card.trap if card.trap else f"Cần ôn tập lại: {card.back}"
            existing_err = conn.execute(
                "SELECT id, attempt_count FROM error_notebook WHERE item_id = ? AND item_type = ? AND remediated = 0",
                (card_id, card.category.value),
            ).fetchone()
            if existing_err:
                conn.execute(
                    "UPDATE error_notebook SET attempt_count = attempt_count + 1 WHERE id = ?",
                    (existing_err["id"],),
                )
            else:
                conn.execute(
                    """
                    INSERT INTO error_notebook (item_type, item_id, prompt, user_answer, correct_answer, trap_analysis, remediated, attempt_count, created_at)
                    VALUES (?, ?, ?, ?, ?, ?, 0, 1, ?)
                    """,
                    (
                        card.category.value,
                        card_id,
                        card.front,
                        f"Rating: {rating.name} (hesitation/mistake)",
                        card.back,
                        trap_note,
                        now_iso,
                    ),
                )
            logged_error = True
        elif rating in (Rating.GOOD, Rating.EASY):
            # Auto-remediate active error notebook entry upon successful recall
            conn.execute(
                """
                UPDATE error_notebook
                SET remediated = 1, remediated_at = ?
                WHERE item_id = ? AND item_type = ? AND remediated = 0
                """,
                (now_iso, card_id, card.category.value),
            )

    return CardWithState(card=card, fsrs=next_fsrs), logged_error


def get_card_stats(db_path=None) -> dict:
    """Get aggregated statistics on deck cards."""
    with get_db(db_path) as conn:
        total = conn.execute("SELECT COUNT(*) AS c FROM cards").fetchone()["c"]
        states = conn.execute(
            "SELECT state, COUNT(*) AS c FROM fsrs_states GROUP BY state"
        ).fetchall()
        categories = conn.execute(
            "SELECT category, COUNT(*) AS c FROM cards GROUP BY category"
        ).fetchall()
        reviews_count = conn.execute("SELECT COUNT(*) AS c FROM review_logs").fetchone()["c"]

        # Good/Easy vs Again/Hard retention
        retention_row = conn.execute(
            """
            SELECT
                COUNT(*) AS total,
                SUM(CASE WHEN rating >= 3 THEN 1 ELSE 0 END) AS successful
            FROM review_logs
            """
        ).fetchone()

        retention_rate = 0.0
        if retention_row and retention_row["total"] > 0:
            retention_rate = round(retention_row["successful"] / retention_row["total"] * 100, 1)

    state_dict = {row["state"]: row["c"] for row in states}
    cat_dict = {row["category"]: row["c"] for row in categories}

    return {
        "total_cards": total,
        "states": {
            "New": state_dict.get("New", 0),
            "Learning": state_dict.get("Learning", 0),
            "Review": state_dict.get("Review", 0),
            "Relearning": state_dict.get("Relearning", 0),
        },
        "categories": cat_dict,
        "total_reviews": reviews_count,
        "retention_rate_pct": retention_rate,
    }
