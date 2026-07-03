# much. Consulting — "The Compliant Digital Thread"
## 5-Minute Future-State Demo Video · Production Blueprint
**Client:** MDR Devices Medizintechnik GmbH · **Recording environment:** the live demo instance (mdr-devices-test.odoo.com) — every visual cue below is a real screen that exists today, not a mockup to be fabricated.
**Companion documents:** Tasks 1–2 (strategic narrative, bridge table, cheat sheet, gap fixer) are in `PITCH_Principal_Consultant_Briefing.md`; the walkthrough details per screen are in `BUILD_LOG_VERIFIED.md`.

---

## Production parameters

| Parameter | Specification |
|---|---|
| Runtime | 5:00 hard ceiling (script below ≈ 690 narrated words @ ~140 wpm + breathing room) |
| Capture | Screen-record the live instance. Browser: clean profile, no bookmarks bar, 100% zoom, 1080p. Odoo dark or light theme — pick one, never mix |
| Audio | Record narration separately after capturing video; match pace in edit. One take per scene beats one take overall |
| Tooling | OBS / Loom / QuickTime for capture; captions ("Annotation Layer") added in edit — keep them to ≤ 8 words each |
| Golden rule | If a screen carries the label *extension-layer preview*, the narration says so. The video's credibility is the pitch's credibility |

---

## SCENE 1 — The Challenge (0:00 – 0:30)

| Visual Cue | Narrated Script | Annotation Layer |
|---|---|---|
| Slide 2 from the deck: four bordered boxes — QMS / LIMS / Field Service / Legacy ERP — broken dotted lines, an implant icon crossing all four with question marks. Hold static 8s, then slow zoom on the white space *between* the boxes | "MDR Devices runs four systems of record. Each one does its job. But an implant's journey — from vendor, to quarantine, to a surgeon's hands, to an invoice — crosses all four. And no system owns that journey. Today, compliance lives in the white space between these tools: enforced by memory, by habit, by the person who's been here longest. That is a standing MDR Article 27 exposure — and it compounds with every product you add." | `4 systems. 0 shared views.` → then, on the zoom: `Audit risk lives in the handoffs` |

## SCENE 2 — The Unified Vision (0:30 – 1:00)

| Visual Cue | Narrated Script | Annotation Layer |
|---|---|---|
| Cut to the live instance: Odoo home menu, **"MDR Devices Medizintechnik GmbH"** visible in the header. Cursor sweeps across Inventory, Manufacturing, Quality, Sales, Purchase, Accounting tiles — one deliberate pass, no clicking | "This is the alternative — and everything you're about to see is live, not a mockup. One platform. One data model. One definition of 'compliant' that every department inherits instead of inventing. Five core applications carry the flow; where standard Odoo genuinely stops short, we extend it deliberately — and we'll tell you exactly where. We don't sell zero custom code. We sell named custom code." | `One validated source of truth` · `Native core + named MedTech extensions` |

## SCENE 3 — The Serialized Journey (1:00 – 4:10)

### 3a · Procurement → Quarantine (1:00 – 1:40) — ⚑ COMPLIANCE CALL-OUT 1
| Visual Cue | Narrated Script | Annotation Layer |
|---|---|---|
| Inventory → Lots/Serials → **LOT-2607-B**. Show the *MDR Compliance* panel: hold release **01-10-2026**. Then: attempt an internal transfer out of WH/Quarantine → **the red block appears**. Hold on the error 3 full seconds | "The journey starts at goods-in. Every raw material lot routes automatically into quarantine — there is no path around it — and the system stamps its ninety-day quality hold the moment it's created. Nobody remembers the hold. Nobody tracks it in a spreadsheet. And here's what matters: watch what happens when someone tries to release this lot early. **The system refuses.** That's the difference between a procedure and a control. A procedure failed the day your best warehouse manager was on holiday. This can't." | ⚑ `SYSTEM IMPROVEMENT — the failure point eliminated: early release by human error. The hold is structural, not procedural` |

### 3b · Manufacturing → UDI genealogy (1:40 – 2:20)
| Visual Cue | Narrated Script | Annotation Layer |
|---|---|---|
| Open serial **SN-HC-0003** → UDI panel (DI, PI batch LOT-2607-A, serial, expiry) → click **Traceability**. Let the full chain render: vendor lot → quarantine → MO → serial → hospital → return. Slow scroll through every row | "Released material becomes an implant — and at birth, that implant gets its complete regulatory identity: Device Identifier, Production Identifier, batch linkage, sterility clock. This screen is the one your auditor asks for: the complete genealogy of one implant, from the vendor's titanium lot to the patient event — one click, eleven rows, zero reconstruction. Today, assembling this evidence takes your team days per device. Here, it's a database property." | `EU MDR Art. 27: full genealogy, one click` · `Audit evidence: days → seconds` |

