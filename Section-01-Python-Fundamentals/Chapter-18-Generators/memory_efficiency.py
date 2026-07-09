"""
Topic: Memory Efficiency with Generators
Chapter: 18
Level: Intermediate

Description:
    The most significant advantage of generators is their memory efficiency. When working 
    with massive datasets (like reading multi-gigabyte log files or processing millions 
    of records), storing everything in memory using lists will crash the program. Generators 
    solve this by keeping only a single item in memory at a time.

Real-Life Analogy:
    Lists: Downloading a full 4K movie before you can watch a single second of it.
    Generators: Streaming the movie on Netflix. You watch it frame by frame, caching only 
    what you immediately need, without requiring hundreds of GBs of local storage.

Key Concepts:
    - Lazy Evaluation
    - Profiling memory usage (sys.getsizeof)
    - Handling large files
"""
import sys
from typing import Iterator

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Eager evaluation (Loads all in memory)
def create_list(n: int) -> list[int]:
    result = []
    for i in range(n):
        result.append(i)
    return result

# Lazy evaluation (Loads one at a time)
def create_generator(n: int) -> Iterator[int]:
    for i in range(n):
        yield i

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Imagine reading a 10GB file. 
# file.readlines() creates a massive list in memory.
# file is an iterator by default, allowing lazy reading.

def read_large_file_lazily(file_path: str) -> Iterator[str]:
    """Yields lines from a file one by one."""
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Process the line lazily
                yield line.strip()
    except FileNotFoundError:
        yield "File not found for simulation."

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def memory_heavy_transformation(data_stream: Iterator[int]) -> Iterator[int]:
    """Simulates a complex pipeline that remains memory efficient."""
    # Step 1: Filter
    filtered = (x for x in data_stream if x % 2 == 0)
    # Step 2: Transform
    transformed = (x * 100 for x in filtered)
    # Step 3: Yield results
    yield from transformed

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Doing `sorted(generator)`. 
# Correction: Functions like `sorted()`, `list()`, or `set()` consume the entire 
# generator and pull it into memory. If the generator is infinite or massive, it will crash.

# Best Practice: Use generators for I/O operations, network streams, and large dataset parsing.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: Why are generators memory efficient?
# A1: They generate values on-the-fly (lazily) and do not store the entire sequence in memory.
#
# Q2: How does `sys.getsizeof()` prove generator efficiency?
# A2: A list of 1 million integers might take 8MB, while a generator of 1 million integers 
#     takes around 100 bytes (just the state machine overhead).
#
# Q3: Does using a generator make code faster?
# A3: Not necessarily in execution speed (building a list is sometimes faster in C), 
#     but it drastically improves memory speed and prevents OS swapping/crashes.
#
# Q4: Can you reverse a generator?
# A4: No. Generators are forward-only iterators. To reverse, you must convert to a list first.
#
# Q5: Why is `with open('file') as f: for line in f:` memory efficient?
# A5: Because file objects in Python are inherently iterators that yield one line at a time.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Compare the size of a list comprehension vs generator expression for 10^6 elements.
# Exercise 2: Write a memory-efficient generator to parse a large mock CSV string line by line.
# Exercise 3: Use a generator to yield prime numbers up to a limit without creating a list.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge: You have a simulated API that returns a massive list of records. 
# Write a function that takes this massive list but processes it into chunks lazily 
# using a generator to keep processing memory footprint low.

def chunk_processor(massive_list: list, chunk_size: int) -> Iterator[list]:
    """Yields chunks of a massive list lazily."""
    for i in range(0, len(massive_list), chunk_size):
        # We only return a slice of the list at a time
        yield massive_list[i:i + chunk_size]

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Generators use Lazy Evaluation.
# - A list of 1,000,000 items takes MBs of memory; a generator takes ~100 bytes.
# - Generators prevent OutOfMemory crashes when dealing with large files.
# - Avoid operations like `sorted()` or `len()` on large generators.

if __name__ == "__main__":
    print("--- Memory Profiling ---")
    N = 10_000_000
    my_list = [x for x in range(1000)] # Smaller for speed, but proves the point
    my_gen = (x for x in range(N))
    
    print(f"Size of list (1000 items): {sys.getsizeof(my_list)} bytes")
    print(f"Size of generator (10,000,000 items): {sys.getsizeof(my_gen)} bytes")
    
    print("\n--- Pipeline Efficiency ---")
    data = (x for x in range(1000000))
    pipeline = memory_heavy_transformation(data)
    # Process only the first 5 to show it's instant and lazy
    print("First 5 processed items:")
    for _ in range(5):
        print(next(pipeline))
        
    print("\n--- Chunk Processing ---")
    large_data = list(range(1, 21))
    for chunk in chunk_processor(large_data, 5):
        print(f"Processing chunk: {chunk}")
