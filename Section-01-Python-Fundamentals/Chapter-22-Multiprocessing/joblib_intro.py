"""
Topic: Introduction to Joblib
Chapter: 22
Level: Intermediate

Description:
    `joblib` is a third-party Python library widely used in data science (like Scikit-Learn) for lightweight pipelining and easy parallel computing. It provides a much simpler syntax than the built-in `multiprocessing` module for running loops in parallel.

Real-Life Analogy:
    If `multiprocessing` is a manual transmission car where you control the gears, `joblib` is an automatic car where you just press the gas pedal to achieve parallelism.

Key Concepts:
    - joblib.Parallel
    - joblib.delayed
    - Backend ('loky', 'multiprocessing', 'threading')
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

import time
import math
import os
# Note: Requires joblib to be installed (pip install joblib)
# We will use try-except to ensure the script doesn't crash if not installed
try:
    from joblib import Parallel, delayed
    JOBLIB_AVAILABLE = True
except ImportError:
    JOBLIB_AVAILABLE = False

def compute_square_root(x: int) -> float:
    """A simple mathematical operation."""
    time.sleep(0.1) # Simulate complex math
    return math.sqrt(x)

def basic_joblib_example() -> None:
    """Demonstrates parallel execution using joblib."""
    if not JOBLIB_AVAILABLE:
        print("Joblib is not installed. Skipping example.")
        return
        
    inputs = [1, 4, 9, 16, 25, 36, 49, 64]
    
    print("Running with Joblib...")
    start = time.time()
    
    # Parallel defines the pool configuration
    # delayed(func)(args) wraps the function and arguments to be executed later
    results = Parallel(n_jobs=4)(delayed(compute_square_root)(i) for i in inputs)
    
    end = time.time()
    print(f"Results: {results}")
    print(f"Time taken: {end - start:.2f}s")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def process_file(filename: str) -> str:
    """Simulates processing a file."""
    print(f"[{os.getpid()}] Processing {filename}...")
    time.sleep(0.5)
    return f"{filename}_processed"

def backend_example() -> None:
    """Demonstrates different joblib backends."""
    if not JOBLIB_AVAILABLE:
        return
        
    files = ["data1.csv", "data2.csv", "data3.csv", "data4.csv"]
    
    # Backend 'threading' is good for I/O
    print("\nUsing Threading backend:")
    Parallel(n_jobs=2, backend="threading")(delayed(process_file)(f) for f in files)
    
    # Backend 'loky' (default) is robust for Multiprocessing
    print("\nUsing Loky backend:")
    Parallel(n_jobs=2, backend="loky")(delayed(process_file)(f) for f in files)

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Joblib also provides caching for slow functions, known as Memoization
try:
    from joblib import Memory
    memory = Memory(location="./cachedir", verbose=0)
except ImportError:
    memory = None

# Caching slow function
if memory:
    @memory.cache
    def expensive_computation(a: int, b: int) -> int:
        print(f"Computing {a} + {b} (This takes time...)")
        time.sleep(2)
        return a + b

def caching_example() -> None:
    if not memory:
        return
        
    print("\nCaching Example:")
    print("First call:")
    print(expensive_computation(10, 20)) # Takes 2 seconds
    
    print("Second call (same args, should be instant):")
    print(expensive_computation(10, 20)) # Instant!

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Using `n_jobs=-1` on a shared server.
# Correction: `n_jobs=-1` uses ALL available CPU cores. This can lock up the system for other users. Be explicit with your core count, or use `n_jobs=-2` to leave one core free.

# Best Practice: Use Joblib for embarrassingly parallel loops (loops where iterations are completely independent of each other).

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: What is `joblib.delayed`?
A: It is a decorator/wrapper that captures the arguments of a function call and delays its execution so it can be passed to `Parallel` to be dispatched to a worker.

Q2: What is the default backend for joblib?
A: 'loky'. It is a robust multiprocessing implementation that avoids memory leaks and handles complex Python objects better than the standard multiprocessing module.

Q3: How do you tell joblib to use threads instead of processes?
A: By setting `backend="threading"` in the `Parallel` constructor.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Install joblib (`pip install joblib`). Write a function that takes a string and reverses it. Use `Parallel` and `delayed` to reverse a list of 100 strings.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

"""
Challenge:
Write a web scraper function that takes a URL and returns its length (mock it with `time.sleep`).
Create a list of 20 URLs.
Use `joblib` with the `threading` backend to fetch all lengths in parallel.
"""

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Joblib simplifies parallel loops significantly.
- `Parallel(n_jobs)(delayed(func)(arg) for arg in iterator)` is the core syntax.
- Supports both multiprocessing ('loky') and threading.
- Excellent for data science workflows.
"""

if __name__ == "__main__":
    print("--- Joblib Examples ---")
    basic_joblib_example()
    backend_example()
    caching_example()
