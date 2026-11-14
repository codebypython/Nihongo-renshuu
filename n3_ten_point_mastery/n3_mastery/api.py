"""FastAPI REST Backend & Single-Page App Server for JLPT N3 10/10 Mastery System."""

import json
import secrets
import tempfile
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any, Dict, List, Optional

from fastapi import FastAPI, File, HTTPException, Query, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles

from n3_mastery import __version__
from n3_mastery.config import get_db_path, get_excel_dir
from n3_mastery.database import get_connection, init_db, transaction
from n3_mastery.drill_engine import (
    get_error_notebook,
    get_next_study_candidate,
    get_study_item,
    submit_answer,
)
from n3_mastery.fsrs_adaptive import (
    apply_fsrs_update,
    compute_pace_feasibility,
    get_pace_settings,
    update_pace_settings,
)
from n3_mastery.grammar_engine import (
    get_grammar_categories,
    get_grammar_overview,
    get_grammar_point_detail,
    get_next_grammar_drill,
    import_jlpt_grammar_pack,
    list_grammar_points,
    list_vocab_foundation,
    seed_grammar_and_foundation,
    submit_grammar_drill,
)
from n3_mastery.importer import import_all_excel, import_excel_file
from n3_mastery.models import (
    BridgeCompleteRequest,
    ExamSubmitRequest,
    GrammarDrillSubmitRequest,
    PaceSettings,
    RatingOverrideRequest,
    SessionHintRequest,
    SessionSubmitRequest,
)
from n3_mastery.readiness import calculate_dual_readiness, is_question_mastered
from n3_mastery.scaffolding import get_contextual_hint

STATIC_DIR = Path(__file__).resolve().parent / "static"
TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    conn = get_connection()
    try:
        q_count = conn.execute("SELECT COUNT(*) FROM QUESTIONS").fetchone()[0]
        gp_count = conn.execute("SELECT COUNT(*) FROM GRAMMAR_POINTS").fetchone()[0]
        qa_count = conn.execute("SELECT COUNT(*) FROM QUESTION_GRAMMAR_ANALYSES").fetchone()[0]
    finally:
        conn.close()
    if q_count == 0 and get_excel_dir().exists():
        import_all_excel(generate_variants=True)
    elif gp_count == 0 or qa_count < q_count:
        seed_grammar_and_foundation()
    yield


