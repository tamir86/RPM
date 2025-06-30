import csv

with open("06_Metadata_And_Indexes/master_metadata.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    headers = next(reader)
    print("CSV headers:", headers)
