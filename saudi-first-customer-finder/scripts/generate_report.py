#!/usr/bin/env python3
"""Generate a standalone bilingual First Customer Finder HTML report from JSON.

Usage:
    python3 generate_report.py analysis.json outputs/saudi-first-customer-report.html

Self-contained: no external assets, no CDN, no storage APIs. Renders Arabic evidence
right-to-left beside English analysis, and is print/PDF friendly.
"""

from __future__ import annotations

import argparse
import html
import json
import unicodedata
from datetime import date, datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


DIMENSIONS = {
    "scope_match": ("Scope match", 20),
    "pain_strength": ("Pain strength", 20),
    "product_fit": ("Product fit", 20),
    "timing": ("Timing", 15),
    "reachability": ("Reachability", 10),
    "evidence_quality": ("Evidence quality", 15),
}

SECTIONS = [
    ("dashboard", "At a glance"),
    ("prospects", "Prospects"),
    ("rejected", "Rejected"),
    ("patterns", "Patterns"),
    ("competitors", "Competition"),
    ("gaps", "Feature gaps"),
    ("vocabulary", "Vocabulary"),
    ("channels", "Channels"),
    ("objections", "Objections"),
    ("plan", "Plan"),
    ("limits", "Limits"),
]


# --------------------------------------------------------------------------- helpers

def esc(value: Any) -> str:
    return html.escape(str(value if value is not None else ""), quote=True)


def clamp(value: Any, maximum: int = 100) -> int:
    try:
        number = round(float(value))
    except (TypeError, ValueError):
        number = 0
    return max(0, min(maximum, number))


def items(value: Any) -> list[Any]:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def dicts(value: Any) -> list[dict[str, Any]]:
    return [x for x in items(value) if isinstance(x, dict)]


def safe_url(value: Any) -> str:
    raw = str(value or "").strip()
    parsed = urlparse(raw)
    return esc(raw) if parsed.scheme in {"http", "https"} and parsed.netloc else "#"


def parse_date(value: Any) -> date | None:
    raw = str(value or "").strip()[:10]
    for fmt in ("%Y-%m-%d", "%Y-%m", "%Y"):
        try:
            return datetime.strptime(raw, fmt).date()
        except ValueError:
            continue
    return None


def stage_class(stage: Any) -> str:
    value = str(stage or "").lower()
    if "high" in value:
        return "hot"
    if "problem" in value or "trigger" in value:
        return "warm"
    return "cool"


def tier_badge(tier: Any) -> str:
    value = str(tier or "").lower()
    labels = {
        "confirmed": ("confirmed", "Confirmed in-market"),
        "likely": ("likely", "Likely in-market"),
        "rejected": ("rejected", "Rejected"),
    }
    cls, label = labels.get(value, ("unverified", "Unverified"))
    return f'<span class="tier {cls}">{label}</span>'


# One or two sentences is enough to prove a signal. Past that the report stops being
# evidence and starts republishing someone's post in full.
QUOTE_CEILING = 280


# Unicode bidi classes that establish right-to-left direction under the
# first-strong-character rule — the same rule behind HTML's dir="auto".
_RTL_BIDI_CLASSES = {"R", "AL"}


def base_direction(text: str) -> str:
    """First-strong-character text direction: 'rtl' or 'ltr'.

    Walks the string and returns as soon as a character with a strong
    direction is found (Unicode bidi class R/AL for right-to-left, L for
    left-to-right). Neutral characters (digits, punctuation, whitespace) are
    skipped. Falls back to 'ltr' if nothing strong is found.
    """
    for ch in text:
        bidi = unicodedata.bidirectional(ch)
        if bidi in _RTL_BIDI_CLASSES:
            return "rtl"
        if bidi == "L":
            return "ltr"
    return "ltr"


def quote_block(text: Any, label: str = "Original quote", lang: Any = None) -> str:
    """Render a verbatim evidence quote in its own language and direction.

    `lang` should come from a per-quote language field in the source JSON
    (e.g. "de", "pt", "ar") whenever the caller has it — that is always more
    reliable than guessing. When it is absent, direction is inferred from
    the text itself via the first-strong-character rule. A language *code*
    is only ever inferred for the right-to-left case (defaulting to "ar",
    since Arabic is this skill's overwhelmingly common right-to-left
    source); a left-to-right quote with no declared language gets the
    correct direction but no `lang` attribute, because Latin script alone
    does not say which language it is.
    """
    value = str(text or "").strip()
    if not value:
        return ""
    if len(value) > QUOTE_CEILING:
        value = value[:QUOTE_CEILING].rstrip() + " […]"
    direction = base_direction(value)
    declared_lang = str(lang or "").strip()
    if declared_lang:
        lang_attr = f' lang="{esc(declared_lang)}"'
    elif direction == "rtl":
        lang_attr = ' lang="ar"'
    else:
        lang_attr = ""
    return (
        f'<div class="ar-block"><span>{esc(label)}</span>'
        f'<p dir="{direction}"{lang_attr}>{esc(value)}</p></div>'
    )


def verified_flag(prospect: dict[str, Any]) -> str:
    if prospect.get("link_verified") is True:
        when = esc(prospect.get("verified_at", ""))
        return f'<span class="verified">&#10003; Link verified{" · " + when if when else ""}</span>'
    return '<span class="verified bad">&#10007; Link NOT verified — do not rely on this entry</span>'


