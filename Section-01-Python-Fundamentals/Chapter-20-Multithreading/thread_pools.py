"""
Topic: Thread Pools
Chapter: 20
Level: Intermediate

Description:
    Creating and destroying threads is expensive in terms of system resources. Thread pools address this by creating a pool of reusable threads.
    When a task is submitted to the pool, an available thread executes it, and then returns to the pool to wait for the next task.

Real-Life Analogy:
    Think of a taxi stand at an airport. Instead of buying a new car and hiring a driver for every passenger, a fixed number of taxis wait. 
    When a passenger arrives, they take an available taxi. When the trip is done, the taxi returns to the stand for the next passenger.

Key Concepts:
    - Thread Reuse
    - Worker Threads
    - Task Queues
    - multiprocessing.pool.ThreadPool
"""

import time
from multiprocessing.pool import ThreadPool
import random

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def simple_task(task_id):
    sleep_time = random.uniform(0.1, 0.5)
    time.sleep(sleep_time)
    return f"Task {task_id} completed in {sleep_time:.2f}s"

def section_1():
    print("--- Section 1: Basic Syntax ---")
    # Create a pool of 3 worker threads
    pool = ThreadPool(processes=3)
    
    # Map a function to an iterable of inputs
    results = pool.map(simple_task, range(5))
    
    # Close the pool and wait for the work to finish
    pool.close()
    pool.join()
    
    for res in results:
        print(res)
    print("Section 1 finished.\n")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def fetch_data(url):
    print(f"Fetching from {url}...")
    time.sleep(random.uniform(0.2, 0.8))  # Simulating network delay
    return f"Data from {url}"

def section_2():
    print("--- Section 2: Practical Examples ---")
    urls = [
        "http://example.com/api/1",
        "http://example.com/api/2",
        "http://example.com/api/3",
        "http://example.com/api/4",
        "http://example.com/api/5"
    ]
    
    pool = ThreadPool(processes=2) # Only 2 threads for 5 URLs
    
    # apply_async allows submitting tasks one by one
    async_results = [pool.apply_async(fetch_data, (url,)) for url in urls]
    
    pool.close()
    pool.join()
    
    # Retrieve results
    for res in async_results:
        print(res.get())
    print("Section 2 finished.\n")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def error_task(n):
    if n == 2:
        raise ValueError("Simulated error for task 2")
    return n * 2

def section_3():
    print("--- Section 3: Advanced Usage ---")
    pool = ThreadPool(processes=3)
    
    try:
        # map will raise an exception if any task fails
        results = pool.map(error_task, [1, 2, 3])
    except ValueError as e:
        print(f"Caught exception from pool: {e}")
        
    pool.close()
    pool.join()
    print("Section 3 finished.\n")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Forgetting to call pool.close() and pool.join(), leading to hanging programs or resource leaks.
# Mistake: Using too many threads in the pool, which causes excessive context switching and degrades performance.
# Best Practice: Generally, thread pool size should be related to the number of concurrent I/O operations expected, not strictly CPU cores.
# Best Practice: Use a context manager (with statement) to automatically manage the pool's lifecycle where available (e.g. concurrent.futures).

def section_4():
    print("--- Section 4: Common Mistakes ---")
    print("Always remember to close() and join() your pools!\n")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# 1. Why use a Thread Pool instead of creating new threads for every task?
# A: Thread creation adds overhead. Pools reuse threads, reducing overhead and limiting the maximum number of concurrent threads to prevent resource exhaustion.
#
# 2. What happens if a task in a thread pool raises an exception?
# A: The exception is caught by the pool and usually re-raised when the result is requested (e.g., via .get() or in map).
#
# 3. What is the difference between map() and apply_async() in a ThreadPool?
# A: map() blocks until all results are ready and returns them in order. apply_async() returns an AsyncResult object immediately, which you can use to check status and get the result later.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Create a list of 10 numbers. Use a ThreadPool to compute the square of each number, with a small random delay in the calculation function.
# Exercise 2: Use apply_async to do the same, and add a callback function that prints the result as soon as it's ready.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Simulate batch image resizing. You have 10 "images" (represented by strings). 
# Process them using a ThreadPool of 4 threads. Each "resize" takes a random time between 0.1 and 1 second.
# Print when an image starts and finishes processing.

def mock_resize(image_name):
    print(f"Starting resize of {image_name}...")
    time.sleep(random.uniform(0.1, 1.0))
    return f"{image_name} resized."

def run_challenge():
    print("--- Section 7: Mini Challenge ---")
    images = [f"Image_{i}.jpg" for i in range(1, 11)]
    pool = ThreadPool(processes=4)
    results = pool.map(mock_resize, images)
    pool.close()
    pool.join()
    print("All images processed.")
    print(results)
    print("Challenge completed.\n")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Thread pools limit the number of active threads and reuse them.
# - multiprocessing.pool.ThreadPool is a useful tool for this.
# - Use map() for simple parallel mapping of functions to data.
# - Use apply_async() for more control over individual task submission.

if __name__ == "__main__":
    section_1()
    section_2()
    section_3()
    section_4()
    run_challenge()
