"""Learning file for with Statement."""

# Topic Name: with Statement
# Level: Beginner
# with automatically manages resources such as files and locks, even if errors occur.
# Read the theory first, then run this file and modify examples.

# Theory
# with automatically manages resources such as files and locks, even if errors occur.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# with open(path) as file:
#     data = file.read()

# Practice Programs
# 1. Write notes to a text file.
# 2. Append a timestamped log line.
# 3. Read CSV rows and convert them into dictionaries.

# Mini Project
# Build a tiny program that uses with statement
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Why use with for files?
# A1. It closes the file automatically even if an error occurs.
# Q2. What is the difference between w and a modes?
# A2. w replaces file contents; a adds to the end.

# Examples and practice implementations start below.
import tempfile
from pathlib import Path


def example_with_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        path = Path(temp_dir) / "data.txt"
        with path.open("w", encoding="utf-8") as file:
            file.write("managed safely")
        with path.open(encoding="utf-8") as file:
            print("Read:", file.read())


class ManagedTimer:
    def __enter__(self):
        print("Timer started")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Timer stopped")
        return False


def practice_context_manager():
    with ManagedTimer():
        print("Doing work")


def main():
    print("--- with Statement ---")
    example_with_file()
    practice_context_manager()


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- with Statement ---
# Read: managed safely
# Timer started
# Doing work
# Timer stopped
# End Expected Output
