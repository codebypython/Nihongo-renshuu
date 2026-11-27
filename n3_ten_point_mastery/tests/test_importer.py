"""Tests for Smart .xlsx Importer, deduplication (166 -> 163), companion sheets, and Micro-Unit mapping."""

import json
import openpyxl
import pytest

from n3_mastery.config import get_excel_dir
from n3_mastery.database import get_connection
from n3_mastery.importer import import_all_excel, import_excel_file


def test_import_all_7_workbooks_exact_counts(isolated_db):
    summary = import_all_excel(generate_variants=False)
    assert summary["files_processed"] == 7
    assert summary["total_raw_rows"] == 166
    assert summary["unique_questions"] == 163
    assert summary["dokkai_passages"] == 18
    assert summary["cloze_passages"] == 4

    conn = get_connection()
    try:
        # Check section breakdown: 98 vocab, 42 grammar, 23 reading
        sec_rows = conn.execute(
            "SELECT section, COUNT(*) AS cnt FROM QUESTIONS GROUP BY section"
        ).fetchall()
        sec_map = {r["section"]: r["cnt"] for r in sec_rows}
        assert sec_map == {"vocab": 98, "grammar": 42, "reading": 23}

        # Check exact 12 Micro-Unit counts
        expected_units = {
            "MU-01": 22,
            "MU-02": 18,
            "MU-03": 11,
            "MU-04": 17,
            "MU-05": 16,
            "MU-06": 14,
            "MU-07": 9,
            "MU-08": 12,
            "MU-09": 11,
            "MU-10": 10,
            "MU-11": 17,
            "MU-12": 6,
        }
        unit_rows = conn.execute(
            "SELECT unit_code, COUNT(*) AS cnt FROM QUESTIONS GROUP BY unit_code"
        ).fetchall()
        unit_map = {r["unit_code"]: r["cnt"] for r in unit_rows}
        assert unit_map == expected_units

        # Check この薬の使い方 upgraded to full 5-blank passage
        kusuri = conn.execute(
            "SELECT id, japanese_text FROM PASSAGES WHERE section='grammar' AND title='この薬の使い方'"
        ).fetchone()
        assert kusuri is not None
        assert "[ 5 ]" in kusuri["japanese_text"]
        linked_q = conn.execute(
            "SELECT COUNT(*) FROM QUESTIONS WHERE passage_id=?", (kusuri["id"],)
        ).fetchone()[0]
        assert linked_q == 5

        # Check companion sheets extracted
        so_tay_cnt = conn.execute(
            "SELECT COUNT(*) FROM QUESTIONS WHERE notebook_meta_json LIKE '%\"so_tay\"%'"
        ).fetchone()[0]
        assert so_tay_cnt == 70  # 35 from Lan 1 + 35 from Lan 3

        grammar_nb_cnt = conn.execute(
            "SELECT COUNT(*) FROM QUESTIONS WHERE notebook_meta_json LIKE '%\"grammar_notebook\"%'"
        ).fetchone()[0]
        assert grammar_nb_cnt == 15

        trap_dec_cnt = conn.execute(
            "SELECT COUNT(*) FROM QUESTIONS WHERE notebook_meta_json LIKE '%\"trap_decoder\"%'"
        ).fetchone()[0]
        assert trap_dec_cnt == 7

        cond_mx_cnt = conn.execute(
            "SELECT COUNT(*) FROM QUESTIONS WHERE notebook_meta_json LIKE '%\"condition_matrix\"%'"
        ).fetchone()[0]
        assert cond_mx_cnt == 6

        # Check all 10 star questions parsed 4-slot assembly
        star_rows = conn.execute(
            "SELECT notebook_meta_json FROM QUESTIONS WHERE section='grammar' AND mondai_type='問題2'"
        ).fetchall()
        assert len(star_rows) == 10
        for row in star_rows:
            meta = json.loads(row["notebook_meta_json"])
            assert "star_assembly" in meta
            sa = meta["star_assembly"]
            assert sorted(sa["slots_order"]) == [0, 1, 2, 3]
            assert 0 <= sa["star_slot_index"] <= 3

        # Check all 23 reading questions have evidence_indices inside passage sentence bounds
        reading_rows = conn.execute(
            """
            SELECT q.id, q.notebook_meta_json, p.evidence_sentences_json
            FROM QUESTIONS q
            JOIN PASSAGES p ON p.id = q.passage_id
            WHERE q.section='reading'
            """
        ).fetchall()
        assert len(reading_rows) == 23
        for row in reading_rows:
            meta = json.loads(row["notebook_meta_json"])
            sents = json.loads(row["evidence_sentences_json"])
            ev_idx = meta.get("evidence_indices", [])
            assert len(sents) >= 2
            assert len(ev_idx) >= 1
            assert all(0 <= i < len(sents) for i in ev_idx)
    finally:
        conn.close()


