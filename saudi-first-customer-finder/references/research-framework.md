# Research and Qualification Framework

Scoring, verification, and the product-intelligence extraction. Everything here is
Saudi-scoped; do not substitute a generic prospecting rubric.

## Sequence

```
brief → query plan → search → identity gate → link verification → score → dedupe
      → patterns → product intelligence → report
```

The identity gate comes **before** scoring. Do not spend effort scoring someone who will
be rejected on identity — and never score first and then rationalize the identity.

## The Saudi product brief

Before any searching, write:

- product and promised outcome
- primary Saudi ICP and one adjacent Saudi ICP
- the urgent job to be done
- **the Arabic complaint phrase for the problem** — what a Saudi person types when
  annoyed by it, not the marketing term
- current workaround (Excel, WhatsApp, a friend, a service office, ChatGPT)
- adoption trigger
- Saudi-specific constraints: Arabic-language requirement, payment methods (mada, Apple
  Pay, tabby/tamara), national-ID or Nafath dependency, sector regulation, Saudization
  rules, gender-specific context where legitimately relevant to the product
- disqualifiers

If the brief cannot reject a weak match, keep working on it.

## Scoring — six dimensions

Score each 0–5, then weight:

| Dimension | Weight | What earns a 5 |
| --- | --- | --- |
| **Scope match** | 20% | Confirmed tier: multiple independent in-market signals, zero contradictions |
| **Pain strength** | 20% | Directly stated, severe, repeated, with a named cost in time or money |
| **Product fit** | 20% | The product solves the exact evidenced job, not an adjacent one |
| **Timing** | 15% | Signal is fresh and a current trigger is visible |
| **Reachability** | 10% | A natural, appropriate public channel exists on the same platform |
| **Evidence quality** | 15% | Specific, first-person, verified link, unambiguous attribution |

```text
score = scope_match/5*20
      + pain_strength/5*20
      + product_fit/5*20
      + timing/5*15
      + reachability/5*10
      + evidence_quality/5*15
```

### Hard gates — applied before the total matters

- `scope_match < 3` → **excluded from the primary shortlist**, regardless of
  total score. Goes to the rejection log.
- `link_verified != true` → **dropped entirely.** Not logged as a prospect, not shown.
- `pain_strength < 2` → not a prospect. ICP membership without evidenced pain is a
  demographic, not a signal.
- No Arabic verbatim (for an Arabic-language source) → not shippable. Go back and get it.

### Bands

- **80–100** — strong Saudi first-customer candidate
- **65–79** — promising, validate quickly
- **55–64** — plausible, a material signal is missing; include only in `deep` mode and
  label the gap
- **Below 55** — excluded from the primary shortlist

### Scope match rubric

| Score | Meaning |
| --- | --- |
| 5 | Confirmed: 3+ independent scope markers across categories, zero contradictions |
| 4 | Confirmed: 2 independent scope markers, zero contradictions |
| 3 | Likely: 1 strong scope marker (clear language-variety cluster or stated in-market location), zero contradictions |
| 2 | Weak: ambiguous regional markers, or in-market context with no personal-scope signal |
| 1 | Unverified: ICP match only |
| 0 | Contradicted: disqualifying marker or neighbouring-market location |

### Timing decay

Twelve-month window, decayed:

| Age of signal | Timing ceiling |
| --- | --- |
| 0–30 days | 5 |
| 1–3 months | 4 |
| 3–6 months | 3 |
| 6–12 months | 2 |
| Over 12 months | 1 — include only for pattern analysis, not the shortlist |

An old explicit request still counts, at a reduced score, with the date shown. A visible
current trigger (just graduated, just launched, just resigned) can hold timing at 4 even
for an older post if the trigger itself is recent.

## Prospect stages

- **High intent** — publicly asking for the solution, or actively switching away from an
  alternative
