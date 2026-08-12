# Platform Playbooks

Each platform surfaces a different slice of the Saudi market and lies about the others.
Use all three, weight them by what they are actually good for, and never let one
platform's population stand in for the market.

| Platform | Best for | Saudi-national density | Main risk |
| --- | --- | --- | --- |
| X | Consumer pain, dialect, live complaints | **Very high** | Noise, bots, promo spam |
| Reddit | Long-form written pain, detail | **Low** — expat-skewed | Mistaking expats for the market |
| LinkedIn | Professional/B2B pain, company triggers | Medium-high | Performative posting, no real complaints |

## Access paths

Two paths, in order of preference:

**Path A — logged-in browser session.** If the agent has browser control with the user's
existing sessions (a browser-automation tool, extension, or equivalent), use it. This is
the only way to get real X advanced search and real LinkedIn results. Operate the site
normally, as a human would: no bulk scraping, no rate-limit evasion, no automated
messaging.

**Path B — public web search fallback.** No login. Use general web search with `site:`
operators. Shallower and biased toward older, indexed content, but works everywhere and
requires no credentials.

Always state which path was used in the report's search scope. A Path B report is a
weaker report and should say so.

**Never** bypass a login wall, defeat a paywall, evade rate limits, or ignore
`robots.txt`. If a platform will not show something publicly, it does not go in the
report.

---

## X (Twitter)

The most important source for Saudi consumer signals. Saudis complain publicly, in
dialect, at volume, and X's Arabic search actually works.

### Search operators that matter

```
lang:ar                          Arabic only — essential
-filter:replies                  Original posts, not reply noise
filter:replies                   Flip it to mine conversation threads
-filter:links                    Excludes most promo and news spam
min_faves:5                      Signals the complaint resonated
min_retweets:2                   Stronger resonance filter
since:2025-08-01 until:2026-08-01  Date window
-filter:verified                 Optional: cuts brand/blue-check promo
from:handle / to:handle          Follow a specific conversation
```

Geocode restricts to a radius around a point — the most reliable location filter X has:

```
geocode:24.7136,46.6753,50km     Riyadh
geocode:21.4858,39.1925,50km     Jeddah
geocode:26.4207,50.0888,50km     Dammam / Khobar / Dhahran
geocode:21.3891,39.8579,30km     Makkah
geocode:24.5247,39.5692,30km     Madinah
geocode:18.2465,42.5117,40km     Abha / Khamis Mushait
geocode:26.3260,43.9750,40km     Buraydah / Qassim
geocode:28.3838,36.5550,40km     Tabuk
```

Geocode coverage is partial — most users disable location — so use it to *find* seeds,
never as the only filter. Absence of geocode data is not a contradiction.

### Query templates

```
"أبغى تطبيق" lang:ar -filter:replies since:2025-08-01
"تعبت من" [pain noun] lang:ar min_faves:3
"وش أفضل" [category] lang:ar -filter:links
"فيه أحد يعرف" [category] lang:ar
"ألغيت الاشتراك" lang:ar
[category] "قهر" lang:ar
[category] geocode:24.7136,46.6753,50km lang:ar
```

Search URL form (works in a browser session):

```
https://x.com/search?q=<url-encoded query>&f=live      Latest
https://x.com/search?q=<url-encoded query>&f=top       Top
```

`f=live` is usually what you want — recency beats engagement for demand signals.

### Working the results

1. Run the query on `f=live`, scroll a meaningful number of results, not just the first
   screen.
2. Open promising posts individually. **The replies are often better than the post** —
   Saudi X threads accumulate "same here" and "I use X instead" responses that are
   themselves qualified prospects and competitor intel.
3. Check the author's recent timeline for dialect confirmation before qualifying.
4. Record: post URL, handle, display name, exact Arabic text, date, engagement counts.

### Hashtags worth seeding from

General: `#السعودية` `#الرياض` `#جدة` `#وظائف_السعودية` `#السوق_المفتوح`
Category hashtags exist for most verticals — find them by looking at what your seed
posts actually tag, rather than guessing.

Hashtag-only search returns mostly promotional accounts. Always pair a hashtag with a
first-person pain or demand verb.

### Traps

- Engagement-bait accounts recycle complaints for reach. Check whether the account has a
  normal, varied timeline.
- Promotional threads disguised as complaints ("I was struggling until I found...") are
  ads. Reject.
- Retweets are not the retweeter's own pain.
- Arabic content farms repost the same complaint text across dozens of accounts. If the
  exact phrasing appears more than twice, it is syndicated, not organic.

---

## Reddit

Useful for detailed, structured pain — and structurally misleading about who the Saudi
market is.

