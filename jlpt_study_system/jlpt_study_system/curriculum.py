"""Curriculum tracker, Pomodoro block manager, and adaptive schedule engine."""

from datetime import datetime, timezone
from typing import Dict, List, Optional, Any

from jlpt_study_system.database import get_db
from jlpt_study_system.models import CurriculumBlock, PomodoroSession
from jlpt_study_system.config import TARGET_DAILY_POMODORO, POMODORO_WORK_MINUTES, SPRINT_TOTAL_DAYS


def get_curriculum_day(day_number: int, db_path=None) -> Dict[str, Any]:
    """Retrieve all curriculum blocks for a specific sprint day, with progress."""
    with get_db(db_path) as conn:
        rows = conn.execute(
            """
            SELECT id, day_number, block_name, title, planned_minutes, completed_minutes, is_completed, notes, completed_at
            FROM curriculum_blocks
            WHERE day_number = ?
            ORDER BY id ASC
            """,
            (day_number,),
        ).fetchall()

    blocks = []
    total_planned = 0
    total_completed = 0
    completed_blocks = 0

    for r in rows:
        block = CurriculumBlock(
            id=r["id"],
            day_number=r["day_number"],
            block_name=r["block_name"],
            title=r["title"],
            planned_minutes=r["planned_minutes"],
            completed_minutes=r["completed_minutes"],
            is_completed=bool(r["is_completed"]),
            notes=r["notes"] or "",
            completed_at=datetime.fromisoformat(r["completed_at"]) if r["completed_at"] else None,
        )
        blocks.append(block)
        total_planned += block.planned_minutes
        total_completed += block.completed_minutes
        if block.is_completed:
            completed_blocks += 1

    completion_pct = round((completed_blocks / len(blocks) * 100), 1) if blocks else 0.0

    return {
        "day_number": day_number,
        "blocks": [b.model_dump() for b in blocks],
        "total_planned_minutes": total_planned,
        "total_completed_minutes": total_completed,
        "completed_blocks_count": completed_blocks,
        "total_blocks_count": len(blocks),
        "completion_rate_pct": completion_pct,
    }


def complete_curriculum_block(
    block_id: int,
    completed_minutes: Optional[int] = None,
    notes: Optional[str] = None,
    is_completed: bool = True,
    db_path=None,
) -> CurriculumBlock:
    """Mark a curriculum block as completed or update spent time."""
    now_iso = datetime.now(timezone.utc).isoformat() if is_completed else None

    with get_db(db_path) as conn:
        row = conn.execute(
            "SELECT * FROM curriculum_blocks WHERE id = ?", (block_id,)
        ).fetchone()
        if not row:
            raise ValueError(f"Curriculum block {block_id} not found.")

        new_minutes = completed_minutes if completed_minutes is not None else row["planned_minutes"]
        new_notes = notes if notes is not None else (row["notes"] or "")

        conn.execute(
            """
            UPDATE curriculum_blocks
            SET is_completed = ?, completed_minutes = ?, notes = ?, completed_at = ?
            WHERE id = ?
            """,
            (1 if is_completed else 0, new_minutes, new_notes, now_iso, block_id),
        )

        updated_row = conn.execute(
            "SELECT * FROM curriculum_blocks WHERE id = ?", (block_id,)
        ).fetchone()

    return CurriculumBlock(
        id=updated_row["id"],
        day_number=updated_row["day_number"],
        block_name=updated_row["block_name"],
        title=updated_row["title"],
        planned_minutes=updated_row["planned_minutes"],
        completed_minutes=updated_row["completed_minutes"],
        is_completed=bool(updated_row["is_completed"]),
        notes=updated_row["notes"] or "",
        completed_at=datetime.fromisoformat(updated_row["completed_at"]) if updated_row["completed_at"] else None,
    )


