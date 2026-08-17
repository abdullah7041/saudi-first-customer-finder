---
name: finding-first-customers
description: Use when someone gives a product URL or idea and wants first customers, early adopters, demand validation, market research, or an ideal customer profile — including finding out whether a market's demand is visible in public text, and confirming a prospect is actually inside the target market rather than a neighbouring one.
---

# Finding First Customers

Turn a product URL or idea into a short, evidence-backed list of plausible first
customers **inside a specific target market**, plus the product intelligence hidden in
their own words. Every prospect is a hypothesis backed by a live public link and a
verbatim quote. Never a confirmed buyer.

The three things this skill does that a generic prospecting pattern cannot:

1. **It searches in the customer's own language**, not translated English. Real demand is
   written in the informal register people actually type in, not the marketing term
   rendered into another language.
2. **It proves the person is in the target market.** Language-variety and civic markers,
   and an explicit rejection log — because a market's search results overwhelmingly
   return neighbouring-market and diaspora voices, and a report built on those is a
   report about a different market.
3. **It mines the signals for product decisions**, not just names: feature gaps,
   landing-page vocabulary, channel map, and trust objections.

## Required reading

Read these before acting. Do not improvise the vocabulary or the scoring.

| File | Read before |
| --- | --- |
| [references/market-profile.md](references/market-profile.md) | Anything else — the profile is derived first, once per job |
| [references/fit-check.md](references/fit-check.md) | Any prospecting query — this runs second, right after the profile |
| [references/platform-playbooks.md](references/platform-playbooks.md) | Working any platform the market profile named |
| [references/scope-verification.md](references/scope-verification.md) | Qualifying or rejecting any person |
| [references/research-framework.md](references/research-framework.md) | Scoring anything |
| [references/report-artifact.md](references/report-artifact.md) | Building the report |
| [examples/saudi.md](examples/saudi.md) | Optional — a worked example of the market profile, filled in for one specific market |

## Invocation

**A bare URL is a complete instruction.** When the user supplies a link and nothing else,
do not ask what the product is, who the customer is, which market or mode to use, or
which platforms to search. Read the site, infer everything, run in `deep` mode, and
deliver the report.

The only acceptable question is a single one, asked once, when the product's category or
target market is genuinely unreadable from its own site — and even then, make a labelled
assumption and proceed rather than blocking on an answer.

State the inferred brief before searching so the user can correct it mid-run if it is
wrong. Announce, do not ask.

## Workflow

### 0. Build the market profile — once per job, before anything else

Run `references/market-profile.md` first, always. It derives the search vocabulary, the
incumbent ladder, the platform to search, the scope markers, and the trust objections from
real posts and the product's own site — at most five queries, most of the work is reading
what comes back. Nothing below this step is possible without it: the fit check's control
and probes, the platform playbooks, and the scope filter all consume its six outputs by
name.

State the profile before spending a single prospecting query, in the shape
`references/market-profile.md` defines. A wrong derivation is cheap to correct now and
expensive to correct after sixty queries have been spent on the wrong vocabulary.

### 0.5. Pre-flight fit check — four queries, always

Some categories cannot produce a prospect shortlist however well the run is executed: the
demand is not written down in public, or the people who have it must not be targeted.
Finding that out after sixty queries wastes an hour.

Run `references/fit-check.md` next, every time, right after the market profile and before
any other prospecting query. It screens the category against a do-not-target table, fires
one control query and three probe queries — the control always runs before the probes —
and returns green, amber, red, or path-b blind.

- **Green** — run `deep` as designed.
- **Amber** — run `deep`, but say up front that the shortlist will be short.
- **Red** — do not run the prospecting pass. Switch to `research-only`, deliver the
  product-intelligence half, and explain why the signal is not visible.
- **Path-B blind** — the search path cannot return posts from the platform at all. Issue
  no market verdict. Say which platform is unreachable and hand the user the routes.

The control query runs **before** the probes and is not optional. A red verdict from a
search path that cannot see the platform is a claim about the market that was never
measured — and it points the user at the opposite decision from the true one.

State the verdict in six lines or fewer, then continue without waiting for permission
unless the verdict is red or blind. On either, stop and let the user choose.

Four queries is the budget for this check — one control, three probes. It is held
separately from the five queries the market profile already spent. If the check grows
past its own budget, it has become the run.

### 1. Build the product brief — from the URL alone

Fetch the supplied URL and read it properly: landing copy, pricing page, features, FAQ,
about page, any localized version of the site, and the repo README if a repository was
given. Everything below is inferred from that reading, not from the user.

Then define:

- product, promised outcome, and the urgent job to be done
- primary in-market ICP and one adjacent ICP
- the **problem's name in the market's own language**, as a normal person in that market
  would say it — not the marketing term, the complaint term
