# MDR Devices — Live Demo Build Log (VERIFIED)
**Instance:** https://mdr-devices-test.odoo.com · Odoo saas-19.3 Enterprise trial
**Status:** every line below read back from the live database via API and, where marked, **fire-tested**. This replaces the earlier unverified build log.

Use this as your screenshot/navigation script. Order below = pitch order.

---

## A. The credential gate — Slide 6 (THE money screenshot) 🔴 FIRE-TESTED
- Contacts: **Dr. M. Feldmann** — cert DE-ORT-4471, expiry 30 Apr 2026, status **Expired**. **Dr. A. Weber** — DE-ORT-5512, valid to 2027, status **Validated**. Both show an "MDR credential" section on the contact form.
- Automation: *MDR Credential Gate — Block Confirm on Invalid HCP* (Settings → Technical → Automation Rules).
- **Proven live:** confirming an order for Dr. Feldmann raises: *"Blocked — HCP certification expired or invalid for Dr. M. Feldmann. Order cannot be confirmed (MDR credential gate)."* Order stays draft.
- **Demo move:** open **S00001** (draft order for Dr. Feldmann) → click Confirm → screenshot the red banner. Then show S00002 (Dr. Weber) confirmed cleanly.

## B. The 90-day quality hold — Slide 8 🔴 FIRE-TESTED
- Receipts auto-route to **WH/Quarantine** (receipt operation default destination).
- Quality Control Point *Inbound Implant Material Inspection* generates a check on every raw-material receipt — 2 checks passed on record.
- **LOT-2607-B — 10 units in WH/Quarantine, hold release 01 Oct 2026 (ACTIVE hold).**
- Automation: *GxP Quarantine Hold — Block Release Before Hold Elapses*. **Proven live:** attempting to move LOT-2607-B to stock raises: *"GxP quarantine gate — quality hold active for lot LOT-2607-B until 2026-10-01. Release to stock is blocked."*
- LOT-2607-A (hold elapsed) sits released in WH/Stock ×18 — held and released states visible side by side.
- **Demo move:** Inventory → Lots/Serials → LOT-2607-B (show hold date in the MDR Compliance section) → try an internal transfer out of Quarantine → screenshot the block.

## C. UDI on the lot record — Slide 7
- Open any serial (SN-HC-0001/0002): **MDR Compliance — UDI & Quality** section shows DI `04012345678901`, PI batch `LOT-2607-A`, PI serial, expiry (2 yr sterility clock), UDI source = Scanned (GS1).
- **Demo move:** serial form screenshot + click **Traceability** — one report: LOT-2607-A (vendor) → quarantine → production → SN-HC-000x → consignment/patient. This single screen answers "show me full traceability from raw material to patient."

## D. Consignment at the hospital, on your books — Slide 10 / Q&A
- **SN-HC-0002 sits at `WH/Consignment/Klinikum München`** — an internal location, so the implant remains in MDR's inventory while physically at the hospital. Location tree: WH → Stock / Quarantine (→ Disposition) / Consignment (→ Klinikum München) / Sterilization.
- **Demo move:** Inventory → Reporting → Locations (or quants view) filtered on Consignment.

## E. Instrument tray sterilization loop — Slide on the asset loop
- **TRAY-A-001** in WH/Sterilization, **cycle 1 of 50** (limit on the record), own DI. Loop already walked: Vendor → Stock → Consignment → Sterilization.
- Quality Control Point *Autoclave Cycle Verification* gates every internal move of the tray — check notes require cycle parameters + second-person countersign (the two-step gate from the GxP plan).
- **Demo move:** tray serial form (cycle count/limit) + the QCP definition.

## F. Consumption → invoice → 3-plan analytics — Slide 9
- SN-HC-0001 consumed ("surgery complete") → **S00002** (Klinikum München Ost / Dr. Weber) → **INV/2026/00001 posted, €4,850**.
- Invoice line carries **all three analytic plans at 100%**: Cost Center = Orthopedics-KMO · Payer Type = Statutory Insurer (GKV) · Product Line = HipCore Implant Line. (Say it precisely in the pitch: the analytic spine is native; the payer-*split* invoicing is the named extension.)
- **Demo move:** invoice form, analytic distribution widget on the line.

## G. Auto-replenishment off post-hold stock — Purchasing answer
- Reordering rule: raw material **min 10 / max 50, scoped to WH/Stock** — quarantined stock does NOT count toward replenishment, exactly as the architecture documents claim.

## Honest boundaries (say these, don't hide them)
- **Field Service app isn't available on this trial tier** — consumption was demonstrated via inventory moves; in the real build, FSM "Surgery Complete" is the trigger.
- The payer split (insurer + co-pay from one event) is **extension-layer** — the demo shows the native analytic spine only, which is exactly what the corrected documents claim.
- These automations are the trial-grade stand-ins for the extension layer — in production they'd be validated at GAMP Cat 5 with the two-step release gate.

## Screenshot shot-list (capture this week — trial expires)
1. S00001 confirm attempt → red credential block (Slide 6)
2. Dr. Feldmann contact form, MDR credential section (Slide 6 inset)
3. LOT-2607-B lot form — active hold date (Slide 8)
4. Blocked quarantine transfer error (Slide 8)
5. SN-HC-0001 serial form — UDI section (Slide 7)
6. Traceability report from the serial (Slide 7/10 — KEY)
7. Consignment location with SN-HC-0002 (Slide 10)
8. TRAY-A-001 — cycle 1/50 (asset loop slide)
9. INV/2026/00001 — 3-plan analytic line (Slide 9)
10. Inventory dashboard overview (Slide 10)

After capture: deck captions change from "mockup" to **"live in sandbox"** — and your Objection 7 answer becomes: *"zero Odoo projects in production, three ERP lifecycles, and every claim in this deck is running in a sandbox I can show you right now."*