def log_pomodoro_session(
    day_number: int,
    block_index: int,
    task_label: str,
    duration_minutes: int = POMODORO_WORK_MINUTES,
    status: str = "completed",
    db_path=None,
) -> PomodoroSession:
    """Record a completed 50-minute Pomodoro study block."""
    now = datetime.now(timezone.utc)
    now_iso = now.isoformat()

    with get_db(db_path) as conn:
        cursor = conn.execute(
            """
            INSERT INTO pomodoro_sessions (day_number, block_index, task_label, duration_minutes, status, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
            RETURNING id
            """,
            (day_number, block_index, task_label, duration_minutes, status, now_iso),
        )
        session_id = cursor.fetchone()["id"]

    return PomodoroSession(
        id=session_id,
        day_number=day_number,
        block_index=block_index,
        task_label=task_label,
        duration_minutes=duration_minutes,
        status=status,
        created_at=now,
    )


def get_pomodoro_summary(day_number: Optional[int] = None, db_path=None) -> Dict[str, Any]:
    """Retrieve Pomodoro completion statistics."""
    with get_db(db_path) as conn:
        if day_number:
            rows = conn.execute(
                "SELECT * FROM pomodoro_sessions WHERE day_number = ? ORDER BY id ASC",
                (day_number,),
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT * FROM pomodoro_sessions ORDER BY id ASC"
            ).fetchall()

    completed = [r for r in rows if r["status"] == "completed"]
    total_minutes = sum(r["duration_minutes"] for r in completed)
    target_sessions = TARGET_DAILY_POMODORO if day_number is not None else (TARGET_DAILY_POMODORO * SPRINT_TOTAL_DAYS)

    return {
        "day_number": day_number,
        "total_sessions": len(rows),
        "completed_sessions": len(completed),
        "target_daily_sessions": TARGET_DAILY_POMODORO,
        "total_study_minutes": total_minutes,
        "target_reach_pct": round(min(100.0, len(completed) / max(1, target_sessions) * 100), 1),
    }


def get_sprint_overview(db_path=None) -> Dict[str, Any]:
    """Provide overall sprint status across all 7 days."""
    days_data = []
    total_blocks = 0
    completed_blocks = 0

    for d in range(1, 8):
        day_info = get_curriculum_day(d, db_path)
        pomo_info = get_pomodoro_summary(d, db_path)
        days_data.append({
            "day_number": d,
            "completion_rate_pct": day_info["completion_rate_pct"],
            "completed_blocks": day_info["completed_blocks_count"],
            "total_blocks": day_info["total_blocks_count"],
            "pomodoro_completed": pomo_info["completed_sessions"],
            "study_minutes": pomo_info["total_study_minutes"],
        })
        total_blocks += day_info["total_blocks_count"]
        completed_blocks += day_info["completed_blocks_count"]

    overall_pct = round((completed_blocks / total_blocks * 100), 1) if total_blocks else 0.0

    return {
        "overall_sprint_completion_pct": overall_pct,
        "total_blocks": total_blocks,
        "completed_blocks": completed_blocks,
        "days": days_data,
    }


