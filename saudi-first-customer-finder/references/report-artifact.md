# Report Artifact

Build the JSON, then run the bundled generator. Do not hand-write report markup.

## Generate

```bash
python3 scripts/generate_report.py analysis.json outputs/saudi-first-customer-report.html
```

Keep `analysis.json` in a working or temporary directory unless the user asks for the raw
data. Return a clickable absolute file link.

## Verify after generating

Open the HTML and confirm:

- Arabic quote blocks render right-to-left, not reversed or mirrored
- every prospect card has a working source link
- the rejection log has entries — an empty one means the identity filter never ran
- the product intelligence section is populated with counts and quotes
- no score is a placeholder or a round default

## JSON schema

```json
{
  "title": "Saudi First Customer Signals",
  "product": "Example product",
  "product_url": "https://example.com",
  "target_customer": "Saudi nationals aged 22-30 applying for private-sector roles",
  "mode": "deep",
  "search_scope": "X (28 Arabic queries, logged-in session), Reddit (19 queries, public), LinkedIn (14 queries, public web search). Window: 2025-08-01 to 2026-08-01.",
  "access_path": "Path A (browser session) for X and LinkedIn; public search for Reddit",
  "generated_at": "2026-08-02",
  "verdict": "Real Saudi demand concentrates on X among recent graduates who describe the problem as قهر and are already paying service offices to do it manually.",

  "icp": {
    "buyer": "Saudi national, 22-30, recent graduate or 1-3 years experience",
    "job": "Turn an existing CV into something that gets a reply",
    "trigger": "Graduated, or three months of silence after applying",
    "disqualifiers": ["Non-Saudi residents", "Senior executives using recruiters"]
  },

  "stats": {
    "candidates_examined": 84,
    "rejected_on_identity": 46,
    "dropped_at_link_verification": 5
  },

  "prospects": [
    {
      "name": "public handle or display name",
      "platform": "X",
      "type": "Public X prospect · recent graduate",
      "stage": "High intent",
      "score": 88,
      "scope_tier": "confirmed",
      "saudi_markers": ["dialect: أبغى، وش، مره", "context: mentions جدارات", "location: الرياض"],
      "quote_ar": "تعبت من كتابة السيرة الذاتية، كل مرة أعيدها ومحد يرد علي",
      "quote_en": "I'm exhausted from writing my CV — I redo it every time and nobody replies.",
      "pain_signal": "Repeatedly rewriting a CV with no responses over several months.",
      "why_fit": "The product compares a CV against one target vacancy and shows what is unproven.",
      "why_now": "Posted 9 days before research; actively applying.",
      "suggested_channel": "Public reply on the same X thread",
      "caution": "Do not imply the product can overcome hiring constraints it cannot affect.",
      "opener_ar": "شفت تغريدتك عن السيرة الذاتية...",
      "opener_note": "Unsent draft. Top-3 prospects only. Omitted in research-only mode.",
      "evidence": "The post names the field, the duration of the search, and the rewriting workflow.",
      "source_title": "Post title or first line",
      "source_url": "https://x.com/example/status/123",
      "source_type": "Public X post",
      "signal_date": "2026-07-24",
      "link_verified": true,
      "verified_at": "2026-08-02",
      "dimensions": {
        "scope_match": 5,
        "pain_strength": 5,
        "product_fit": 4,
        "timing": 5,
        "reachability": 4,
        "evidence_quality": 5
      }
    }
  ],

  "rejected": [
    {
      "platform": "Reddit",
      "tier": "rejected",
      "reason": "Egyptian dialect markers (عايز، مش، ازاي) with no KSA context signal",
      "note": "Pain signal is real and counted in product intelligence, but out of Saudi scope."
    }
  ],

  "patterns": [
    {
      "title": "The workaround is already paid",
      "count": 7,
      "insight": "Multiple prospects pay a service office rather than use software, which sets a real price anchor.",
      "quote_ar": "رحت مكتب خدمات وسويتها بمئة ريال"
    }
  ],

  "product_intelligence": {
    "feature_gaps": [
      {
        "title": "Arabic-language output, not just an Arabic interface",
        "count": 6,
        "insight": "Users assume any AI tool produces awkward translated Arabic and want proof otherwise.",
        "quote_ar": "كل البرامج تطلع عربي مترجم ومايناسب",
        "type": "build"
      }
    ],
    "vocabulary": [
      {
        "term_ar": "سيرة ذاتية",
        "meaning_en": "CV / resume",
        "count": 31,
        "use": "Category term — use in headline"
      },
      {
        "term_ar": "محد يرد علي",
        "meaning_en": "nobody replies to me",
        "count": 14,
        "use": "Problem term — use as the hook, not 'optimize your resume'"
      }
    ],
    "channels": [
      {
        "name": "#وظائف_السعودية",
        "platform": "X",
        "why": "Continuous stream of first-person job-search frustration",
        "activity": "High, daily",
        "rules": "Open hashtag; promotional replies tolerated if useful"
      }
    ],
    "objections": [
      {
        "title": "Scam fatigue around paid CV services",
        "count": 5,
        "insight": "Prior bad experiences with paid ATS 'experts' make claims of guaranteed results actively harmful.",
        "quote_ar": "كلهم نصب، دفعت ومحصلت شي"
      }
    ],
    "competitors": [
      {
        "name": "@example_cv_service",
        "platform": "X",
        "kind": "Human service",
        "threat": "high",
        "offer": "Writes an ATS-compatible CV to order, posts several times a day.",
        "order_channel": "WhatsApp number in the post",
        "price": "Not stated publicly",
        "quote_ar": "نجهز لك سيرة ذاتية احترافية ومتوافقة مع نظام ATS",
        "source_url": "https://x.com/example/status/123"
      },
      {
        "name": "Circulating ChatGPT prompt",
        "platform": "X",
        "kind": "Free workaround",
        "threat": "high",
        "offer": "A copy-paste Arabic prompt that tailors a CV to a job description with ATS keywords.",
        "order_channel": "Reshared as social content",
        "price": "Free",
        "quote_ar": "عدّل سيرتي الذاتية [الصقها هنا] خصيصًا لهذي الوظيفة",
        "source_url": "https://x.com/example/status/456"
      }
    ]
  },

  "plan": {
    "angle": "Validate the pain with a free manual review before proposing software.",
    "first_step": "Days 1-2: re-check the three freshest sources and community rules. Reply publicly to at most one active thread per platform.",
    "follow_up": "Days 3-5: for anyone who responds, do one manual review and ask what they did not trust.",
    "success": "Three problem-confirmation conversations and one design-partner commitment by day 7."
  },

  "limits": [
    "These are potential customers inferred from public signals, not confirmed buyers or people who consented to contact.",
    "46 of 84 candidates were rejected on Saudi identity — visible English-language demand skews expat.",
    "Snapchat and TikTok carry large Saudi audiences but were not searchable for text evidence."
  ]
}
```

