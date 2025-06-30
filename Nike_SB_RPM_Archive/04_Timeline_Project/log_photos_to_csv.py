
import os
import csv
from datetime import datetime

# Define the root path to scan (current folder)
root_dir = os.path.dirname(os.path.abspath(__file__))
models_dir = os.path.join(root_dir, "02_Models")
output_file = os.path.join(root_dir, "Photo_Metadata_Log.csv")

# Model name mapping (can be expanded)
model_names = {
    "BA2449-089": "Elephant Vinyl",
    "BA2037-089": "Elephant OG",
    "BA4592-311": "Green Camo OG"
}

# Extract viewpoint from filename
def extract_viewpoint(filename):
    lower = filename.lower()
    if "front" in lower:
        return "Front View"
    if "side" in lower:
        return "Side View"
    if "back" in lower:
        return "Back View"
    if "top" in lower:
        return "Top View"
    return "Unlabeled"

# Prepare log
existing = set()
if os.path.exists(output_file):
    with open(output_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            existing.add(row["Filename"])

# Scan folders
entries = []
for root, _, files in os.walk(models_dir):
    for file in files:
        if file.lower().endswith(".jpg"):
            if file in existing:
                continue
            style_code = os.path.basename(os.path.dirname(os.path.dirname(root)))
            model_name = model_names.get(style_code, "Unknown")
            viewpoint = extract_viewpoint(file)
            entries.append({
                "Model": model_name,
                "Style Code": style_code,
                "Filename": file,
                "Viewpoint": viewpoint,
                "Date Added": datetime.now().strftime("%Y-%m-%d")
            })

# Write to CSV
if entries:
    write_header = not os.path.exists(output_file)
    with open(output_file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["Model", "Style Code", "Filename", "Viewpoint", "Date Added"])
        if write_header:
            writer.writeheader()
        writer.writerows(entries)

print(f"✅ Logged {len(entries)} new photo(s).")