### 3c · The credential gate (2:20 – 3:00) — ⚑ COMPLIANCE CALL-OUT 2 · *the money shot*
| Visual Cue | Narrated Script | Annotation Layer |
|---|---|---|
| Sales → open **S00001** (Dr. M. Feldmann) → contact preview showing *Expired, 04/2026* → click **Confirm** → **red banner: "Blocked — HCP certification expired…"**. Hold 3s. Then flash **S00004** (Dr. Okafor, locum): confirmed, with the *credential verification* activity visible | "Before any implant ships, the system asks a question no one asks reliably today: is this surgeon still certified? Doctor Feldmann's certification lapsed in April. His order **cannot be confirmed** — not 'shouldn't be' — cannot. And the design knows the real world: a visiting locum with no record yet isn't blocked, but routed to a credential review queue, because a hard block there would be operationally wrong. Compliance is now a property of the sales process itself — not a training slide." | ⚑ `SYSTEM IMPROVEMENT — the failure point eliminated: shipment to an uncertified physician. Hard block for expired; review queue for unknown` |

### 3d · Consignment, sterilization loop, returns (3:00 – 3:40) — ⚑ COMPLIANCE CALL-OUT 3
| Visual Cue | Narrated Script | Annotation Layer |
|---|---|---|
| Location view: **SN-HC-0002 at WH/Consignment/Klinikum München**. Cut to the two trays side by side: TRAY-A-001 *cycle 1/50* and TRAY-B-001 *cycle 50/50* → attempt to dispatch TRAY-B → **blocked: "Reuse limit reached… route to retirement"**. End on SN-HC-0003 in *Quarantine/Returns*, disposition "Re-Quarantine — surgery cancelled" | "At the hospital, consigned implants stay on your balance sheet — location-driven valuation an auditor can verify, not a spreadsheet estimate. Instrument trays run their own loop: every sterilization cycle counted automatically, and when a tray reaches its manufacturer's reuse limit — watch — **it refuses to ship.** An over-cycled kit physically cannot reach an operating theatre. And when a surgery is cancelled? The return flows back with a logged disposition. The thread shows the return. It never shows a gap." | ⚑ `SYSTEM IMPROVEMENT — the failure point eliminated: over-cycled instruments reaching surgery. Cycle 50/50 = no dispatch, no exceptions` |

### 3e · Financial reconciliation (3:40 – 4:10)
| Visual Cue | Narrated Script | Annotation Layer |
|---|---|---|
| Invoice list filtered to the three settlement documents → open **INV/2026/00001** → hover the analytic widget: Cost Center / Payer Type / Product Line. Show the insurer + co-pay drafts sharing the reference | "Surgery complete — and the money follows the clinical event, structurally. Every invoice line carries three analytic dimensions the moment it's generated: cost center, payer, product line. The insurer-and-co-pay split you see beside it is generated by our named extension layer — we're precise about that boundary — but the thread that ties every payer document back to one surgical event? That's native, and it's what turns claims reconciliation from a month-end spreadsheet exercise into a query." | `One clinical event → every payer document` · `Extension layer: named, scoped, validated separately` |

## SCENE 4 — Close (4:10 – 5:00)

| Visual Cue | Narrated Script | Annotation Layer |
|---|---|---|
| Return to the traceability report, slow zoom out; cross-fade to Slide 12 (Roadmap & The Ask). Hold The Ask box for the final 10 seconds | "One implant. One thread. Every control you just watched fire is running in a live system today — built to the same pattern we've proven across regulated device manufacturing: native platform wherever it holds up under audit, five named extensions where it doesn't. What we're proposing is simple: a fixed-fee, three-week Discovery Sprint — your credential gating and quarantine automation, live on your own data, in your own sandbox, before your next board update. You're not buying software. You're securing the regulatory future of every device you'll ever ship. We need your decision within five business days — and we're ready to start." | `Fixed fee · 3 weeks · your data` → final card: `much. Consulting — One Compliant Thread. From Receipt to Patient.` |

