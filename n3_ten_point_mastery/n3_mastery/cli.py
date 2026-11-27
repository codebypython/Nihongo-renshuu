"""Rich Terminal CLI for JLPT N3 10/10 Mastery System."""

import argparse
import json
import secrets
import sys
from pathlib import Path
from typing import List, Optional

import uvicorn
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from n3_mastery.config import DEFAULT_API_HOST, DEFAULT_API_PORT, get_excel_dir
from n3_mastery.database import get_connection, init_db, transaction
from n3_mastery.drill_engine import (
    get_error_notebook,
    get_next_study_candidate,
    submit_answer,
)
from n3_mastery.fsrs_adaptive import (
    compute_pace_feasibility,
    update_pace_settings,
)
from n3_mastery.importer import import_all_excel, import_excel_file
from n3_mastery.readiness import calculate_dual_readiness, is_question_mastered
from n3_mastery.scaffolding import get_contextual_hint

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

console = Console()


def _ensure_seeded_if_empty() -> None:
    init_db()
    conn = get_connection()
    try:
        cnt = conn.execute("SELECT COUNT(*) FROM QUESTIONS").fetchone()[0]
    finally:
        conn.close()
    if cnt == 0 and get_excel_dir().exists():
        import_all_excel(generate_variants=True)


def cmd_status() -> int:
    _ensure_seeded_if_empty()
    rep = calculate_dual_readiness()
    pace = compute_pace_feasibility()

    console.print(
        Panel(
            f"[bold]Điểm Đề Gốc (Original Bank):[/bold] {rep.original_score_10:.2f} / 10.00\n"
            f"[bold]Điểm Chống Biến Thể (Anti-Rote Mastery):[/bold] {rep.mastery_score_10:.2f} / 10.00\n"
            f"[bold]Độ lệch học vẹt (Rote Gap):[/bold] {rep.rote_gap_10:.2f}\n"
            f"[bold]Đạt cổng [MASTERED 10/10]:[/bold] {rep.mastered_count} / {rep.total_questions} ({rep.mastered_percent}%)\n"
            f"[bold]Nhận định trung thực:[/bold] {rep.honest_verdict}",
            title="JLPT N3 10/10 MASTERY — BẢNG ĐIỂM KÉP",
        )
    )

    pace_msg = (
        f"Ngày còn lại: {pace.days_remaining} | Phút/ngày: {pace.daily_minutes} | "
        f"Tải còn lại: {pace.remaining_workload_minutes:.1f} phút | Yêu cầu: {pace.required_minutes_per_day:.1f} phút/ngày\n"
        f"Trạng thái: {pace.status_tag}"
    )
    if pace.warning_message:
        pace_msg += f"\n{pace.warning_message}"
    console.print(Panel(pace_msg, title="ADAPTIVE PACE & FSRS HORIZON"))

    conn = get_connection()
    try:
        units = conn.execute(
            """
            SELECT u.code, u.title, u.section, b.completed AS bridge_done
            FROM MICRO_UNITS u
            LEFT JOIN N4_BRIDGE_CAPSULES b ON b.unit_code=u.code
            ORDER BY u.order_index
            """
        ).fetchall()
        q_rows = conn.execute(
            """
            SELECT q.unit_code, f.clean_original_passed, f.variant_passed,
                   f.spaced_clean_sessions, f.state,
                   (SELECT a.is_correct FROM ATTEMPT_LOGS a WHERE a.question_id=q.id ORDER BY a.id DESC LIMIT 1) AS latest_overall_correct
            FROM QUESTIONS q JOIN FSRS_STATES f ON f.question_id=q.id
            """
        ).fetchall()
    finally:
        conn.close()

    table = Table(title="Lộ trình 12 Micro-Units (N5 -> N4 -> N3 10/10)")
    table.add_column("Mã", style="bold")
    table.add_column("Phân môn")
    table.add_column("Trạm N4")
    table.add_column("Đề gốc")
    table.add_column("Biến thể")
    table.add_column("[MASTERED 10/10]")
    table.add_column("Tên Unit")

    grouped = {}
    for qr in q_rows:
        grouped.setdefault(qr["unit_code"], []).append(dict(qr))

    for u in units:
        items = grouped.get(u["code"], [])
        tot = len(items)
        orig = sum(1 for x in items if int(x["clean_original_passed"]) == 1)
        var = sum(1 for x in items if int(x["variant_passed"]) >= 1)
        mast = sum(1 for x in items if is_question_mastered(x))
        table.add_row(
            u["code"],
            u["section"],
            "[OK]" if u["bridge_done"] else "[CHƯA]",
            f"{orig}/{tot}",
            f"{var}/{tot}",
            f"{mast}/{tot}",
            u["title"],
        )
    console.print(table)
    return 0


