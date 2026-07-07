"""Learning file for Dictionaries."""

# Topic Name: Dictionaries
# Level: Beginner
# Dictionaries map unique keys to values and are the core structure for records, indexes, and JSON-like data.
# Read the theory first, then run this file and modify examples.

# Theory
# Dictionaries map unique keys to values and are the core structure for records, indexes, and JSON-like data.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# person = {'name': 'Asha'}
# person['age'] = 21
# person.get('city', 'Unknown')

# Practice Programs
# 1. Create a student report dictionary.
# 2. Update inventory quantities safely.
# 3. Read nested dictionary values with get().

# Mini Project
# Build a tiny program that uses dictionaries
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What must dictionary keys be?
# A1. Keys must be hashable, such as strings, numbers, or tuples of immutable values.
# Q2. What does get() prevent?
# A2. It avoids KeyError by returning a default when the key is missing.

# Examples and practice implementations start below.
def example_create_access():
    student = {"name": "Asha", "marks": 92}
    print("Name:", student["name"])
    student["grade"] = "A"
    print("Student:", student)


def example_get_default():
    settings = {"theme": "light"}
    print("Language:", settings.get("language", "English"))


def practice_word_frequency(sentence):
    frequency = {}
    for word in sentence.lower().split():
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


def main():
    print("--- Dictionaries ---")
    example_create_access()
    example_get_default()
    print("Frequency:", practice_word_frequency("python is fun python"))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Dictionaries ---
# Name: Asha
# Student: {'name': 'Asha', 'marks': 92, 'grade': 'A'}
# Language: English
# Frequency: {'python': 2, 'is': 1, 'fun': 1}
# End Expected Output
