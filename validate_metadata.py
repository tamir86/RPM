import re
import csv
from pathlib import Path

# ————————————————————————————————————————
# 1) Regex & validator function
#    Matches: BA####-###_[view]_[seq].ext
#    e.g. BA2037-089_front_1.jpg
# ————————————————————————————————————————
FILENAME_PATTERN = re.compile(
    r'^(BA\d{4}-\d{3})_([a-z]+)_(\d+)\.(\w+)$',
    re.IGNORECASE
)

def validate_filename(fname: str):
    """
    Returns (is_valid, groups) where:
      - is_valid: True if fname matches the pattern
      - groups: (style_code, view_tag, sequence, extension) if valid, else ()
    """
    m = FILENAME_PATTERN.match(fname)
    if not m:
        return False, ()
    return True, (m.group(1), m.group(2), m.group(3), m.group(4))


# ————————————————————————————————————————
# 2) Gather all failures into a list
# ————————————————————————————————————————
def gather_failures(folder_path):
    """
    Scans folder_path for files whose names do not match the pattern.
    Returns a list of dicts: { original, reason, suggestion }
    """
    failures = []
    for f in Path(folder_path).iterdir():
        if not f.is_file():
            continue
        valid, _ = validate_filename(f.name)
        if not valid:
            # simple fallback suggestion: lowercase, replace spaces with underscores
            suggestion = f.name.lower().replace(" ", "_")
            failures.append({
                "original":   f.name,
                "reason":     "does not match BA####-###_[view]_[seq].ext",
                "suggestion": suggestion
            })
    return failures


# ————————————————————————————————————————
# 3) Main: run validator and write CSV report
# ————————————————————————————————————————
if __name__ == "__main__":
    target_folder = Path("06_Metadata_And_Indexes")  # default scan folder
    report_path   = Path("filename_validation_report.csv")

    failures = gather_failures(target_folder)

    # Write out the CSV
    with report_path.open("w", newline="") as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=["original", "reason", "suggestion"]
        )
        writer.writeheader()
        writer.writerows(failures)

    print(f"{len(failures)} failures ▶ {report_path.name}")
