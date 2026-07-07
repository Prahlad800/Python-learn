"""Learning file for yield Keyword."""

# Topic Name: yield Keyword
# Level: Advanced
# yield pauses a function and returns a value while preserving local state for the next call.
# Read the theory first, then run this file and modify examples.

# Theory
# yield pauses a function and returns a value while preserving local state for the next call.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# yield item
# yield from iterable

# Practice Programs
# 1. Generate even numbers lazily.
# 2. Read a large file line by line using a generator.
# 3. Compare a list comprehension with a generator expression.

# Mini Project
# Build a tiny program that uses yield keyword
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Why use generators?
# A1. They produce values lazily and can save memory.
# Q2. What does yield do?
# A2. It returns a value and pauses the function state until the next iteration.

# Examples and practice implementations start below.
def read_chunks(text, size):
    for index in range(0, len(text), size):
        yield text[index:index + size]


def example_yield_state():
    chunks = list(read_chunks("Python", 2))
    print("Chunks:", chunks)


def practice_countdown(start):
    while start >= 0:
        yield start
        start -= 1


def main():
    print("--- yield Keyword ---")
    example_yield_state()
    print("Countdown:", list(practice_countdown(3)))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- yield Keyword ---
# Chunks: ['Py', 'th', 'on']
# Countdown: [3, 2, 1, 0]
# End Expected Output