def test_reimport_is_idempotent(isolated_db):
    first = import_all_excel(generate_variants=False)
    second = import_all_excel(generate_variants=False)
    assert first["unique_questions"] == 163
    assert second["unique_questions"] == 163
    assert second["total_newly_imported"] == 0


def test_dedup_order_independence_kusuri(tmp_path, monkeypatch):
    """Importing full 5-question file BEFORE 3-question file keeps full 5-question passage."""
    db_file = tmp_path / "order_test.db"
    monkeypatch.setenv("N3_MASTERY_DB_PATH", str(db_file))
    excel_dir = get_excel_dir()

    f_full = excel_dir / "JLPT_N3_Dokkai_Ngu_Phap_Doan_Van_3_Bai_Chi_Tiet.xlsx"
    f_short = excel_dir / "JLPT_N3_Bo_De_3_Phan_34_Cau_11_Goi_Chi_Tiet.xlsx"

    import_excel_file(f_full, generate_variants=False)
    import_excel_file(f_short, generate_variants=False)

    conn = get_connection()
    try:
        kusuri = conn.execute(
            "SELECT id, japanese_text FROM PASSAGES WHERE section='grammar' AND title='この薬の使い方'"
        ).fetchone()
        assert "[ 5 ]" in kusuri["japanese_text"]
        total_q = conn.execute("SELECT COUNT(*) FROM QUESTIONS").fetchone()[0]
        assert total_q == 15 + 34 - 3  # 46 unique questions
    finally:
        conn.close()


def test_import_new_custom_vocab_workbook(tmp_path, isolated_db):
    """Ensure newly uploaded .xlsx following Gemini Layout A imports cleanly."""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Tong_Hop_On_Thi"
    ws.append(["ĐỀ MỞ RỘNG TEST"])
    ws.append(["Hướng dẫn"])
    ws.append([])
    ws.append([
        "Mondai", "Câu", "Từ khóa", "Đề bài", "Đ1", "Đ2", "Đ3", "Đ4",
        "Tự chọn", "KQ", "Đáp án đúng", "Nội dung", "Dịch", "Giải thích"
    ])
    ws.append([
        "問題1: Cách đọc Kanji", 1, "経験 → けいけん", "これはいい【経験】になった。",
        "けいかん", "けいけん", "きょうけん", "きけん", None, None, 2, "2. けいけん",
        "Đây đã trở thành một kinh nghiệm tốt.",
        "• Đáp án đúng: 2. けいけん.\n• Bẫy:\n  - 1. けいかん (警官: cảnh sát).\n  - 4. きけん (危険: nguy hiểm)."
    ])
    ws_nb = wb.create_sheet("So_Tay_Tu_Vung")
    ws_nb.append(["SỔ TAY"])
    ws_nb.append([])
    ws_nb.append(["STT", "Nguồn câu", "Từ vựng", "Hiragana", "Hán Việt", "Nghĩa", "Mẹo"])
    ws_nb.append([1, "Câu 1", "経験", "けいけん", "KINH NGHIỆM", "Kinh nghiệm", "いい経験になる"])

    custom_xlsx = tmp_path / "custom_n3.xlsx"
    wb.save(custom_xlsx)

    res = import_excel_file(custom_xlsx, generate_variants=False)
    assert res["layout_type"] == "vocab_35"
    assert res["raw_count"] == 1
    assert res["imported_count"] == 1


