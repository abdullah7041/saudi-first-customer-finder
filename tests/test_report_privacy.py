import generate_report as g


def test_rejected_entries_never_reach_the_html():
    """A handle written into the JSON must not appear in the report.

    Aggregation lives in the generator precisely so a mistake upstream cannot
    leak an identity, so this asserts on the rendered page, not on the helper.
    """
    data = {
        "product": {"name": "Test"},
        "prospects": [],
        "rejected": [
            {"name": "@someone", "source_url": "https://x.com/someone/status/9",
             "platform": "X", "reason": "Out of market scope",
             "quote_ar": "identifying quote"},
            {"name": "@other", "platform": "X", "reason": "Out of market scope"},
        ],
    }
    html = g.build_html(data)
    assert "@someone" not in html
    assert "@other" not in html
    assert "identifying quote" not in html
    assert "https://x.com/someone/status/9" not in html


def test_rejections_are_counted_by_reason_and_platform():
    rows = g.aggregate_rejected([
        {"platform": "X", "reason": "Out of market scope"},
        {"platform": "X", "reason": "Out of market scope"},
        {"platform": "Reddit", "reason": "Vendor account"},
    ])
    assert ("Out of market scope", "X", 2) in rows
    assert ("Vendor account", "Reddit", 1) in rows


def test_quotes_are_truncated_at_the_ceiling():
    long_quote = "ب" * (g.QUOTE_CEILING + 120)
    rendered = g.quote_block(long_quote)
    assert "[…]" in rendered
    assert len(rendered) < len(long_quote) + 200


def test_short_quotes_are_left_alone():
    assert "[…]" not in g.quote_block("ب" * 40)


def test_right_to_left_evidence_keeps_its_direction():
    """The worked example depends on this, so the rename tasks must not regress it."""
    rendered = g.quote_block("أبغى أداة")
    assert 'dir="rtl"' in rendered
    assert 'lang="ar"' in rendered


def test_left_to_right_evidence_renders():
    """A German or Brazilian run must render evidence just as well as an Arabic one,
    with the direction and language tag the text actually deserves — not a hardcoded
    Arabic default."""
    rendered = g.quote_block("Ich suche ein Tool dafür")
    assert "Ich suche ein Tool" in rendered
    assert 'dir="ltr"' in rendered
    assert 'lang="ar"' not in rendered

    rendered_with_lang = g.quote_block("Ich suche ein Tool dafür", lang="de")
    assert 'dir="ltr"' in rendered_with_lang
    assert 'lang="de"' in rendered_with_lang


def _opener_html(prospect: dict) -> str:
    """render_prospect() builds the opener blockquote inline; isolate just that
    fragment so these tests read like the quote_block tests above rather than
    parsing the whole prospect card."""
    rendered = g.render_prospect(prospect, 1)
    start = rendered.find("<blockquote>")
    end = rendered.find("</blockquote>") + len("</blockquote>")
    assert start != -1, "expected an opener blockquote in the rendered prospect"
    return rendered[start:end]


def test_rtl_opener_keeps_its_direction():
    """An Arabic opener_ar with no declared opener_lang must still render rtl/ar —
    the worked example depends on this."""
    opener = _opener_html({"opener_ar": "شفت تغريدتك عن السيرة الذاتية"})
    assert 'dir="rtl"' in opener
    assert 'lang="ar"' in opener


def test_ltr_opener_renders_with_its_own_direction():
    """A German or Brazilian opener draft must not be tagged as Arabic."""
    opener = _opener_html({"opener_ar": "Ich habe deinen Beitrag gesehen"})
    assert 'dir="ltr"' in opener
    assert 'lang="ar"' not in opener


def test_opener_uses_explicit_opener_lang_when_given():
    opener = _opener_html({"opener_ar": "Ich habe deinen Beitrag gesehen", "opener_lang": "de"})
    assert 'dir="ltr"' in opener
    assert 'lang="de"' in opener


def test_opener_with_no_opener_lang_infers_conservatively():
    """No opener_lang and an RTL text still infers 'ar' (documented conservative
    default); no opener_lang and an LTR text gets a direction but no lang guess."""
    rtl_opener = _opener_html({"opener_ar": "أبغى أداة"})
    assert 'dir="rtl"' in rtl_opener
    assert 'lang="ar"' in rtl_opener

    ltr_opener = _opener_html({"opener_ar": "I saw your post about this"})
    assert 'dir="ltr"' in ltr_opener
    assert "lang=" not in ltr_opener
