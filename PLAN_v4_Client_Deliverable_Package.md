# Plan — v4 Client-Facing Deliverable Package
## What Capgemini / Deloitte / IBM / Accenture actually leave behind at pitch stage — and how we get there from what we already have

**Purpose of this document:** a build plan, not a deliverable. Nothing in here goes to the client. It exists so the next work session executes against a specific, gap-checked list instead of improvising.

---

## 0. The distinction that governs every decision below

There are two categories of ERP consulting documents, and conflating them is the single most common mistake a mid-level candidate makes:

| | **Pitch-stage / pre-sales leave-behind** | **Delivery-stage / post-contract execution** |
|---|---|---|
| When | Before a signed contract, to win the work | After signature, during the engagement |
| Purpose | Prove methodology maturity, fit, and vision | Actually execute the validated build |
| Examples | Solution Design, Architecture Blueprint, CSV **Strategy**, Roadmap, SOW **shape**, RTM | Executed URS/FRS sign-offs, IQ/OQ/PQ **protocols with real test data**, signed RACI with named client staff, final commercial SOW with negotiated numbers |
| Fabricating the wrong one | — | Signals you don't understand the sales cycle — a real CIO would ask "who signed this?" |

**Governing rule for this plan:** every new document is a pitch-stage artifact. Where a Big 4 firm would show a *template with the shape and logic filled in and the client-specific numbers left as placeholders* (matching the discipline already used throughout this whole project — the fee line, the date line), we do the same. We do not fabricate a signed SOW, a named RACI, or an executed validation protocol. That would be a *regression* in the honesty discipline that has been this package's differentiator through five rounds.

---

## 1. Target deliverable set — reasoned from first principles, not just the pasted research

Your pasted research is a solid start (it correctly identifies the Executive Deck, Process Maps, Roadmap, Functional Design, Tech Architecture, GxP Strategy, Demo assets). Independently reasoning through what Capgemini/Deloitte/IBM/Accenture actually hand over at this exact stage — a competitive pitch for a regulated-industry ERP transformation — surfaces **four categories your research didn't name**, because they are more "consulting craft" than "content," and they're exactly what separates a mid-level submission from a Principal-level one:

1. **Requirements Traceability Matrix (RTM)** — confirmed via research as a near-universal artifact: Requirement → Source → Odoo Module/Mechanism → Fit or Gap → Config/Extension → Test Case ID. This is the single document a technical CIO trusts most, because it's checkable line by line — and we already have 90% of its content scattered across the Object Schema and GxP regression suite. It has just never been assembled as *its own document*, which is the format the CIO actually expects.
2. **Statement of Work (shape, not signed)** — scope in/scope out, deliverables list, assumptions, exclusions, commercial structure (fee still placeholder, consistent with everything else). Real Big 4 leave-behinds almost always include this even pre-contract, because it signals "we know exactly what we're proposing to sign up for," which is a trust signal distinct from the pitch narrative.
3. **Risk & Assumptions Register** — a named list of what could go wrong and how it's mitigated (data quality, adoption resistance, EUDAMED timeline pressure, Field-Service-unavailable-on-trial class of caveats). Surfacing your own risks before being asked is a specific, well-known Big 4 tell of seniority.
4. **Change Management / Adoption One-Pager** — most ERP failures are adoption failures, not technology failures, and *every* major firm includes at least a page on this. We have zero coverage of it today, and it is a one-page, high-leverage gap.

Two more genuine gaps, lower priority:

5. **True visual process diagrams (BPMN/swimlane).** Our Value Stream spec is excellent *prose and tables* — but "the digital thread" as a literal drawn diagram (boxes, arrows, swimlanes per department) is what your research calls out and what a CIO expects to see, not just read. This is a rendering-format gap, not a content gap — we already have every fact needed.
6. **Data Migration & Cutover one-pager** — content already exists buried in GxP Plan §6; it deserves its own short, visual document because migration risk is usually the first thing a CIO's own team raises internally after the pitch.

## 2. Full target list, mapped against what we already have

