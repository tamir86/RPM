#!/usr/bin/env python3
import csv
import sys
from pathlib import Path

base = Path(__file__).parent
input_dir = base / "02_Models"
output_csv = base / "06_Metadata_And_Indexes" / "master_metadata.csv"

if not input_dir.is_dir() or not output_csv.parent.is_dir():
    print("Input or output folder missing.")
    sys.exit(1)

fields = ["filename", "style_code", "colorway", "view_type", "sequence"]
with output_csv.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    for img in sorted(input_dir.rglob("*.jp*g")):
        name = img.name
        parts = name.lower().rsplit(".",1)[0].split("_")
        if len(parts)!=3: continue
        style, view, seq = parts
        color = img.parent.name.lower()
        writer.writerow({
            "filename": name,
            "style_code": style,
            "colorway": color,
            "view_type": view,
            "sequence": seq
        })
print(f"Master metadata with colorway at {output_csv}")