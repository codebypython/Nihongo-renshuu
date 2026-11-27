"""Error Notebook (Sổ tay bẫy trắc nghiệm) persistence and remediation."""

from datetime import datetime, timezone
from typing import Dict, List, Optional, Any

from jlpt_study_system.database import get_db
from jlpt_study_system.models import ErrorItem


def log_mistake(
    item_type: str,
    prompt: str,
    user_answer: str,
    correct_answer: str,
    trap_analysis: str,
    item_id: Optional[int] = None,
    db_path=None,
) -> ErrorItem:
    """Log or update an error entry in the Error Notebook."""
    now = datetime.now(timezone.utc)
    now_iso = now.isoformat()

    with get_db(db_path) as conn:
        existing = conn.execute(
            """
            SELECT id, attempt_count FROM error_notebook
            WHERE prompt = ? AND item_type = ? AND remediated = 0
            """,
            (prompt, item_type),
        ).fetchone()

        if existing:
            new_attempts = existing["attempt_count"] + 1
            conn.execute(
                """
                UPDATE error_notebook
                SET attempt_count = ?, user_answer = ?, trap_analysis = ?
                WHERE id = ?
                """,
                (new_attempts, user_answer, trap_analysis, existing["id"]),
            )
            err_id = existing["id"]
        else:
            cursor = conn.execute(
                """
                INSERT INTO error_notebook (item_type, item_id, prompt, user_answer, correct_answer, trap_analysis, remediated, attempt_count, created_at)
                VALUES (?, ?, ?, ?, ?, ?, 0, 1, ?)
                RETURNING id
                """,
                (item_type, item_id, prompt, user_answer, correct_answer, trap_analysis, now_iso),
            )
            err_id = cursor.fetchone()["id"]
            new_attempts = 1

    return ErrorItem(
        id=err_id,
        item_type=item_type,
        item_id=item_id,
        prompt=prompt,
        user_answer=user_answer,
        correct_answer=correct_answer,
        trap_analysis=trap_analysis,
        remediated=False,
        attempt_count=new_attempts,
        created_at=now,
    )


def get_error_items(
    remediated: Optional[bool] = None,
    item_type: Optional[str] = None,
    limit: Optional[int] = 100,
    db_path=None,
) -> List[ErrorItem]:
    """Retrieve error items with optional filtering by remediation status and type."""
    query = "SELECT * FROM error_notebook WHERE 1=1"
    params: List[Any] = []

    if remediated is not None:
        query += " AND remediated = ?"
        params.append(1 if remediated else 0)

    if item_type:
        query += " AND item_type = ?"
        params.append(item_type)

    query += " ORDER BY attempt_count DESC, id DESC"
    if limit:
        query += f" LIMIT {int(limit)}"

    results = []
    with get_db(db_path) as conn:
        rows = conn.execute(query, params).fetchall()
        for r in rows:
            results.append(
                ErrorItem(
                    id=r["id"],
                    item_type=r["item_type"],
                    item_id=r["item_id"],
                    prompt=r["prompt"],
                    user_answer=r["user_answer"],
                    correct_answer=r["correct_answer"],
                    trap_analysis=r["trap_analysis"],
                    remediated=bool(r["remediated"]),
                    attempt_count=r["attempt_count"],
                    created_at=datetime.fromisoformat(r["created_at"]) if r["created_at"] else None,
                    remediated_at=datetime.fromisoformat(r["remediated_at"]) if r["remediated_at"] else None,
                )
            )
    return results


def remediate_error_item(error_id: int, success: bool = True, db_path=None) -> ErrorItem:
    """Record remediation attempt on an error notebook entry."""
    now_iso = datetime.now(timezone.utc).isoformat()

    with get_db(db_path) as conn:
        row = conn.execute(
            "SELECT * FROM error_notebook WHERE id = ?", (error_id,)
        ).fetchone()
        if not row:
            raise ValueError(f"Error item {error_id} not found.")

        if success:
            conn.execute(
                """
                UPDATE error_notebook
                SET remediated = 1, remediated_at = ?
                WHERE id = ?
                """,
                (now_iso, error_id),
            )
        else:
            conn.execute(
                """
                UPDATE error_notebook
                SET attempt_count = attempt_count + 1
                WHERE id = ?
                """,
                (error_id,),
            )

        updated = conn.execute(
            "SELECT * FROM error_notebook WHERE id = ?", (error_id,)
        ).fetchone()

    return ErrorItem(
        id=updated["id"],
        item_type=updated["item_type"],
        item_id=updated["item_id"],
        prompt=updated["prompt"],
        user_answer=updated["user_answer"],
        correct_answer=updated["correct_answer"],
        trap_analysis=updated["trap_analysis"],
        remediated=bool(updated["remediated"]),
        attempt_count=updated["attempt_count"],
        created_at=datetime.fromisoformat(updated["created_at"]) if updated["created_at"] else None,
        remediated_at=datetime.fromisoformat(updated["remediated_at"]) if updated["remediated_at"] else None,
    )


def remediate_by_item(item_id: int, item_type: str, db_path=None) -> int:
    """Automatically resolve active error notebook entries for a specific card or drill item."""
    now_iso = datetime.now(timezone.utc).isoformat()
    with get_db(db_path) as conn:
        cursor = conn.execute(
            """
            UPDATE error_notebook
            SET remediated = 1, remediated_at = ?
            WHERE item_id = ? AND item_type = ? AND remediated = 0
            """,
            (now_iso, item_id, item_type),
        )
        return cursor.rowcount


def get_error_notebook_stats(db_path=None) -> Dict[str, Any]:
    """Calculate aggregated stats for the Error Notebook."""
    with get_db(db_path) as conn:
        total = conn.execute("SELECT COUNT(*) AS c FROM error_notebook").fetchone()["c"]
        unresolved = conn.execute("SELECT COUNT(*) AS c FROM error_notebook WHERE remediated = 0").fetchone()["c"]
        remediated = conn.execute("SELECT COUNT(*) AS c FROM error_notebook WHERE remediated = 1").fetchone()["c"]
        
        breakdown = conn.execute(
            """
            SELECT item_type, COUNT(*) AS count
            FROM error_notebook
            WHERE remediated = 0
            GROUP BY item_type
            """
        ).fetchall()

        top_traps = conn.execute(
            """
            SELECT id, item_type, prompt, trap_analysis, attempt_count
            FROM error_notebook
            WHERE remediated = 0
            ORDER BY attempt_count DESC
            LIMIT 5
            """
        ).fetchall()

    breakdown_dict = {r["item_type"]: r["count"] for r in breakdown}
    
    return {
        "total_errors_logged": total,
        "unresolved_errors": unresolved,
        "remediated_errors": remediated,
        "remediation_rate_pct": round(remediated / total * 100, 1) if total > 0 else 100.0,
        "unresolved_by_type": breakdown_dict,
        "top_recurring_traps": [
            {
                "id": t["id"],
                "type": t["item_type"],
                "prompt": t["prompt"][:60],
                "trap": t["trap_analysis"][:100],
                "attempts": t["attempt_count"],
            }
            for t in top_traps
        ],
    }
