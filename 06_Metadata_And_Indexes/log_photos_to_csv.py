import os
import pandas as pd
from datetime import datetime

# Define your archive root
archive_root = r"C:\Users\ofric\Nike_SB_RPM_Clean\Nike_SB_RPM_Archive"
photo_base = os.path.join(archive_root, "02_Models")
metadata_file = os.path.join(photo_base, "master_metadata.csv")

# Load or create metadata file
if os.path.exists(metadata_file):
    df_metadata = pd.read_csv(metadata_file)
else:
    df_metadata = pd.DataFrame(columns=[
        "filename", "style_code", "view_type", "sequence", "date_saved",
        "source_url", "context_notes", "confidence_level", "seller_name"
    ])

# Walk through all subfolders
new_entries = []
for root, dirs, files in os.walk(photo_base):
    if not root.endswith("Photos"):
        continue

    for filename in files:
        if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue
        if filename in df_metadata['filename'].values:
            continue  # already logged

        parts = filename.split('_')
        if len(parts) < 3:
            continue  # invalid format

        style_code = parts[0]
        view_type = parts[1]
        try:
            sequence = int(parts[2])
        except ValueError:
            continue

        source = parts[3].split('.')[0] if len(parts) > 3 else ""
        seller_name = ""
        source_url = ""
        context_notes = ""

        if source == "ebay":
            print(f"\n🔍 Found eBay image: {filename}")
            seller_name = input("Enter seller name: ").strip()
            source_url = input("Enter source URL: ").strip()
            context_notes = input("Any context notes? (optional): ").strip()

        new_entries.append({
            "filename": filename,
            "style_code": style_code,
            "view_type": view_type,
            "sequence": sequence,
            "date_saved": datetime.today().strftime('%Y-%m-%d'),
            "source_url": source_url,
            "context_notes": context_notes,
            "confidence_level": "",
            "seller_name": seller_name
        })

# Save updated metadata
if new_entries:
    df_new = pd.DataFrame(new_entries)
    df_metadata = pd.concat([df_metadata, df_new], ignore_index=True)
    df_metadata.to_csv(metadata_file, index=False)
    print(f"\n✅ {len(new_entries)} new entries added to master_metadata.csv")
else:
    print("\n✅ No new photos found. All up to date.")
