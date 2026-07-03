# MDR Devices — Live Demo Build Log (VERIFIED · v2 "pitch-centerpiece" build)
**Instance:** https://mdr-devices-test.odoo.com · Odoo saas-19.3 Enterprise trial · Company renamed: **MDR Devices Medizintechnik GmbH** (every screen now carries the client's name)
**Status:** every line read back from the live database via API; every control marked 🔴 was **fire-tested** (a real blocked/routed transaction, then cleaned up). Six controls, six tests, six passes.

Use this as your demo walkthrough — the section order below is a natural pitch order.

---

## The one-breath story of what's in the box
A raw titanium lot arrives and is *automatically* quarantined with a 90-day hold it cannot escape; implants are manufactured with full serial-level UDI traceability back to that lot; a sales order physically cannot confirm against an expired surgeon; consigned implants sit at the hospital while staying on MDR's books; a cancelled surgery flows back through a documented return disposition; instrument trays count their own sterilization cycles and refuse to ship at end-of-life; and every invoice carries a three-dimensional analytic key back to the clinical event. **All of it live. None of it mockups.**

---

## A. Credential gate — Slide 6 🔴 FIRE-TESTED (block) + 🔴 FIRE-TESTED (routing)
- **Dr. M. Feldmann** (Expired, cert to 30 Apr 2026) → confirming his order raises: *"Blocked — HCP certification expired or invalid for Dr. M. Feldmann. Order cannot be confirmed (MDR credential gate)."*
- **Dr. A. Weber** (Validated) → S00002 confirmed, delivered, invoiced. The gate passes good orders.
- **Dr. S. Okafor (Locum — Pending Verification)** → order **S00004 confirms but is routed**: a "HCP credential verification required" activity lands in the review queue and the order chatter logs the routing. This is the exact locum behaviour the architecture documents promise (TC-16) — a hard block would be wrong, and the demo shows you know the difference.
- **Demo moves:** open S00001 (Feldmann, draft) → Confirm → screenshot the block · open S00004 → show the review activity + chatter message.

## B. 90-day quality hold — Slide 8 🔴 FIRE-TESTED
- Receipts auto-route to **WH/Quarantine**; the inbound Quality Control Point generates a check on every receipt (2 passed on record).
- **New lots get their hold date automatically** — automation stamps receipt + 90 days on every new raw lot (no human remembers anything).
- **LOT-2607-B: 10 units, held until 01 Oct 2026.** Attempting release raises: *"GxP quarantine gate — quality hold active for lot LOT-2607-B until 2026-10-01."* LOT-2607-A (hold elapsed) sits released beside it — both states visible.
- **Demo moves:** lot form of LOT-2607-B (hold date in the MDR Compliance section) → attempt internal transfer → screenshot the block.

## C. UDI + full genealogy — Slide 7
- Serials SN-HC-0001/2/3 carry DI `04012345678901`, PI batch `LOT-2607-A`, PI serial, sterility expiry, UDI source = Scanned (GS1) — in a dedicated **"MDR Compliance — UDI & Quality"** section on the form.
- **Demo move:** any serial → **Traceability** button → one report: vendor lot → quarantine → manufacturing order → serial → consignment/patient/return. The single most powerful screen in the demo.

## D. Consignment on-book at the hospital — Slide 10 / CEO question
- **SN-HC-0002 at `WH/Consignment/Klinikum München`** — internal location, still MDR's inventory while physically at the hospital.
- **Demo move:** location hierarchy + quants filtered on Consignment.

## E. Reverse flow, Stage 4B — the "what about returns?" answer, LIVE
- **SN-HC-0003**: manufactured (WH/MO/00004, consumed LOT-2607-A), consigned to the hospital, then **returned** — surgery cancelled — into **WH/Quarantine/Returns**, with disposition logged on the lot: **Re-Quarantine**, reason *"Surgery cancelled — packaging intact, within sterility window; fresh quality check required before restock."*
- Traceability on SN-HC-0003 shows the full loop including the return — the chain shows the return, not a gap.
- **Demo move:** SN-HC-0003 lot form (disposition + reason fields) → Traceability report.

## F. Instrument tray asset loop — 🔴 FIRE-TESTED (reuse-limit block)
- **TRAY-A-001**: cycle **1 of 50**, sitting in Sterilization; cycles now **auto-increment** on every entry into the sterilization location; QCP *Autoclave Cycle Verification* gates each cycle (parameters + second-person countersign in the check notes).
- **TRAY-B-001**: the end-of-life prop — **50 of 50 cycles**. Dispatching it raises: *"Reuse limit reached — tray TRAY-B-001 has completed 50 of 50 sterilization cycles. Dispatch blocked; route to retirement."*
- **Demo moves:** both tray forms side by side (1/50 vs 50/50) → attempt to dispatch TRAY-B-001 → screenshot the block.

## G. Multi-payer settlement — Slide 9
- **Posted:** INV/2026/00001 — Klinikum München Ost, €4,850, invoice line tagged across all three analytic plans (Cost Center: Orthopedics-KMO · Payer Type: GKV · Product Line: HipCore) at 100%.
- **Extension-layer preview (draft, labeled as such):** a settlement split pair for the same surgery — **AOK Bayern (insurer, 90%)** + **M. Schneider (patient co-pay, 10%)** — two invoices, two partners, **one shared analytic key**. Say it precisely: the analytic spine is native and live; generating this split automatically is the named extension. (Draft amounts show the trial's default tax — inert for the demo.)
- **Demo move:** the three invoices in one list view (one posted, two drafts sharing the reference "Settlement split — Surgery SN-HC-0001"), then one invoice line's analytic widget.

## H. Purchasing — auto-replenish off post-hold stock
- Reordering rule: raw material min 10 / max 50 **scoped to WH/Stock** — held stock never counts toward replenishment. This is the literal answer to the case's auto-replenish sentence.

---

## The six fire-tested controls (your Q&A ammunition)
| # | Control | Result |
|---|---|---|
| TC-01 | Expired-credential order block | 🔴 BLOCKED, exact banner captured |
| TC-16 | Locum → review queue, not hard block | 🔴 ROUTED, activity created |
| TC-05 | Quarantine hold release block | 🔴 BLOCKED, lot stays held |
| TC-14 | Tray reuse-limit dispatch block | 🔴 BLOCKED at 50/50 cycles |
| — | Valid order passes the gate | ✅ S00002 confirmed → invoiced |
| — | Auto-hold on new lots / auto cycle count | ✅ automations live |

## Honest boundaries (state them — they're pitch material)
- Field Service app unavailable on this trial tier → consumption demoed via inventory moves; production build uses FSM "Surgery Complete" as the trigger.
- The payer split runs as a labeled draft preview → in production it's the named Category 5 extension.
- These trial automations stand in for the extension layer → production versions get GAMP Cat 5 validation and the two-step release gate.

## Screenshot shot-list (12 shots, capture this week — trial expires)
1. S00001 Confirm → red credential block · 2. Dr. Feldmann form (credential section) · 3. S00004 review activity (locum routing) · 4. LOT-2607-B hold date · 5. Blocked quarantine release · 6. SN-HC-0001 UDI section · 7. Traceability report (KEY) · 8. Consignment quant at Klinikum · 9. SN-HC-0003 return disposition · 10. TRAY-B-001 50/50 + dispatch block · 11. Three-invoice settlement list + analytic widget · 12. Inventory dashboard with "MDR Devices Medizintechnik GmbH" in the header.

**Closing line you've earned:** *"Every control on these slides is enforced in a live system I built and tested — I can show you any of them right now."*
