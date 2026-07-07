"""Learning file for Custom Modules."""

# Topic Name: Custom Modules
# Level: Intermediate
# Custom modules let you reuse your own functions across files.
# Read the theory first, then run this file and modify examples.

# Theory
# Custom modules let you reuse your own functions across files.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# # helpers.py
# from helpers import add
# add(2, 3)

# Practice Programs
# 1. Move helper functions into a custom module.
# 2. Use built-in modules to calculate dates and statistics.
# 3. Explain why packages need clear module boundaries.

# Mini Project
# Build a tiny program that uses custom modules
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Why split code into modules?
# A1. Modules make code reusable, organized, and easier to test.
# Q2. What is a package?
# A2. A package is a folder of related modules that can be imported together.

# Examples and practice implementations start below.
import importlib.util
import tempfile
from pathlib import Path


def load_module_from_path(module_name, path):
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def example_custom_module():
    with tempfile.TemporaryDirectory() as temp_dir:
        helper_path = Path(temp_dir) / "helpers.py"
        helper_path.write_text(
            "def add(left, right):\n    return left + right\n",
            encoding="utf-8",
        )
        helpers = load_module_from_path("helpers", helper_path)
        print("2 + 3:", helpers.add(2, 3))


def practice_slug(text):
    return text.strip().lower().replace(" ", "-")


def main():
    print("--- Custom Modules ---")
    example_custom_module()
    print("Slug:", practice_slug("Custom Module"))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Custom Modules ---
# 2 + 3: 5
# Slug: custom-module
# End Expected Output