---

## Director's notes (the difference between good and masterpiece)

1. **Let the blocks breathe.** The three refusal moments (3a, 3c, 3d) are the entire video. Freeze 3 seconds on each red banner; the silence does the selling.
2. **Cursor discipline.** Move slowly, in straight lines, and never circle. A wandering cursor reads as improvisation; this must read as inevitability.
3. **Record scenes separately**, narrate after, assemble in edit. Re-record any scene where a screen loads slower than 2 seconds — or cut the wait.
4. **The honesty beats stay in.** "Named custom code" (Scene 2) and "generated by our named extension layer" (3e) are not hedges to trim for time — they're the differentiator; a panel of Odoo experts will notice their absence faster than their presence.
5. **Timing check:** narration ≈ 690 words. At a measured 140 wpm that's 4:55. If you run long, cut from Scene 2 — never from a call-out or the ask.
6. **Fallback:** if video production isn't feasible before submission, this blueprint *is* the live-demo script — the same five scenes, presented by hand in the pitch, in the same order, with the same three freeze-moments.

---

## Technical Annotation Guide — much. Consulting brand standard

**Design intent:** the annotations must read as *engineering markings on a validated system*, not marketing decoration. Minimal, precise, and always subordinate to the live screen. If an overlay competes with the Odoo UI for attention, delete the overlay.

### Color system
| Token | Value | Use |
|---|---|---|
| Ink Navy | `#16233F` | Annotation text, lower-third bars, end card background |
| Slate | `#5A6577` | Secondary/context captions ("where we are in the thread") |
| Signal Amber | `#B07A1E` | The three ⚑ System Improvement call-outs — *reserved exclusively for them*, three uses in five minutes |
| Block Red | `#A63232` | Never drawn by us — the red comes from Odoo's own error banners; our overlays go silent during blocks (see Motion rules) |
| Verified Teal | `#0E7A6F` | Checkmark micro-icons on "live / fire-tested" captions |
| Paper | `#FFFFFF` at 92% opacity | Caption background chips, 2px radius, no drop shadows |

### Typography
| Element | Spec |
|---|---|
| Annotation captions | Inter (or Helvetica Neue) Medium, 22–24px @1080p, Ink Navy on Paper chip, sentence case, ≤ 8 words |
| ⚑ call-out cards | Inter Semibold 26px headline + Regular 20px sub-line, max 2 lines, Signal Amber left border 3px |
| Kicker labels (scene openers) | Inter Semibold 14px, ALL CAPS, +2.2px letter-spacing, Slate — mirrors the document template's kicker style |
| End card | "One Compliant Thread. From Receipt to Patient." — Inter Light 40px centered, Paper on Ink Navy; much. Consulting wordmark bottom-right, 60% scale |

### Motion rules
1. **Enter/exit:** captions fade in 200 ms, hold ≥ 3 s, fade out 200 ms. No slides, bounces, or wipes — ever.
2. **Arrows & highlights:** a single 2px Ink Navy underline or rounded-rectangle outline drawn on in 300 ms to indicate a field (e.g., the hold-release date, the analytic widget). One highlight on screen at a time. No animated arrows.
3. **The silence rule:** when an Odoo red block banner appears (Scenes 3a, 3c, 3d), *all overlays exit first*. The screen holds the native error alone for a full 3 seconds; the ⚑ Signal Amber call-out card enters only after. The product's own refusal is the star; the annotation is the caption to it.
4. **Zoom:** max 115%, ease-in-out, only to make a field legible — never for drama.
5. **Cursor:** system default, no click-ripple effects; deliberate straight-line movement (see Director's notes).

### Audio & pacing
- Voice-over: measured ~140 wpm, one tone — advisor, not advertiser. No music under Scenes 3a–3d (the blocks land harder in silence); optional low ambient bed ≤ −28 LUFS under Scenes 1–2 and 4 only.
- Scene transitions: hard cuts. Cross-fade permitted exactly once — into the end card.

### Compliance-grade finish
- Every caption stating a test result carries the Verified Teal ✓ and the word *live* or *fire-tested* — and must be literally true in the recorded instance.
- The extension-layer boundary caption in Scene 3e (`Extension layer: named, scoped, validated separately`) may not be cut for time under any edit pressure — it is the brand.
- Export: 1080p H.264, 16:9, captions burned in; filename `much_consulting_MDR_Devices_FutureState_Demo_v1.mp4`.