def bars(rows: list[tuple[str, int]], accent: str = "green") -> str:
    """Horizontal labelled bar chart. rows = [(label, count)]."""
    if not rows:
        return '<p class="empty">No data</p>'
    peak = max((c for _, c in rows), default=0) or 1
    out = []
    for label, count in rows:
        pct = round(count / peak * 100)
        out.append(
            f'<div class="bar"><span>{esc(label)}</span>'
            f'<div class="bar-track"><i class="{accent}" style="width:{max(pct, 2)}%"></i></div>'
            f'<b>{count}</b></div>'
        )
    return "".join(out)


# --------------------------------------------------------------------------- sections

def render_dimensions(data: dict[str, Any]) -> str:
    out = []
    for key, (label, weight) in DIMENSIONS.items():
        score = clamp(data.get(key, 0), 5)
        out.append(
            f'<div class="metric"><span>{esc(label)} <em>{weight}%</em></span>'
            f'<div class="track"><i style="width:{score * 20}%"></i></div><b>{score}/5</b></div>'
        )
    return "".join(out)


def render_prospect(prospect: dict[str, Any], index: int) -> str:
    score = clamp(prospect.get("score"))
    source = safe_url(prospect.get("source_url"))
    markers = items(prospect.get("scope_markers"))
    marker_html = "".join(f"<li>{esc(m)}</li>" for m in markers)
    opener = str(prospect.get("opener_ar") or "").strip()
    opener_html = ""
    if opener:
        note = esc(prospect.get("opener_note", "Unsent draft — review before using."))
        opener_direction = base_direction(opener)
        opener_lang = str(prospect.get("opener_lang") or "").strip()
        if not opener_lang and opener_direction == "rtl":
            opener_lang = "ar"
        opener_lang_attr = f' lang="{esc(opener_lang)}"' if opener_lang else ""
        opener_html = (
            f'<blockquote><span>Suggested opener &middot; unsent draft</span>'
            f'<p dir="{opener_direction}"{opener_lang_attr}>{esc(opener)}</p><small>{note}</small></blockquote>'
        )

    return f"""
    <article class="prospect reveal">
      <header class="prospect-head">
        <div class="rank">{index:02d}</div>
        <div class="identity">
          <span class="eyebrow">{esc(prospect.get('type', 'Public prospect'))} &middot; {esc(prospect.get('platform', ''))}</span>
          <h3>{esc(prospect.get('name', f'Prospect {index}'))}</h3>
          <div class="badges">
            <span class="stage {stage_class(prospect.get('stage'))}">{esc(prospect.get('stage', 'Potential fit'))}</span>
            {tier_badge(prospect.get('scope_tier'))}
            <span class="chip date">{esc(prospect.get('signal_date', 'Date unavailable'))}</span>
          </div>
        </div>
        <div class="score" style="--score:{score}" aria-label="Fit score {score} out of 100"><strong>{score}</strong><small>/100</small></div>
      </header>

      {quote_block(prospect.get('quote_ar'), lang=prospect.get('quote_lang'))}
      <div class="signal"><span>What they said &middot; English</span><p>{esc(prospect.get('quote_en') or prospect.get('pain_signal', ''))}</p></div>

      <div class="prospect-grid">
        <div><span>Why it fits</span><p>{esc(prospect.get('why_fit', ''))}</p></div>
        <div><span>Why now</span><p>{esc(prospect.get('why_now', ''))}</p></div>
        <div><span>Suggested channel</span><p>{esc(prospect.get('suggested_channel', ''))}</p></div>
        <div class="warn"><span>Caution</span><p>{esc(prospect.get('caution', 'Confirm current relevance before any contact.'))}</p></div>
      </div>
      {opener_html}

      <details>
        <summary>Evidence, identity markers, and score breakdown</summary>
        <div class="evidence">
          <div><span>Evidence</span><p>{esc(prospect.get('evidence', ''))}</p></div>
          <div>
            <span>Source</span>
            <p>{esc(prospect.get('source_type', 'Public source'))}</p>
            <a href="{source}" target="_blank" rel="noreferrer">{esc(prospect.get('source_title', 'Open original source'))} &#8599;</a>
            <p>{verified_flag(prospect)}</p>
          </div>
        </div>
        <div class="markers"><span>Scope markers</span><ul>{marker_html or '<li>None recorded</li>'}</ul></div>
        <div class="metrics">{render_dimensions(prospect.get('dimensions') if isinstance(prospect.get('dimensions'), dict) else {})}</div>
      </details>
    </article>"""


def aggregate_rejected(entries: list[dict[str, Any]]) -> list[tuple[str, str, int]]:
    """Collapse the rejection log to reason x platform counts.

    The log exists to prove the identity filter ran, and a count proves that. Naming
    the individuals does not: a handle published beside an inferred nationality and the
    word "rejected" is a sensitive inference about a real person, in an artifact built
    to be shared. Aggregation happens here rather than upstream so that a handle written
    into the JSON still cannot reach the page.
    """
    counts: dict[tuple[str, str], int] = {}
    for entry in entries:
        reason = str(entry.get("reason") or "No reason recorded").strip()
        platform = str(entry.get("platform") or "unspecified").strip()
        counts[(reason, platform)] = counts.get((reason, platform), 0) + 1
    return [(r, p, n) for (r, p), n in sorted(counts.items(), key=lambda kv: -kv[1])]


def render_rejected(row: tuple[str, str, int]) -> str:
    reason, platform, count = row
    return f"""
    <tr>
      <td data-l="Reason"><b>{esc(reason)}</b></td>
      <td data-l="Platform">{esc(platform)}</td>
      <td data-l="Count">{count}</td>
    </tr>"""


def render_pattern(pattern: dict[str, Any], index: int, kind: str = "") -> str:
    return f"""
    <article class="pattern reveal {kind}">
      <span class="pattern-num">{index:02d}</span>
      <div>
        <h3>{esc(pattern.get('title', 'Repeated signal'))}</h3>
        <p>{esc(pattern.get('insight', ''))}</p>
        {quote_block(pattern.get('quote_ar'), 'Representative quote', pattern.get('quote_lang'))}
      </div>
      <strong>{clamp(pattern.get('count'), 999)}&times;</strong>
    </article>"""


