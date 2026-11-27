"""Tests for 3-tier Furigana/Hán-Việt Scaffolding & strict 【...】 target masking."""

from n3_mastery.scaffolding import apply_scaffolding, determine_scaffold_tier, get_contextual_hint


def test_tier1_masks_target_keyword_and_annotates_background():
    prompt = "日本の夏は気温も【湿度】も高くて過ごしにくい。"
    options = ["しつけ", "しつど", "しっき", "しめど"]
    res = apply_scaffolding(prompt, options, stability=1.2, exam_mode=False, focus_keyword="湿度 → しつど")

    assert res["tier"] == 1
    # Target keyword MUST stay inside target-mask without any <ruby> or Hán-Việt
    assert '<span class="target-mask">【湿度】</span>' in res["prompt_html"]
    assert "しつど" not in res["prompt_html"]
    assert "THẤP ĐỘ" not in res["prompt_html"]
    # Background words MUST get scaffold <ruby> + Hán-Việt
    assert '<ruby class="scaffold-ruby"' in res["prompt_html"]
    assert "日本" in res["prompt_html"] and "にほん" in res["prompt_html"]
    assert "気温" in res["prompt_html"] and "きおん" in res["prompt_html"]
    # Background glossary excludes masked target word
    gl_words = {g["word"] for g in res["background_glossary"]}
    assert "湿度" not in gl_words
    assert "気温" in gl_words
    # Options MUST NOT get injected ruby
    assert all("scaffold-ruby" not in o for o in res["options_html"])


def test_tier2_hides_furigana_by_default_and_allows_safe_hint():
    prompt = "桜（さくら）の花は、もう【散】ってしまった。"
    options = ["いって", "まって", "さって", "ちって"]
    res = apply_scaffolding(prompt, options, stability=4.5, exam_mode=False, focus_keyword="散って")

    assert res["tier"] == 2
    assert res["hint_allowed"] is True
    assert "scaffold-ruby" not in res["prompt_html"]
    assert res["background_glossary"] == []
    # Exam-original furigana 桜（さくら） MUST be preserved
    assert '<ruby class="orig-ruby">桜<rt>さくら</rt></ruby>' in res["prompt_html"]
    assert '<span class="target-mask">【散】</span>' in res["prompt_html"]

    hint = get_contextual_hint(prompt, stability=4.5, exam_mode=False, focus_keyword="散って", bridge_focus="Vて chia nhóm 1")
    assert hint["allowed"] is True
    assert "ちって" not in (hint["hint_text"] or "")


def test_tier3_and_exam_mode_lock_all_artificial_scaffolding_and_hints():
    prompt = "その歌手は離婚のうわさを【否定】した。"
    options = ["ひて", "ふってい", "ひてい", "ふてい"]

    # Stability >= 7.0 triggers Tier 3
    assert determine_scaffold_tier(7.0, exam_mode=False) == 3
    res_t3 = apply_scaffolding(prompt, options, stability=7.5, exam_mode=False)
    assert res_t3["tier"] == 3
    assert res_t3["hint_allowed"] is False
    assert "scaffold-ruby" not in res_t3["prompt_html"]

    hint_t3 = get_contextual_hint(prompt, stability=7.5, exam_mode=False)
    assert hint_t3["allowed"] is False

    # Exam mode overrides even low stability (< 3.0) to Tier 3
    res_exam = apply_scaffolding(prompt, options, stability=0.5, exam_mode=True)
    assert res_exam["tier"] == 3
    assert "scaffold-ruby" not in res_exam["prompt_html"]
    assert res_exam["background_glossary"] == []

    hint_exam = get_contextual_hint(prompt, stability=0.5, exam_mode=True)
    assert hint_exam["allowed"] is False
