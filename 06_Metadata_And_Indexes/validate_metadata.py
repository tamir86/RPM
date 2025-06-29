import os
import re
import pandas as pd

# CONFIG
ARCHIVE_ROOT = r"C:\Users\ofric\Nike_SB_RPM_Clean\Nike_SB_RPM_Archive"
MODELS_DIR = os.path.join(ARCHIVE_ROOT, "02_Models")
METADATA_PATH = os.path.join(ARCHIVE_ROOT, "06_Metadata_And_Indexes", "master_metadata.csv")
LOG_PATH = os.path.join(ARCHIVE_ROOT, "06_Metadata_And_Indexes", "validator_log.txt")

# SETTINGS
REQUIRED_VIEWS = {"front", "back"}
VALID_VIEWS = {"front", "back", "side", "bottom", "top", "detail", "tag", "interior", "strap"}
VALID_EXTS = {".jpg", ".jpeg", ".png"}
FILENAME_REGEX = re.compile(r'^BA\d{4}-\d{3}_(\w+)_\d+(_ebay)?\.(jpg|jpeg|png)$', re.IGNORECASE)

# LOAD MASTER METADATA
master_df = pd.read_csv(METADATA_PATH)
logged_filenames = set(master_df["filename"].values)

# STORAGE FOR REPORT
bad_format = []
not_logged = []
unknown_views = []
missing_views = {}

# WALK THROUGH MODEL FOLDERS
for model_folder in os.listdir(MODELS_DIR):
    folder_path = os.path.join(MODELS_DIR, model_folder, "Photos")
    if not os.path.isdir(folder_path):
        continue

    model_views_found = set()

    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)
        _, ext = os.path.splitext(file)
        ext = ext.lower()

        if ext not in VALID_EXTS:
            continue

        if not FILENAME_REGEX.match(file):
            bad_format.append(file)
            continue

        if file not in logged_filenames:
            not_logged.append(file)

        view_match = re.search(r'_(\w+)_\d+', file)
        if view_match:
            view = view_match.group(1).lower()
            model_views_found.add(view)
            if view not in VALID_VIEWS:
                unknown_views.append(file)

    missing = REQUIRED_VIEWS - model_views_found
    if missing:
        missing_views[model_folder] = list(missing)

# CREATE REPORT
report_lines = []

if bad_format:
    report_lines.append("❌ Bad Filename Format:")
    report_lines.extend(bad_format)
    report_lines.append("")

if not_logged:
    report_lines.append("⚠️ Not Logged in master_metadata.csv:")
    report_lines.extend(not_logged)
    report_lines.append("")

if unknown_views:
    report_lines.append("❗ Unknown View Types:")
    report_lines.extend(unknown_views)
    report_lines.append("")

if missing_views:
    report_lines.append("📦 Models Missing Required Views:")
    for model, views in missing_views.items():
        report_lines.append(f"{model}: Missing {', '.join(views)}")
    report_lines.append("")

if not report_lines:
    report_lines.append("✅ All files passed validation!")

# OUTPUT REPORT
with open(LOG_PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines))

print("\n".join(report_lines))
