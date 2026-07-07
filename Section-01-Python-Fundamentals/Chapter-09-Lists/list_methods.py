"""Learning file for List Methods."""

# Topic Name: List Methods
# Level: Beginner
# List methods mutate, search, count, sort, and copy list data.
# Read the theory first, then run this file and modify examples.

# Theory
# List methods mutate, search, count, sort, and copy list data.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# items.append(x)
# items.extend(values)
# items.sort()
# items.pop()

# Practice Programs
# 1. Create a marks list and calculate average marks.
# 2. Remove duplicates while preserving order.
# 3. Build a 3x3 matrix and print row totals.

# Mini Project
# Build a tiny program that uses list methods
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Are lists mutable?
# A1. Yes. You can add, remove, and modify list items in place.
# Q2. What is a list comprehension?
# A2. A compact expression for building a new list from an iterable.

# Examples and practice implementations start below.
def example_common_methods():
    tasks = ["read", "code"]
    tasks.append("test")
    tasks.insert(1, "plan")
    print("Tasks:", tasks)
    print("Removed:", tasks.pop())


def example_sort_count():
    scores = [90, 75, 90, 88]
    scores.sort()
    print("Sorted:", scores)
    print("90 count:", scores.count(90))


def practice_unique_order(values):
    unique = []
    for value in values:
        if value not in unique:
            unique.append(value)
    return unique


def main():
    print("--- List Methods ---")
    example_common_methods()
    example_sort_count()
    print("Unique:", practice_unique_order([1, 2, 1, 3, 2]))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- List Methods ---
# Tasks: ['read', 'plan', 'code', 'test']
# Removed: test
# Sorted: [75, 88, 90, 90]
# 90 count: 2
# Unique: [1, 2, 3]
# End Expected Output
