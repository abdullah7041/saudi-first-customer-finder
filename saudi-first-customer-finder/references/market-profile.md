# Market Profile — deriving the search vocabulary at runtime

**Translated queries find translated people.**

An English phrase rendered into the local language by an agent finds the population that
also writes translated English — bilingual professionals, agencies, content marketers,
diaspora accounts, and SEO farms. That population is usually not the market. The people
who have the problem describe it in the informal register they actually type in, which no
translation step will produce, because the translation is grammatical and their writing is
not.

So the vocabulary is not shipped with this skill. It is derived at the start of every run,
from real posts, for whatever market the product is aimed at. This file is that
derivation. It runs once per job, and it is finished before any prospecting query is spent.

## Budget: at most five queries

Five. Not five per output — five for the whole profile. Output 1 costs nothing: it is read
off the product site, not searched for.

The reason this fits in five is that **most of the work is reading the returned posts, not
issuing more queries.** One good result set feeds four of the six outputs at once. If you
find yourself on query eight, you have started the run instead of preparing it.

| Query | Primary target | Also harvested from the same results |
| --- | --- | --- |
| 1 | Local phrasing — explicit demand | Where the audience writes; scope markers |
| 2 | Local phrasing — pain | Scope markers; trust objections |
| 3 | Local phrasing — workaround | Incumbent ladder (DIY rung); scope markers |
| 4 | Local phrasing — switching / competitor | Incumbent ladder (free/official + informal rungs); trust objections |
| 5 | Local phrasing — timing trigger | Where the audience writes |

Nothing in the table is a rule about which query goes first. It is an accounting of where
each output's evidence comes from, so that a missing output is traceable to a query that
was never read properly rather than to a query that was never run.

The six outputs below are named exactly as the rest of the skill refers to them. Each
states **what to produce**, **where it comes from**, and **how to tell a good result from a
bad one**. The third element is not commentary. A method that says "identify the local
phrasing" without saying how you know you got it right produces confident garbage, and
this is the part that stops it.

---

## Market and language

**What to produce.** The market the product is being sold into, and the language or
languages its buyers write in. Both, separately — they are not the same fact, and a
market with two writing languages needs both recorded.

**Where it comes from.** The product site, not a search. Read the pricing page for the
currency, the footer for the legal entity and country, the language switcher for which
languages the founder already believes matter, and any "available in" or shipping copy.
Record the URL of the page each fact came from.

**How to tell a good result from a bad one.** Pass: every fact here cites the page it was
read from, and the languages named are the ones buyers *write* in, not the ones the site
is published in. Wrong answer: recording a market and a language as a bare pair and moving
on, with nothing to check against. A second wrong answer is smoothing over a gap — if the
site is published only in a language the market's buyers do not casually write in, that is
a finding about the founder's assumption and belongs in the report, not in the bin. If the
site names no market at all, say so and ask the user which market to run; do not guess one
from the currency alone.

---

## Local phrasing

**What to produce.** Real phrase forms, lifted verbatim from real posts, in five buckets:

1. **Explicit demand** — someone asking out loud for a product like this
2. **Pain** — someone describing the problem without naming a product
3. **Workaround** — someone describing how they do it manually today
4. **Switching / competitor** — someone leaving, cancelling, or complaining about a paid
   alternative
5. **Timing trigger** — a life or business event that makes the product relevant now

For each phrase form, record the form itself and the URL of the post it came from.

**Where it comes from.** Posts. Only posts. The construction pattern is:

```
[local first-person verb] + [category noun] + [local context word]
```

Fill the brackets **from real posts, never from a dictionary or a translation.** The
procedure is: search a form you believe is plausible, open the results, and take the
phrasing people actually used — including the phrasing you did not expect and would not
have written. The believed-plausible form is a door, not an answer. If a search returns
nothing, the correct move is a broader first-person verb, not a better translation.

Spelling and inflection variation is a general problem, not a feature of any one language.
Languages with case, gender, or agreement will not match a single query form. Languages
with informal contractions will not match their own dictionary form. Languages with
non-standard or transliterated orthography will not match any single spelling at all.
Definite articles, singular and plural, and formal versus informal registers each split the
corpus again. So: vary the forms deliberately, and **state which variants you used** in the
profile. An unstated variant set cannot be reviewed, and a single-form search silently
reports a market as quiet when it was only misspelled.

**How to tell a good result from a bad one.** Pass: every recorded phrase form traces to a
specific post URL, the forms come from more than one author, and at least two buckets have
forms you would not have produced by translating the product brief. Any form with no
source post gets deleted — no exceptions, because that form is a translation wearing a
disguise. Wrong answer: a clean, grammatical set of phrases that reads like the English
brief rendered into the target language; or every form traced to one prolific author; or
forms that appear only inside vendor ads, which is the phrasing sellers use to advertise,
not the phrasing buyers use to complain. This check produces the `Phrasing sourced` line of
the closing block: posts read, phrase forms recorded.

---

## Incumbent ladder

**What to produce.** Three rungs, named, for how the problem gets solved today without
this product:

1. **The free or official option** — a government or institutional service, a platform's
   own built-in feature, a free tier, a widely circulated free template or prompt
2. **The informal human service** — a person or small shop doing it by hand for a fee,
   usually taking orders through a messaging app rather than a website
