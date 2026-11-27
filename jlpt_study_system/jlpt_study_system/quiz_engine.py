"""Interactive Drill and Quiz Engine for Choukai Reflex and Dokkai Decoder."""

from datetime import datetime, timezone
import json
import random
from typing import Dict, List, Optional, Any

from jlpt_study_system.database import get_db
from jlpt_study_system.models import DrillItem, DrillResult, DrillType
from jlpt_study_system.error_notebook import log_mistake, remediate_by_item


def get_drill_items_by_type(
    drill_type: DrillType,
    count: Optional[int] = 5,
    db_path=None,
) -> List[DrillItem]:
    """Retrieve drill items for interactive testing."""
    with get_db(db_path) as conn:
        rows = conn.execute(
            """
            SELECT id, drill_type, section, prompt, context, options_json, correct_index, trap_analysis
            FROM drill_items
            WHERE drill_type = ?
            ORDER BY RANDOM()
            """,
            (drill_type.value,),
        ).fetchall()

    items = []
    for r in rows:
        options = json.loads(r["options_json"])
        items.append(
            DrillItem(
                id=r["id"],
                drill_type=DrillType(r["drill_type"]),
                section=r["section"],
                prompt=r["prompt"],
                context=r["context"] or "",
                options=options,
                correct_index=r["correct_index"],
                trap_analysis=r["trap_analysis"] or "",
            )
        )
        if count and len(items) >= count:
            break

    return items


def submit_drill_answer(
    drill_item_id: int,
    selected_index: int,
    response_time_sec: float = 0.0,
    db_path=None,
) -> DrillResult:
    """Evaluate drill answer, log performance, and auto-record mistakes into Error Notebook."""
    now_iso = datetime.now(timezone.utc).isoformat()
    logged_error = False

    with get_db(db_path) as conn:
        row = conn.execute(
            "SELECT * FROM drill_items WHERE id = ?", (drill_item_id,)
        ).fetchone()

        if not row:
            raise ValueError(f"Drill item {drill_item_id} not found.")

        options = json.loads(row["options_json"])
        correct_index = row["correct_index"]
        is_correct = (selected_index == correct_index)

        # Log into drill_history
        conn.execute(
            """
            INSERT INTO drill_history (drill_item_id, selected_index, is_correct, response_time_sec, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (drill_item_id, selected_index, 1 if is_correct else 0, response_time_sec, now_iso),
        )

    correct_answer_str = options[correct_index] if 0 <= correct_index < len(options) else ""
    selected_answer_str = options[selected_index] if 0 <= selected_index < len(options) else "Invalid Option"
    trap_analysis_str = row["trap_analysis"] or ""

    if not is_correct:
        log_mistake(
            item_type=row["drill_type"],
            item_id=drill_item_id,
            prompt=row["prompt"],
            user_answer=selected_answer_str,
            correct_answer=correct_answer_str,
            trap_analysis=trap_analysis_str,
            db_path=db_path,
        )
        logged_error = True
    else:
        # Auto-remediate active error notebook entry if this question was previously failed
        remediate_by_item(item_id=drill_item_id, item_type=row["drill_type"], db_path=db_path)

    return DrillResult(
        is_correct=is_correct,
        selected_index=selected_index,
        correct_index=correct_index,
        correct_answer=correct_answer_str,
        explanation=trap_analysis_str,
        trap_analysis=trap_analysis_str,
        logged_to_error_notebook=logged_error,
    )


def generate_mini_mock_quiz(count_per_section: int = 3, db_path=None) -> Dict[str, Any]:
    """Assemble a combined mini mock test across Dokkai and Choukai reflex modules."""
    choukai = get_drill_items_by_type(DrillType.CHOUKAI_REFLEX, count=count_per_section, db_path=db_path)
    dokkai = get_drill_items_by_type(DrillType.DOKKAI_DECODER, count=count_per_section, db_path=db_path)

    all_items = choukai + dokkai
    random.shuffle(all_items)

    return {
        "title": "JLPT N3 Sprint Mini-Mock Assessment",
        "total_items": len(all_items),
        "target_pass_score": int(len(all_items) * 0.7),
        "items": [
            {
                "id": item.id,
                "drill_type": item.drill_type.value,
                "section": item.section,
                "context": item.context,
                "prompt": item.prompt,
                "options": item.options,
            }
            for item in all_items
        ],
    }


def get_drill_performance_summary(db_path=None) -> Dict[str, Any]:
    """Retrieve overall quiz performance and accuracy metrics."""
    with get_db(db_path) as conn:
        stats = conn.execute(
            """
            SELECT
                d.drill_type,
                COUNT(*) AS total_attempts,
                SUM(h.is_correct) AS correct_count,
                AVG(h.response_time_sec) AS avg_speed
            FROM drill_history h
            JOIN drill_items d ON h.drill_item_id = d.id
            GROUP BY d.drill_type
            """
        ).fetchall()

    performance: Dict[str, Any] = {}
    total_all = 0
    correct_all = 0

    for s in stats:
        t = s["drill_type"]
        attempts = s["total_attempts"]
        correct = s["correct_count"] or 0
        speed = round(s["avg_speed"] or 0.0, 2)
        acc = round(correct / attempts * 100, 1) if attempts > 0 else 0.0
        performance[t] = {
            "attempts": attempts,
            "correct": correct,
            "accuracy_pct": acc,
            "avg_response_time_sec": speed,
        }
        total_all += attempts
        correct_all += correct

    overall_acc = round(correct_all / total_all * 100, 1) if total_all > 0 else 0.0
    performance["overall"] = {
        "total_attempts": total_all,
        "correct_count": correct_all,
        "accuracy_pct": overall_acc,
    }
    return performance
