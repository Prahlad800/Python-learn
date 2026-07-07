"""Learning file for String Methods."""

# Topic Name: String Methods
# Level: Beginner
# String methods clean, search, transform, split, and join text without changing the original string.
# Read the theory first, then run this file and modify examples.

# Theory
# String methods clean, search, transform, split, and join text without changing the original string.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# text.strip()
# text.upper()
# text.replace(old, new)
# text.split(',')

# Practice Programs
# 1. Clean and normalize user names.
# 2. Check whether a sentence is a palindrome after removing spaces.
# 3. Count words and characters in text.

# Mini Project
# Build a tiny program that uses string methods
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Are strings mutable?
# A1. No. String methods return new strings instead of changing the original.
# Q2. What does slicing exclude?
# A2. The stop index is excluded from the result.

# Examples and practice implementations start below.
def example_cleaning():
    text = "  Python Programming  "
    print("strip:", text.strip())
    print("lower:", text.lower().strip())
    print("replace:", text.replace("Programming", "Course").strip())


def example_split_join():
    csv_line = "red,green,blue"
    colors = csv_line.split(",")
    print("Colors:", colors)
    print("Joined:", " | ".join(colors))


def practice_title_case(sentence):
    return sentence.strip().title()


def main():
    print("--- String Methods ---")
    example_cleaning()
    example_split_join()
    print(practice_title_case("  learn python daily  "))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- String Methods ---
# strip: Python Programming
# lower: python programming
# replace: Python Course
# Colors: ['red', 'green', 'blue']
# Joined: red | green | blue
# Learn Python Daily
# End Expected Output
