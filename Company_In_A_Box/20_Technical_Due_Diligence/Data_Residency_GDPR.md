---
title: Technical Due Diligence — Data Residency & GDPR
subtitle: Confirming the data architecture supports UK GDPR compliance.
pack: Pack 20 — Technical Due Diligence
purpose: Verify where data lives and how transfers are handled, to close the compliance loop.
status: Build-now · Question set
reading_time: 3 min
date: July 2026
---

<div class="bluf"><span class="lbl">Bottom line up front</span><br>
The compliance plan (Pack 15) needs one technical fact confirmed: <b>where UK customer data physically resides and how UK→EU transfer is handled</b>. Get this from RRUP's team so the DPA and cross-border mechanism (Pack 15) are built on reality, not assumption.</div>

## Data residency & GDPR questions

1. Will the UK operation run on a fully isolated, local (UK/EU) multi-tenant environment, or share instances with existing continental European data centres?
2. Where does UK customer personal data physically reside, and what transfer mechanism covers any UK→EU flow?
3. What security measures (encryption, access controls, tokenisation) protect personal data at rest and in transit?
4. Can RRUP support the DPA terms and data-subject-rights processes UK GDPR requires (Pack 15)?

<div class="warn"><span class="lbl">This closes the compliance loop</span><br>
The compliance pack (Pack 15) specifies the obligations; this confirms the technical reality that makes them satisfiable. The two must match — a DPA that assumes UK residency when data sits in the EU is worthless. Confirm before signing the DPA.</div>

## Implication

These answers let the solicitor (Pack 14) draft a DPA and transfer mechanism that actually fit the architecture — turning the compliance plan from paper into practice.

## Sources & confidence

| Claim | Source | Confidence |
|---|---|---|
| EU server location | inferred from RRUP being Polish | ⚠️ Confirm |
| GDPR obligations | ICO | ✅ Verified |
