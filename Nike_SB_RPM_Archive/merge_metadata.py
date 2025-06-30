import csv
import sys
from pathlib import Path

base = Path(__file__).parent
master_f = base / "06_Metadata_And_Indexes" / "master_metadata.csv"
manual_f = base / "06_Metadata_And_Indexes" / "manual_metadata.csv"
output_f = base / "06_Metadata_And_Indexes" / "merged_metadata.csv"

# Ensure both input files exist
for p in (master_f, manual_f):
    if not p.is_file():
        sys.exit(f"Missing required file: {p}")

# Load master metadata
with master_f.open("r", newline="", encoding="utf-8") as mf:
    master = list(csv.DictReader(mf))

# Load manual enrichment into a lookup dict
lookup = {}
with manual_f.open("r", newline="", encoding="utf-8") as mdf:
    for row in csv.DictReader(mdf):
        lookup[row["filename"]] = row

# Determine columns for output
base_cols = list(master[0].keys())
manual_cols = [c for c in lookup[next(iter(lookup))].keys() if c != "filename"]
out_fields = base_cols + manual_cols

# Write merged CSV
with output_f.open("w", newline="", encoding="utf-8") as mf:
    writer = csv.DictWriter(mf, fieldnames=out_fields)
    writer.writeheader()
    for m in master:
        merged = dict(m)
        if m["filename"] in lookup:
            for col in manual_cols:
                merged[col] = lookup[m["filename"]].get(col, "")
        else:
            for col in manual_cols:
                merged[col] = ""
        writer.writerow(merged)

print(f"Merged metadata written to {output_f}")