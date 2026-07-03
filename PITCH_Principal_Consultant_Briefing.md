# much. Consulting — Principal Consultant Briefing
## Strategic Pitch · Technical Readiness · Operational Improvement Directive
**Client:** MDR Devices Medizintechnik GmbH · **Audience:** CIO & Executive Board
**Alignment note:** every claim in this briefing is consistent with the corrected v2 pitch package and, where marked **[LIVE]**, is already running and fire-tested in the demonstration instance (mdr-devices-test.odoo.com).

---

# TASK 1 — The Pitch Foundation

## 1.1 The Strategic Narrative: A Regulatory & Operational Transformation

MDR Devices does not have a software problem. It has a **coherence problem with regulatory consequences**: four systems of record — QMS, LIMS, field service, legacy ERP — each performing well in isolation, governing a single continuous clinical event none of them can see end to end. Today, "compliant" is enforced by tenure and habit: Sales assumes Quality cleared the lot; Quality assumes Sales won't ship to an uncertified surgeon; nobody owns the white space between systems — and the white space is where audit exposure lives.

This engagement is therefore not an ERP install. It is the construction of **one validated definition of "compliant," end to end — the Compliant Digital Thread** — on which three transformations ride:

- **Regulatory:** EU MDR Article 27 traceability and GxP process control become *structural* (a control exists in the system) rather than *procedural* (staff remembered correctly). Audits shift from weeks of evidence assembly to a same-day system export.
- **Operational:** handoffs that are unwritten today become system-enforced gates: credential-checked order confirmation, automated quarantine, disposition-controlled returns, cycle-limited instrument reuse.
- **Financial:** every invoice, claim and rebate carries a structural key back to its clinical event — reconciliation stops being a spreadsheet exercise, and contractually earned vendor rebates stop leaking.

**The architecture principle we sell:** native Odoo Enterprise wherever the platform genuinely covers the requirement; a precisely named MedTech extension layer where it does not (UDI structuring, recall & consignment depth, multi-payer & rebate settlement, instrument reprocessing, QA dual-release). *We don't sell zero custom code. We sell named custom code.*

## 1.2 Departmental Bridge Table

| Department | Current Siloed Reality | Odoo Integrated Efficiency |
|---|---|---|
| **Logistics** — traceability, sterility, JIT | UDI data re-keyed across systems; sterility windows tracked in spreadsheets; cold-chain evidence scattered; surgery dates communicated by phone/email; a recall means days of manual cross-referencing | One `stock.lot` record carries UDI (DI/PI), sterility clock, cold-chain envelope and full movement genealogy **[LIVE]**; deliveries scheduled against the confirmed surgery date; a recall is a single traceability query — vendor lot → implant → hospital → patient event **[LIVE]** |
| **Sales / CRM** — physician records, consignment | Certification records in a standalone CRM nobody checks at order time; consignment stock at hospitals invisible to finance, counted by fax and goodwill | Order confirmation is **credential-gated**: expired/suspended surgeon → hard block; unknown locum → routed to verification queue **[LIVE, fire-tested]**; hospital consignment modeled as internal locations — visible, counted, and on MDR's balance sheet until consumption **[LIVE]** |
| **Accounting** — multi-stage claims, cost centers | Claims matched to surgeries by hand; cost-center allocation applied after the fact; rebates tracked in spreadsheets and routinely under-collected | Every financial document auto-tagged across three analytic plans (Cost Center / Payer Type / Product Line) resolved at invoice generation **[LIVE]**; payer-split settlement runs in the named extension layer against that native analytic spine; rebate thresholds tracked structurally — *recovery of value already earned, not projected savings* |
| **Purchasing** — quality hold, lead times | The three-month quality hold tracked manually; replenishment triggers off gross stock (including unreleased stock) causing surprise shortages; supplier qualification a binder, not a control | Incoming lots auto-routed to quarantine with the hold date stamped automatically; release **blocked** until quality pass + hold elapse **[LIVE, fire-tested]**; reordering rules scoped to *post-hold* stock only **[LIVE]**; MPS plans long-lead materials against forecast; vendor qualification becomes a PO-confirmation gate (same proven pattern as the credential gate) |

## 1.3 The "Look and Feel" Demo Script — One Implant, Five Steps
*Every step below runs in the live demonstration instance today. Compliance Checkpoints (CC) marked where the system — not a person — enforces GxP.*

