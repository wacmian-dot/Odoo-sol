# REBUILD RUNBOOK — The MDR Devices Demo, Rebuilt 1:1

**A machine-executable master document. An AI executor (Claude, incl. Sonnet 5) with Bash + Python + a fresh Odoo trial API key can run this end-to-end and reproduce the exact demonstration instance that was originally built for the much. Consulting MedTech case — every field, record, date, refusal message, document number, UDI composite and analytic tag identical to the delivered client package.**

The original instance (`mdr-devices-test.odoo.com`, Odoo Enterprise saas~19.3 trial) has **expired**. This runbook was reconstructed from the surviving live-capture snapshot (`regression/*.json`, taken 2026‑07‑05 hours before expiry), the verified build log, and the delivered package. There is no replayable original build script — this document *is* the build script now.

---

## PART 0 · MISSION & OPERATING RULES

### 0.0 What you are building
A single Odoo Enterprise trial instance renamed **"MDR Devices Medizintechnik GmbH"** containing: 7 compliance locations, 3 products, 7 named business partners, 3 sales orders, 7 lots/serials, 3 invoices, 4 enforced automation rules, 2 quality control points, and a full transactional history — such that the 9‑stop live demo (Part 3) runs identically to the original, including three live refusals with byte‑exact error messages.

**Why fidelity is absolute:** the client holds a delivered document package that quotes these exact values (document numbers, dates, the €4,850 invoice, the UDI strings, the refusal texts). Any drift is a visible contradiction in front of the panel. When in doubt, do not improvise — see the STOP‑AND‑ASK list (0.4).

### 0.1 Executor inputs (the ONLY four things the human supplies)
Fill these into `api.py` (Part 1.1). Everything else in this document is fixed.
1. **Instance URL** — e.g. `https://<newname>.odoo.com`
2. **Database name** — usually the subdomain, e.g. `<newname>`
3. **Login email** — the odoo.com account email
4. **API key** — Settings → Account Security → New API Key (on the instance)

The old key (`2d7eb471…`) is DEAD. Never print the odoo.com account password anywhere.

### 0.2 Source-of-truth precedence (when any two facts disagree, higher wins)
1. The embedded **CANONICAL DATASET** in this document (Part 0.5 + Part 4) — mirrors the live‑capture snapshot, this is truth.
2. Delivered package values (Functional Spec, UAT Guide, schema doc).
3. Everything else.
**Record IDs from the old system are void** — a fresh instance renumbers everything. NEVER hardcode a model_id, field_id, or record id from the old system; always resolve by name/lookup.

### 0.3 Exact-as-built-replica scope (USER DECISION — LOCKED)
Build a **1:1 copy of the live demo as it actually was** — nothing more. The delivered *design document* describes 5 extra custom fields that were **specified on paper but never built into the live demo**. **DO NOT build them.** They are listed in 0.3.1 only so you know they are *deliberately excluded*, not forgotten.

**0.3.1 Fields that are DESIGNED-BUT-NOT-BUILT — do NOT create these:**
- res.partner: `x_hcp_device_qualifications`, `x_consignee_type`
- stock.lot: `x_asset_type`, `x_last_sterilization_date`, `x_storage_temp_min`, `x_storage_temp_max`

Correspondingly, the credential-gate rule is the **as-built** version (checks state + expiry only — it does NOT check device qualifications). Use the verbatim code in Stage F.

### 0.4 STOP-AND-ASK list (halt and ask the user; never guess)
1. **S00004 (Dr. Okafor) order total = €5,820**, not €4,850. No surviving record gives the line composition. Observation: €4,850 × 1.2 = €5,820 exactly (**possible** 20% trial-default tax on that order, or a second ~€970 line) — but this is a hypothesis, not a fact. **Before building S00004's order lines, ask the user** what the line composition is. Until answered, build S00004 with a single HipCore line at €4,850 and flag it ⚠ in the audit as "total mismatch pending user input."
2. **Date collision** (see 0.6) — if the rebuild happens on/after ~2026‑09‑25.
3. **Any audit item still ❌ after 3 repair passes** (Part 4).

### 0.5 THE CANONICAL FACTS DICTIONARY
> Every value below is fixed truth. The machine-readable copy is the `CANON` dict in Part 4.2 — this table is the human-readable master.

**People & organisations (res.partner) — target count 11 (7 named below + Odoo defaults):**

| Name | Role | Key fields |
|---|---|---|
| Dr. M. Feldmann | Expired physician (the block) | `x_hcp_certification_number`=**DE-ORT-4471**, `x_hcp_certification_expiry`=**2026-04-30**, `x_validation_state`=**expired** |
| Dr. A. Weber | Valid physician (passes) | `x_hcp_certification_number`=**DE-ORT-5512**, `x_hcp_certification_expiry`=**2027-12-31**, `x_validation_state`=**validated** |
| Dr. S. Okafor | Locum (routes to review) | `x_validation_state`=**pending_verification**; cert fields blank |
| OrthoAlloy GmbH | Vendor (raw titanium) | supplier |
| Klinikum München Ost | Customer (hospital) | company; the consignment site |
| AOK Bayern | Insurer (settlement split, 90%) | customer |
| M. Schneider | Patient (co-pay, 10%) | individual |

**Sales orders (sale.order) — target count 3; record IDs land 1, 2, 4 (S00003 is a deliberate gap):**

