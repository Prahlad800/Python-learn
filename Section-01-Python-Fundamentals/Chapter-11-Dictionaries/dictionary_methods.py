"""Learning file for Dictionary Methods."""

# Topic Name: Dictionary Methods
# Level: Beginner
# Dictionary methods make it safer to read, update, merge, iterate, and remove key-value pairs.
# Read the theory first, then run this file and modify examples.

# Theory
# Dictionary methods make it safer to read, update, merge, iterate, and remove key-value pairs.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# data.keys()
# data.items()
# data.update(other)
# data.pop(key)

# Practice Programs
# 1. Create a student report dictionary.
# 2. Update inventory quantities safely.
# 3. Read nested dictionary values with get().

# Mini Project
# Build a tiny program that uses dictionary methods
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What must dictionary keys be?
# A1. Keys must be hashable, such as strings, numbers, or tuples of immutable values.
# Q2. What does get() prevent?
# A2. It avoids KeyError by returning a default when the key is missing.

# Examples and practice implementations start below.
def example_methods():
    profile = {"name": "Asha", "role": "developer"}
    profile.update({"city": "Delhi"})
    print("Keys:", list(profile.keys()))
    print("Items:", list(profile.items()))
    print("Removed:", profile.pop("city"))


def example_setdefault():
    counters = {}
    counters.setdefault("visits", 0)
    counters["visits"] += 1
    print("Counters:", counters)


def practice_merge(left, right):
    merged = left.copy()
    merged.update(right)
    return merged


def main():
    print("--- Dictionary Methods ---")
    example_methods()
    example_setdefault()
    print("Merged:", practice_merge({"a": 1}, {"b": 2}))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Dictionary Methods ---
# Keys: ['name', 'role', 'city']
# Items: [('name', 'Asha'), ('role', 'developer'), ('city', 'Delhi')]
# Removed: Delhi
# Counters: {'visits': 1}
# Merged: {'a': 1, 'b': 2}
# End Expected Output
