"""
Topic: Introduction to Generators
Chapter: 18
Level: Beginner

Description:
    Generators are a simple way of creating iterators in Python. They allow you to iterate 
    through a sequence of values without having to store all of them in memory at once. 
    Instead of returning all values, generators yield one value at a time and suspend their state.

Real-Life Analogy:
    Imagine a vending machine. It doesn't drop all of its snacks onto the floor at once 
    when you buy something. Instead, it yields one snack at a time when you ask for it, 
    pausing its operation until the next request.

Key Concepts:
    - Iterables vs Iterators
    - The difference between functions and generators
    - Using `yield` instead of `return`
"""
from typing import Generator, Iterator

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# A regular function uses 'return' and terminates completely.
def simple_function() -> list[int]:
    """Returns all values at once."""
    return [1, 2, 3]

# A generator uses 'yield' and pauses execution.
def simple_generator() -> Iterator[int]:
    """Yields values one at a time."""
    yield 1
    yield 2
    yield 3

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def generate_even_numbers(limit: int) -> Iterator[int]:
    """Generates even numbers up to a specified limit."""
    num = 0
    while num <= limit:
        yield num
        num += 2

def countdown(start: int) -> Iterator[int]:
    """Counts down from a start number to zero."""
    while start >= 0:
        yield start
        start -= 1

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Generators can also manage state across yields
def stateful_generator() -> Iterator[str]:
    """Demonstrates state retention between yields."""
    state = "Initial"
    yield f"State: {state}"
    
    state = "In Progress"
    yield f"State: {state}"
    
    state = "Final"
    yield f"State: {state}"

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Trying to reuse a generator after it's exhausted.
# Correction: Generators can only be iterated over once. Create a new one to iterate again.

# Best Practice: Use generators for reading large files line by line instead of readlines()
# which loads the whole file into memory.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is the main difference between a generator and a regular list?
# A1: A generator evaluates elements lazily (one at a time), saving memory. A list evaluates
#     all elements eagerly and stores them in memory.
#
# Q2: How do you extract the next value from a generator manually?
# A2: Using the built-in `next()` function.
#
# Q3: What exception is raised when a generator is empty?
# A3: StopIteration.
#
# Q4: Can you use a generator multiple times?
# A4: No, they are exhausted after one full iteration.
#
# Q5: What is the return type of a function that contains a 'yield' statement?
# A5: It returns a generator object.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a generator `squares(n)` that yields the square of numbers from 1 to n.
# Exercise 2: Write a generator `fibonacci(n)` that yields the first n numbers of the Fibonacci sequence.
# Exercise 3: Create a generator that yields only vowels from a given string.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge: Write a generator `batch_processor(data, batch_size)` that takes a list of data
# and yields smaller batches of size `batch_size`.

def batch_processor(data: list, batch_size: int) -> Iterator[list]:
    """Yields batches of data."""
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Generators use 'yield' instead of 'return'.
# - They are lazy iterators, generating items only when requested.
# - Excellent for memory efficiency with large datasets.
# - Exhausted after one full iteration.
# - Automatically handle StopIteration in 'for' loops.

if __name__ == "__main__":
    print("--- Basic Syntax ---")
    gen = simple_generator()
    print(next(gen))  # 1
    print(next(gen))  # 2
    print(next(gen))  # 3
    
    print("\n--- Practical Examples ---")
    print("Evens up to 10:", list(generate_even_numbers(10)))
    print("Countdown from 3:", list(countdown(3)))
    
    print("\n--- Advanced Usage ---")
    for s in stateful_generator():
        print(s)
        
    print("\n--- Mini Challenge ---")
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for batch in batch_processor(data, 3):
        print("Batch:", batch)