def test_import_layout_a_without_companion_sheets_and_variants(tmp_path, isolated_db):
    """Layout A (Tong_Hop_On_Thi only, no So_Tay_Tu_Vung) imports cleanly and generates variants."""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Tong_Hop_On_Thi"
    ws.append([
        "Mondai", "Câu", "Từ khóa", "Đề bài", "Đ1", "Đ2", "Đ3", "Đ4",
        "Tự chọn", "KQ", "Đáp án đúng", "Nội dung", "Dịch", "Giải thích",
    ])
    ws.append([
        "問題2: Viết Kanji", 1, "きかい → 機会", "いい【きかい】があったら行きたい。",
        "機械", "機会", "奇怪", "帰会", None, None, 2, "2. 機会",
        "Nếu có cơ hội tốt tôi muốn đi.",
        "• Đáp án đúng: 2. 機会 (cơ hội).\n• Bẫy:\n  - 1. 機械: máy móc cơ khí.",
    ])

    xlsx_path = tmp_path / "layout_a_minimal.xlsx"
    wb.save(xlsx_path)

    res = import_excel_file(xlsx_path, generate_variants=True)
    assert res["layout_type"] == "vocab_35"
    assert res["raw_count"] == 1
    assert res["imported_count"] == 1
    assert res["variants_generated"] >= 1

    conn = get_connection()
    try:
        q = conn.execute("SELECT id, unit_code FROM QUESTIONS WHERE source_label='Câu 1'").fetchone()
        assert q is not None
        assert q["unit_code"] == "MU-02"
        v_cnt = conn.execute("SELECT COUNT(*) FROM VARIANT_DRILLS WHERE question_id=?", (q["id"],)).fetchone()[0]
        assert v_cnt >= 1
    finally:
        conn.close()


