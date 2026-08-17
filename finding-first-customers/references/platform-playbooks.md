# Platform Playbooks

Each platform surfaces a different slice of a market and lies about the others. The
platform ranking itself is not this file's job — it comes from the market profile's
**where the audience writes** output (`references/market-profile.md`). This file
describes how to work each platform once one has been chosen: never let one platform's
population stand in for the market.

The three platforms below — a fast consumer network, a long-form discussion platform, and
a professional network — are worked examples of the shape most markets fall into. If the
profile names a different platform, apply the same discipline (operators that matter,
access paths, cross-platform hygiene) to that platform instead.

| Platform | Best for | Main risk |
| --- | --- | --- |
| Fast consumer network (e.g. X) | Consumer pain, dialect, live complaints | Noise, bots, promo spam |
| Long-form discussion platform (e.g. Reddit) | Long-form written pain, detail | Mistaking expatriate/diaspora voices for the market |
| Professional network (e.g. LinkedIn) | Professional/B2B pain, company triggers | Performative posting, no real complaints |

## Access paths

Two paths, in order of preference:

**Path A — logged-in browser session.** If the agent has browser control with the user's
existing sessions (a browser-automation tool, extension, or equivalent), use it. This is
the only way to get real advanced search and real results on platforms that gate search
behind a session. Operate the site normally, as a human would: no bulk scraping, no
rate-limit evasion, no automated messaging.

**Path B — public web search fallback.** No login. Use general web search with `site:`
operators. Shallower and biased toward older, indexed content, but works everywhere and
requires no credentials.

Always state which path was used in the report's search scope. A Path B report is a
weaker report and should say so.

**Never** bypass a login wall, defeat a paywall, evade rate limits, or ignore
`robots.txt`. If a platform will not show something publicly, it does not go in the
report.

---

## Fast consumer network (X-shaped platforms)

Often the most important source for consumer signals: people complain publicly, in
dialect, at volume, and search on these platforms often actually works on the local
language.

### Search operators that matter

```
<language filter, if the platform has one>       Local-language only — essential
-filter:replies                  Original posts, not reply noise
filter:replies                   Flip it to mine conversation threads
-filter:links                    Excludes most promo and news spam
min_faves:5                      Signals the complaint resonated
min_retweets:2                   Stronger resonance filter
since:<date> until:<date>        Date window
-filter:verified                 Optional: cuts brand/blue-check promo
from:handle / to:handle          Follow a specific conversation
```

Geocode restricts to a radius around a point — the most reliable location filter these
platforms tend to have. Get coordinates for the market's main population centers and use
them to *find* seeds, never as the only filter — coverage is always partial, since most
users disable location, and absence of geocode data is not a contradiction.

```
geocode:<lat>,<long>,<radius>km  <population centre>
```

A worked coordinate table for one specific market is in `examples/saudi.md`.

### Query templates

```
"<demand phrase>" <language filter> -filter:replies since:<date>
"<pain phrase>" [pain noun] <language filter> min_faves:3
"<comparison phrase>" [category] <language filter> -filter:links
"<discovery phrase>" [category] <language filter>
"<cancellation phrase>" <language filter>
[category] "<strong pain word>" <language filter>
[category] geocode:<lat>,<long>,<radius>km <language filter>
```

Search URL form (works in a browser session):

```
https://<platform>/search?q=<url-encoded query>&f=live      Latest
https://<platform>/search?q=<url-encoded query>&f=top       Top
```

Latest/recency is usually what you want — recency beats engagement for demand signals.

### Working the results

1. Run the query on the "latest" sort, scroll a meaningful number of results, not just
   the first screen.
2. Open promising posts individually. **The replies are often better than the post** —
   threads accumulate "same here" and "I use X instead" responses that are themselves
   qualified prospects and competitor intel.
3. Check the author's recent timeline for language-variety confirmation before qualifying.
4. Record: post URL, handle, display name, exact source-language text, date, engagement
   counts.

### Hashtags worth seeding from

Category hashtags exist for most verticals — find them by looking at what your seed posts
actually tag, rather than guessing. A worked hashtag list for one specific market is in
`examples/saudi.md`.

Hashtag-only search returns mostly promotional accounts. Always pair a hashtag with a
first-person pain or demand verb.

### Traps

- Engagement-bait accounts recycle complaints for reach. Check whether the account has a
  normal, varied timeline.
- Promotional threads disguised as complaints ("I was struggling until I found...") are
  ads. Reject.
- Retweets are not the retweeter's own pain.
- Content farms repost the same complaint text across dozens of accounts. If the exact
  phrasing appears more than twice, it is syndicated, not organic.