app = FastAPI(
    title="JLPT N3 10/10 Mastery System",
    description="Hệ thống Luyện thi Chinh phục 10/10 JLPT N3 — Chống học vẹt, Bắc cầu N4->N3 & Giàn giáo 3 cấp.",
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

if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


def _get_units_overview() -> List[Dict[str, Any]]:
    conn = get_connection()
    try:
        units = conn.execute(
            """
            SELECT u.*, b.grammar_focus, b.completed AS bridge_completed
            FROM MICRO_UNITS u
            LEFT JOIN N4_BRIDGE_CAPSULES b ON b.unit_code = u.code
            ORDER BY u.order_index
            """
        ).fetchall()
        q_rows = conn.execute(
            """
            SELECT q.id, q.unit_code, f.state, f.clean_original_passed, f.variant_passed,
                   f.spaced_clean_sessions,
                   (SELECT a.is_correct FROM ATTEMPT_LOGS a WHERE a.question_id=q.id ORDER BY a.id DESC LIMIT 1) AS latest_overall_correct
            FROM QUESTIONS q
            JOIN FSRS_STATES f ON f.question_id = q.id
            """
        ).fetchall()
    finally:
        conn.close()

    by_unit: Dict[str, List[Dict[str, Any]]] = {}
    for qr in q_rows:
        by_unit.setdefault(qr["unit_code"], []).append(dict(qr))

    result: List[Dict[str, Any]] = []
    for u in units:
        items = by_unit.get(u["code"], [])
        total = len(items)
        clean_orig = sum(1 for x in items if int(x["clean_original_passed"]) == 1)
        var_pass = sum(1 for x in items if int(x["variant_passed"]) >= 1)
        relearning = sum(1 for x in items if x["state"] == "relearning")
        mastered = sum(1 for x in items if is_question_mastered(x))
        result.append(
            {
                "code": u["code"],
                "order_index": int(u["order_index"]),
                "title": u["title"],
                "section": u["section"],
                "target_skill": u["target_skill"],
                "estimated_minutes": int(u["estimated_minutes"]),
                "grammar_focus": u["grammar_focus"] or "",
                "bridge_completed": bool(u["bridge_completed"]),
                "total_questions": total,
                "clean_original_count": clean_orig,
                "variant_passed_count": var_pass,
                "mastered_count": mastered,
                "relearning_count": relearning,
            }
        )
    return result


@app.get("/", response_class=HTMLResponse)
def get_root_spa():
    index_path = TEMPLATES_DIR / "index.html"
    if not index_path.exists():
        return HTMLResponse("<h1>JLPT N3 10/10 Mastery API</h1>", status_code=200)
    return HTMLResponse(index_path.read_text(encoding="utf-8"))


@app.get("/favicon.ico", include_in_schema=False)
def get_favicon():
    return Response(status_code=204)


@app.get("/api/health")
def get_health() -> Dict[str, Any]:
    conn = get_connection()
    try:
        q_cnt = conn.execute("SELECT COUNT(*) FROM QUESTIONS").fetchone()[0]
        v_cnt = conn.execute("SELECT COUNT(*) FROM VARIANT_DRILLS").fetchone()[0]
        p_cnt = conn.execute("SELECT COUNT(*) FROM PASSAGES WHERE section='reading'").fetchone()[0]
        u_cnt = conn.execute("SELECT COUNT(*) FROM MICRO_UNITS").fetchone()[0]
        gp_cnt = conn.execute("SELECT COUNT(*) FROM GRAMMAR_POINTS").fetchone()[0]
        gd_cnt = conn.execute("SELECT COUNT(*) FROM GRAMMAR_DRILLS").fetchone()[0]
        qga_cnt = conn.execute("SELECT COUNT(*) FROM QUESTION_GRAMMAR_ANALYSES").fetchone()[0]
        vf_cnt = conn.execute("SELECT COUNT(*) FROM VOCAB_FOUNDATION").fetchone()[0]
    finally:
        conn.close()
    return {
        "status": "online",
        "version": __version__,
        "db_path": str(get_db_path()),
        "total_questions": int(q_cnt),
        "total_variants": int(v_cnt),
        "dokkai_passages": int(p_cnt),
        "micro_units": int(u_cnt),
        "grammar_points": int(gp_cnt),
        "grammar_drills": int(gd_cnt),
        "question_grammar_analyses": int(qga_cnt),
        "vocab_foundation": int(vf_cnt),
    }


@app.post("/api/seed")
def post_seed() -> Dict[str, Any]:
    return import_all_excel(generate_variants=True)


@app.get("/api/dashboard")
def get_dashboard() -> Dict[str, Any]:
    readiness = calculate_dual_readiness()
    pace = compute_pace_feasibility()
    settings = get_pace_settings()
    units = _get_units_overview()
    errors = get_error_notebook(limit=50)
    grammar_summary = get_grammar_overview()
    conn = get_connection()
    try:
        wb_cnt = conn.execute("SELECT COUNT(*) FROM SOURCE_WORKBOOKS").fetchone()[0]
        exams = conn.execute(
            "SELECT * FROM MOCK_EXAMS ORDER BY id DESC LIMIT 10"
        ).fetchall()
    finally:
        conn.close()
    return {
        "readiness": readiness.model_dump(),
        "pace": pace.model_dump(),
        "settings": settings.model_dump(),
        "units": units,
        "error_count": len(errors),
        "workbooks_count": int(wb_cnt),
        "recent_exams": [dict(r) for r in exams],
        "grammar_summary": grammar_summary,
    }


@app.get("/api/settings")
def get_settings_api() -> Dict[str, Any]:
    settings = get_pace_settings()
    pace = compute_pace_feasibility()
    readiness = calculate_dual_readiness()
    return {
        "settings": settings.model_dump(),
        "pace": pace.model_dump(),
        "readiness": readiness.model_dump(),
    }


@app.put("/api/settings")
def update_settings_api(req: PaceSettings) -> Dict[str, Any]:
    updated = update_pace_settings(
        days_remaining=req.days_remaining,
        daily_minutes=req.daily_minutes,
        scoring_mode=req.scoring_mode.value,
    )
    pace = compute_pace_feasibility()
    readiness = calculate_dual_readiness(scoring_mode=updated.scoring_mode)
    return {
        "settings": updated.model_dump(),
        "pace": pace.model_dump(),
        "readiness": readiness.model_dump(),
    }


@app.get("/api/units")
def list_units() -> Dict[str, Any]:
    return {"units": _get_units_overview()}


@app.get("/api/units/{unit_code}")
def get_unit_detail(unit_code: str) -> Dict[str, Any]:
    conn = get_connection()
    try:
        unit = conn.execute("SELECT * FROM MICRO_UNITS WHERE code=?", (unit_code,)).fetchone()
        if not unit:
            raise HTTPException(status_code=404, detail=f"Không tìm thấy Micro-Unit '{unit_code}'")
        cap = conn.execute("SELECT * FROM N4_BRIDGE_CAPSULES WHERE unit_code=?", (unit_code,)).fetchone()
        q_rows = conn.execute(
            """
            SELECT q.id, q.section, q.mondai_type, q.source_label, q.focus_keyword, q.prompt_jp,
                   f.stability, f.reps, f.lapses, f.state, f.scaffold_tier,
                   f.clean_original_passed, f.variant_passed, f.spaced_clean_sessions,
                   (SELECT COUNT(*) FROM VARIANT_DRILLS v WHERE v.question_id=q.id) AS variant_count,
                   (SELECT a.is_correct FROM ATTEMPT_LOGS a WHERE a.question_id=q.id ORDER BY a.id DESC LIMIT 1) AS latest_overall_correct
            FROM QUESTIONS q
            JOIN FSRS_STATES f ON f.question_id = q.id
            WHERE q.unit_code=?
            ORDER BY q.id
            """,
            (unit_code,),
        ).fetchall()
    finally:
        conn.close()

    questions = []
    for r in q_rows:
        d = dict(r)
        d["mastered_10_10"] = is_question_mastered(d)
        questions.append(d)

    capsule = None
    if cap:
        capsule = {
            "id": cap["id"],
            "unit_code": cap["unit_code"],
            "grammar_focus": cap["grammar_focus"],
            "explanation_vi": cap["explanation_vi"],
            "examples": json.loads(cap["examples_json"] or "[]"),
            "quick_check": json.loads(cap["quick_check_json"] or "[]"),
            "completed": bool(cap["completed"]),
        }

    return {
        "unit": dict(unit),
        "bridge_capsule": capsule,
        "questions": questions,
    }


@app.post("/api/units/{unit_code}/bridge/complete")
def complete_unit_bridge(unit_code: str, req: BridgeCompleteRequest) -> Dict[str, Any]:
    conn = get_connection()
    try:
        cap = conn.execute("SELECT * FROM N4_BRIDGE_CAPSULES WHERE unit_code=?", (unit_code,)).fetchone()
        if not cap:
            raise HTTPException(status_code=404, detail=f"Không tìm thấy Trạm Bắc cầu cho '{unit_code}'")
        quick_checks = json.loads(cap["quick_check_json"] or "[]")
    finally:
        conn.close()

    qc_results = []
    all_ok = True
    if req.quick_check_answers is not None:
        if len(req.quick_check_answers) != len(quick_checks):
            raise HTTPException(status_code=400, detail="Số câu kiểm tra nhanh không khớp.")
        for idx, ans in enumerate(req.quick_check_answers):
            expected = int(quick_checks[idx]["correct_index"])
            ok = int(ans) == expected
            if not ok:
                all_ok = False
            qc_results.append({"index": idx, "is_correct": ok, "expected_index": expected, "note": quick_checks[idx]["note"]})

    if all_ok:
        with transaction() as wconn:
            wconn.execute("UPDATE N4_BRIDGE_CAPSULES SET completed=1 WHERE unit_code=?", (unit_code,))

    return {
        "unit_code": unit_code,
        "completed": all_ok,
        "quick_check_results": qc_results,
        "pace": compute_pace_feasibility().model_dump(),
    }


@app.get("/api/session/next")
def get_next_session_item(
    unit_code: Optional[str] = None,
    mode: str = Query("mixed", pattern="^(mixed|original|variant|remediation)$"),
    question_id: Optional[int] = None,
    variant_id: Optional[int] = None,
    session_seed: Optional[str] = None,
    exam_mode: bool = False,
) -> Dict[str, Any]:
    seed = session_seed or secrets.token_hex(4)
    try:
        if question_id is not None:
            item = get_study_item(
                question_id=question_id,
                mode="variant" if variant_id is not None else mode,
                variant_id=variant_id,
                session_seed=seed,
                exam_mode=exam_mode,
            )
            return {"item": item, "empty": False}
        item = get_next_study_candidate(
            unit_code=unit_code,
            mode=mode,
            session_seed=seed,
            exam_mode=exam_mode,
        )
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))

    if item is None:
        return {
            "item": None,
            "empty": True,
            "reason": "Không còn câu hỏi phù hợp trong hàng đợi này.",
        }
    return {"item": item, "empty": False}


