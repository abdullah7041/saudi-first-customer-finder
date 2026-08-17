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
    rendered = g.arabic(long_quote)
    assert "[…]" in rendered
    assert len(rendered) < len(long_quote) + 200


def test_short_quotes_are_left_alone():
    assert "[…]" not in g.arabic("ب" * 40)


def test_right_to_left_evidence_keeps_its_direction():
    """The worked example depends on this, so the rename tasks must not regress it."""
    rendered = g.arabic("أبغى أداة")
    assert 'dir="rtl"' in rendered
    assert 'lang="ar"' in rendered


def test_left_to_right_evidence_renders():
    """A German or Brazilian run must render evidence just as well as an Arabic one."""
    rendered = g.arabic("Ich suche ein Tool dafür")
    assert "Ich suche ein Tool" in rendered