---

## Long-form discussion platform (Reddit-shaped platforms)

Useful for detailed, structured pain — and structurally misleading about who the market
actually is.

### The expatriate/diaspora-skew problem

Expatriate-heavy and diaspora communities exist on every platform, not just one, and this
is where they tend to concentrate hardest. This is not a flaw in the platform; it reflects
who uses it in a given region. Local-national penetration is frequently low compared to
faster consumer platforms.

Practical consequence: **a shortlist dominated by this platform is probably not an
in-market shortlist.** Run scope verification on every candidate from here and expect a
high rejection rate. If this platform supplies most of the shortlist, say so explicitly in
the limits section.

### Finding the right communities

Most markets have a mix of general regional communities (mixed nationals and expats),
national-leaning communities (smaller, more in-market), explicitly expat communities (log,
do not shortlist under an in-market-only scope), and category-specific communities
(pain-rich, nationality-blind — verification essential for every one of them). A worked
community table for one specific market is in `examples/saudi.md`.

### Search

The platform's own search, run in a browser or via public web search:

```
https://<platform>/r/<community>/search/?q=<query>&restrict_sr=1&sort=new&t=year
https://<platform>/search/?q=<query>&sort=new&t=year
```

Public web-search fallback:

```
site:<platform> [pain phrase]
site:<platform> "<in-market location>" [category]
site:<platform> "<market name>" [category] "any recommendations"
```

Local-language queries on these platforms typically return far less than on the fast
consumer network, but run them anyway — the ones that do hit are high-quality, since a
local-language post here is usually a genuine in-market author.

### Working the results

- Sort by `new` for timing, `top` + a year window for pattern discovery.
- Read the comment tree. In resume, finance, and service-provider threads the comments
  carry the competitive landscape.
- Deleted accounts and removed posts fail link verification. Drop them.

---

## Professional network (LinkedIn-shaped platforms)

The professional layer. Essential for `b2b` mode and for any product sold to working
professionals. Activity level varies a lot by market — some markets have unusually active
professional-network cultures driven by local policy or economic programmes.

### What it is good for

- Public complaints about professional workflows (softer than consumer platforms, but
  real)
- Company timing triggers: hiring posts, expansion, funding, new programmes, office
  openings
- Identifying decision roles by title
- Local workforce-policy and localization discussions that reveal market constraints

### What it is bad for

- Raw emotional pain. People perform competence here. The strongest dialect pain markers
  rarely appear.
- Anonymous honesty. Use the fast consumer network for that and this platform for the
  professional framing of the same problem.

### Search

With a session (Path A): use the platform's own search, filter to content, set a date
range, and filter by location = target market. Search both local-language and English
terms.

Without a session (Path B): public web search only.

```
site:linkedin.com/posts "<market name>" [pain phrase]
site:linkedin.com/posts "<market name>" [category] "struggling"
site:linkedin.com/jobs [role] "<population centre>"          → hiring triggers
site:linkedin.com/company [sector] "<market name>"            → company context
```

Public post URLs have the form `linkedin.com/posts/<slug>-activity-<id>` and are readable
without login when the author posted publicly. Those are the ones you can cite.

### Rules

- Public professional information only. No connection requests, no InMail, no scraping of
  contact details, no third-party enrichment tools.
- A person's employer, title, and public posts are fair evidence. Their email, phone, and
  personal address are not — do not collect them even if visible.
- Comments on a public post are public evidence and are often the richest signal on the
  platform.

---

## Cross-platform discipline

1. **Deduplicate people across platforms.** The same person may appear on more than one
   platform. Merge into one prospect and note both sources — that is stronger evidence,
   not two prospects.
2. **Balance the shortlist.** A shortlist that is 90% one platform is a report about that
   platform. If one platform dominates, either search the others harder or state the
   imbalance in the limits.
3. **Record the platform mix** in the report's search scope: how many queries per
   platform, which access path, what date window.
4. **Note what you could not reach.** If a platform's search was unavailable without a
   session, that is a limitation the reader needs.

## Other sources worth checking

Not primary, but occasionally decisive:

- **App Store / Google Play reviews** of competing apps, filtered to the market's
  storefront and language. Extremely high-signal complaint data.
- **Public forums** where they still exist for a vertical, in the market's language.
- Some platforms carry enormous audiences in a given market but very little searchable
  text (ephemeral or video-first platforms are common examples). Treat these as
  inaccessible for evidence purposes rather than pretending to have searched.
- **Private groups and chats** — do not use. Effectively private spaces.
