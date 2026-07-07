"""Learning file for CSV and JSON Files."""

# Topic Name: CSV and JSON Files
# Level: Intermediate
# CSV and JSON are common formats for exchanging tabular and structured data.
# Read the theory first, then run this file and modify examples.

# Theory
# CSV and JSON are common formats for exchanging tabular and structured data.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# csv.DictReader(file)
# json.dumps(data)
# json.loads(text)

# Practice Programs
# 1. Write notes to a text file.
# 2. Append a timestamped log line.
# 3. Read CSV rows and convert them into dictionaries.

# Mini Project
# Build a tiny program that uses csv and json files
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Why use with for files?
# A1. It closes the file automatically even if an error occurs.
# Q2. What is the difference between w and a modes?
# A2. w replaces file contents; a adds to the end.

# Examples and practice implementations start below.
import csv
import json
import tempfile
from pathlib import Path


def example_csv():
    with tempfile.TemporaryDirectory() as temp_dir:
        path = Path(temp_dir) / "students.csv"
        with path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "marks"])
            writer.writeheader()
            writer.writerow({"name": "Asha", "marks": 92})
        with path.open(encoding="utf-8") as file:
            rows = list(csv.DictReader(file))
        print("CSV:", rows)


def example_json():
    data = {"course": "Python", "active": True}
    text = json.dumps(data, sort_keys=True)
    print("JSON:", text)
    print("Loaded:", json.loads(text)["course"])


def practice_to_json(records):
    return json.dumps(records, sort_keys=True)


def main():
    print("--- CSV and JSON Files ---")
    example_csv()
    example_json()
    print("Practice:", practice_to_json([{"id": 1}]))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- CSV and JSON Files ---
# CSV: [{'name': 'Asha', 'marks': '92'}]
# JSON: {"active": true, "course": "Python"}
# Loaded: Python
# Practice: [{"id": 1}]
# End Expected Output
