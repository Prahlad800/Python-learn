"""Learning file for Dictionary Practice Programs."""

# Topic Name: Dictionary Practice Programs
# Level: Beginner
# Dictionary Practice Programs reinforces the chapter with runnable examples.
# Read the theory first, then run this file and modify examples.

# Theory
# Dictionary Practice Programs reinforces the chapter with runnable examples.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# # See the runnable examples below for the topic syntax.

# Practice Programs
# 1. Create a student report dictionary.
# 2. Update inventory quantities safely.
# 3. Read nested dictionary values with get().

# Mini Project
# Build a tiny program that uses dictionary practice programs
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What must dictionary keys be?
# A1. Keys must be hashable, such as strings, numbers, or tuples of immutable values.
# Q2. What does get() prevent?
# A2. It avoids KeyError by returning a default when the key is missing.

# Examples and practice implementations start below.
def invert_dictionary(data):
    return {value: key for key, value in data.items()}


def inventory_value(inventory):
    total = 0
    for item in inventory.values():
        total += item["price"] * item["quantity"]
    return total


def practice_group_by_first_letter(words):
    groups = {}
    for word in words:
        groups.setdefault(word[0], []).append(word)
    return groups


def main():
    print("--- Dictionary Practice Programs ---")
    print("Invert:", invert_dictionary({"a": 1, "b": 2}))
    print("Inventory:", inventory_value({"pen": {"price": 10, "quantity": 3}}))
    print("Groups:", practice_group_by_first_letter(["apple", "ant", "bat"]))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Dictionary Practice Programs ---
# Invert: {1: 'a', 2: 'b'}
# Inventory: 30
# Groups: {'a': ['apple', 'ant'], 'b': ['bat']}
# End Expected Output