def cmd_import(target: Optional[str]) -> int:
    init_db()
    p = Path(target) if target else get_excel_dir()
    try:
        if p.is_dir():
            res = import_all_excel(excel_dir=p, generate_variants=True)
            console.print(
                Panel(
                    f"Đã xử lý {res['files_processed']} tệp Excel | Tổng dòng gốc: {res['total_raw_rows']} -> "
                    f"Câu hỏi duy nhất: {res['unique_questions']} | Văn bản Dokkai: {res['dokkai_passages']} | "
                    f"Biến thể trong DB: {res['total_variants_in_db']}",
                    title="[OK] KẾT QUẢ IMPORT EXCEL",
                )
            )
        else:
            res = import_excel_file(p, generate_variants=True)
            console.print(
                Panel(
                    f"Tệp: {res['filename']} | Layout: {res['layout_type']} | "
                    f"Dòng gốc: {res['raw_count']} | Mới thêm: {res['newly_imported_count']} | "
                    f"Biến thể tạo mới: {res['variants_generated']}",
                    title="[OK] KẾT QUẢ IMPORT EXCEL",
                )
            )
        return 0
    except (FileNotFoundError, ValueError) as exc:
        console.print(f"[FAIL] {exc}")
        return 1


def cmd_pace(days: Optional[int], minutes: Optional[int], scoring: Optional[str]) -> int:
    _ensure_seeded_if_empty()
    settings = update_pace_settings(days_remaining=days, daily_minutes=minutes, scoring_mode=scoring)
    pace = compute_pace_feasibility()
    msg = (
        f"Cấu hình mới: {settings.days_remaining} ngày còn lại | {settings.daily_minutes} phút/ngày | "
        f"Trọng số: {settings.scoring_mode.value}\n"
        f"Tải còn lại: {pace.remaining_workload_minutes:.1f} phút | Cần: {pace.required_minutes_per_day:.1f} phút/ngày\n"
        f"Nén FSRS tối đa (Horizon cap): {pace.horizon_cap_days} ngày\n"
        f"Trạng thái: {pace.status_tag}"
    )
    if pace.warning_message:
        msg += f"\n{pace.warning_message}"
    console.print(Panel(msg, title="CẬP NHẬT ADAPTIVE PACE"))
    return 0


def cmd_bridge(unit_code: str, complete: bool = False) -> int:
    _ensure_seeded_if_empty()
    conn = get_connection()
    try:
        cap = conn.execute("SELECT * FROM N4_BRIDGE_CAPSULES WHERE unit_code=?", (unit_code,)).fetchone()
        unit = conn.execute("SELECT * FROM MICRO_UNITS WHERE code=?", (unit_code,)).fetchone()
    finally:
        conn.close()
    if not cap or not unit:
        console.print(f"[FAIL] Không tìm thấy Micro-Unit '{unit_code}'")
        return 1

    examples = json.loads(cap["examples_json"] or "[]")
    ex_lines = "\n".join(f"  - {e['jp']} -> {e['vi']}" for e in examples)
    console.print(
        Panel(
            f"[bold]{unit['code']} — {unit['title']}[/bold]\n"
            f"[bold]Trọng tâm N4->N3:[/bold] {cap['grammar_focus']}\n\n"
            f"{cap['explanation_vi']}\n\n"
            f"[bold]Ví dụ đối chiếu:[/bold]\n{ex_lines}",
            title=f"TRẠM BẮC CẦU N4->N3 ({unit_code})",
        )
    )
    if complete:
        with transaction() as wconn:
            wconn.execute("UPDATE N4_BRIDGE_CAPSULES SET completed=1 WHERE unit_code=?", (unit_code,))
        console.print(f"[OK] Đã đánh dấu hoàn thành Trạm Bắc cầu N4 cho {unit_code}.")
    return 0


