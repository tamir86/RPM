# analyze_master_metadata.py
import csv

# Relative path from this script to your CSV
path = "06_Metadata_And_Indexes/master_metadata.csv"

with open(path, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        print(row)
        if i >= 20:  # stop after header + 20 data rows
            break
