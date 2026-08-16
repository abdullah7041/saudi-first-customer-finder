---
name: saudi-first-customer-finder
description: Use when someone gives a product URL or idea and wants first customers, early adopters, demand validation, or customer research inside Saudi Arabia (KSA) — including defining a Saudi ICP, finding Saudi-dialect Arabic pain or demand signals on X, Reddit or LinkedIn, checking whether a prospect is actually Saudi rather than expat or other-Gulf, or sourcing Arabic landing-page vocabulary from real Saudi users.
---

# Saudi First Customer Finder

Turn a product URL or idea into a short, evidence-backed list of plausible first
customers **inside Saudi Arabia**, plus the product intelligence hidden in their own
words. Every prospect is a hypothesis backed by a live public link and a verbatim
quote. Never a confirmed buyer.

This skill is a Saudi-market rebuild of the generic first-customer-finder pattern. The
three things it does that a generic version cannot:

1. **It searches in Saudi Arabic**, not translated English. Real demand is written
   `أبغى أداة تسوي كذا` and `تعبت من...`, not "looking for a tool that".
2. **It proves the person is Saudi.** Dialect markers, local context, and an explicit
   rejection log — because "Saudi market" searches overwhelmingly return expat and
   other-Gulf voices, and a report built on those is a report about a different market.
3. **It mines the signals for product decisions**, not just names: feature gaps,
   landing-page vocabulary, channel map, and trust objections.

## Required reading

Read these before acting. Do not improvise the Arabic or the scoring.

| File | Read before |
| --- | --- |
| [references/fit-check.md](references/fit-check.md) | Anything else — this runs first |
| [references/arabic-query-lexicon.md](references/arabic-query-lexicon.md) | Writing any search query |
| [references/platform-playbooks.md](references/platform-playbooks.md) | Touching X, Reddit, or LinkedIn |
| [references/saudi-identity-verification.md](references/saudi-identity-verification.md) | Qualifying or rejecting any person |
| [references/research-framework.md](references/research-framework.md) | Scoring anything |
| [references/report-artifact.md](references/report-artifact.md) | Building the report |

## Invocation

**A bare URL is a complete instruction.** When the user supplies a link and nothing else,
do not ask what the product is, who the customer is, which mode to use, or which platforms
to search. Read the site, infer everything, run in `deep` mode, and deliver the report.

The only acceptable question is a single one, asked once, when the product's category is
genuinely unreadable from its own site — and even then, make a labelled assumption and
proceed rather than blocking on an answer.

State the inferred brief before searching so the user can correct it mid-run if it is
wrong. Announce, do not ask.

## Workflow

### 0. Pre-flight fit check — three queries, always

Some categories cannot produce a prospect shortlist however well the run is executed:
the demand is not written down in public, or the people who have it must not be targeted.
Finding that out after sixty queries wastes an hour.

Run `references/fit-check.md` first, every time. It screens the category against a
do-not-target table, fires one control query and three probe queries, and returns green,
amber, red, or path-b blind.

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

Four queries is the budget — one control, three probes. If the check grows past that, it
has become the run.

### 1. Build the Saudi product brief — from the URL alone

Fetch the supplied URL and read it properly: landing copy, pricing page, features, FAQ,
about page, any Arabic version of the site, and the repo README if a repository was given.
Everything below is inferred from that reading, not from the user.

Then define:

- product, promised outcome, and the urgent job to be done
- primary Saudi ICP and one adjacent Saudi ICP
- the **Arabic** name for the problem as a normal Saudi person would say it — not the
  marketing term, the complaint term
- current workaround (very often: Excel, WhatsApp, a friend, or ChatGPT)
- adoption trigger
- disqualifiers, including any that are Saudi-specific (sector, regulation,
  Arabic-language requirement, payment method, Nafath/national-ID dependency)
- whether the buyer is an individual, a household, or a business

Label every inference as an inference. A wrong inference stated plainly is correctable; a
question asked instead of working is not.

State the brief before searching. If the brief is not specific enough to *reject* a
weak match, it is not finished.

### 2. Plan queries across five buckets and two languages

Use the lexicon file. For every bucket, generate Arabic **and** English variants, and
vary the Arabic across spelling forms (`أبغى` / `ابغى` / `أبي` / `ابي`) — Saudi users do
not write standardized Arabic and one spelling misses most of the corpus.

Buckets: explicit demand · pain · workaround · switching/competitor · timing trigger.

Minimum query counts by mode are in the Modes section. Under-searching is the most
common failure: one query per bucket produces a report that says more about the query
than about the market.

