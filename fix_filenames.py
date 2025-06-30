#!/usr/bin/env python3
import csv
import argparse
import logging
import sys
import re
from pathlib import Path

# ───────────────────────────────────────────────────────────────
# Setup logging to file
logging.basicConfig(
    filename="fixer_log.txt",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s"
)
# ───────────────────────────────────────────────────────────────

def normalize_name(filename: str) -> str:
    """
    1) Strip whitespace and BOM/directional marks
    2) Lowercase
    3) Collapse spaces/underscores/dashes runs to one underscore
    """
    # Remove any non-alphanumeric chars at the start (drop BOMs, RTL marks, etc)
    name = re.sub(r"^[^A-Za-z0-9]+", "", filename.strip())
    # Lowercase
    name = name.lower()
    # Collapse spaces, underscores, dashes into one underscore
    name = re.sub(r"[ _-]+", "_", name)
    return name

def load_report(report_path: Path):
    with report_path.open() as f:
        reader = csv.DictReader(f)
        return list(reader)

def apply_renames(rows, folder: Path, do_apply: bool):
    for row in rows:
        src = folder / row["original"]
        suggested = normalize_name(row["original"])
        dst = folder / suggested
        action = "Applying" if do_apply else "Would apply"
        print(f"{action}: {src.name} → {dst.name}")
        logging.info(f"{action}: {src.name} → {dst.name}")
        if do_apply:
            if src.exists():
                src.rename(dst)
            else:
                print(f"⚠️ Missing file: {src.name}")
                logging.warning(f"Missing file: {src.name}")

def main():
    parser = argparse.ArgumentParser(
        description="Apply filename fixes from a validator report"
    )
    parser.add_argument(
        "-r", "--report",
        type=Path,
        required=True,
        help="Path to the CSV report file."
    )
    parser.add_argument(
        "-f", "--folder",
        type=Path,
        required=True,
        help="Folder containing the files to rename."
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually apply the renames (default is dry-run)."
    )
    args = parser.parse_args()

    if not args.report.is_file():
        print(f"Error: report not found: {args.report}", file=sys.stderr)
        sys.exit(1)
    if not args.folder.is_dir():
        print(f"Error: folder not found: {args.folder}", file=sys.stderr)
        sys.exit(1)

    rows = load_report(args.report)
    apply_renames(rows, args.folder, args.apply)
    print("Done.")

if __name__ == "__main__":
    main()
