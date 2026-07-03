# Odoo Trial Demo Build — Agent Execution Runbook
## "The Compliant Digital Thread" — live demonstration instance for the MDR Devices pitch

**Purpose:** Build, inside a standard Odoo Online trial, a working demonstration of every claim in the pitch — so slides 6–8 carry *real* screenshots and the presenter can say "this is running in a sandbox I built."
**Executor:** AI agent via browser automation (Playwright/Chromium), or Waqas manually following the same steps.
**Prerequisites from Waqas:** trial instance URL (`https://<yourname>.odoo.com`), login email + password, confirmation the trial is Odoo Online (default from odoo.com/trial) and which version it reports (Settings → About). Change the password after the agent session if you wish.
**Time estimate:** agent ~60–90 min including screenshots; manual ~3–4 hrs.
**Ground rule (matches the pitch's honesty discipline):** anything the trial *can't* do natively gets configured as far as native allows and the boundary is recorded — those boundaries ARE pitch material ("this is where the named extension layer starts").

---

## Phase 0 — Instance preparation (10 min)

**0.1 Install apps** (Apps menu, search + Activate each):
Sales · CRM · Inventory · Purchase · Manufacturing · Quality · Accounting (or Invoicing) · Barcode · Field Service · **Studio** (this is what makes custom fields/automations possible; included in trials).

**0.2 Enable settings** (Settings → per-app section, Save after each block):
- Inventory: **Lots & Serial Numbers** ✓ · **Expiration Dates** ✓ · **Storage Locations** ✓ · **Multi-Step Routes** ✓
- Accounting: **Analytic Accounting** ✓ (then Configuration → Analytic Plans: create plans `Cost Center`, `Payer Type`, `Product Line`)
- General: company name → **MDR Devices Medizintechnik GmbH** (Settings → Companies), currency EUR.

**Acceptance check:** Inventory → Configuration menu shows "Locations" and "Routes"; a product form shows a Traceability section.

## Phase 1 — Master data (15 min)

**1.1 Locations** (Inventory → Configuration → Locations, remove default filter):
| Location | Parent | Type |
|---|---|---|
| `WH/Quarantine` | WH | Internal |
| `WH/Quarantine/Disposition` | WH/Quarantine | Internal |
| `WH/Consignment` | WH | Internal |
| `WH/Consignment/Klinikum München` | WH/Consignment | Internal |
| `WH/Sterilization` | WH | Internal |

**1.2 Products:**
- **HipCore Ti-64 Femoral Stem** — storable, Tracking: *By Unique Serial Number*, Expiration Dates ✓ (Expiration 730 days), route: Manufacture, Buy on component. Internal ref `IMP-HC-001`.
- **Ti-6Al-4V Rod Stock (Raw)** — storable, Tracking: *By Lots*, Buy route, vendor = supplier below, reordering rule min 10 / max 50 **with location = WH/Stock** (this is the "reorder off post-hold stock" demo point).
- **Instrument Tray — Hip Set A** — storable, Tracking: *By Unique Serial Number*.
- BoM: HipCore Stem = 1 × Ti Rod Stock (Manufacturing → Products → Bills of Materials).

**1.3 Partners:**
- **OrthoAlloy GmbH** (vendor).
- **Klinikum München Ost** (customer, company).
- **Dr. M. Feldmann** (individual, linked to Klinikum) — the demo's *expired* physician.
- **Dr. A. Weber** — the *valid* physician.

**Acceptance check:** all locations visible in hierarchy; both doctors exist.

## Phase 2 — Credential gating (Slide 6 · the money demo) (20 min)

**2.1 Studio fields on Contact** (open Dr. Feldmann → toggle Studio (top-right) → drag fields onto the form):
- `x_hcp_certification_number` — Char, label "HCP Certification #"
- `x_hcp_certification_expiry` — Date, label "Certification Expiry"
- `x_validation_state` — Selection [Draft / Validated / Expired / Suspended / Pending Verification], label "Credential Status"

Set data: Feldmann → cert `DE-ORT-4471`, expiry **2026-04-30** (past), status **Expired**. Weber → cert `DE-ORT-5512`, expiry 2027-12-31, status **Validated**.

**2.2 Blocking automation** (Settings → Technical → Automation Rules, or Studio → Automations, on model *Sales Order*):
- Trigger: **On state change / when order is confirmed** (v17+: trigger "Sales Order" → "On save" with condition state = sale, or use the "Confirmation" trigger if offered).
- Action: **Execute Code** (available with Studio on Online) — pseudo-logic:
  ```python
  for order in records:
      p = order.partner_id
      if p.x_validation_state in ('expired','suspended') or (p.x_hcp_certification_expiry and p.x_hcp_certification_expiry < datetime.date.today()):
          raise UserError("Blocked — HCP certification expired or invalid for %s. Order cannot be confirmed (MDR credential gate)." % p.name)
  ```
- **Fallback if Execute Code is unavailable on the trial:** trigger "On save" + filtered domain, action "Create Activity / Send Warning" — and record this as an extension-layer boundary (it literally proves the pitch's "five-line server action" claim).

**2.3 Demo script:** create SO for Dr. Feldmann, 1 × HipCore Stem → click Confirm → **red error banner**. 📸 **SCREENSHOT A (Slide 6).** Then same order for Dr. Weber → confirms cleanly. 📸 **SCREENSHOT B** (contact form showing credential fields).

## Phase 3 — Quarantine & quality hold (Slide 8) (20 min)

**3.1 Route stock to quarantine:** Inventory → Configuration → Operations Types → Receipts → set default destination = `WH/Quarantine` (simplest reliable method in a trial; push-rule alternative noted for discovery).

**3.2 Quality Control Point** (Quality → Quality Control → Control Points): title "Inbound Implant Material Inspection", operation = Receipts, product = Ti Rod Stock, type = Pass-Fail, instructions "Visual inspection · temperature log review · CoA verification".

**3.3 The 90-day hold:** Studio field on Lot/Serial (`stock.lot`): `x_hold_release_date` — Date, label "Quality Hold Release". Automation on lot creation: set = today + 90 days (or set manually during demo — visible is what matters). Optional stretch: automation rule blocking internal transfers from Quarantine when today < release date; if trial permissions block it, the *visible hold date + named boundary* still demos well.

**3.4 Demo script:** PO to OrthoAlloy for 20 rods → Receive → assign lot `LOT-2607-A` → quality check appears → **Fail** one demo run (shows deviation path), **Pass** the real run → stock sits in `WH/Quarantine` with a release date 90 days out. 📸 **SCREENSHOT C** (quality check on receipt) · 📸 **SCREENSHOT D** (lot record with hold release date + expiry — also feeds Slide 7).

## Phase 4 — UDI on the lot (Slide 7) (10 min)

Studio fields on Lot/Serial: `x_udi_di` (Char, "UDI — Device Identifier"), `x_udi_pi_batch`, `x_udi_pi_serial`, `x_udi_pi_expiry` (Date). Manufacture 2 HipCore stems (MO consumes LOT-2607-A → new finished serials `SN-HC-0001/0002`), fill UDI fields: DI `04012345678901`, batch `LOT-2607-A`, expiry 2028-07. 📸 **SCREENSHOT E** — finished serial showing UDI fields **and** the Traceability report (Lot → Traceability button) proving raw-lot → implant chain. That traceability report is the single strongest artifact in the whole demo.

## Phase 5 — Consignment + the flagged sandbox verifications (15 min)

**5.1** Internal transfer: 1 × `SN-HC-0001` from WH/Stock → `WH/Consignment/Klinikum München`.
**5.2 VERIFY (flagged claim #1):** Inventory → Reporting → Valuation — confirm the consigned serial still appears in company valuation while in the consignment location. Record result honestly either way. 📸 **SCREENSHOT F** (location hierarchy + stock at hospital, on-book).
**5.3** Instrument tray mini-loop: transfer tray serial to hospital → back to `WH/Sterilization` → Studio field `x_sterilization_cycle_count` on the serial, increment manually → shows the loop concept. 📸 optional.

## Phase 6 — Consumption → invoice thread (Slides 9–10) (10 min)

Field Service task "Hip Arthroplasty — Klinikum München Ost" for Dr. Weber's confirmed SO; mark done; internal transfer of `SN-HC-0001` to a `Consumed/Customers` location; create the invoice from the SO with analytic distribution set (Cost Center/Payer Type/Product Line). **Record the boundary honestly:** the *automation* consumption→invoice and the payer split are extension-layer — the demo shows the data thread (serial → surgery task → invoice with analytic tags), which is exactly what the pitch claims natively. 📸 **SCREENSHOT G** (invoice with analytic tags) · 📸 **SCREENSHOT H** (Inventory dashboard / overview as the Slide 10 "live picture").

## Phase 7 — Screenshot manifest → deck (10 min)

| Shot | Content | Replaces |
|---|---|---|
| A | SO blocked banner — expired credential | Slide 6 mockup |
| B | Contact form with credential fields | Slide 6 inset |
| C | Quality check on receipt | Slide 8 |
| D | Lot with hold release + expiry | Slide 8 / 7 |
| E | Serial UDI fields + traceability report | Slide 7 |
| F | Consignment location, stock on-book | Slide 10 / Q&A ammo |
| G | Invoice with 3-plan analytic tags | Slide 9 |
| H | Live dashboard | Slide 10 |

Caption change in the deck: "screenshot-style mockup" → **"live in sandbox"**. Update the cue-card beat for Objection 7: "…and I built this in a sandbox — here's what I verified."

---

## Agent execution notes (for the automated run)

1. **Login flow:** navigate to instance URL → /web/login → fill credentials → wait for app grid. Odoo trials sometimes show onboarding banners — dismiss via visible "skip/close" only.
2. **Robustness:** Odoo's UI is JS-heavy; act on visible labels/placeholders, wait for network-idle after each save; after every Studio field creation, reload and confirm the field renders before proceeding.
3. **Order matters:** Phase 0 settings before Phase 1 (lot tracking fields won't exist otherwise); Studio fields before automations that reference them.
4. **Failure protocol:** if any step is blocked by trial limitations, do not fake it — record "native boundary" in the build log with a screenshot of the block; these become pitch material.
5. **Evidence:** save every 📸 as PNG named `slideX_<desc>.png`, plus a build log (step → result → timestamp) so the whole run is auditable — same discipline as the document package.
6. **Safety:** no real personal data in the trial (all names above are fictional); Waqas may rotate the password after the session.

**What I need from Waqas to execute:** (1) instance URL, (2) login email + password, (3) the version shown at Settings → About (or I'll detect it), (4) go-ahead. If the network policy of this environment blocks *.odoo.com, fallback is pair-driving: I give per-step instructions and verify against your screenshots.
