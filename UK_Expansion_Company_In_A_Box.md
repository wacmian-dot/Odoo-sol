# SalesOps CRM UK — Company-in-a-Box
**A complete start-to-finish assessment: who RRUP/SalesOps CRM are, whether this UK expansion is viable, how to build it, how to fund it, and how to run it.**

**Status key used throughout:** ✅ Verified from a primary source (company website, government source, named search result) · 📊 Public market data · ⚠️ Framework/estimate — needs your input or professional advice to firm up · ❓ Open question for you or for RRUP · 🚩 Audit finding — a claim in your own prior material that didn't survive verification

---

## PART 0 — AUDIT OF YOUR FIVE EXISTING DOCUMENTS

You asked me to analyze everything you'd already produced and improve on it. I read all five documents in full and cross-checked every checkable claim against independent sources rather than taking them at face value — this is the same discipline the whole project runs on (see the method playbook). Here's the honest result, most important first.

### 🚩 0.1 The Polsat claim — do not use this until RRUP confirms it in writing
Four of your five documents state as settled fact that **SalesOps/RRUP's "flagship anchor tenant" is Grupa Polsat Plus** — a multi-billion-euro Polish media/energy conglomerate — and that this reference is safe to use as your central credibility weapon in UK sales pitches, cold outreach, and objection-handling scripts.

**I could not find one independent source connecting RRUP or SalesOps CRM to Polsat, anywhere.** I fully scraped RRUP's own website — the same site that proudly names "Polsat" nowhere, while featuring real, named, checkable testimonials (Maciej Bodo at "4eco," Yuliia Popova) that are nothing like a multi-billion-euro telecom/energy conglomerate managing "gigawatt-scale wind, solar, and hydrogen networks." A client of that size and profile is exactly the kind of name a 600-deployment mid-market vendor would headline on their homepage, not omit. It also doesn't fit RRUP's actual profile: their pricing, testimonials, and 15,000-user/600-deployment scale all point to a mid-market Polish trade-software vendor, not a supplier to a national telecom giant's gigawatt-scale infrastructure.

**My assessment: this is very likely an AI hallucination from whatever tool produced those documents** — Polsat is a real, famous, easily-searchable Polish company, which is exactly the kind of plausible-sounding name a language model reaches for to manufacture false credibility when asked to build a "trust shield." The one document that treats this carefully is the technical due-diligence slide deck (in Polish) — it correctly poses Polsat as a question to *ask RRUP's technical team to substantiate*, not a fact to assert. That instinct was right; the other four documents got it wrong.

**Why this matters more than a normal factual error:** if you say this to RRUP's CEO and it's false, you look like you don't understand their own business before a partnership is even signed. If you say it to a UK prospect and they check it (a competent Operations Director at a £5-50M firm will), it's a false statement about a third company made in a commercial pitch — a real reputational and potential legal exposure, not just an embarrassing correction. **Do not use the Polsat reference anywhere — in conversation with RRUP or with any prospect — until RRUP's own team confirms it to you directly, in writing, with something checkable (a case study, a named contact at Polsat, anything).** The technical due-diligence deck's question 12 ("how was this scaled across corporate divisions...") is exactly the right way to raise it with RRUP first.

### 🚩 0.2 Two incompatible deal structures are described across your own documents
This needs resolving before anything else here is buildable:
- **Documents 1 and 2** (the Strategic Expansion Plan and the Bart recruitment brief) describe you as **"Managing Director, UK Division,"** running a **branch/subsidiary** with "Regional Equity Pool" compensation — i.e., an operating company you have equity in, consistent with what you told me earlier (50/50 co-ownership).
- **Document 4** (the "PhD advisor" transcript) describes an entirely different model: a **50% sales commission / agency arrangement** under an "International Master Agency Agreement" with **"Territorial Exclusivity," "lifetime commission rights,"** and explicit language that **"your vehicle bears no engineering or infrastructure liability"** — i.e., you're a paid sales agent/reseller for RRUP's existing product, not a co-owner of a UK operating business.

