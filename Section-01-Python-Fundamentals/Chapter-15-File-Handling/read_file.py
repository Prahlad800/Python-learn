"""Learning file for Reading Files."""

# Topic Name: Reading Files
# Level: Beginner
# Reading files loads text or structured data from disk into a program.
# Read the theory first, then run this file and modify examples.

# Theory
# Reading files loads text or structured data from disk into a program.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# path.read_text(encoding='utf-8')
# with open(path) as file:

# Practice Programs
# 1. Write notes to a text file.
# 2. Append a timestamped log line.
# 3. Read CSV rows and convert them into dictionaries.

# Mini Project
# Build a tiny program that uses reading files
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Why use with for files?
# A1. It closes the file automatically even if an error occurs.
# Q2. What is the difference between w and a modes?
# A2. w replaces file contents; a adds to the end.

# Examples and practice implementations start below.
import tempfile
from pathlib import Path


def example_read_text():
    with tempfile.TemporaryDirectory() as temp_dir:
        path = Path(temp_dir) / "notes.txt"
        path.write_text("Python\nFiles\n", encoding="utf-8")
        print("Content:", path.read_text(encoding="utf-8").splitlines())


def example_read_lines():
    with tempfile.TemporaryDirectory() as temp_dir:
        path = Path(temp_dir) / "todo.txt"
        path.write_text("read\ncode\ntest\n", encoding="utf-8")
        print("Lines:", [line.strip() for line in path.open(encoding="utf-8")])


def practice_count_lines(text):
    return len(text.splitlines())


def main():
    print("--- Reading Files ---")
    example_read_text()
    example_read_lines()
    print("Line count:", practice_count_lines("a\nb\nc\n"))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Reading Files ---
# Content: ['Python', 'Files']
# Lines: ['read', 'code', 'test']
# Line count: 3
# End Expected Output