| Step | The story | On screen | Compliance Checkpoint |
|---|---|---|---|
| **1. Procurement & Quarantine** | 10 units of Ti-6Al-4V arrive from a qualified vendor as LOT-2607-B | Receipt auto-routes to WH/Quarantine; inspection checklist (visual, storage conditions, CoA) generated automatically; hold date stamped: receipt + 90 days | **CC-1:** stock *cannot* bypass quarantine routing. **CC-2 [fire-tested]:** attempted early release is refused: *"quality hold active until 2026-10-01 — release blocked"* |
| **2. Manufacturing & UDI birth** | Released material becomes implant SN-HC-0003; the serial inherits DI, carries parsed PI, batch link and sterility expiry | Manufacturing order consuming LOT-2607-A; the serial's "MDR Compliance — UDI & Quality" panel; one-click Traceability report showing vendor→implant genealogy | **CC-3:** backward traceability is a database property, not a reconstruction |
| **3. Credential-gated dispatch & consignment** | The implant ships for Dr. Weber's case — but first, the system checks *who is operating* | Confirm an order for Dr. Feldmann (expired cert) → **red block banner**; Dr. Okafor (locum) → order routed to credential review queue; Dr. Weber → confirms; implant sits at WH/Consignment/Klinikum München, still on MDR's books | **CC-4 [fire-tested]:** unqualified physician = order cannot confirm. **CC-5:** consignment valuation is location-driven, audit-defensible |
| **4. The loop nobody else models: sterilization & returns** | A tray returns dirty; a surgery gets cancelled | TRAY-A-001: cycle auto-increments on sterilization entry, autoclave QCP gates redeploy (cycle 1/50); TRAY-B-001 at 50/50 → dispatch refused; SN-HC-0003 returned to WH/Quarantine/Returns with logged disposition "Re-Quarantine — surgery cancelled, packaging intact" | **CC-6 [fire-tested]:** end-of-life tray physically cannot ship. **CC-7:** a return is a documented state in the same lot history — the thread shows the return, not a gap |
| **5. Consumption & financial reconciliation** | Surgery complete → the money follows the clinical event | Consumption move → posted invoice €4,850 carrying all three analytic dimensions; beside it, the settlement split preview (insurer 90% / patient co-pay 10%) — two invoices, one shared analytic key | **CC-8:** finance reconciles structurally against the clinical event; the payer split itself is the *named* extension — stated, not smuggled |

**Closing beat:** *"Nothing you've just seen is a mockup. Every control fired live, and I can re-run any of them right now."*

---

# TASK 2 — Functional Consultant Cheat Sheet

## 2.1 Configuring Odoo as a Gated System

| Gate | Mechanism (precise) | Status |
|---|---|---|
| Inbound quarantine | Receipt operation type default destination → `WH/Quarantine` (internal type — on balance sheet) | **[LIVE]** |
| Inspection checklist | Quality Control Point on the receipt operation auto-generates a `quality.check` (visual / storage conditions / CoA); the receipt cannot validate with an open check | **[LIVE]** |
| Hold enforcement | Automated action stamps `x_hold_release_date = receipt + 90d` on lot creation; a second automation blocks any move out of Quarantine before that date (Disposition route exempted) | **[LIVE, fire-tested]** |
| Credential gate | Automated action on sale-order confirmation: Expired/Suspended or date-lapsed certification → `UserError` hard block; Pending Verification (locum) → confirm + mandatory review activity | **[LIVE, fire-tested both paths]** |
| Reuse limiter | Cycle counter auto-increments on entry to Sterilization; dispatch automation blocks at `count ≥ limit` | **[LIVE, fire-tested]** |
| Vendor/PO gate | Same pattern as the credential gate applied to `res.partner` vendors: qualification state + expiry fields; automation on PO confirmation blocks unqualified vendors | Design-ready (pattern proven twice above) |
| **Digital signatures — the honest line** | Odoo does **not** natively provide dual-authentication e-signatures for quality release. The compliant design is a **two-step release gate**: quality pass by the inspector + a separately permissioned "QA Release" re-authentication by a distinct role, both timestamped and user-attributed in the audit trail — satisfying the dual-control intent of 21 CFR Part 11 / EU GMP Annex 11 (applied as the GxP benchmark). Never claim native e-sig; claiming it is an audit failure waiting to happen. | Cat 5 extension scope |
| Audit trail | `mail.thread` chatter + field-level tracking; archive-only policy on `stock.lot`, `quality.check`, `account.move` — no hard-delete path inside the validated boundary | Native config |

## 2.2 Technical Rebuttals — Expert-Level Q&A

**Q: "We serialize every implant. Will Odoo survive high-volume serial tracking?"**
*A:* "Serial tracking in Odoo is one `stock.lot` row and indexed move lines per unit — the database side scales comfortably into the millions; the real constraint is *capture*, not storage. That's why receipt and consumption are scan-driven through the Barcode app with native GS1 parsing, why we'd batch-generate serials at manufacturing rather than key them, and why the two things I'd actually size in discovery are your scan throughput at goods-in and the traceability report's response time at your real volumes — both testable in the first sprint, on your data, before you've committed to anything."

**Q: "How do you stop purchasing from unqualified vendors?"**
*A:* "Identically to how we stop sales to unqualified surgeons — it's the same proven gate pointed at the other end of the chain. Vendor qualification state and expiry live on the supplier record; a confirmation-time control blocks any PO against an unqualified or lapsed vendor and routes borderline cases to quality review. Qualification evidence attaches to the same record, so the auditor's question — 'show me this vendor was qualified when you bought' — is one click, not a binder."

