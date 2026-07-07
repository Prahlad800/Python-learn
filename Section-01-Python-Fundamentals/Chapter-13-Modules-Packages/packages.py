"""Learning file for Packages."""

# Topic Name: Packages
# Level: Intermediate
# Packages organize modules inside folders and expose larger reusable libraries.
# Read the theory first, then run this file and modify examples.

# Theory
# Packages organize modules inside folders and expose larger reusable libraries.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# package/module.py
# from package import module
# __init__.py

# Practice Programs
# 1. Move helper functions into a custom module.
# 2. Use built-in modules to calculate dates and statistics.
# 3. Explain why packages need clear module boundaries.

# Mini Project
# Build a tiny program that uses packages
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Why split code into modules?
# A1. Modules make code reusable, organized, and easier to test.
# Q2. What is a package?
# A2. A package is a folder of related modules that can be imported together.

# Examples and practice implementations start below.
from pathlib import Path


def example_package_path():
    chapter_folder = Path(__file__).parent
    print("Chapter folder:", chapter_folder.name)
    print("Is package-like folder:", chapter_folder.is_dir())


def example_import_style():
    import statistics
    print("Mean:", statistics.mean([10, 20, 30]))


def practice_module_name(path_text):
    return Path(path_text).stem


def main():
    print("--- Packages ---")
    example_package_path()
    example_import_style()
    print("Module stem:", practice_module_name("helpers.py"))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Packages ---
# Chapter folder: Chapter-13-Modules-Packages
# Is package-like folder: True
# Mean: 20
# Module stem: helpers
# End Expected Output
