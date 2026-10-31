# Arabic glossary for Major Revisions (مسرد المصطلحات العربية)

This glossary explains the term choices in the Arabic edition of Major Revisions (`i18n/ar/cards.json`,
`i18n/ar/ui.json`) so that a native-speaking methodologist can check or contest them. Major Revisions is a game of the
SMART-Lab Science Game Kit; its Arabic follows the reviewed decisions of Methodical
(`methodical-card-game/i18n/ar/GLOSSARY.md`) and Red Flag (`red-flag-card-game/i18n/ar/GLOSSARY.md`), so a concept
has the same Arabic term in all kit games.

Principles (as in Methodical and Red Flag):

- **The term Arabic scientific writing actually uses**: WHO EMRO usage (Unified Medical Dictionary, EMHJ) first for
  medicine and epidemiology; Arabic textbooks, theses and journal guidance for statistics, social science and
  publishing.
- **The most widely understood form** where regions differ; alternatives are listed in the notes.
- **One concept, one term** across card names, card text, explanations, interface strings and picture labels.
- Modern Standard Arabic, Arabic punctuation (، ؛ ؟) and «guillemets», Western digits with a comma as thousands
  separator (3,000؛ 1,204), as in the sibling editions. Author, guideline, tool, database and compound names stay in
  Latin script (CONSORT, STROBE, PRISMA, COREQ, STARD, ARRIVE, TIDieR, PROSPERO, PubMed, RoB 2, PICO, Egger,
  Braun & Clarke, NR-4). Statistical symbols stay Latin (p، t، I²، H₁).
- The "why" explanations end with the fix in verbal nouns («قابل للإصلاح: إعادة التحليل…», «طفيف: إضافة…»), which
  is shorter than the imperative and does not address the reader as the author.

"Usage" in the source column marks a choice based on common usage for which no authoritative online source was
checked. "[M]" means the term is taken over unchanged from Methodical's or Red Flag's reviewed Arabic glossary.
Numbers in brackets refer to the sources at the end.

## The game's own vocabulary