### 3. Search each platform on its own terms

Follow the playbooks. Summary of what matters:

- **X (twitter)** is the primary source for Saudi B2C consumer pain. Saudis complain on
  X in dialect, publicly, constantly. Use Arabic queries with `lang:ar`, date windows,
  and geocode filters. This is where the report earns its value.
- **Reddit** is genuinely useful but **structurally expat-skewed** in the KSA subs.
  Treat r/RiyadhExpats, r/qatar-style expat subs, and English-only KSA job threads as
  *likely disqualified* until identity is verified. Reddit is a good source for detailed
  written pain, a poor source for Saudi-national representativeness.
- **LinkedIn** is the primary source for professional and B2B signals and for Saudi
  business triggers (hiring, expansion, funding, Vision 2030 programs). Public post
  search is limited without a session — see the playbook for both paths.

Prefer opening the original post over reading a search snippet. A snippet is not
evidence.

### 4. Verify Saudi identity — mandatory gate

Apply `references/saudi-identity-verification.md` to every candidate.

- **Confirmed Saudi**: two or more independent Saudi signals, zero contradictions.
- **Likely Saudi**: one strong signal, zero contradictions.
- **Rejected**: any disqualifying dialect or context marker, or no Saudi signal at all.

Record every rejection with its reason and platform, and **no identifier** — no handle,
no display name, no link, no quote. The log ships as counts by reason. A report with no
rejection log is not trustworthy, because it means the filter never ran; a report that
names the people it rejected is worse, because it publishes an inferred nationality
attached to a real person. The count carries the whole evidentiary load.

Their pain still counts in product intelligence. It is the identity that does not ship.

Score `saudi_authenticity` below 3 is an automatic exclusion from the primary shortlist,
regardless of how strong the pain signal is.

### 5. Verify every link before it enters the report

Re-open each source URL and confirm:

- the page loads and is public
- the quoted text is actually on that page
- the visible date matches what you recorded
- the account/post has not been deleted since you found it

A prospect whose link cannot be re-opened and re-read is dropped. No exceptions, no
"probably still there". Set `link_verified: true` only after this pass.

### 6. Capture the Arabic verbatim

For every prospect, record the original Arabic text of the pain signal exactly as
written — dialect, typos, missing hamza and all — plus a faithful English translation.

Quote minimally: one or two sentences, enough to prove the signal. Never invent, clean
up, or "fix" the Arabic. The unedited text is the evidence.

### 7. Score, deduplicate, rank

Use the six-dimension framework in `references/research-framework.md`. Drop duplicates,
drop anything under the threshold, and never present a prospect as interested, consenting,
or likely to buy. The label is always "potential customer based on public signals".

### 8. Extract product intelligence

This is the section a generic prospecting skill does not produce. From the full signal
set — including rejected prospects, whose pain is still real market data — extract:

- **Feature gaps**: what people ask for that the product does not do, ranked by how many
  independent signals mention it.
- **Vocabulary**: the exact Arabic words and phrases used for the problem, the product
  category, and the desired outcome. This is landing-page and ad copy, sourced from
  customers instead of from a translator.
- **Channel map**: where the demand actually concentrates — which hashtags, which
  accounts, which subreddits, which LinkedIn communities, and how alive each one is.
- **Trust objections**: what makes Saudi users distrust this category. Pricing, privacy,
  data residency, scam fatigue, "does it actually work in Arabic", and payment friction
  all appear repeatedly. Quote them.

- **Competitive landscape**: the sellers your searches surfaced. In Saudi Arabia the
  incumbent is very often *not* another app — it is a human service sold over WhatsApp, a
  Snapchat/X account taking DM orders, or a free circulating ChatGPT prompt. Record who
  they are, what they sell, how they take orders, and any visible price. This sets the
  price anchor the product will actually be compared against.

Every item needs a count and at least one quoted source.

A note on where sellers show up: category keywords (`ATS`, the product-category noun)
tend to return vendors, while symptom phrases (`محد يرد`, `ما انقبلت`) return buyers.
When a query returns mostly sellers, that is not a failed query — route the results into
the competitive landscape and re-run the bucket with a first-person symptom phrase.

### 9. Draft openers (top three only)

Unless the mode is `research-only`:

- Write one short opener **in Saudi Arabic** for the three highest-scoring prospects.
- Ground it only in the cited public context. Do not imply familiarity.
- Match the register of the platform: X replies are short and casual, LinkedIn is
  formal, Reddit is plain and direct.
- Mark openers as optional drafts.

Never send, reply, follow, connect, comment, or create a CRM record. Drafting is the
end of the skill's authority.

