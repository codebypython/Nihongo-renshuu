"""Rich Terminal CLI for JLPT N3 10/10 Mastery System."""

import argparse
from datetime import datetime
import json
import secrets
import socket
import sqlite3
import sys
import threading
import time
import urllib.request
import webbrowser
from pathlib import Path
from typing import List, Optional

import uvicorn
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from n3_mastery.config import BASE_DIR, DEFAULT_API_HOST, DEFAULT_API_PORT, get_db_path, get_excel_dir
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
from n3_mastery.grammar_engine import (
    get_grammar_overview,
    get_grammar_point_detail,
    list_grammar_points,
    seed_grammar_and_foundation,
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
        gp_cnt = conn.execute("SELECT COUNT(*) FROM GRAMMAR_POINTS").fetchone()[0]
        qa_cnt = conn.execute("SELECT COUNT(*) FROM QUESTION_GRAMMAR_ANALYSES").fetchone()[0]
    finally:
        conn.close()
    if cnt == 0 and get_excel_dir().exists():
        import_all_excel(generate_variants=True)
    elif gp_cnt == 0 or qa_cnt < cnt:
        seed_grammar_and_foundation()


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


def cmd_grammar(level: Optional[str], exam_only: bool, search: Optional[str]) -> int:
    _ensure_seeded_if_empty()
    ov = get_grammar_overview()
    lvl_summary = " | ".join(
        f"{lb['level']}: {lb['mastered']}/{lb['total']}" for lb in ov.get("levels", [])
    )
    console.print(
        Panel(
            f"[bold]Tổng điểm ngữ pháp:[/bold] {ov['total_points']} "
            f"(Bộ đề .xlsx: {ov['exam_corpus_count']} | Mở rộng JLPT: {ov['jlpt_extension_count']})\n"
            f"[bold]Bài luyện ngữ pháp (Drills):[/bold] {ov['total_drills']} | "
            f"[bold]Từ vựng Nền tảng:[/bold] {ov['vocab_foundation_count']}\n"
            f"[bold]Phân bố JLPT:[/bold] {lvl_summary or 'Chưa có dữ liệu'}",
            title="THƯ VIỆN NGỮ PHÁP & LỘ TRÌNH JLPT (N5 -> N2)",
        )
    )

    pts = list_grammar_points(
        scope="exam" if exam_only else "all",
        level=level,
        q=search,
    )
    if not pts:
        console.print("[INFO] Không tìm thấy mẫu ngữ pháp phù hợp bộ lọc.")
        return 0

    table = Table(title=f"Danh sách Ngữ pháp ({len(pts)} mẫu)")
    table.add_column("Mã", style="bold")
    table.add_column("Cấp")
    table.add_column("Nguồn")
    table.add_column("Mẫu ngữ pháp")
    table.add_column("Nghĩa cốt lõi")
    table.add_column("FSRS")
    for p in pts:
        src_tag = "[THI]" if p["in_exam_corpus"] else "[JLPT]"
        fsrs = p["fsrs"]
        fsrs_tag = "[MASTERED]" if fsrs["mastered"] else fsrs["state"].upper()
        table.add_row(
            p["code"],
            p["jlpt_level"],
            src_tag,
            p["pattern"],
            p["core_meaning_vi"][:60],
            fsrs_tag,
        )
    console.print(table)
    return 0


def cmd_grammar_inspect(code: str) -> int:
    _ensure_seeded_if_empty()
    detail = get_grammar_point_detail(code)
    if detail is None:
        console.print(f"[FAIL] Không tìm thấy mẫu ngữ pháp '{code}'")
        return 1

    form_lines = "\n".join(
        f"  - {row.get('pos', '')}: {row.get('rule', '')}"
        for row in detail.get("formation_table", [])
    )
    pair_lines = "\n".join(
        f"  - Đối chiếu {cp.get('rival_pattern', '')}: {cp.get('difference_vi', '')} (Mẹo: {cp.get('quick_test_vi', '')})"
        for cp in detail.get("confusable_pairs", [])
    )
    ex_lines = "\n".join(
        f"  - {ex.get('jp', '')} -> {ex.get('vi', '')}"
        for ex in detail.get("examples", [])
    )
    q_lines = "\n".join(
        f"  - Q#{lq['question_id']} [{lq['unit_code']} {lq['mondai_type']} {lq['role']}]: {lq['note_vi']}"
        for lq in detail.get("linked_questions", [])
    )

    body = (
        f"[bold]Mẫu:[/bold] {detail['pattern']} ({detail['jlpt_level']} · {detail['category_label_vi']})\n"
        f"[bold]Phạm vi:[/bold] {'[THI CUỐI KÌ .xlsx]' if detail['in_exam_corpus'] else '[MỞ RỘNG JLPT]'} | "
        f"[bold]Văn phong:[/bold] {detail['register_tag']}\n"
        f"[bold]Công thức kết hợp:[/bold] {detail['formation_formula']}\n"
        f"{form_lines}\n\n"
        f"[bold]Nghĩa cốt lõi:[/bold] {detail['core_meaning_vi']}\n"
        f"[bold]Giải phẫu ngữ nghĩa & ngữ dụng:[/bold]\n{detail['deep_explanation_vi']}\n\n"
        f"[bold]Cặp dễ nhầm:[/bold]\n{pair_lines or '  (Không có)'}\n\n"
        f"[bold]Ví dụ chuẩn:[/bold]\n{ex_lines or '  (Không có)'}\n\n"
        f"[bold]Câu hỏi đề thi liên kết ({len(detail.get('linked_questions', []))}):[/bold]\n{q_lines or '  (Mẫu mở rộng JLPT ngoài bộ đề)'}"
    )
    console.print(Panel(body, title=f"BÀI HỌC NGỮ PHÁP 3 CHIỀU — {detail['code']}"))
    return 0


def _local_url(host: str, port: int) -> str:
    connect_host = "127.0.0.1" if host in ("0.0.0.0", "::", "") else host
    return f"http://{connect_host}:{port}"


def _is_mastery_server_running(host: str, port: int) -> bool:
    """Return True if an active instance of this app already answers /api/health."""
    url = f"{_local_url(host, port)}/api/health"
    try:
        with urllib.request.urlopen(url, timeout=1.5) as resp:
            if resp.status != 200:
                return False
            data = json.loads(resp.read().decode("utf-8"))
            return isinstance(data, dict) and data.get("status") in ("online", "ok") and "grammar_points" in data
    except Exception:
        return False


def _pick_available_port(host: str, preferred_port: int) -> int:
    """Return preferred_port if bindable, otherwise scan preferred_port+1..+20."""
    bind_host = host or "127.0.0.1"
    for port in range(preferred_port, preferred_port + 21):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.bind((bind_host, port))
                return port
            except OSError:
                continue
    return preferred_port


def _open_browser_when_ready(base_url: str, timeout: float = 15.0) -> None:
    """Poll /api/health in background and open default browser once ready."""
    deadline = time.time() + timeout
    health_url = f"{base_url}/api/health"
    while time.time() < deadline:
        try:
            with urllib.request.urlopen(health_url, timeout=1.0) as resp:
                if resp.status == 200:
                    webbrowser.open(base_url)
                    return
        except Exception:
            time.sleep(0.25)


def cmd_help_banner() -> int:
    """Print friendly Vietnamese quick-start guide when CLI is invoked without arguments."""
    console.print(
        Panel(
            "[bold]CÁCH MỞ NHANH GIAO DIỆN WEB (KHUYÊN DÙNG):[/bold]\n"
            "  • Nhấp đúp [bold]CHAY_NHANH_WEB.bat[/bold] (ở thư mục Language_Lab) hoặc [bold]start_web.bat[/bold]\n"
            "  • Hoặc gõ: [bold]py -3.11 n3_cli.py quickstart[/bold]\n\n"
            "[bold]CÁC LỆNH TIỆN ÍCH KHÁC:[/bold]\n"
            "  • [bold]doctor[/bold]           : Kiểm tra dữ liệu đề thi, ngữ pháp và cấu hình\n"
            "  • [bold]status[/bold]           : Xem điểm hiện tại và tiến độ 12 chủ đề\n"
            "  • [bold]grammar[/bold]          : Xem danh sách ngữ pháp N5->N2 và bài học\n"
            "  • [bold]study[/bold]            : Làm nhanh câu hỏi ngay trên terminal\n"
            "  • [bold]import[/bold]           : Nạp lại toàn bộ file đề Excel (.xlsx)\n"
            "  • [bold]backup[/bold]           : Sao lưu an toàn tiến độ học tập (.db)",
            title="HƯỚNG DẪN SỬ DỤNG CHƯƠNG TRÌNH ÔN THI TIẾNG NHẬT",
        )
    )
    return 0


def cmd_doctor() -> int:
    """Verify SQLite integrity, exam corpus counts, grammar corpus, and Excel source directory."""
    _ensure_seeded_if_empty()
    db_path = get_db_path()
    excel_dir = get_excel_dir()

    conn = get_connection(db_path)
    try:
        integrity = str(conn.execute("PRAGMA integrity_check").fetchone()[0])
        counts = {
            "QUESTIONS": conn.execute("SELECT COUNT(*) FROM QUESTIONS").fetchone()[0],
            "DOKKAI_PASSAGES": conn.execute("SELECT COUNT(*) FROM PASSAGES WHERE section='reading'").fetchone()[0],
            "VARIANT_DRILLS": conn.execute("SELECT COUNT(*) FROM VARIANT_DRILLS").fetchone()[0],
            "GRAMMAR_POINTS": conn.execute("SELECT COUNT(*) FROM GRAMMAR_POINTS").fetchone()[0],
            "GRAMMAR_DRILLS": conn.execute("SELECT COUNT(*) FROM GRAMMAR_DRILLS").fetchone()[0],
            "VOCAB_FOUNDATION": conn.execute("SELECT COUNT(*) FROM VOCAB_FOUNDATION").fetchone()[0],
            "ATTEMPT_LOGS": conn.execute("SELECT COUNT(*) FROM ATTEMPT_LOGS").fetchone()[0],
        }
    finally:
        conn.close()

    excel_exists = excel_dir.exists()
    xlsx_files = list(excel_dir.glob("*.xlsx")) if excel_exists else []
    healthy = integrity.lower() == "ok" and counts["QUESTIONS"] > 0

    table = Table(title="KIỂM TRA SỨC KHỎE HỆ THỐNG (DOCTOR)")
    table.add_column("Hạng mục")
    table.add_column("Trạng thái")
    table.add_column("Chi tiết")

    table.add_row("Cơ sở dữ liệu SQLite", "[OK]" if integrity.lower() == "ok" else "[FAIL]", f"{db_path} ({integrity})")
    table.add_row("Thư mục đề Excel", "[OK]" if excel_exists else "[WARN]", f"{excel_dir} ({len(xlsx_files)} file .xlsx)")
    table.add_row("Ngân hàng câu hỏi đề gốc", "[OK]" if counts["QUESTIONS"] > 0 else "[FAIL]", f"{counts['QUESTIONS']} câu | {counts['DOKKAI_PASSAGES']} bài đọc | {counts['VARIANT_DRILLS']} câu đổi dạng")
    table.add_row("Kho Ngữ pháp & Từ vựng", "[OK]" if counts["GRAMMAR_POINTS"] > 0 else "[WARN]", f"{counts['GRAMMAR_POINTS']} mẫu ngữ pháp | {counts['GRAMMAR_DRILLS']} bài tập | {counts['VOCAB_FOUNDATION']} từ vựng")
    table.add_row("Lịch sử làm bài đã lưu", "[OK]", f"{counts['ATTEMPT_LOGS']} lượt làm bài")
    console.print(table)
    return 0 if healthy else 1


def cmd_backup(output_dir: Optional[str] = None) -> int:
    """Create a hot SQLite backup copy in data/backups (or specified --dir)."""
    init_db()
    src_path = get_db_path()
    target_dir = Path(output_dir) if output_dir else (BASE_DIR / "data" / "backups")
    target_dir.mkdir(parents=True, exist_ok=True)

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest_path = target_dir / f"n3_mastery_backup_{stamp}.db"
    suffix = 1
    while dest_path.exists():
        dest_path = target_dir / f"n3_mastery_backup_{stamp}_{suffix}.db"
        suffix += 1

    src_conn = sqlite3.connect(str(src_path))
    try:
        dst_conn = sqlite3.connect(str(dest_path))
        try:
            src_conn.backup(dst_conn)
        finally:
            dst_conn.close()
        q_cnt = src_conn.execute("SELECT COUNT(*) FROM QUESTIONS").fetchone()[0]
        att_cnt = src_conn.execute("SELECT COUNT(*) FROM ATTEMPT_LOGS").fetchone()[0]
    finally:
        src_conn.close()

    console.print(
        Panel(
            f"[OK] Đã sao lưu an toàn dữ liệu học tập!\n"
            f"Tệp sao lưu: {dest_path}\n"
            f"Nội dung bảo toàn: {q_cnt} câu hỏi | {att_cnt} lượt làm bài.",
            title="SAO LƯU DỮ LIỆU THÀNH CÔNG",
        )
    )
    return 0


def cmd_quickstart(host: str, port: int, no_browser: bool) -> int:
    """Initialize DB if needed, reuse running server or pick free port, print guide, and launch browser."""
    _ensure_seeded_if_empty()

    if _is_mastery_server_running(host, port):
        url = _local_url(host, port)
        console.print(f"[OK] Chương trình đang chạy sẵn tại {url}")
        if not no_browser:
            webbrowser.open(url)
        return 0

    chosen_port = _pick_available_port(host, port)
    base_url = _local_url(host, chosen_port)

    conn = get_connection()
    try:
        q_cnt = conn.execute("SELECT COUNT(*) FROM QUESTIONS").fetchone()[0]
        gp_cnt = conn.execute("SELECT COUNT(*) FROM GRAMMAR_POINTS").fetchone()[0]
        vf_cnt = conn.execute("SELECT COUNT(*) FROM VOCAB_FOUNDATION").fetchone()[0]
    finally:
        conn.close()

    console.print(
        Panel(
            f"[bold]Địa chỉ Web App:[/bold] {base_url}\n"
            f"[bold]Kho học liệu sẵn sàng:[/bold] {q_cnt} câu đề Excel | {gp_cnt} mẫu ngữ pháp N5–N2 | {vf_cnt} từ vựng\n\n"
            "[bold]3 bước học nhanh trên trình duyệt:[/bold]\n"
            "  1. Mở tab [bold]Ngữ pháp & Từ vựng[/bold] để xem công thức và làm bài tập chia thể.\n"
            "  2. Mở tab [bold]Làm câu hỏi[/bold] để luyện đề và đọc phần giải thích sau mỗi câu.\n"
            "  3. Vào tab [bold]Thi thử[/bold] để kiểm tra năng lực thực tế như thi thật.\n\n"
            "Nhấn [bold]Ctrl + C[/bold] tại cửa sổ này khi bạn muốn tắt máy chủ.",
            title="KHỞI CHẠY NHANH ÔN THI TIẾNG NHẬT",
        )
    )

    if not no_browser:
        threading.Thread(
            target=_open_browser_when_ready,
            args=(base_url,),
            daemon=True,
        ).start()

    uvicorn.run("n3_mastery.api:app", host=host, port=chosen_port, reload=False)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="n3_cli.py",
        description="JLPT N3 10/10 Mastery System CLI",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_qs = sub.add_parser("quickstart", help="Kiểm tra dữ liệu, khởi chạy Web App và tự mở trình duyệt")
    p_qs.add_argument("--host", default=DEFAULT_API_HOST)
    p_qs.add_argument("--port", type=int, default=8000)
    p_qs.add_argument("--no-browser", action="store_true", help="Không tự động mở trình duyệt")

    sub.add_parser("doctor", help="Kiểm tra sức khỏe cơ sở dữ liệu và bộ đề Excel")

    p_bk = sub.add_parser("backup", help="Sao lưu an toàn cơ sở dữ liệu tiến độ học (.db)")
    p_bk.add_argument("--dir", default=None, help="Thư mục lưu file sao lưu")

    sub.add_parser("status", help="Xem Bảng điểm Kép /10, lịch học và tiến độ 12 chủ đề")

    p_imp = sub.add_parser("import", help="Nạp dữ liệu từ tệp .xlsx hoặc thư mục Excel")
    p_imp.add_argument("target", nargs="?", default=None, help="Đường dẫn file .xlsx hoặc thư mục")

    p_pace = sub.add_parser("pace", help="Cập nhật ngày thi còn lại, phút học/ngày và chế độ điểm")
    p_pace.add_argument("--days", type=int, default=None)
    p_pace.add_argument("--minutes", type=int, default=None)
    p_pace.add_argument("--scoring", choices=["jlpt_weighted", "equal_weighted"], default=None)

    p_bridge = sub.add_parser("bridge", help="Xem bài học Trạm Bắc cầu N4->N3 của một chủ đề")
    p_bridge.add_argument("unit_code", help="Ví dụ: MU-01")
    p_bridge.add_argument("--complete", action="store_true", help="Đánh dấu hoàn thành trạm bắc cầu")

    sub.add_parser("errors", help="Xem Sổ tay câu hay sai")

    p_study = sub.add_parser("study", help="Luyện tập tương tác trên terminal")
    p_study.add_argument("--unit", default=None, help="Mã chủ đề (vd: MU-01)")
    p_study.add_argument("--mode", default="mixed", choices=["mixed", "original", "variant", "remediation"])
    p_study.add_argument("--limit", type=int, default=5)
    p_study.add_argument("--exam", action="store_true", help="Bật chế độ Thi thử (khóa gợi ý)")

    p_gram = sub.add_parser("grammar", help="Xem thư viện Ngữ pháp & lộ trình JLPT N5->N2")
    p_gram.add_argument("--level", default=None, choices=["N5", "N4", "N3", "N2", "N1"])
    p_gram.add_argument("--exam-only", action="store_true", help="Chỉ hiển thị mẫu có trong bộ đề .xlsx")
    p_gram.add_argument("--search", default=None, help="Tìm kiếm theo mã, mẫu hoặc nghĩa")

    p_gi = sub.add_parser("grammar-inspect", help="Xem chi tiết 3 chiều và câu đề liên kết của một mẫu ngữ pháp")
    p_gi.add_argument("code", help="Ví dụ: GP-N3-001")

    p_srv = sub.add_parser("serve", help="Khởi chạy máy chủ Web SPA FastAPI")
    p_srv.add_argument("--host", default=DEFAULT_API_HOST)
    p_srv.add_argument("--port", type=int, default=DEFAULT_API_PORT)
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    effective_argv = sys.argv[1:] if argv is None else list(argv)
    if len(effective_argv) == 0:
        return cmd_help_banner()

    parser = build_parser()
    args = parser.parse_args(effective_argv)
    if args.command == "quickstart":
        return cmd_quickstart(args.host, args.port, args.no_browser)
    if args.command == "doctor":
        return cmd_doctor()
    if args.command == "backup":
        return cmd_backup(args.dir)
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
    if args.command == "grammar":
        return cmd_grammar(args.level, args.exam_only, args.search)
    if args.command == "grammar-inspect":
        return cmd_grammar_inspect(args.code)
    if args.command == "serve":
        uvicorn.run("n3_mastery.api:app", host=args.host, port=args.port, reload=False)
        return 0
    return 1
