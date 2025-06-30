import re
from pathlib import Path
import csv
import argparse
import sys

# Regex to match normalized schema: ba####-###_<view>_<seq>.jpg
pattern = re.compile(
    r'^(?P<style>ba\d{4}-\d{3})_(?P<view>[a-z]+)_(?P<seq>\d+)\.(?P<ext>jpe?g)$'
)


def normalize_name(filename: str) -> str:
    name = filename.strip()
    name = re.sub(r"[ _-]+", "_", name)
    return name.lower()


def validate_filename(filename: str) -> bool:
    name = normalize_name(filename)
    return bool(pattern.match(name))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    report = []
    for img in args.folder.rglob("*.jp*g"):
        orig = img.name
        valid = validate_filename(orig)
        if not valid:
            report.append({"original": orig, "reason": "invalid format", "suggestion": normalize_name(orig)})

    with args.output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["original","reason","suggestion"])
        writer.writeheader()
        writer.writerows(report)

    print(f"Validation complete: {len(report)} issues found.")

if __name__ == "__main__":
    main()