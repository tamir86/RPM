from pathlib import Path

MODELS_DIR = Path(r"C:\Users\ofric\Nike_SB_RPM_Clean\Nike_SB_RPM_Archive\02_Models")

if MODELS_DIR.exists():
    print("✅ Folder found!")
else:
    print("❌ Folder NOT found. Check the path again.")
