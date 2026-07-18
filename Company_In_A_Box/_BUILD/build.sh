#!/usr/bin/env bash
# Batch build: render every Pack .md -> PDF, clean up HTML. Run from CIAB/ root.
# Usage: bash _BUILD/build.sh [PackFolder]   (omit arg = build all packs)
set -u
export NODE_PATH=/opt/node22/lib/node_modules
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BUILD="$ROOT/_BUILD"
TARGET="${1:-}"
built=0
for md in $(find "$ROOT" -path "$ROOT/_BUILD" -prune -o -name "*.md" -print | sort); do
  case "$md" in
    "$ROOT/_CANONICAL/"*|"$ROOT/_SIMULATION/"*) continue;;  # internal working files, not partner PDFs
  esac
  if [ -n "$TARGET" ] && [[ "$md" != *"/$TARGET/"* ]]; then continue; fi
  html="${md%.md}.html"; pdf="${md%.md}.pdf"
  python3 "$BUILD/render.py" "$md" >/dev/null || { echo "RENDER FAIL: $md"; continue; }
  node "$BUILD/html2pdf.js" "$html" "$pdf" >/dev/null 2>&1 || { echo "PDF FAIL: $md"; continue; }
  rm -f "$html"
  sz=$(stat -c%s "$pdf")
  printf "OK  %-70s %6s KB\n" "${pdf#$ROOT/}" "$((sz/1024))"
  built=$((built+1))
done
echo "--- built $built PDFs ---"