These are fundamentally different arrangements with different funding needs, different legal structures, different tax treatment, and different risk profiles (an agency deal has essentially no downside capital risk; a 50/50 equity JV means you're jointly liable for a real operating company). **I can't tell from what's in front of me which one is actually being discussed with RRUP, or whether both were floated at different points.** This is the single most important thing to nail down before we go further — see the question list at the end of this document.

### 🚩 0.3 Smaller factual corrections
- **"600,000 heat pumps per year by 2030"** (Document 1, §2) — the real UK government target is **600,000 per year by 2028**, not 2030. Real target, wrong year — worth fixing before it's said out loud to anyone who knows the policy.
- **Academic citations** ("Kumar & Reinartz's enterprise models," "Adrian Payne's *Handbook of CRM*, pages 378–380," "V. Kumar's *Customer Relationship Management*") appear in Documents 1 and 3 with suspiciously precise page numbers. I can't verify these citations and the specificity is a classic pattern of AI-generated citations that sound authoritative but aren't checkable — treat these as decoration, not real academic support, and don't repeat the page numbers to anyone who might actually own the book.
- **"500+ European clients"** (Document 2) vs. what I verified directly from RRUP's own site (**600+ deployments, 15,000+ users**) — not necessarily contradictory (clients vs. deployments aren't the same count), but it's an unreconciled number; use my directly-sourced 600+/15,000+ figures, not the 500+ figure.
- Illustrative numbers presented with false precision, e.g. "£50,000 in custom development fees" (Document 4) as the cost to replicate this in Salesforce — this is a plausible-sounding but invented figure, fine as a rhetorical device in a live pitch, not something to print as a fact.

### 🚩 0.4 "Bart" content — disregarded per your instruction
Documents 2 and 4 build significant material around a named sales co-founder ("Bart," including his employer "Crown Energy" as a lead-generation asset). You've told me Bart is not your partner, so I've dropped all Bart/Crown-Energy-specific personnel planning entirely. Two underlying *ideas* (not the Bart-specific execution) are still worth keeping and are folded into Part 3 below: mining a warm industry-insider network for lookalike prospects, and the MCS-register-plus-LinkedIn cross-referencing method for building a target list.

### ✅ 0.5 What was genuinely good and is now merged into this document
Real, useful strategic thinking survived the audit and is incorporated below: the **SAP S/4HANA "system of engagement vs. system of record" positioning** (a smart, specific way to defuse the "rip and replace" objection with mid-market/enterprise prospects using SAP), the **lean 3-role launch pod structure** with weekly activity metrics, the **90-day phased operational roadmap**, the **30-day onboarding framework** (Day 1–7 data migration / 8–21 configuration / 22–30 field crew training) aimed at the same churn-prevention problem RRUP's own 30-day free trial creates, the **"leaky bucket" pitch framing** (lead with quantified operational pain, not features), the competitor list (several names — Commusoft, Simpro, BigChange, Jobber/ServiceM8 — independently corroborate what I found), and a real, previously-unknown trade show: **InstallerSHOW, 23–26 June 2026, NEC Birmingham — 1,000+ exhibitors, 40,000+ visitors from heat/water/air/energy trades.** ✅ (verified)

**One gap in your own documents worth naming directly: none of the five mention Payaca or Reonic** — the two competitors most directly relevant to what you're actually about to do (Payaca is the UK-native renewables-specific CRM leader; Reonic is the German company running the exact EU-to-UK playbook you're being asked to run). That gap is now closed in Part 2 below.

---

## PART 1 — WHO THEY ARE

### 1.1 The company ✅
**RRUP sp. z o.o.** — a Polish limited-liability company (the Polish equivalent of a UK Ltd).
- **KRS (company register number):** 0000978166
- **NIP (tax ID):** 5423451043
- **Offices:** Białystok (HQ — ul. Świętego Andrzeja Boboli 24, 15-649 Białystok) and Sejny (ul. Zawadzkiego 1, 16-500 Sejny), north-eastern Poland
- **Sales line:** +48 574 422 173 · **Support line:** +48 731 426 000
- **Self-described positioning:** "a fast-growing IT company... producer of RRUP CRM software for managing projects, customer relationships, and organising the whole company in one place."

This is not a two-person outfit — it's an established, scaled Polish software vendor.

### 1.2 Real scale — their own published numbers ✅
| Metric | Value |
|---|---|
| Users on the platform | **15,000+** |
| Documents generated by the system | **2.5 million+** |
| System deployments/implementations | **600+** |
| Lines of code (stated, marketing claim) | 200,000+ |
| Free trial offered | 30 days, no obligation |

600+ deployments and 15,000+ users is a genuinely proven product, not an early-stage MVP — this materially de-risks the "is the product any good" question before you've even seen the demo.

### 1.3 What the product actually does ✅
RRUP CRM is a vertical-specific, trade/field-service CRM built around one core idea: **one system covering the entire customer lifecycle** — lead capture → quoting/proposals → contract generation & e-signature → installation/job scheduling → completion → invoicing/commission → reporting — for physical-installation trades.

