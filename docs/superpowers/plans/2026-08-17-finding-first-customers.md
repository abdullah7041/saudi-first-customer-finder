# finding-first-customers Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn `saudi-first-customer-finder` into a market-neutral skill, `finding-first-customers`, published as `finding-first-customers-skill@2.0.0`.

**Architecture:** Market knowledge stops being shipped data and becomes a method the skill runs at the start of every job. A new `references/market-profile.md` derives language, phrasing, incumbents, platform, scope markers and trust objections for whatever market the product targets. The Saudi material moves to `examples/saudi.md` as the worked example. Everything else — fit check, scope verification, link verification, scoring, product intelligence, source ladder, privacy-safe rejection log — stays and loses its Saudi hardcoding.

**Tech Stack:** Markdown skill files, Python 3.10+ report generator (stdlib only), Node 16+ installer, npm packaging.

## Global Constraints

- Skill directory name: `finding-first-customers`. npm package: `finding-first-customers-skill`. Version: `2.0.0`.
- The report generator uses the Python standard library only. No new dependencies.
- `aggregate_rejected()` and `QUOTE_CEILING = 280` behaviour must not regress: no handle, display name, source URL or quote from a `rejected` entry may reach the HTML.
- Frontmatter `description` states triggering conditions only, never a workflow summary, and stays under 500 characters.
- No Arabic in `SKILL.md`, `README.md`, or any file under `references/`. Arabic appears only in `examples/saudi.md`.
- Every scoring weight and hard gate keeps its current value. Only the name `saudi_authenticity` → `scope_match` changes.
- Tests live in `tests/` at the repo root and run with `python -m pytest tests/ -v`.

---

### Task 1: Test harness for the report generator

Nothing currently pins the generator's privacy and truncation behaviour. Later tasks rename identifiers throughout that file, so the safety net comes first.

**Files:**
- Create: `tests/test_report_privacy.py`
- Create: `tests/conftest.py`

**Interfaces:**
- Consumes: `saudi-first-customer-finder/scripts/generate_report.py` — functions `aggregate_rejected(entries: list[dict]) -> list[tuple[str, str, int]]`, `arabic(text: Any, label: str = ...) -> str`, `QUOTE_CEILING: int`, `build_html(data: dict) -> str`
- Produces: a passing pytest suite that Tasks 4 and 5 must keep green

- [ ] **Step 1: Write `tests/conftest.py` so the generator is importable**

```python
"""Put the generator's directory on sys.path.

The script lives inside the skill payload rather than an installable package,
so tests import it by path rather than by module name.
"""
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPTS = REPO / "saudi-first-customer-finder" / "scripts"
sys.path.insert(0, str(SCRIPTS))
```

- [ ] **Step 2: Write the failing privacy test**

```python
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
```

- [ ] **Step 3: Run the tests to confirm they pass against current behaviour**

Run: `python -m pytest tests/ -v`
Expected: 6 passed. These pin behaviour that already works — if any fail, stop and fix the generator before continuing, because Task 4 renames code in this file.

- [ ] **Step 4: Commit**

```bash
git add tests/
git commit -m "test: pin the report generator's privacy and truncation behaviour"
```

---

### Task 2: Write the market-profile method

The core of the generalization. This file replaces the Arabic lexicon as step 1 of every run.

**Files:**
- Create: `saudi-first-customer-finder/references/market-profile.md`

**Interfaces:**
- Produces: the six-output market profile that `SKILL.md` (Task 5), `fit-check.md` (Task 3) and `scope-verification.md` (Task 4) all reference by name: **market and language**, **local phrasing**, **incumbent ladder**, **where the audience writes**, **scope markers**, **trust objections**

- [ ] **Step 1: Write the file**

Content requirements, all of which the reviewer should check for:

- Opens with the governing rule as its own line: **translated queries find translated people.** Then the reason: an English phrase rendered into the local language by an agent finds the population that also writes translated English, which is usually not the market.
- Budget stated explicitly: at most five queries. Output 1 is read from the product site, not searched for.
- One section per output, each stating **what to produce**, **where it comes from**, and **how to tell a good result from a bad one**. That third element is what makes the method checkable rather than aspirational.
- Local phrasing covers the same five buckets the workflow already uses: explicit demand, pain, workaround, switching/competitor, timing trigger. For each, the instruction is to find real posts first and lift the phrasing from them — never to translate an English template.
- Spelling and inflection variation is called out as a general problem, not an Arabic one: languages with case, gender, informal contractions, or non-standard orthography will not match a single query form. The agent must vary forms and say which variants it used.
- Incumbent ladder names three rungs to look for: the free or official option, the informal human service, the DIY workaround. States why: it sets the price anchor the product is compared against.
- Scope markers section states what may and may not be used. Permitted: self-described location, local civic and institutional references, currency, timezone, language variety, local platform use. Forbidden, carried over verbatim in spirit from the existing rules: tribe, ethnicity, religion, sect, health, financial hardship, political view, and nationality used as a slur.
- Closes with a required output block the agent states to the user before searching, so a wrong derivation is correctable mid-run:

```
Market profile — [product]
Market / language:   [market] / [language(s)]
Phrasing sourced:    [N] real posts read; [M] phrase forms recorded
Incumbent ladder:    free/official: [x] · informal service: [y] · DIY: [z]
Audience writes on:  [platform] — [why this one]
Scope markers:       [marker], [marker], [marker]
Trust objections:    [objection], [objection]
```

- [ ] **Step 2: Verify no Arabic and no Saudi references leaked in**

Run: `grep -nP "[\x{0600}-\x{06FF}]|Saudi|Arabic" saudi-first-customer-finder/references/market-profile.md`
Expected: no output. The one permitted exception is a sentence pointing to `examples/saudi.md` as the worked example, which may name Saudi — if that line is present, it is the only match.

- [ ] **Step 3: Commit**

```bash
git add saudi-first-customer-finder/references/market-profile.md
git commit -m "feat: derive the market profile at runtime instead of shipping a lexicon"
```

---

### Task 3: Generalize fit-check.md

**Files:**
- Modify: `saudi-first-customer-finder/references/fit-check.md`

**Interfaces:**
- Consumes: the market profile's **local phrasing** and **where the audience writes** outputs from Task 2
- Produces: verdicts `GREEN`, `AMBER`, `RED`, `PATH-B BLIND`, unchanged in meaning

- [ ] **Step 1: Replace the hardcoded Arabic probes with profile-driven ones**

The three probe templates currently embed Arabic strings. Replace each with the bucket it represents plus an instruction to use the phrasing recorded in the market profile:

1. Demand probe — the market's demand phrasing + the category noun
2. Pain probe — the market's symptom phrasing + the domain noun
3. Workaround probe — the market's manual-method phrasing + the domain noun

Keep the existing guidance that symptom phrases find buyers while category nouns find vendors — it is market-neutral and it is the most useful sentence in the file.

- [ ] **Step 2: Generalize the control query**

The control currently hardcodes an Arabic phrase. Replace with: a phrase in the market's language that the platform certainly contains in volume, taken from the market profile's local phrasing. Keep all four qualifying conditions and the 3-or-more threshold exactly as they are.

- [ ] **Step 3: Update the category screen and source ladder wording**

In the category-screen table, replace "Saudi" with "the target market" throughout. In the source ladder, replace "Saudi government and semi-government services" with "government or public-sector services in the target market" and keep the rule that this rung is not optional where such a service exists. The two recorded field tests stay, relabelled as observations from the Saudi worked example.

- [ ] **Step 4: Verify**

Run: `grep -nP "[\x{0600}-\x{06FF}]" saudi-first-customer-finder/references/fit-check.md`
Expected: no output.

- [ ] **Step 5: Commit**

```bash
git add saudi-first-customer-finder/references/fit-check.md
git commit -m "refactor: drive fit-check probes from the market profile"
```

---

### Task 4: Rename scope verification and the scoring dimension

**Files:**
- Create: `saudi-first-customer-finder/references/scope-verification.md` (from `saudi-identity-verification.md`)
- Delete: `saudi-first-customer-finder/references/saudi-identity-verification.md`
- Modify: `saudi-first-customer-finder/references/research-framework.md`
- Modify: `saudi-first-customer-finder/references/report-artifact.md`
- Modify: `saudi-first-customer-finder/scripts/generate_report.py`
- Test: `tests/test_report_privacy.py` (must stay green)

**Interfaces:**
- Consumes: the market profile's **scope markers** output from Task 2
- Produces: JSON field `scope_match` replacing `saudi_authenticity`; JSON field `scope_tier` replacing `saudi_tier`; tier values `confirmed`, `likely`, `rejected` unchanged

- [ ] **Step 1: Create scope-verification.md from the existing file**

```bash
git mv saudi-first-customer-finder/references/saudi-identity-verification.md saudi-first-customer-finder/references/scope-verification.md
```

