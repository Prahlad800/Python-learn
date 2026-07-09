"""
Topic: The yield Keyword Deep Dive
Chapter: 18
Level: Beginner

Description:
    The `yield` keyword is the heart of Python generators. When a function contains `yield`, 
    it automatically becomes a generator function. Unlike `return`, which terminates the 
    function and destroys its local state, `yield` temporarily pauses the function, saves 
    its local state, and hands control back to the caller.

Real-Life Analogy:
    Think of `yield` like a bookmark in a book. You read a chapter (execute code), place a 
    bookmark (`yield`), and put the book down. When you pick it back up, you don't start 
    from the beginning; you start exactly where the bookmark was left.

Key Concepts:
    - State preservation
    - yield vs return execution flow
    - Resuming execution with next()
"""
from typing import Iterator, Any

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def yield_demonstration() -> Iterator[str]:
    """Demonstrates how execution pauses at each yield."""
    print("Starting generator...")
    yield "First Pause"
    
    print("Resuming after first pause...")
    yield "Second Pause"
    
    print("Resuming after second pause...")
    yield "Third Pause"
    print("Generator exhausted.")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def alternating_boolean() -> Iterator[bool]:
    """An infinite generator that alternates yielding True and False."""
    state = True
    while True:
        yield state
        state = not state  # Flip the state

def fibonacci_generator(n_terms: int) -> Iterator[int]:
    """Generates the first N terms of the Fibonacci sequence using yield."""
    a, b = 0, 1
    for _ in range(n_terms):
        yield a
        a, b = b, a + b

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def yield_with_cleanup() -> Iterator[int]:
    """Demonstrates using try/finally block with yield."""
    try:
        print("Setup resources")
        yield 1
        yield 2
    finally:
        # This cleanup code runs when the generator is exhausted or closed
        print("Cleaning up resources (closing file, DB connection, etc.)")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Expecting a generator function to execute when called.
# Correction: Calling a generator function only returns a generator object.
# It doesn't run any code until next() is called or it's iterated over.

# Best Practice: Use generators for data streams that shouldn't be fully loaded into memory.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What happens to local variables when a function yields?
# A1: They are preserved in memory until the generator is resumed or garbage collected.
#
# Q2: Can a function have both yield and return?
# A2: Yes, in Python 3.3+, `return value` inside a generator raises StopIteration(value).
#
# Q3: How do you properly close a generator before it finishes?
# A3: By calling the `.close()` method on the generator object.
#
# Q4: Why use yield instead of a list append?
# A4: To save memory and process items on the fly (lazily).
#
# Q5: Does a generator function execute code immediately when called?
# A5: No, it just returns a generator object.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Create a generator that yields the powers of 2 (1, 2, 4, 8, 16...) endlessly.
# Exercise 2: Write a generator `extract_integers(mixed_list)` that yields only the integers.
# Exercise 3: Use a try/finally block in a generator to print "Done!" when it finishes.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge: Write a generator `running_average(numbers)` that takes a list of numbers
# and yields the running average up to that point.

def running_average(numbers: list[float]) -> Iterator[float]:
    """Yields the running average of a list of numbers."""
    total = 0.0
    for count, num in enumerate(numbers, 1):
        total += num
        yield total / count

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - `yield` pauses a function and saves its local state.
# - The function resumes right after the `yield` statement on the next iteration.
# - Generators provide lazy evaluation, drastically reducing memory footprint.
# - A function with `yield` returns a generator object, not the actual values.

if __name__ == "__main__":
    print("--- Yield Demonstration ---")
    gen = yield_demonstration()
    print("Returned object:", type(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    
    print("\n--- Alternating Boolean ---")
    alt = alternating_boolean()
    print([next(alt) for _ in range(5)])
    
    print("\n--- Fibonacci Generator ---")
    print(list(fibonacci_generator(7)))
    
    print("\n--- Yield with Cleanup ---")
    cleanup_gen = yield_with_cleanup()
    print(next(cleanup_gen))
    print(next(cleanup_gen))
    try:
        next(cleanup_gen) # Will trigger finally block and StopIteration
    except StopIteration:
        pass
        
    print("\n--- Mini Challenge ---")
    nums = [10, 20, 30, 40]
    print(list(running_average(nums)))
