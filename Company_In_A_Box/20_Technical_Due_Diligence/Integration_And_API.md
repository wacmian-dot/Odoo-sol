---
title: Technical Due Diligence — Integration & API
subtitle: Confirming the integration capabilities the sales strategy depends on.
pack: Pack 20 — Technical Due Diligence
purpose: Verify the API/integration depth behind the SAP co-existence and accounting-sync claims.
status: Build-now · Question set
reading_time: 4 min
date: July 2026
---

<div class="bluf"><span class="lbl">Bottom line up front</span><br>
Two sales strategies depend on integration: the <b>SAP system-of-engagement</b> play (Pack 09) and <b>accounting sync</b> (Xero/Sage/QuickBooks). Confirm the API can actually deliver these before promising them — the open API is verified to exist (Pack 02), but the specific integration depth is not.</div>

## Integration & API questions

1. How are the REST APIs / web-service schemas optimised for real-time transfer of finalised contracts, project data and e-signatures into an external system of record (e.g. SAP S/4HANA) without transactional latency?
2. What ETL tools / bulk-migration scripts does the team use to safely migrate historical customer data from HubSpot/Salesforce/spreadsheets into SalesOps? (Critical for the 30-day onboarding, Pack 12.)
3. What are the supported/pre-built integrations to UK accounting tools (Xero, Sage, QuickBooks)?
4. For a field technician offline in a low-signal area, how does the local storage/offline sync protect data integrity before the office dashboard updates?

<div class="callout"><span class="lbl">Why this gates the enterprise play</span><br>
The SAP co-existence pitch (Pack 09) is powerful but must not be over-promised. Confirming the real integration depth here is what lets you sell it honestly to Tier-3 prospects — architecture and intent are sound; the specific build must be scoped, not assumed.</div>

## Implication

These answers determine what you can credibly promise on integration (Pack 09) and how smooth onboarding migration will be (Pack 12). Both are commercially load-bearing.

## Sources & confidence

| Claim | Source | Confidence |
|---|---|---|
| Open API exists | rrup.pl | ✅ Verified |
| Specific integration depth | — | 🚩 Verify with RRUP |