def render_gap(gap: dict[str, Any], index: int) -> str:
    kind = str(gap.get("type", "")).lower()
    tag = (
        '<span class="tag build">Build</span>' if kind == "build"
        else '<span class="tag message">Message</span>' if kind == "message"
        else ""
    )
    return f"""
    <article class="pattern reveal">
      <span class="pattern-num">{index:02d}</span>
      <div>
        <h3>{esc(gap.get('title', 'Gap'))} {tag}</h3>
        <p>{esc(gap.get('insight', ''))}</p>
        {quote_block(gap.get('quote_ar'), 'Evidence', gap.get('quote_lang'))}
      </div>
      <strong>{clamp(gap.get('count'), 999)}&times;</strong>
    </article>"""


def render_competitor(c: dict[str, Any]) -> str:
    source = safe_url(c.get("source_url"))
    link = f'<a href="{source}" target="_blank" rel="noreferrer">Open &#8599;</a>' if source != "#" else ""
    threat = str(c.get("threat", "")).lower()
    threat_cls = "hot" if threat == "high" else "warm" if threat == "medium" else "cool"
    return f"""
    <article class="competitor">
      <header>
        <h3>{esc(c.get('name', 'Competitor'))}</h3>
        <span class="stage {threat_cls}">{esc(c.get('threat', 'unknown'))} threat</span>
      </header>
      <span class="chip">{esc(c.get('platform', ''))}</span>
      <span class="chip">{esc(c.get('kind', ''))}</span>
      <p>{esc(c.get('offer', ''))}</p>
      <div class="comp-meta">
        <div><span>How they take orders</span><p>{esc(c.get('order_channel', 'Unknown'))}</p></div>
        <div><span>Visible price</span><p>{esc(c.get('price', 'Not stated'))}</p></div>
      </div>
      {quote_block(c.get('quote_ar'), 'Their pitch', c.get('quote_lang'))}
      {link}
    </article>"""


def render_vocab(term: dict[str, Any]) -> str:
    return f"""
    <tr>
      <td data-l="Arabic" dir="rtl" lang="ar" class="ar-cell">{esc(term.get('term_ar', ''))}</td>
      <td data-l="Meaning">{esc(term.get('meaning_en', ''))}</td>
      <td data-l="Count" class="num">{clamp(term.get('count'), 9999)}</td>
      <td data-l="Use">{esc(term.get('use', ''))}</td>
    </tr>"""


def render_channel(channel: dict[str, Any]) -> str:
    return f"""
    <article class="channel">
      <h3>{esc(channel.get('name', 'Channel'))}</h3>
      <span class="chip">{esc(channel.get('platform', ''))}</span>
      <p>{esc(channel.get('why', ''))}</p>
      <div class="channel-meta">
        <div><span>Activity</span><p>{esc(channel.get('activity', 'Unknown'))}</p></div>
        <div><span>Rules</span><p>{esc(channel.get('rules', 'Check before participating'))}</p></div>
      </div>
    </article>"""


# --------------------------------------------------------------------------- dashboard

def build_dashboard(prospects: list[dict[str, Any]], generated: date | None) -> str:
    score_rows = [
        ("80-100 strong", sum(1 for p in prospects if clamp(p.get("score")) >= 80)),
        ("65-79 promising", sum(1 for p in prospects if 65 <= clamp(p.get("score")) < 80)),
        ("55-64 thin", sum(1 for p in prospects if 55 <= clamp(p.get("score")) < 65)),
    ]

    platforms: dict[str, int] = {}
    for p in prospects:
        key = str(p.get("platform") or "Unknown").strip() or "Unknown"
        platforms[key] = platforms.get(key, 0) + 1
    platform_rows = sorted(platforms.items(), key=lambda kv: -kv[1])

    buckets = [("0-30 days", 0), ("1-3 months", 0), ("3-6 months", 0), ("6-12 months", 0), ("Older / unknown", 0)]
    counts = dict(buckets)
    for p in prospects:
        signal = parse_date(p.get("signal_date"))
        if not signal or not generated:
            counts["Older / unknown"] += 1
            continue
        days = (generated - signal).days
        if days <= 30:
            counts["0-30 days"] += 1
        elif days <= 92:
            counts["1-3 months"] += 1
        elif days <= 183:
            counts["3-6 months"] += 1
        elif days <= 365:
            counts["6-12 months"] += 1
        else:
            counts["Older / unknown"] += 1
    fresh_rows = [(k, counts[k]) for k, _ in buckets]

    tiers = [
        ("Confirmed in-market", sum(1 for p in prospects if str(p.get("scope_tier", "")).lower() == "confirmed")),
        ("Likely in-market", sum(1 for p in prospects if str(p.get("scope_tier", "")).lower() == "likely")),
    ]

    return f"""
      <div class="dash">
        <article><h3>Score distribution</h3>{bars(score_rows)}</article>
        <article><h3>Platform mix</h3>{bars(platform_rows, 'blue')}</article>
        <article><h3>Signal freshness</h3>{bars(fresh_rows, 'sand')}</article>
        <article><h3>Identity confidence</h3>{bars(tiers, 'cyan')}</article>
      </div>"""


# --------------------------------------------------------------------------- styles

