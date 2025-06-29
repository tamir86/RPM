import os
import csv
import re
from datetime import datetime

# === CONFIGURATION ===
ROOT_DIR = r"C:\Users\ofric\Nike_SB_RPM_Clean\Nike_SB_RPM_Archive\02_Models"
OUTPUT_CSV = r"C:\Users\ofric\Nike_SB_RPM_Clean\Nike_SB_RPM_Archive\06_Metadata_And_Indexes\master_metadata.csv"

# === STRICT NAMING FORMAT ===
filename_pattern = re.compile(
    r"(?P<style_code>BA\d{4}-\d{3})_(?P<view_type>[a-zA-Z]+)_(?P<sequence>\d+)\.\w+$"
)

image_extensions = {".jpg", ".jpeg", ".png", ".webp"}

entries = []

# === MAIN WALK ===
for model_folder in os.listdir(ROOT_DIR):
    model_path = os.path.join(ROOT_DIR, model_folder)

    photos_path = ""
    for item in os.listdir(model_path):
        if os.path.isdir(os.path.join(model_path, item)) and item.lower() == "photos":
            photos_path = os.path.join(model_path, item)
            break

    if not photos_path or not os.path.isdir(photos_path):
        continue

    for filename in os.listdir(photos_path):
        ext = os.path.splitext(filename)[1].lower()
        if ext in image_extensions:
            match = filename_pattern.match(filename)
            if match:
                style_code = match.group("style_code")
                view_type = match.group("view_type")
                sequence = match.group("sequence")
                title = f"{style_code} - {view_type.capitalize()} View"

                entry = {
                    "filename": filename,
                    "style_code": style_code,
                    "view_type": view_type,
                    "sequence": sequence,
                    "date_saved": datetime.now().strftime("%Y-%m-%d"),
                    "title":  f"{style_code} - {view_type.capitalize()} View",
                    "identifier": style_code,
                    "creator": "Nike SB",
                    "date": "",
                    "publisher": "",
                    "type": "Image",
                    "format": "JPEG or PNG",
                    "source": "",
                    "language": "en",
                    "description": "",
                    "coverage": "",
                    "subject": "",
                    "relation": "",
                    "rights": "For archival use only",
                    "contributor": "Tamir Segal"
                }
                entries.append(entry)

# === WRITE OUTPUT ===
if entries:
    with open(OUTPUT_CSV, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=entries[0].keys())
        writer.writeheader()
        writer.writerows(entries)
    print(f"✅ Metadata written to: {OUTPUT_CSV}")
else:
    print("⚠️ No valid images found.")