- **Problem aware** — clearly describing the pain or an expensive workaround
- **Trigger present** — a current life or business event makes the product relevant now
- **Potential fit** — ICP match with incomplete evidence; stays outside the shortlist

## Link verification pass

Run this as a distinct step, after scoring and before writing the report. For each
surviving prospect:

1. Re-open the source URL.
2. Confirm the page loads publicly and is not deleted, private, or removed.
3. Confirm the quoted Arabic text appears on that page, character for character.
4. Confirm the date matches what was recorded.
5. Set `link_verified: true` and `verified_at` to today's date.

Anything that fails is dropped, and the drop is noted in the limits section as "N
prospects dropped at link verification". That number is a credibility signal — report it.

## Evidence ledger

For every prospect record:

- public display name or handle (never a private legal name discovered elsewhere)
- platform and source type
- source title and URL
- visible publication date, or "date unavailable"
- **original Arabic verbatim** plus faithful English translation
- concise pain or timing signal in English
- what was observed versus what was inferred — keep these separate
- identity tier, markers, contradictions
- six-dimension score breakdown
- freshness warning where relevant

## Product intelligence extraction

Run this over the **entire** signal corpus — including rejected candidates. A
non-Saudi's complaint is not a Saudi prospect, but it is still evidence about the
problem.

### Feature gaps

For each recurring unmet need:

- title, count of independent signals, insight, at least one Arabic quote with source
- distinguish "the product doesn't do this" from "the product does this but nobody knows"
  — those need opposite responses (build vs. message)
- rank by count, then by pain strength of the underlying signals

### Vocabulary

The words customers use, for landing pages, ads, and in-product copy:

- the Arabic term for the **problem** (what they complain about)
- the Arabic term for the **product category** (what they'd search for)
- the Arabic term for the **outcome** (what they say they want)
- the words used for the **workaround** they'd be abandoning
- terms to avoid: formal MSA phrasing that no one actually types, and any translated
  English that reads foreign

Record term, count, and where it appeared. This section replaces guessing at Arabic copy.

### Channel map

Where the demand concentrates:

- platform, specific location (hashtag, subreddit, account, community)
- observed activity level and recency
- what kind of signal appears there
- whether promotional participation is permitted by the community's rules

### Trust objections

What stops Saudi users from adopting this category. Recurring themes across most
verticals:

- price and subscription resentment
- scam fatigue around paid digital services
- doubt that a tool genuinely works in Arabic rather than being an English tool with a
  translated UI
- data privacy, especially for national ID, salary, and personal documents
- payment friction — cards, mada support, local billing
- preference for a human intermediary (a service office, a friend, a specialist) over
  software

Each objection needs a count and a quote. Do not include an objection you did not
observe.

## Patterns

A pattern needs at least three independent signals. Two is a coincidence; one is an
anecdote. Report each with title, count, and the insight it implies for positioning or
product. Patterns that contradict the user's assumed ICP are the most valuable output of
the entire run — surface them prominently rather than smoothing them over.

## Outreach drafting (skip in `research-only`)

Top three prospects only. Shape:

1. reference the public context naturally, in one clause
2. connect it to the specific problem
3. one sentence on what the product does
4. one low-friction question

Under 60 words in Arabic. Match platform register: X is casual and can use dialect,
LinkedIn is formal MSA, Reddit is plain and direct. Never claim familiarity, never
promise an outcome, never mention anything the person did not post publicly.

Mark every opener as an unsent draft.

## Honest-failure conditions

Report these plainly rather than padding the shortlist:

- Fewer than five verified Saudi prospects found → the demand may not be publicly visible
  yet, or the queries were wrong. Say which you believe and why.
- Shortlist is entirely `likely` tier with no `confirmed` → the identity evidence is weak
- One platform supplied everything → the sample is platform-shaped, not market-shaped
- All signals older than six months → the pain may be resolved, or the market moved
- High rejection rate on identity → the visible demand for this product in KSA is
  expat-driven, which is itself a finding worth acting on
