<div align="center">

# Saudi First Customer Finder

### An AI coding-agent skill that finds real Saudi customers, not translated ones

**Arabic-first search · Saudi identity verification · Verified links · Product intelligence**

</div>

---

Most "Saudi market research" is English research with a flag on it. You search
`best app in Saudi Arabia`, get expat threads and SEO listicles, and ship a report about
a market you never actually looked at.

This skill turns a product URL or idea into a shortlist of **verified Saudi** potential
first customers, sourced from public signals on X, Reddit, and LinkedIn — each one
carrying the person's own words in Arabic, a link you can open, and an explicit statement
of how their Saudi identity was established.

It never sends outreach.

## What makes it different

**It searches in Saudi dialect.** Real demand is written `أبغى تطبيق يسوي كذا` and
`تعبت من...` and `قهر`. It is not written "looking for a tool that". The skill ships a
lexicon of Saudi demand, pain, workaround, switching, and trigger vocabulary — with the
spelling variants Saudis actually type.

**It proves the person is Saudi.** Every candidate passes a dialect + location + civic
context check. Egyptian, Levantine, Iraqi, and other-Gulf markers are disqualifying.
Every rejection is logged with a neutral reason, and the log ships in the report — because
a filter you cannot see is a filter that never ran.

**It verifies every link.** Sources are re-opened and re-read before the report is
written. If a post was deleted or the quote is not on the page, the prospect is dropped
and the drop count is published.

**It extracts product intelligence.** Beyond names: feature gaps ranked by signal count,
the exact Arabic vocabulary for your landing page, a map of where demand concentrates,
and the trust objections that will kill your conversion — all quoted.

## Install

Clone, then run the installer. Node 16+ is the only requirement, and it works the same
on macOS, Linux, and Windows.

```bash
git clone https://github.com/abdullah7041/saudi-first-customer-finder.git
cd saudi-first-customer-finder
node scripts/install.js
```

That installs to `~/.claude/skills/saudi-first-customer-finder`. Other targets:

```bash
node scripts/install.js --agent codex             # ~/.codex/skills
node scripts/install.js --agent agents            # ~/.agents/skills (Codex, Copilot CLI, Gemini CLI)
node scripts/install.js --agent both              # claude + codex
node scripts/install.js --skills-dir ./.claude/skills   # project-local
node scripts/install.js --link                    # link the checkout instead of copying
```

`--link` is for editing the skill: the installed path points back at your clone, so
changes take effect on the next agent restart with no reinstall. On Windows it creates a
directory junction, which needs no administrator rights.

**Restart your agent afterwards.** Skills are read at startup; the skill will not appear
in a session that was already running.

The generated HTML report needs **Python 3.10+** on your PATH. Everything else in the
skill is plain markdown.

> Not on npm yet — the `npx saudi-first-customer-finder-skill` route will work only once
> the package is published.

## Usage

Paste a link. That's the whole instruction.

```
Use $saudi-first-customer-finder on https://example.com
```

The skill reads the site itself — landing copy, pricing, features, the Arabic version if
there is one — infers the Saudi ICP, picks `deep` mode, and runs. It asks you nothing. It
states the brief it inferred before searching so you can correct it mid-run.

Validation instead of outreach:

```
Use $saudi-first-customer-finder in research-only mode for [URL]. I want the pain
patterns, feature gaps, Arabic vocabulary, and trust objections — no outreach drafts.
```

Saudi businesses:

```
Use $saudi-first-customer-finder in b2b mode for [URL]. Find Saudi companies with
public timing triggers and the decision roles associated with them.
```

## Modes

| Mode | Prospects | Min queries | Use for |
| --- | --- | --- | --- |
| `fit-check` | none | 3 | Pre-flight only — is this category even searchable |
| `quick` | 5 | 20 | Fast sanity check |
| `standard` | 10 | 35 | Balanced run |
| `deep` | 20+ | 60 | **Default.** Full dialect fan-out and pattern analysis |
| `research-only` | 20+ | 60 | Product validation, no outreach drafts |
| `b2b` | 12 | 40 | Saudi companies and business triggers |
| `consumer` | 20+ | 60 | Individuals only, X-weighted |

## What the report contains

1. Verdict — is there reachable Saudi demand, and where
2. At-a-glance dashboard — score distribution, platform mix, signal freshness
3. Saudi ICP — buyer, job, trigger, disqualifiers
4. Audit strip — candidates examined, rejected on identity, dropped at link verification
5. Top prospect
6. Prospect shortlist — Arabic verbatim, English translation, verified link, six-dimension score, identity tier
7. **Rejection log** — who was excluded and why
8. Repeated patterns
9. **Competitive landscape** — who already sells to this customer, how they take orders, what they charge
10. **Feature gaps** — build vs. message, ranked by count
11. **Arabic vocabulary table** — landing-page copy sourced from customers
12. **Channel map** — where demand concentrates and whether promotion is allowed there
13. **Trust objections** — quoted adoption blockers
14. Seven-day manual validation plan
15. Limits

## Scoring

Six weighted dimensions, 0–5 each:

| Dimension | Weight |
| --- | --- |
| Saudi authenticity | 20% |
| Pain strength | 20% |
| Product fit | 20% |
| Timing (12-month decay) | 15% |
| Reachability | 10% |
| Evidence quality | 15% |

Hard gates, applied before the total matters:

- `saudi_authenticity < 3` → excluded from the shortlist, logged as rejected
- `link_verified != true` → dropped entirely
- No Arabic verbatim on an Arabic source → not shippable

Below 55 does not make the primary shortlist.

## Data access

Two paths, both within platform rules:

- **Path A** — a logged-in browser session driven by the agent. Real X advanced search
  and real LinkedIn results. Used like a human would use them.
- **Path B** — public web search with `site:` operators. No credentials, shallower,
  and the report says so.

No login-wall bypassing, no paywall circumvention, no rate-limit evasion, no scraping
against a site's terms, no data brokers, no leaked datasets, no private groups, no
personal email or phone enrichment.

## Ethics

- Prospects are hypotheses from public signals — never confirmed buyers, never people who
  consented to contact.
- The skill drafts openers. It never sends, replies, follows, connects, comments, or
  writes to a CRM.
- Saudi-identity verification is a **market-scope filter** applied to public
  self-description. It is never a judgment about any person, and rejection reasons are
  recorded neutrally.
- No targeting or inference on tribe, sect, religion, health, financial hardship,
  political view, or nationality as a slur.
- Public professional information only. A person's title and public posts are evidence;
  their phone, email, and address are not, and are never collected.

## Repo layout

```
saudi-first-customer-finder-skill/
├── saudi-first-customer-finder/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── references/
│   │   ├── fit-check.md                     Pre-flight category screen
│   │   ├── arabic-query-lexicon.md          Saudi dialect search vocabulary
│   │   ├── saudi-identity-verification.md   Dialect markers and rejection rules
│   │   ├── platform-playbooks.md            X, Reddit, LinkedIn tactics
│   │   ├── research-framework.md            Scoring, gates, product intelligence
│   │   └── report-artifact.md               JSON schema
│   └── scripts/generate_report.py           Bilingual RTL HTML generator
├── scripts/install.js                          Cross-platform installer
├── package.json
├── LICENSE
└── README.md
```

## Credits

Rebuilt from the [first-customer-finder](https://github.com/Kappaemme-git/codex-first-customer-finder-skill)
skill by Francesco Mistero (MIT). The workflow spine and report-generator approach come
from that project; the Saudi lexicon, identity verification, platform playbooks, six-
dimension scoring, link-verification gate, and product-intelligence layer are new.

## License

MIT