| English | Arabic used | Source | Note |
|---|---|---|---|
| Reviewer | **المحكّم** (pl. المحكّمون) | [1] [M] | Methodical already uses «المحكّم 2» for Reviewer 2. Arabic journals call peer review التحكيم and reviewers المحكّمون (Qatar University's *Tajseer* peer-review page [1]). مراجِع is also heard, but in this game it would clash with مراجعة منهجية (systematic review): the S7 review's own screeners are therefore «باحثان», not «مراجعان». |
| Peer review; review round | **تحكيم الأقران; جولة تحكيم** | [1] [M] | Methodical: «جولة تحكيم الأقران». "Under review" → «قيد التحكيم»; "peer-reviewed" (S7) → «محكّمة». Nav "Review" → «التحكيم»; "Review a manuscript" → «حكِّم مخطوطة». |
| Manuscript; Manuscript card | **المخطوطة; بطاقة المخطوطة** (deck: بطاقات المخطوطة) | usage | The word Arabic journals use for a submitted paper («إرسال المخطوطة»). Feminine, so "sound" on a card and a manuscript is «سليمة». |
| Request | **طلب** (deck: الطلبات) | usage | Request "asks" addressed to the authors use the plural imperative («اعرضوا»، «اذكروا»، «صِفوا») or a direct question, as a reviewer's comment would. |
| Verdict | **القرار** (deck: القرارات) | [1] usage | The editorial decision. Red Flag uses حكم for a player's call on a claim; here the card is the journal's decision, for which Arabic journals say «القرار» (قرار المحرر / هيئة التحرير). "Right verdict" → «القرار الصحيح». |
| Accept / Minor revisions / Major revisions / Reject | **قبول / تعديلات طفيفة / تعديلات جوهرية / رفض** | [1] [2] | [1] lists قبول المقال دون… تعديلات، تعديلات بسيطة، تعديلات جوهرية، رفض المقال. طفيفة (rather than بسيطة) follows the reviewer instructions of other Arabic university journals found in the same search [2] («تعديلات جذرية أو طفيفة»), and pairs better with the card's severity tag. Stamp labels: «قبول، طفيفة، جوهرية، رفض». |
| As submitted | **كما قُدِّمت** | usage | Refers to the manuscript (feminine). |
| Flaw; flawed; sound | **خلل (أوجه الخلل); معيب / معيبة; سليم / سليمة** | [M] | Red Flag: معيب أم سليم؟ Plural counts use «أوجه الخلل» ("Flaws found" → «أوجه خلل مكتشفة»). |
| Planted flaw; to plant | **خلل مدسوس; دسّ** | usage | دسّ = to slip in secretly, which is the Author's move. |
| Flaw severity: minor / major / reject | **خلل · طفيف / خلل · جوهري / خلل · يوجب الرفض** | usage | Same adjectives as the verdicts, so the tag predicts the verdict. In "why" texts, "Minor:" → «طفيف:», "Fixable:" → «قابل للإصلاح:». |
| Slots: Question / Method / Sample / Measurement / Analysis | **السؤال / المنهج / العينة / القياس / التحليل** | [M] | المنهج follows Methodical's card type for *Method*. |
| Author (role) | **المؤلف** (pl. المؤلفون) | [M] | |
| Report (reviewer's report); to mark | **التقرير; أشِّر على** | usage | "Marked as flawed" → «المؤشَّر عليها بأنها معيبة». |
| Reporting guideline | **إرشادات الإبلاغ** | usage | No official Arabic translation of CONSORT or the EQUATOR guidance was found [3]. الإبلاغ follows Methodical's «أبلِغ عن». |
| Checklist item | **بند (بنود قائمة التحقق)** | usage | "CONSORT item 22a" → «البند 22a من CONSORT»; item numbers unchanged. |
| Flow diagram | **مخطط التدفق** | usage | The literal form, transparent to readers of the English guidelines. |
| Flaw key (answer key) | **مفتاح أوجه الخلل** | [M] | Red Flag: مفتاح الإجابات. |

## Cross-cutting terms reused from the kit

| English | Arabic used | Source | Note |
|---|---|---|---|
| outcome; exposure | **الحصيلة (الحصائل); التعرض** | [M] | Primary outcome → «حصيلة أولية». |
| cohort study; parent cohort | **دراسة أترابية; المجموعة الأترابية الأم** | [M] | |
| case–control; controls | **الحالات والشواهد; الشواهد** | [M] | |
| randomised trial; randomisation | **تجربة معشاة; التوزيع العشوائي** | [M] | معشاة only inside the trial name. "As randomised" → «كما وُزِّعوا». |
| allocation; allocation sequence | **التخصيص; تسلسل التخصيص** | [M] | |
| blinding; unblinded | **التعمية; غير معمَّى / بلا تعمية** | [M] | |
| confounding; confounder; adjust for | **الإرباك; العامل المربك; التعديل لـ** | [M] | Red Flag open question 7 (التعديل vs ضبط) applies here too. |
| bias; risk of bias | **التحيز; خطر التحيز** | [M] usage | |
| recall bias; spectrum bias; publication bias | **تحيز الاستدعاء; تحيز الطيف; تحيز النشر** | [M] | |
| attrition, loss to follow-up | **الاستنزاف; الفقد أثناء المتابعة** | [M] | "Selective loss to follow-up" → «الاستنزاف الانتقائي». تسرّب stays reserved for data leakage, so survey drop-off is «الانقطاع». |
| intention to treat; per protocol | **تحليل النية للعلاج; وفق البروتوكول** | [M] usage | |
| sensitivity analysis; sensitivity / specificity | **تحليل الحساسية; الحساسية / النوعية** | [M] | |
| reference standard; cut-off | **المعيار المرجعي; الحد الفاصل** | [M] | Methodical art: CUTOFF → «حد فاصل». |
| confidence interval | **فترة الثقة** | [M] | |
| odds ratio | **نسبة الأرجحية** | [M] | |
| statistically significant | **دالّ إحصائيًا** | [M] | |
| p-hacking | **التلاعب بقيمة p** | [M] | Methodical: «المسارات المتشعبة والتلاعب بقيمة p». |
| multiplicity correction | **تصحيح تعدد الاختبارات** | [M] | |
| systematic review; meta-analysis; pooled | **مراجعة منهجية; تحليل تلوي; مدموج** | [M] | |
| heterogeneity | **عدم التجانس** | [M] | |
| funnel plot | **مخطط القمع** | [M] | |
| validity; validated | **الصدق; مُتحقَّق من صدقه** | [M] | Art label VALID? → «صادق؟». Reliability → الثبات. |
| purposive sampling; saturation | **المعاينة القصدية; التشبع** | [M] | |
| reflexivity; thematic analysis; themes | **الانعكاسية; التحليل الموضوعاتي; الموضوعات** | [M] | The interview guide's *topics* are «محاور» so that الموضوعات stays reserved for *themes*. |
| coding; codes; coder | **الترميز; الرموز; مُرمِّز** | [M] usage | Coding tree → «شجرة الترميز»; audit trail → «مسار تدقيق». |
| pilot (data, study) | **دراسة استطلاعية** | [M] | Interview-guide *piloting* → «جُرِّب مسبقًا». |
| burnout | **الاحتراق الوظيفي** | [M] | |
| population (source) / (sampling frame) | **السكان / المجتمع الإحصائي** | [M] | |
| statistical power | **القوة الإحصائية** | [M] | |
| false alarm | **إنذار كاذب** | [M] | |

## Terms new in Major Revisions

| English | Arabic used | Source | Note |
|---|---|---|---|
| registration; registry entry; preregistered | **التسجيل; قيد السجل; مسجّل مسبقًا** | [M] usage | |
| prespecified | **محدد مسبقًا** | usage | |
| HARKing | **فرضية لاحقة (HARKing)** | usage | English acronym kept in brackets, as the kit does for p-hacking in Red Flag. |
| overclaiming | **المبالغة في الادعاء** | usage | |
| intervention; comparator | **التدخل; المقارِن** | usage | |
| recruitment; eligible; included; screened | **التجنيد; مؤهل; مُدرَج; فُرز** | [M] usage | Methodical uses التجنيد in feasibility. Screening for eligibility is الفرز (not فحص, which Red Flag reserves for its Check cards). |
| data saturation | **تشبع البيانات** | usage | |
| interviewer | **مُجري المقابلات** | usage | |
| partial verification (bias) | **التحقق الجزئي** | usage | |
| pseudoreplication | **التكرار الزائف** | usage | No Arabic source found. |
| multiple imputation; prorated | **التعويض المتعدد; عُوِّض بالتناسب** | usage | Alternatives seen: الإحلال المتعدد، الإسناد المتعدد. |
| weighting; weighted | **الترجيح; مرجَّح** | usage | |
| random effects; standardised mean difference | **التأثيرات العشوائية; فروق المتوسطات المعيارية** | usage | |
| small-study effects | **آثار الدراسات الصغيرة** | usage | |
| reporting bias | **تحيز الإبلاغ** | usage | |
| infarct volume; vehicle | **حجم الاحتشاء; المادة الحاملة** | usage | UMD-style alternative for vehicle: السَّواغ. |
| actigraphy | **قياس النشاط بجهاز على المعصم** | usage | Described rather than named; no settled Arabic term found. |
| histology | **الفحص النسيجي** | usage | |
| bedside ultrasound | **الموجات فوق الصوتية بجانب السرير** | usage | |
| moral distress | **الضيق الأخلاقي** | usage | |
| mindfulness | **اليقظة الذهنية** | usage | |
| moderate (pooled effect) | **معتدل** | usage | Not متوسط, which is the statistical *mean*. |
| home-made (measure, item) | **من إعداد الباحثين** | usage | Not «محلي الصنع», which reads as "locally produced" (made in this country). Added in review. |

## Units, numbers and right-to-left display

Applied exactly as in Red Flag (its glossary, "Units, numbers and right-to-left display", measured in headless Chrome):

- **Signed numbers**: an invisible left-to-right mark (U+200E, `‎` in the JSON) before every signed score
  placeholder: `play.scoring` (‎+{found}، ‎{wrong}، ‎+{verdict}، ‎+{unused}), `result.b_wrong`
  (‎{pts}, because pts is −1) and `result.b_verdict` (‎{pts}, because the app passes "+2").
- **Scoring reference card**: the labels `card.sc_found`, `sc_wrong`, `sc_verdict`, `sc_unused`, `sc_author` end with
  U+200E, because `tools/cards.py` prints the score (+3, −1) right after them; this is Red Flag's fix for
  «الأفضل» «فخ».
- **Picture labels**: SVG pictures are drawn left to right; the one label that mixes Arabic with Latin and a
  subscript, «H₁ قبل البيانات», is wrapped in a right-to-left isolate (U+2067 … U+2069). All other labels are pure
  Arabic (with the Arabic question mark ؟) or stay Latin (AB on the allocation slips, Zz for sleep). The kit's
  `i18n.problems` control-character check (`[\x00-\x08\x0b\x0c\x0e-\x1f]`) does not reject these marks.
- **Short formulas** (p < 0.05، p < 0.001، I² = 34%) use no-break spaces (` `), as in Red Flag.
- **Arrows**: the request log («{request} ← بطاقة {slot}») points left, from the request to the card in the reading
  direction. The kit link («→ SMART-Lab Science Game Kit») points right, towards the start of an RTL line, i.e. "back",
  as the English ← does in LTR and exactly as in Red Flag's Arabic `kit.link`.
- **Unit**: mm → مم, as in the sibling editions.

## Not yet checked in the browser

These files were validated with `i18n.problems('ar')` and `i18n.coverage('ar')` only. The build and the card-fit
check are run afterwards by the project owner; the bidi marks follow Red Flag's measured technique but were not
measured on this game's pages.

## Still open (for a native methodologist)

1. **Minor revisions**: «تعديلات طفيفة» (chosen) or «تعديلات بسيطة» (Qatar University's *Tajseer* [1])? Both are in
   journal use; طفيفة was chosen for its pairing with جوهرية.
2. **Verdict**: «القرار» (editorial decision) here, while Red Flag's player call is «حكم». Is the split right, or
   should the kit use one word?
3. **Reviewer**: المحكّم (chosen, kit) versus المراجِع, which some medical journals use. Check that المحكّم reads
   naturally to clinicians, not only to humanities and law journals.
4. **Manuscript**: «المخطوطة» can suggest a historical handwritten manuscript to lay readers; «البحث المقدَّم» or
   «الورقة» are alternatives.
5. **Flow diagram, reporting guideline, checklist item**: no official Arabic CONSORT/PRISMA/STARD translation was
   found; the literal forms مخطط التدفق، إرشادات الإبلاغ، البند should be checked against any Arabic translation a
   reviewer knows.
6. **Multiple imputation**: التعويض المتعدد versus الإحلال المتعدد.
7. **Pseudoreplication**: التكرار الزائف is a literal coinage.
8. **Planted** («مدسوس»): does the metaphor read naturally in a game?
9. **Picture labels** «اختبار الحقيقة» (THE TRUTH TEST, the reference standard) and «تسلسل مختوم» (SEALED SEQUENCE):
   playful renderings that keep the English tone; «المعيار المرجعي» and «تسلسل مُخفى» are the plain alternatives.
10. **Gender**: the head nurse (S5) is rendered masculine because English does not say; the interviewer in the sound
    version is feminine, as in the English ("her nursing background").

## Review (independent pass, 31 October 2026)

Every string of `ui.json` and `cards.json` was read against the English. The translation is accurate and consistent
with the kit; the changes below were made directly in `cards.json`. `ui.json` needed no change.

### Meaning (fixed)

| Where | English | Was | Now | Why |
|---|---|---|---|---|
| S7 sample, recruitment "why" | Unpublished trials *more often* find no effect | التجارب غير المنشورة تجد **في الغالب** ألّا أثر | التجارب غير المنشورة **أكثر من المنشورة ميلًا** إلى ألّا تجد أثرًا | «في الغالب» says *most* unpublished trials find no effect, a different and unsupported claim. The English is a comparison with published trials. |
| S3 claim | *doubles* the risk | **يضاعف** خطر كسر الورك | **يرفع** خطر كسر الورك **إلى الضعف** | ضاعف can mean "multiply many times" (أضعافًا مضاعفة); the multiplier must read as ×2 only. |
| S4 claim | poor supervision *causes it* | وسوء الإشراف **هو السبب** | وسوء الإشراف **يسببه** | «هو السبب» makes it *the* (sole) cause, stronger than the authors' claim the player has to judge. |
| Flaw *unvalidated measure*; S2 measurement "why" | *home-made* measure / item | مقياس **محلي الصنع**؛ بند واحد محلي الصنع | مقياس **من إعداد الباحثين**؛ بند واحد … من إعداد الباحثين | محلي الصنع means "locally manufactured / domestic"; a reader can take it as "developed in this country", which is not the flaw. من إعداد الباحثين is how Arabic theses describe a self-made instrument (usage). |

### Precision and wording (fixed)

| Where | Was | Now | Why |
|---|---|---|---|
| S1 claim (physical function) | الأداء البدني | الأداء الوظيفي البدني | One term for *function* (الأداء الوظيفي) across the study; الأداء البدني drifts towards "physical performance", the name of the test. |
| S1 method, allocation sound (released *only after* enrolment) | تصدره خدمة ويب مركزية بعد الإدراج فقط | لا تكشفه خدمة ويب مركزية إلا بعد الإدراج | «بعد الإدراج فقط» can be read "releases it after enrolment, and that is all"; لا … إلا puts *only* on the timing, which is the point of concealment. |
| S1 question, registration sound (before the first patient) | قبل المريض الأول | قبل إدراج المريض الأول | Before what about the first patient. |
| Request *Test cut-offs* (cut-off for a positive test) | الحد الفاصل للاختبار الإيجابي | الحد الفاصل لعدّ الاختبار إيجابيًا | The cut-off decides when a test counts as positive; the old phrase read as "the cut-off of the positive test". |
| S5 claim (staffing) | نقص الكوادر | أعداد الكوادر | English says *staffing*, not *shortage*; the translation added a finding. |
| Flaw *missing data ignored* (who is missing is not random) | مع أن الغياب ليس عشوائيًا | مع أن فقدها ليس عشوائيًا | الغياب suggests absence from work or class; the point is the records' missingness. |
| Flaw *single coder* (nobody can follow how) | ولا يستطيع أحد تتبّع كيف. | ولا يستطيع أحد تتبّع طريقته. | A sentence cannot end on a bare «كيف» in MSA. |

### Bidirectional text (checked, no change needed)

- Signed numbers: `play.scoring`, `result.b_wrong` (pts = −1, sent by the app as "-1") and `result.b_verdict` ("+2")
  carry U+200E before the placeholder. Because an LRM is a strong L character, the digits after it resolve to L
  (UAX #9, rule W7) and the sign stays on their left, the same technique Red Flag uses (`play.scoring`, `print.key_intro`).
  `result.b_found` and `result.b_unused` receive unsigned 3 and 1, so need no mark. The score labels on the reference
  card end in U+200E before `tools/cards.py` prints "+3", which works by the same rule.
- Formulas in running text (p < 0.05, p < 0.001, I² = 34% / 89%) start with a Latin letter, so their digits resolve to
  L and the run shows left to right; their no-break spaces are kept.
- Latin with digits (RoB 2, NR-4, Braun & Clarke (2006), ARRIVE item 9 → «البند 9 من ARRIVE») is safe for the same reason.
- Pure-number spans (1:1، 6%، 63 × 88 مم، {n} × {pts}) follow the Arabic reading order (the first number is on the
  right), which is the expected display in Arabic.
- `result.caught_by` fills `{item}` with ranges such as "2–3" or "24a–b". In running RTL text "2–3" shows with 2 on
  the right, read correctly right to left; "24a–b" stays one left-to-right run. Acceptable; wrapping `{item}` in
  `<bdi>` in the app would make it independent of the surrounding text (a code change, not made here).
- Picture label «H₁ قبل البيانات» in RLI…PDI: correct, because `tools/cards.py` sets the SVG to `direction: ltr`.

### Verdict terms (checked)

Qatar University's *Tajseer* peer-review page [1] was opened again on 31 October 2026 and reads: reviewers
(«المحكمين») may accept the article without changes, ask for «تعديلات بسيطة» or «تعديلات جوهرية», or reject
(«رفض المقال»). قبول، تعديلات جوهرية، رفض are therefore confirmed by a journal page. «تعديلات طفيفة» is common usage:
a second web search (31 October 2026) found reviewer forms using «قبول مع تعديلات طفيفة» / «صالح للنشر بعد تعديلات
طفيفة», but only as PDF or form snippets, not opened.

### Open questions settled

1. **Minor revisions**: keep «تعديلات طفيفة». Both forms are in use; طفيفة is the more exact opposite of جوهرية and
   matches the card's severity tag «خلل · طفيف». Not a source-based decision.
2. **Verdict**: keep «القرار». Red Flag's «حكم» is a player's judgement on a claim; here the card is the editorial
   decision on a manuscript ("the call an editor makes", `tip.verdicts`), which Arabic journals call a decision
   (قرار). Where this game means a player's judgement it already uses حكم («إجابة واحدة، حكم واحد»), so the two words
   keep the same meanings in both games.
3. **Reviewer**: keep «المحكّم»: confirmed on the Tajseer page [1] and already the kit term (Methodical's «المحكّم 2»).
   Whether clinicians prefer المراجِع stays unverified, but المراجِع would clash with مراجعة منهجية.
8. **Planted («مدسوس»)**: keep; دسّ is exactly "to slip in secretly", natural for the Author's hidden move.
9. **Picture labels**: keep «تسلسل مختوم» (sealed envelopes are «مظاريف مختومة» in everyday Arabic) and «اختبار
   الحقيقة»; both are pictures' captions, where the plain terms would cost length.
10. **Gender**: keep. رئيس التمريض as a generic masculine is normal MSA when the sex is not given.

Still open: 4 (المخطوطة vs البحث المقدَّم; kept, the game context removes the "old handwritten text" reading),
5 (no Arabic CONSORT/PRISMA/STARD translation checked), 6 (multiple imputation), 7 (pseudoreplication).

## Sources

1. Qatar University, Ibn Khaldon Center, *Tajseer* journal, "عملية التحكيم" (peer-review process), checked
   31 October 2026: reviewers («المحكّمون») may accept without changes, ask for «تعديلات بسيطة» or «تعديلات جوهرية»,
   or reject. https://www.qu.edu.qa/ar/Research/IbnKhaldon/Tajseer/Pages/peer-review-process.aspx
2. Web search, 31 October 2026, for Arabic journals' reviewer instructions: search snippets of the reviewing rules of
   the Kuwait International Law School journal and the Qassim University *Journal of Administrative and Economic
   Sciences* use «تعديلات جذرية أو طفيفة». The documents themselves were not opened (PDF downloads), so this is
   evidence of usage only.
3. Web search, 31 October 2026, for an Arabic CONSORT translation: none found; only an explanatory blog post
   (blog.ajsrp.com) that keeps the name CONSORT in Latin script.
4. Methodical's reviewed Arabic glossary, `methodical-card-game/i18n/ar/GLOSSARY.md` (its sources: WHO EMRO EMHJ,
   UMD, World Bank Arabic slides, Arabic Wikipedia and others).
5. Red Flag's reviewed Arabic glossary, `red-flag-card-game/i18n/ar/GLOSSARY.md`, including its right-to-left
   measurements in headless Chrome (Unicode UAX #9 behaviour of signs, isolates and formulas).
