<div align="center">

# Finding First Customers

### An AI coding-agent skill that finds evidence-backed potential first customers inside a specific target market

</div>

---

This skill takes a product URL or idea and produces a shortlist of prospects verified as
inside a specific target market, sourced from public signals on X, Reddit, and LinkedIn.
Each prospect carries a verbatim quote in the market's own language, a link you can open,
and a stated reason for why they were judged to be in scope. It also extracts product
intelligence from the same signals — feature gaps, landing-page vocabulary, a channel map,
and trust objections — whether or not a shortlist ships.

It never sends outreach.

## Install

One command, no clone, no config. Requires Node.js; works the same on macOS, Linux, and
Windows.

```bash
npx --yes finding-first-customers-skill@2.0.0
```

That installs to `~/.claude/skills/finding-first-customers`. Other targets:

```bash
# Codex
npx --yes finding-first-customers-skill@2.0.0 --agent codex

# ~/.agents/skills — also read by Codex, Copilot CLI and Gemini CLI
npx --yes finding-first-customers-skill@2.0.0 --agent agents

# Claude + Codex
npx --yes finding-first-customers-skill@2.0.0 --agent both

# Project-local, checked in with the repo
npx --yes finding-first-customers-skill@2.0.0 --skills-dir ./.claude/skills
```

**Restart your agent afterwards.** Skills are read at startup; the skill will not appear
in a session that was already running.

The generated HTML report needs **Python 3.10+** on your PATH. Everything else in the
skill is plain markdown.

### From a clone

Works without npm, and is the route to take if you want to edit the skill.

```bash
git clone https://github.com/abdullah7041/saudi-first-customer-finder.git
cd saudi-first-customer-finder
node scripts/install.js          # same flags as above
node scripts/install.js --link   # link the checkout instead of copying
```

`--link` points the installed path back at your clone, so edits take effect on the next
agent restart with no reinstall. On Windows it creates a directory junction, which needs
no administrator rights.

## Usage

Paste a link. That's the whole instruction.

```
Use $finding-first-customers on https://example.com
```

The skill reads the site itself — landing copy, pricing, features, any localized version —
derives the target market and its search vocabulary at runtime, infers the ICP, picks
`deep` mode, and runs. It asks you nothing beyond one labelled assumption when the
category or market genuinely cannot be read from the site. It states the brief and the
market profile it inferred before searching so you can correct it mid-run.

Validation instead of outreach:

```
Use $finding-first-customers in research-only mode for [URL]. I want the pain patterns,
feature gaps, vocabulary, and trust objections — no outreach drafts.
```

Business customers:

```
Use $finding-first-customers in b2b mode for [URL]. Find companies in [market] with
public timing triggers and the decision roles associated with them.
```

## How it handles a market it has never seen

The skill ships no lexicon and no country list. At the start of every run it derives a
market profile from the product's own site and a handful of real search results: the
market and the language its buyers actually write in, real phrase forms for demand, pain,
workaround, and switching (never a translation of the English brief), a three-rung ladder
of how the problem is solved today, the one platform where the audience writes in
searchable text, and the observable markers that place someone inside the market rather
than a neighbour. That derivation is capped at five queries and is finished before any
prospecting query is spent — every later step, including the pre-flight fit check and the
scope filter, consumes its output by name. See
`finding-first-customers/references/market-profile.md` for the method, and
`finding-first-customers/examples/saudi.md` for one market worked through it end to end.

## Modes

| Mode | Prospects | Min queries | Use for |
| --- | --- | --- | --- |
| `fit-check` | none | 4 | Pre-flight only — is this category even searchable, and is the platform even reachable |
| `quick` | 5 | 20 | Fast sanity check |
| `standard` | 10 | 35 | Balanced run |
| `deep` | 20+ | 60 | **Default.** Full local-language fan-out and pattern analysis |
| `research-only` | none | 60 | Product intelligence only — no shortlist, no individuals named |
| `b2b` | 12 | 40 | In-market companies and business triggers |
| `consumer` | 20+ | 60 | Individuals only, consumer-platform-weighted, dialect-heavy |

## What the report contains

1. Verdict — is there reachable demand, and where
2. At-a-glance dashboard — score distribution, platform mix, signal freshness
3. ICP — buyer, job, trigger, disqualifiers
4. Audit strip — candidates examined, rejected on scope, dropped at link verification
5. Top prospect
6. Prospect shortlist — source-language verbatim, English translation, verified link,
   six-dimension score, scope tier
