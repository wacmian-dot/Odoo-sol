# Horizon 2 — "The Thread Doesn't End at the Invoice"
## The upsell that turns compliance from a cost centre into a product
**much. Consulting · MDR Devices Medizintechnik GmbH — the slide you show after they've bought the first one**

---

## Why this exists (the interview logic)

Every candidate will pitch the system MDR Devices asked for. Almost none will answer the question a Partner is silently scoring: *"does this person see the engagement after this engagement?"* Horizon 2 is that answer — three moves that all run on data the Compliant Digital Thread **already captures**, which is precisely what makes them credible rather than speculative. The pitch line: *"Everything I've shown you today was Horizon 1. Here's what the same thread earns you next — and one of these has a legal deadline in four months."*

---

## Move 1 — The EUDAMED Autopilot ⏰ *the urgent one, with a real date*

**The regulatory fact (verified, current):** EUDAMED's first four modules — including **UDI/Device registration** — became **mandatory on 28 May 2026** ([European Commission](https://health.ec.europa.eu/latest-updates/eudamed-four-first-modules-will-be-mandatory-use-28-may-2026-2025-11-27_en), [MedTech Europe](https://www.medtecheurope.org/2026/06/04/eudamed-reaches-a-major-milestone-mandatory-use-of-the-first-four-modules-begins/)). New devices must be registered **before being placed on the market**; **legacy devices must be registered by 27 November 2026** ([Obelis](https://www.obelis.net/news/eudamed-becomes-mandatory-on-28-may-2026-deadlines-for-actor-device-and-certificate-registrations/), [Registrar Corp](https://www.registrarcorp.com/blog/medical-devices/medical-device-registration/eudamed-2026-registration/)).

**The pitch moment:** as of the pitch date, MDR Devices is **~4 months from the legacy-device registration deadline** — a compliance obligation they carry *today*, whether or not they buy anything. Most manufacturers are handling it with spreadsheets and manual data entry into the EUDAMED portal.

**The proposal:** the thread already holds every field EUDAMED's UDI/Device module wants — UDI-DI from the product template, PI structure, manufacturer data, device attributes. The Autopilot is an extension-layer module that:
- generates EUDAMED-conformant device registration datasets directly from `product.template` / `stock.lot`,
- maintains a **submission queue with acknowledgement tracking** (submitted / acknowledged / rejected — each state audit-trailed),
- runs the **legacy-device bulk registration** as a one-time managed service before 27 November,
- and keeps registrations synchronized when device data changes — because EUDAMED is not a one-shot filing.

**Why it lands:** it has a date, a penalty for inaction, and a data source you've already built. It converts "nice roadmap" into "you need this by November regardless — the only question is whether you type it by hand."

## Move 2 — The Patient Implant Passport 🫀 *the emotional one nobody else will have*

