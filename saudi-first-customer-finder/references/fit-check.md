# Pre-flight Fit Check

A full run is 60+ queries and a long stretch of work. Some categories cannot produce a
prospect shortlist no matter how well the run is executed — the demand is not written
down in public text, or targeting the people who have it would be wrong.

This check costs **four queries and about a minute** — one control plus three probes. It
runs on the market profile's outputs, so `references/market-profile.md` is derived first,
once per job; the check then runs before any prospecting query is spent. It ends with one
verdict, stated to the user before any real searching begins.

Two of the profile's six outputs drive this check. **Local phrasing** supplies every query
below, and **where the audience writes** supplies the platform those queries are aimed at.
Wherever this file says "the platform" it means that named platform, and wherever a query
template asks for a phrase form it means one recorded verbatim in **local phrasing** —
never one translated at this step.

## Step 1 — Category screen, no searching required

Read the product brief against this table before spending a single one of this check's
queries.

| Category | Verdict | Why |
| --- | --- | --- |
| Health conditions, mental health, addiction, fertility, disability | **Prospecting off** | Targeting people on health signals is forbidden by this skill's own rules, and the posts are rarely public anyway |
| Debt, financial hardship, bankruptcy, salary loans | **Prospecting off** | Same rule: financial hardship is a protected signal, never a targeting criterion |
| Dating, marriage, divorce, family conflict | **Prospecting off** | Intimate and identifying; the harm from being named in a report outweighs the research value |
| Religion, sect, political affiliation | **Prospecting off** | Protected attributes. Not targetable, not inferable |
| Legal trouble, immigration status, criminal record | **Prospecting off** | Identifying and potentially harmful |
| Enterprise B2B, government procurement, defence | **Company triggers only** | Nobody posts procurement pain publicly. `b2b` mode finds hiring, expansion, and programme triggers instead of individual complaints |
| Products for children, elderly, or blue-collar workers | **Proxy only** | The end user is not on these platforms. Search for the person who buys on their behalf — a parent, an adult child, an employer |
| Single-location physical business (a café, a clinic, a barber) | **Intel only** | Demand is foot traffic, not posts. Vocabulary, competitors, and objections still work |
| Anything else sold to consumers or small businesses in the target market | **Proceed** | This is the skill's home ground |

**Prospecting off** does not mean stop. It means switch to `research-only`, skip the
prospect shortlist and the rejection log, and deliver the product-intelligence half:
vocabulary, trust objections, competitive landscape, and channel map. Those are built
from how people discuss the *category*, not from identifying individuals — which is both
safer and, for a sensitive product, usually the more useful half anyway.

Say plainly which rule was applied and why. Never silently downgrade the run.

## Step 2 — Control query, before any probe

**REQUIRED. Run this first, every time — first within this check.** It measures the search
path, not the market.

Fire one first-person query in the market's language with no category noun at all — a
phrase the platform is certainly full of, on any topic.

Take three forms from the **pain** bucket of **local phrasing**, choosing the ones that
already carry **no category and no domain noun**: the bare first-person expressions of
frustration or exhaustion that people type about anything. Those are what a control is made
of, because their volume on the platform has nothing to do with this product. Use them
exactly as recorded.

**Do not manufacture one by deleting the noun from a longer recorded form.** A stripped
form is no longer verbatim, and `references/market-profile.md` is explicit that case,
gender, agreement, and contraction break single-form matching — remove a token from an
inflected phrase and you can be left with a string the index has never contained. The
control would return zero, the run would report **PATH-B BLIND**, and the user would be
sent to `research-only` over a search path that was never blind. That is precisely the
misreading Step 2 exists to prevent.

If no recorded pain form is category-free, do not search for one and do not invent one.
Open a pain post you already read for the profile and lift the generic fragment verbatim
from it. That is a lookup of something already named, not a search, so it costs nothing —
and it is the only way to get a form that is both verbatim and category-free.

```
site:<the platform> ("<generic pain form>" OR "<generic pain form>" OR "<generic pain form>") <the platform's language filter, if it has one>
```

