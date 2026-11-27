"""Rich CLI interface for JLPT N3 Study System."""

import argparse
import sys
import time
from typing import Optional

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn

from jlpt_study_system.importer import import_all
from jlpt_study_system.database import init_db
from jlpt_study_system.fsrs_scheduler import get_due_cards, process_card_review, get_card_stats
from jlpt_study_system.models import Rating, DrillType
from jlpt_study_system.quiz_engine import get_drill_items_by_type, submit_drill_answer
from jlpt_study_system.error_notebook import get_error_items, remediate_error_item, get_error_notebook_stats
from jlpt_study_system.readiness import calculate_sectional_readiness
from jlpt_study_system.curriculum import get_curriculum_day, log_pomodoro_session


console = Console()


def cmd_init():
    """Seed and initialize database."""
    console.print("[bold cyan][SYSTEM][/bold cyan] Initializing SQLite database and importing assets...")
    counts = import_all()
    console.print("[bold green][OK][/bold green] Database seeded successfully:")
    for k, v in counts.items():
        console.print(f"  - {k}: [bold]{v}[/bold]")


def cmd_status():
    """Display overall executive readiness report and score projections."""
    init_db()
    readiness = calculate_sectional_readiness()
    deck_stats = get_card_stats()
    error_stats = get_error_notebook_stats()

    # Hero projection panel
    color = "green" if readiness.pass_status == "PASS" else ("yellow" if readiness.pass_status == "AT_RISK" else "red")
    console.print()
    console.print(
        Panel.fit(
            f"[bold {color}]PROJECTED SCORE: {readiness.total_score} / 180.0[/bold {color}]\n"
            f"Pass Status: [bold {color}][{readiness.pass_status}][/bold {color}] (Passing Threshold: >= 95.0, Cutoff: >= 19.0)",
            title="[bold]JLPT N3 SPRINT READINESS PROJECTION[/bold]",
            border_style=color,
        )
    )

    # Section Cutoff Table
    table = Table(title="Sectional Readiness & Cutoff Safeguards", border_style="dim")
    table.add_column("Section", style="cyan")
    table.add_column("Projected Score", justify="right", style="bold")
    table.add_column("Section Cutoff", justify="right")
    table.add_column("Cutoff Status", justify="center")
    table.add_column("Sample Count", justify="right")

    for sec in [readiness.gengo, readiness.reading, readiness.listening]:
        st_color = "green" if sec.pass_cutoff else "red"
        st_text = f"[{st_color}][VƯỢT SÀN][/{st_color}]" if sec.pass_cutoff else f"[{st_color}][NGUY CƠ LIỆT][/{st_color}]"
        table.add_row(
            sec.section_name.value,
            f"{sec.score:.1f} / 60",
            ">= 19.0",
            st_text,
            str(sec.sample_count),
        )
    console.print(table)

    # Triage recommendations
    console.print("\n[bold cyan][PARETO 80/20 STRATEGIC RECOMMENDATIONS][/bold cyan]")
    for rec in readiness.critical_recommendations:
        console.print(f"  • {rec}")

    # Summary table
    console.print(
        f"\n[dim]Deck Total: {deck_stats['total_cards']} cards | Reviews: {deck_stats['total_reviews']} | Retention: {deck_stats['retention_rate_pct']}% | Active Traps: {error_stats['unresolved_errors']}[/dim]\n"
    )