def cmd_errors() -> int:
    _ensure_seeded_if_empty()
    errs = get_error_notebook(limit=50)
    if not errs:
        console.print("[OK] Sổ tay Lỗ hổng hiện đang trống (0 câu đang Relearning).")
        return 0
    table = Table(title=f"Sổ tay Lỗ hổng ({len(errs)} câu cần vá)")
    table.add_column("ID")
    table.add_column("Unit")
    table.add_column("Mondai")
    table.add_column("Lapses")
    table.add_column("Từ khóa")
    table.add_column("Đề bài")
    for e in errs:
        table.add_row(
            str(e["question_id"]),
            e["unit_code"],
            e["mondai_type"],
            str(e["lapses"]),
            e["focus_keyword"],
            e["prompt_jp"].replace("\n", " ")[:60],
        )
    console.print(table)
    return 0


def cmd_study(unit_code: Optional[str], mode: str, limit: int, exam_mode: bool) -> int:
    _ensure_seeded_if_empty()
    seed = secrets.token_hex(4)
    done = 0
    while done < limit:
        item = get_next_study_candidate(
            unit_code=unit_code,
            mode=mode,
            session_seed=seed,
            exam_mode=exam_mode,
        )
        if item is None:
            console.print("[INFO] Không còn câu hỏi trong hàng đợi này.")
            break

        console.print(
            Panel(
                f"Unit: {item['unit_code']} | {item['mondai_type']} | Chế độ: {item['variant_mode']} | {item['scaffolding']['tier_label']}",
                title=f"CÂU HỎI #{item['question_id']}",
            )
        )
        if item["passage"]:
            sents = item["passage"]["sentences"]
            p_lines = "\n".join(f"[{s['index']}] {s['text']}" for s in sents)
            console.print(Panel(p_lines, title=f"VĂN BẢN: {item['passage']['title']}"))

        console.print(item["prompt_jp"])
        if item["interaction_type"] == "star_4slot":
            sa = item["star_assembly"]
            console.print(f"Vị trí dấu ★: Ô số {sa['star_slot_index'] + 1}")
            for c in sa["chunks"]:
                console.print(f"  Mảnh [{c['chunk_index']}]: {c['text']}")
            raw = console.input("Nhập thứ tự 4 chỉ số mảnh cách nhau bởi dấu cách (vd: 2 0 1 3) hoặc 'q' để thoát: ").strip()
            if raw.lower() == "q":
                break
            try:
                slots = [int(x) for x in raw.split()]
                res = submit_answer(
                    item["question_id"],
                    mode=item["mode"],
                    variant_id=item["variant_id"],
                    slot_order=slots,
                    session_seed=seed,
                    exam_mode=exam_mode,
                )
            except Exception as exc:
                console.print(f"[FAIL] {exc}")
                continue
        else:
            for idx, opt in enumerate(item["options"], 1):
                console.print(f"  {idx}. {opt}")
            used_hint = False
            while True:
                prompt_msg = "Chọn đáp án 1-4 (nhấn 'h' gợi ý, 'q' thoát): "
                raw = console.input(prompt_msg).strip().lower()
                if raw == "q":
                    return 0
                if raw == "h":
                    h = get_contextual_hint(
                        item["prompt_jp"],
                        stability=item["fsrs"]["stability"],
                        exam_mode=exam_mode,
                    )
                    if h["allowed"]:
                        used_hint = True
                        console.print(f"[INFO] {h['hint_text']}")
                    else:
                        console.print(f"[WARN] {h['reason']}")
                    continue
                if raw in ("1", "2", "3", "4"):
                    sel_idx = int(raw) - 1
                    ev_indices = None
                    if item["interaction_type"] == "dokkai_evidence":
                        ev_raw = console.input("Nhập chỉ số câu chốt bằng chứng trong bài (vd: 0 hoặc 1 2): ").strip()
                        ev_indices = [int(x) for x in ev_raw.split() if x.isdigit()]
                    try:
                        res = submit_answer(
                            item["question_id"],
                            mode=item["mode"],
                            variant_id=item["variant_id"],
                            selected_index=sel_idx,
                            evidence_indices=ev_indices,
                            used_hint=used_hint,
                            session_seed=seed,
                            exam_mode=exam_mode,
                        )
                    except Exception as exc:
                        console.print(f"[FAIL] {exc}")
                        continue
                    break

        tag = "[OK] CHÍNH XÁC" if res["is_correct"] else "[FAIL] SAI"
        console.print(f"{tag} | Đáp án đúng: {res['correct_option_text']}")
        console.print(res["explanation_vi"])
        done += 1
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="n3_cli.py",
        description="JLPT N3 10/10 Mastery System CLI",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("status", help="Xem Bảng điểm Kép /10, Adaptive Pace và tiến độ 12 Micro-Units")

    p_imp = sub.add_parser("import", help="Nạp dữ liệu từ tệp .xlsx hoặc thư mục Excel")
    p_imp.add_argument("target", nargs="?", default=None, help="Đường dẫn file .xlsx hoặc thư mục")

    p_pace = sub.add_parser("pace", help="Cập nhật ngày thi còn lại, phút học/ngày và chế độ điểm")
    p_pace.add_argument("--days", type=int, default=None)
    p_pace.add_argument("--minutes", type=int, default=None)
    p_pace.add_argument("--scoring", choices=["jlpt_weighted", "equal_weighted"], default=None)

    p_bridge = sub.add_parser("bridge", help="Xem bài học Trạm Bắc cầu N4->N3 của một Unit")
    p_bridge.add_argument("unit_code", help="Ví dụ: MU-01")
    p_bridge.add_argument("--complete", action="store_true", help="Đánh dấu hoàn thành trạm bắc cầu")

    sub.add_parser("errors", help="Xem Sổ tay Lỗ hổng")

    p_study = sub.add_parser("study", help="Luyện tập tương tác trên terminal")
    p_study.add_argument("--unit", default=None, help="Mã Micro-Unit (vd: MU-01)")
    p_study.add_argument("--mode", default="mixed", choices=["mixed", "original", "variant", "remediation"])
    p_study.add_argument("--limit", type=int, default=5)
    p_study.add_argument("--exam", action="store_true", help="Bật chế độ Phòng thi (khóa Giàn giáo)")

    p_srv = sub.add_parser("serve", help="Khởi chạy máy chủ Web SPA FastAPI")
    p_srv.add_argument("--host", default=DEFAULT_API_HOST)
    p_srv.add_argument("--port", type=int, default=DEFAULT_API_PORT)
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "status":
        return cmd_status()
    if args.command == "import":
        return cmd_import(args.target)
    if args.command == "pace":
        return cmd_pace(args.days, args.minutes, args.scoring)
    if args.command == "bridge":
        return cmd_bridge(args.unit_code, complete=args.complete)
    if args.command == "errors":
        return cmd_errors()
    if args.command == "study":
        return cmd_study(args.unit, args.mode, args.limit, args.exam)
    if args.command == "serve":
        uvicorn.run("n3_mastery.api:app", host=args.host, port=args.port, reload=False)
        return 0
    return 1
