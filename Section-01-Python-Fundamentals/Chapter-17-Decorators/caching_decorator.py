"""
Topic: Caching and Memoization Decorators
Chapter: 17
Level: Advanced

Description:
    Caching (or memoization) decorators save the results of expensive function calls and return the cached result when the same inputs occur again. 
    Python provides a built-in `lru_cache` for this, but building one from scratch helps understand the concept.

Real-Life Analogy:
    Imagine solving a complex math problem on a chalkboard. Instead of erasing it, you write the final answer in a notebook next to the question. 
    If someone asks the same question later, you just read the answer from the notebook instead of recalculating it.

Key Concepts:
    - Memoization.
    - Storing state in dictionaries.
    - Python's built-in `functools.lru_cache`.
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def simple_cache(func):
    """A basic caching decorator."""
    cache = {}  # This dictionary persists across function calls
    
    import functools
    @functools.wraps(func)
    def wrapper(*args):
        # We only use *args here because **kwargs can't easily be hashed (lists/dicts aren't hashable)
        if args in cache:
            print(f"[CACHE HIT] Returning cached result for {args}")
            return cache[args]
        
        print(f"[CACHE MISS] Computing result for {args}")
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@simple_cache
def expensive_computation(n):
    """Simulates a heavy calculation."""
    import time
    time.sleep(1)
    return n * n

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# The most common use case for memoization is the Fibonacci sequence.
# Without caching, the recursive fibonacci function takes exponential time.

@simple_cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Python provides an optimized, built-in caching decorator.
from functools import lru_cache

# LRU stands for Least Recently Used. It limits the cache size.
@lru_cache(maxsize=3)
def fetch_data(key):
    print(f"Fetching data from server for {key}...")
    return f"Data for {key}"

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Trying to cache functions that take unhashable arguments (like lists or dicts).
# Dictionary keys must be hashable. If you pass a list, `args in cache` will throw a TypeError.

# Mistake 2: Caching functions with side effects (like database writes). 
# If a function is supposed to write to a DB, but it returns a cached result, the DB write never happens!

# Best Practice: Use `functools.lru_cache` or `functools.cache` instead of writing your own, as they are written in C and highly optimized.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is memoization?
# A1: Memoization is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again.

# Q2: How does a caching decorator maintain state between calls?
# A2: The cache (usually a dictionary) is defined in the outer decorator function. Because the inner wrapper function creates a closure, it retains access to that dictionary across all executions.

# Q3: What does LRU mean in `lru_cache`?
# A3: Least Recently Used. When the cache reaches its `maxsize`, the oldest, least accessed item is removed to make room for the new one.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise: Write a decorator `time_limited_cache` that expires cached items after a certain number of seconds.
import time
import functools

def time_limited_cache(expiration_seconds):
    def decorator(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
            current_time = time.time()
            if args in cache:
                result, timestamp = cache[args]
                if current_time - timestamp < expiration_seconds:
                    print(f"Valid cache for {args}")
                    return result
                else:
                    print(f"Cache expired for {args}")
            
            result = func(*args)
            cache[args] = (result, current_time)
            return result
        return wrapper
    return decorator

@time_limited_cache(expiration_seconds=2)
def get_stock_price(ticker):
    print(f"Calling API for {ticker}...")
    return 150.00

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge: Demonstrate the `maxsize` behavior of `lru_cache`.
# Call `fetch_data` 4 times with different keys, then call the first key again to show it was evicted.

def demonstrate_lru():
    fetch_data("A") # Miss
    fetch_data("B") # Miss
    fetch_data("C") # Miss
    # Cache is full: {A, B, C}
    fetch_data("D") # Miss (Evicts A)
    # Cache: {B, C, D}
    fetch_data("A") # Miss (Because A was evicted)

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Caching avoids redundant computations.
# - Decorators form closures, allowing state (like a cache dict) to persist.
# - Use `functools.lru_cache` for built-in, efficient memoization.
# - Ensure arguments are hashable (tuples, strings, ints).

if __name__ == "__main__":
    print("--- Basic Syntax ---")
    expensive_computation(5)
    expensive_computation(5) # Instant!
    
    print("\n--- Practical Examples ---")
    print("Fibonacci(10):", fibonacci(10))
    
    print("\n--- Advanced Usage ---")
    fetch_data("User1")
    fetch_data("User1") # Cached
    
    print("\n--- Practice Exercises ---")
    get_stock_price("AAPL")
    get_stock_price("AAPL") # Valid cache
    time.sleep(2.5)
    get_stock_price("AAPL") # Expired cache
    
    print("\n--- Mini Challenge ---")
    demonstrate_lru()
