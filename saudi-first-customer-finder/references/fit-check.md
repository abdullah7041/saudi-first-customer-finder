# Pre-flight Fit Check

A full run is 60+ queries and a long stretch of work. Some categories cannot produce a
prospect shortlist no matter how well the run is executed — the demand is not written
down in public text, or targeting the people who have it would be wrong.

This check costs **three queries and about a minute**. Run it first, every time. It ends
with one of three verdicts, stated to the user before any real searching begins.

## Step 1 — Category screen, no searching required

Read the product brief against this table before spending a single query.

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
| Anything else sold to Saudi consumers or small businesses | **Proceed** | This is the skill's home ground |

**Prospecting off** does not mean stop. It means switch to `research-only`, skip the
prospect shortlist and the rejection log, and deliver the product-intelligence half:
vocabulary, trust objections, competitive landscape, and channel map. Those are built
from how people discuss the *category*, not from identifying individuals — which is both
safer and, for a sensitive product, usually the more useful half anyway.

Say plainly which rule was applied and why. Never silently downgrade the run.

## Step 2 — Three probe queries

One query per bucket, in Saudi Arabic, on X. Do not run more than three. Do not fix a
disappointing probe by adding a fourth — the point is a fast read, and a category that
needs six queries to show one signal is already telling you the answer.

1. **Demand probe** — dialect verb + category noun
   `("أبغى" OR "ابغى" OR "أبي") [category noun] lang:ar`
2. **Pain probe** — symptom phrase + domain noun
   `("تعبت من" OR "طفشت من" OR "قهر") [domain noun] lang:ar -filter:links`
3. **Workaround probe** — the manual method + domain
   `(بالاكسل OR "يدوي" OR "شات جي بي تي") [domain noun] lang:ar`

If the product has no obvious Arabic category noun, that is itself a signal — note it and
lean toward amber at best.

## Step 3 — Count three things

For each probe, count only what a full run would actually keep:

- **First-person Saudi hits** — someone describing their own situation, with at least one
  Saudi dialect or context marker, who is not selling anything
- **Vendor ratio** — share of results that are ads, service accounts, or content farms
- **Freshest hit** — age of the most recent qualifying result

Then apply:

| Verdict | Condition | Action |
| --- | --- | --- |
| **Green** | 6+ first-person Saudi hits across the three probes, and at least one under 30 days old | Run the full `deep` pass as designed |
| **Amber** | 2–5 hits, or every hit older than three months, or vendor ratio above 60% | Run `deep`, but say up front that the shortlist will be short. Consider widening the date window before widening the geography |
| **Red** | 0–1 hits, or vendor ratio above 80%, or all three probes return only ads and unrelated stemming noise | Do not run the full prospecting pass. Switch to `research-only` and explain the finding |

When the result sits between two bands, take the lower one. Optimism here costs the user
an hour.

### Counting the vendor ratio honestly

Arabic X has a large population of general-services accounts — essay mills, assignment
shops, design and translation sellers — that list dozens of deliverables in one post.
Any probe containing a deliverable noun (`سيرة ذاتية`, `عرض تقديمي`, `قالب`, `تقرير`)
will pull them in bulk, and a probe can easily return 100% of them.

They count fully toward the vendor ratio. Do not discount them as noise: a category
where sellers outnumber sufferers this heavily is telling you something real about how
the demand gets met. Route them to the competitive landscape and let the ratio push the
verdict down.

`قالب` on its own is the worst offender. Prefer `أسويها يدوي`, `بالاكسل`, or
`سويتها بالشات جي بي تي` as workaround probes — those describe an action rather than a
product, which is what separates a person from a shop.

### Field test

Run against an Arabic-first Saudi CV product on 2026-08-05, the check returned:

```
Probes:          demand 1 · pain 2 · workaround 0 first-person Saudi hits
Vendor ratio:    ~75% overall, 100% on the workaround probe
Freshest signal: 8 days
Verdict:         AMBER — running deep, expect a short list
```

A full 60-query pass on the same product, run separately, produced exactly that: one
strong prospect, a wall of WhatsApp CV services, and a free circulating ChatGPT prompt
as the real incumbent. The check reached the same conclusion in three queries. That is
the entire point of it.

## Step 4 — State the verdict before proceeding

Report it in this shape, in six lines or fewer, then continue without waiting for
permission unless the verdict is red:

```
Fit check — [product], Saudi market
Category screen:  proceed | prospecting off ([rule])
Probes:           demand N · pain N · workaround N first-person Saudi hits
Vendor ratio:     N%
Freshest signal:  N days
Verdict:          GREEN — running deep | AMBER — running deep, expect a short list | RED — switching to research-only
```

On red, stop and hand the user the choice: research-only now, a different Arabic framing
of the category, or a widened scope. Do not burn an hour proving a red verdict right.

## What red does not mean

Red means the demand is **not visible in public Arabic text on X, Reddit, or LinkedIn**.
It does not mean there is no market. Common innocent explanations:

- The audience lives on Snapchat or TikTok, where there is no searchable text
- The problem is embarrassing, private, or discussed only in closed groups
- The category is too new to have a name people type
- The pain is real but low-salience — annoying enough to tolerate, not to post about
- The Arabic framing used in the probes is wrong

Say which of these you think it is. "No public signal" plus a plausible reason is a
finding the user can act on. "No prospects found" with no explanation is a failed run.

## Cost discipline

The fit check is three queries. If it starts turning into ten, it has stopped being a
check and become the run. Stop, take the lower verdict, and move on.