CSS = """
:root{--bg:#07090c;--panel:#10141b;--panel2:#161c25;--ink:#f7f4ed;--muted:#96a1b0;
--line:#252d3a;--line2:#323c4c;--green:#00c265;--sand:#e9c987;--blue:#6fb6ff;--cyan:#5ee8d0;
--amber:#ffab5e;--red:#ff7a7a;--radius:16px;--shadow:0 24px 80px rgba(0,0,0,.42)}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:78px}
body{margin:0;background:var(--bg);color:var(--ink);line-height:1.55;
font-family:Inter,ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
-webkit-font-smoothing:antialiased}
body:before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;
background:radial-gradient(1100px 520px at 78% -8%,rgba(0,194,101,.13),transparent 62%),
radial-gradient(760px 420px at 4% 6%,rgba(111,182,255,.09),transparent 60%)}
a{color:inherit}.skip{position:absolute;left:-9999px}
.skip:focus{left:16px;top:16px;z-index:99;background:var(--green);color:#04150c;padding:10px}
.shell{width:min(1200px,calc(100% - 40px));margin:auto;position:relative;z-index:1}
.empty{color:var(--muted);font-size:13px;margin:0}

/* nav */
.top{position:sticky;top:0;z-index:40;background:rgba(7,9,12,.82);backdrop-filter:blur(14px);
border-bottom:1px solid var(--line)}
.top-in{width:min(1200px,calc(100% - 40px));margin:auto;display:flex;justify-content:space-between;
align-items:center;gap:16px;padding:13px 0}
.brand{font-weight:850;display:flex;align-items:center;gap:9px;white-space:nowrap;font-size:15px}
.brand i{width:11px;height:11px;border-radius:50%;background:var(--green);box-shadow:0 0 20px var(--green)}
.nav{display:flex;gap:2px;overflow-x:auto;scrollbar-width:none}.nav::-webkit-scrollbar{display:none}
.nav a{padding:7px 11px;border-radius:8px;color:var(--muted);text-decoration:none;
font:700 12px inherit;white-space:nowrap}
.nav a:hover{color:var(--ink);background:var(--panel2)}
button{background:var(--ink);color:#111;border:0;border-radius:999px;padding:8px 14px;
font:800 12px inherit;cursor:pointer;white-space:nowrap}
button:focus-visible,summary:focus-visible,a:focus-visible{outline:3px solid var(--blue);outline-offset:3px}
.chip,.stage,.tier,.tag{border:1px solid var(--line2);border-radius:999px;padding:5px 10px;color:var(--muted);
font:750 10px ui-monospace,monospace;text-transform:uppercase;letter-spacing:.07em;display:inline-block}

/* hero */
.hero{display:grid;grid-template-columns:1.5fr .5fr;gap:36px;align-items:end;padding:62px 0 38px}
.eyebrow{color:var(--green);font:750 11px ui-monospace,monospace;text-transform:uppercase;letter-spacing:.11em}
h1{font-size:clamp(42px,6.4vw,84px);line-height:.93;letter-spacing:-.062em;margin:12px 0 22px}
.verdict{font-size:clamp(17px,2vw,23px);color:#dbe1e9;max-width:820px;margin:0;text-wrap:pretty}
.hero-card{background:linear-gradient(150deg,var(--green),#00934c);color:#04150c;padding:24px;
border-radius:var(--radius);box-shadow:var(--shadow)}
.hero-card span{font:800 10px ui-monospace,monospace;text-transform:uppercase;letter-spacing:.08em}
.hero-card strong{display:block;font-size:60px;line-height:1;letter-spacing:-.08em;margin:14px 0 6px}
.hero-card p{margin:0;font-weight:700;font-size:12px}

/* strips */
.stats{display:grid;grid-template-columns:repeat(4,1fr);border:1px solid var(--line);
border-radius:var(--radius);overflow:hidden;margin-bottom:12px;background:var(--panel)}
.stats>div{padding:16px}.stats>div+div{border-left:1px solid var(--line)}
.stats span,.prospect-grid span,.signal span,.evidence span,blockquote span,.ar-block span,
.markers span,.channel-meta span,.comp-meta span,.icp span,.audit span
{display:block;color:var(--muted);font:700 10px ui-monospace,monospace;text-transform:uppercase;
letter-spacing:.08em;margin-bottom:5px}
.stats strong{font-size:16px}
.audit{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:12px}
.audit>div{border:1px dashed var(--line2);border-radius:12px;padding:14px;background:rgba(255,255,255,.012)}
.audit b{display:block;font-size:25px;color:var(--sand);letter-spacing:-.03em}
.icp{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:26px}
.icp>div{border:1px solid var(--line);border-radius:12px;padding:14px;background:var(--panel)}
.icp span{color:var(--green)}.icp p{margin:0;font-size:14px}

/* dashboard */
.dash{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:64px}
.dash article{border:1px solid var(--line);border-radius:14px;padding:18px;background:var(--panel)}
.dash h3{margin:0 0 14px;font-size:13px;color:var(--muted);text-transform:uppercase;
letter-spacing:.08em;font-family:ui-monospace,monospace}
.bar{display:grid;grid-template-columns:1fr 60px 26px;gap:8px;align-items:center;
margin-bottom:9px;font-size:12px;color:var(--muted)}
.bar-track{height:7px;background:var(--line);border-radius:7px;overflow:hidden}
.bar-track i{display:block;height:100%;border-radius:7px;background:var(--green)}
.bar-track i.blue{background:var(--blue)}.bar-track i.sand{background:var(--sand)}
.bar-track i.cyan{background:var(--cyan)}
.bar b{color:var(--ink);text-align:right;font-size:13px}

/* best */
.best{display:grid;grid-template-columns:200px 1fr auto;gap:22px;align-items:center;padding:24px;
background:linear-gradient(150deg,var(--sand),#d9b464);color:#1b1408;border-radius:var(--radius);
box-shadow:var(--shadow);margin:0 0 64px}
.best-label{font:800 10px ui-monospace,monospace;text-transform:uppercase;letter-spacing:.1em}
.best h2{font-size:clamp(25px,3.4vw,40px);letter-spacing:-.045em;line-height:1;margin:0 0 8px}
.best p{margin:0;font-size:15px}.best strong{font-size:42px}

/* sections */
.section-head{display:flex;justify-content:space-between;align-items:end;gap:24px;
padding-bottom:16px;border-bottom:1px solid var(--line);margin-bottom:18px}
.section-head h2{font-size:clamp(28px,4.4vw,54px);line-height:.98;letter-spacing:-.055em;margin:0}
.section-head p{color:var(--muted);max-width:460px;margin:0;font-size:14px}
section{scroll-margin-top:78px}

/* prospects */
.prospects{display:grid;gap:14px;margin-bottom:64px}
.prospect{background:linear-gradient(150deg,var(--panel),#0d1116);border:1px solid var(--line);
border-radius:var(--radius);padding:24px;box-shadow:0 12px 38px rgba(0,0,0,.2)}
.prospect:hover{border-color:var(--line2)}
.prospect-head{display:grid;grid-template-columns:50px 1fr 88px;gap:16px;align-items:start}
.rank{font:850 23px ui-monospace,monospace;color:var(--green);padding-top:8px}
.identity h3{font-size:26px;letter-spacing:-.04em;margin:5px 0 9px;word-break:break-word}
.badges{display:flex;gap:5px;flex-wrap:wrap}
.stage.hot{color:var(--amber);border-color:rgba(255,171,94,.5)}
.stage.warm{color:var(--cyan);border-color:rgba(94,232,208,.45)}
.tier.confirmed{color:var(--green);border-color:rgba(0,194,101,.55)}
.tier.likely{color:var(--sand);border-color:rgba(233,201,135,.45)}
.tier.rejected{color:var(--red);border-color:rgba(255,122,122,.45)}
.tag.build{color:var(--blue);border-color:rgba(111,182,255,.5)}
.tag.message{color:var(--cyan);border-color:rgba(94,232,208,.45)}
.score{--score:0;width:84px;height:84px;border-radius:50%;display:grid;place-content:center;
text-align:center;background:radial-gradient(circle,var(--panel) 57%,transparent 59%),
conic-gradient(var(--green) calc(var(--score)*1%),var(--line) 0)}
.score strong{font-size:25px;line-height:1}.score small{color:var(--muted);font-size:11px}
.ar-block{margin:18px 0 10px;padding:17px;background:rgba(0,194,101,.07);
border:1px solid rgba(0,194,101,.26);border-radius:12px}
.ar-block p{margin:0;font-size:20px;line-height:1.95}
.ar-block p[dir="rtl"]{font-family:"Noto Naskh Arabic","Geeza Pro","Segoe UI",Tahoma,"Arabic Typesetting",serif}
.ar-block p[dir="ltr"]{font-family:Inter,ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
.ar-cell{font-size:17px;font-family:"Noto Naskh Arabic","Geeza Pro","Segoe UI",Tahoma,serif}
.signal{margin:10px 0 12px;padding:15px;background:var(--panel2);border-left:3px solid var(--green);
border-radius:0 10px 10px 0}
.signal p{font-size:15px;margin:0}
.prospect-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.prospect-grid>div,.evidence>div,.markers{border:1px solid var(--line);border-radius:11px;
padding:14px;background:rgba(255,255,255,.015)}
.prospect-grid .warn{border-color:rgba(255,171,94,.3)}
.prospect-grid p,.evidence p{margin:0;font-size:14px}
blockquote{margin:12px 0 0;padding:16px;border:1px dashed rgba(0,194,101,.48);
border-radius:12px;background:rgba(0,194,101,.04)}
blockquote p{margin:0 0 8px;font-size:18px;line-height:1.95}
blockquote p[dir="rtl"]{font-family:"Noto Naskh Arabic","Geeza Pro","Segoe UI",Tahoma,serif}
blockquote p[dir="ltr"]{font-family:Inter,ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
blockquote small{color:var(--muted);font-size:11px}
details{margin-top:10px}
summary{cursor:pointer;color:var(--green);font-weight:800;padding:9px 0;font-size:13px}
.evidence{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.evidence a{display:inline-block;color:var(--blue);margin-top:7px;word-break:break-word;font-size:13px}
.verified{display:inline-block;margin-top:7px;color:var(--green);font:700 11px ui-monospace,monospace}
.verified.bad{color:var(--red)}
.markers{margin-top:8px}.markers ul{margin:0;padding-left:17px;color:var(--muted);font-size:13px}
.metrics{display:grid;gap:7px;margin-top:13px}
.metric{display:grid;grid-template-columns:190px 1fr 38px;gap:11px;align-items:center;font-size:12px}
.metric span{margin:0;text-transform:none;letter-spacing:0;font-family:inherit;font-size:12px}
.metric em{color:var(--line2);font-style:normal}
.track{height:7px;background:var(--line);border-radius:7px;overflow:hidden}
.track i{display:block;height:100%;background:linear-gradient(90deg,var(--blue),var(--green))}

/* tables */
table{width:100%;border-collapse:collapse;border:1px solid var(--line);border-radius:var(--radius);
overflow:hidden;margin-bottom:64px;background:var(--panel)}
th,td{text-align:left;padding:12px 14px;border-bottom:1px solid var(--line);font-size:14px;vertical-align:top}
th{background:var(--panel2);color:var(--muted);font:700 10px ui-monospace,monospace;
text-transform:uppercase;letter-spacing:.08em}
td small{display:block;color:var(--muted);margin-top:4px}
td.num{color:var(--sand);font-weight:800}tr:last-child td{border-bottom:0}

/* patterns + competitors + channels */
.patterns{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-bottom:64px}
.pattern{display:grid;grid-template-columns:38px 1fr auto;gap:14px;align-items:start;padding:19px;
border:1px solid var(--line);border-radius:14px;background:var(--panel)}
.pattern-num{color:var(--green);font:800 12px ui-monospace,monospace;padding-top:3px}
.pattern h3{margin:0 0 5px;font-size:17px;letter-spacing:-.02em}
.pattern p{margin:0;color:var(--muted);font-size:14px}
.pattern>strong{font-size:26px;color:var(--green)}
.pattern .ar-block{margin:11px 0 0;padding:11px}.pattern .ar-block p{font-size:16px}
.objection{border-color:rgba(255,122,122,.28)}
.objection .pattern-num,.objection>strong{color:var(--red)}
.competitors{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:64px}
.competitor{border:1px solid var(--line);border-radius:14px;padding:18px;background:var(--panel)}
.competitor header{display:flex;justify-content:space-between;align-items:start;gap:10px;margin-bottom:9px}
.competitor h3{margin:0;font-size:17px;word-break:break-word}
.competitor p{margin:9px 0 0;color:var(--muted);font-size:14px}
.comp-meta{display:grid;gap:8px;margin-top:12px}
.comp-meta p{margin:0;color:var(--ink);font-size:13px}
.competitor .ar-block{margin:11px 0}.competitor .ar-block p{font-size:16px}
.competitor>a{color:var(--blue);font-size:13px}
.channels{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:64px}
.channel{border:1px solid var(--line);border-radius:14px;padding:18px;background:var(--panel)}
.channel h3{margin:0 0 8px;font-size:16px;word-break:break-word}
.channel p{margin:8px 0 0;color:var(--muted);font-size:14px}
.channel-meta{display:grid;gap:8px;margin-top:11px}
.channel-meta p{margin:0;color:var(--ink);font-size:13px}

/* plan + limits */
.plan{display:grid;grid-template-columns:.8fr 1.2fr;gap:26px;
background:linear-gradient(150deg,var(--green),#00934c);color:#04150c;padding:28px;
border-radius:var(--radius);margin-bottom:28px}
.plan h2{font-size:32px;line-height:1.06;letter-spacing:-.045em;margin:10px 0}
.plan-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.plan-grid>div{border:1px solid rgba(0,0,0,.22);border-radius:11px;padding:13px;
background:rgba(255,255,255,.1)}
.plan-grid span{display:block;font:750 10px ui-monospace,monospace;text-transform:uppercase;
letter-spacing:.07em;margin-bottom:5px}
.plan-grid p{margin:0;font-size:13px}
.limits{border:1px solid var(--line);border-radius:var(--radius);padding:24px;
color:var(--muted);margin-bottom:52px;background:var(--panel)}
.limits h2{color:var(--ink);margin-top:0;font-size:22px}
.limits li{margin-bottom:7px}
footer{display:flex;justify-content:space-between;gap:20px;border-top:1px solid var(--line);
padding:20px 0 40px;color:var(--muted);font-size:12px}
.reveal{animation:rise .4s ease both}@keyframes rise{from{opacity:0;transform:translateY(10px)}}

@media(max-width:1000px){.dash,.competitors,.channels{grid-template-columns:repeat(2,1fr)}
.icp,.audit{grid-template-columns:repeat(2,1fr)}}
@media(max-width:820px){.shell,.top-in{width:min(100% - 22px,1200px)}
.hero,.plan{grid-template-columns:1fr}.hero{padding-top:38px}
.stats{grid-template-columns:1fr 1fr}.stats>div+div{border-left:0;border-top:1px solid var(--line)}
.best{grid-template-columns:1fr}.prospect-head{grid-template-columns:34px 1fr}.score{grid-column:1/-1}
.prospect-grid,.evidence,.patterns,.plan-grid,.dash,.competitors,.channels,.icp,.audit{grid-template-columns:1fr}
.metric{grid-template-columns:135px 1fr 36px}.brand span{display:none}
table,tbody,tr,td{display:block;width:100%}thead{display:none}
td{border-bottom:0;padding:6px 14px}td:before{content:attr(data-l);display:block;
color:var(--muted);font:700 9px ui-monospace,monospace;text-transform:uppercase;letter-spacing:.08em}
tr{border-bottom:1px solid var(--line);padding:10px 0}}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important;
scroll-behavior:auto!important}}
@media print{body{background:#fff;color:#111}body:before{display:none}
.top{position:static;background:#fff}.top button,.nav{display:none}
.shell{width:100%}.prospect,.pattern,.limits,.channel,.competitor,table,.dash article
{background:#fff;color:#111;break-inside:avoid;border-color:#ccc}
.ar-block{background:#f3f9f5}.signal{background:#f6f6f6}
.prospect-grid span,.signal span,.evidence span,blockquote span,.dash h3{color:#555}
details{display:block}summary{color:#111}
h1{font-size:38px}.section-head h2{font-size:26px}}
"""