@app.post("/api/session/hint")
def request_session_hint(req: SessionHintRequest) -> Dict[str, Any]:
    conn = get_connection()
    try:
        q = conn.execute("SELECT * FROM QUESTIONS WHERE id=?", (req.question_id,)).fetchone()
        if not q:
            raise HTTPException(status_code=404, detail=f"Không tìm thấy câu hỏi id={req.question_id}")
        fsrs = conn.execute("SELECT stability FROM FSRS_STATES WHERE question_id=?", (req.question_id,)).fetchone()
        cap = conn.execute("SELECT grammar_focus FROM N4_BRIDGE_CAPSULES WHERE unit_code=?", (q["unit_code"],)).fetchone()
        v_row = None
        if req.variant_id is not None:
            v_row = conn.execute(
                "SELECT prompt_jp, options_json FROM VARIANT_DRILLS WHERE id=? AND question_id=?",
                (req.variant_id, req.question_id),
            ).fetchone()
    finally:
        conn.close()

    stab = float(fsrs["stability"]) if fsrs else 0.5
    target_prompt = str(v_row["prompt_jp"]) if v_row else str(q["prompt_jp"])
    target_options = json.loads(v_row["options_json"] if v_row else q["options_json"])
    return get_contextual_hint(
        prompt_jp=target_prompt,
        stability=stab,
        exam_mode=req.exam_mode,
        focus_keyword=q["focus_keyword"],
        bridge_focus=cap["grammar_focus"] if cap else None,
        options=target_options,
    )