def cmd_study(limit: int = 20, category: Optional[str] = None):
    """Interactive Spaced Repetition flashcard review session."""
    init_db()
    due = get_due_cards(limit=limit, category=category)
    if not due:
        console.print("[bold green][OK][/bold green] All due flashcards reviewed! Outstanding work.")
        return

    console.print(f"[bold cyan][STUDY SESSION][/bold cyan] {len(due)} cards in queue. Let's begin.")
    reviewed_count = 0

    for item in due:
        card = item.card
        fsrs = item.fsrs

        console.clear()
        console.print(f"[bold cyan]CARD {reviewed_count + 1} / {len(due)}[/bold cyan] [dim][{card.category.value.upper()}] (State: {fsrs.state.value})[/dim]")
        console.print()
        console.print(
            Panel(
                f"[bold white]{card.front}[/bold white]",
                title="[bold]PROMPT (FRONT)[/bold]",
                border_style="cyan",
            )
        )

        input("\n[Press ENTER to flip card and verify answer] ")

        # Back display
        back_text = f"[bold white]{card.back}[/bold white]"
        if card.trap:
            back_text += f"\n\n[bold red][BẪY TRẮC NGHIỆM][/bold red]\n{card.trap}"
        if card.example:
            back_text += f"\n\n[bold cyan][VÍ DỤ][/bold cyan]\n{card.example}"

        console.print(
            Panel(
                back_text,
                title="[bold]EXPLANATION & TRAP (BACK)[/bold]",
                border_style="green",
            )
        )

        console.print("\nSelect your recall grade:")
        console.print("  [bold red][1] AGAIN[/bold red] (Forgot / 10m lapse)")
        console.print("  [bold yellow][2] HARD[/bold yellow] (Hesitant / 1 day)")
        console.print("  [bold green][3] GOOD[/bold green] (Solid / 2-3 days)")
        console.print("  [bold blue][4] EASY[/bold blue] (Instant reflex / 4-5 days)")
        console.print("  [dim][q] Quit session[/dim]")

        choice = Prompt.ask("Your grade", choices=["1", "2", "3", "4", "q"], default="3")
        if choice == "q":
            break

        rating = Rating(int(choice))
        process_card_review(card_id=card.id, rating=rating)
        reviewed_count += 1

    console.print(f"\n[bold green][OK][/bold green] Session completed: Reviewed {reviewed_count} cards.")


def cmd_drill(drill_type_str: str = "choukai"):
    """Run interactive Choukai reflex or Dokkai decoder drill."""
    init_db()
    dtype = DrillType.CHOUKAI_REFLEX if drill_type_str == "choukai" else DrillType.DOKKAI_DECODER
    items = get_drill_items_by_type(dtype, count=5)

    if not items:
        console.print("[bold red][FAIL][/bold red] No drill items found. Please run init first.")
        return

    console.print(f"[bold cyan][INTERACTIVE DRILL][/bold cyan] {dtype.value.upper()} (5 questions)\n")
    correct_count = 0

    for i, item in enumerate(items, 1):
        console.print(f"[bold cyan]QUESTION {i} / {len(items)}[/bold cyan] [dim]{item.context}[/dim]")
        console.print(Panel(item.prompt, border_style="cyan"))

        for idx, opt in enumerate(item.options):
            console.print(f"  [bold][{idx + 1}][/bold] {opt}")

        start_time = time.time()
        ans_str = Prompt.ask(
            "Select option (or 'q' to quit)",
            choices=[str(x + 1) for x in range(len(item.options))] + ["q"],
            default="1",
        )
        if ans_str == "q":
            break
        elapsed = time.time() - start_time
        selected_idx = int(ans_str) - 1

        result = submit_drill_answer(
            drill_item_id=item.id,
            selected_index=selected_idx,
            response_time_sec=elapsed,
        )

        if result.is_correct:
            console.print(f"[bold green][CHÍNH XÁC][/bold green] (Phản xạ: {elapsed:.1f}s)")
            correct_count += 1
        else:
            console.print(f"[bold red][BẪY TRẮC NGHIỆM][/bold red] (Đáp án đúng: [{result.correct_index + 1}] {result.correct_answer})")
            if result.trap_analysis:
                console.print(f"[yellow]{result.trap_analysis}[/yellow]")
            console.print("[dim]=> Đã tự động ghi nhận vào Sổ tay bẫy trắc nghiệm.[/dim]")
        console.print("-" * 50)

    console.print(f"\n[bold]DRILL RESULT:[/bold] {correct_count} / {len(items)} correct ({round(correct_count / len(items) * 100, 1)}%)")


