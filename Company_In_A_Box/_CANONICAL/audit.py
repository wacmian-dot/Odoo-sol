#!/usr/bin/env python3
"""Self-healing verification for the Company-in-a-Box. Prints PASS/FAIL per check.
Run from CIAB/ root: python3 _CANONICAL/audit.py"""
import os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FAILS = []
def check(cond, label):
    print(("PASS " if cond else "FAIL ") + label)
    if not cond: FAILS.append(label)

md_files = [p for p in glob.glob(ROOT + "/**/*.md", recursive=True)
            if "/_CANONICAL/" not in p and "/_SIMULATION/" not in p and "/_BUILD/" not in p]

# A. Structural
for md in md_files:
    pdf = md[:-3] + ".pdf"
    words = len(open(md, encoding="utf-8").read().split())
    # 240w floor: concise operational docs (SOPs, checklists) are legitimate; below this is suspiciously thin
    check(words >= 240, f"[len>=240w] {os.path.relpath(md, ROOT)} ({words}w)")
    check(os.path.exists(pdf), f"[pdf exists] {os.path.relpath(pdf, ROOT)}")
    if os.path.exists(pdf):
        kb = os.path.getsize(pdf)//1024
        check(kb >= 40, f"[pdf>=40KB] {os.path.relpath(pdf, ROOT)} ({kb}KB)")

# B. Integrity (grep across all md)
# A Polsat mention is safe if the line frames it as something to verify/resolve — never as an asserted client fact.
FLAGWORDS = ("unverified","🚩","confirm","not verified","couldn't verify","could not verify","absent",
             "verify","claim","flag","resolve","gate","substantiate","unresolved","question","open item")
for md in md_files:
    text = open(md, encoding="utf-8").read()
    rel = os.path.relpath(md, ROOT)
    # Polsat safety: any line mentioning Polsat must contain a flag word
    for i, line in enumerate(text.splitlines(), 1):
        if "polsat" in line.lower():
            safe = any(fw.lower() in line.lower() for fw in FLAGWORDS)
            check(safe, f"[polsat-flagged] {rel}:{i}")
    # Reference bleed from the OTHER company's package
    for bad in ("student finance","university partnership","SI-UK","Uniroute","mature student"):
        check(bad.lower() not in text.lower(), f"[no-ref-bleed:{bad}] {rel}")
    # Heat-pump year correctness
    if "600,000" in text or "600000" in text:
        check("2030" not in text, f"[hp-year-2028-not-2030] {rel}")

print("\n" + ("ALL PASS" if not FAILS else f"{len(FAILS)} FAILURES"))
sys.exit(1 if FAILS else 0)
