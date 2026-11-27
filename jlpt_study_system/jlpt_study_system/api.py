"""FastAPI REST application for the JLPT N3 Study System."""

from contextlib import asynccontextmanager
from pathlib import Path
from typing import Dict, List, Optional, Any

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from jlpt_study_system import __version__
from jlpt_study_system.config import BASE_DIR, DEFAULT_DB_PATH
from jlpt_study_system.database import init_db
from jlpt_study_system.models import (
    CardCategory,
    CardWithState,
    DrillItem,
    DrillResult,
    DrillSubmission,
    DrillType,
    ErrorItem,
    Rating,
    ReadinessReport,
    ReviewSubmission,
)
from jlpt_study_system.importer import import_all
from jlpt_study_system.fsrs_scheduler import (
    get_due_cards,
    process_card_review,
    get_card_stats,
)
from jlpt_study_system.curriculum import (
    get_curriculum_day,
    complete_curriculum_block,
    log_pomodoro_session,
    get_pomodoro_summary,
    get_sprint_overview,
    get_adaptive_schedule_advice,
)
from jlpt_study_system.error_notebook import (
    get_error_items,
    remediate_error_item,
    get_error_notebook_stats,
)
from jlpt_study_system.quiz_engine import (
    get_drill_items_by_type,
    submit_drill_answer,
    generate_mini_mock_quiz,
    get_drill_performance_summary,
)
from jlpt_study_system.readiness import calculate_sectional_readiness


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Ensure database schema is initialized and seeded on startup."""
    init_db()
    stats = get_card_stats()
    if stats["total_cards"] == 0:
        import_all()
    yield


app = FastAPI(
    title="JLPT N3 Sprint Study System",
    description="High-yield triage study platform with FSRS scheduler, Pomodoro block manager, and interactive drill engine.",
    version=__version__,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static directory if it exists
STATIC_DIR = Path(__file__).resolve().parent / "static"
if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"


# Request / Response Schemas for API
class CompleteBlockRequest(BaseModel):
    completed_minutes: Optional[int] = None
    notes: Optional[str] = None
    is_completed: bool = True


class PomodoroLogRequest(BaseModel):
    day_number: int
    block_index: int = 1
    task_label: str
    duration_minutes: int = 50
    status: str = "completed"


class RemediateRequest(BaseModel):
    success: bool = True




# --- Health & Maintenance ---
@app.get("/api/health")
def get_health() -> Dict[str, Any]:
    stats = get_card_stats()
    return {
        "status": "online",
        "version": __version__,
        "database": str(DEFAULT_DB_PATH),
        "total_cards": stats["total_cards"],
    }


@app.post("/api/seed")
def post_seed_database() -> Dict[str, Any]:
    res = import_all()
    return {"message": "Database successfully initialized and seeded.", "counts": res}


# --- Spaced Repetition (FSRS) Endpoints ---
@app.get("/api/cards/due", response_model=List[CardWithState])
def get_cards_due(
    limit: int = Query(50, ge=1, le=200),
    category: Optional[CardCategory] = None,
):
    return get_due_cards(limit=limit, category=category)


@app.get("/api/cards/stats")
def get_deck_stats():
    return get_card_stats()


@app.post("/api/cards/review")
def post_card_review(submission: ReviewSubmission):
    try:
        updated, logged = process_card_review(
            card_id=submission.card_id,
            rating=submission.rating,
            elapsed_seconds=submission.elapsed_seconds,
        )
        return {
            "card_with_state": updated,
            "logged_to_error_notebook": logged,
            "message": f"Review recorded with rating {submission.rating.name}.",
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# --- Curriculum & Pomodoro Endpoints ---
@app.get("/api/curriculum/day/{day_number}")
def get_day_plan(day_number: int):
    if day_number < 1 or day_number > 7:
        raise HTTPException(status_code=400, detail="Day number must be between 1 and 7.")
    return get_curriculum_day(day_number)


@app.get("/api/curriculum/sprint")
def get_sprint_overview_api():
    return get_sprint_overview()


@app.post("/api/curriculum/block/{block_id}/complete")
def post_complete_block(block_id: int, req: CompleteBlockRequest):
    try:
        block = complete_curriculum_block(
            block_id=block_id,
            completed_minutes=req.completed_minutes,
            notes=req.notes,
            is_completed=req.is_completed,
        )
        return block
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.get("/api/curriculum/advice/{day_number}")
def get_advice(day_number: int):
    advice = get_adaptive_schedule_advice(current_day=day_number)
    return {"day_number": day_number, "recommendations": advice}


@app.post("/api/pomodoro/session")
def post_pomodoro_session(req: PomodoroLogRequest):
    session = log_pomodoro_session(
        day_number=req.day_number,
        block_index=req.block_index,
        task_label=req.task_label,
        duration_minutes=req.duration_minutes,
        status=req.status,
    )
    return session


@app.get("/api/pomodoro/summary")
def get_pomo_summary(day_number: Optional[int] = None):
    return get_pomodoro_summary(day_number=day_number)


# --- Interactive Drill & Quiz Endpoints ---
@app.get("/api/drills/choukai", response_model=List[DrillItem])
def get_choukai_drills(count: int = Query(5, ge=1, le=25)):
    return get_drill_items_by_type(DrillType.CHOUKAI_REFLEX, count=count)


@app.get("/api/drills/dokkai", response_model=List[DrillItem])
def get_dokkai_drills(count: int = Query(5, ge=1, le=25)):
    return get_drill_items_by_type(DrillType.DOKKAI_DECODER, count=count)


@app.get("/api/drills/mock")
def get_mock_quiz(count_per_section: int = Query(3, ge=1, le=10)):
    return generate_mini_mock_quiz(count_per_section=count_per_section)


@app.post("/api/drills/submit", response_model=DrillResult)
def post_drill_answer(submission: DrillSubmission):
    try:
        return submit_drill_answer(
            drill_item_id=submission.item_id,
            selected_index=submission.selected_index,
            response_time_sec=submission.response_time_sec,
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.get("/api/drills/performance")
def get_drill_performance():
    return get_drill_performance_summary()


# --- Error Notebook Endpoints ---
@app.get("/api/error-notebook", response_model=List[ErrorItem])
def get_errors(
    remediated: Optional[bool] = None,
    item_type: Optional[str] = None,
    limit: int = Query(100, ge=1, le=500),
):
    return get_error_items(remediated=remediated, item_type=item_type, limit=limit)


@app.get("/api/error-notebook/stats")
def get_errors_stats():
    return get_error_notebook_stats()


@app.post("/api/error-notebook/{error_id}/remediate", response_model=ErrorItem)
def post_remediate_error(error_id: int, req: RemediateRequest):
    try:
        return remediate_error_item(error_id=error_id, success=req.success)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# --- Sectional Readiness & Score Projection ---
@app.get("/api/readiness", response_model=ReadinessReport)
def get_readiness():
    return calculate_sectional_readiness()


# --- Web UI Single Page Application Root ---
@app.get("/", response_class=HTMLResponse)
def get_ui():
    index_file = TEMPLATES_DIR / "index.html"
    if index_file.exists():
        return HTMLResponse(content=index_file.read_text(encoding="utf-8"))
    return HTMLResponse("<h1>JLPT N3 Study System API</h1><p>Visit /docs for API schema.</p>")
