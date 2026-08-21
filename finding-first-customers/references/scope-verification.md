# Scope Verification

The single biggest failure mode of market research is a shortlist full of people who are
not in the target market. Neighbouring-market threads, region-wide accounts, and
translated content farms dominate the easy search results. This file is the filter.

## What this is and is not

This is a **market-scope filter** applied to what people have chosen to publish about
themselves. It exists so a report about a market's demand is actually about that
market's demand.

It is **not** a judgment about any person, and it is not a nationality check in the legal
sense. Never use it to make claims about someone's worth, rights, or belonging. Write
every rejection reason neutrally and factually: "neighbouring-market language markers, no
target-market context" — never anything pejorative. Do not attempt to identify tribe,
sect, region as ethnicity, or immigration status.

## Verification tiers

| Tier | Requirement | Shortlist eligible |
| --- | --- | --- |
| **Confirmed** | 2+ independent in-market signals, 0 contradictions | Yes |
| **Likely** | 1 strong in-market signal, 0 contradictions | Yes, labelled |
| **Unverified** | ICP match but no scope signal | No — log only |
| **Rejected** | Any disqualifying marker, or no in-market signal at all | No — log with reason |

Independent means from different categories of the scope markers derived in the market
profile (`references/market-profile.md`, "Scope markers" output). Two mentions of the
same category are one signal, not two. A marker from the permitted list plus a stated
location is two.

## Applying the scope markers

The market profile derives the observable signals that place a person inside the target
market rather than a neighbouring one, and their counterparts that indicate the
neighbouring market instead — see `references/market-profile.md`, "Scope markers." Use
those markers here, not a shipped list: read every candidate's recent posts against the
categories the profile recorded (self-described location, civic and institutional
references, currency and price conventions, timezone as a weak supporting signal only,
language variety, and local platform use), and score independence and contradiction
exactly as the tiers above define them.

The market profile also carries the forbidden list — tribe, ethnicity, religion, health,
financial hardship, political affiliation, immigration or residency status, legal status
of any kind, and nationality used pejoratively. That list is not restated here; it is
binding on this filter exactly as written there, with no exceptions carved out for a
particular market.

**Regional overlap.** Some markets share a language, or a language variety, with a
neighbour, and the market profile will name the civic or institutional markers that carry
the distinguishing weight in that case — dialect and vocabulary alone will not separate
them. When a candidate's writing matches the target market's language variety but also
carries a neighbouring market's civic markers (a different government platform, a
different currency, a different city named as home), the civic contradiction outranks the
linguistic match.

## Disqualifying markers — automatic rejection

A candidate is rejected outright, without reaching a tier, on any of the following:

- Any marker the profile records as belonging to a **neighbouring market** rather than the
  target one — the language-variety and civic counterparts named alongside the scope
  markers themselves.
- Any marker from the forbidden list above, however it is phrased.
- Non-human and commercial accounts: brands, agencies, recruiters, resellers, content
  farms, SEO blogs, news outlets and aggregators, and obvious bots (repetitive posting,
  engagement-bait, follower-farm patterns, an entirely promotional feed). Reject these
  outright — do not log them as prospects, and do not log them in the rejection count
  either, since they were never in scope to begin with.

Context indicating the person is a visitor, remote worker, or resident of the target
market without being part of it (as the profile's forbidden list defines that boundary)
is handled neutrally: log it, do not delete it, and do not use immigration or residency
status as the deciding factor — the market profile's warning on this point governs.

## Contradiction handling

A contradiction outranks a positive signal. Example pattern: a target-market civic marker
appears alongside a neighbouring-market language-variety marker with no counter-signal —
that is a contradiction, and it is rejected, not averaged.

When signals genuinely conflict and neither dominates, the tier is **Unverified**, not
Likely. Unverified never enters the shortlist.

## Recording the verdict

For every candidate examined, record the tier, the markers that produced it (by category,
not verbatim personal detail beyond what the profile permits), any contradictions, and a
reason for anything not confirmed or likely.

Confirmed and likely go to `prospects`. Unverified and rejected go to `rejected` in the
report JSON. Rejections are recorded as counts, with no identifier — see
`references/report-artifact.md`'s field rules for exactly which fields a `rejected` entry
may and may not carry. Publishing the rejection log is what makes the shortlist credible —
it shows the filter ran and what it cost, without publishing a claim about any individual.

## Practical guidance

- Read the account's recent posts, not just the one that matched the query. One post is
  not a language sample.
- A retweet or quote is not the person's own words. Verify the marker comes from text
  they wrote.
- Bios lie less often than you'd expect, but empty bios are the norm. Absence of a
  location is not a contradiction — it just means you need a language-variety or civic
  signal instead.
- If the whole shortlist ends up `likely` rather than `confirmed`, say so in the limits
  section. That is a real weakness in the evidence, not a detail to bury.
- If in-market signals are genuinely absent across the entire search, the honest finding
  is that demand for this product is not publicly visible yet in this market. Report that.
