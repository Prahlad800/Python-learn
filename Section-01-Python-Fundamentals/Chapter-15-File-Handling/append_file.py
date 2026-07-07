"""Learning file for Appending Files."""

# Topic Name: Appending Files
# Level: Beginner
# Appending files adds new content without deleting what is already there.
# Read the theory first, then run this file and modify examples.

# Theory
# Appending files adds new content without deleting what is already there.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# with open(path, 'a') as file:
#     file.write('new line\n')

# Practice Programs
# 1. Write notes to a text file.
# 2. Append a timestamped log line.
# 3. Read CSV rows and convert them into dictionaries.

# Mini Project
# Build a tiny program that uses appending files
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Why use with for files?
# A1. It closes the file automatically even if an error occurs.
# Q2. What is the difference between w and a modes?
# A2. w replaces file contents; a adds to the end.

# Examples and practice implementations start below.
import tempfile
from pathlib import Path


def example_append_text():
    with tempfile.TemporaryDirectory() as temp_dir:
        path = Path(temp_dir) / "log.txt"
        path.write_text("start\n", encoding="utf-8")
        with path.open("a", encoding="utf-8") as file:
            file.write("continue\n")
        print("Log:", path.read_text(encoding="utf-8").splitlines())


def example_append_many():
    lines = []
    lines.append("first")
    lines.append("second")
    print("Memory log:", lines)


def practice_log_line(level, message):
    return f"[{level.upper()}] {message}"


def main():
    print("--- Appending Files ---")
    example_append_text()
    example_append_many()
    print(practice_log_line("info", "File updated"))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Appending Files ---
# Log: ['start', 'continue']
# Memory log: ['first', 'second']
# [INFO] File updated
# End Expected Output