def test_import_layout_b_partial_sheets_without_dashboard(tmp_path, isolated_db):
    """Layout B works with partial Phan_I/Phan_II/Phan_III subsets and without Dashboard_Tong_Quan."""
    # Case 1: Phan_II_Ngu_Phap only (with bracketed ★, unbracketed ★, and 問題3 cloze)
    wb_p2 = openpyxl.Workbook()
    ws2 = wb_p2.active
    ws2.title = "Phan_II_Ngu_Phap"
    ws2.append(["ĐỀ TÙY BIẾN PHẦN II"])
    ws2.append(["Hướng dẫn"])
    ws2.append([])
    ws2.append([
        "Gói câu hỏi", "Câu", "Mẫu", "Đề bài", "Đ1", "Đ2", "Đ3", "Đ4",
        "Tự chọn", "KQ", "Đáp án đúng", "Nội dung", "Câu hoàn chỉnh", "Giải thích",
    ])
    ws2.append([
        "II-1. 問題1: Ngữ pháp câu đơn", "1)", "Vて + みる", "新しい料理を作って（　　　）。",
        "みた", "おいた", "あった", "しまった", None, None, 1, "1. みた",
        "Tôi đã thử nấu món ăn mới.",
        "• Đáp án đúng: 1. みた (làm thử).\n• Bẫy:\n  - 2. おいた: làm sẵn trước.",
    ])
    ws2.append([
        "II-2. 問題2: Sắp xếp câu sao ★", "2)", "Định ngữ", "友達と ＿＿＿ ＿＿＿ ★ ＿＿＿ ことにした。",
        "映画を", "見に行く", "約束した", "週末に", None, None, 2, "2. 見に行く",
        "Câu hoàn chỉnh: 友達と [3. 約束した] [4. 週末に] [★ 2. 見に行く] [1. 映画を] ことにした。",
        "Giải thích trật tự bổ nghĩa danh từ.",
    ])
    ws2.append([
        "II-2. 問題2: Sắp xếp câu sao ★", "3)", "Trật tự câu", "図書館で ＿＿＿ ＿＿＿ ★ ＿＿＿ います。",
        "日本の", "歴史を", "毎日", "調べて", None, None, 4, "4. 調べて",
        "Câu hoàn chỉnh: 図書館で毎日日本の歴史を調べています。",
        "Giải thích: 毎日 + 日本の + 歴史を + ★調べて.",
    ])
    ws2.append([
        "II-3. 問題3: Ngữ pháp đoạn văn (新しい習慣)", "[1]", "～ように",
        "毎日少しずつ練習する [ 1 ] なりました。",
        "ように", "ために", "ことに", "そうに", None, None, 1, "1. ように",
        "",
        "• Đáp án đúng: 1. ように (trở nên có thể).\n• Bẫy:\n  - 2. ために: vì mục đích chủ động.",
    ])
    ws2.append(["TOÀN VĂN ĐOẠN ĐỌC CỦA 問題3: 「新しい習慣」"])
    ws2.append([
        "【Đoạn văn gốc tiếng Nhật】\n毎日少しずつ練習する [ 1 ] なりました。続けることが大切です。",
        None, None, None, None, None, None,
        "【Bản dịch tiếng Việt】Tôi đã trở nên luyện tập từng chút mỗi ngày.",
    ])

    p2_path = tmp_path / "layout_b_phan2_only.xlsx"
    wb_p2.save(p2_path)
    res_p2 = import_excel_file(p2_path, generate_variants=True)
    assert res_p2["layout_type"] == "comprehensive_3_part"
    assert res_p2["raw_count"] == 4
    assert res_p2["imported_count"] == 4
    assert res_p2["variants_generated"] >= 4

    conn = get_connection()
    try:
        star_rows = conn.execute(
            "SELECT notebook_meta_json FROM QUESTIONS WHERE mondai_type='問題2' ORDER BY id"
        ).fetchall()
        assert len(star_rows) == 2
        for sr in star_rows:
            sa = json.loads(sr["notebook_meta_json"]).get("star_assembly")
            assert sa is not None
            assert sorted(sa["slots_order"]) == [0, 1, 2, 3]
        shift_cnt = conn.execute(
            "SELECT COUNT(*) FROM VARIANT_DRILLS WHERE variant_mode='star_4slot_shift'"
        ).fetchone()[0]
        assert shift_cnt >= 4

        cloze_p = conn.execute("SELECT id FROM PASSAGES WHERE title='新しい習慣'").fetchone()
        assert cloze_p is not None
        cloze_q = conn.execute("SELECT passage_id, unit_code FROM QUESTIONS WHERE mondai_type='問題3'").fetchone()
        assert cloze_q["passage_id"] == cloze_p["id"]
        assert cloze_q["unit_code"] == "MU-09"
    finally:
        conn.close()

    # Case 2: Phan_I_Tu_Vung_Kanji + Phan_III_Doc_Hai only (missing Dashboard & Phan_II)
    wb_p13 = openpyxl.Workbook()
    ws1 = wb_p13.active
    ws1.title = "Phan_I_Tu_Vung_Kanji"
    ws1.append(["Header", "Câu", "Từ khóa", "Đề bài", "Đ1", "Đ2", "Đ3", "Đ4", "T", "K", "ĐA", "ND", "Dịch", "GT"])
    ws1.append([
        "I-1. 問題1: Cách đọc Kanji", "問1", "準備 → じゅんび", "旅行の【準備】をする。",
        "じゅんぴ", "じゅんび", "しゅんび", "じゅんみ", None, None, 2, "2. じゅんび",
        "Chuẩn bị cho chuyến du lịch.",
        "• Đáp án đúng: 2. じゅんび.\n• Bẫy:\n  - 1. じゅんぴ: sai âm đục.",
    ])
    ws3 = wb_p13.create_sheet("Phan_III_Doc_Hai")
    ws3.append(["III-1. Bài đọc ngắn tùy biến"])
    ws3.append(["【Ⅲ 読解 — テスト】\n朝早く起きると気持ちがいい。健康のために毎日歩いている。", None, None, None, None, None, None, "Dịch thử"])
    ws3.append(["Gói", "Câu", "Câu hỏi", "Đ1", "Đ2", "Đ3", "Đ4", "T", "K", "ĐA", "ND", "Kỹ năng", "GT"])
    ws3.append([
        "III-1. Bài đọc ngắn", "問1", "筆者は何のために歩いているか。",
        "仕事のため", "健康のため", "買い物するため", "友だちに会うため", None, None, 2, "2. 健康のため",
        "Tìm nguyên nhân",
        "• Đáp án đúng: 2. Câu chốt: 「健康のために毎日歩いている」.",
    ])

    p13_path = tmp_path / "layout_b_p1_p3.xlsx"
    wb_p13.save(p13_path)
    res_p13 = import_excel_file(p13_path, generate_variants=True)
    assert res_p13["layout_type"] == "comprehensive_3_part"
    assert res_p13["raw_count"] == 2
    assert res_p13["imported_count"] == 2
    assert res_p13["variants_generated"] >= 2

    conn = get_connection()
    try:
        ev_cnt = conn.execute(
            "SELECT COUNT(*) FROM VARIANT_DRILLS WHERE variant_mode='dokkai_evidence'"
        ).fetchone()[0]
        assert ev_cnt == 1
        p_row = conn.execute(
            "SELECT title FROM PASSAGES WHERE section='reading' AND japanese_text LIKE '%朝早く起きると%'"
        ).fetchone()
        assert p_row is not None
        assert p_row["title"] == "III-1. Bài đọc ngắn tùy biến"
    finally:
        conn.close()


