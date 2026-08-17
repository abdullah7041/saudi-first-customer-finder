# finding-first-customers — design

Generalize `saudi-first-customer-finder` into a market-neutral skill, published as
`finding-first-customers-skill@2.0.0`.

## Problem

The skill finds evidence-backed potential first customers from public signals, and it
works — but every market-specific fact is hardcoded to Saudi Arabia: an Arabic lexicon,
Saudi dialect markers, Saudi platform assumptions, a scoring dimension called
`saudi_authenticity`. A user in Brazil or Germany gets nothing.

The Saudi specificity was never the point. The point was the *insight* behind it: demand
is written in the customer's own words, not in translated English, and a report built on
the wrong population is a report about a different market. That insight is universal. The
Arabic was one instance of it.

## Approach

Replace hardcoded market knowledge with a method for deriving it at runtime. Saudi
becomes a worked example demonstrating the method rather than the skill's subject.

Rejected alternatives:

- **Shipped per-country profiles.** High quality where a profile exists, useless
  elsewhere, and every profile rots as platforms and incumbents change. Unbounded
  maintenance for bounded coverage.
- **User supplies the profile.** Breaks paste-a-URL-and-go, and most users cannot name
  their market's informal incumbent offhand — which is exactly the fact the skill exists
  to surface.

## What carries over unchanged

These are the additions this rebuild made over the upstream skill it came from. All are
market-neutral already, and all stay:

| Capability | Why it stays |
| --- | --- |
| Pre-flight fit check | Screens categories that cannot produce a shortlist, before an hour is spent |
| Blind-path control query | Distinguishes "the market is quiet" from "the search path cannot reach recent posts" |
| Link verification gate | A prospect whose source cannot be re-opened is dropped |
| Verbatim + translation | Applies to any source language that is not the report language |
| Privacy-safe rejection log | Counts by reason, never identities |
| Six-dimension scoring with hard gates | Ordering is not the same as qualification |
| Product intelligence | Feature gaps, vocabulary, channel map, trust objections |
| Competitive landscape | The incumbent is often a human service or a free workaround, not an app |
| Source ladder | Makes `research-only` a procedure rather than a word |

## What changes

### 1. New file: `references/market-profile.md`

Runs first on every job, before the fit check. At most five queries, producing six
outputs — the first is read from the product site rather than searched for:

1. **Market and language** — inferred from the product's own site
2. **Local phrasing** for demand, pain, workaround, switching, and timing — sourced by
   reading real posts in the local language, never by translating English phrasing
3. **Incumbent ladder** — the free or official option, the informal human service, the
   DIY workaround. This sets the price anchor the product is compared against
4. **Where the audience writes** — which platform carries searchable text in this market
5. **Scope markers** — what distinguishes someone in the target market from a visitor in
   public text: spelling and dialect, civic references, currency, timezone, local
   institutions
6. **Trust objections** — what makes people in this market distrust this category

The governing rule, stated once and enforced throughout: **translated queries find
translated people.** An English query rendered into the local language by an agent finds
the population that also writes translated English. The phrasing must come from reading
what people in that market actually wrote.

### 2. Renames

| From | To | Reason |
| --- | --- | --- |
| `saudi-identity-verification.md` | `scope-verification.md` | Verifying market scope, not nationality |
| `saudi_authenticity` (score) | `scope_match` | Same weight, same gate at < 3 |
| `arabic-query-lexicon.md` | folded into `examples/saudi.md` | Becomes illustration, not instruction |

The scope-verification file keeps its current framing intact: this is a market-scope
filter applied to public self-description, never a claim about a person, and rejections
ship as counts.

### 3. `examples/saudi.md`

The Arabic lexicon, Saudi dialect markers, and the two recorded field tests, presented as
the method applied end to end. Shows what a completed market profile looks like. A reader
targeting Brazil should be able to read it and see the shape they need to produce.

### 4. Report generator

Labels become market-neutral. Bidi handling stays — it is already correct for RTL and
must not regress, since the worked example depends on it. `aggregate_rejected` and the
280-character quote ceiling are unchanged.

## Naming and migration

- Skill directory: `finding-first-customers`
- npm package: `finding-first-customers-skill`, version `2.0.0`
- `saudi-first-customer-finder-skill` is deprecated via `npm deprecate`, pointing at the
  new package. No final release needed; 1.0.0 stays installable for anyone pinned to it.
- Repository keeps its current URL. README is rewritten plain and factual: what the skill
  does, when to use it, what it produces. Arabic appears only inside the worked example.

Version 2.0.0 rather than 1.2.0: the skill's subject changes, `saudi_authenticity`
disappears from the report schema, and existing analysis JSON will not validate.

## Testing

| Gate | Method | Pass condition |
| --- | --- | --- |
| Generator regressions | Unit-test `aggregate_rejected`, quote ceiling, RTL and LTR rendering | No identifier reaches the HTML from a payload containing handles; quotes truncate at 280; both text directions render |
| Package integrity | `npm pack` and install the tarball into a temp skills dir | Frontmatter parses; no `__pycache__`; every reference file present |
| **Generalization** | Live `fit-check` run on a non-Saudi, non-Arabic product | The market profile derives a language and phrasing set with no Arabic anywhere, and the fit check reaches a verdict on that basis |
| No regression on the worked example | Re-run `fit-check` on the Saudi case | Same verdict as the recorded field test, given the same search path |

The generalization gate is the one that matters. If the method only works in Arabic, it
fails there and the design is wrong.

## Out of scope

- `design-partners` mode from the upstream skill — no observed need, and upstream's
  version is a table row with no procedure behind it
- Per-country profile files
- Multi-language report output — the report is written in the user's language; only the
  evidence is bilingual

## Risks

**The derivation is only as good as the agent doing it.** Hardcoded lexicons are wrong
in fewer ways than derived ones. Mitigation: `market-profile.md` must be concrete and
checkable — every output has a stated source and a way to tell a good result from a bad
one — and the profile is stated to the user before searching, so a wrong derivation is
correctable mid-run rather than discovered in the report.

**Wording is untested.** The market-profile method is behaviour-shaping guidance. Per
writing-skills it warrants a micro-test against a no-guidance control before it can be
called verified. The live acceptance run is a single sample, not that test.