def cmd_errors():
    """Review items in Error Notebook."""
    init_db()
    errors = get_error_items(remediated=False)
    if not errors:
        console.print("[bold green][OK][/bold green] No active unresolved errors in the Error Notebook.")
        return

    table = Table(title="Error Notebook (Bẫy trắc nghiệm tồn đọng)", border_style="red")
    table.add_column("ID", justify="right", style="dim")
    table.add_column("Type", style="cyan")
    table.add_column("Prompt", style="white")
    table.add_column("Trap / Solution", style="yellow")
    table.add_column("Attempts", justify="center")

    for err in errors[:15]:
        table.add_row(
            str(err.id),
            err.item_type,
            err.prompt[:40] + ("..." if len(err.prompt) > 40 else ""),
            err.trap_analysis[:50] + ("..." if len(err.trap_analysis) > 50 else ""),
            str(err.attempt_count),
        )
    console.print(table)


def cmd_pomodoro(minutes: int = 50, day: int = 1):
    """Run an interactive 50-minute Pomodoro study block with live progress."""
    init_db()
    task = Prompt.ask("Task label for this block", default="Ngữ pháp Tier 1 & Discourse Drills")
    total_seconds = minutes * 60

    console.print(f"\n[bold cyan][POMODORO][/bold cyan] Starting {minutes}-minute focus block: [bold]{task}[/bold]")
    console.print("[dim]Press Ctrl+C to interrupt if needed.[/dim]\n")

    try:
        with Progress(
            TextColumn("[bold blue]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeRemainingColumn(),
        ) as progress:
            task_prog = progress.add_task(f"[cyan]{task}", total=total_seconds)
            for _ in range(total_seconds):
                time.sleep(1)
                progress.update(task_prog, advance=1)

        log_pomodoro_session(day_number=day, block_index=1, task_label=task, duration_minutes=minutes)
        console.print("\n[bold green][HOÀN THÀNH][/bold green] 50 phút tập trung cao độ kết thúc! Hãy nghỉ 10 phút.")
    except KeyboardInterrupt:
        console.print("\n[yellow][TẠM DỪNG][/yellow] Pomodoro bị ngắt quãng.")


def cmd_serve(port: int = 8000, host: str = "127.0.0.1"):
    """Start FastAPI uvicorn server."""
    import uvicorn
    console.print(f"[bold cyan][SERVER][/bold cyan] Launching JLPT N3 Study System on http://{host}:{port} ...")
    uvicorn.run("jlpt_study_system.api:app", host=host, port=port, reload=False)


def main():
    parser = argparse.ArgumentParser(description="JLPT N3 Sprint Study System CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("init", help="Seed database from sprint reference assets")
    subparsers.add_parser("status", help="Display readiness report and score projections")

    study_p = subparsers.add_parser("study", help="Interactive flashcard spaced repetition session")
    study_p.add_argument("--limit", type=int, default=20)
    study_p.add_argument("--category", type=str, default=None)

    drill_p = subparsers.add_parser("drill", help="Interactive drill testing")
    drill_p.add_argument("type", choices=["choukai", "dokkai"], default="choukai", nargs="?")

    subparsers.add_parser("errors", help="View active Error Notebook items")

    pomo_p = subparsers.add_parser("pomodoro", help="Start 50-minute Pomodoro study block")
    pomo_p.add_argument("--minutes", type=int, default=50)
    pomo_p.add_argument("--day", type=int, default=1)

    serve_p = subparsers.add_parser("serve", help="Start FastAPI web server")
    serve_p.add_argument("--port", type=int, default=8000)
    serve_p.add_argument("--host", type=str, default="127.0.0.1")

    args = parser.parse_args()

    if args.command == "init":
        cmd_init()
    elif args.command == "status":
        cmd_status()
    elif args.command == "study":
        cmd_study(limit=args.limit, category=args.category)
    elif args.command == "drill":
        cmd_drill(args.type)
    elif args.command == "errors":
        cmd_errors()
    elif args.command == "pomodoro":
        cmd_pomodoro(minutes=args.minutes, day=args.day)
    elif args.command == "serve":
        cmd_serve(port=args.port, host=args.host)
    else:
        cmd_status()


if __name__ == "__main__":
    main()