# --------------------------------------------------------------------------- document

def build_html(data: dict[str, Any]) -> str:
    prospects = dicts(data.get("prospects"))
    rejected = dicts(data.get("rejected"))
    patterns = dicts(data.get("patterns"))
    intel = data.get("product_intelligence") if isinstance(data.get("product_intelligence"), dict) else {}
    gaps = dicts(intel.get("feature_gaps"))
    vocab = dicts(intel.get("vocabulary"))
    channels = dicts(intel.get("channels"))
    objections = dicts(intel.get("objections"))
    competitors = dicts(intel.get("competitors")) or dicts(data.get("competitors"))
    icp = data.get("icp") if isinstance(data.get("icp"), dict) else {}
    stats = data.get("stats") if isinstance(data.get("stats"), dict) else {}
    plan = data.get("plan") if isinstance(data.get("plan"), dict) else {}

    scores = [clamp(p.get("score")) for p in prospects]
    average = round(sum(scores) / len(scores)) if scores else 0
    high_intent = sum(1 for p in prospects if "high" in str(p.get("stage", "")).lower())
    confirmed = sum(1 for p in prospects if str(p.get("scope_tier", "")).lower() == "confirmed")
    top = max(prospects, key=lambda p: clamp(p.get("score")), default={})
    generated = parse_date(data.get("generated_at")) or date.today()

    limits = "".join(f"<li>{esc(x)}</li>" for x in items(data.get("limits")))
    disqualifiers = ", ".join(str(x) for x in items(icp.get("disqualifiers"))) or "Not specified"

    nav = "".join(f'<a href="#{sid}">{esc(label)}</a>' for sid, label in SECTIONS)

    prospect_html = "".join(render_prospect(p, i) for i, p in enumerate(prospects, 1))
    rejected_html = "".join(render_rejected(r) for r in aggregate_rejected(rejected))
    pattern_html = "".join(render_pattern(p, i) for i, p in enumerate(patterns, 1))
    gap_html = "".join(render_gap(g, i) for i, g in enumerate(gaps, 1))
    vocab_html = "".join(render_vocab(v) for v in vocab)
    channel_html = "".join(render_channel(c) for c in channels)
    objection_html = "".join(render_pattern(o, i, "objection") for i, o in enumerate(objections, 1))
    competitor_html = "".join(render_competitor(c) for c in competitors)

    rejected_section = f"""
      <section id="rejected">
        <header class="section-head">
          <h2>Who was<br>excluded.</h2>
          <p>The identity filter is only credible if its cost is visible. These candidates matched the problem but not the target market scope. Counted by reason, never named — a handle printed beside an inferred nationality is a claim about a person, and this report does not make one.</p>
        </header>
        <table>
          <thead><tr><th>Reason</th><th>Platform</th><th>Count</th></tr></thead>
          <tbody>{rejected_html}</tbody>
        </table>
      </section>""" if rejected_html else """
      <section id="rejected" class="limits" style="border-color:#ff7a7a">
        <h2>No rejection log</h2>
        <p>No candidates were recorded as rejected. Either the scope filter did not run, or its results were not captured. Treat this shortlist with caution.</p>
      </section>"""

    competitors_section = f"""
      <section id="competitors">
        <header class="section-head">
          <h2>Who already<br>sells to them.</h2>
          <p>The incumbent is often not an app — it can be a human service, a messaging-app seller, or a free circulating prompt. This is the real price anchor.</p>
        </header>
        <div class="competitors">{competitor_html}</div>
      </section>""" if competitor_html else ""

    gaps_section = f"""
      <section id="gaps">
        <header class="section-head">
          <h2>What they<br>asked for.</h2>
          <p>Unmet needs across the full signal corpus, including rejected candidates. Build means the product lacks it; Message means it has it and nobody knows.</p>
        </header>
        <div class="patterns">{gap_html}</div>
      </section>""" if gap_html else ""

    vocab_section = f"""
      <section id="vocabulary">
        <header class="section-head">
          <h2>Their words,<br>not your translation.</h2>
          <p>The exact Arabic customers use for this problem. Put these on the landing page instead of translated marketing copy.</p>
        </header>
        <table>
          <thead><tr><th>Arabic term</th><th>Meaning</th><th>Count</th><th>How to use it</th></tr></thead>
          <tbody>{vocab_html}</tbody>
        </table>
      </section>""" if vocab_html else ""

    channels_section = f"""
      <section id="channels">
        <header class="section-head">
          <h2>Where the<br>demand lives.</h2>
          <p>Concentrations of relevant signal, with observed activity and participation rules.</p>
        </header>
        <div class="channels">{channel_html}</div>
      </section>""" if channel_html else ""

    objections_section = f"""
      <section id="objections">
        <header class="section-head">
          <h2>Why they<br>won't trust it.</h2>
          <p>Observed adoption blockers, quoted. Address these before spending on acquisition.</p>
        </header>
        <div class="patterns">{objection_html}</div>
      </section>""" if objection_html else ""

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="color-scheme" content="dark">
  <title>{esc(data.get('title', 'First Customer Finder'))}</title>
  <style>{CSS}</style>
