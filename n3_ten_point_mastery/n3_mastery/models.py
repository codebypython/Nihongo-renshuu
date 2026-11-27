"""Pydantic v2 models and enums for JLPT N3 10/10 Mastery System."""

from enum import Enum
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class Section(str, Enum):
    VOCAB = "vocab"
    GRAMMAR = "grammar"
    READING = "reading"


class ScoringMode(str, Enum):
    JLPT_WEIGHTED = "jlpt_weighted"
    EQUAL_WEIGHTED = "equal_weighted"


class FSRSStateName(str, Enum):
    NEW = "new"
    LEARNING = "learning"
    REVIEW = "review"
    RELEARNING = "relearning"


class VariantMode(str, Enum):
    DISTRACTOR_INVERT = "distractor_invert"
    ERROR_DIAGNOSIS = "error_diagnosis"
    STAR_4SLOT_SHIFT = "star_4slot_shift"
    DOKKAI_EVIDENCE = "dokkai_evidence"
    CONDITION_SHIFT = "condition_shift"


class Rating(int, Enum):
    AGAIN = 1
    HARD = 2
    GOOD = 3
    EASY = 4


class PaceSettings(BaseModel):
    days_remaining: int = Field(default=14, ge=1, le=365)
    daily_minutes: int = Field(default=60, ge=5, le=720)
    scoring_mode: ScoringMode = ScoringMode.JLPT_WEIGHTED


class PaceFeasibility(BaseModel):
    days_remaining: int
    daily_minutes: int
    available_budget_minutes: float
    remaining_workload_minutes: float
    required_minutes_per_day: float
    is_feasible: bool
    shortfall_minutes_per_day: float
    new_units_per_day: float
    questions_per_day: float
    variants_per_day: float
    horizon_cap_days: float
    warning_message: Optional[str] = None
    status_tag: str


class SectionReadiness(BaseModel):
    section: str
    label_vi: str
    weight_10: float
    total_questions: int
    attempted_original: int
    correct_original: int
    variant_passed_count: int
    mastered_count: int
    original_score_10: float
    mastery_score_10: float


class DualReadinessReport(BaseModel):
    scoring_mode: ScoringMode
    original_score_10: float
    mastery_score_10: float
    rote_gap_10: float
    total_questions: int
    attempted_count: int
    mastered_count: int
    mastered_percent: float
    sections: List[SectionReadiness]
    honest_verdict: str


class SessionSubmitRequest(BaseModel):
    question_id: int
    variant_id: Optional[int] = None
    mode: str = "original"  # original | variant | remediation | exam
    selected_index: Optional[int] = None
    slot_order: Optional[List[int]] = None
    evidence_indices: Optional[List[int]] = None
    used_hint: bool = False
    response_sec: float = Field(default=0.0, ge=0.0)
    session_seed: str = "default"
    exam_mode: bool = False


class SessionHintRequest(BaseModel):
    question_id: int
    variant_id: Optional[int] = None
    exam_mode: bool = False


class RatingOverrideRequest(BaseModel):
    question_id: int
    rating: Rating
    used_hint: bool = False


class BridgeCompleteRequest(BaseModel):
    quick_check_answers: Optional[List[int]] = None


class ExamAnswerItem(BaseModel):
    question_id: int
    selected_index: Optional[int] = None
    slot_order: Optional[List[int]] = None
    evidence_indices: Optional[List[int]] = None
    session_seed: str = "exam"


class ExamSubmitRequest(BaseModel):
    exam_mode: str = "mini_mock"
    answers: List[ExamAnswerItem]
    duration_sec: float = 0.0