def get_adaptive_schedule_advice(current_day: int = 1, db_path=None) -> List[str]:
    """Generate dynamic adaptive study suggestions based on error notebook and drill stats."""
    recommendations = []

    with get_db(db_path) as conn:
        # Check unresolved error notebook counts by category
        unresolved_errors = conn.execute(
            """
            SELECT item_type, COUNT(*) AS cnt
            FROM error_notebook
            WHERE remediated = 0
            GROUP BY item_type
            """
        ).fetchall()
        err_dict = {r["item_type"]: r["cnt"] for r in unresolved_errors}

        # Check Choukai reflex drill accuracy
        choukai_stats = conn.execute(
            """
            SELECT
                COUNT(*) AS total,
                SUM(is_correct) AS correct,
                AVG(response_time_sec) AS avg_speed
            FROM drill_history h
            JOIN drill_items d ON h.drill_item_id = d.id
            WHERE d.drill_type = 'choukai_reflex'
            """
        ).fetchone()

        # Check Dokkai drill accuracy
        dokkai_stats = conn.execute(
            """
            SELECT
                COUNT(*) AS total,
                SUM(is_correct) AS correct
            FROM drill_history h
            JOIN drill_items d ON h.drill_item_id = d.id
            WHERE d.drill_type = 'dokkai_decoder'
            """
        ).fetchone()

    # Grammar weakness adaptation
    grammar_errs = err_dict.get("grammar", 0)
    if grammar_errs >= 3:
        recommendations.append(
            f"[THÍCH ỨNG NGÀY {current_day}] Phát hiện {grammar_errs} bẫy Ngữ pháp chưa khắc phục. Dành riêng 1 block Pomodoro 50 phút tập trung giải phẫu bẫy trong Sổ tay bẫy trắc nghiệm."
        )

    # Vocab / Discourse weakness adaptation
    vocab_errs = err_dict.get("vocab", 0)
    if vocab_errs >= 3:
        recommendations.append(
            f"[THÍCH ỨNG NGÀY {current_day}] Từ nối lập luận còn {vocab_errs} từ nhầm lẫn. Cần tăng cường 100 lượt review flashcard từ nối trước khi làm bài Đọc hiểu."
        )

    # Choukai reflex error notebook weakness
    choukai_errs = err_dict.get("choukai_reflex", 0)
    if choukai_errs >= 2:
        recommendations.append(
            f"[THÍCH ỨNG NGÀY {current_day}] Phát hiện {choukai_errs} bẫy đối đáp Mondai 5 chưa khắc phục. Ôn lại các cặp phản xạ 'khiêm tốn' và 'từ chối khéo' trong Sổ tay bẫy."
        )

    # Dokkai decoder error notebook weakness
    dokkai_errs = err_dict.get("dokkai_decoder", 0)
    if dokkai_errs >= 2:
        recommendations.append(
            f"[THÍCH ỨNG NGÀY {current_day}] Phát hiện {dokkai_errs} bẫy Đọc hiểu chưa khắc phục. Rà soát quy tắc quét chú thích hoa thị và bẫy ngoài bài."
        )

    # Choukai accuracy & speed adaptation
    if choukai_stats and choukai_stats["total"] >= 3:
        acc = choukai_stats["correct"] / choukai_stats["total"]
        avg_speed = choukai_stats["avg_speed"] or 0.0
        if acc < 0.7:
            recommendations.append(
                f"[CẢNH BÁO SÀN LIỆT NGHE] Tỷ lệ chính xác Mondai 5 chỉ đạt {round(acc*100, 1)}%. Bổ sung 1 lượt luyện phản xạ tức thì 20 câu để bảo vệ mốc an toàn 30 điểm."
            )
        if avg_speed > 3.5:
            recommendations.append(
                f"[TỐC ĐỘ PHẢN XẠ NGHE] Thời gian chọn đáp án trung bình {round(avg_speed, 1)}s (chậm hơn chuẩn 2.0s). Luyện thói quen chọn đáp án ngay khi câu hỏi vừa dứt."
            )

    # Dokkai accuracy adaptation
    if dokkai_stats and dokkai_stats["total"] >= 3:
        acc = dokkai_stats["correct"] / dokkai_stats["total"]
        if acc < 0.7:
            recommendations.append(
                f"[CẢNH BÁO ĐỌC HIỂU] Độ chính xác đọc quét đạt {round(acc*100, 1)}%. Áp dụng triệt để quy tắc loại trừ bẫy Tuyệt đối hóa (loại đáp án có 'すべて', '絶対に')."
            )

    if not recommendations:
        recommendations.append(
            f"[TIẾN ĐỘ CHUẨN] Nhịp độ học tập ngày {current_day} đang vận hành ổn định. Tiếp tục duy trì kỷ luật 12 Pomodoro/ngày theo Sổ tay tác chiến."
        )

    return recommendations