</head>
<body>
  <a class="skip" href="#main">Skip to report</a>

  <header class="top">
    <div class="top-in">
      <div class="brand"><i></i><span>First Customer Finder</span></div>
      <nav class="nav">{nav}</nav>
      <button type="button" onclick="window.print()">Save PDF</button>
    </div>
  </header>

  <div class="shell">
    <main id="main">
      <section class="hero">
        <div>
          <span class="eyebrow">Saudi early-customer report &middot; {esc(data.get('generated_at', ''))} &middot; mode: {esc(data.get('mode', 'deep'))}</span>
          <h1>{esc(data.get('title', 'Saudi First Customer Signals'))}</h1>
          <p class="verdict">{esc(data.get('verdict', 'No verdict supplied.'))}</p>
        </div>
        <aside class="hero-card">
          <span>Verified Saudi prospects</span>
          <strong>{len(prospects)}</strong>
          <p>Potential customers from public signals. Not confirmed buyers.</p>
        </aside>
      </section>

      <section class="stats">
        <div><span>Product</span><strong><a href="{safe_url(data.get('product_url'))}" target="_blank" rel="noreferrer">{esc(data.get('product', 'Not specified'))}</a></strong></div>
        <div><span>Saudi target customer</span><strong>{esc(data.get('target_customer', 'Not specified'))}</strong></div>
        <div><span>High intent</span><strong>{high_intent}</strong></div>
        <div><span>Average fit score</span><strong>{average}/100</strong></div>
      </section>

      <section class="audit">
        <div><span>Candidates examined</span><b>{clamp(stats.get('candidates_examined'), 99999)}</b></div>
        <div><span>Rejected on Saudi identity</span><b>{clamp(stats.get('rejected_on_identity'), 99999)}</b></div>
        <div><span>Dropped at link verification</span><b>{clamp(stats.get('dropped_at_link_verification'), 99999)}</b></div>
      </section>

      <section class="icp">
        <div><span>Buyer</span><p>{esc(icp.get('buyer', 'Not specified'))}</p></div>
        <div><span>Job to be done</span><p>{esc(icp.get('job', 'Not specified'))}</p></div>
        <div><span>Trigger</span><p>{esc(icp.get('trigger', 'Not specified'))}</p></div>
        <div><span>Disqualifiers</span><p>{esc(disqualifiers)}</p></div>
      </section>

      <section id="dashboard">
        <header class="section-head">
          <h2>At a glance.</h2>
          <p>Shape of the evidence before you read any of it. A shortlist skewed to one platform or one age band is a shortlist about that platform, not the market.</p>
        </header>
        {build_dashboard(prospects, generated)}
      </section>

      <section class="best">
        <div class="best-label">Highest-confidence prospect &middot; {confirmed} confirmed Saudi in shortlist</div>
        <div>
          <h2>{esc(top.get('name', 'No qualified prospect'))}</h2>
          <p>{esc(top.get('why_now', top.get('pain_signal', '')))}</p>
        </div>
        <strong>{clamp(top.get('score'))}</strong>
      </section>

      <section id="prospects">
        <header class="section-head">
          <h2>Saudis with a reason<br>to care now.</h2>
          <p>Every prospect carries a verbatim Arabic quote, a verified public link, and an explicit Saudi-identity tier. Open the evidence before acting on any of it.</p>
        </header>
        <div class="prospects">{prospect_html or '<p class="empty">No qualified Saudi prospects were found. See the limits section.</p>'}</div>
      </section>

      {rejected_section}

      <section id="patterns">
        <header class="section-head">
          <h2>Signals that repeat.</h2>
          <p>A pattern needs three independent signals. Two is a coincidence.</p>
        </header>
        <div class="patterns">{pattern_html or '<p class="empty">No repeated patterns supplied.</p>'}</div>
      </section>

      {competitors_section}
      {gaps_section}
      {vocab_section}
      {channels_section}
      {objections_section}

      <section id="plan" class="plan">
        <div>
          <span class="eyebrow" style="color:#04150c">Seven-day manual validation plan</span>
          <h2>{esc(plan.get('angle', 'Validate the pain before pitching the product.'))}</h2>
        </div>
        <div class="plan-grid">
          <div><span>First step</span><p>{esc(plan.get('first_step', ''))}</p></div>
          <div><span>Follow-up</span><p>{esc(plan.get('follow_up', ''))}</p></div>
          <div><span>Success signal</span><p>{esc(plan.get('success', ''))}</p></div>
          <div><span>Research scope</span><p>{esc(data.get('search_scope', 'Not specified'))} &middot; {esc(data.get('access_path', ''))}</p></div>
        </div>
      </section>

      <section id="limits" class="limits">
        <h2>Use this shortlist responsibly</h2>
        <ul>{limits or '<li>These are potential customers inferred from public signals, not confirmed buyers or people who consented to contact.</li>'}</ul>
      </section>
    </main>

    <footer>
      <span>Generated by $saudi-first-customer-finder</span>
      <span>Outreach is never sent automatically.</span>
    </footer>
  </div>
