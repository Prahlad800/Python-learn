"""Learning file for Writing Files."""

# Topic Name: Writing Files
# Level: Beginner
# Writing files saves new content and replaces existing file content when using write mode.
# Read the theory first, then run this file and modify examples.

# Theory
# Writing files saves new content and replaces existing file content when using write mode.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# path.write_text(data, encoding='utf-8')
# with open(path, 'w') as file:

# Practice Programs
# 1. Write notes to a text file.
# 2. Append a timestamped log line.
# 3. Read CSV rows and convert them into dictionaries.

# Mini Project
# Build a tiny program that uses writing files
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Why use with for files?
# A1. It closes the file automatically even if an error occurs.
# Q2. What is the difference between w and a modes?
# A2. w replaces file contents; a adds to the end.

# Examples and practice implementations start below.
import tempfile
from pathlib import Path


def example_write_text():
    with tempfile.TemporaryDirectory() as temp_dir:
        path = Path(temp_dir) / "output.txt"
        path.write_text("Learning Python", encoding="utf-8")
        print("Written:", path.read_text(encoding="utf-8"))


def example_write_lines():
    with tempfile.TemporaryDirectory() as temp_dir:
        path = Path(temp_dir) / "tasks.txt"
        tasks = ["plan", "code", "review"]
        path.write_text("\n".join(tasks), encoding="utf-8")
        print("Tasks:", path.read_text(encoding="utf-8").splitlines())


def practice_report(name, score):
    return f"{name}: {score}/100"


def main():
    print("--- Writing Files ---")
    example_write_text()
    example_write_lines()
    print("Report:", practice_report("Asha", 95))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Writing Files ---
# Written: Learning Python
# Tasks: ['plan', 'code', 'review']
# Report: Asha: 95/100
# End Expected Output