def test_import_layout_c_and_d_without_companion_sheets_and_invalid_rejected(tmp_path, isolated_db):
    """Layout C (grammar_cloze) and Layout D (dokkai_short / dokkai_info) work without companion sheets."""
    # Layout C without So_Tay_Ngu_Phap_Dokkai
    wb_c = openpyxl.Workbook()
    ws_c = wb_c.active
    ws_c.title = "Bai_Doc_Va_Luyen_Tap"
    ws_c.append(["Gói 1: Bài đọc — 「朝の散歩」"])
    ws_c.append(["【朝の散歩】\n朝に歩くと頭がすっきりする。[ 1 ]、毎日続けるのは簡単ではない。", None, None, None, None, None, None, "Đi dạo buổi sáng."])
    ws_c.append(["Gói", "Câu", "Ngữ cảnh", "Đ1", "Đ2", "Đ3", "Đ4", "T", "K", "ĐA", "ND", "Mẫu", "Giải thích"])
    ws_c.append([
        "Gói 1: 朝の散歩", "Câu [1]", "頭がすっきりする。[ 1 ]、毎日続けるのは簡単ではない。",
        "それで", "しかし", "つまり", "たとえば", None, None, 2, "2. しかし", "Từ nối đối lập",
        "• Đáp án đúng: 2. しかし (tuy nhiên).\n• Bẫy:\n  - 1. それで: vì thế (chỉ kết quả).",
    ])
    path_c = tmp_path / "layout_c_no_companion.xlsx"
    wb_c.save(path_c)
    res_c = import_excel_file(path_c, generate_variants=True)
    assert res_c["layout_type"] == "grammar_cloze_3_passages"
    assert res_c["raw_count"] == 1
    assert res_c["imported_count"] == 1
    assert res_c["variants_generated"] >= 1

    # Layout D1 (dokkai_short) without Bang_Giai_Ma_Bay_Dokkai
    wb_d1 = openpyxl.Workbook()
    ws_d1 = wb_d1.active
    ws_d1.title = "Dokkai_Doan_Van_Ngan"
    ws_d1.append(["Gói 1 — Bài [99]: Thông báo thư viện"])
    ws_d1.append(["【Đoạn văn [99]】\n図書館は月曜日が休みです。火曜日から日曜日まで開いています。", None, None, None, None, None, None, "Thư viện nghỉ thứ 2."])
    ws_d1.append(["Gói", "Bài", "Câu hỏi", "Đ1", "Đ2", "Đ3", "Đ4", "T", "K", "ĐA", "ND", "Kỹ năng", "Giải thích"])
    ws_d1.append([
        "Gói 1", "[99]", "図書館の休みはいつか。",
        "月曜日", "火曜日", "土曜日", "日曜日", None, None, 1, "1. 月曜日", "Đọc thông báo",
        "• Đáp án đúng: 1. Câu chốt: 「図書館は月曜日が休みです」.",
    ])
    path_d1 = tmp_path / "layout_d1_no_companion.xlsx"
    wb_d1.save(path_d1)
    res_d1 = import_excel_file(path_d1, generate_variants=True)
    assert res_d1["layout_type"] == "dokkai_short"
    assert res_d1["raw_count"] == 1
    assert res_d1["imported_count"] == 1
    assert res_d1["variants_generated"] >= 1

    # Layout D2 (dokkai_info) without Ma_Tran_Doi_Chieu_Dieu_Kien
    wb_d2 = openpyxl.Workbook()
    ws_d2 = wb_d2.active
    ws_d2.title = "Tim_Kiem_Thong_Tin_Dokkai"
    ws_d2.append(["Gói 1 — 「市民プール案内」"])
    ws_d2.append(["【Tình huống đề bài (99)】\n市民プールは午前9時から利用できます。\n注意：中学生以下は無料です。", None, None, None, None, None, None, "Hồ bơi miễn phí cho HS cấp 2 trở xuống."])
    ws_d2.append(["Gói", "Câu", "Câu hỏi", "Đ1", "Đ2", "Đ3", "Đ4", "T", "K", "ĐA", "ND", "Kỹ năng", "Giải thích"])
    ws_d2.append([
        "Gói 1", "[1]", "中学生の料金はいくらか。",
        "無料", "300円", "500円", "1000円", None, None, 1, "1. 無料", "Tìm điều kiện ẩn 注意",
        "• Đáp án đúng: 1. 無料. Căn cứ mục 「注意：中学生以下は無料です」.",
    ])
    path_d2 = tmp_path / "layout_d2_no_companion.xlsx"
    wb_d2.save(path_d2)
    res_d2 = import_excel_file(path_d2, generate_variants=True)
    assert res_d2["layout_type"] == "dokkai_info"
    assert res_d2["raw_count"] == 1
    assert res_d2["imported_count"] == 1
    assert res_d2["variants_generated"] >= 1

    conn = get_connection()
    try:
        info_q = conn.execute("SELECT unit_code, notebook_meta_json FROM QUESTIONS WHERE mondai_type='情報検索'").fetchone()
        assert info_q is not None
        assert info_q["unit_code"] == "MU-12"
        ev_idx = json.loads(info_q["notebook_meta_json"])["evidence_indices"]
        assert 1 in ev_idx  # 注意 line is sentence index 1
    finally:
        conn.close()

    # Unknown workbook / Dashboard-only workbook MUST raise ValueError
    wb_bad = openpyxl.Workbook()
    wb_bad.active.title = "Dashboard_Tong_Quan"
    bad_path = tmp_path / "dashboard_only_invalid.xlsx"
    wb_bad.save(bad_path)
    with pytest.raises(ValueError):
        import_excel_file(bad_path, generate_variants=False)