## Field rules

- `quote_ar` is **required** for any Arabic-language source. Verbatim, unedited.
- `link_verified` must be `true` for every entry in `prospects`. Anything else was
  dropped before this stage.
- `scope_tier` is `confirmed` or `likely` for prospects. `unverified` and `rejected`
  belong in the `rejected` array.
- `opener_ar` is present only for the top three, and omitted entirely in `research-only`
  mode.
- `rejected` must not be empty on a real run. If nothing was rejected, the identity
  filter did not run.
- `rejected` entries carry **no `name`, no `source_url`, and no quote**. A count proves
  the filter ran; a handle printed beside an inferred nationality is a sensitive claim
  about a real person, in a document built to be shared. The generator aggregates the
  array to reason × platform counts and cannot render an identifier even if one is
  present, so writing handles here does not leak — it is simply wasted work.
- `quote_ar` on a prospect is one or two sentences. The generator truncates anything
  over 280 characters: past that the report has stopped quoting evidence and started
  republishing the post.
- `quote_lang` is an **optional** companion to any `quote_ar` field (on a prospect,
  pattern, feature gap, or competitor) — a BCP-47-style language code such as `"ar"`,
  `"de"`, or `"pt"`. It decides the `lang` attribute and, indirectly, the render
  direction of that quote block. When omitted, the generator infers direction from the
  quote text itself using the first-strong-character rule (the same rule behind HTML's
  `dir="auto"`): the first character with a strong direction decides right-to-left or
  left-to-right for the whole quote. It only ever guesses a specific *language* code for
  the right-to-left case, defaulting to `"ar"`, because Arabic is this skill's
  overwhelmingly common right-to-left source; a left-to-right quote with no declared
  `quote_lang` renders with the correct direction but no `lang` attribute, since Latin
  script alone does not say whether the text is German, Portuguese, or something else.
  Set `quote_lang` explicitly whenever the source language is known — it is always more
  reliable than inference.
- Counts in `patterns` and `product_intelligence` are counts of observed independent
  signals. Never estimated, never rounded up.
- `type` on a feature gap is `build` (product does not do it) or `message` (product does
  it but nobody knows).
- `competitors[].kind` is free text but should name the actual form: `Human service`,
  `Free workaround`, `App`, `Agency`, `Marketplace seller`. `threat` is `high`, `medium`,
  or `low`. Include the incumbent even when it is free — a circulating ChatGPT prompt is
  usually the hardest competitor to displace.
- `signal_date` drives the freshness chart in the dashboard. Use `YYYY-MM-DD` where the
  source shows an exact date, `YYYY-MM` where it only shows a month. Anything unparseable
  lands in the "older / unknown" bucket, which is visible to the reader.