</body>
</html>"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate the Saudi first-customer HTML report.")
    parser.add_argument("input", type=Path, help="Path to report JSON")
    parser.add_argument("output", type=Path, help="Path to output HTML")
    args = parser.parse_args()

    with args.input.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise SystemExit("Input JSON must contain an object at the top level.")

    prospects = dicts(data.get("prospects"))
    unverified = [p for p in prospects if p.get("link_verified") is not True]
    if unverified:
        names = ", ".join(str(p.get("name", "unnamed")) for p in unverified)
        print(f"WARNING: {len(unverified)} prospect(s) have link_verified != true: {names}")
    if not dicts(data.get("rejected")):
        print("WARNING: rejection log is empty — the scope filter may not have run.")
    missing_ar = [p for p in prospects if not str(p.get("quote_ar") or "").strip()]
    if missing_ar:
        print(f"WARNING: {len(missing_ar)} prospect(s) have no Arabic verbatim quote.")
    named_rejects = [r for r in dicts(data.get("rejected")) if r.get("name") or r.get("source_url")]
    if named_rejects:
        print(
            f"NOTE: {len(named_rejects)} rejection entr(ies) carried a handle or source URL. "
            "The report counts rejections by reason and does not publish either."
        )
    long_quotes = [p for p in prospects if len(str(p.get("quote_ar") or "")) > QUOTE_CEILING]
    if long_quotes:
        print(f"NOTE: {len(long_quotes)} quote(s) exceeded {QUOTE_CEILING} chars and were truncated in the report.")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(build_html(data), encoding="utf-8")
    print(f"Created report: {args.output.resolve()}")


if __name__ == "__main__":
    main()
