# analyze_master_metadata.py
import csv

path = "06_Metadata_And_Indexes/master_metadata.csv"
with open(path, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        print(row)
        if i >= 20:  # header + 20 data rows
            break
