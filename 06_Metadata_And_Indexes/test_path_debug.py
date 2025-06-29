from pathlib import Path
import os

print("🔍 Current working directory:", os.getcwd())

# Define and check the actual folder
target = Path(r"C:\Users\ofric\Nike_SB_RPM_Clean\Nike_SB_RPM_Archive\02_Models")
print("📂 Target path given:", target)

# Manual folder test
if target.exists():
    print("✅ YES: The folder exists!")
    print("📁 Contents:")
    for item in target.iterdir():
        print("   -", item)
else:
    print("❌ NO: The folder DOES NOT exist.")
    print("💡 Double-check the path in Windows File Explorer.")
