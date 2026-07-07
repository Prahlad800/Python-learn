"""Learning file for Iterators."""

# Topic Name: Iterators
# Level: Advanced
# Iterators power loops by implementing the next-value protocol.
# Read the theory first, then run this file and modify examples.

# Theory
# Iterators power loops by implementing the next-value protocol.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# iterator = iter(iterable)
# next(iterator)

# Practice Programs
# 1. Use iter() and next() manually.
# 2. Build a countdown iterator.
# 3. Explain StopIteration in your own words.

# Mini Project
# Build a tiny program that uses iterators
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What protocol powers for loops?
# A1. The iterator protocol: __iter__ returns an iterator and __next__ returns values.
# Q2. What ends iteration?
# A2. Raising StopIteration.

# Examples and practice implementations start below.
def example_manual_iteration():
    colors = iter(["red", "green", "blue"])
    print(next(colors))
    print(next(colors))
    print(next(colors))


def example_for_loop_protocol():
    text = "py"
    iterator = iter(text)
    print("Letters:", next(iterator), next(iterator))


def practice_take(iterable, count):
    iterator = iter(iterable)
    result = []
    for _ in range(count):
        result.append(next(iterator))
    return result


def main():
    print("--- Iterators ---")
    example_manual_iteration()
    example_for_loop_protocol()
    print("Take:", practice_take([10, 20, 30], 2))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Iterators ---
# red
# green
# blue
# Letters: p y
# Take: [10, 20]
# End Expected Output