| # | Target deliverable | Do we have the CONTENT already? | Where | Format gap? | Priority |
|---|---|---|---|---|---|
| 1 | Executive Pitch Deck | ✅ Yes | v3: deck.pptx, blueprint, script | None | — |
| 2 | Strategic Memorandum (exec pre-read) | ✅ Yes | v3: Strategic Memo | None | — |
| 3 | Integrated Process Maps ("Digital Thread") | ⚠️ Content yes, format no | v3: Value Stream spec (tabular) | **Yes — needs true BPMN/swimlane diagram render** | HIGH |
| 4 | Operational / Implementation Roadmap | ⚠️ Partial | Slide 12 (4 phases, no durations/workstreams) | **Yes — needs its own visual Gantt-style one-pager** | HIGH |
| 5 | Functional Solution Design (Requirement→Module map) | ⚠️ Content yes, never assembled as its own doc | Object Schema (native/extension), Value Stream | **Yes — assemble as Requirements Traceability Matrix** | **HIGHEST — biggest gap** |
| 6 | Technical Architecture Blueprint (diagram) | ⚠️ Content yes, format no | Object Schema (prose/tables) | **Yes — needs an actual system/data-flow diagram** | HIGH |
| 7 | GxP Validation **Strategy** | ✅ Yes, correctly scoped as strategy not execution | v3: GxP Validation Plan | None — already correctly pitch-stage, not over-delivered | — |
| 8 | Demo "Golden Path" / UAT Script | 🔶 In progress this session | uat/shots.py + build log | Being built now | IN PROGRESS |
| 9 | System Demo Walkthrough (screenshots/video) | ✅ Yes | v3: 09_Video_Production + Live Demo Evidence | None | — |
| 10 | **Requirements Traceability Matrix (standalone)** | ❌ Net new (content exists, never assembled) | — | New document | **HIGHEST** |
| 11 | **Statement of Work (shape)** | ❌ Net new | — | New document | HIGH |
| 12 | **Risk & Assumptions Register** | ❌ Net new | — | New document | HIGH |
| 13 | **Change Management / Adoption one-pager** | ❌ Net new | — | New document | MEDIUM |
| 14 | **Data Migration & Cutover one-pager** | ⚠️ Content buried in GxP §6 | GxP Validation Plan §6 | Extract + visualize | MEDIUM |
| 15 | Horizon 2 Roadmap (upsell) | ✅ Yes | Horizon_2_Package.zip | None | — |
| 16 | Technical Assurance Report | ✅ Yes (internal, not client-facing) | Technical_Assurance_Report.pdf | Stays internal | — |

