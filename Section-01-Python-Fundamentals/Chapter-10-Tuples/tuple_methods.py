"""Learning file for Tuple Methods."""

# Topic Name: Tuple Methods
# Level: Beginner
# Tuples have fewer methods because they are immutable, but count() and index() are often useful.
# Read the theory first, then run this file and modify examples.

# Theory
# Tuples have fewer methods because they are immutable, but count() and index() are often useful.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# values.count(item)
# values.index(item)

# Practice Programs
# 1. Return multiple values from a function using a tuple.
# 2. Unpack coordinates into x and y variables.
# 3. Count repeated values in a tuple.

# Mini Project
# Build a tiny program that uses tuple methods
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Why use tuples?
# A1. Use tuples for fixed-size records, immutable data, and multiple return values.
# Q2. Can a tuple contain mutable objects?
# A2. Yes. The tuple binding is immutable, but a contained mutable object can change.

# Examples and practice implementations start below.
def example_count_index():
    values = ("red", "blue", "red", "green")
    print("red count:", values.count("red"))
    print("blue index:", values.index("blue"))


def example_membership():
    extensions = (".py", ".txt", ".csv")
    print(".py supported:", ".py" in extensions)


def practice_has_duplicate(values):
    return len(values) != len(set(values))


def main():
    print("--- Tuple Methods ---")
    example_count_index()
    example_membership()
    print("Has duplicate:", practice_has_duplicate((1, 2, 1)))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Tuple Methods ---
# red count: 2
# blue index: 1
# .py supported: True
# Has duplicate: True
# End Expected Output
