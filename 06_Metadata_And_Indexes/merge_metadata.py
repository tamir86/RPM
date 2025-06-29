import csv

# === File Paths ===
master_csv_path = "master_metadata.csv"
manual_csv_path = "manual_metadata.csv"
output_csv_path = "merged_metadata.csv"

# === Read Manual Metadata into Dictionary ===
manual_data = {}
with open(manual_csv_path, mode='r', encoding='utf-8') as manual_file:
    reader = csv.DictReader(manual_file)
    for row in reader:
        manual_data[row['filename']] = row

# === Merge with Master Metadata ===
merged_entries = []

with open(master_csv_path, mode='r', encoding='utf-8') as master_file:
    reader = csv.DictReader(master_file)
    fieldnames = reader.fieldnames + ['description', 'subject', 'coverage', 'relation', 'source']
    
    for row in reader:
        filename = row['filename']
        manual = manual_data.get(filename, {})
        
        # Fill in manual fields if present
        for field in ['description', 'subject', 'coverage', 'relation', 'source']:
            row[field] = manual.get(field, "")
        
        merged_entries.append(row)

# === Write Merged Output ===
with open(output_csv_path, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(merged_entries)

print(f"✅ Merged metadata written to: {output_csv_path}")
