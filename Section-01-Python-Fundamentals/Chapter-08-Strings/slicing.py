"""Learning file for String Slicing."""

# Topic Name: String Slicing
# Level: Beginner
# Slicing extracts substrings using start, stop, and step indexes.
# Read the theory first, then run this file and modify examples.

# Theory
# Slicing extracts substrings using start, stop, and step indexes.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# text[start:stop]
# text[start:stop:step]
# text[::-1]

# Practice Programs
# 1. Clean and normalize user names.
# 2. Check whether a sentence is a palindrome after removing spaces.
# 3. Count words and characters in text.

# Mini Project
# Build a tiny program that uses string slicing
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Are strings mutable?
# A1. No. String methods return new strings instead of changing the original.
# Q2. What does slicing exclude?
# A2. The stop index is excluded from the result.

# Examples and practice implementations start below.
def example_basic_slices():
    text = "Python"
    print("first three:", text[:3])
    print("last two:", text[-2:])
    print("reverse:", text[::-1])


def example_step_slice():
    text = "abcdef"
    print("Every second:", text[::2])


def practice_mask_email(email):
    name, domain = email.split("@")
    return name[:2] + "***@" + domain


def main():
    print("--- String Slicing ---")
    example_basic_slices()
    example_step_slice()
    print("Masked:", practice_mask_email("asha@example.com"))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- String Slicing ---
# first three: Pyt
# last two: on
# reverse: nohtyP
# Every second: ace
# Masked: as***@example.com
# End Expected Output