Then rewrite its contents: the dialect-marker tables become an instruction to apply the scope markers derived in the market profile. Tiering is unchanged — confirmed is two or more independent in-market signals with zero contradictions, likely is one strong signal with zero contradictions, rejected is any disqualifying marker or no in-market signal at all. The framing paragraph stating this is a market-scope filter and never a claim about a person is kept verbatim. The rule that rejections are recorded as counts with no identifier is kept verbatim.

- [ ] **Step 2: Rename the scoring dimension in research-framework.md**

`saudi_authenticity` → `scope_match`, weight stays 20%, the `< 3` hard gate stays. "Saudi authenticity rubric" becomes "Scope match rubric", and its levels are rewritten against the market profile's scope markers rather than Arabic dialect. Every other dimension, weight, and threshold is untouched.

- [ ] **Step 3: Rename the fields in report-artifact.md**

`saudi_authenticity` → `scope_match`, `saudi_tier` → `scope_tier`. The field rules added for privacy — no name, no source_url, no quote on rejected entries; the 280-character quote note — stay exactly as written.

- [ ] **Step 4: Rename in the generator**

In `scripts/generate_report.py`:
- Line ~23 `"saudi_authenticity": ("Saudi authenticity", 20)` → `"scope_match": ("Scope match", 20)`
- Lines ~98-99 tier labels `"Confirmed Saudi"` / `"Likely Saudi"` → `"Confirmed in-market"` / `"Likely in-market"`
- Line ~211 `Saudi identity markers` → `Scope markers`
- Lines ~358-359 `p.get("saudi_tier")` → `p.get("scope_tier")`, labels to match Step 4's tier labels
- Line ~634 "the Saudi market scope" → "the target market scope"
- Line ~643 "the Saudi identity filter" → "the scope filter"
- Line ~650 the competitive-landscape blurb: replace the Saudi-specific sentence with "The incumbent is often not an app — it can be a human service, a messaging-app seller, or a free circulating prompt. This is the real price anchor."
- Lines ~2, ~700, ~708 title, `<title>` default and brand string → `First Customer Finder`

- [ ] **Step 5: Run the tests**

Run: `python -m pytest tests/ -v`
Expected: 6 passed. The privacy tests do not reference renamed fields, so they must still pass unchanged. If they fail, the rename broke `build_html` — fix before committing.

- [ ] **Step 6: Generate a report end to end**

```bash
python saudi-first-customer-finder/scripts/generate_report.py tests/fixtures/sample.json /tmp/out.html
```

First create `tests/fixtures/sample.json` with one prospect scoring `scope_match: 4`, `scope_tier: "confirmed"`, `link_verified: true`, a short `quote_ar`, and two `rejected` entries carrying handles. Expected: the file is written, stdout notes the rejection entries carried identifiers, and `grep -c "@" /tmp/out.html` finds no handle from the rejected entries.

- [ ] **Step 7: Commit**

```bash
git add -A
git commit -m "refactor: scope verification replaces Saudi identity verification"
```

---

### Task 5: Rewrite SKILL.md and move the Saudi material to examples

**Files:**
- Modify: `saudi-first-customer-finder/SKILL.md`
- Create: `saudi-first-customer-finder/examples/saudi.md`
- Delete: `saudi-first-customer-finder/references/arabic-query-lexicon.md`
- Modify: `saudi-first-customer-finder/references/platform-playbooks.md`

**Interfaces:**
- Consumes: every reference file from Tasks 2-4, by their new names
- Produces: the workflow contract the report and modes tables depend on

- [ ] **Step 1: Build examples/saudi.md**

```bash
git mv saudi-first-customer-finder/references/arabic-query-lexicon.md saudi-first-customer-finder/examples/saudi.md
```

Reframe it as the method applied end to end: a completed market profile for Saudi Arabia in the exact output block shape Task 2 defines, followed by the Arabic lexicon as the "local phrasing" section's filled-in result, followed by the Saudi scope markers moved out of the old identity file, followed by the two recorded field tests. Open with one sentence stating this is an illustration of `references/market-profile.md`, not a required input.

- [ ] **Step 2: Rewrite SKILL.md frontmatter**

Name becomes `finding-first-customers`. Description states triggering conditions only, under 500 characters, no workflow summary, no Saudi. It must trigger on: a product URL or idea, first customers, early adopters, demand validation, market research, ideal customer profile, and finding out whether a market's demand is visible in public text.

- [ ] **Step 3: Rewrite the SKILL.md body**

