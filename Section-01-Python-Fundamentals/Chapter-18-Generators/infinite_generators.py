"""
Topic: Infinite Generators
Chapter: 18
Level: Intermediate

Description:
    Infinite generators are generators that never terminate on their own. They contain 
    a `while True` loop and continuously yield values. They are incredibly useful for 
    simulating infinite sequences, data streams, or assigning unique IDs indefinitely 
    without causing memory overflow (since values are generated one at a time).

Real-Life Analogy:
    Think of a flowing river. The water keeps coming endlessly. You don't store the 
    whole river in a tank; you just scoop out a bucket of water (yield) whenever you need it.

Key Concepts:
    - while True loops in generators
    - Using itertools.islice with infinite generators
    - Stream simulation
"""
from typing import Iterator
import time
import random

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def infinite_counter(start: int = 0) -> Iterator[int]:
    """Generates an infinite sequence of numbers."""
    while True:
        yield start
        start += 1

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def generate_ids() -> Iterator[str]:
    """Generates infinite unique IDs."""
    counter = 1
    while True:
        yield f"USER-{counter:04d}"
        counter += 1

def sensor_data_stream() -> Iterator[float]:
    """Simulates an infinite stream of temperature sensor data."""
    base_temp = 20.0
    while True:
        fluctuation = random.uniform(-0.5, 0.5)
        yield round(base_temp + fluctuation, 2)

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# To use infinite generators safely, you must pair them with an external
# limit, such as a loop counter, `break` statement, or `itertools.islice`.

import itertools

def process_infinite_stream():
    """Demonstrates slicing an infinite generator."""
    stream = sensor_data_stream()
    
    # islice takes (iterable, stop) and safely cuts off the infinite stream
    first_10_readings = list(itertools.islice(stream, 10))
    return first_10_readings

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Calling `list()` on an infinite generator.
# Correction: This will result in an infinite loop and eventually crash your program 
# due to MemoryError. Always iterate with limits.

# Best Practice: Use `itertools.islice` or a manual counter to break out of loops 
# that consume infinite generators.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What makes a generator infinite?
# A1: The absence of a termination condition, typically implemented with `while True`.
#
# Q2: How do infinite generators avoid MemoryError?
# A2: They only hold one value in memory at a time, regardless of how many values they've yielded.
#
# Q3: How do you safely extract the first N items from an infinite generator?
# A3: Using `itertools.islice(generator, N)`.
#
# Q4: Can you use a `for` loop on an infinite generator?
# A4: Yes, but you MUST have a `break` statement inside the loop, otherwise it will run forever.
#
# Q5: Provide a use case for an infinite generator.
# A5: Polling a network socket, reading real-time sensor data, or generating unique transaction IDs.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write an infinite generator that cycles through the colors "Red", "Green", "Blue".
# Exercise 2: Create an infinite generator for the Fibonacci sequence.
# Exercise 3: Write an infinite generator that yields timestamps (using time.time()) endlessly.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge: Write an infinite generator `collatz_conjecture(n)` that yields the Collatz 
# sequence for a given number `n`. Note: While the Collatz conjecture says it always 
# reaches 1, pretend we want it to keep yielding 1, 4, 2, 1, 4, 2 infinitely after that.

def collatz_conjecture(n: int) -> Iterator[int]:
    """Yields the infinite Collatz sequence."""
    yield n
    while True:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        yield n

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Infinite generators use `while True` to yield forever.
# - They are safe from memory overflow because evaluation is lazy.
# - Never cast an infinite generator to a list or tuple.
# - `itertools.islice` is the best tool for slicing infinite streams safely.

if __name__ == "__main__":
    print("--- Infinite Counter (Manual Break) ---")
    counter = infinite_counter(100)
    for _ in range(5):
        print(next(counter))
        
    print("\n--- Unique IDs ---")
    ids = generate_ids()
    print([next(ids) for _ in range(3)])
    
    print("\n--- Sensor Stream with islice ---")
    print(process_infinite_stream())
    
    print("\n--- Mini Challenge (Collatz) ---")
    collatz = collatz_conjecture(7)
    # Get the first 20 numbers to see the sequence and the infinite 4,2,1 loop
    print(list(itertools.islice(collatz, 20)))
