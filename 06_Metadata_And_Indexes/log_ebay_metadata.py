import os
import re
import pandas as pd

# === CONFIG ===
PHOTO_DIR = r"C:\Users\ofric\Nike_SB_RPM_Clean\Nike_SB_RPM_Archive\02_Models\Photos"
OUTPUT_CSV = os.path.join(PHOTO_DIR, "ebay_visual_metadata.csv")

# === REGEX RULE ===
pattern = re.compile(
    r"^(BA\d{4}-\d{3})_ebay_([a-zA-Z0-9]+)_(\d{4}-\d{2}-\d{2})_([a-z]+)_(\d+)\.(jpg|jpeg|png)$"
)

# === PROCESS FILES ===
metadata = []
for filename in os.listdir(PHOTO_DIR):
    match = pattern.match(filename)
    if match:
        style_code, seller, date_captured, view_type, seq, ext = match.groups()
        metadata.append({
            "filename": filename,
            "style_code": style_code,
            "view_type": view_type,
            "source_type": "ebay",
            "seller": seller,
            "listing_id": "",
            "listing_url": "",
            "date_captured": date_captured,
            "notes": ""
        })

# === SAVE CSV ===
df = pd.DataFrame(metadata)
df.to_csv(OUTPUT_CSV, index=False)
print(f"✅ Metadata logged for {len(df)} files.\nSaved to: {OUTPUT_CSV}")
