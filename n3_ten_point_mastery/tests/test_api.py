"""Tests for FastAPI REST Backend, E2E study workflow, Excel upload, and mock exams."""

import io
import json
import openpyxl
from fastapi.testclient import TestClient

from n3_mastery.api import app
from n3_mastery.database import get_connection


def test_api_lifespan_health_dashboard_and_zero_score(isolated_db):
    with TestClient(app) as client:
        h = client.get("/api/health")
        assert h.status_code == 200
        hd = h.json()
        assert hd["total_questions"] == 163
        assert hd["dokkai_passages"] == 18
        assert hd["micro_units"] == 12
        assert hd["total_variants"] >= 163

        dash = client.get("/api/dashboard")
        assert dash.status_code == 200
        dd = dash.json()
        assert dd["readiness"]["original_score_10"] == 0.0
        assert dd["readiness"]["mastery_score_10"] == 0.0
        assert len(dd["units"]) == 12


def test_api_adaptive_pace_and_units_bridge(isolated_db):
    with TestClient(app) as client:
        # Tight budget triggers honest capacity warning
        put_res = client.put(
            "/api/settings",
            json={"days_remaining": 4, "daily_minutes": 25, "scoring_mode": "jlpt_weighted"},
        )
        assert put_res.status_code == 200
        pace = put_res.json()["pace"]
        assert pace["is_feasible"] is False
        assert "[WARN]" in pace["warning_message"]

        # Bridge capsule check & complete for MU-01
        u_res = client.get("/api/units/MU-01")
        assert u_res.status_code == 200
        qc = u_res.json()["bridge_capsule"]["quick_check"]
        answers = [item["correct_index"] for item in qc]
        c_res = client.post("/api/units/MU-01/bridge/complete", json={"quick_check_answers": answers})
        assert c_res.status_code == 200
        assert c_res.json()["completed"] is True


def test_api_session_flow_star_validation_and_exam(isolated_db):
    with TestClient(app) as client:
        # Request MU-10 (問題2 ★)
        s_res = client.get("/api/session/next?unit_code=MU-10&mode=original&session_seed=apitest")
        assert s_res.status_code == 200
        item = s_res.json()["item"]
        assert item["interaction_type"] == "star_4slot"

        # Submitting incomplete 1-slot guess returns 400
        bad_sub = client.post(
            "/api/session/submit",
            json={
                "question_id": item["question_id"],
                "mode": "original",
                "slot_order": [0],
                "session_seed": "apitest",
            },
        )
        assert bad_sub.status_code == 400

        # Submit full correct 4 slots
        conn = get_connection()
        sa = json.loads(
            conn.execute("SELECT notebook_meta_json FROM QUESTIONS WHERE id=?", (item["question_id"],)).fetchone()[0]
        )["star_assembly"]
        conn.close()
        ok_sub = client.post(
            "/api/session/submit",
            json={
                "question_id": item["question_id"],
                "mode": "original",
                "slot_order": sa["slots_order"],
                "session_seed": "apitest",
            },
        )
        assert ok_sub.status_code == 200
        assert ok_sub.json()["result"]["is_correct"] is True
        assert ok_sub.json()["readiness"]["original_score_10"] > 0.0

        # Hint on MU-01 item
        v_res = client.get("/api/session/next?unit_code=MU-01&mode=original&session_seed=hseed")
        v_item = v_res.json()["item"]
        hint_res = client.post("/api/session/hint", json={"question_id": v_item["question_id"], "exam_mode": True})
        assert hint_res.status_code == 200
        assert hint_res.json()["allowed"] is False

        # Generate and submit mini mock exam (1 per section = 3 questions)
        ex_gen = client.get("/api/exam/generate?count_per_section=1&session_seed=mock1").json()
        assert ex_gen["total_questions"] == 3
        exam_answers = []
        for ex_item in ex_gen["items"]:
            assert ex_item["scaffolding"]["tier"] == 3
            if ex_item["interaction_type"] == "star_4slot":
                conn = get_connection()
                sa2 = json.loads(
                    conn.execute("SELECT notebook_meta_json FROM QUESTIONS WHERE id=?", (ex_item["question_id"],)).fetchone()[0]
                )["star_assembly"]
                conn.close()
                exam_answers.append(
                    {"question_id": ex_item["question_id"], "slot_order": sa2["slots_order"], "session_seed": "mock1"}
                )
            else:
                exam_answers.append(
                    {"question_id": ex_item["question_id"], "selected_index": 0, "session_seed": "mock1"}
                )
        ex_sub = client.post(
            "/api/exam/submit",
            json={"exam_mode": "mini_mock", "answers": exam_answers, "duration_sec": 60.0},
        )
        assert ex_sub.status_code == 200
        assert ex_sub.json()["total_questions"] == 3


