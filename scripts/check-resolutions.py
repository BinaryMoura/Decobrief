#!/usr/bin/env python3
"""
Merge-gate checker from resolution-capture-agent.md.
Reads docs/resolutions/*.md and exits 1 if any record is not confirmed.

Usage:
  python3 scripts/check-resolutions.py
  npm run check-resolutions
"""
import pathlib, re, sys

root = pathlib.Path(__file__).parent.parent
resolutions_dir = root / "docs" / "resolutions"

if not resolutions_dir.exists():
    print("No docs/resolutions/ directory found — nothing to check.")
    sys.exit(0)

bad = []
checked = 0

for f in sorted(resolutions_dir.glob("*.md")):
    if f.name == "README.md":
        continue
    checked += 1
    text = f.read_text(encoding="utf-8")
    m = re.search(r"^status:\s*([a-z-]+)", text, re.MULTILINE)
    st = m.group(1) if m else "missing-status"
    if st != "confirmed":
        bad.append((f.name, st))

if checked == 0:
    print("No resolution records found.")
    sys.exit(0)

for name, status in bad:
    print(f"UNCONFIRMED: {name} ({status})")

if bad:
    sys.exit(1)

print(f"All {checked} resolution record(s) confirmed.")
sys.exit(0)