Three forms, not one, because **local phrasing** records spelling and inflection variants
for a reason — a single form can be absent from an index for orthography alone, and that
would read here as a dead search path.

**On the language filter slot.** **Where the audience writes** names a platform, not query
syntax, and many platforms — forums, discussion boards, professional networks — have no
language operator at all. Where the platform has one, use it. Where it does not, omit the
slot and enforce the language by reading the results, exactly as you do for the four
qualifying conditions below. A filter you cannot express is never a reason to translate the
query into a language the platform can filter on.

Count a result only if **all four** hold. Anything else scores zero:

1. It is a permalink to a single post — the platform's single-post URL form — not a
   profile, search, or landing page. A profile whose *username* happens to contain the
   phrase is not a hit.
2. The post text is visible, and the phrase is in the text — not only in the URL slug.
3. Someone is describing their own situation. Not poetry, quotes, lyrics, or reposted
   aphorisms, all of which the general indexes carry in bulk and which get reposted
   forever on every platform.
4. Posted within the last 24 months.

| Qualifying posts | Meaning | Action |
| --- | --- | --- |
| 3 or more | The search path can see the corpus | Continue to Step 3 |
| 0–2 | The search path cannot reach recent posts | Stop. Verdict is **PATH-B BLIND**, not red |

Two is blind, not borderline. Note what the failure usually looks like: not an empty
result, but three real permalinks that are all years old and all high-engagement. A
general index carries the viral back-catalogue and misses this month entirely. Demand
signals are recent, narrow, and low-engagement — the exact slice such a path cannot
return. Report it as *cannot reach recent posts*, not *cannot see the platform*: the
distinction tells the user their next move is a session, not a different platform.

A search path that cannot return first-person posts on a topic the platform is saturated
with cannot produce evidence of absence for a narrower one. Reporting red from a blind
path states a fact about the market that was never measured.

Budget: one control plus three probes. Four queries total — the check's own budget, held
separately from the five the market profile already spent.

## Step 3 — Three probe queries

One query per bucket, in the market's language, on the platform named by **where the
audience writes**. Three of **local phrasing**'s five buckets are probed here — explicit
demand, pain, workaround. **Switching / competitor** and **timing trigger** are
deliberately not probed: both need an incumbent or an event already named before a query
against them means anything, and the budget does not stretch to them. Do not run more than
three. Do not fix a disappointing probe by adding a fourth — the point is a fast read, and
a category that needs six queries to show one signal is already telling you the answer.

1. **Demand probe** — the recorded **explicit demand** forms + the category noun
   `("<demand form>" OR "<demand form>" OR "<demand form>") [category noun] <language filter, if the platform has one>`
2. **Pain probe** — the recorded **pain** forms + the domain noun
   `("<pain form>" OR "<pain form>" OR "<pain form>") [domain noun] <language filter, if any> <exclude-links operator, if any>`
3. **Workaround probe** — the recorded **workaround** forms + the domain noun
   `("<workaround form>" OR "<workaround form>" OR "<workaround form>") [domain noun] <language filter, if any>`

Both operator slots follow the Step 2 rule: use them where the platform has them, omit them
where it does not, and never reshape a query to suit an operator it cannot express.

Use the forms verbatim, including the spelling and inflection variants the profile stated
it searched. Do not compose a fresh phrase here by translating the product brief: a
translated probe measures the translated population the profile exists to route around,
and a zero from it is unreadable.

If the product has no obvious category noun in the market's language, that is itself a
signal — note it and lean toward amber at best.

## Step 4 — Count three things

For each probe, count only what a full run would actually keep:

- **First-person in-market hits** — someone describing their own situation, carrying at
  least one of the profile's **scope markers**, who is not selling anything
- **Vendor ratio** — share of results that are ads, service accounts, or content farms
- **Freshest hit** — age of the most recent qualifying result

Then apply:

| Verdict | Condition | Action |
| --- | --- | --- |
| **Green** | 6+ first-person in-market hits across the three probes, and at least one under 30 days old | Run the full `deep` pass as designed |
| **Amber** | 2–5 hits, or every hit older than three months, or vendor ratio above 60% | Run `deep`, but say up front that the shortlist will be short. Consider widening the date window before widening the geography |
| **Red** | 0–1 hits, or vendor ratio above 80%, or all three probes return only ads and unrelated stemming noise | Do not run the full prospecting pass. Switch to `research-only` and explain the finding |

**Red requires a control that passed.** If the control in Step 2 came back blind, the
verdict is `PATH-B BLIND` no matter what the probes returned. Red says the market is
quiet; blind says you could not hear it. They lead the user to opposite decisions —
abandon the category, versus get a session and look properly.

When the result sits between two bands, take the lower one. Optimism here costs the user
an hour. Blind is not a band — it replaces the verdict entirely.

### Counting the vendor ratio honestly

Every large platform carries a population of general-services accounts — essay mills,
assignment shops, design and translation sellers — that list dozens of deliverables in one
post. Any probe containing a **deliverable noun**, meaning the name of the artefact the
product produces rather than the trouble it removes, will pull them in bulk, and a probe
can easily return 100% of them.

They count fully toward the vendor ratio. Do not discount them as noise: a category
where sellers outnumber sufferers this heavily is telling you something real about how
the demand gets met. Route them to the competitive landscape and let the ratio push the
verdict down.

The bare generic word for the artefact is the worst offender. Prefer workaround forms that
describe **an action** — doing it by hand, doing it in a spreadsheet, doing it with a
general AI assistant — over forms that name a product. An action separates a person from a
shop, which is exactly why **local phrasing**'s workaround bucket is defined as how someone
does it manually today. The rule the whole check rests on: **symptom phrases find buyers,
category nouns find vendors.**

Deliverable nouns and preferred action forms worked out for one specific market are in
`examples/saudi.md`.

### Observation — the check against a full run

From the Saudi worked example in `examples/saudi.md`, kept as an observation from one
market rather than as thresholds to reuse. Its specifics are stated plainly because they
are one market's data, not a template. Run against an Arabic-first Saudi CV product on
2026-08-05, the check — then three probes, before the control existed — returned:

```
Probes:          demand 1 · pain 2 · workaround 0 first-person Saudi hits
Vendor ratio:    ~75% overall, 100% on the workaround probe
Freshest signal: 8 days
Verdict:         AMBER — running deep, expect a short list
```

A full 60-query pass on the same product, run separately, produced exactly that: one
strong prospect, a wall of WhatsApp CV services, and a free circulating ChatGPT prompt
as the real incumbent. That three-probe check reached the same conclusion in three
queries. That is the entire point of it.

### Observation — why the control exists

Also from the Saudi worked example, and likewise stated in its own specifics. Run on
2026-08-16 against a Saudi resume-matching product, on a harness whose only web search was
a general index with `site:x.com`:

```
Probes, noun-framed:     demand 0 · pain 0 · workaround 0
Probes, symptom-framed:  demand 0 · pain 0 · workaround 0
Returned instead:        blogs, Quora, Iraqi Facebook pages, TikTok discover pages
```

Six probes, two framings, zero first-person posts — while the same index returned plenty
of *other* Arabic job-seeking content. The check reported RED twice. That was wrong: X is
saturated with Saudi job-seeking complaints, and the run had simply established that the
search path could not return X post text at all.

The control was then run on the same harness, on a phrase X contains millions of times. It
returned one 2024 poem and one profile page whose username *was* the search phrase —
which is why the scoring rules above are a count of qualifying permalinks rather than an
impression. Two loose matches read as "the path works." They do not.

RED told the user their market was silent. The truth was that the microphone was off.
Hence Step 2: one query would have caught it before the probes ran.

## Step 5 — State the verdict before proceeding

Report it in this shape, in six lines or fewer, then continue without waiting for
permission unless the verdict is red or blind:

```
Fit check — [product], [market]
Category screen:  proceed | prospecting off ([rule])
Control:          passed (N first-person posts) | BLIND (no platform posts returned)
Probes:           demand N · pain N · workaround N first-person in-market hits
Vendor ratio:     N%
Freshest signal:  N days
Verdict:          GREEN — running deep | AMBER — running deep, expect a short list | RED — switching to research-only | PATH-B BLIND — need a session
```

On **PATH-B BLIND**, do not issue a market verdict at all. Say that the search path
cannot reach recent posts, name the platform, and hand the user the three routes: a
logged-in session (Path A), `research-only` over the source ladder below, or a different
platform where the audience actually writes in public text.

The third route needs care, because **where the audience writes** names exactly one
platform — there is no runner-up recorded to fall back on, and the one alternative it does
record is a blind spot precisely because it carries no searchable text, so it cannot answer
a search-path failure. So do not guess. Go back to the profile's own result sets and count
again: the platform was chosen by where the qualifying first-person posts landed, and if
any of them landed somewhere else that can be read as permalinks, that second place is the
third route. If none did, say so — the third route does not exist for this run, and the
user has two, not three. A blind verdict that invents a platform is the same error as a red
verdict that invents a market.

Never soften blind into red, and never let a blind run's zero counts appear as evidence
about the market. If the counts are reported at all, mark them unmeasured.

## The source ladder — what to run when the platform is unreachable

`research-only` is the escape hatch from a red or blind verdict, so it needs to be a
procedure rather than a word. Work the ladder in order. Each rung says what it reliably
yields, because none of them yield prospects — they yield the product-intelligence half.

| Rung | Source | Reliably yields |
| --- | --- | --- |
| 1 | Localized app-store reviews of the incumbents — Apple App Store and Google Play, each with its language parameter set to the market's language | Trust objections and feature gaps, first-person, dated, and fully public |
| 2 | Competitor landing pages found by category keyword in the market's language | Price anchor, positioning vocabulary, what the market already promises |
| 3 | Government or public-sector services in the target market, in the category | The free incumbent — the one that decides whether anyone pays at all |
| 4 | The market's own vertical platforms and their content marketing (job boards, marketplaces, sector portals) | The formal register of the market's language, and which pains are common enough to write SEO about |
| 5 | Video-platform titles, comments, and discovery pages in the market's language | Where the audience actually is when it is not on the platform named by **where the audience writes**. Titles are searchable even when the discussion is not |
| 6 | Regional discussion boards and local-language forums | Long-form written pain — but these often over-represent writers who are not the market's buyers, so check the profile's **scope markers** before trusting the vocabulary they give you |

Two rules. Rung 3 is not optional in any category where a government or public-sector
service in the target market exists: a free official option resets the whole price
question, and a report that misses it recommends a price the market will never pay. This
is the price-anchor argument the market profile's incumbent ladder turns on, and this rung
is where the agent goes to look for it. And a rung that yields nothing is a finding —
record it, because "the incumbents have no reviews in the market's language" says
something about the category.

Individuals surfaced on these rungs are **not** prospects. No shortlist, no scoring, no
openers. A blind run has not verified anyone's identity and cannot start now.

On red, stop and hand the user the choice: research-only now, a different framing of the
category in the market's language, or a widened scope. Do not burn an hour proving a red
verdict right.

## What red does not mean

Red means the demand is **not visible in public text, in the market's language, on the
platforms searched**. It does not mean there is no market. Common innocent explanations:

- The audience lives on a platform that carries no searchable text — which **where the
  audience writes** should already have recorded as a known blind spot
- The problem is embarrassing, private, or discussed only in closed groups
- The category is too new to have a name people type
- The pain is real but low-salience — annoying enough to tolerate, not to post about
- The framing used in the probes is wrong — **local phrasing** may have missed the
  register this particular category is discussed in

Say which of these you think it is. "No public signal" plus a plausible reason is a
finding the user can act on. "No prospects found" with no explanation is a failed run.

## Cost discipline

The fit check is four queries — one control plus three probes. If it starts turning into
ten, it has stopped being a check and become the run. Stop, take the lower verdict, and
move on.