def test_import_edge_cases_zero_rows_row1_bracketless_multi_cloze_and_minimal_variants(tmp_path, isolated_db):
    """Test zero-row rejection, Row-1 data, bracketless passages, multi-cloze linking, and leak-free minimal variants."""
    # 1. Workbook matching Layout A sheet name but with 0 valid question rows MUST fail and not pollute SOURCE_WORKBOOKS
    wb_empty = openpyxl.Workbook()
    ws_empty = wb_empty.active
    ws_empty.title = "Tong_Hop_On_Thi"
    ws_empty.append(["Mondai", "Câu", "Từ khóa", "Đề bài", "Đ1", "Đ2", "Đ3", "Đ4", "T", "K", "ĐA"])
    empty_path = tmp_path / "empty_layout_a.xlsx"
    wb_empty.save(empty_path)
    with pytest.raises(ValueError, match="không có câu hỏi hợp lệ"):
        import_excel_file(empty_path, generate_variants=True)
    conn = get_connection()
    try:
        assert conn.execute("SELECT COUNT(*) FROM SOURCE_WORKBOOKS").fetchone()[0] == 0
    finally:
        conn.close()

    # 2. Row-1 headerless question (Layout A) + minimal metadata for 問題1/問題2 (no leaks, no empty brackets)
    wb_min = openpyxl.Workbook()
    ws_min = wb_min.active
    ws_min.title = "Tong_Hop_On_Thi"
    ws_min.append([
        "問題1: Cách đọc Kanji", 1, "", "新しい【技術】を学ぶ。",
        "きじゅつ", "ぎじゅつ", "ぎしゅつ", "きしゅつ", None, None, 2, "2. ぎじゅつ", "", "Đáp án đúng là 2.",
    ])
    ws_min.append([
        "問題2: Viết Kanji", 2, "機会 → きかい", "いい【きかい】があったら行きたい。",
        "機械", "機会", "奇怪", "帰会", None, None, 2, "2. 機会", "", "Đáp án đúng là 2.",
    ])
    min_path = tmp_path / "row1_minimal_vocab.xlsx"
    wb_min.save(min_path)
    res_min = import_excel_file(min_path, generate_variants=True)
    assert res_min["raw_count"] == 2
    assert res_min["imported_count"] == 2

    conn = get_connection()
    try:
        v_rows = conn.execute(
            "SELECT v.prompt_jp, v.options_json, v.correct_index, q.mondai_type FROM VARIANT_DRILLS v JOIN QUESTIONS q ON q.id=v.question_id"
        ).fetchall()
        assert len(v_rows) == 2
        for vr in v_rows:
            assert "【】" not in vr["prompt_jp"]
            assert "「」" not in vr["prompt_jp"]
            assert "(nghĩa: )" not in vr["prompt_jp"]
            opts = json.loads(vr["options_json"])
            ans = opts[vr["correct_index"]]
            assert ans not in vr["prompt_jp"]
    finally:
        conn.close()

    # 3. Row-1 bracketless Dokkai passage without 【...】 in Dokkai_Doan_Van_Ngan
    wb_bl = openpyxl.Workbook()
    ws_bl = wb_bl.active
    ws_bl.title = "Dokkai_Doan_Van_Ngan"
    ws_bl.append(["図書館は月曜日が休みです。火曜日から日曜日まで毎日開いています。", None, None, None, None, None, None, "Thư viện nghỉ thứ 2."])
    ws_bl.append([
        "Gói 1", "[1]", "図書館が休みの日はいつか。",
        "月曜日", "火曜日", "土曜日", "日曜日", None, None, 1, "1. 月曜日", "Đọc thông báo",
        "• Đáp án đúng: 1. Câu chốt: 「図書館は月曜日が休みです」.",
    ])
    bl_path = tmp_path / "row1_bracketless_dokkai.xlsx"
    wb_bl.save(bl_path)
    res_bl = import_excel_file(bl_path, generate_variants=True)
    assert res_bl["raw_count"] == 1
    conn = get_connection()
    try:
        q_bl = conn.execute(
            "SELECT id, passage_id FROM QUESTIONS WHERE prompt_jp LIKE '%図書館が休みの日%'"
        ).fetchone()
        assert q_bl is not None and q_bl["passage_id"] is not None
        ev_v = conn.execute(
            "SELECT variant_mode FROM VARIANT_DRILLS WHERE question_id=?", (q_bl["id"],)
        ).fetchone()
        assert ev_v is not None and ev_v["variant_mode"] == "dokkai_evidence"
    finally:
        conn.close()

    # 3b. Reading question without passage row falls back to Reading label (not Ngữ pháp)
    wb_nop = openpyxl.Workbook()
    ws_nop = wb_nop.active
    ws_nop.title = "Phan_III_Doc_Hai"
    ws_nop.append([
        "III-1. Bài đọc ngắn", "問1", "なぜ遅れたか。",
        "雨だから", "寝坊したから", "電車が止まったから", "道に迷ったから", None, None, 3, "3. 電車が止まったから",
        "Tìm lý do", "Đáp án đúng là 3.",
    ])
    nop_path = tmp_path / "reading_no_passage.xlsx"
    wb_nop.save(nop_path)
    res_nop = import_excel_file(nop_path, generate_variants=True)
    assert res_nop["raw_count"] == 1
    conn = get_connection()
    try:
        v_nop = conn.execute(
            "SELECT v.prompt_jp FROM VARIANT_DRILLS v JOIN QUESTIONS q ON q.id=v.question_id WHERE q.prompt_jp LIKE '%なぜ遅れたか%'"
        ).fetchone()
        assert v_nop is not None
        assert "Đọc hiểu" in v_nop["prompt_jp"]
        assert "Ngữ pháp" not in v_nop["prompt_jp"]
    finally:
        conn.close()

    # 4. Multiple 問題3 cloze passages in Phan_II_Ngu_Phap WITHOUT (Title) in pkg_raw
    wb_mc = openpyxl.Workbook()
    ws_mc = wb_mc.active
    ws_mc.title = "Phan_II_Ngu_Phap"
    ws_mc.append([
        "II-1. 問題1: Ngữ pháp câu đơn", "1)", "～ように", "日本語が話せる（　　　）毎日練習する。",
        "ように", "ために", "ことに", "そうに", None, None, 1, "1. ように", "", "Đáp án đúng là 1.",
    ])
    ws_mc.append([
        "II-3. 問題3: Ngữ pháp đoạn văn", "[1]", "～ため", "雨の [ 1 ] 中止になった。",
        "ため", "おかげ", "せい", "ほど", None, None, 1, "1. ため", "", "Đáp án đúng là 1.",
    ])
    ws_mc.append(["TOÀN VĂN ĐOẠN ĐỌC CỦA 問題3: 「Đoạn A」"])
    ws_mc.append(["【Đoạn văn gốc tiếng Nhật】\n雨の [ 1 ] 試合は中止になった。", None, None, None, None, None, None, "Trận đấu bị hủy do mưa."])
    ws_mc.append([
        "II-3. 問題3: Ngữ pháp đoạn văn", "[2]", "～ばかり", "毎日遊んで [ 2 ] いる。",
        "ばかり", "だけ", "しか", "こそ", None, None, 1, "1. ばかり", "", "Đáp án đúng là 1.",
    ])
    ws_mc.append(["TOÀN VĂN ĐOẠN ĐỌC CỦA 問題3: 「Đoạn B」"])
    ws_mc.append(["【Đoạn văn gốc tiếng Nhật】\n夏休みは毎日遊んで [ 2 ] いる。", None, None, None, None, None, None, "Nghỉ hè toàn chơi."])
    mc_path = tmp_path / "multi_cloze_p2.xlsx"
    wb_mc.save(mc_path)
    res_mc = import_excel_file(mc_path, generate_variants=True)
    assert res_mc["raw_count"] == 3

    conn = get_connection()
    try:
        # Verify Grammar 問題1 minimal variant doesn't leak 'ように'
        g1_v = conn.execute(
            "SELECT v.prompt_jp FROM VARIANT_DRILLS v JOIN QUESTIONS q ON q.id=v.question_id WHERE q.mondai_type='問題1' AND q.section='grammar'"
        ).fetchone()
        assert g1_v is not None
        assert "ように" not in g1_v["prompt_jp"]

        # Verify Cloze A linked to Đoạn A and Cloze B linked to Đoạn B
        qa = conn.execute(
            "SELECT p.title FROM QUESTIONS q JOIN PASSAGES p ON p.id=q.passage_id WHERE q.section='grammar' AND q.source_label='[1]'"
        ).fetchone()
        qb = conn.execute(
            "SELECT p.title FROM QUESTIONS q JOIN PASSAGES p ON p.id=q.passage_id WHERE q.section='grammar' AND q.source_label='[2]'"
        ).fetchone()
        assert qa["title"] == "Đoạn A"
        assert qb["title"] == "Đoạn B"
    finally:
        conn.close()
