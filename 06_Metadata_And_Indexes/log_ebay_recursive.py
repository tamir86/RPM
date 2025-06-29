import os
import re
import pandas as pd
from pathlib import Path

# === DEBUG: SHOW CURRENT WORKING DIRECTORY ===
print("🔍 Current working directory:", os.getcwd())

# === CONFIG: UPDATE THIS PATH IF NEEDED ===
MODELS_DIR = Path(r"C:\Users\ofric\Nike_SB_RPM_Clean\Nike_SB_RPM_Archive\02_Models")
print("📂 Target Models Directory:", MODELS_DIR)

OUTPUT_CSV = MODELS_DIR / "ebay_visual_metadata.csv"

# === REGEX PATTERN ===
# Example: BA2037-089_ebay_dunkjunkie_2024-05-12_front_1.jpg
pattern = re.compile(
    r"^(BA\d{4}-\d{3})_ebay_([a-zA-Z0-9]+)_(\d{4}-\d{2}-\d{2})_([a-z]+)_(\d+)\.(jpg|jpeg|png)$"
)

# === VALIDATE MODELS_DIR EXISTS ===
if not MODELS_DIR.exists():
    print("❌ ERROR: The folder path does not exist. Please double-check the MODELS_DIR setting.")
    exit()

# === SCAN ALL 'Photos' FOLDERS INSIDE EACH MODEL FOLDER ===
metadata = []

for model_folder in MODELS_DIR.iterdir():
    photos_folder = model_folder / "Photos"
    if photos_folder.exists() and photos_folder.is_dir():
        for file in photos_folder.iterdir():
            if file.is_file():
                match = pattern.match(file.name)
                if match:
                    style_code, seller, date_captured, view_type, seq, ext = match.groups()
                    metadata.append({
                        "filename": file.name,
                        "style_code": style_code,
                        "view_type": view_type,
                        "source_type": "ebay",
                        "seller": seller,
                        "listing_id": "",
                        "listing_url": "",
                        "date_captured": date_captured,
                        "notes": "",
                        "relative_path": str(file.relative_to(MODELS_DIR))
                    })

# === SAVE TO CSV ===
df = pd.DataFrame(metadata)
df.to_csv(OUTPUT_CSV, index=False)

print(f"✅ Metadata logged for {len(df)} files.")
print(f"📄 Saved to: {OUTPUT_CSV}")