def test_api_upload_new_excel_workbook(isolated_db):
    with TestClient(app) as client:
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Tong_Hop_On_Thi"
        ws.append(["ĐỀ UPLOAD MỚI"])
        ws.append(["Hướng dẫn"])
        ws.append([])
        ws.append([
            "Mondai", "Câu", "Từ khóa", "Đề bài", "Đ1", "Đ2", "Đ3", "Đ4",
            "Tự chọn", "KQ", "Đáp án đúng", "Nội dung", "Dịch", "Giải thích"
        ])
        ws.append([
            "問題1: Cách đọc Kanji", 1, "技術 → ぎじゅつ", "新しい【技術】を学ぶ。",
            "きじゅつ", "ぎじゅつ", "ぎしゅつ", "きしゅつ", None, None, 2, "2. ぎじゅつ",
            "Học kỹ thuật mới.",
            "• Đáp án đúng: 2. ぎじゅつ.\n• Bẫy:\n  - 1. きじゅつ (記述: ghi chép)."
        ])
        ws_nb = wb.create_sheet("So_Tay_Tu_Vung")
        ws_nb.append(["SỔ TAY"])
        ws_nb.append([])
        ws_nb.append(["STT", "Nguồn câu", "Từ vựng", "Hiragana", "Hán Việt", "Nghĩa", "Mẹo"])
        ws_nb.append([1, "Câu 1", "技術", "ぎじゅつ", "KỸ THUẬT", "Kỹ thuật", "新しい技術"])

        buf = io.BytesIO()
        wb.save(buf)
        buf.seek(0)

        up_res = client.post(
            "/api/import/excel",
            files={"file": ("extra_vocab.xlsx", buf.getvalue(), "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")},
        )
        assert up_res.status_code == 200
        data = up_res.json()
        assert data["import_report"]["imported_count"] == 1
        assert data["import_report"]["variants_generated"] >= 1
        assert data["health"]["total_questions"] == 164

        # Reject invalid extension
        bad = client.post(
            "/api/import/excel",
            files={"file": ("bad.txt", b"not excel", "text/plain")},
        )
        assert bad.status_code == 400


def _wb_to_bytes(wb: openpyxl.Workbook) -> bytes:
    buf = io.BytesIO()
    wb.save(buf)
    return buf.getvalue()