3. **The DIY workaround** — the spreadsheet, the notes app, the copy-paste, the general
   AI assistant

**Where it comes from.** Mostly the workaround and switching query results, read for what
people say they already do and already pay. The free/official rung often has to be
confirmed by looking at the institution's own site once you have a name for it.

**Why three rungs and not a competitor list.** The ladder sets the **price anchor** the
product is compared against. A buyer does not compare your price to your nearest funded
competitor; they compare it to what they pay now, which is frequently zero or the cost of
one message to a person they trust. A report that misses a free official option recommends
a price the market will never pay.

**How to tell a good result from a bad one.** Pass: all three rungs are named, or a rung is
explicitly recorded as absent with the evidence for its absence. Wrong answer: all three
rungs are software products — that is a competitive set, not a ladder. The informal human
service is the rung that goes missing most often, because it does not advertise where
search engines look; its genuine absence in a market is itself a finding worth stating, and
so is its dominance.

---

## Where the audience writes

**What to produce.** One platform, named, with the reason it is the one — plus a note on
any platform where the audience clearly is but does not leave searchable text.

**Where it comes from.** The result sets you already have. Count where the qualifying
first-person posts actually landed.

**How to tell a good result from a bad one.** Pass: you can point to first-person posts in
the local language, on that platform, dated inside the run's freshness window, reached as
individual permalinks. Wrong answer: naming the platform with the largest user count in
that country. Reach is not the criterion — searchable first-person text is. A platform
where the whole audience lives but posts only video or ephemeral content produces no
evidence a report can cite, and naming it is how a run ends with zero prospects and no
explanation. Record it as a known blind spot instead, which is a finding, and pick the
platform that can be read.

---

## Scope markers

**What to produce.** The observable signals that a person is inside the target market
rather than adjacent to it, and their counterparts that indicate a neighbouring market.

**Permitted — what may be used:**

- Self-described location, in a bio or in post text
- Local civic and institutional references: government services, universities, employment
  and benefits platforms, banks, and similar systems specific to the market
- Currency used as a default, and local price conventions
- Timezone behaviour, as a weak supporting signal only
- Language variety: regional vocabulary, spelling conventions, and informal forms that
  distinguish one market's writing from a neighbour's
- Local platform use — services that exist only, or overwhelmingly, in that market

**Forbidden — never used, never inferred, never recorded:**

- Tribe or clan
- Ethnicity
- Religion or sect
- Health, including mental health and disability
- Financial hardship
- Political view or affiliation
- Nationality used as a slur, or any pejorative framing of origin

These are not stylistic preferences. Targeting on them is out of bounds for this skill
regardless of how visible the signal is, and a marker being publicly posted does not move
it into the permitted column.

**Where it comes from.** The result sets you already have, read for what distinguishes the
posts you kept from the posts you discarded. When two neighbouring markets share a language,
the distinguishing markers are usually civic and institutional rather than linguistic.

**How to tell a good result from a bad one.** Pass: at least three markers, each drawn
from a different category above, each one you saw in an actual post rather than assumed
from general knowledge — and every one of them checkable by a reader who opens the same
post. Wrong answer: a marker list that is really a demographic profile; markers so broad
they match the whole language rather than the market; or any entry from the forbidden list
appearing under a euphemism. Write every marker and every scope rejection neutrally and
factually. A scope filter states where someone writes from; it never states anything about
their worth or belonging.

---

## Trust objections

**What to produce.** The reasons someone in this market does not buy a product in this
category. Each with a count and a quote.

**Where it comes from.** Localized app-store reviews of the incumbents you named on the
ladder — first-person, dated, public, and available without a logged-in session — plus the
switching and pain result sets. Recurring themes across most markets and verticals, offered
as places to look rather than as answers:

- Price and subscription resentment
- Scam fatigue around paid digital services
- Doubt that a tool genuinely works in the local language rather than being a foreign tool
  with a translated interface
- Data privacy, especially around identity documents, salary, and personal files
- Payment friction — which cards, which local payment methods, whether local billing exists
- Preference for a human intermediary over software

**How to tell a good result from a bad one.** Pass: every objection carries a count of
independent signals and at least one quote with a source. Wrong answer: the list above
copied into the profile because it sounded right. **An objection you did not observe does
not go in.** An objection observed once is recorded as observed once, not promoted; and a
category where you found no objections at all is reported as that, which usually means you
looked at the wrong incumbents rather than that the market trusts freely.

---

## State the profile before searching

Say this to the user after the derivation and before any prospecting query. A wrong
derivation is cheap to correct now and expensive to correct after sixty queries have been
spent on the wrong vocabulary. Do not wait for approval unless a line is empty.

```
Market profile — [product]
Market / language:   [market] / [language(s)]
Phrasing sourced:    [N] real posts read; [M] phrase forms recorded
Incumbent ladder:    free/official: [x] · informal service: [y] · DIY: [z]
Audience writes on:  [platform] — [why this one]
Scope markers:       [marker], [marker], [marker]
Trust objections:    [objection], [objection]
```

Each line is the receipt for the check in its section, not a summary of it. A line that
cannot be filled from evidence is left visibly empty and named as a gap — never filled with
a plausible guess, because a guessed line reads identically to a derived one and there is
no later step that can tell them apart.

A fully worked profile for one specific market is in `examples/saudi.md`, kept as a worked
example rather than as data to reuse.
