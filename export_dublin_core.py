import csv
import sys
from pathlib import Path

# --- Configuration Paths ---
base_dir = Path(__file__).parent

# Input: merged metadata (from merge_metadata.py)
inp = base_dir / "merged_metadata_final.csv"
# Output: Berlin Core–formatted CSV
out = base_dir / "merged_metadata_berlin_core.csv"

# Verify input exists
if not inp.is_file():
    sys.exit(f"Error: Missing input file: {inp}")

# --- Berlin Core Field Mapping ---
dc_map = {
    'style_code'   : 'dc:identifier',   # model code
    'release_date' : 'dc:date',         # MM/YYYY
    'source'       : 'dc:description',  # your sale-note
    'relation'     : 'dc:source',       # your “Precedes…” info
    'photo_paths'  : 'dc:hasFormat'     # semicolon-separated photo filenames
}

# Define the exact output column order
output_fields = [
    'dc:identifier',
    'dc:date',
    'dc:description',
    'dc:source',
    'dc:hasFormat'
]

# --- Read & Write CSV ---
with inp.open(newline='', encoding='utf-8') as fin, \
     out.open('w', newline='', encoding='utf-8') as fout:
    reader = csv.DictReader(fin)
    writer = csv.DictWriter(fout, fieldnames=output_fields)
    writer.writeheader()

    for row in reader:
        # Map each source column to its DC term
        out_row = { dc_map[src]: row.get(src, '') for src in dc_map }
        writer.writerow(out_row)

print(f"✅ Berlin Core export written to: {out}")