@app.post("/api/session/submit")
def submit_session_answer(req: SessionSubmitRequest) -> Dict[str, Any]:
    try:
        result = submit_answer(
            question_id=req.question_id,
            mode=req.mode,
            variant_id=req.variant_id,
            selected_index=req.selected_index,
            slot_order=req.slot_order,
            evidence_indices=req.evidence_indices,
            used_hint=req.used_hint,
            response_sec=req.response_sec,
            session_seed=req.session_seed,
            exam_mode=req.exam_mode,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    readiness = calculate_dual_readiness()
    pace = compute_pace_feasibility()
    errors = get_error_notebook(limit=500)
    return {
        "result": result,
        "readiness": readiness.model_dump(),
        "pace": pace.model_dump(),
        "error_count": len(errors),
    }


@app.post("/api/session/rate")
def override_fsrs_rating(req: RatingOverrideRequest) -> Dict[str, Any]:
    try:
        res = apply_fsrs_update(
            question_id=req.question_id,
            rating=req.rating.value,
            used_hint=req.used_hint,
        )
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    return {"fsrs": res, "readiness": calculate_dual_readiness().model_dump()}


@app.get("/api/exam/generate")
def generate_mock_exam(
    count_per_section: int = Query(5, ge=1, le=20),
    unit_code: Optional[str] = None,
    session_seed: Optional[str] = None,
) -> Dict[str, Any]:
    seed = session_seed or f"exam-{secrets.token_hex(4)}"
    conn = get_connection()
    try:
        items: List[Dict[str, Any]] = []
        if unit_code:
            rows = conn.execute(
                "SELECT id FROM QUESTIONS WHERE unit_code=? ORDER BY RANDOM() LIMIT ?",
                (unit_code, count_per_section * 3),
            ).fetchall()
            q_ids = [int(r["id"]) for r in rows]
        else:
            q_ids = []
            for sec in ("vocab", "grammar", "reading"):
                rows = conn.execute(
                    "SELECT id FROM QUESTIONS WHERE section=? ORDER BY RANDOM() LIMIT ?",
                    (sec, count_per_section),
                ).fetchall()
                q_ids.extend(int(r["id"]) for r in rows)
    finally:
        conn.close()

    for qid in q_ids:
        items.append(get_study_item(qid, mode="original", session_seed=seed, exam_mode=True))

    return {
        "exam_mode": "unit_exam" if unit_code else "mini_mock",
        "session_seed": seed,
        "total_questions": len(items),
        "items": items,
    }


@app.post("/api/exam/submit")
def submit_mock_exam(req: ExamSubmitRequest) -> Dict[str, Any]:
    if not req.answers:
        raise HTTPException(status_code=400, detail="Bài thi nộp lên không có câu trả lời nào.")

    # Pre-validate all exam answers before inserting MOCK_EXAMS or mutating ATTEMPT_LOGS
    conn = get_connection()
    try:
        for ans in req.answers:
            q = conn.execute(
                "SELECT id, section, mondai_type, notebook_meta_json FROM QUESTIONS WHERE id=?",
                (ans.question_id,),
            ).fetchone()
            if not q:
                raise HTTPException(status_code=400, detail=f"Câu {ans.question_id}: Không tìm thấy câu hỏi.")
            q_meta = json.loads(q["notebook_meta_json"] or "{}")
            if q["section"] == "grammar" and q["mondai_type"] == "問題2" and q_meta.get("star_assembly"):
                slots = ans.slot_order
                if slots is None or len(slots) != 4 or sorted(slots) != [0, 1, 2, 3]:
                    raise HTTPException(
                        status_code=400,
                        detail=f"Câu {ans.question_id}: Bắt buộc ghép đủ cả 4 ô ★ [0..3] hợp lệ.",
                    )
            else:
                if ans.selected_index is None or not (0 <= int(ans.selected_index) <= 3):
                    raise HTTPException(
                        status_code=400,
                        detail=f"Câu {ans.question_id}: Vui lòng chọn đáp án hợp lệ 0..3.",
                    )
    finally:
        conn.close()

    with transaction() as conn:
        cur = conn.execute(
            "INSERT INTO MOCK_EXAMS (exam_mode, total_questions) VALUES (?, ?)",
            (req.exam_mode, len(req.answers)),
        )
        exam_id = int(cur.lastrowid)

    details = []
    correct_count = 0
    for ans in req.answers:
        try:
            res = submit_answer(
                question_id=ans.question_id,
                mode="exam",
                variant_id=None,
                selected_index=ans.selected_index,
                slot_order=ans.slot_order,
                evidence_indices=ans.evidence_indices,
                used_hint=False,
                response_sec=req.duration_sec / max(1, len(req.answers)),
                session_seed=ans.session_seed,
                exam_mode=True,
                mock_exam_id=exam_id,
            )
            if res["is_correct"]:
                correct_count += 1
            details.append(res)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=f"Câu {ans.question_id}: {exc}")

    readiness = calculate_dual_readiness()
    errors = get_error_notebook(limit=500)
    with transaction() as conn:
        conn.execute(
            """
            UPDATE MOCK_EXAMS
            SET original_score_10=?, mastery_score_10=?, correct_count=?
            WHERE id=?
            """,
            (
                readiness.original_score_10,
                readiness.mastery_score_10,
                correct_count,
                exam_id,
            ),
        )

    return {
        "mock_exam_id": exam_id,
        "total_questions": len(req.answers),
        "correct_count": correct_count,
        "exam_accuracy_10": round((correct_count / len(req.answers)) * 10.0, 2),
        "readiness": readiness.model_dump(),
        "error_count": len(errors),
        "details": details,
    }


