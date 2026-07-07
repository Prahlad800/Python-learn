"""Learning file for String Practice Programs."""

# Topic Name: String Practice Programs
# Level: Beginner
# String Practice Programs reinforces the chapter with runnable examples.
# Read the theory first, then run this file and modify examples.

# Theory
# String Practice Programs reinforces the chapter with runnable examples.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# # See the runnable examples below for the topic syntax.

# Practice Programs
# 1. Clean and normalize user names.
# 2. Check whether a sentence is a palindrome after removing spaces.
# 3. Count words and characters in text.

# Mini Project
# Build a tiny program that uses string practice programs
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Are strings mutable?
# A1. No. String methods return new strings instead of changing the original.
# Q2. What does slicing exclude?
# A2. The stop index is excluded from the result.

# Examples and practice implementations start below.
def is_palindrome(text):
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


def count_words(sentence):
    return len(sentence.split())


def practice_initials(full_name):
    return "".join(part[0].upper() for part in full_name.split())


def main():
    print("--- String Practice Programs ---")
    print("Madam palindrome:", is_palindrome("Madam"))
    print("Word count:", count_words("Python is easy to read"))
    print("Initials:", practice_initials("Asha Rao"))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- String Practice Programs ---
# Madam palindrome: True
# Word count: 5
# Initials: AR
# End Expected Output