def test_api_upload_all_4_layouts_including_partial_without_companions(isolated_db):
    """Upload partial Layout B, Layout C, Layout D1, and Layout D2 via HTTP and exercise generated variants."""
    mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    with TestClient(app) as client:
        # 1. Partial Layout B (Phan_II_Ngu_Phap only, no Dashboard_Tong_Quan)
        wb_b = openpyxl.Workbook()
        ws_b = wb_b.active
        ws_b.title = "Phan_II_Ngu_Phap"
        ws_b.append(["Gói", "Câu", "Mẫu", "Đề bài", "Đ1", "Đ2", "Đ3", "Đ4", "T", "K", "ĐA", "ND", "Câu hoàn chỉnh", "GT"])
        ws_b.append([
            "II-2. 問題2: Sắp xếp câu sao ★", "1)", "Định ngữ",
            "駅の前で ＿＿＿ ＿＿＿ ★ ＿＿＿ 買った。",
            "花を", "きれいな", "友だちに", "渡す", None, None, 4, "4. 渡す",
            "Câu hoàn chỉnh: 駅の前で [3. 友だちに] [4. 渡す] [★ 2. きれいな] [1. 花を] 買った。",
            "Giải thích.",
        ])
        # Wait: ensure correct_index matches ★ slot or star_assembly works consistently:
        # Let's fix col 11 to 2 matching [★ 2. きれいな]
        ws_b.cell(2, 11, 2)
        ws_b.cell(2, 12, "2. きれいな")

        res_b = client.post("/api/import/excel", files={"file": ("partial_b.xlsx", _wb_to_bytes(wb_b), mime)})
        assert res_b.status_code == 200
        db_b = res_b.json()
        assert db_b["import_report"]["layout_type"] == "comprehensive_3_part"
        assert db_b["import_report"]["imported_count"] == 1
        assert db_b["import_report"]["variants_generated"] >= 1
        assert db_b["health"]["total_questions"] == 164

        # Verify uploaded 問題2 ★ works in /api/session/next and /api/session/submit
        conn = get_connection()
        new_star_id = conn.execute(
            "SELECT id FROM QUESTIONS WHERE prompt_jp LIKE '%駅の前で%' AND mondai_type='問題2'"
        ).fetchone()[0]
        conn.close()
        st_item = client.get(f"/api/session/next?question_id={new_star_id}&mode=variant&session_seed=upb").json()["item"]
        assert st_item["interaction_type"] == "star_4slot"
        assert st_item["variant_mode"] == "star_4slot_shift"
        sub_b = client.post(
            "/api/session/submit",
            json={
                "question_id": new_star_id,
                "variant_id": st_item["variant_id"],
                "mode": "variant",
                "slot_order": [2, 3, 1, 0],
                "session_seed": "upb",
            },
        )
        assert sub_b.status_code == 200
        assert sub_b.json()["result"]["is_correct"] is True

        # 2. Layout C (Bai_Doc_Va_Luyen_Tap only, no So_Tay_Ngu_Phap_Dokkai)
        wb_c = openpyxl.Workbook()
        ws_c = wb_c.active
        ws_c.title = "Bai_Doc_Va_Luyen_Tap"
        ws_c.append(["Gói 1: Bài đọc — 「図書館の利用」"])
        ws_c.append(["【図書館の利用】\n本を借りる人は [ 1 ] カードを作ってください。", None, None, None, None, None, None, "Hướng dẫn thư viện."])
        ws_c.append(["Gói", "Câu", "Ngữ cảnh", "Đ1", "Đ2", "Đ3", "Đ4", "T", "K", "ĐA", "ND", "Mẫu", "GT"])
        ws_c.append([
            "Gói 1", "Câu [1]", "本を借りる人は [ 1 ] カードを作ってください。",
            "まず", "しかし", "それでも", "まさか", None, None, 1, "1. まず", "Từ nối trình tự",
            "• Đáp án đúng: 1. まず (trước tiên).\n• Bẫy:\n  - 2. しかし: nhưng (đối lập).",
        ])
        res_c = client.post("/api/import/excel", files={"file": ("partial_c.xlsx", _wb_to_bytes(wb_c), mime)})
        assert res_c.status_code == 200
        dc = res_c.json()
        assert dc["import_report"]["layout_type"] == "grammar_cloze_3_passages"
        assert dc["import_report"]["imported_count"] == 1
        assert dc["import_report"]["variants_generated"] >= 1
        assert dc["health"]["total_questions"] == 165

        # 3. Layout D1 (Dokkai_Doan_Van_Ngan only, no Bang_Giai_Ma_Bay_Dokkai)
        wb_d1 = openpyxl.Workbook()
        ws_d1 = wb_d1.active
        ws_d1.title = "Dokkai_Doan_Van_Ngan"
        ws_d1.append(["Gói 1 — Bài [88]"])
        ws_d1.append(["【Đoạn văn [88]】\n明日は雨の予報だ。ピクニックは来週に延期する。", None, None, None, None, None, None, "Dời picnic sang tuần sau."])
        ws_d1.append(["Gói", "Bài", "Câu hỏi", "Đ1", "Đ2", "Đ3", "Đ4", "T", "K", "ĐA", "ND", "KN", "GT"])
        ws_d1.append([
            "Gói 1", "[88]", "ピクニックはどうするか。",
            "明日行う", "来週に延期する", "中止する", "室内で行う", None, None, 2, "2. 来週に延期する", "Tìm thông tin chính",
            "• Đáp án đúng: 2. Câu chốt: 「ピクニックは来週に延期する」.",
        ])
        res_d1 = client.post("/api/import/excel", files={"file": ("partial_d1.xlsx", _wb_to_bytes(wb_d1), mime)})
        assert res_d1.status_code == 200
        dd1 = res_d1.json()
        assert dd1["import_report"]["layout_type"] == "dokkai_short"
        assert dd1["import_report"]["imported_count"] == 1
        assert dd1["import_report"]["variants_generated"] >= 1
        assert dd1["health"]["total_questions"] == 166

        # 4. Layout D2 (Tim_Kiem_Thong_Tin_Dokkai only, no Ma_Tran_Doi_Chieu_Dieu_Kien)
        wb_d2 = openpyxl.Workbook()
        ws_d2 = wb_d2.active
        ws_d2.title = "Tim_Kiem_Thong_Tin_Dokkai"
        ws_d2.append(["Gói 1 — 「体育館の案内」"])
        ws_d2.append(["【Tình huống (88)】\n利用時間：午前9時～午後9時。\n休館日：毎週水曜日。", None, None, None, None, None, None, "Nghỉ thứ 4 hàng tuần."])
        ws_d2.append(["Gói", "Câu", "Câu hỏi", "Đ1", "Đ2", "Đ3", "Đ4", "T", "K", "ĐA", "ND", "KN", "GT"])
        ws_d2.append([
            "Gói 1", "[1]", "体育館が使えない日はいつか。",
            "月曜日", "火曜日", "水曜日", "日曜日", None, None, 3, "3. 水曜日", "Lọc ngày nghỉ 休館日",
            "• Đáp án đúng: 3. 水曜日. Căn cứ 「休館日：毎週水曜日」.",
        ])
        res_d2 = client.post("/api/import/excel", files={"file": ("partial_d2.xlsx", _wb_to_bytes(wb_d2), mime)})
        assert res_d2.status_code == 200
        dd2 = res_d2.json()
        assert dd2["import_report"]["layout_type"] == "dokkai_info"
        assert dd2["import_report"]["imported_count"] == 1
        assert dd2["import_report"]["variants_generated"] >= 1
        assert dd2["health"]["total_questions"] == 167

        # Verify Dokkai Evidence-First item from newly uploaded Layout D2 works via API
        conn = get_connection()
        d2_qid = conn.execute(
            "SELECT id FROM QUESTIONS WHERE prompt_jp LIKE '%体育館が使えない日%'"
        ).fetchone()[0]
        conn.close()
        ev_item = client.get(f"/api/session/next?question_id={d2_qid}&mode=variant&session_seed=upd2").json()["item"]
        assert ev_item["interaction_type"] == "dokkai_evidence"
        assert ev_item["passage"] is not None
        assert len(ev_item["passage"]["sentences"]) == 2

        # 5. Reject unrecognized sheet structure AND 0-question valid-sheet workbooks with HTTP 400
        wb_bad = openpyxl.Workbook()
        wb_bad.active.title = "Random_Unknown_Sheet"
        bad_xl = client.post("/api/import/excel", files={"file": ("bad_layout.xlsx", _wb_to_bytes(wb_bad), mime)})
        assert bad_xl.status_code == 400

        wb_zero = openpyxl.Workbook()
        wb_zero.active.title = "Tong_Hop_On_Thi"
        wb_zero.active.append(["Mondai", "Câu", "Từ khóa", "Đề bài", "Đ1", "Đ2", "Đ3", "Đ4", "T", "K", "ĐA"])
        zero_xl = client.post("/api/import/excel", files={"file": ("zero_rows.xlsx", _wb_to_bytes(wb_zero), mime)})
        assert zero_xl.status_code == 400
        # Confirm workbooks list remained clean (7 seeded + 4 valid partial uploads = 11)
        wbs = client.get("/api/workbooks").json()["workbooks"]
        assert len(wbs) == 11
