# Saudi Identity Verification

The single biggest failure mode of Saudi-market research is a shortlist full of people
who are not in the Saudi market. Expat threads, Gulf-wide accounts, and Arabic content
farms dominate the easy search results. This file is the filter.

## What this is and is not

This is a **market-scope filter** applied to what people have chosen to publish about
themselves. It exists so a report about Saudi demand is actually about Saudi demand.

It is **not** a judgment about any person, and it is not a nationality check in the legal
sense. Never use it to make claims about someone's worth, rights, or belonging. Write
every rejection reason neutrally and factually: "Egyptian dialect markers, no KSA
context" — never anything pejorative. Do not attempt to identify tribe, sect, region as
ethnicity, or immigration status.

## Verification tiers

| Tier | Requirement | Shortlist eligible |
| --- | --- | --- |
| **Confirmed Saudi** | 2+ independent Saudi signals, 0 contradictions | Yes |
| **Likely Saudi** | 1 strong Saudi signal, 0 contradictions | Yes, labelled |
| **Unverified** | ICP match but no identity signal | No — log only |
| **Rejected** | Any disqualifying marker | No — log with reason |

Independent means from different categories below. Two city mentions are one signal, not
two. Dialect + stated location is two.

## Signal category A — Dialect markers (strong)

These are Najdi/Hijazi/Saudi-general forms. Presence of several is near-conclusive.

**Core Saudi markers:**

| Marker | Meaning | Notes |
| --- | --- | --- |
| وش | what | Saudi/Gulf hallmark. `وش رايكم`, `وش السالفة` |
| أبغى / ابغى / أبي | I want | Najdi. Very strong |
| كذا | like this | Saudi. Egyptian equivalent is `كده` |
| مره / مرة | very | `حلو مره`. Saudi intensifier |
| زين | good | Najdi |
| طيب | ok/well | Shared but common |
| يبيله / تبيله | it needs | Najdi construction |
| السالفة | the story/matter | Strongly Saudi |
| عطني | give me | Saudi |
| ترى | actually/you know | Very common Saudi discourse particle |
| ما هوب / مو | not | Saudi negation. Egyptian uses `مش` |
| قاعد أسوي | I'm doing | Saudi progressive |
| خلاص | enough/done | Shared |
| يا رجال / يا شباب | address forms | Saudi |
| أجل | so then | Najdi |
| عشان / علشان | because | Weak — shared with Egyptian |

**Hijazi-specific** (Jeddah, Makkah, Madinah, Taif):

`إيش` · `دحين` · `كده` (Hijazi overlaps Egyptian here — needs a second signal) ·
`أبغى` · `عاد` · `يعني إيه`

**Eastern Province:** overlaps Bahraini and Kuwaiti forms. Requires a second,
non-dialect signal.

## Signal category B — Stated location and context (strong)

- KSA location in bio, profile, or post text
- Saudi city named as *home*, not as a destination: الرياض، جدة، الدمام، الخبر، مكة،
  المدينة، الطائف، أبها، خميس مشيط، تبوك، بريدة، عنيزة، حائل، جازان، نجران، الجبيل،
  ينبع، الأحساء، الهفوف، القطيف، الباحة، سكاكا، عرعر
- Saudi neighbourhood or landmark: العليا، الملقا، حطين، النرجس، الروضة، طريق الملك
  فهد، بوليفارد، الدرعية، كورنيش جدة، أبراج البيت
- Saudi phone format mentioned in public text (`05...`) — note it, never store or
  contact it
- Saudi flag emoji in profile combined with Arabic content
- KSA timezone behaviour (posting patterns during Saudi working hours) — weak, supporting
  only

## Signal category C — Institutional and civic context (strong)

Mentions of Saudi-only systems are very hard to fake and rarely appear in non-KSA
content:

**Government platforms:** أبشر · توكلنا · ناجز · قوى · جدارات · طاقات · مساند ·
التأمينات الاجتماعية · نافذ · مقيم · اعتماد · صحتي · نفاذ

**Education:** جامعة الملك سعود · جامعة الملك عبدالعزيز · KFUPM · KAUST · جامعة الإمام ·
جامعة الملك فيصل · جامعة الأميرة نورة · الابتعاث · قياس · تحصيلي · قدرات · نافس

**Employment/economy:** السعودة · نطاقات · حافز · هدف · منشآت · مسك · رؤية 2030 ·
نيوم · روشن · القدية · البحر الأحمر