@app.get("/api/errors")
def list_errors(limit: int = Query(100, ge=1, le=500)) -> Dict[str, Any]:
    items = get_error_notebook(limit=limit)
    return {"errors": items, "total": len(items)}


@app.get("/api/workbooks")
def list_workbooks() -> Dict[str, Any]:
    conn = get_connection()
    try:
        rows = conn.execute("SELECT * FROM SOURCE_WORKBOOKS ORDER BY id").fetchall()
        return {"workbooks": [dict(r) for r in rows]}
    finally:
        conn.close()


@app.post("/api/import/excel")
async def upload_excel_workbook(file: UploadFile = File(...)) -> Dict[str, Any]:
    filename = file.filename or "uploaded.xlsx"
    if not filename.lower().endswith(".xlsx"):
        raise HTTPException(status_code=400, detail="Chỉ hỗ trợ tệp định dạng .xlsx")

    content = await file.read()
    if not content:
        raise HTTPException(status_code=400, detail="Tệp Excel tải lên rỗng.")

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir) / Path(filename).name
        tmp_path.write_bytes(content)
        try:
            report = import_excel_file(tmp_path, generate_variants=True)
        except Exception as exc:
            raise HTTPException(status_code=400, detail=f"Lỗi đọc cấu trúc Excel: {exc}")

    return {
        "import_report": report,
        "health": get_health(),
        "readiness": calculate_dual_readiness().model_dump(),
    }


