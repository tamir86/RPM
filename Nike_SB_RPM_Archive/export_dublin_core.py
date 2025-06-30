import csv
import sys
from pathlib import Path

base = Path(__file__).parent
inp = base / "06_Metadata_And_Indexes" / "merged_metadata.csv"
out = base / "06_Metadata_And_Indexes" / "dublin_core_metadata.csv"

if not inp.is_file():
    sys.exit(f"Missing input file: {inp}")

# Map our columns to Dublin Core fields
dc_map = {
    'filename': 'dc:identifier',
    'description': 'dc:description',
    'subject': 'dc:subject',
    'coverage': 'dc:coverage',
    'relation': 'dc:relation',
    'source': 'dc:source'
}

# Read merged CSV and write DC CSV
with inp.open("r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    # Determine extra fields to preserve
    extras = [c for c in reader.fieldnames if c not in dc_map]
    # Order: DC fields first, then extras
    out_fields = [dc_map[c] for c in reader.fieldnames if c in dc_map] + extras

    with out.open("w", newline="", encoding="utf-8") as w:
        writer = csv.DictWriter(w, fieldnames=out_fields)
        writer.writeheader()
        for row in reader:
            out_row = {}
            # Populate DC mapped fields
            for orig, dc in dc_map.items():
                out_row[dc] = row.get(orig, "")
            # Populate extras
            for c in extras:
                out_row[c] = row.get(c, "")
            writer.writerow(out_row)

print(f"Dublin Core CSV written to {out}")