**Banking/payments:** مدى · سداد · أبشر أعمال · الراجحي · الأهلي · stc pay · تمارا · تابي

**Cultural/temporal:** اليوم الوطني السعودي · يوم التأسيس · موسم الرياض · Hijri dates
used naturally · ريال / SAR as default currency

## Disqualifying markers — automatic rejection

### Egyptian dialect

`ازاي` · `عايز` · `عاوز` · `دلوقتي` · `كده` (alone, without Saudi markers) · `مش` ·
`بتاع` · `أوي` · `خالص` · `ايوة` · `فين` · `ليه كده` · `يلا بينا` · `جامد`

The `مش` vs `مو/ما` split is the cleanest single discriminator between Egyptian and
Saudi writing.

### Levantine (Syria, Lebanon, Jordan, Palestine)

`شو` · `بدي` · `هيك` · `هلق` · `كتير` · `منيح` · `عم بعمل` · `ليش هيك` · `تمام يعني`

### Iraqi

`شلون` (also Kuwaiti) · `هواي` · `جذي` · `زين هيه` · `اكو` / `ماكو`

### Other Gulf — reject for Saudi-only scope, log as adjacent market

- **Kuwaiti:** `شلون` · `جذي` · `الديرة` · KWD · Kuwaiti institutions
- **Emirati:** `شحالك` · `وايد` (caution: also Eastern Province) · AED · Dubai/Abu Dhabi
  as home · UAE platforms (ICP, DEWA, Salik)
- **Qatari:** QAR · Doha as home · Hukoomi
- **Bahraini:** BHD · Manama as home · overlaps Eastern Province heavily — needs care
- **Omani:** OMR · Muscat as home

### Non-Saudi context in KSA

These indicate a resident expat rather than a Saudi national. Under `Saudi nationals
only` scope they are rejected; under a wider scope they go into an adjacent tier:

- Iqama / اقامة referenced as one's own status
- "transferable iqama", "sponsor", "kafeel", "exit re-entry", "final exit"
- Expat-focused communities as the person's primary context (r/RiyadhExpats and similar)
- Discussion of home-country remittance, home-country degree equivalency (معادلة الشهادة)
  as a personal obstacle
- Explicit self-description as a non-Saudi national

Handle these neutrally. They are a different market segment, not a lesser one — and for
many products they are a legitimate secondary ICP the user may want to target later.
Always log them rather than deleting them.

### Non-human and commercial accounts

Reject outright, do not log as prospects:

- Brand, agency, recruiter, and reseller accounts
- Content farms and SEO blogs
- News outlets and aggregators
- Obvious bots: repetitive posting, engagement-bait, follower-farm patterns
- Accounts whose entire feed is promotional

## Contradiction handling

A contradiction outranks a positive signal. Examples:

- Saudi city mentioned but consistent Egyptian dialect → rejected, `visiting or resident
  non-Saudi`
- Arabic content but bio lists a non-KSA country → rejected unless a strong civic marker
  overrides
- Uses `أبغى` once but `مش` and `عايز` throughout → rejected

When signals genuinely conflict and neither dominates, the tier is **Unverified**, not
Likely. Unverified never enters the shortlist.

## Recording the verdict

For every candidate examined, record:

```json
{
  "handle_or_name": "public display name only",
  "platform": "X | Reddit | LinkedIn",
  "tier": "confirmed | likely | unverified | rejected",
  "markers": ["dialect: أبغى، وش، مره", "context: mentions جدارات", "location: الرياض in bio"],
  "contradictions": [],
  "reason": "Required for rejected and unverified"
}
```

Confirmed and likely go to `prospects`. Unverified and rejected go to `rejected` in the
report JSON. Publishing the rejection log is what makes the shortlist credible — it shows
the filter ran and what it cost.

## Practical guidance

- Read the account's recent posts, not just the one that matched the query. One post is
  not a dialect sample.
- A retweet or quote is not the person's own words. Verify the marker comes from text
  they wrote.
- Bios lie less often than you'd expect, but empty bios are the norm. Absence of a
  location is not a contradiction — it just means you need dialect or context.
- If the whole shortlist ends up `likely` rather than `confirmed`, say so in the limits
  section. That is a real weakness in the evidence, not a detail to bury.
- If Saudi signals are genuinely absent across the entire search, the honest finding is
  that the Saudi demand for this product is not publicly visible yet. Report that.