Named capabilities, all confirmed on their site:
- **Automated sales funnel** — lead to close, with no manual hand-offs required
- **Work-Flow engine** — auto-assigns tasks, sends SMS/system notifications at each contract stage, routes responsibility to named people/teams, **auto-calculates sales commission** on status completion
- **Document generation** — branded PDF quotes/contracts/completion protocols on the client's own letterhead, e-signature with contractors
- **100+ pre-built add-on modules**, open API for integrations, and bespoke development for unique client requirements
- **Reporting/analytics** — sales pipeline, user activity, install/job reports, meeting summaries
- **Vertical-specific modules**, each marketed as "the most extensive CRM for this industry available on the Polish market": Solar PV (fotowoltaika), Heat Pumps (with a native integration into **cieplo.app**, a heat-pump sizing/design tool), Air Conditioning/Refrigeration, Service sales, Construction, Field Service/Maintenance, HRV/MVHR (rekuperacje), IT/project management

### 1.4 Real client evidence ✅
Named, on-record testimonials (not anonymous marketing copy):
- **Maciej Bodo, Technical Director** — large-organisation phased rollout, "significantly customised to our requirements," cites improved communication, optimised costs, automated most processes, higher staff productivity and profit.
- **Yuliia Popova, Board Member** — confirms working directly with "RRUP sp. z o.o." from the outset, full process automation, professional client-facing offers, single-workspace company control.
- A third (unnamed in the extract) — solar PV + heat pump modules, described implementation as "pure pleasure."

### 1.5 Pricing model ✅ (their live Polish price list, net of VAT)
Per-seat SaaS, volume-tiered:

| Users | PLN/user/month | Approx. GBP/user/month* |
|---|---|---|
| 1–10 | 100 zł | ~£20 |
| 11–20 | 90 zł | ~£18 |
| 21–30 | 80 zł | ~£16 |
| 31–69 | 70 zł | ~£14 |
| 70–199 | 60 zł | ~£12 |
| 200–499 | 50 zł | ~£10 |
| 500+ | 40 zł | ~£8 |

\*Converted at the mid-July 2026 rate (1 PLN ≈ £0.198). This is the **Polish** price list — UK pricing is a decision you and RRUP need to make (see §7). Do not assume it transfers directly: UK trade software (Payaca, Commusoft) tends to price higher per seat, which is actually a competitive opening, not a constraint.

### 1.6 The UK brand already exists — and that's important ❗
"**SalesOps CRM**" is RRUP's own existing brand name for the UK market — confirmed via multiple independent search results describing it as "a RRUP product," using the same vertical structure (solar, heat pumps, HVAC, construction, service, HRV). Public search snippets already describe SalesOps CRM in superlative UK-market terms ("the most extensive CRM for the HRV systems industry available on the UK market," "the most advanced construction CRM available on the UK market").

**The gap this reveals:** the brand and marketing site exist, and stake bold UK-market claims, but per what you've told me there is no actual UK operational presence — no UK team, no UK customer base, no UK support. That's a real, specific risk worth naming to RRUP directly and early: **the website is ahead of the business.** Part of your job in this partnership isn't just "launch a new market" — it's making claims that are already published, true. That's a stronger opening line with them than it sounds ("I read your UK site before we spoke — here's how I close the gap between what it says and what's actually true").

