# Saudi Arabic Query Lexicon

The search vocabulary is the product. Translated-English queries return content written
*about* Saudis; dialect queries return content written *by* them.

## Rule zero: spelling variation is not optional

Saudis type fast and informally. Hamza is dropped, ta marbuta and ha are interchanged,
and vowels are inconsistent. One spelling misses most of the corpus. Always fan out:

| Canonical | Also search |
| --- | --- |
| أبغى | ابغى · ابغا · أبغا · بغيت |
| أبي | ابي · أبى · ابى |
| وش | ايش · إيش · وشو |
| مرة | مره |
| كذا | كدا (rare in KSA — check for Egyptian contamination) |
| سيرة ذاتية | سيره ذاتيه · السي في · CV · سيفي |
| تطبيق | ابليكيشن · app |
| موقع | ويبسايت |

Also search the same concept with and without the definite article (`تطبيق` vs
`التطبيق`), and both singular and plural.

## Bucket 1 — Explicit demand

The highest-intent bucket. Someone is asking for the product out loud.

```
أبغى تطبيق                      ابغى موقع
أبي برنامج                       أدور على تطبيق
ادور على أداة                    محتاج تطبيق
فيه أحد يعرف تطبيق               فيه تطبيق يسوي
وش أفضل تطبيق                    وش احسن موقع
وش تنصحوني                       تنصحوني بتطبيق
يا ليت فيه تطبيق                 ليش ما فيه تطبيق
هل يوجد تطبيق                    ابحث عن تطبيق
بديل لـ                          فيه بديل
أحد جرب                          مين جرب
عندكم توصية                      اقتراحاتكم
```

Combine each with the product noun in Arabic. For a resume tool:
`أبغى تطبيق يسوي سيرة ذاتية`, `وش أفضل موقع لكتابة السيرة الذاتية`,
`أدور على قالب سيرة ذاتية`.

## Bucket 2 — Pain

Saudi frustration vocabulary is distinctive and emotionally loaded. These words rarely
appear in formal Arabic content, which makes them excellent authenticity signals as well
as pain signals.

```
تعبت من            طفشت من            زهقت
مليت               قهر                 قهرتني
معاناة             أعاني من            صعب جدا
مشكلة كبيرة        ما ضبط              مو ضابط
ما يشتغل           خربان               معلق
ياخذ وقت           يستهلك وقت          ساعات وأنا
دوخة               تعقيد               معقد مره
محبط               إحباط               ما لقيت حل
كل مرة أعيد        رجعت من الصفر       ضاع تعبي
```

`قهر` / `قهرتني` is one of the strongest Saudi pain markers available. If someone writes
it, the pain is real and current.

## Bucket 3 — Workaround

Someone already solving the problem manually is a better prospect than someone merely
annoyed by it. They have proven willingness to spend effort.

```
أسويها يدوي         يدوياً             بالاكسل
اكسل               الاكسل             شيت
نسخ ولصق           كوبي بيست          قالب
قوالب              تمبليت             ملف وورد
كل شي يدوي         أرتبها بنفسي       أسجلها في الجوال
واتساب             في الجوال          دفتر
سويتها بالشات جي بي تي              استخدمت ChatGPT
جربت شات جي بي تي   عن طريق مكتب      عن طريق مكتب خدمات
```

`سويتها بالشات جي بي تي` is now one of the most common Saudi workarounds across every
category. It signals both the pain and the price ceiling.

## Bucket 4 — Switching and competitor frustration

```
ألغيت الاشتراك      لغيت الاشتراك      وقفت الاشتراك
ما يستاهل           غالي مره           أسعارهم غالية
ندمت                تجربتي مع          تجربتي السيئة
سيئ جداً            خدمة سيئة          ما ينفع
نصب                 نصابين             حرامية
ما رد علي           الدعم ما يرد       خدمة العملاء
انتقلت من           تركت               بحث عن بديل
مو مستاهل الفلوس    ضيعت فلوسي
```

`نصب` and `ما يستاهل` cluster hard in Saudi discourse around paid digital services. If
they appear in your category, trust is your primary conversion barrier and belongs in
the objections section.

## Bucket 5 — Timing triggers

Consumer triggers:

```
تخرجت               تخرجت حديثاً        خريج جديد
استقلت              تركت الشركة        دوام جديد
بديت مشروع          فتحت متجر          سجلت سجل تجاري
انتقلت للرياض       رحت جدة            رجعت من الابتعاث
تزوجت               بيت جديد           سيارة جديدة
```

Business triggers (for `b2b` mode):

```
نبحث عن موظف        وظائف شاغرة        نوظف
توسعنا              فرع جديد           افتتاح
أطلقنا              إطلاق              شراكة
حصلنا على تمويل     جولة تمويل         مستثمر
تحول رقمي           أتمتة              رقمنة
```

Vision 2030 program names are strong dated triggers: `نيوم`, `روشن`, `القدية`,
`البحر الأحمر`, `الرياض الخضراء`, `مسار`, `سعوده`, `نطاقات`, `منشآت`, `مسك`.

## Sector and platform nouns worth pairing

Government and quasi-government platforms are constantly discussed and carry both
context and pain:

```
أبشر · توكلنا · نافذ · ناجز · قوى · جدارات · طاقات · مساند · أبشر أعمال
منصة العمل · التأمينات · موارد · فرصة · هدف · درة · سهل · اعتماد · مقيم · نافس
```

Saudi consumer brands (useful for both context and competitive signals):

```
stc · موبايلي · زين · الراجحي · الأهلي · الرياض · دفع · مدى · تمارا · تابي
نون · جرير · اكسترا · هنقرستيشن · جاهز · نينجا · نعناع · طلبات · كريم · أوبر
سلة · زد · فودكس · ريناد · قوى
```

## Query construction pattern

```
[dialect verb] + [product noun] + [Saudi context word]
```

Examples:

```
أبغى تطبيق يرتب لي فواتيري
تعبت من ترتيب الفواتير بالاكسل
وش أفضل برنامج محاسبة للمتاجر الصغيرة بالسعودية
فيه أحد يعرف موقع يسوي سيرة ذاتية بالعربي
ألغيت اشتراك [competitor] لأنه غالي
```

Then add platform operators from `platform-playbooks.md`.

## English queries still matter — but expect a different population

English-language KSA queries return expats, recruiters, and content marketers far more
often than Saudi nationals. Run them, but route the results straight through
`saudi-identity-verification.md` and expect a high rejection rate. Useful English
patterns:

```
"in Saudi" + [pain]        "Riyadh" + "any app that"
"KSA" + "recommend"        "Saudi Arabia" + "is there a tool"
"anyone in Riyadh"         "Jeddah" + "struggling with"
```

## Field-tested corrections

These come from live runs. Ignore them and you will repeat the same wasted queries.

**Quote short civic terms.** X's Arabic stemmer will reduce `جدارات` to `جدار` (wall) and
return poetry about leaning on walls. Always write `"جدارات"`, `"طاقات"`, `"قوى"` in
quotes. The same risk applies to any short term with a common root.

**`تعبت من` + a product noun returns sellers, not buyers.** Service accounts open their
ads with exactly that phrase — "tired of X? we're the solution". Add `-filter:links`, and
consider excluding `-مكتب -واتساب -للطلب -تواصل`.

**Category keywords belong to vendors; symptom phrases belong to buyers.** Searching the
English-loan category term (`ATS`, `CRM`, `POS`) in Arabic returns promotional accounts
almost exclusively. Real customers describe the symptom instead — `محد يرد`,
`ما انقبلت`, `ما يضبط`. Use category terms to map competitors, and symptom phrases to
find people.

**High-yield phrases are often ambiguous.** `محد يرد` catches unanswered phone calls,
ignored WhatsApp messages, and dead customer-support lines as often as job applications.
Always pair it with a domain noun.

**Sellers are data too.** When a query returns a wall of vendors, do not discard it —
that is the competitive landscape, and in Saudi Arabia the vendor is usually a human
service taking orders by WhatsApp or DM, which sets the price anchor.

## Anti-patterns

Do not search these — they return marketing content, not customers:

- `best app in Saudi Arabia 2026` — SEO listicles
- `أفضل تطبيقات السعودية` — affiliate content farms
- Any query that is a product category name alone — returns vendors
- Hashtag-only searches without a pain or demand word — returns promotional spam

If a query returns mostly branded accounts, blogs, or news, the query is wrong. Add a
first-person verb (`أبغى`, `تعبت`, `جربت`, `أدور`) and run it again.