### 10. Produce the report

Order:

1. **Verdict** — is there reachable Saudi early-customer demand, and where
2. **Saudi ICP** — buyer, job, trigger, disqualifiers
3. **Top prospect** — strongest verified candidate and why now
4. **Prospect shortlist** — Arabic quote, translation, verified link, scores, stage
5. **Rejection log** — who was excluded and why
6. **Repeated patterns** — pains and triggers across prospects
7. **Competitive landscape** — who already sells to this customer, and at what price
8. **Product intelligence** — feature gaps, vocabulary, channels, objections
9. **Seven-day validation plan** — manual, low-volume, Saudi-appropriate
10. **Limits** — what is missing and what must be confirmed by talking to people

Build a standalone bilingual HTML report unless the user explicitly asks for chat only:

1. Write the JSON described in `references/report-artifact.md`.
2. Run the generator **by its absolute path inside this skill directory** — the working
   directory is the user's workspace, not the skill, so a relative `scripts/...` path
   will not resolve:

   ```
   <skill-dir>/scripts/generate_report.py <analysis.json> <outputs/report.html>
   ```

   `<skill-dir>` is the directory this SKILL.md lives in — typically
   `~/.claude/skills/saudi-first-customer-finder` or
   `~/.codex/skills/saudi-first-customer-finder`. Invoke it with `python3`, falling back
   to `python` on Windows where `python3` is often absent. Python 3.10 or newer.
3. The generator creates the output directory itself; target the workspace `outputs/`.
4. Read the warnings it prints — unverified links, an empty rejection log, and missing
   Arabic verbatims are all reported on stderr/stdout and all block shipping.
5. Open the result and verify: Arabic renders right-to-left, every source link is
   present, the rejection log is populated, and no score is a placeholder.
6. Return a clickable absolute file link.

## Modes

| Mode | Prospects | Minimum queries | Notes |
| --- | --- | --- | --- |
| `fit-check` | none | 4 | The pre-flight check on its own — one control plus three probes. Answers "is this category even searchable, and can I even see the platform" in about a minute |
| `quick` | up to 5 | 20 | Sanity check or re-run against an existing baseline |
| `standard` | up to 10 | 35 | Balanced run across all three platforms |
| `deep` | 20+ | 60 | **Default.** Full dialect variation, full pattern and product-intelligence analysis |
| `research-only` | none | 60 | Product intelligence without a shortlist. Openers removed, no individuals named. Where a red or blind fit check lands — run the source ladder in `references/fit-check.md` |
| `b2b` | up to 12 | 40 | Saudi companies and public business triggers; LinkedIn-weighted |
| `consumer` | 20+ | 60 | Individuals only; X-weighted, dialect-heavy |

Default to `deep`. Announce the mode before starting — never ask which one to use. Switch
only if the user names a different mode themselves.

## Hard rules

- **Saudi or excluded.** Other-Gulf and expat voices are logged, not shortlisted, unless
  the user explicitly widens the scope.
- **No link, no prospect.** Verified and re-readable, or it does not ship.
- **No paraphrase without the original.** Every pain signal carries its Arabic verbatim.
- **Public and permitted only.** No login-wall bypassing, no paywall circumvention, no
  rate-limit evasion, no scraping against a site's terms, no data brokers, no leaked
  datasets, no private groups, no personal email or phone enrichment.
- **No sensitive targeting.** Never infer or target on tribe, region-as-ethnicity,
  religion, sect, health, financial hardship, political view, or nationality-as-slur.
  Saudi-identity verification is a market-scope filter applied to public self-description
  — it is never a claim about anyone's worth, and the rejection log states reasons
  neutrally.
- **No outreach.** Drafting only.
- **No invented numbers.** Counts come from actual observed signals. If the pool is
  thin, the report says the pool is thin.
- **Never target a sensitive category.** Health, mental health, addiction, fertility,
  disability, debt and financial hardship, dating and family conflict, religion, sect,
  political affiliation, legal trouble, and immigration status are never grounds for a
  prospect shortlist — even when the posts are public and the product genuinely helps.
  Those runs go to `research-only` and deliver category-level intelligence instead.

## Quality bar

- Ten verified Saudi prospects beat fifty unverified names.
- If the honest answer is "there is no reachable Saudi demand for this yet", say that in
  the verdict. A negative verdict backed by evidence is a useful result.
- Show the search scope and the date window. Stale evidence must be visible, not hidden.
- The product-intelligence section should change what the user builds next. If it only
  restates the prospect list, it is not finished.