- current workaround (very often: a spreadsheet, a messaging app, a friend, or a general
  AI assistant)
- adoption trigger
- market-specific constraints — language, payment methods, identity or regulatory
  dependencies, sector rules
- whether the buyer is an individual, a household, or a business

Label every inference as an inference. A wrong inference stated plainly is correctable; a
question asked instead of working is not.

State the brief before searching. If the brief is not specific enough to *reject* a weak
match, it is not finished.

### 2. Plan queries across five buckets and two languages

Use the phrasing the market profile derived. For every bucket, generate local-language
**and** English variants, and vary the local-language forms across the spelling and
inflection variants the profile stated it used — real users do not write standardized
prose and one form misses most of the corpus.

Buckets: explicit demand · pain · workaround · switching/competitor · timing trigger.

Minimum query counts by mode are in the Modes section. Under-searching is the most common
failure: one query per bucket produces a report that says more about the query than about
the market.

### 3. Search each platform on its own terms

Follow `references/platform-playbooks.md`. The platform ranking comes from the market
profile's **where the audience writes** output, not from a fixed assumption about which
platform matters most — these playbooks describe how to work each platform once it has
been chosen.

- Search in the local language with whatever operators the platform supports (language
  filters, date windows, location signals), and prefer opening the original post over
  reading a search snippet. A snippet is not evidence.
- Expatriate-heavy and diaspora communities exist on every platform, not just one. Treat
  them as a scope risk, not a market sample — verify identity there especially.
- Professional networks are the primary source for B2B signals and for business triggers
  (hiring, expansion, funding, sector programmes) — public post search is often limited
  without a session; see the playbook for both paths.

### 4. Verify market scope — mandatory gate

Apply `references/scope-verification.md` to every candidate.

- **Confirmed**: two or more independent in-market signals, zero contradictions.
- **Likely**: one strong signal, zero contradictions.
- **Rejected**: any disqualifying marker, or no in-market signal at all.

Record every rejection with its reason and platform, and **no identifier** — no handle, no
display name, no link, no quote. The log ships as counts by reason. A report with no
rejection log is not trustworthy, because it means the filter never ran; a report that
names the people it rejected is worse, because it publishes an inferred market attachment
tied to a real person. The count carries the whole evidentiary load.

Their pain still counts in product intelligence. It is the scope-membership claim that
does not ship.

Score `scope_match` below 3 is an automatic exclusion from the primary shortlist,
regardless of how strong the pain signal is.

### 5. Verify every link before it enters the report

Re-open each source URL and confirm:

- the page loads and is public
- the quoted text is actually on that page
- the visible date matches what you recorded
- the account/post has not been deleted since you found it

A prospect whose link cannot be re-opened and re-read is dropped. No exceptions, no
"probably still there". Set `link_verified: true` only after this pass.

### 6. Capture the verbatim source text

For every prospect, record the original text of the pain signal exactly as written —
dialect, typos, informal spelling and all — plus a faithful English translation when the
source is not in English.

Quote minimally: one or two sentences, enough to prove the signal. Never invent, clean up,
or "fix" the source text. The unedited text is the evidence.

### 7. Score, deduplicate, rank

Use the six-dimension framework in `references/research-framework.md`. Drop duplicates,
drop anything under the threshold, and never present a prospect as interested, consenting,
or likely to buy. The label is always "potential customer based on public signals".

### 8. Extract product intelligence

This is the section a generic prospecting skill does not produce. From the full signal
set — including rejected prospects, whose pain is still real market data — extract:

- **Feature gaps**: what people ask for that the product does not do, ranked by how many
  independent signals mention it.
- **Vocabulary**: the exact words and phrases used for the problem, the product category,
  and the desired outcome. This is landing-page and ad copy, sourced from customers
  instead of from a translator.
- **Channel map**: where the demand actually concentrates — which hashtags, which
  accounts, which subreddits, which professional communities, and how alive each one is.
- **Trust objections**: what makes people in this market distrust this category. Pricing,
  privacy, data residency, scam fatigue, "does it actually work in my language", and
  payment friction all appear repeatedly across markets. Quote them.
- **Competitive landscape**: the sellers your searches surfaced. The incumbent your
  product is compared against is very often *not* another app — it is a human service
  sold over a messaging app, a social account taking DM orders, or a free circulating AI
  prompt. Record who they are, what they sell, how they take orders, and any visible
  price. This sets the price anchor the product will actually be compared against.

Every item needs a count and at least one quoted source.

A note on where sellers show up: category keywords (the plain product-category noun) tend
to return vendors, while symptom phrases return buyers. When a query returns mostly
sellers, that is not a failed query — route the results into the competitive landscape and
re-run the bucket with a first-person symptom phrase.

### 9. Draft openers (top three only)

Unless the mode is `research-only`:

- Write one short opener **in the market's own language** for the three highest-scoring
  prospects.
- Ground it only in the cited public context. Do not imply familiarity.
- Match the register of the platform: quick consumer platforms are short and casual,
  professional networks are formal, long-form forums are plain and direct.
- Mark openers as optional drafts.

Never send, reply, follow, connect, comment, or create a CRM record. Drafting is the end of
the skill's authority.

### 10. Produce the report

Order:

1. **Verdict** — is there reachable early-customer demand in the target market, and where
2. **ICP** — buyer, job, trigger, disqualifiers
3. **Top prospect** — strongest verified candidate and why now
4. **Prospect shortlist** — verbatim quote, translation, verified link, scores, stage
5. **Rejection log** — who was excluded and why
6. **Repeated patterns** — pains and triggers across prospects
7. **Competitive landscape** — who already sells to this customer, and at what price
8. **Product intelligence** — feature gaps, vocabulary, channels, objections
9. **Seven-day validation plan** — manual, low-volume, market-appropriate
10. **Limits** — what is missing and what must be confirmed by talking to people

Build a standalone bilingual HTML report unless the user explicitly asks for chat only:

1. Write the JSON described in `references/report-artifact.md`.
2. Run the generator **by its absolute path inside this skill directory** — the working
   directory is the user's workspace, not the skill, so a relative `scripts/...` path
   will not resolve:

   ```
   <skill-dir>/scripts/generate_report.py <analysis.json> <outputs/report.html>
   ```

   `<skill-dir>` is the directory this SKILL.md lives in. Invoke it with `python3`,
   falling back to `python` on Windows where `python3` is often absent. Python 3.10 or
   newer.
3. The generator creates the output directory itself; target the workspace `outputs/`.
4. Read the warnings it prints — unverified links, an empty rejection log, and missing
   source-language verbatims are all reported on stderr/stdout and all block shipping.
5. Open the result and verify: quotes render in their source language's own direction,
   every source link is present, the rejection log is populated, and no score is a
   placeholder.
6. Return a clickable absolute file link.

## Modes

| Mode | Prospects | Minimum queries | Notes |
| --- | --- | --- | --- |
| `fit-check` | none | 4 | The pre-flight check on its own — one control plus three probes. Answers "is this category even searchable, and can I even see the platform" in about a minute |
| `quick` | up to 5 | 20 | Sanity check or re-run against an existing baseline |
| `standard` | up to 10 | 35 | Balanced run across all three platforms |
| `deep` | 20+ | 60 | **Default.** Full spelling and inflection variation, full pattern and product-intelligence analysis |
| `research-only` | none | 60 | Product intelligence without a shortlist. Openers removed, no individuals named. Where a red or blind fit check lands — run the source ladder in `references/fit-check.md` |
| `b2b` | up to 12 | 40 | In-market companies and public business triggers; professional-network-weighted |
| `consumer` | 20+ | 60 | Individuals only; consumer-platform-weighted, dialect-heavy |

Default to `deep`. Announce the mode before starting — never ask which one to use. Switch
only if the user names a different mode themselves.

## Hard rules

- **In-market or excluded.** Neighbouring-market and expatriate/diaspora voices are
  logged, not shortlisted, unless the user explicitly widens the scope.
- **No link, no prospect.** Verified and re-readable, or it does not ship.
- **No paraphrase without the original.** Every pain signal carries its source-language
  verbatim.
- **Public and permitted only.** No login-wall bypassing, no paywall circumvention, no
  rate-limit evasion, no scraping against a site's terms, no data brokers, no leaked
  datasets, no private groups, no personal email or phone enrichment.
- **No sensitive targeting.** Never infer or target on tribe, region-as-ethnicity,
  religion, sect, health, financial hardship, political view, or nationality-as-slur.
  Scope verification is a market-scope filter applied to public self-description — it is
  never a claim about anyone's worth, and the rejection log states reasons neutrally.
- **No outreach.** Drafting only.
- **No invented numbers.** Counts come from actual observed signals. If the pool is thin,
  the report says the pool is thin.
- **Never target a sensitive category.** Health, mental health, addiction, fertility,
  disability, debt and financial hardship, dating and family conflict, religion, sect,
  political affiliation, legal trouble, and immigration status are never grounds for a
  prospect shortlist — even when the posts are public and the product genuinely helps.
  Those runs go to `research-only` and deliver category-level intelligence instead.

## Quality bar

- Ten verified prospects beat fifty unverified names.
- If the honest answer is "there is no reachable demand for this yet in this market", say
  that in the verdict. A negative verdict backed by evidence is a useful result.
- Show the search scope and the date window. Stale evidence must be visible, not hidden.
- The product-intelligence section should change what the user builds next. If it only
  restates the prospect list, it is not finished.