I could not load `salesopscrm.com` directly (Cloudflare bot-protection blocks non-browser requests, and I don't have working browser automation in this session — see the earlier turn). Everything above about SalesOps CRM specifically is from search-engine snippets and inference from RRUP's identical Polish site, not a direct read of the UK site itself. **Getting real access to that site (and to the CRM demo) is the single highest-value unblock for sharpening all of this — see the CRM access section again below.**

---

## PART 2 — IS THIS VIABLE? MARKET & OPPORTUNITY ASSESSMENT

### 2.1 The UK market is real, large, and growing fast 📊
| Metric | 2025/2026 figure |
|---|---|
| MCS-certified UK installers (all technologies) | **5,250+** (highest since MCS began in 2008) |
| MCS-certified solar PV installers | **4,000+** |
| Solar PV systems installed in the UK, 2025 | **267,032** — a 31% jump over the prior record (2011) |
| Heat pump installations, 2025 | **60,000+** — the most in a single year ever |
| Cumulative UK heat pump installs (since 2009) | **250,000+** (passed Feb 2026) |
| 2026 forecast growth | **+50% year-on-year** |
| Government heat pump installation target | **600,000 per year by 2028** ✅ (corrected — your Document 1 cited 2030; the real target year is 2028, per the 2020 Ten-Point Plan) |

**Why now, specifically:** the Boiler Upgrade Scheme grant (up to £7,500 off a heat pump), 0% VAT on solar installations (through March 2027), and the MCS mandate itself are structural, government-driven tailwinds pushing installer businesses to scale fast — and scaling installer businesses is exactly when they outgrow spreadsheets/WhatsApp and start shopping for a CRM. The market isn't just growing; it's growing for reasons that specifically create CRM demand (more jobs, more compliance paperwork, more subcontractor coordination).

### 2.2 Competitive landscape 📊 — you are not first, and that's informative not fatal
| Competitor | Position |
|---|---|
| **Payaca** | UK-native, the most complete dedicated platform for solar/heat pump/battery/EV installers — CRM, pipeline, **MCS-compliant proposals**, scheduling, invoicing. This is your closest direct competitor and the one to benchmark feature-for-feature once demo access works. |
| **Reonic** | German-founded (2021), raised **€13M Series A in 2024**, actively expanding into the UK right now — i.e. a well-funded continental European player running exactly the playbook you're being asked to run. Worth treating as the pattern-match for "how does a EU trade-CRM vendor actually break into the UK," not just a threat. |
| **Commusoft** | Broader UK trade-CRM (plumbing/heating/electrical), deep feature set, not renewables-specific — competes at the edges. |
| **Tradify, AdminBase, BigChange, Simpro** | General trade job-management/CRM tools — compete on price/simplicity rather than renewables-specific depth. |

**What this tells you, honestly:** the UK renewables-installer CRM niche is already being actively contested by at least one well-funded EU entrant (Reonic) and one UK-native leader (Payaca). This is not a blue ocean. It is a real, validated, fast-growing category with room for a third credible player — but only with genuine differentiation, not just "we're cheaper" or "we're new." The next section addresses that directly.

### 2.3 Where RRUP's actual differentiation could sit ⚠️ (thesis — needs demo verification)
Based on published capability alone, three areas look like plausible wedges once verified against the demo and against what Payaca/Reonic actually ship:
1. **Cross-vertical breadth in one system.** RRUP already covers solar, heat pumps, AC/refrigeration, construction, service, HRV, and IT — a UK installer who does solar *and* heat pumps *and* battery storage (increasingly the norm, not the exception, per the "solar + heat pump combo" trend showing up repeatedly in UK market coverage) may prefer one system over stitching together single-vertical tools.
2. **Depth of workflow automation.** The Work-Flow engine (auto-tasking, SMS/notification cascades, auto commission calculation) is a specific, named capability — confirm whether Payaca/Reonic match it before claiming it as a differentiator, but it's a strong candidate.
3. **Price-to-depth ratio.** If UK pricing lands meaningfully below Payaca on a comparable feature set (their Polish pricing, even marked up 30-50% for the UK market, likely still undercuts UK-native competitors), that's a real, usable wedge for price-sensitive smaller installers — the exact segment growing fastest per the MCS data (more new entrants = more small, cost-conscious shops).

**This whole section is a thesis to pressure-test, not a settled USP** — it needs the demo and a genuine Payaca/Reonic feature comparison to become a real claim you can put in front of a prospect.

### 2.3b Objection-handling positioning that's genuinely good (from your own Document 1/3/4) ✅ (strategy, not fabricated fact)
One piece of your existing strategic thinking is worth keeping and is a real point of craft: **"System of Engagement" vs. "System of Record."** For any Tier-2/3 contractor already running SAP, Xero, Sage, or QuickBooks for core accounting, don't position SalesOps CRM as a replacement — position it as an agile front-end that sits on top of their existing system of record via API, handling the vertical-specific calculations (solar array layout, heat pump flow rates/COP, BTU sizing) that would cost tens of thousands in custom development to bolt onto a generic ERP. This is a legitimate, well-worn enterprise-software sales pattern (not something that needs a fabricated case study to work) and it directly defuses the single biggest objection a finance-literate prospect will raise ("why would I add another system").

### 2.4 Viability verdict ⚠️
**On the evidence gathered so far: this is a defensible, fundable opportunity, not a speculative one.** You have a proven product (600+ deployments, 15,000+ users, real named references), a genuinely growing target market with structural tailwinds, and a specific, nameable gap (the UK brand exists on paper but not in operational reality) that is exactly the kind of gap a hands-on local co-owner is supposed to close. The real risk isn't "does this market exist" — it's execution risk (can you actually win against Payaca/Reonic on the ground) and partnership risk (does a 50/50 structure with a Polish parent actually work in practice — see Part 5).

---

## PART 3 — WHO TO SELL TO, AND HOW TO FIND THEM

### 3.1 Ideal customer profile (first beachhead) ⚠️
Start narrower than "all UK installers." Recommended first segment: **MCS-certified solar PV and/or heat pump installers with 10–50 employees**, i.e. past the "WhatsApp and a spreadsheet" stage but too small to have already signed a 3-year Payaca/Commusoft contract with switching costs. This matches RRUP's own pricing curve (the per-seat discounts kick in meaningfully at 11+ and 21+ users) and is the fastest-growing part of the installer base per the MCS data (new entrants riding the 2026 +50% growth wave).

### 3.2 Where the leads actually are — concrete, checkable sources
| Source | What it gives you | Status |
|---|---|---|
| **MCS Installation Database** (`certificate.microgenerationcertification.org`) | The public, government-linked directory of every MCS-certified installer in the UK — this is the single best-qualified, lowest-cost list you can build a cold outreach campaign from, because every entry is by definition your ICP (certified, active, installing now). | ✅ Public, confirmed live |
| **Companies House SIC-code search** | Free filtering of all UK-registered companies by industry code (construction, renewable energy installation, HVAC) — cross-reference against MCS data to find companies not yet MCS-listed (newer entrants, worth an early relationship). | ✅ Free, public (`resources.companieshouse.gov.uk/sic/`) |
| **Paid B2B data providers** (B2B Data Scout, Prospect360, More Than Words) | SIC-code and company-size filtered contact lists with decision-maker names/emails, ~95%+ accuracy claimed. Useful to accelerate outreach once you know your ICP precisely; not a substitute for the free MCS/Companies House sources for this specific niche. | 📊 Commercial, cost not yet confirmed — get quotes before committing |
| **RECC and HIES** (the mandatory consumer-protection codes every MCS installer must join) | Trade-body partnership/sponsorship opportunities — a joint webinar, newsletter mention, or partner-directory listing with RECC/HIES reaches your entire ICP at once and carries third-party credibility. | ✅ Real, verified bodies — worth a direct partnership conversation |
| **Futurebuild** (12–14 May 2026, ExCeL London) | 26,590 visitors, 450 exhibitors, sustainable-construction focus — broader than solar/heat pump but strong for the construction-vertical CRM angle. | ✅ Confirmed dates/scale |
| **Solar & Storage Live UK** (22–24 Sept 2026, NEC Birmingham) | 20,000+ solar/storage professionals, 500+ exhibitors, and specifically a **"Meet the Installers" zone** — this is as close to "your exact ICP walking past a stand" as UK trade shows get. | ✅ Confirmed dates/scale |
| **InstallerSHOW** (23–26 June 2026, NEC Birmingham) | The UK's largest installer event across heat/water/air/energy trades — **1,000+ exhibitors, 40,000+ visitors**, broader than solar/heat pump alone (plumbing, electrical, renewables). Bigger reach than Solar & Storage Live, less renewables-specific. | ✅ Confirmed — found via your own Document 4, independently verified |
| **RRUP's own EU customer base** | Any existing customers with UK operations, or EU installers expanding into the UK themselves, are a warm-referral channel RRUP can open doors to directly — ask them. | ❓ Ask RRUP directly |
| **MCS register + LinkedIn cross-reference** | Systematically cross-referencing the MCS installer database against LinkedIn to identify named Managing Directors/Operations Directors at each firm — turns an anonymous company list into an actual outreach target list with real names. | ⚠️ Sound method (from your Document 4), manual/semi-automated effort required — check MCS's terms of use before any automated scraping |

### 3.3 How you actually secure them — the pitch motion ⚠️
1. **Lead with the free 30-day trial** — RRUP already offers this in Poland; carrying it to the UK removes the biggest first-call objection ("prove it works before I switch off my spreadsheet").
2. **Open with the vertical-specific angle, not "we're a CRM."** "Built specifically for solar and heat pump installers, not adapted from a generic trade tool" is a sharper hook than competing head-on with Payaca on features you haven't verified you match.
3. **Use the MCS-compliance and commission-automation hooks** as the two concrete pains to lead with — paperwork/compliance burden and manual commission calculation are named, specific frustrations for growing installer businesses, and both map directly to features RRUP already has.
4. **Reference-sell as soon as you have 2–3 UK logos** — the Polish testimonials prove the product works, but a UK installer will trust a UK peer's name far more; get your first few customers to agree to a case study early and use it aggressively.
5. **Trade-show presence + MCS/RECC channel partnership** does the "who do I even call" problem for you at scale, while cold outreach against the MCS database does the immediate pipeline-filling in month one.

---

## PART 3B — HOW YOU ACTUALLY RUN IT (operational build-out, from your own Documents 1/3, audited and kept)
This is the part of your existing material that needed the least correction — it's sound operator thinking. Kept largely as you had it, with the personnel specifics (i.e. "Bart") stripped out.

### 3B.1 The lean launch pod ✅ (structure) / ⚠️ (comp numbers — illustrative, not costed)
A 3-role team under you, rather than hiring ahead of revenue:

| Role | Core function | Weekly metric |
|---|---|---|
| **Outbound SDR** | ABM + cold outreach targeting Tier-2 contractors (£5–50M revenue) across North West/Midlands/Yorkshire | ~40–60 outreaches/day |
| **Vertical Account Executive** | Runs vertical-specific demos, CPQ/pricing walkthroughs, contract close via e-signature | 10–15 demos/week |
| **Technical Implementation Consultant ("Personal Tutor")** | Owns the 30-day onboarding window — legacy data migration, compliance config, field-crew training. Protects retention, not sales-comped. | 80%+ trial-to-paid conversion |

Sourcing pools suggested in your originals are reasonable: SDR from UK trade-merchant/outbound backgrounds, AE from UK renewables/HVAC/trade-software sales, Technical Consultant from field-service-management implementation backgrounds. **The specific comp numbers (base+bonus tiers, equity pool %) in your documents are illustrative placeholders, not verified market rates — benchmark UK SaaS SDR/AE comp before using them in an actual job offer.**

### 3B.2 The 30-day onboarding framework ✅ (structure — genuinely addresses a real, named CRM-industry problem)
Matches RRUP's own 30-day free trial exactly, and directly targets the well-documented pattern that most CRM churn happens in the first 30 days from poor data migration and low adoption:
- **Days 1–7:** legacy data ingestion — pull the prospect off spreadsheets/WhatsApp/whatever they're using now, migrate historic customer records.
- **Days 8–21:** configure the client's specific pricing catalogs, CPQ rules, and UK compliance workflows (MCS/DNO/ECO4 fields) into the system.
- **Days 22–30:** live field-crew and office-admin training, verify mobile/photo sync, confirm adoption before the trial ends.

### 3B.3 90-day phased setup roadmap ✅ (structure, sequencing is sound)
- **Days 1–30:** legal entity + co-working office (Manchester — Spinningfields/Ancoats were named, sensible low-capex options), GBP/VAT configuration, UK regulatory template ingestion (MCS/ECO4/DNO fields).
- **Days 31–60:** hire the pod, two-week onboarding, launch ABM outreach across North West/Midlands/Yorkshire, first wave of trial sign-ups.
- **Days 61–90:** activate the onboarding framework for all live trials, integrate with Xero/Sage/QuickBooks (the UK SME accounting tools that matter — this part is accurate; those three do dominate UK SME cloud accounting).

**Manchester as the hub is a defensible choice independent of anything fabricated** — it's a genuine, verified regional beachhead: Greater Manchester's 2038 carbon-neutral target (12 years ahead of the national 2050 date) is real and confirmed directly by the Greater Manchester Combined Authority, and it does correlate with real trade-contractor density in the North West. Worth keeping as the launch city.

---

## PART 4 — MONEY: WHAT THIS COSTS AND WHERE IT COMES FROM

### 4.1 What it will likely cost to get to first revenue ⚠️ (framework — needs your real cost assumptions)
Rough categories to budget, not fabricated totals:
- **UK company formation & legal** (Companies House registration, shareholders' agreement drafting — see Part 5) — a few thousand pounds in solicitor fees for a properly drafted JV agreement; this is not a place to cut corners given the deadlock risk of 50/50 structures.
- **Your own working capital / salary** during the pre-revenue ramp — however many months you need to cover personally before the UK arm is cash-flow positive.
- **Sales & marketing** — trade show stand costs (Futurebuild/Solar & Storage Live — get exhibitor quotes directly, not found in this research pass), any paid data lists, initial website/localisation costs for a genuinely UK-operational SalesOps CRM presence.
- **Localisation/product costs** — UK-specific requirements (MCS-compliant proposal templates, GBP invoicing/VAT handling, UK data protection/GDPR-UK compliance) — some of this may already exist if the SalesOps CRM site/product has UK-specific work already done; confirm with RRUP rather than assuming from scratch.

### 4.2 Funding routes actually available to you ✅
| Route | Detail | Fit for this deal |
|---|---|---|
| **UK Start Up Loan** (British Business Bank / gov.uk) | £500–£25,000 **per person** (unsecured personal loan), up to £100,000 total if up to 4 partners/directors each apply; fixed interest **7.5%** (rose from 6% in April 2026); 1–5 year repayment; no application fee; includes free business-plan support and 12 months free mentoring; eligible even if you've traded up to 60 months. | ✅ Directly accessible to you now, doesn't require RRUP's involvement, and the free mentoring/business-plan support is genuinely useful for a first-time UK JV operator. Good first step regardless of what else you pursue. |
| **SEIS/EIS investment** | ⚠️ **Likely doesn't work for this structure as described.** A foreign parent (RRUP) does not qualify the UK entity for SEIS/EIS merely by owning a UK subsidiary/JV — the *parent itself* would need its own UK permanent establishment, which it doesn't have yet. This is a genuine structural obstacle, not a paperwork detail — flag it to RRUP early if outside angel investment is part of either of your plans, because it changes what kind of ownership/funding structure would even be eligible. |
| **Innovate UK Smart Grants** | UK-registered company requirement is straightforward to meet once the JV entity exists; however, **Smart Grants were paused from January 2025** pending a new support pilot — check current status on the Innovation Funding Service before counting on this. Not reliable to plan around right now. |
| **Alternative/revenue-based lenders, bank business loans** | Standard options once the UK entity has some trading history — not a month-one solution, but worth lining up for month 6-12 growth capital once you have UK revenue and can show traction. |
| **RRUP itself** | The most obvious funding source for a 50/50 JV is the two partners' own capital contribution, split per the equity agreement. ❓ **You need to establish directly with RRUP: what capital (cash, product/IP licence value, existing SalesOps CRM brand/site) they're contributing vs. what they expect from you** — this is foundational and I can't infer it. |

### 4.3 The honest funding recommendation ⚠️
Start with the **Start Up Loan** application in parallel with the JV conversation — it's fast, doesn't depend on RRUP, comes with free mentoring that will sharpen everything in this document, and £25–100k is a realistic bridge for the first 6–12 months of a lean UK launch (you + maybe one early hire, trade show costs, legal fees). Treat SEIS/EIS and Innovate UK as **not currently available** to this structure rather than planning around them, unless RRUP's setup changes.

---

## PART 5 — STRUCTURING THE PARTNERSHIP

### 5.1 What a 50/50 JV needs beyond the equity split ✅
50/50 is colloquially called a "**deadlock**" structure for a reason: neither party can outvote the other, so **every** material decision needs either genuine agreement or a pre-agreed mechanism for when you don't agree. This is standard UK corporate law territory (LexisNexis and Practical Law both have full precedent frameworks for exactly this scenario), and the standard components are:
- **A board with defined "reserved matters"** — decisions (budget approval, borrowing above a threshold, material contracts, senior hires, strategic changes) that explicitly require both shareholders' sign-off, spelled out rather than assumed.
- **A deadlock-breaking mechanism**, agreed *before* you need it — common options: escalation to named senior individuals at each side, mediation, independent expert determination for technical/product disputes, or (as a last resort) a buy-sell/"Russian roulette" clause forcing one side to buy the other out at a fair price if deadlock is unresolved.
- **Clear IP/licensing terms** — does the UK JV own SalesOps CRM's UK brand and customer relationships outright, or license the product from RRUP in Poland? This materially affects what happens if the partnership ever ends, and is exactly the kind of term that needs to be right from day one, not retrofitted after a dispute.
- **An exit mechanism** — how either party can sell their stake, what happens if one party wants out, valuation method for buy-out.

### 5.2 What I can and can't do here
I can lay out these options and risks (done above) and help you prepare intelligent questions for RRUP and for a solicitor. **I should not draft actual shareholders' agreement terms as if they were legal advice** — this genuinely needs a UK corporate solicitor experienced in cross-border JVs before anything is signed, consistent with the same discipline used throughout this project (no fabricated legal/financial instruments presented as settled). Budget for this properly; it is not the place to economise given how much a badly-structured 50/50 can cost you later.

### 5.3 Questions to put to RRUP directly ❓
0. **Which deal is this, actually — equity co-ownership of a UK operating company, or a commission/agency arrangement with no equity?** (See Part 0.2 — your own prior documents describe both, and everything downstream of this — legal structure, funding options, liability, whether Start Up Loans or SEIS/EIS are even relevant — depends on the answer. Resolve this first, before any of the other questions.)
1. What exactly does each side contribute — cash, the RRUP CRM product/IP licence, the existing SalesOps CRM brand and any UK web presence/leads already generated, your time/operational role?
2. Who owns the UK customer contracts and data if the partnership ends?
3. Does RRUP intend to provide any UK-facing product localisation (MCS-compliant templates, GBP/VAT handling) or is that entirely your build?
4. What's RRUP's expectation for how fast the UK arm reaches profitability, and what happens if it takes longer?
5. Has anyone at RRUP already generated the SalesOps CRM UK-market marketing copy/claims I found — and if so, is there any existing UK pipeline, however small, that transfers to you?
6. **Can you substantiate the Polsat reference?** — asked directly, neutrally, and early (see Part 0.1). If it's real, it's a genuinely powerful asset and you should get the case-study detail properly. If RRUP can't substantiate it, you need to know that now, not after you've said it to a prospect.

### 5.4 Technical due-diligence questions for RRUP's technical team ✅ (from your own Document 5 — genuinely good, kept as-is)
Your technical briefing deck (the Polish-language pptx) asked exactly the right category of hard questions before committing — these hold up under audit and are worth asking verbatim in a technical call with RRUP's engineering team, translated here:
1. **SAP/API integration:** How are your REST APIs or web-service schemas optimized for real-time transfer of finalized contracts, project tokens, and e-signatures into a SAP S/4HANA database without transactional latency?
2. **Data migration tooling:** What ETL tools or standardized bulk-migration scripts does your engineering team use to safely map historical customer metrics from HubSpot/Salesforce/spreadsheets into SalesOps?
3. **Offline field sync:** How does the local browser storage/offline sync engine protect data integrity and prevent file loss for field technicians working in low-signal UK areas, before the office dashboard next updates?
4. **CPQ localization depth:** How modular is the pricing/calculation logic for adapting to UK-specific technical metrics — BTU units, heat pump COP coefficients, regional roof-pitch/shading factors for solar?
5. **Regulatory automation depth:** Are the MCS/ECO4/DNO "Procedure Patterns" hard-coded configuration templates, or does the implementation team build them from scratch per client? (This materially affects your onboarding speed and cost.)
6. **Database/photo-storage performance at scale:** How is the central cloud repository built to handle high-volume multi-tier photo galleries with permission controls as the UK user base grows, without degrading real-time search/query speed?
7. **Onboarding telemetry:** What user telemetry or activity thresholds does RRUP monitor in the first 30 days that signal successful adoption, and can your team access this data to catch at-risk trial accounts early?
8. **Data residency/GDPR:** Will the UK operation run on a fully isolated, local multi-tenant cloud environment, or share instances with existing continental European data centres? This is a real UK GDPR question with a real compliance answer needed, not a formality.
9. **Technical debt guardrails:** What technical guardrails need to be established early to prevent configuration debt that would slow future system updates?
10. **Team-scaling permissions:** Do user access/permission levels allow cleanly isolating a prospecting environment from core sales data as the team grows past the initial pod (e.g. past the ~£100k ARR mark), without system changes?
11. **The Polsat question, asked properly:** From a systems-architecture perspective, how was any large-scale deployment (naming Polsat specifically, if RRUP raises it) scaled across corporate divisions on the RRUP core, and what database/field-crew-coordination bottlenecks did the technical team have to solve? — **This is the right way to raise Polsat: as a question for RRUP to answer, not a claim you make first.**

---

## PART 6 — WHAT'S STILL BLOCKING A SHARPER VERSION OF THIS

1. **Which deal structure is real** (Part 0.2 / 5.3 Q0) — the single highest-priority open item. It changes almost everything downstream.
2. **Whether Polsat is real** (Part 0.1 / 5.3 Q6) — do not repeat this claim anywhere until answered.
3. **CRM demo access** — still a major unblock. Once `demo.salesopscrm.com` is reachable (it's currently down at the infrastructure level, independent of anything on my side — see earlier), a real feature-by-feature comparison against Payaca and Reonic becomes possible, which sharpens Parts 1.6, 2.3, and the whole pitch playbook from thesis to fact.
4. **The salesopscrm.com UK site itself** — blocked by bot protection to automated fetches; if you can view it yourself and paste back the text (pricing page, any UK-specific case studies, any team/contact info), I can fold it in directly.
5. **Real deal terms with RRUP** — Part 5.3's questions 1–5.
6. **Your own capital/runway position** — how much of the Start Up Loan or personal capital you're realistically able/willing to commit shapes the whole Part 4 plan.

---

## What I did NOT do here (honesty discipline, carried from the method playbook)
- No fabricated revenue projections, headcount plans, or funding amounts presented as decided — every number above is either sourced (✅/📊) or explicitly flagged as a framework/estimate (⚠️) needing your input.
- No legal drafting of JV terms — options and risks only.
- No claims about SalesOps CRM's actual UK feature set beyond what's publicly inferable from the identical Polish product — competitive claims stay conditional until the demo is verified.
