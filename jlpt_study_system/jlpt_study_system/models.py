"""Data models for JLPT N3 Study System."""

from datetime import datetime
from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class CardCategory(str, Enum):
    GRAMMAR = "grammar"
    VOCAB = "vocab"
    READING_SIGNAL = "reading_signal"
    LISTENING_REFLEX = "listening_reflex"


class Rating(int, Enum):
    AGAIN = 1
    HARD = 2
    GOOD = 3
    EASY = 4


class CardState(str, Enum):
    NEW = "New"
    LEARNING = "Learning"
    REVIEW = "Review"
    RELEARNING = "Relearning"


class DrillType(str, Enum):
    CHOUKAI_REFLEX = "choukai_reflex"
    DOKKAI_DECODER = "dokkai_decoder"
    MINI_MOCK = "mini_mock"


class SectionName(str, Enum):
    GENGO = "Language Knowledge"
    READING = "Reading"
    LISTENING = "Listening"


class Card(BaseModel):
    id: Optional[int] = None
    category: CardCategory
    front: str
    back: str
    trap: str = ""
    example: str = ""
    tags: str = ""
    created_at: Optional[datetime] = None


class FSRSState(BaseModel):
    card_id: int
    stability: float = 2.0
    difficulty: float = 5.0
    reps: int = 0
    lapses: int = 0
    state: CardState = CardState.NEW
    last_review: Optional[datetime] = None
    due_date: Optional[datetime] = None
    scheduled_days: int = 0


class CardWithState(BaseModel):
    card: Card
    fsrs: FSRSState


class ReviewSubmission(BaseModel):
    card_id: int
    rating: Rating
    elapsed_seconds: float = 0.0


class DrillItem(BaseModel):
    id: Optional[int] = None
    drill_type: DrillType
    section: str
    prompt: str
    context: str = ""
    options: List[str]
    correct_index: int
    trap_analysis: str = ""


class DrillSubmission(BaseModel):
    item_id: int
    selected_index: int
    response_time_sec: float = 0.0


class DrillResult(BaseModel):
    is_correct: bool
    selected_index: int
    correct_index: int
    correct_answer: str
    explanation: str
    trap_analysis: str
    logged_to_error_notebook: bool


class ErrorItem(BaseModel):
    id: Optional[int] = None
    item_type: str
    item_id: Optional[int] = None
    prompt: str
    user_answer: str
    correct_answer: str
    trap_analysis: str
    remediated: bool = False
    attempt_count: int = 1
    created_at: Optional[datetime] = None
    remediated_at: Optional[datetime] = None


class CurriculumBlock(BaseModel):
    id: Optional[int] = None
    day_number: int
    block_name: str
    title: str
    planned_minutes: int = 50
    completed_minutes: int = 0
    is_completed: bool = False
    notes: str = ""
    completed_at: Optional[datetime] = None


class PomodoroSession(BaseModel):
    id: Optional[int] = None
    day_number: int
    block_index: int = 1
    task_label: str
    duration_minutes: int = 50
    status: str = "completed"
    created_at: Optional[datetime] = None


class SectionReadiness(BaseModel):
    section_name: SectionName
    score: float
    max_score: float = 60.0
    cutoff: float = 19.0
    pass_cutoff: bool
    mastery_ratio: float
    retention_rate: float
    sample_count: int
    status_label: str


class ReadinessReport(BaseModel):
    total_score: float
    max_total_score: float = 180.0
    pass_total: bool
    gengo: SectionReadiness
    reading: SectionReadiness
    listening: SectionReadiness
    at_risk_sections: List[str]
    pass_status: str  # PASS, AT_RISK, FAIL
    critical_recommendations: List[str]
    generated_at: datetime = Field(default_factory=datetime.now)