@app.get("/api/grammar/overview")
def get_grammar_overview_api() -> Dict[str, Any]:
    return get_grammar_overview()


@app.get("/api/grammar/points")
def list_grammar_points_api(
    scope: str = Query("all", pattern="^(all|exam|jlpt)$"),
    level: Optional[str] = None,
    category: Optional[str] = None,
    state: Optional[str] = None,
    q: Optional[str] = None,
) -> Dict[str, Any]:
    points = list_grammar_points(
        scope=scope,
        level=level,
        category=category,
        state=state,
        q=q,
    )
    return {
        "total": len(points),
        "points": points,
        "categories": get_grammar_categories(),
    }


@app.get("/api/grammar/points/{code}")
def get_grammar_point_detail_api(code: str) -> Dict[str, Any]:
    detail = get_grammar_point_detail(code)
    if detail is None:
        raise HTTPException(status_code=404, detail=f"Không tìm thấy điểm ngữ pháp '{code}'")
    return detail


@app.get("/api/grammar/drill/next")
def get_next_grammar_drill_api(
    drill_type: str = Query("mixed", pattern="^(mixed|formation|contrast|application)$"),
    scope: str = Query("all", pattern="^(all|exam|jlpt)$"),
    level: Optional[str] = None,
    grammar_code: Optional[str] = None,
    session_seed: Optional[str] = None,
) -> Dict[str, Any]:
    seed = session_seed or secrets.token_hex(4)
    try:
        drill = get_next_grammar_drill(
            drill_type=drill_type,
            scope=scope,
            level=level,
            grammar_code=grammar_code,
            session_seed=seed,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    if drill is None:
        return {
            "drill": None,
            "empty": True,
            "reason": "Không tìm thấy bài luyện ngữ pháp phù hợp bộ lọc hiện tại.",
        }
    return {"drill": drill, "empty": False}


@app.post("/api/grammar/drill/submit")
def submit_grammar_drill_api(req: GrammarDrillSubmitRequest) -> Dict[str, Any]:
    try:
        res = submit_grammar_drill(
            drill_id=req.drill_id,
            selected_index=req.selected_index,
            response_sec=req.response_sec,
            session_seed=req.session_seed,
        )
    except ValueError as exc:
        msg = str(exc)
        status = 404 if "Không tìm thấy" in msg else 400
        raise HTTPException(status_code=status, detail=msg)
    res["overview"] = get_grammar_overview()
    return res


@app.post("/api/grammar/import")
async def import_grammar_pack_api(file: UploadFile = File(...)) -> Dict[str, Any]:
    filename = file.filename or "grammar_pack.json"
    lower_name = filename.lower()
    if not lower_name.endswith((".json", ".xlsx")):
        raise HTTPException(status_code=400, detail="Chỉ hỗ trợ tệp định dạng .json hoặc .xlsx")

    content = await file.read()
    if not content:
        raise HTTPException(status_code=400, detail="Tệp tải lên rỗng.")

    try:
        res = import_jlpt_grammar_pack(content, filename=filename)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Lỗi nạp gói ngữ pháp: {exc}")

    res["overview"] = get_grammar_overview()
    res["health"] = get_health()
    return res


@app.get("/api/foundation/vocab")
def list_vocab_foundation_api(
    scope: str = Query("all", pattern="^(all|exam|curated|jlpt)$"),
    level: Optional[str] = None,
    q: Optional[str] = None,
    limit: int = Query(200, ge=1, le=500),
) -> Dict[str, Any]:
    items = list_vocab_foundation(scope=scope, level=level, q=q, limit=limit)
    return {"total": len(items), "items": items}
