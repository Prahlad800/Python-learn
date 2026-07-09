"""
Topic: Lazy Evaluation
Chapter: 19
Level: Advanced

Description:
    Lazy evaluation is an evaluation strategy which delays the evaluation of an expression until its value is actually needed. In Python, iterators and generators are the primary ways to achieve lazy evaluation. This avoids allocating large amounts of memory to store intermediate results, making your code significantly faster and more memory-efficient when handling large datasets.

Real-Life Analogy:
    Imagine ordering food at a restaurant. Eager evaluation is like the kitchen cooking the entire menu in advance, hoping you'll eat it all. Lazy evaluation is a made-to-order system: the kitchen only cooks a specific dish exactly when you request it.

Key Concepts:
    - Eager vs Lazy evaluation
    - Memory efficiency
    - Infinite data streams
    - Pipelining operations
"""

import sys
import time
from typing import Iterator

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def eager_vs_lazy() -> None:
    print("--- Section 1: Eager vs Lazy ---")
    
    # Eager Evaluation (List Comprehension)
    # Calculates all 10,000 squares immediately and stores them in memory
    eager_list = [x * x for x in range(10000)]
    
    # Lazy Evaluation (Generator Expression)
    # Calculates nothing immediately; yields one square at a time when asked
    lazy_gen = (x * x for x in range(10000))
    
    print(f"Size of eager list in bytes: {sys.getsizeof(eager_list)}")
    print(f"Size of lazy generator in bytes: {sys.getsizeof(lazy_gen)}")


# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def process_large_data() -> None:
    print("\n--- Section 2: Practical Data Processing ---")
    
    # Simulating a massive log file processing
    def generate_logs(num_lines: int) -> Iterator[str]:
        """Lazy log generator"""
        for i in range(num_lines):
            # Simulate reading a line
            if i % 5 == 0:
                yield f"ERROR: Disk space low on node {i}"
            else:
                yield f"INFO: Node {i} functioning normally"

    # We want to extract only the ERROR node IDs
    logs = generate_logs(100) # Could be 10,000,000, memory usage stays the same!
    
    # Pipeline of lazy operations
    error_logs = (line for line in logs if line.startswith("ERROR"))
    node_ids = (line.split()[-1] for line in error_logs)
    
    print("Extracted first 3 error nodes:")
    for _ in range(3):
        print(next(node_ids))


# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def delayed_computation_demo() -> None:
    print("\n--- Section 3: Delayed Expensive Computation ---")
    
    def expensive_operation(n: int) -> int:
        """Simulate a time-consuming CPU task."""
        time.sleep(0.1) # 100ms
        return n * 10
        
    numbers = [1, 2, 3, 4, 5]
    
    print("Creating lazy pipeline...")
    start_time = time.time()
    # The expensive function is NOT called here!
    lazy_results = map(expensive_operation, numbers)
    print(f"Pipeline created in {time.time() - start_time:.4f}s")
    
    print("Consuming first two results...")
    start_time = time.time()
    print(next(lazy_results))
    print(next(lazy_results))
    print(f"Two items processed in {time.time() - start_time:.4f}s")


# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes() -> None:
    print("\n--- Section 4: Common Mistakes ---")
    
    # Mistake: Accidentally forcing eager evaluation when lazy is needed
    lazy_nums = (x for x in range(1000000))
    
    # Doing this loads all 1 million items into memory immediately!
    # count = len(list(lazy_nums)) 
    
    # Best Practice: If you just need to count, use a loop or sum()
    # E.g., count = sum(1 for _ in lazy_nums)
    print("Remember: calling list(), set(), or sorted() on an iterator forces eager evaluation.")


# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: What is lazy evaluation in Python?
A1: It's an evaluation strategy where expressions are not evaluated when they are bound to variables, but deferred until their results are actually needed (e.g., using generators or map/filter).

Q2: Why is lazy evaluation beneficial?
A2: It massively reduces memory usage (since the whole dataset isn't loaded into RAM) and can reduce computation time if you end up not needing the entire dataset (short-circuiting).

Q3: What built-in functions in Python 3 return lazy iterators?
A3: `map()`, `filter()`, `zip()`, `enumerate()`, and `reversed()`.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
"""
Exercise 1:
Write a lazy pipeline using generator expressions to:
1. Generate numbers from 1 to 100.
2. Filter only odd numbers.
3. Square them.
Print only the first 5 results.

Exercise 2:
Implement your own version of the `map()` function using a generator function.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================
"""
Challenge: Prime Number Pipeline.
Create an infinite lazy generator of integers starting from 2.
Filter it lazily to only yield prime numbers.
Consume the pipeline to find the first 5 primes greater than 100.
"""

def is_prime(n: int) -> bool:
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True

def mini_challenge() -> None:
    print("\n--- Section 7: Mini Challenge Demo ---")
    import itertools
    
    # 1. Infinite integer stream
    numbers = itertools.count(2)
    
    # 2. Lazy prime filter
    primes = filter(is_prime, numbers)
    
    # 3. Lazy filter for primes > 100
    large_primes = (p for p in primes if p > 100)
    
    print("First 5 primes > 100:")
    for _ in range(5):
        print(next(large_primes), end=" ")
    print()


# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- Lazy evaluation delays computation until the exact moment a value is required.
- It prevents memory exhaustion when working with large or infinite datasets.
- Generator expressions, `map()`, and `filter()` are primary lazy tools in Python.
- Avoid converting lazy iterators to lists unless you absolutely need the whole collection in memory.
"""

if __name__ == "__main__":
    eager_vs_lazy()
    process_large_data()
    delayed_computation_demo()
    common_mistakes()
    mini_challenge()
