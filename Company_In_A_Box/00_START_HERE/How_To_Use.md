---
title: How to Use This Package
subtitle: The recommended reading order and the workflow for updating it.
pack: Pack 00 — Start Here
purpose: Tell the reader how to get value fast and how to keep the package current.
status: Build-now · Guidance
reading_time: 3 min
date: July 2026
---

<div class="bluf"><span class="lbl">Bottom line up front</span><br>
For the fast picture: read Pack 01, then Pack 23, then Pack 22. To act: send the ten CEO questions (Pack 22) and start the five actions in Pack 23's Executive Action Plan. To update: change the Assumptions Register (Pack 16) and the deal-structure branch (Pack 14) when the CEO answers, then rebuild.</div>

## Recommended reading order

| If you want… | Read |
|---|---|
| The whole picture in 15 minutes | Pack 01 (Exec Summary) → Pack 23 (Master Report) |
| To act this week | Pack 22 (CEO Questions) + Pack 23 (Executive Action Plan) |
| The market/competition case | Packs 03, 04 |
| The commercial playbook | Packs 06, 08, 09 |
| The money | Packs 16, 17, 18 |
| The deal/legal position | Packs 14, 15 |

## How to update the package
This package is built to update cleanly, not to be rebuilt:
1. Record the CEO's answers in Pack 22's Answer_Capture_Template.
2. Update the **Assumptions Register (Pack 16)** — the financial model re-derives from it.
3. Set the **deal-structure branch (Pack 14)** and remove resolved flags (Polsat, pricing).
4. Rebuild the affected PDFs with the toolchain in `_BUILD` (run `bash _BUILD/build.sh`), and run `_CANONICAL/audit.py` to re-verify consistency.

<div class="callout"><span class="lbl">The design principle</span><br>
Every fact traces to one source (`_CANONICAL/facts.md`) and every figure to one register (Pack 16). That means an update is a small, safe edit in one place that propagates — not a risky rewrite. The package is a living instrument.</div>

## Sources & confidence
| Item | Confidence |
|---|---|
| Workflow | this package's design | ✅ |