### The expat-skew problem

The English-language KSA subreddits are dominated by expatriate residents. This is not a
flaw in Reddit; it reflects who uses Reddit in Arabic-speaking countries. Reddit
penetration among Saudi nationals is low compared to X.

Practical consequence: **a Reddit-heavy shortlist is probably not a Saudi-national
shortlist.** Run identity verification on every Reddit candidate and expect a high
rejection rate. If Reddit supplies most of the shortlist, say so explicitly in the limits
section.

### Subreddits

| Subreddit | Character |
| --- | --- |
| r/saudiarabia | Mixed nationals and expats. The best single source |
| r/Riyadh | Mixed, moderate volume |
| r/Jeddah | Smaller, mixed |
| r/saudi | Smaller, more national-leaning |
| r/RiyadhExpats | **Expat by definition.** Log, do not shortlist under Saudi-only scope |
| r/arabs | Pan-Arab. Heavy dialect mixing — verification essential |
| r/AskMiddleEast | Pan-regional, low Saudi density |
| Category subs (r/personalfinance, r/EngineeringResumes, etc.) | Pain-rich, nationality-blind — verification essential |

### Search

Reddit's own search, run in a browser or via public web search:

```
https://www.reddit.com/r/saudiarabia/search/?q=<query>&restrict_sr=1&sort=new&t=year
https://www.reddit.com/search/?q=<query>&sort=new&t=year
```

Public web-search fallback:

```
site:reddit.com/r/saudiarabia [pain phrase]
site:reddit.com "in Riyadh" [category]
site:reddit.com "Saudi" [category] "any recommendations"
```

Arabic queries on Reddit return far less than on X, but run them anyway — the ones that
do hit are high-quality, since an Arabic Reddit post in a KSA sub is usually a national.

### Working the results

- Sort by `new` for timing, `top` + `t=year` for pattern discovery.
- Read the comment tree. In resume, finance, and service-provider threads the comments
  carry the competitive landscape.
- Deleted accounts and removed posts fail link verification. Drop them.

---

## LinkedIn

The professional layer. Essential for `b2b` mode and for any product sold to working
professionals. Saudi LinkedIn is unusually active — Vision 2030 professional culture
made it the default career network.

### What it is good for

- Public complaints about professional workflows (softer than X, but real)
- Company timing triggers: hiring posts, expansion, funding, new programmes, office
  openings
- Identifying decision roles by title
- Saudization and localization discussions that reveal market constraints

### What it is bad for

- Raw emotional pain. People perform competence on LinkedIn. `قهر` does not appear there.
- Anonymous honesty. Use X for that and LinkedIn for the professional framing of the same
  problem.

### Search

With a session (Path A): use LinkedIn's own search, filter Content, set date range, and
filter by location = Saudi Arabia. Search both Arabic and English terms.

Without a session (Path B): public web search only.

```
site:linkedin.com/posts "السعودية" [pain phrase]
site:linkedin.com/posts "Saudi Arabia" [category] "struggling"
site:linkedin.com/jobs [role] "Riyadh"          → hiring triggers
site:linkedin.com/company [sector] "Saudi"      → company context
```

Public post URLs have the form `linkedin.com/posts/<slug>-activity-<id>` and are
readable without login when the author posted publicly. Those are the ones you can cite.

### Rules

- Public professional information only. No connection requests, no InMail, no scraping
  of contact details, no third-party enrichment tools.
- A person's employer, title, and public posts are fair evidence. Their email, phone,
  and personal address are not — do not collect them even if visible.
- Comments on a public post are public evidence and are often the richest signal on the
  platform.

---

## Cross-platform discipline

1. **Deduplicate people across platforms.** The same person may appear on X and LinkedIn.
   Merge into one prospect and note both sources — that is stronger evidence, not two
   prospects.
2. **Balance the shortlist.** A shortlist that is 90% one platform is a report about that
   platform. If one platform dominates, either search the others harder or state the
   imbalance in the limits.
3. **Record the platform mix** in the report's search scope: how many queries per
   platform, which access path, what date window.
4. **Note what you could not reach.** If LinkedIn search was unavailable without a
   session, that is a limitation the reader needs.

## Other Saudi sources worth checking

Not primary, but occasionally decisive:

- **App Store / Google Play reviews** of competing apps, filtered to the Saudi
  storefront and Arabic reviews. Extremely high-signal complaint data.
- **Public Saudi forums** where they still exist for a vertical.
- **Snapchat and TikTok** carry enormous Saudi audiences but very little searchable text.
  Treat as inaccessible for evidence purposes rather than pretending to have searched.
- **Public Telegram/WhatsApp groups** — do not use. Effectively private spaces.
