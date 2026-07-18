---
title: Technical Due Diligence — Architecture & Scale
subtitle: The architecture questions to put to RRUP's engineering team.
pack: Pack 20 — Technical Due Diligence
purpose: Verify the platform's scale, reliability and data model before committing.
status: Build-now · Question set (for RRUP technical call)
reading_time: 4 min
date: July 2026
---

<div class="bluf"><span class="lbl">Bottom line up front</span><br>
Before relying on the platform commercially, confirm its architecture holds up: performance at scale, reliability (the demo was down once), and how any large deployment was engineered. These are the right questions to ask RRUP's technical team in a dedicated call — verify, don't assume.</div>

## Architecture & scale questions

1. How does the central cloud repository handle high-volume, multi-tier photo galleries with permission controls as the UK user base grows — without degrading real-time search/query speed?
2. What is the platform's uptime/reliability track record, and what caused the recent demo-instance outage? What's the production SLA?
3. What technical guardrails prevent configuration debt that would slow future updates?
4. How is a large multi-division deployment scaled on the core platform, and what database/coordination bottlenecks were solved? *(If RRUP raises Polsat here, this is the place to ask them to substantiate it — Pack 02, Pack 22 Q6.)*

<div class="warn"><span class="lbl">Reliability is commercial</span><br>
The demo outage during this research is a reminder: platform reliability is not just a technical detail, it's a sales risk (a demo that won't load loses the deal) and a retention risk. Get concrete answers on uptime and support response before scaling on it.</div>

## Implication

These answers confirm (or qualify) the "proven platform" pillar of the positioning (Pack 04). Ask them once a technical point of contact is established — likely after the commercial reset (Pack 22).

## Sources & confidence

| Claim | Source | Confidence |
|---|---|---|
| Question set | derived from prior technical briefing + this research | 📊 Reasoned |
| Demo outage | observed | ✅ Verified |
