"""Learning file for Generator Expressions."""

# Topic Name: Generator Expressions
# Level: Advanced
# Generator expressions are lazy versions of comprehensions.
# Read the theory first, then run this file and modify examples.

# Theory
# Generator expressions are lazy versions of comprehensions.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# (x * x for x in range(5))
# sum(x for x in values if x > 0)

# Practice Programs
# 1. Generate even numbers lazily.
# 2. Read a large file line by line using a generator.
# 3. Compare a list comprehension with a generator expression.

# Mini Project
# Build a tiny program that uses generator expressions
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Why use generators?
# A1. They produce values lazily and can save memory.
# Q2. What does yield do?
# A2. It returns a value and pauses the function state until the next iteration.

# Examples and practice implementations start below.
def example_generator_expression():
    squares = (number ** 2 for number in range(1, 6))
    print("Squares:", list(squares))


def example_memory_friendly_sum():
    total = sum(number for number in range(1, 101) if number % 2 == 0)
    print("Even total:", total)


def practice_clean_words(words):
    return (word.strip().lower() for word in words if word.strip())


def main():
    print("--- Generator Expressions ---")
    example_generator_expression()
    example_memory_friendly_sum()
    print("Words:", list(practice_clean_words([" Python ", "", "Generators"])))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Generator Expressions ---
# Squares: [1, 4, 9, 16, 25]
# Even total: 2550
# Words: ['python', 'generators']
# End Expected Output