**Reading this table straight: 6 of 16 target deliverables are genuinely net-new content; 4 are format-only gaps (the content already exists and is verified — we're re-presenting it, not re-researching it); 6 are already done.** That is a much smaller lift than it first sounds, and it's the right way to scope this — most of the "new" work is assembly and visualization of facts we've already verified against the live instance, not fresh research.

---

## 3. Build plan — sequenced, with source material named for each

### Phase A — Assemble from existing verified content (fast, low-risk, do first)
1. **Requirements Traceability Matrix** — pull every requirement from the original case brief (Sales/Marketing, Accounting, Logistics, Purchasing, CEO) and every one of the 19 regression test cases (TC-01–TC-19) from the GxP Plan; join them against the Object Schema's native/extension mapping. Output: one table, ~25–30 rows, columns = *Case Requirement → Odoo Mechanism → Native/Extension → Regression Test ID → Verified Status*. This is mechanical assembly of facts already fire-tested — the fastest, highest-trust document to produce.
2. **Data Migration & Cutover one-pager** — extract GxP Plan §6 (parallel-run window, record-state treatment table, reconciliation log) into its own short visual document with a simple before/after diagram.

### Phase B — New visual diagrams (content is fully known; this is rendering work)
3. **Digital Thread process diagram** — true swimlane/BPMN-style rendering of the Value Stream's six stages + Stage 4B + the instrument loop, department lanes (Purchasing/Quality/Logistics/Sales/Field Service/Finance) across the top, matching the house visual style already established in the video frames.
4. **Technical Architecture diagram** — one-page system diagram: five core Odoo apps + CRM/Field Service, the five named extension-layer components, data flow arrows, and the Odoo.sh deployment tier — visual counterpart to the Object Schema's prose.
5. **Roadmap Gantt-style one-pager** — expand Slide 12's four phases into a proper phased roadmap with workstreams (Sales/Quality, Manufacturing/Finance, Validation, Go-Live) as swimlanes and relative durations — still no fabricated dates, consistent with the existing "confirmed in discovery" discipline.

### Phase C — Genuinely new written content (requires drafting, kept to the same honesty discipline)
6. **Statement of Work (shape)** — scope in/out, deliverable list (mirrors this very package), assumptions & dependencies, exclusions, commercial structure with the fee left as the same placeholder used throughout. This is the one document where over-specifying would be actively dishonest — keep it disciplined.
7. **Risk & Assumptions Register** — 8–10 named risks (data quality at cutover, EUDAMED timeline pressure, adoption resistance in Sales/Logistics, extension-layer validation cost, trial-tier Field Service gap, consignment valuation config effort) each with a mitigation, in the same register format a Big 4 firm would leave behind.
8. **Change Management / Adoption one-pager** — stakeholder map (five departments + CEO + CIO), a simple adoption curve narrative, and the specific point already proven in the rebuttal playbook ("the block isn't a new rule, it's the rule they already follow — now enforced") reused as the core adoption argument.

### Phase D — Finish the in-progress UAT + Functional Spec (already underway)
9. Finish the 16-scenario annotated UAT script (screens already rendered this session) as its own PDF.
10. Produce the Principal-grade Functional Specification (step-by-step build breakdown with the same screenshots, in the SAP/IBM functional-spec format previously requested) — this absorbs and formalizes the Technical Assurance Report's verified facts rather than duplicating them.

### Phase E — Assembly
11. New template pass consistent with the existing house style (same navy/amber/teal system, same footer).
12. Assemble into a **new, separate zip** — a genuine client-facing "Solution Design & Validation Package" distinct from the interview-prep v3 zip — with its own START_HERE index explaining what's client-appropriate vs. what stays in your back pocket.
13. Cross-check pass: re-verify every new document's technical claims against the live instance one more time before finalizing (same discipline as the Technical Assurance Report).

---

## 4. What this plan deliberately does NOT do

- **No executed validation protocols** (IQ/OQ/PQ test runs) — that's delivery-phase and would look premature pre-contract.
- **No fabricated commercial numbers** in the SOW — placeholder discipline continues.
- **No invented named stakeholders** in the RACI/adoption content — roles and functions only (e.g., "Quality Lead," "CIO"), never invented names on the client side.
- **No duplicate documents** — where format-only gaps exist (process maps, architecture, roadmap), we visualize existing verified content; we do not re-research it.

## 5. Effort estimate for the next session

| Phase | Item count | Relative effort |
|---|---|---|
| A — Assembly | 2 docs | Low |
| B — New diagrams | 3 diagrams | Medium (design-heavy, not research-heavy) |
| C — New written content | 3 docs | Medium |
| D — UAT + Functional Spec | 2 docs | Medium–High (already in progress) |
| E — Template + zip assembly | — | Low |

**Total new client-facing documents in the v4 package: 10** (RTM, Migration one-pager, Process diagram, Architecture diagram, Roadmap one-pager, SOW shape, Risk Register, Change Management one-pager, UAT Script, Functional Specification) — on top of the six already-complete assets carried forward from v3.

---

## Decision point — confirm before I build

1. **Proceed with all of Phase A–E as scoped above?** Or trim anything (e.g., skip the SOW if you'd rather not show a document shape with fee still blank)?
2. **Should the new zip fully replace v3 as what you submit, or sit alongside it** (v3 = interview-prep + evidence trail you keep; v4 = the clean client-facing "Solution Design Package" you actually send)? My recommendation is the latter — it matches the audience-separation discipline already established (send memo + deck + this new package; keep the rest as your prep).
3. Confirm and I'll execute Phases A→E in order, finishing the UAT script and Functional Specification already underway in Phase D as part of the same pass.