**Q: "How do you keep custom code from wrecking MDR validation?"**
*A:* "By naming it and starving it. The native core — credential gating, quarantine automation, the analytic spine — is configuration, validated at GAMP Category 4 with risk-based testing. Five named items exceed native capability — UDI structuring, recall/consignment depth, multi-payer & rebate settlement, instrument reprocessing, QA dual-release — and only those five receive Category 5 rigor, each with its own traceability-matrix line and regression tests (TC-01 through TC-19) re-run on every release candidate on an Odoo.sh staging branch before promotion. Your recurring validation cost concentrates in a small, budgeted, named footprint — not smeared invisibly across the platform. We don't sell zero custom code; we sell named custom code."

---

# TASK 3 — Operational Improvement Directive (The Gap Fixer)

## 3.1 Diagnostic: Three Immediate Fixes (pre-go-live, bypassing the fragmented tools)

1. **Stand up the single lot/serial registry first.** Before any module go-live, consolidate lot/serial identity — UDI, sterility window, hold status, current custody — from QMS/LIMS/ERP into the Odoo lot registry as the interim source of truth. Every downstream control depends on this identity being singular; it is also the highest-risk migration object, so it goes first, not last.
2. **Enforce the credential check now, procedurally.** The credential gate is a five-minute system control in Odoo but a zero-day fix as policy: export the physician certification list from the CRM weekly, and make order confirmation conditional on it *today*. When the system gate goes live, it lands as "the rule we already follow, finally automated" — which is also your change-management strategy.
3. **Freeze the informal quality-hold workarounds.** Document the current hold practice (who releases, on what evidence, where recorded), then route every early-release exception through one named quality owner with a written log. This surfaces the true exception rate — data you need to configure the structural gate — and eliminates the audit finding of undocumented releases immediately.

## 3.2 Per-Department Process Improvements

| Dept | Improvement | Manual effort removed | Audit-trail gain |
|---|---|---|---|
| **R&D** | Attach design/change documentation to the product template and BoM version in Odoo (PLM-style), so a device's engineering state is linked to the lots built from it | Chasing "which drawing was current when this lot was made" across drives | Device history documentation references a versioned BoM, not a folder convention |
| **Logistics** | Scan-driven receipt with GS1 parse populating UDI fields automatically (manual-entry fallback flagged `Manual`) | Re-keying DI/PI/batch/expiry at every touch | Scanned vs. hand-entered records distinguishable — data provenance itself becomes auditable |
| **Sales** | Credential status surfaced on the order screen with block/route behaviour **[LIVE]**; consignment counts from system quants, not hospital faxes | Pre-order manual certificate checks; quarterly consignment reconciliation marathons | Every confirmation carries a logged credential decision; consignment custody is continuous record, not periodic estimate |
| **Accounting** | Analytic distribution auto-applied from product category + customer type at invoice generation **[LIVE]** | Post-hoc cost-center journal corrections; claim-to-surgery matching by spreadsheet | Every euro traceable to a clinical event through one structural key — reconciliation becomes a query |

## 3.3 The Pre-Flight Audit — CIO's Data-Reliability Blueprint

**Purpose:** identify which departmental data is *unreliable* before it contaminates a validated system. Run in the 3-week discovery sprint; output feeds the URS and cutover plan.

| Phase | What we test | Method | Red flag threshold |
|---|---|---|---|
| **1. Identity integrity** (Logistics/QMS) | Do lot/serial numbers reconcile across QMS, LIMS, ERP? | Extract all three registries; three-way match on lot ID + product + quantity | >2% orphaned or conflicting lot identities → traceability data quarantined for manual remediation before migration |
| **2. Credential currency** (Sales/CRM) | Are physician certification records current and complete? | Sample 100 active physician records against expiry dates and source documents | >5% expired-but-active or undocumented → CRM data enters Odoo as *Pending Verification*, not *Validated* — the system's own state model absorbs the uncertainty |
| **3. Consignment truth** (Logistics/Finance) | Does booked consignment stock physically exist at hospitals? | Cycle-count the top 10 consignment sites against the ledger | >3% variance → consignment opens in Odoo from a fresh counted baseline, never from migrated balances |
| **4. Open-record hygiene** (Quality) | How many device history records, complaints, CAPAs are genuinely open? | Age analysis; anything dormant >12 months reviewed for formal closure | Dormant records closed in legacy *before* cutover — they never migrate as false liabilities |
| **5. Financial mapping** (Accounting) | Can historic invoices be mapped to cost centers and payers? | Sample mapping of last quarter's invoices to the three analytic dimensions | Unmappable share defines the analytic backfill scope — decided consciously, not discovered in month two |

**Deliverable:** a one-page Data Reliability Scorecard per department (Green = migrate / Amber = migrate with named remediation / Red = rebaseline in Odoo), signed by each business owner — which doubles as the URS evidence base and makes the CIO the owner of *facts* about data quality rather than the referee of departmental opinions.

---
*Prepared in the voice of much. Consulting for interview use. Consistent with pitch package v2 and the live demonstration instance; the honest platform boundaries (e-signature design gate, payer-split extension, Field-Service-on-trial limitation) are stated, not hidden — that candour is the brand.*