7. **Rejection log** — counts by reason and platform, no identities
8. Repeated patterns
9. **Competitive landscape** — who already sells to this customer, how they take orders,
   what they charge
10. **Feature gaps** — build vs. message, ranked by count
11. **Vocabulary table** — landing-page copy sourced from customers
12. **Channel map** — where demand concentrates and whether promotion is allowed there
13. **Trust objections** — quoted adoption blockers
14. Seven-day manual validation plan
15. Limits

## Scoring

Six weighted dimensions, 0–5 each:

| Dimension | Weight |
| --- | --- |
| Scope match | 20% |
| Pain strength | 20% |
| Product fit | 20% |
| Timing (12-month decay) | 15% |
| Reachability | 10% |
| Evidence quality | 15% |

Hard gates, applied before the total matters:

- `scope_match < 3` → excluded from the shortlist, logged as rejected
- `link_verified != true` → dropped entirely
- No source-language verbatim on a non-English source → not shippable

Below 55 does not make the primary shortlist.

## Data access

Three paths, all within platform rules:

- **Path A** — a logged-in browser session driven by the agent. Real platform search and
  real results. Used like a human would use them.
- **Path B** — public web search with `site:` operators. No credentials, shallower, and
  the report says so.
- **Path C** — the source ladder, run when Path A and Path B both fail to reach the
  platform: localized app-store reviews, competitor pages, the free government incumbent,
  vertical platforms, video-platform titles, forums. Yields product intelligence, never
  prospects.

A pre-flight fit check runs a control query before any probe, and can return one of four
verdicts: **green** (run `deep` as designed), **amber** (run `deep`, expect a short list),
**red** (switch to `research-only` — the demand is not visible), or **PATH-B BLIND** (the
search path cannot return posts from the platform at all — no market verdict is issued,
and the run stops for the user to choose a session, the source ladder, or a different
platform). The control exists so a search path that cannot see the platform is never
mistaken for a quiet market.

No login-wall bypassing, no paywall circumvention, no rate-limit evasion, no scraping
against a site's terms, no data brokers, no leaked datasets, no private groups, no
personal email or phone enrichment.

## Ethics

- Prospects are hypotheses from public signals — never confirmed buyers, never people who
  consented to contact.
- The skill drafts openers. It never sends, replies, follows, connects, comments, or
  writes to a CRM.
- Scope verification is a **market-scope filter** applied to public self-description. It
  is never a judgment about any person. Rejections ship as counts by reason and platform —
  no handle, no link, no quote — because a name printed beside an inferred market
  attachment is a claim about a person no matter how neutral the wording around it.
- Quoted verbatims are capped at 280 characters. Past that the report has stopped citing
  evidence and started republishing someone's post.
- No targeting or inference on tribe, sect, religion, health, financial hardship,
  political view, or nationality as a slur.
- Public professional information only. A person's title and public posts are evidence;
  their phone, email, and address are not, and are never collected.

## Repo layout

```
saudi-first-customer-finder/
├── finding-first-customers/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── examples/
│   │   └── saudi.md                         Worked example of the runtime market profile
│   ├── references/
│   │   ├── market-profile.md                Runtime derivation of vocabulary and scope
│   │   ├── fit-check.md                     Pre-flight category and reachability screen
│   │   ├── platform-playbooks.md            X, Reddit, LinkedIn tactics
│   │   ├── scope-verification.md            Market-scope markers and rejection rules
│   │   ├── research-framework.md            Scoring, gates, product intelligence
│   │   └── report-artifact.md               JSON schema
│   └── scripts/generate_report.py           Bilingual RTL-aware HTML generator
├── scripts/install.js                          Cross-platform installer
├── package.json
├── LICENSE
└── README.md
```

## Credits

Rebuilt from the [first-customer-finder](https://github.com/Kappaemme-git/codex-first-customer-finder-skill)
skill by Francesco Mistero (MIT). The workflow spine and report-generator approach come
from that project. This version adds: a pre-flight fit check with a blind-path control,
runtime market profiling in place of a shipped lexicon, market-scope verification,
link verification, privacy-safe rejection reporting, product intelligence, and the HTML
report.

## License

MIT