**The regulatory fact:** **MDR Article 18** obliges manufacturers of implantable devices to supply an **implant card** with the device — carrying device name, serial/lot, **UDI**, manufacturer details — plus **patient-accessible information kept updated on the manufacturer's website**, in the patient's language, understandable to a lay person ([MDCG 2019-8 v2](https://www.eclevarmedtech.com/en/mdcg-2019-8-v2-implant-card-relating-to-the-application-of-article-18-regulation-eu-2017-745-of-the-european-parliament-and-of-the-council-of-5-april-2017-on-medical-devices-and-mdcg-2021-11/), [Clin R](https://clin-r.com/eu-mdr-requirements-for-implant-cards/)). Orthopedic joint implants — MDR Devices' core product — are squarely in scope (the Article 18 exemption list covers minor hardware like screws, plates and wires, not femoral stems).

**The proposal:** the moment Field Service marks *Surgery Complete* and the consumption move fires — the event the thread already owns — the system automatically:
1. **generates the Article 18 implant card** (wallet format, print-ready PDF) populated from the serial's UDI record: device, DI/PI, implant date, implanting institution — zero manual transcription;
2. **publishes the patient-facing device page** on the Odoo portal (native Website/Portal module): lay-language device information, safety notices, multilingual per Member State requirement, *updated automatically* when the device record changes — which is the exact "kept updated on the website" obligation almost every manufacturer currently fails quietly;
3. prints a **QR code on the card** linking to that page — so the patient, or an emergency clinician, reaches the device record in seconds.

**Why it lands — three registers at once:**
- **Regulatory:** it closes a live Article 18 obligation as a *by-product of the consumption event* — no new data entry anywhere.
- **Emotional (the boardroom moment):** *"Today, the thread ends at your invoice. With this, it ends in the patient's pocket — and when a patient in an A&E anywhere in Europe is asked 'what's in your hip?', the answer is a scan of a card your ERP printed automatically."* No competing candidate will have this.
- **Commercial:** it makes compliance *visible to the customer* — hospitals and surgeons see a manufacturer whose devices come with a digital passport. Compliance stops being overhead and becomes product differentiation MDR Devices can sell on.

**Honest scope note (keep the brand):** the card layout and content per MDCG 2019-8 and per-Member-State language rules are a defined design task; the portal page is native Odoo Website capability; the auto-generation trigger is the same automation pattern proven six times in the live demo. Extension-layer item, Category 5 validation, sized in discovery.

## Move 3 — The Compliance Copilot 🤖 *the platform-currency one, governed honestly*

**The platform fact:** Odoo 19 ships **native AI agents** (RAG-trained on your own records and documents, able to query live data and draft actions) and **AI fields/server actions** — embedded in the platform, not a bolt-on ([Odoo 19 AI agents documentation](https://www.odoo.com/documentation/19.0/applications/productivity/ai/agents.html)). The demo instance already carries the AI module set.

**The proposal:** an AI agent trained on the thread and the QMS documentation, scoped to three jobs:
- **Natural-language audit retrieval:** *"Show me every lot that breached its storage envelope in the last 12 months, and where those devices are now"* → grounded answer from live `stock.lot` / `quality.check` data, with the records linked. The auditor-facing hours saved are the same "weeks to same-day" argument — compressed again.
- **Deviation & CAPA drafting:** first-draft deviation summaries and trend narratives from quality check data — drafted by AI, **reviewed and released by a human, always**.
- **PMS trend watch:** periodic scan of returns, complaints and sterilization-failure patterns feeding the post-market surveillance file — the Article 83–86 obligation that gets harder as the device fleet grows.

**The governance line that makes this senior rather than naive:** *"The copilot drafts; it never releases. Every AI output lands behind the same two-person gate as everything else in this system — and the agent's scope, training data and logs sit inside the validated boundary, documented the same way we document any Category 5 component. AI accelerates the compliance team; it is never itself the approver."* That one paragraph — AI enthusiasm with validation discipline — is worth more in this interview than the feature itself.

---

## How the three moves sequence (the roadmap slide)

| Wave | What | Why then | Commercial shape |
|---|---|---|---|
| **Now → Nov 2026** | EUDAMED Autopilot + legacy bulk registration | Hard legal deadline 27 Nov 2026 | Fixed-fee module + one-time managed service |
| **At go-live** | Patient Implant Passport | Rides the consumption event the moment it exists | Per-device-family configuration + recurring passport service |
| **Post-stabilization** | Compliance Copilot | Needs 6–12 months of thread data to be worth querying | Subscription — the first genuinely recurring line |

**The strategic frame to say out loud:** *"Horizon 1 makes you compliant. Horizon 2 makes compliance pay: the same thread files your EUDAMED registrations, prints your implant cards, and answers your auditors — and each of those is a product, not a project. That's what 'buying the pattern once' means."*

## Deploying it in the pitch (don't oversell it)

- **One slide, 60 seconds, after The Ask** — as the "where this goes" close, not a second proposal. Visual: the three-wave roadmap with the EUDAMED countdown badge.
- **One line in the memo:** "The same thread is also the data source for EUDAMED registration (mandatory since May 2026; legacy deadline 27 November 2026), Article 18 implant cards, and — governed properly — Odoo 19's native AI agents. We address these as Horizon 2."
- **In Q&A, if asked "what's next":** lead with the passport (memorable), anchor with EUDAMED (dated), close with the copilot governance line (senior).
- **The 60-second script:** *"One last slide. Everything today was Horizon 1 — the compliant thread. But notice what you now own: the exact dataset EUDAMED demands — and your legacy-device registration deadline is the 27th of November, four months out. The same consumption event that triggers your invoice can print the Article 18 implant card and publish the patient's device page — the thread ends in the patient's pocket, not at the invoice. And once the thread has a year of data, Odoo 19's native AI agents can answer your auditors in plain language — drafting, never releasing; the two-person gate applies to machines too. Compliance stops costing you money and starts being the product. That's Horizon 2 — and it's why the discovery sprint is the cheapest decision on this roadmap."*

---
**Sources:** [EC — EUDAMED mandatory 28 May 2026](https://health.ec.europa.eu/latest-updates/eudamed-four-first-modules-will-be-mandatory-use-28-may-2026-2025-11-27_en) · [MedTech Europe — milestone](https://www.medtecheurope.org/2026/06/04/eudamed-reaches-a-major-milestone-mandatory-use-of-the-first-four-modules-begins/) · [Obelis — deadlines](https://www.obelis.net/news/eudamed-becomes-mandatory-on-28-may-2026-deadlines-for-actor-device-and-certificate-registrations/) · [MDCG 2019-8 v2 — implant card](https://www.eclevarmedtech.com/en/mdcg-2019-8-v2-implant-card-relating-to-the-application-of-article-18-regulation-eu-2017-745-of-the-european-parliament-and-of-the-council-of-5-april-2017-on-medical-devices-and-mdcg-2021-11/) · [Clin R — Article 18 requirements](https://clin-r.com/eu-mdr-requirements-for-implant-cards/) · [Odoo 19 AI agents docs](https://www.odoo.com/documentation/19.0/applications/productivity/ai/agents.html)
