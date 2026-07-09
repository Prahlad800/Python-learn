"""
Topic: Process Pools
Chapter: 22
Level: Intermediate

Description:
    Process Pools provide a convenient way to manage multiple worker processes. Instead of manually creating, starting, and joining individual processes, a Pool handles the lifecycle and distribution of tasks (a concept known as data parallelism).

Real-Life Analogy:
    A call center with 5 operators (the pool). When customers call (tasks), they are automatically routed to the next available operator. You don't hire a new operator for every single call.

Key Concepts:
    - multiprocessing.Pool
    - map() vs imap()
    - apply() vs apply_async()
    - Task Distribution
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

import multiprocessing
import time
import os

def double_number(n: int) -> int:
    """A simple function to double a number."""
    time.sleep(0.1) # Simulate some work
    return n * 2

def basic_pool_map() -> None:
    """Demonstrates mapping a function over an iterable using a Pool."""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    
    # Create a pool with a specific number of worker processes
    # If processes is not specified, it defaults to os.cpu_count()
    print(f"Creating a pool with 4 workers. CPU count: {os.cpu_count()}")
    
    with multiprocessing.Pool(processes=4) as pool:
        # pool.map blocks until the entire result is ready, returning a list
        results = pool.map(double_number, numbers)
        
    print(f"Results of pool.map: {results}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def process_image(image_id: int) -> str:
    """Simulates processing an image."""
    print(f"Process {os.getpid()} is processing image {image_id}")
    time.sleep(0.5)
    return f"Image_{image_id}_processed.jpg"

def pool_apply_async_example() -> None:
    """Demonstrates apply_async for non-blocking task submission."""
    images = [101, 102, 103, 104, 105]
    
    with multiprocessing.Pool(processes=3) as pool:
        # submit tasks asynchronously
        results_objects = [pool.apply_async(process_image, args=(img,)) for img in images]
        
        print("Tasks submitted. Doing other things in main process...")
        time.sleep(0.2)
        print("Now waiting for results...")
        
        # Extract actual results using the .get() method
        final_results = [res.get() for res in results_objects]
        
    print(f"Processed images: {final_results}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def cpu_heavy_task(x: int) -> int:
    """A slightly heavier CPU task to demonstrate imap."""
    total = 0
    for i in range(x * 100000):
        total += i
    return total

def pool_imap_example() -> None:
    """Demonstrates imap, which yields results lazily as they finish."""
    tasks = [5, 2, 8, 1, 3]
    
    with multiprocessing.Pool(processes=2) as pool:
        # imap returns an iterator. It maintains the order of the input iterable.
        print("Starting imap...")
        start = time.time()
        for result in pool.imap(cpu_heavy_task, tasks):
            print(f"Got result: {result} at {time.time() - start:.2f}s")
            
        # imap_unordered yields results as soon as they are ready, ignoring input order.
        print("\nStarting imap_unordered...")
        start = time.time()
        for result in pool.imap_unordered(cpu_heavy_task, tasks):
            print(f"Got unordered result: {result} at {time.time() - start:.2f}s")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Forgetting to close and join the pool if not using the `with` statement.
# Correction: Always use the context manager (`with Pool() as pool:`) to automatically handle cleanup.

# Mistake: Passing unpicklable objects (like nested functions or lambdas) to pool methods.
# Correction: Only pass top-level functions to Pool methods, as arguments and functions must be serialized (pickled) to be sent to worker processes.

# Best Practice: Use `pool.imap_unordered` if you don't care about the order of results and want to process them as soon as possible.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: What is a Process Pool?
A: A Pool manages a fixed number of worker processes to which tasks can be submitted. It handles the scheduling and distribution of tasks.

Q2: What is the difference between `pool.map` and `pool.apply_async`?
A: `map` takes an iterable, chunks it, distributes it to workers, and blocks until all results are ready in a list. `apply_async` takes a single task, submits it without blocking, and returns an AsyncResult object from which you can retrieve the result later via `.get()`.

Q3: Why would you use `imap_unordered` instead of `map`?
A: `imap_unordered` yields results as soon as any task finishes, which is memory efficient and faster for processing variable-length tasks if order doesn't matter. `map` waits for all tasks to finish and returns a complete list.

Q4: What happens if an exception is raised inside a worker function in a Pool?
A: If using `.get()` on an AsyncResult or iterating over `map`/`imap` results, the exception raised in the worker will be re-raised in the main process.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Create a function that calculates the factorial of a number. Use a Pool of 4 processes and `pool.map` to calculate factorials for numbers 1 to 10.
Exercise 2: Create a function that takes a string and returns it capitalized. Use `pool.apply_async` to capitalize a list of 5 words.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

"""
Challenge:
Write a function that checks if a number is prime.
Create a list of 10,000 random integers between 1 and 100,000.
Use `multiprocessing.Pool` and `map` to find how many of these numbers are prime.
Compare the time taken with a single-threaded approach.
"""

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- `Pool` is ideal for executing a function across multiple inputs (data parallelism).
- `map` is blocking and preserves order.
- `apply_async` is non-blocking and handles single function calls.
- `imap` and `imap_unordered` provide lazy iteration over results.
- Context managers (`with` block) ensure proper resource cleanup.
"""

if __name__ == "__main__":
    print("--- Basic Pool Map ---")
    basic_pool_map()
    
    print("\n--- Pool Apply Async ---")
    pool_apply_async_example()
    
    print("\n--- Pool Imap vs Imap Unordered ---")
    pool_imap_example()