- Required-reading table lists `market-profile.md` first, then `fit-check.md`, `platform-playbooks.md`, `scope-verification.md`, `research-framework.md`, `report-artifact.md`. Add `examples/saudi.md` as optional, labelled "worked example".
- Workflow gains step 0.5: build the market profile, before the fit check.
- Steps 1-10 lose their Saudi wording. "Saudi ICP" becomes "in-market ICP"; "the Arabic name for the problem" becomes "the problem's name in the market's own language"; the Saudi-specific disqualifier list becomes "market-specific constraints — language, payment methods, identity or regulatory dependencies, sector rules".
- The three differentiator bullets at the top are rewritten market-neutrally: searches in the customer's own language rather than translated English; proves the person is in the target market; mines signals for product decisions.
- Hard rules keep every prohibition. "Saudi or excluded" becomes "In-market or excluded". The sensitive-category rule and the no-identifier rejection rule stay verbatim.
- Modes table: `fit-check` 4 queries, `research-only` no prospects, all other rows unchanged.

- [ ] **Step 4: Generalize platform-playbooks.md**

Keep the per-platform tactics. Replace the assertion that X is the primary source with: the platform ranking comes from the market profile's "where the audience writes" output, and these playbooks describe how to work each platform once chosen. The Reddit expat-skew warning generalizes to: expatriate-heavy and diaspora communities on any platform are a scope risk, not a market sample.

- [ ] **Step 5: Verify**

Run: `grep -rnP "[\x{0600}-\x{06FF}]" saudi-first-customer-finder/SKILL.md saudi-first-customer-finder/references/`
Expected: no output. All Arabic now lives in `examples/saudi.md`.

Run: `head -5 saudi-first-customer-finder/SKILL.md`
Expected: frontmatter with `name: finding-first-customers` and a description that does not describe the workflow.

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "feat: generalize the workflow, demote the Saudi material to a worked example"
```

---

### Task 6: Rename the payload directory and repackage

**Files:**
- Rename: `saudi-first-customer-finder/` → `finding-first-customers/`
- Modify: `scripts/install.js:7`
- Modify: `package.json`
- Modify: `tests/conftest.py`

**Interfaces:**
- Consumes: everything from Tasks 1-5
- Produces: an installable `finding-first-customers-skill@2.0.0` tarball

- [ ] **Step 1: Rename the payload directory**

```bash
git mv saudi-first-customer-finder finding-first-customers
```

- [ ] **Step 2: Update the installer's skill name**

In `scripts/install.js`, line 7: `const SKILL_NAME = "finding-first-customers";`
The example invocation printed at the end of `main()` must also lose its Saudi wording.

- [ ] **Step 3: Update package.json**

`name` → `finding-first-customers-skill`, `version` → `2.0.0`, `bin` key → `finding-first-customers-skill`, `files[0]` → `finding-first-customers`, `description` rewritten market-neutrally, `keywords` with the Saudi-specific entries replaced by market-neutral ones (`customer-discovery`, `early-adopters`, `market-research`, `prospecting`, `agent-skill`).

- [ ] **Step 4: Update the test path**

In `tests/conftest.py`, `SCRIPTS = REPO / "finding-first-customers" / "scripts"`.

- [ ] **Step 5: Run the tests**

Run: `python -m pytest tests/ -v`
Expected: 6 passed.

- [ ] **Step 6: Verify the tarball**

Run: `npm pack --dry-run`
Expected: 14 files — LICENSE, README.md, package.json, `scripts/install.js`, and under `finding-first-customers/`: SKILL.md, 6 reference files, `examples/saudi.md`, `scripts/generate_report.py`, `agents/openai.yaml`. No `__pycache__`, no `.pyc`, no `tests/`, no `docs/`.

- [ ] **Step 7: Install from the tarball into a scratch directory**

```bash
npm pack --pack-destination /tmp
npx --yes --package=/tmp/finding-first-customers-skill-2.0.0.tgz -- finding-first-customers-skill --skills-dir /tmp/skills-test
```

Expected: `Installed: /tmp/skills-test/finding-first-customers`, and the frontmatter check passes. Confirm `ls /tmp/skills-test/finding-first-customers` shows `examples/`.

- [ ] **Step 8: Commit**

```bash
git add -A
git commit -m "build: rename the payload and package for the 2.0.0 release"
```

---

### Task 7: Rewrite the README

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Rewrite**

Plain and factual, for a reader deciding whether to install. Required sections, in order: what it does (three sentences), install, usage, modes table, what the report contains, scoring table with the `scope_match` name, data access paths A/B/C, ethics, repo layout, credits, license.

Rules: no Arabic anywhere. No marketing rhetoric. Every claim checkable against the skill's own files. Install examples pinned to `@2.0.0`. The credits section keeps the attribution to the upstream `first-customer-finder` skill by Francesco Mistero (MIT) and states plainly what this version adds: pre-flight fit check with a blind-path control, runtime market profiling, scope verification, link verification, privacy-safe rejection reporting, product intelligence, and the HTML report.

Add one short section, "How it handles a market it has never seen", summarising the market-profile method in four or five sentences. That is the question a reader will actually have.

- [ ] **Step 2: Verify**

Run: `grep -nP "[\x{0600}-\x{06FF}]" README.md`
Expected: no output.

Run: `grep -c "2.0.0" README.md`
Expected: 5 or more.

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "docs: rewrite the README for a market-neutral skill"
```