| Name | Partner | State | amount_total | Notes |
|---|---|---|---|---|
| S00001 | Dr. M. Feldmann | **draft** | 4850.00 | NEVER confirmed — the credential block leaves it in draft |
| S00002 | Dr. A. Weber | **sale** | 4850.00 | confirmed clean → this surgery is invoiced |
| S00004 | Dr. S. Okafor | **sale** | **5820.00** ⚠ (STOP-AND-ASK #1) | confirmed WITH a "HCP credential verification required" review activity |

**Products (product.template / product.product) — target count 3:**

| Product | Internal ref | Tracking | Config | Std cost | Sale price |
|---|---|---|---|---|---|
| HipCore Ti-64 Femoral Stem | **IMP-HC-001** | serial | use_expiration_date=True, expiration_time=**730**, route=Manufacture, BoM = 1 × Ti rod | **1200.00** | **4850.00** |
| Ti-6Al-4V Rod Stock (Raw) | — | lot | route=Buy, vendor=OrthoAlloy, reorder **min 10 / max 50 scoped to WH/Stock** | **120.00** | — |
| Instrument Tray (Loaner) | — | serial | reusable asset (sterilisation loop) | **3000.00** | — |

> ⚠ Naming trap: the DRAFT runbook calls the tray "Instrument Tray — Hip Set A". That is wrong. The as-built + delivered name is **"Instrument Tray (Loaner)"**. The sterilisation rule matches on the substring "Instrument Tray", so the name MUST contain it.

**Lots & serials (stock.lot) — target count 7:**

| Name | Type | Key fields |
|---|---|---|
| LOT-2607-A | lot | `x_hold_release_date`=**2026-07-02** (hold elapsed, released to WH/Stock); 20 units received; cycle 0/0 |
| LOT-2607-B | lot | `x_hold_release_date`=**2026-10-01** (HELD in WH/Quarantine); 10 units; from receipt **WH/IN/00002**; cycle 0/0 |
| SN-HC-0001 | serial | `x_udi_pi`=**(10)LOT-2607-A(21)SN-HC-0001(17)280701**; consumed at surgery → invoiced; expiration_date=**2028-07-01** |
| SN-HC-0002 | serial | `x_udi_pi`=**(10)LOT-2607-A(21)SN-HC-0002(17)280701**; consigned at Klinikum, €1,200 on-book; expiration_date=**2028-07-01** |
| SN-HC-0003 | serial | `x_udi_pi`=**(10)LOT-2607-A(21)SN-HC-0003(17)280702**; from **WH/MO/00004**; returned to WH/Quarantine/Returns; `x_return_disposition`=**requarantine**; `x_return_reason`=**"Surgery cancelled — packaging intact, within sterility window; fresh quality check required before restock."**; expiration_date=**2028-07-02** |
| TRAY-A-001 | serial | `x_sterilization_cycle_count`=**1**, `x_sterilization_cycle_limit`=**50**; in Sterilization loop |
| TRAY-B-001 | serial | `x_sterilization_cycle_count`=**50**, `x_sterilization_cycle_limit`=**50**; dispatch-refused; at WH/Stock |

All three implant serials: `x_udi_di`=**04012345678901**, `x_udi_source`=**scan**, `use_expiration_date`=True.

**Invoices (account.move) — target count 3 (1 posted + 2 draft split preview); account.move.line count 8:**

| Name / ref | Partner | State | Total | Analytics |
|---|---|---|---|---|
| INV/2026/00001 | Klinikum München Ost | **posted** | **4850.00** | one line 100% across all 3 plans: Cost Center=**Orthopedics-KMO**, Payer Type=**GKV**, Product Line=**HipCore** |
| ref "Settlement split — Surgery SN-HC-0001" | **AOK Bayern** (insurer) | **draft** | 90% split | same analytic key |
| ref "Settlement split — Surgery SN-HC-0001" | **M. Schneider** (patient) | **draft** | 10% co-pay | same analytic key |

**Analytic plans (4) & accounts (3):** plans = Cost Center, Payer Type, Product Line (+ Odoo's default plan makes 4). Accounts = **Orthopedics-KMO** (under Cost Center), **GKV** (under Payer Type), **HipCore** (under Product Line).

**Exact selection sets (keys, not labels — the rule code depends on the keys):**
- `x_validation_state`: `draft` / `validated` / `expired` / `suspended` / `pending_verification` *(rule also tolerates bare `pending`)*
- `x_udi_source`: `scan` (label "Scanned (GS1)") / `manual` (label "Manual")
- `x_return_disposition`: `requarantine` (Re-Quarantine) / `scrap` (Scrap) / `rtv` (Return-to-Vendor) / `under_investigation` (Under Investigation)

**Document numbers that MUST match:** S00001, S00002, S00004 · WH/IN/00002 (the OrthoAlloy 10‑unit receipt) · WH/MO/00004 (SN-HC-0003's manufacturing order) · INV/2026/00001.

**Record counts to hit (from the live inventory census):**
`res.partner`=11 · `stock.lot`=7 · `stock.location`=12 · `stock.picking`=13 · `stock.move`=22 · `mrp.production`=4 · `quality.point`=2 · `quality.check`=3 · `sale.order`=3 · `account.move`=3 · `account.move.line`=8 · `base.automation`=4 · `account.analytic.plan`=4 · `account.analytic.account`=3 · `product.template`=3.

### 0.6 ⚠ DATE-INTEGRITY PROTOCOL — RUN THIS AS LITERAL STEP 1
The **Auto Quality Hold** rule stamps `x_hold_release_date = today + 90 days` when a raw lot is created. On a rebuild "today" is not 2026‑07‑05, so the auto‑stamp will NOT equal the canonical dates. Two consequences:

1. **After** the rule fires on each raw lot (which proves the mechanism works), you must **explicitly overwrite** the dates to canonical:
   - LOT-2607-B → `x_hold_release_date` = **2026-10-01**
   - LOT-2607-A → `x_hold_release_date` = **2026-07-02**
   - SN-HC-0001, SN-HC-0002 → `expiration_date` = **2028-07-01**
   - SN-HC-0003 → `expiration_date` = **2028-07-02**
2. **Collision check (do this before building anything):** print today's date. **If today ≥ 2026‑09‑25**, the canonical hold date 2026‑10‑01 is at/near the past, and the LOT‑2607‑B "quarantine hold" refusal (a core demo moment) will no longer fire. This is a genuine conflict with no safe default → **STOP AND ASK the user**: (a) shift LOT‑2607‑B's hold to a near-future date (breaks exact fidelity with the delivered docs), or (b) keep 2026‑10‑01 (the live refusal won't trigger). Do not choose for them.

```python
import datetime
print("TODAY:", datetime.date.today())
if datetime.date.today() >= datetime.date(2026, 9, 25):
    print("⚠ STOP-AND-ASK #2: canonical hold 2026-10-01 is at/past today; LOT-2607-B refusal will not fire. Ask the user before proceeding.")
```

---

## PART 1 · CONNECTION & THE saas~19.3 API QUIRKS APPENDIX

Everything here was learned by driving the live API and is written into this document because it is recorded nowhere else. Each quirk is an exact error → the working fix.

### 1.1 The connection helper (`api.py`)
Create `api.py` next to your scripts. Fill the four constants from 0.1.

```python
"""Shared Odoo XML-RPC helper."""
import xmlrpc.client, ssl, os

URL  = "https://<INSTANCE>.odoo.com"     # 0.1 input 1
DB   = "<DATABASE>"                        # 0.1 input 2
USER = "<LOGIN_EMAIL>"                     # 0.1 input 3
KEY  = "<API_KEY>"                         # 0.1 input 4  (NEVER the account password)

def conn():
    common = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/common", allow_none=True)
    uid = common.authenticate(DB, USER, KEY, {})
    models = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/object", allow_none=True)
    return uid, models, common

def mk(models, uid):
    def ex(model, method, *args, **kw):
        return models.execute_kw(DB, uid, KEY, model, method, list(args), kw)
    return ex

def mk_void(ex):
    """For methods that may return None (XML-RPC can't marshal None)."""
    import xmlrpc.client
    def exv(model, method, *args, **kw):
        try:
            return ex(model, method, *args, **kw)
        except xmlrpc.client.Fault as f:
            if "cannot marshal None" in str(f): return None
            raise
    return exv
```
Smoke test: `uid, models, common = conn(); print(uid, common.version()["server_serie"])` → expect a uid and `saas~19.3`.

### 1.2 The quirks (exact error → fix) — saas~19.3
1. **Domains must be a positional list-of-lists.** `ex('res.partner','search',[('id','>',0)])` works; `ex(...,[[]])` raises `ValueError: Domain() invalid item in domain: []`, and a string domain raises the same. Rule: pass `[('field','op',val)]` as the *first positional arg* to search/search_read, e.g. `ex('res.partner','search',[('id','>',0)], limit=3)`. To read everything, use `[('id','>',0)]`, never `[]`.
2. **`stock.move` has no `name` field** on saas~19.3 → `ValueError: Invalid field 'name' in 'stock.move'`. Omit `name`. Required create fields: `date`, `company_id`, `product_id`, `product_uom_qty`, `uom_id`, `location_id`, `location_dest_id`.
3. **`stock.move.line`** has no `product_uom_id` and no `qty_done` → use `quantity` for the moved amount.
4. **`base.automation` has no `state` field, and the action code lives in a separate `ir.actions.server`.** Build order: create the `ir.actions.server` (`state='code'`, `model_id=<M>`, `code=<verbatim>`) FIRST, then create the `base.automation` with `action_server_ids=[(6,0,[server_id])]`. The automation's fields: `trigger` (`'on_state_set'` or `'on_create'`), `trigger_field_ids=[(6,0,[<id of the model's 'state' field>])]` for state-set triggers, and `filter_domain` (a *string*, e.g. `"[('state','=','sale')]"`).
5. **All numeric model/field/record IDs from the old system are void.** Old values were model_id 3184 (Sales Order), 3759 (Transfer/stock.picking), 3757 (Lot/Serial/stock.lot). **Resolve everything fresh with these helpers (used throughout — never hardcode an id):**
   ```python
   def model_id(ex, model):                     # e.g. model_id(ex,'sale.order')
       return ex('ir.model','search',[('model','=',model)])[0]
   def field_id(ex, model, fname):              # the id of a field on a model (e.g. the 'state' field)
       return ex('ir.model.fields','search',[('model','=',model),('name','=',fname)])[0]
   def rec_id(ex, model, name, field='name'):   # a record's id by its name/complete_name
       r = ex(model,'search',[(field,'=',name)]); return r[0] if r else None
   def loc_id(ex, complete_name):               # a stock.location id by complete_name (e.g. 'WH/Quarantine')
       return rec_id(ex,'stock.location',complete_name,'complete_name')
   def wh(ex):                                  # the default warehouse + its view location id
       w = ex('stock.warehouse','search_read',[('id','>',0)], fields=['view_location_id','lot_stock_id','in_type_id','manu_type_id'])[0]
       return w   # w['view_location_id'][0]=WH view loc, w['lot_stock_id'][0]=WH/Stock, w['in_type_id'][0]=Receipts type, w['manu_type_id'][0]=Manufacturing type
   def seq_of_picking_type(ex, ptype_id):       # the ir.sequence id feeding a picking type's numbering
       return ex('stock.picking.type','read',[ptype_id], fields=['sequence_id'])[0]['sequence_id'][0]
   def seq_by_code(ex, code):                   # e.g. seq_by_code(ex,'sale.order'), seq_by_code(ex,'mrp.production')
       r = ex('ir.sequence','search',[('code','=',code)]); return r[0] if r else None
   ```
   **NOTE on `search_read`/`search_count` options:** pass options as **kwargs**, never as a trailing positional dict. Correct: `ex('res.partner','search_read',[('id','>',0)], fields=['name'], limit=5)`. WRONG: `ex('res.partner','search_read',[('id','>',0)], {'fields':['name']})` — the dict lands in the `fields` positional slot and raises `Invalid field 'fields'`. (Create/write take positional args and are unaffected.)
6. **`stock.lot` has no `active` field** → cannot archive via API. **`stock.quant` unlink is permission-blocked** (`You are not allowed to delete 'Quant'`). To remove stray stock: use an inventory adjustment to zero it, or neutralise the lot (rename `ZZ-…`, push its dates far out) and leave it — but for an exact count, prefer never creating strays.
7. **`cannot marshal None`** on some method returns → wrap with `mk_void`.
8. **Custom fields are created via `ir.model.fields` create** (`state='manual'`, `name` must start with `x_`, set `ttype`). For Selection, set `selection_ids` (one `(0,0,{'value':<key>,'name':<label>,'sequence':N})` per option) — the **keys** must match the values the rule code and records use.
9. **Trial tier: Field Service is unavailable.** The "Surgery Complete" consumption trigger is therefore represented by a plain inventory move (UAT scenario T‑14 = SIMULATED). Preserve this boundary exactly — it is stated openly in the delivered package and is pitch material, not a defect to hide.
10. **Form-view placement** of the "MDR Compliance — UDI & Quality" section: the reliable path is the manual Studio route (Part 5). An API `ir.ui.view` arch-patch can work but is fragile across trials; if you attempt it and the fields don't render, fall back to Studio and mark it MANUAL — the fields existing and holding correct values is what the audit checks; their visual grouping is cosmetic.

---

## PART 2 · THE BUILD, STAGE BY STAGE

Run stages **in order** — dependencies are real (settings before data, fields before automations, sequences before named records). **Every stage ends with a VERIFY block; if it fails, fix it immediately using the Part 4 remediation table before moving on.**

### Stage A — Instance preparation
1. Rename the company → **"MDR Devices Medizintechnik GmbH"**, currency EUR:
   `ex('res.company','write',[cid],{'name':'MDR Devices Medizintechnik GmbH'})` (resolve `cid` = `ex('res.company','search',[('id','>',0)])[0]`).
2. Install apps: **Inventory, Purchase, Manufacturing, Quality, Sales, CRM, Accounting, Barcode, Studio**. (Field Service will not install on the trial — expected; skip it.) App install via API is unreliable; do it in the UI (Apps → search → Activate) — this is a MANUAL step, verify each app's root menu appears.
3. Enable settings (Settings UI or `res.config.settings`): Inventory → **Lots & Serial Numbers**, **Expiration Dates**, **Storage Locations**, **Multi-Step Routes**; Accounting → **Analytic Accounting**.

**VERIFY A:** `ex('ir.module.module','search_count',[('name','in',['stock','purchase','mrp','quality_control','sale_management','crm','account','stock_barcode']),('state','=','installed')])` == 8. A product form has a Traceability section; Inventory → Configuration shows Locations & Routes.

### Stage B — Locations (7, all internal)
`WH/Stock` already exists (`wh(ex)['lot_stock_id']`). Create the other 6 under the WH view location. All `usage='internal'`.

| Create (leaf name) | parent (`location_id`) → resolve with |
|---|---|
| Stock | (exists — `wh(ex)['lot_stock_id'][0]`) |
| Quarantine | WH view loc = `wh(ex)['view_location_id'][0]` |
| Disposition | `loc_id(ex,'WH/Quarantine')` |
| Returns | `loc_id(ex,'WH/Quarantine')` |
| Consignment | WH view loc |
| Klinikum München | `loc_id(ex,'WH/Consignment')` |
| Sterilization | WH view loc |

Create each: `ex('stock.location','create',{'name':'Quarantine','location_id':wh(ex)['view_location_id'][0],'usage':'internal'})` (name is the leaf; `complete_name` is derived — e.g. leaf "Klinikum München" under WH/Consignment renders `WH/Consignment/Klinikum München`). Create parents before children (Quarantine and Consignment before their sub-locations).
Then set the **Receipts operation type default destination → WH/Quarantine** (load-bearing — makes quarantine unavoidable):
```python
recv = wh(ex)['in_type_id'][0]
ex('stock.picking.type','write',[recv],{'default_location_dest_id':loc_id(ex,'WH/Quarantine')})
```

**VERIFY B:** all 7 `complete_name`s exist with `usage='internal'`; Receipts type's `default_location_dest_id` is WH/Quarantine.

### Stage C — Analytics
1. Create/confirm 3 plans: Cost Center, Payer Type, Product Line (`account.analytic.plan`). Odoo's default plan brings the count to 4.
2. Create 3 analytic accounts, one under each plan: **Orthopedics-KMO** (Cost Center), **GKV** (Payer Type), **HipCore** (Product Line) — `account.analytic.account` with `plan_id` set.
3. **Capture the three ANALYTIC-ACCOUNT ids** (not the plan ids): `acct_ids = [rec_id(ex,'account.analytic.account',n) for n in ['Orthopedics-KMO','GKV','HipCore']]`. The invoice line's `analytic_distribution` key is the comma-joined string of these three account ids (Stage I.7).

**VERIFY C:** `account.analytic.plan` count == 4; `account.analytic.account` count == 3 with the three names above.

### Stage D — Products (3)
> **Ordering prerequisite:** the Ti rod's vendor link points to **OrthoAlloy GmbH**, which is created in Stage H. Create the OrthoAlloy partner FIRST (`ex('res.partner','create',{'name':'OrthoAlloy GmbH','supplier_rank':1})`) so the `seller_ids`/`supplierinfo` link resolves here — the rest of Stage H's partners can stay in Stage H.

Create per the 0.5 product table. Set product category "Goods" costing method → **Standard Price** (`ex('product.category','write',[rec_id(ex,'product.category','Goods')],{'property_cost_method':'standard'})`). Standard costs (`standard_price`): implant 1200, rod 120, tray 3000; implant `list_price` 4850. On the Ti rod set `seller_ids=[(0,0,{'partner_id':rec_id(ex,'res.partner','OrthoAlloy GmbH')})]`. BoM: HipCore = 1 × Ti rod (`mrp.bom` + `mrp.bom.line`). Reorder rule (`stock.warehouse.orderpoint`) on the Ti rod: `product_min_qty=10`, `product_max_qty=50`, `location_id`=`loc_id(ex,'WH/Stock')`.

**VERIFY D:** 3 `product.template`; HipCore tracking=serial, use_expiration_date=True, expiration_time=730; rod reorder rule min10/max50 at WH/Stock; tray name contains "Instrument Tray".

### Stage E — Custom fields (exactly 14; the 5 in 0.3.1 are EXCLUDED)
Create via `ir.model.fields`. **res.partner (3):**
- `x_hcp_certification_number` — Char, label "HCP Certification #"
- `x_hcp_certification_expiry` — Date, label "Certification Expiry"
- `x_validation_state` — Selection, label "Credential Status", keys: draft/validated/expired/suspended/pending_verification

**stock.lot (11):**
- `x_hold_release_date` — Date, "Quality Hold Release"
- `x_udi_di` — Char, "UDI — Device Identifier"
- `x_udi_pi` — Char, "UDI — Production Identifier (composite)"  *(plain stored Char; NOT computed)*
- `x_udi_pi_batch` — Char, "UDI PI — Batch (AI 10)"
- `x_udi_pi_serial` — Char, "UDI PI — Serial (AI 21)"
- `x_udi_pi_expiry` — Date, "UDI PI — Expiry (AI 17)"
- `x_udi_source` — Selection, "UDI Source", keys: scan (Scanned (GS1)) / manual (Manual)
- `x_sterilization_cycle_count` — Integer, "Sterilization Cycle Count"
- `x_sterilization_cycle_limit` — Integer, "Sterilization Cycle Limit"
- `x_return_disposition` — Selection, "Return Disposition", keys: requarantine (Re-Quarantine) / scrap (Scrap) / rtv (Return-to-Vendor) / under_investigation (Under Investigation)
- `x_return_reason` — Char, "Return Reason"

> Every field's `field_description` (label) is given above — always pass it on create (it is required). Selection fields also need `selection_ids` with the exact keys (see the pattern below).

Selection create pattern:
```python
ex('ir.model.fields','create',{
  'name':'x_validation_state','model_id':model_id(ex,'res.partner'),'ttype':'selection',
  'field_description':'Credential Status','state':'manual',
  'selection_ids':[(0,0,{'value':'draft','name':'Draft','sequence':10}),
                   (0,0,{'value':'validated','name':'Validated','sequence':20}),
                   (0,0,{'value':'expired','name':'Expired','sequence':30}),
                   (0,0,{'value':'suspended','name':'Suspended','sequence':40}),
                   (0,0,{'value':'pending_verification','name':'Pending Verification','sequence':50})]})
```
Place the built fields into an "MDR Compliance — UDI & Quality" section on the stock.lot form (Studio, MANUAL — Part 5). **Do NOT create the 6 fields in 0.3.1.**

**VERIFY E:** exactly the 14 names above exist (3 on res.partner, 11 on stock.lot); the three selection fields carry the exact keys; none of the 6 excluded names exist.

### Stage F — The 4 automation rules (VERBATIM code)
For each rule: create `ir.actions.server` (state='code', model_id, code = the exact block below), then `base.automation` with the trigger/domain given. Resolve `model_id`/state-`field_id` by lookup (quirk 5). After creation, dry-fire once (Part 4 fire-tests) and assert the exact message.

> **`base.automation.name` is the FULL rule name WITHOUT the "Rule N — " prefix.** e.g. the first rule's `name` is exactly `"MDR Credential Gate — Block Confirm on Invalid HCP"` (matching `CANON["automations"]`). Do NOT include "Rule 1 — ". The `ir.actions.server.name` can be anything (e.g. the same text + " Code"); only the `base.automation.name` is audited.
>
> **Skeleton for each rule** (resolve ids with the helpers):
> ```python
> def make_rule(ex, rule_name, model, trigger, filter_domain, code):
>     sa = ex('ir.actions.server','create',{'name':rule_name+' Code','model_id':model_id(ex,model),'state':'code','code':code})
>     vals = {'name':rule_name,'model_id':model_id(ex,model),'trigger':trigger,'action_server_ids':[(6,0,[sa])]}
>     if trigger=='on_state_set': vals['trigger_field_ids']=[(6,0,[field_id(ex,model,'state')])]
>     if filter_domain: vals['filter_domain']=filter_domain
>     return ex('base.automation','create',vals)
> ```

**Rule 1 — MDR Credential Gate — Block Confirm on Invalid HCP**
model: `sale.order` · trigger: `on_state_set` · `filter_domain`: `"[('state','=','sale')]"` · `trigger_field_ids`: [state field of sale.order]
```python
for order in records:
    p = order.partner_id
    state = p.x_validation_state
    if state in ("expired", "suspended") or (p.x_hcp_certification_expiry and p.x_hcp_certification_expiry < datetime.date.today()):
        raise UserError("Blocked — HCP certification expired or invalid for %s. Order cannot be confirmed (MDR credential gate)." % p.name)
    if state in ("pending","pending_verification") or not state:
        order.activity_schedule("mail.mail_activity_data_todo",
            summary="HCP credential verification required",
            note="Order confirmed for a physician with no verified credential record (locum/visiting). Routed to credential review queue — verify certification before delivery release.",
            user_id=env.user.id)
        order.message_post(body="MDR credential gate: physician %s is Pending Verification — order routed to manual credential review queue (delivery held until verified)." % p.name)
```

**Rule 2 — GxP Quarantine Hold — Block Release Before Hold Elapses**
model: `stock.picking` (Transfer) · trigger: `on_state_set` · `filter_domain`: `"[('state','=','done')]"` · `trigger_field_ids`: [state field of stock.picking]
```python
for picking in records:
    for ml in picking.move_line_ids:
        lot = ml.lot_id
        src = ml.location_id.complete_name or ""
        dst = ml.location_dest_id.complete_name or ""
        if lot and lot.x_hold_release_date and "Quarantine" in src and "Disposition" not in dst:
            if lot.x_hold_release_date > datetime.date.today():
                raise UserError("GxP quarantine gate — quality hold active for lot %s until %s. Release to stock is blocked." % (lot.name, lot.x_hold_release_date))
```

**Rule 3 — Auto Quality Hold — 90 Days on New Raw Lots**
model: `stock.lot` (Lot/Serial) · trigger: `on_create` · `filter_domain`: false (none)
```python
for lot in records:
    if not lot.x_hold_release_date and lot.product_id.tracking == "lot":
        lot.write({"x_hold_release_date": datetime.date.today() + datetime.timedelta(days=90)})
```

**Rule 4 — Sterilization Cycle — Auto-Count and Reuse-Limit Block**
model: `stock.picking` (Transfer) · trigger: `on_state_set` · `filter_domain`: `"[('state','=','done')]"` · `trigger_field_ids`: [state field of stock.picking]
```python
for picking in records:
    for ml in picking.move_line_ids:
        lot = ml.lot_id
        if not lot or "Instrument Tray" not in (ml.product_id.name or ""):
            continue
        dst = ml.location_dest_id.complete_name or ""
        if "Sterilization" in dst:
            lot.write({"x_sterilization_cycle_count": (lot.x_sterilization_cycle_count or 0) + 1})
        if "Consignment" in dst and lot.x_sterilization_cycle_limit:
            if (lot.x_sterilization_cycle_count or 0) >= lot.x_sterilization_cycle_limit:
                raise UserError("Reuse limit reached — tray %s has completed %s of %s sterilization cycles. Dispatch blocked; route to retirement (MDR reusable-device control)." % (lot.name, lot.x_sterilization_cycle_count, lot.x_sterilization_cycle_limit))
```

> Escaping note: when writing these into an `ir.actions.server` `code` value over XML-RPC, pass them as ordinary Python strings — do not double-escape the `%` or the quotes. Copy the block exactly, including the em-dash `—` (U+2014) in each message.

**VERIFY F:** `base.automation` count == 4 with the four exact names; each linked server action's `code` matches the block; the three refusal messages fire byte-exact (Part 4 fire-tests).

### Stage G — Quality control points (2)
`quality.point` create dicts (resolve the picking-type and product ids with the helpers). `measure_on='operation'`, `test_type_id` = the "Pass - Fail" test type: `ptt = rec_id(ex,'quality.point.test_type','Pass - Fail')` — if that lookup misses on the trial, resolve via `ex('quality.point.test_type','search',[('technical_name','=','passfail')])[0]`.
```python
ti_rod = rec_id(ex,'product.product','Ti-6Al-4V Rod Stock (Raw)') or ex('product.product','search',[('name','like','Ti-6Al-4V')])[0]
tray    = ex('product.product','search',[('name','like','Instrument Tray')])[0]
recv    = wh(ex)['in_type_id'][0]
internal= ex('stock.picking.type','search',[('code','=','internal')])[0]
ex('quality.point','create',{'title':'Inbound Implant Material Inspection','product_ids':[(6,0,[ti_rod])],
    'picking_type_ids':[(6,0,[recv])],'measure_on':'operation','test_type_id':ptt,
    'note':'Visual inspection · storage-condition / temperature-log review · certificate-of-analysis verification'})
ex('quality.point','create',{'title':'Autoclave Cycle Verification','product_ids':[(6,0,[tray])],
    'picking_type_ids':[(6,0,[internal])],'measure_on':'operation','test_type_id':ptt,
    'note':'Record autoclave cycle reference + parameters (temperature, duration, pressure); second-person countersign required before redeploy'})
```
The transactional flow (Stage I) produces **3 quality.checks**, all passed (pass a check with `ex('quality.check','write',[cid],{'quality_state':'pass'})` or the `do_pass()` method).

**VERIFY G:** `quality.point` count == 2; after Stage I, `quality.check` count == 3, all `quality_state='pass'`.

### Stage H — Partners (7 named)
Create OrthoAlloy GmbH (supplier), Klinikum München Ost (customer, is_company), AOK Bayern (customer), M. Schneider (individual), and the 3 physicians with the exact credential values from 0.5 (Feldmann expired/DE-ORT-4471/2026-04-30; Weber validated/DE-ORT-5512/2027-12-31; Okafor pending_verification). Link Feldmann to Klinikum if desired (cosmetic).

**VERIFY H:** the 7 named partners exist; the 3 physicians carry the exact `x_validation_state` keys + cert fields.

### Stage I — Transactional choreography
**Sequence management FIRST** (document numbers are canonical; resolve every sequence with the helpers — never guess an id):
- **Receipts (WH/IN):** `ex('ir.sequence','write',[seq_of_picking_type(ex, wh(ex)['in_type_id'][0])],{'number_next_actual':2})` so the OrthoAlloy 10-unit receipt is **WH/IN/00002**. (Alternatively let an earlier throwaway receipt consume WH/IN/00001.)
- **MOs (WH/MO):** ensure SN-HC-0003's MO is **WH/MO/00004** — the flow creates 4 MOs (see step 3 topology); set `ex('ir.sequence','write',[seq_of_picking_type(ex, wh(ex)['manu_type_id'][0])],{'number_next_actual':1})` before the first MO so numbering runs 1→4 cleanly.
- **Sales (S):** create S00001 (Feldmann), S00002 (Weber), a **throwaway S00003 then delete it** so Okafor's order lands as **S00004** (reproduces record ids 1,2,4 and the S00003 name gap). Primary: create S00003, `ex('sale.order','unlink',[id])`. Fallback if unlink is blocked: `ex('ir.sequence','write',[seq_by_code(ex,'sale.order')],{'number_next_actual':4})` before creating Okafor's order.

Then, each step immediately VERIFY'd against 0.5:
1. **PO → OrthoAlloy**, receive **10 units** → receipt **WH/IN/00002**, lot **LOT-2607-B** lands in WH/Quarantine (Auto Quality Hold fires, stamps a +90d date — corrected in step 10). Pass the Inbound QC check.
2. **Second raw receipt, 20 units → LOT-2607-A** → also lands in WH/Quarantine and gets auto-stamped a +90d hold. **Before releasing it, override its hold to a past date** (`ex('stock.lot','write',[lotA_id],{'x_hold_release_date':'2026-07-02'})`) — otherwise **Rule 2 (already live) will block the Quarantine→Stock transfer** because the auto-stamped hold is in the future. Pass its QC, then create+validate an internal transfer LOT-2607-A → **WH/Stock** (now permitted).
3. **4 manufacturing orders** consuming LOT-2607-A, numbered WH/MO/00001…00004. **Topology (spell it out — needed to hit `mrp.production`=4 with only 3 surviving serials):** WH/MO/00001 → produces **SN-HC-0001**; WH/MO/00002 → produces **SN-HC-0002**; **WH/MO/00003 = a padding MO** (created and left in `draft`/`confirmed`, no finished serial — it exists only to advance the sequence so the next MO is 00004; it consumes nothing and produces nothing); WH/MO/00004 → produces **SN-HC-0003**. (Each producing MO backflushes 1 × LOT-2607-A → 1 finished serial; mark it done.) For each of the 3 finished serials write: `x_udi_di`='04012345678901', `x_udi_pi`=the per-serial composite (0.5), `x_udi_pi_batch`='LOT-2607-A', `x_udi_pi_serial`=the serial name, `x_udi_pi_expiry`=2028-07-01 (0001/0002) or 2028-07-02 (0003), `x_udi_source`='scan', `use_expiration_date`=True.
4. **Consign SN-HC-0002** → internal transfer to WH/Consignment/Klinikum München. VERIFY €1,200 on-book, location usage=internal.
5. **Consume SN-HC-0001** at surgery — inventory move to a customer/consumed location (T-14 SIMULATED; Field Service is off-tier).
6. **Sales orders:** S00001 for Feldmann (1 × HipCore, €4,850) — attempt Confirm ONCE (the credential gate blocks it → message logged in chatter), leave it in **draft**. Confirm S00002 for Weber (€4,850 → this is the invoiced surgery). Create+delete throwaway S00003. Create S00004 for Okafor and Confirm (routes to review — a "HCP credential verification required" activity is created; order state = sale). **S00004 total: STOP-AND-ASK #1** — build ONE €4,850 HipCore line for now; the audit will show it ⚠ pending the user's answer on the €5,820 composition (`amount_total` is a computed field — do NOT try to write 5820 directly; add/adjust order LINES once the user supplies the composition).
7. **Invoicing:** post **INV/2026/00001** from Weber's SO — one invoice line, `analytic_distribution` = `{",".join(str(a) for a in acct_ids): 100.0}` where `acct_ids` are the 3 analytic-account ids from Stage C (key is the comma-joined string of the three account ids). Then create **2 draft** `account.move` invoices (`move_type='out_invoice'`, `state` left draft) with `ref="Settlement split — Surgery SN-HC-0001"`: one to **AOK Bayern** (line ~90% of 4850 = 4365.00), one to **M. Schneider** (line ~10% = 485.00), both carrying the same `analytic_distribution`. Leave both **draft** (extension-layer preview).
8. **Trays:** create TRAY-A-001 and TRAY-B-001 (serials on the Instrument Tray (Loaner) product). Run ONE real sterilisation-loop transfer for TRAY-A-001 into WH/Sterilization (so chatter shows the auto-count mechanism — the rule increments it to 1), then set `x_sterilization_cycle_count`=1, `x_sterilization_cycle_limit`=50. Set TRAY-B-001 to `x_sterilization_cycle_count`=50, `x_sterilization_cycle_limit`=50. Attempt to dispatch TRAY-B-001 to a Consignment location ONCE → the reuse-limit refusal fires and is logged; leave the tray at WH/Stock, undispatched.
9. **Return flow:** move SN-HC-0003 to WH/Quarantine/Returns; set `x_return_disposition`='requarantine' and `x_return_reason`=the exact text in 0.5.
10. **Apply canonical date overrides** (0.6): overwrite LOT-2607-B hold → 2026-10-01, LOT-2607-A hold → 2026-07-02, serial expiries → 2028-07-01/02. Final VERIFY: hero records == 0.5, counts == 0.5.

> **Expected `account.move.line` = 8 breakdown** (so you can hit the count): INV/2026/00001 = 1 product line + 1 receivable line (2); AOK Bayern draft = 1 product + 1 receivable (2); M. Schneider draft = 1 product + 1 receivable (2); plus the 2 lines Odoo auto-adds for tax/rounding across the set as applicable — if your count lands at 6, the two split invoices likely posted without a tax line; if it lands at 9+, an extra invoice or line crept in. The audit reports the number; the remediation is to inspect `account.move.line` names and add/remove to reach 8. This count is the softest target in the build — treat a ±1 as acceptable if every named record and value is otherwise ✅, and note it in the final report rather than forcing a stray line.

---

## PART 3 · THE SHOWCASE INVENTORY (what the presenter clicks through)

Every record above exists so a specific demo moment lands. This is the map. **The demo is the three refusals; everything else is connective tissue.**

### 3.1 The 9-stop demo path (exact refusal strings in bold)
1. **Identity** — Dashboard; header reads "MDR Devices Medizintechnik GmbH". *"A running system, not a mockup."*
2. **REFUSAL #1 — Credential gate.** Contacts → Dr. M. Feldmann (Credential Status: Expired, lapsed 30/04/2026). Open **S00001** → Confirm → **"Blocked — HCP certification expired or invalid for Dr. M. Feldmann. Order cannot be confirmed (MDR credential gate)."** Order stays Draft. Contrast: **S00002** (Weber) confirms clean; **S00004** (Okafor, Pending Verification) confirms WITH a "HCP credential verification required" review activity.
3. **Quarantine by construction** — receipt **WH/IN/00002** (OrthoAlloy, 10 units) → destination WH/Quarantine, lot **LOT-2607-B** created; show the passed inbound quality check.
4. **REFUSAL #2 — 90-day hold.** LOT-2607-B hold release **2026-10-01**; create an internal transfer Quarantine → Stock, attempt to validate → **"GxP quarantine gate — quality hold active for lot LOT-2607-B until 2026-10-01. Release to stock is blocked."** Discard the draft transfer afterwards.
5. **Birth of an implant** — **WH/MO/00004**: consumed LOT-2607-A → produced **SN-HC-0003**. Open the serial → "MDR Compliance — UDI & Quality": DI 04012345678901, composite **(10)LOT-2607-A(21)SN-HC-0003(17)280702**, source Scanned (GS1), sterility expiry.
6. **Consignment truth** — Inventory by location → **SN-HC-0002** at WH/Consignment/Klinikum München, **€1,200 on-book**. *"Physically at the hospital, financially on MDR's balance sheet."*
7. **Money follows the event** — **INV/2026/00001**, posted, €4,850, line 100% across Cost Center (Orthopedics-KMO) / Payer Type (GKV) / Product Line (HipCore). Then the settlement-split list: the posted invoice + the two drafts (AOK Bayern 90%, M. Schneider 10%) sharing ref "Settlement split — Surgery SN-HC-0001".
8. **REFUSAL #3 — Instrument loop.** TRAY-A-001 (1/50) vs **TRAY-B-001 (50/50)** → attempt dispatch → **"Reuse limit reached — tray TRAY-B-001 has completed 50 of 50 sterilization cycles. Dispatch blocked; route to retirement (MDR reusable-device control)."** Cancel the draft transfer.
9. **One-query close** — Traceability report from **SN-HC-0003**: receipt → quarantine → release → manufacture → consignment → return, one screen. *"EU MDR Article 27 evidence in one screen."*

### 3.2 The 6 fire-tested behaviours (Q&A ammunition)
| # | Control | Expected |
|---|---|---|
| TC-01 | Expired-credential order block | BLOCKED, exact banner |
| TC-16 | Locum → review queue (not hard block) | ROUTED, activity created |
| TC-05 | Quarantine hold release block | BLOCKED, lot stays held |
| TC-14 | Tray reuse-limit dispatch block | BLOCKED at 50/50 |
| — | Valid order passes the gate | S00002 confirmed → invoiced |
| — | Auto-hold on new lots / auto cycle count | automations live |

### 3.3 The 12-shot screenshot manifest (regenerate the deck's "live in sandbox" images)
1. S00001 Confirm → red credential block · 2. Dr. Feldmann form (credential section) · 3. S00004 review activity (locum routing) · 4. LOT-2607-B hold date · 5. Blocked quarantine release · 6. SN-HC-0001 UDI section · 7. Traceability report (KEY) · 8. Consignment quant at Klinikum · 9. SN-HC-0003 return disposition · 10. TRAY-B-001 50/50 + dispatch block · 11. Three-invoice settlement list + analytic widget · 12. Inventory dashboard with the company name in the header.

### 3.4 The 16 UAT scenarios (acceptance checklist; T-14 SIMULATED)
T-01 login/dashboard · T-02 Weber credential record · T-03 Feldmann block · T-04 Weber confirms · T-05 Okafor routed · T-06 receipt auto-quarantine · T-07 QC generated+passed · T-08 90-day hold blocks release · T-09 lot/serial register · T-10 UDI on serial · T-11 MO genealogy · T-12 consignment on-book · T-13 sterilisation reuse-limit block · **T-14 surgery event (SIMULATED)** · T-15 invoice 3-plan analytics · T-16 end-to-end traceability one query.

### 3.5 The "let them pick one" live re-run
After Stop 9, the presenter may invite the panel to choose which refusal to re-run cold. Keep a spare path available: a throwaway physician whose certification you can re-lapse, a fresh raw lot you can hold, or a spare tray at limit — so any of the three gates can be triggered live on the panel's choice without disturbing the hero records.

---

## PART 4 · SELF-AUDITING & SELF-HEALING ACCEPTANCE SUITE

**This is the safety net for a lighter executor.** You do not reason about fixes — you run `audit.py`, and for every ❌ you apply the exact repair from the Remediation Table (4.3), then re-run. Loop until all ✅ or a STOP-AND-ASK.

### 4.1 Principle
The canonical expected state is embedded in this document as the `CANON` dict (4.2). The audit reads the live instance and compares. **The document is truth; the instance is wrong wherever it differs; repair the instance, never edit the expectation.**

### 4.2 The embedded canonical dataset (`CANON`)
```python
CANON = {
  "counts": {"res.partner":11,"stock.lot":7,"stock.location":12,"stock.picking":13,
    "stock.move":22,"mrp.production":4,"quality.point":2,"quality.check":3,
    "sale.order":3,"account.move":3,"account.move.line":8,"base.automation":4,
    "account.analytic.plan":4,"account.analytic.account":3,"product.template":3},
  "sale_orders": {
    "S00001": {"state":"draft","amount_total":4850.0},
    "S00002": {"state":"sale","amount_total":4850.0},
    "S00004": {"state":"sale","amount_total":5820.0}},   # ⚠ STOP-AND-ASK #1
  "lots": {
    "LOT-2607-A": {"x_hold_release_date":"2026-07-02","x_sterilization_cycle_count":0,"x_sterilization_cycle_limit":0,"x_return_disposition":False},
    "LOT-2607-B": {"x_hold_release_date":"2026-10-01","x_sterilization_cycle_count":0,"x_sterilization_cycle_limit":0,"x_return_disposition":False},
    "SN-HC-0001": {"x_udi_di":"04012345678901","x_udi_pi":"(10)LOT-2607-A(21)SN-HC-0001(17)280701","x_udi_source":"scan"},
    "SN-HC-0002": {"x_udi_di":"04012345678901","x_udi_pi":"(10)LOT-2607-A(21)SN-HC-0002(17)280701","x_udi_source":"scan"},
    "SN-HC-0003": {"x_udi_di":"04012345678901","x_udi_pi":"(10)LOT-2607-A(21)SN-HC-0003(17)280702","x_udi_source":"scan","x_return_disposition":"requarantine",
                   "x_return_reason":"Surgery cancelled — packaging intact, within sterility window; fresh quality check required before restock."},
    "TRAY-A-001": {"x_sterilization_cycle_count":1,"x_sterilization_cycle_limit":50},
    "TRAY-B-001": {"x_sterilization_cycle_count":50,"x_sterilization_cycle_limit":50}},
  "physicians": {
    "Feldmann": {"x_validation_state":"expired","x_hcp_certification_number":"DE-ORT-4471","x_hcp_certification_expiry":"2026-04-30"},
    "Weber":    {"x_validation_state":"validated","x_hcp_certification_number":"DE-ORT-5512","x_hcp_certification_expiry":"2027-12-31"},
    "Okafor":   {"x_validation_state":"pending_verification"}},
  "invoice": {"INV/2026/00001": {"state":"posted","amount_total":4850.0}},
  # The two extension-layer preview drafts for the same surgery. amount_total is NOT
  # asserted (trial-default tax makes it non-canonical, like S00004) — only existence,
  # draft state, partner, and the shared ref are checked.
  "settlement_split": {"ref":"Settlement split — Surgery SN-HC-0001",
                       "partners":["AOK Bayern","M. Schneider"], "count":2, "state":"draft"},
  # INV/2026/00001's single line must carry 100% analytic distribution across the 3
  # analytic-account ids (resolved by name at audit time — ids are instance-specific).
  "posted_invoice_analytic": {"invoice":"INV/2026/00001", "pct_total":100.0,
                              "accounts":["Orthopedics-KMO","GKV","HipCore"]},
  "automations": ["MDR Credential Gate — Block Confirm on Invalid HCP",
                  "GxP Quarantine Hold — Block Release Before Hold Elapses",
                  "Auto Quality Hold — 90 Days on New Raw Lots",
                  "Sterilization Cycle — Auto-Count and Reuse-Limit Block"],
  "custom_fields": {
    "res.partner": ["x_hcp_certification_number","x_hcp_certification_expiry","x_validation_state"],
    "stock.lot": ["x_hold_release_date","x_udi_di","x_udi_pi","x_udi_pi_batch","x_udi_pi_serial",
                  "x_udi_pi_expiry","x_udi_source","x_sterilization_cycle_count",
                  "x_sterilization_cycle_limit","x_return_disposition","x_return_reason"]},
  "must_not_exist_fields": {  # 0.3.1 — deliberately excluded
    "res.partner": ["x_hcp_device_qualifications","x_consignee_type"],
    "stock.lot": ["x_asset_type","x_last_sterilization_date","x_storage_temp_min","x_storage_temp_max"]},
  "analytic_accounts": ["Orthopedics-KMO","GKV","HipCore"],
  "locations": ["WH/Stock","WH/Quarantine","WH/Quarantine/Disposition","WH/Quarantine/Returns",
                "WH/Consignment","WH/Consignment/Klinikum München","WH/Sterilization"],
  "doc_numbers": ["S00001","S00002","S00004","WH/IN/00002","WH/MO/00004","INV/2026/00001"],
  "refusals": {
    "credential":"Blocked — HCP certification expired or invalid for Dr. M. Feldmann. Order cannot be confirmed (MDR credential gate).",
    "quarantine":"GxP quarantine gate — quality hold active for lot LOT-2607-B until 2026-10-01. Release to stock is blocked.",
    "tray":"Reuse limit reached — tray TRAY-B-001 has completed 50 of 50 sterilization cycles. Dispatch blocked; route to retirement (MDR reusable-device control)."},
}
```

### 4.3 `audit.py` — read back & compare, print ✅/❌ per item
```python
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from api import conn, mk
# paste CANON = {...} here (4.2)

uid, models, common = conn(); ex = mk(models, uid)
ok = bad = warn = 0
def check(label, got, want):
    global ok, bad
    passed = (got == want)
    print(("✅" if passed else "❌"), f"{label:52s} got={got!r} want={want!r}")
    ok += passed; bad += (not passed)
def warn_line(label, got):
    global warn
    print("⚠", f"{label:52s} got={got!r}  (STOP-AND-ASK — not auto-repaired)")
    warn += 1

# IMPORTANT: every search_read/search_count options dict below is passed as KWARGS
# (fields=[...], limit=...), never as a trailing positional dict — see Part 1.2 quirk note.

# counts
for m, n in CANON["counts"].items():
    check(f"count {m}", ex(m,"search_count",[('id','>',0)]), n)
# custom fields present
for model, names in CANON["custom_fields"].items():
    have = ex('ir.model.fields','search_read',[('model','=',model),('name','like','x_')], fields=['name'])
    haveset = {f['name'] for f in have}
    for nm in names: check(f"field {model}.{nm}", nm in haveset, True)
# excluded fields absent
for model, names in CANON["must_not_exist_fields"].items():
    have = {f['name'] for f in ex('ir.model.fields','search_read',[('model','=',model),('name','like','x_')], fields=['name'])}
    for nm in names: check(f"EXCLUDED {model}.{nm} absent", nm not in have, True)
# sale orders — S00004's amount_total is STOP-AND-ASK #1 (computed field, line
# composition unknown); report state normally but WARN on the total instead of ❌.
for name, exp in CANON["sale_orders"].items():
    r = ex('sale.order','search_read',[('name','=',name)], fields=['state','amount_total'])
    if name == "S00004":
        check(f"SO {name} state", (r[0]['state'] if r else None), exp['state'])
        if r and r[0]['amount_total'] == exp['amount_total']:
            check(f"SO {name} amount_total", r[0]['amount_total'], exp['amount_total'])
        else:
            warn_line(f"SO {name} amount_total", r[0]['amount_total'] if r else None)
    else:
        got = (r and {'state':r[0]['state'],'amount_total':r[0]['amount_total']}) or None
        check(f"SO {name}", got, exp)
# lots/serials
for name, exp in CANON["lots"].items():
    fields=list(exp.keys())
    r = ex('stock.lot','search_read',[('name','=',name)], fields=fields)
    got = {k:(r[0].get(k) if r else None) for k in fields}
    check(f"lot {name}", got, exp)
# physicians
for key, exp in CANON["physicians"].items():
    fields=list(exp.keys())
    r = ex('res.partner','search_read',[('name','like',key)], fields=fields)
    got = {k:(r[0].get(k) if r else None) for k in fields}
    check(f"physician {key}", got, exp)
# invoice (posted hero)
for name, exp in CANON["invoice"].items():
    r = ex('account.move','search_read',[('name','=',name)], fields=['state','amount_total'])
    check(f"invoice {name}", (r and {'state':r[0]['state'],'amount_total':r[0]['amount_total']}) or None, exp)
# settlement-split drafts (extension-layer preview) — existence/state/partner/ref only
ss = CANON["settlement_split"]
drafts = ex('account.move','search_read',[('ref','=',ss['ref'])], fields=['state','partner_id'])
check("settlement-split count", len(drafts), ss['count'])
check("settlement-split all draft", all(d['state']=='draft' for d in drafts), True)
draft_partner_names = {d['partner_id'][1] for d in drafts if d.get('partner_id')}
for p in ss['partners']:
    check(f"settlement-split partner {p}", any(p in n for n in draft_partner_names), True)
# posted-invoice analytic_distribution: 100% across the 3 resolved analytic-account ids
pia = CANON["posted_invoice_analytic"]
acct_ids = []
for nm in pia['accounts']:
    r = ex('account.analytic.account','search_read',[('name','=',nm)], fields=['id'])
    acct_ids.append(r[0]['id'] if r else None)
inv = ex('account.move','search_read',[('name','=',pia['invoice'])], fields=['id'])
lines = ex('account.move.line','search_read',[('move_id','=',inv[0]['id']),('display_type','=',False)], fields=['analytic_distribution']) if inv else []
dist = lines[0]['analytic_distribution'] if lines else {}
dist_ids = {int(k) for k in (dist or {}).keys()}
pct_sum = sum((dist or {}).values())
check("posted invoice analytic covers 3 accounts", acct_ids and dist_ids == set(acct_ids), True)
check("posted invoice analytic sums to 100%", round(pct_sum,2) if dist else None, pia['pct_total'])
# automations
autos = {a['name'] for a in ex('base.automation','search_read',[('id','>',0)], fields=['name'])}
for nm in CANON["automations"]: check(f"automation {nm[:30]}", nm in autos, True)
# analytic accounts
accts = {a['name'] for a in ex('account.analytic.account','search_read',[('id','>',0)], fields=['name'])}
for nm in CANON["analytic_accounts"]: check(f"analytic acct {nm}", nm in accts, True)
# locations internal
for cn in CANON["locations"]:
    r = ex('stock.location','search_read',[('complete_name','=',cn)], fields=['usage'])
    check(f"loc {cn}", (r[0]['usage'] if r else None), "internal")
# document numbers exist (across models)
for dn in CANON["doc_numbers"]:
    found = (ex('sale.order','search_count',[('name','=',dn)]) or ex('stock.picking','search_count',[('name','=',dn)])
             or ex('mrp.production','search_count',[('name','=',dn)]) or ex('account.move','search_count',[('name','=',dn)]))
    check(f"doc# {dn}", bool(found), True)

print(f"\n{'ALL ✅' if bad==0 else '❌ FAILURES'} ({ok}/{ok+bad})  ⚠ warnings (STOP-AND-ASK, not auto-repaired): {warn}")
```
**Fire-tests** (run separately — a real `xmlrpc.client.Fault` from `execute_kw` cannot be asserted with `==`; the transport wraps the `UserError` text inside `faultString` alongside a traceback header, so match by **substring**):
```python
import xmlrpc.client
from api import conn, mk
uid, models, common = conn(); ex = mk(models, uid)

def fire_test(label, action, expect_substring):
    try:
        action()
        print("❌", label, "— expected a blocking Fault, none raised")
    except xmlrpc.client.Fault as f:
        hit = expect_substring in f.faultString
        print(("✅" if hit else "❌"), label, "— substring", "found" if hit else "MISSING", f"(expected: {expect_substring[:60]}...)")

so1 = rec_id(ex, 'sale.order', 'S00001')
lotB = rec_id(ex, 'stock.lot', 'LOT-2607-B')
trayB = rec_id(ex, 'stock.lot', 'TRAY-B-001')

fire_test("credential gate (S00001 confirm)", lambda: ex('sale.order','action_confirm',[so1]), CANON['refusals']['credential'])
# LOT-2607-B release / TRAY-B-001 dispatch fire-tests are executed as the internal-transfer
# attempts described in Stage F/Part 3; wrap each transfer's `button_validate` call the same
# way, matching CANON['refusals']['quarantine'] / CANON['refusals']['tray'] by substring.
```

### 4.4 REMEDIATION TABLE — for each ❌, the exact repair
| ❌ Symptom | Deterministic repair |
|---|---|
| Custom field missing | Re-run its Stage E `ir.model.fields` create (exact spec above) |
| Field wrong type / missing selection key | Unlink the field, recreate with the exact Stage E spec, re-write dependent record values from `CANON` |
| Excluded field present (0.3.1) | Unlink it (it should never have been created) |
| Automation missing / code wrong | Re-run its Stage F create with the verbatim block; relink server action |
| Refusal string mismatch | Overwrite the linked `ir.actions.server.code` with the verbatim block; re-run the fire-test |
| Hold/expiry date wrong | `write` the canonical date (0.6): LOT-2607-B→2026-10-01, LOT-2607-A→2026-07-02, serials→2028-07-01/02 |
| Record value wrong (state/total/cycle/UDI/disposition/reason) | `write` the exact `CANON` value onto the record |
| Count too LOW | Diff live names vs the expected named set; create the missing record via its Stage-I recipe |
| Count too HIGH | Find the extra by name; if a build artifact (leftover `ZZ`/test lot), zero its quant via inventory adjustment and neutralise |
| Document number wrong | Fix `ir.sequence.number_next` for that model and recreate the mis-numbered record |
| Analytic distribution missing/wrong | `write` `analytic_distribution` on the invoice line = `{"<3 acct ids joined by comma>":100.0}` |
| Location missing / not internal | Create/fix the `stock.location` (usage=internal, correct parent) |
| Physician state/cert wrong | `write` the exact `CANON['physicians']` values |
| Analytic account missing (Orthopedics-KMO/GKV/HipCore not found) | Re-run Stage C's `account.analytic.account` create for the missing name(s) under the correct plan; re-resolve `acct_ids` and re-write `analytic_distribution` |
| Settlement-split draft missing/wrong (count/state/partner/ref) | Re-run Stage I.7's two draft-invoice creates with the exact ref `"Settlement split — Surgery SN-HC-0001"` and partners AOK Bayern (90%)/M. Schneider (10%) |
| SO S00004 amount_total ⚠ (does not match 5820.0) | **Not auto-repaired** — this is STOP-AND-ASK #1 (computed field, line composition unknown). Do not guess a line breakdown; halt and ask the user per Part 6 |

### 4.5 The heal loop
```
run audit.py
while any ❌ and passes < 3:
    for each ❌: apply its Remediation Table repair
    run audit.py
if still ❌ or an item is a STOP-AND-ASK: HALT, print (item, expected, actual, repair tried), ask the user
else: print "ALL ✅" table  → this is the deliverable proof
```

---

## PART 5 · MANUAL-UI APPENDIX & PITFALLS

### 5.1 Steps that are MANUAL (UI, not API) on a trial
- **App installation** (Stage A.2) — Apps menu, Activate each; verify menus appear.
- **Some settings toggles** — if a `res.config.settings` write is refused, set it in Settings UI (Inventory / Accounting) and Save.
- **"MDR Compliance — UDI & Quality" form section** — open a stock.lot, toggle Studio, add a group/section titled exactly that, drag the 11 built fields in; reload and confirm they render. (The audit only checks the fields exist and hold correct values; grouping is cosmetic but expected for the demo screenshots.)
- **Company logo** (optional) — Settings → Companies → upload; purely cosmetic.

### 5.2 What NOT to do
- Never hardcode a model/field/record id from the old system — resolve by lookup.
- Never let an auto-stamped hold/expiry date stand — always apply the 0.6 overrides.
- Never skip a stage's VERIFY.
- If a refusal string differs, fix the **rule code**, never the expectation.
- Never confirm S00001; never release LOT-2607-B; never dispatch TRAY-B-001 — the blocked states ARE the assets.
- Never print the odoo.com account password.

---

## PART 6 · EXECUTOR OPERATING CONTRACT (follow literally)

1. **Run the Part 0.6 date check FIRST.** If it prints the STOP-AND-ASK, stop and ask the user.
2. **Execute Stages A → I in order.** Run each stage's VERIFY before moving on. A stage ❌ is fixed immediately via the Part 4 Remediation Table — never deferred.
3. **After Stage I, run the Part 4 heal loop to convergence** (max 3 passes).
4. **On any STOP-AND-ASK** (S00004 €5,820 composition; the date collision; or an item still ❌ after 3 passes), **HALT and ask the user** with the precise expected-vs-actual — do not improvise a value.
5. **Paste the final "ALL ✅ (N/N)" audit table** as the proof of a clean rebuild.

**Golden rule:** the canonical dataset embedded in this document is truth; the live instance is wrong wherever it differs; repair the instance, never edit the expectation.

*End of runbook.*
