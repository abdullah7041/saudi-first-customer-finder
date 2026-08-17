# Acceptance run — 2.0.0 generalization

> **German is no longer in supported scope.** After this run, the skill was limited to
> Arabic and English — one product in one market is not enough evidence to claim a
> language. This record stays because it is the evidence that the architecture
> generalizes, which is what justifies keeping that architecture behind the limit. It is
> not a support claim. A repeat of this run is what it would take to add German.

Ran 2026-08-18 against a non-Saudi, non-Arabic product, following
`finding-first-customers/references/market-profile.md` as written.

**Product:** sevdesk (https://sevdesk.de) — invoicing and bookkeeping SaaS for German
freelancers, sole traders and small businesses. Chosen because German inflects for case
and gender and splits formal/informal register, which tests the "vary the forms"
instruction that was written generically after being derived from Arabic.

**Search path:** Path B (public web search with `site:` operators). No logged-in session.

## Derived market profile

| Output | Result | Source |
| --- | --- | --- |
| Market and language | Germany, Austria secondary. Buyers write German. EUR pricing, legal entity Offenburg. | sevdesk.de homepage, pricing, footer — no query spent |
| Local phrasing | See below — 4 of 5 buckets filled | 4 queries |
| Incumbent ladder | Free/official: none in this category. **Informal human service: Steuerberater (tax advisor).** DIY: spreadsheets, paper, "Buchhaltung selber machen" | queries 2-3 |
| Where the audience writes | **German vertical forums** — sellerforum.de, rechnungswesenforum.de, finanztip.de/community, lex-forum.net, datev-community.de, and trade forums like woodworker.de | queries 2-3 |
| Scope markers | German-language posting, EUR amounts, German tax vocabulary (Kleinunternehmer §19 UStG, Finanzamt, GoBD, Steuerberater), DE/AT platform choice | queries 2-4 |
| Trust objections | Data availability after cancellation; whether software covers a GmbH; GoBD-compliant archiving | queries 3-4 |

### Local phrasing recorded

| Bucket | Verbatim form | Source |
| --- | --- | --- |
| Pain | "Sicher gibt es günstigere Lösungen, aber ich hasse Buchhaltung" | sellerforum.de thread 58564 |
| Pain | "ich alleine in der Buchhaltung" | rechnungswesenforum.de thread 6576 |
| Explicit demand | "Wie macht Ihr eure Buchhaltung? Welches Tool?" | sellerforum.de thread 58564 |
| Explicit demand | "Erfahrungen mit digitaler Buchhaltung & E-Rechnung gesucht" | finanztip.de community 43583 |
| Workaround | "Buchhaltung selber machen?" | rechnungswesenforum.de thread 419978 |
| Workaround | "macht hier jemand seine Buchhaltung selbst?" | woodworker.de thread 115130 |
| Switching | "Wechsel von DATEV Unternehmen Online zu Lexoffice" | datev-community.de 460785 |
| Switching | GmbH "von DATEV (über Steuerberater) zu lexoffice" gewechselt, zum 1.1.2024 | lex-forum.net 14694 |
| Timing trigger | E-Rechnungspflicht — receiving mandatory since 2025-01-01, issuance for all B2B from 2028 | IHK Frankfurt, vendor guides |

Timing trigger returned vendor and chamber-of-commerce pages rather than first-person
posts. Recorded as vendor-heavy rather than padded.

## Control query

`"hat jemand Erfahrung" 2026 site:sellerforum.de OR site:rechnungswesenforum.de OR site:finanztip.de`

One qualifying first-person thread (finanztip.de community 45087, April 2026). The rest
were Finanztip's own SEO review pages, not community posts. Under the four qualifying
conditions that is 1 of the 3 required, which lands in the **PATH-B BLIND** band.

The control query itself was weak — mixing three `site:` operators with a year token
pulled the host's marketing pages ahead of its forum. A cleaner control would target one
forum at a time. The verdict machinery executed correctly on the input it was given.

## Verdict against the four pass conditions

| # | Condition | Result |
| --- | --- | --- |
| 1 | Derived market and language match the product's actual target market | **PASS** — Germany/Austria, German |
| 2 | Recorded phrasing is idiomatic, not translated English | **PASS** — see below |
| 3 | Control query and verdict logic execute normally | **PASS** — executed, scored, banded |
| 4 | No Arabic and no Saudi-specific assumption anywhere in the run | **PASS** — see below |

**On condition 2.** The forms are ones a translation step would not have produced.
"Buchhaltung selber machen" is how the workaround bucket is actually written; an English
brief translated forward gives "Buchhaltung selbst erledigen" or similar and misses the
threads. "Ich hasse Buchhaltung" appears mid-sentence inside a post about tool choice —
found by reading the result, not by querying for it. Query 1 failed exactly as the file
predicts a translated door-form fails: it returned Shopify and SEO content farms and zero
first-person posts, and the file's prescribed fix (broader first-person verb, not better
translation) is what recovered it on query 2.

**On condition 4, the strongest evidence in this run.** The two most Saudi-shaped
defaults in the 1.x skill both came out different here, without intervention:

- **Platform.** 1.x asserted X as the primary source. The derivation named German
  vertical and vendor-run forums, and never proposed X.
- **Informal incumbent rung.** 1.x described a human service selling over WhatsApp. The
  derivation named the Steuerberater — a regulated professional, billing by fee schedule.
  The rung's shape survived; its instantiation did not.

Nothing in the run referenced Arabic, dialect splits, or any Saudi institution.

## Budget

Four searches for the profile plus one control. Under the five-query cap. Output 1 and
the incumbent/competitor pages were named-page lookups and unbudgeted, as the file
specifies.

## What this run does not establish

One product, one market, one search path, one agent. It shows the method produces a
market-appropriate profile for a language it was not derived from — not that it does so
reliably. `market-profile.md` is behaviour-shaping guidance and has not been micro-tested
against a no-guidance control across repeated runs, which is what
superpowers:writing-skills asks for before calling wording verified.

The PATH-B BLIND band reached here is a property of the search tool available, not a
finding about the German market.