---

### Task 8: Acceptance run on a non-Arabic product

The gate that can actually fail. Everything before this proves the files are consistent; this proves the method works.

**Files:**
- Create: `docs/superpowers/acceptance-2026-08-17.md`

- [ ] **Step 1: Install the built skill locally**

```bash
node scripts/install.js
```

Restart the agent so the skill loads.

- [ ] **Step 2: Run fit-check mode against a non-Saudi, non-Arabic product**

Pick a product whose market is plainly not Saudi Arabia — a German B2B SaaS, a Brazilian consumer app, a US developer tool. Invoke the skill in `fit-check` mode with only the URL.

- [ ] **Step 3: Record what happened**

Write `docs/superpowers/acceptance-2026-08-17.md` capturing: the market profile the skill derived, verbatim; the phrasing it recorded and whether any of it reads like translated English; the control result; the verdict; and whether any Arabic or Saudi assumption appeared anywhere in the run.

**Pass conditions, all four required:**
1. The derived market and language match the product's actual target market
2. The recorded phrasing is idiomatic to that language, not translated English
3. The control query and verdict logic execute normally
4. No Arabic and no Saudi-specific assumption appears anywhere

**If any fails, stop.** Do not publish. Record the failure and revise `market-profile.md` — that is the file at fault, and the failure is exactly the evidence needed to fix it.

- [ ] **Step 4: Re-run the Saudi case**

Invoke `fit-check` on the Saudi product from the recorded field tests. Expected: same `PATH-B BLIND` verdict as before, reached through the derived profile rather than the shipped lexicon. Append the result to the acceptance document.

- [ ] **Step 5: Commit**

```bash
git add docs/superpowers/acceptance-2026-08-17.md
git commit -m "docs: record the 2.0.0 acceptance run"
```

---

### Task 9: Publish and deprecate the old package

Publishing requires an OTP, which only the maintainer can supply. The final step is theirs to run.

- [ ] **Step 1: Confirm auth before attempting anything**

Run: `npm whoami`
Expected: the maintainer's username. On `E401`, stop — `npm login` is needed first, and a publish attempted without it fails in a way that looks like success in the terminal output above the error.

- [ ] **Step 2: Hand the maintainer the publish command**

```bash
npm publish --otp=123456
```

Success is the final line reading `+ finding-first-customers-skill@2.0.0`. The tarball listing printed above it means nothing.

- [ ] **Step 3: Verify against the registry, not the terminal**

```bash
curl -s https://registry.npmjs.org/finding-first-customers-skill | node -e "let d='';process.stdin.on('data',c=>d+=c).on('end',()=>{const j=JSON.parse(d);console.log(j['dist-tags'])})"
```

Expected: `{ latest: '2.0.0' }`. Anything else means the publish failed regardless of what the terminal showed.

- [ ] **Step 4: Deprecate the old package**

```bash
npm deprecate saudi-first-customer-finder-skill "Renamed to finding-first-customers-skill, which works for any market."
```

- [ ] **Step 5: Install from npm and confirm**

```bash
npx --yes finding-first-customers-skill@2.0.0
```

Expected: installs to `~/.claude/skills/finding-first-customers`, frontmatter check passes.

---

## Notes for the implementer

**The directory rename lands in Task 6, not Task 1.** Tasks 2-5 edit files under the old `saudi-first-customer-finder/` path. This keeps each commit reviewable — a rename mixed with content edits produces a diff nobody can read.

**Task 8 is a real gate.** It is the only step that can prove the design wrong, and its failure mode is "the method only worked because the author already knew Arabic." Treat a failure there as information, not as an obstacle.

**Wording is not verified by Task 8.** A single acceptance run is one sample. `market-profile.md` is behaviour-shaping guidance, and superpowers:writing-skills asks for a micro-test against a no-guidance control, 5+ reps, before calling it verified. That test is not in this plan; say so plainly rather than implying the method is proven.
