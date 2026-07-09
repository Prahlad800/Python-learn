"""
Topic: Global Interpreter Lock (GIL)
Chapter: 20
Level: Advanced

Description:
    The Global Interpreter Lock (GIL) is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecodes at once. This lock is necessary mainly because CPython's memory management is not thread-safe.

Real-Life Analogy:
    Imagine a kitchen (the Python interpreter) with many chefs (threads) but only one set of utensils (the GIL). Even if there are many chefs ready to cook, only the one holding the utensils can actually do any work. The others must wait until the utensils are passed to them.

Key Concepts:
    - CPython implementation details
    - CPU-bound vs I/O-bound tasks
    - The impact of GIL on multithreading
    - Bypassing the GIL with multiprocessing
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

import threading
import time

# The GIL means that in CPython, only one thread can execute Python bytecode at a time.
# Let's demonstrate how this affects CPU-bound tasks.

def count_down(n):
    while n > 0:
        n -= 1

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def single_thread_test():
    start = time.time()
    count_down(50_000_000)
    count_down(50_000_000)
    end = time.time()
    print(f"Single Thread Time: {end - start:.4f} seconds")

def multi_thread_test():
    start = time.time()
    t1 = threading.Thread(target=count_down, args=(50_000_000,))
    t2 = threading.Thread(target=count_down, args=(50_000_000,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    end = time.time()
    print(f"Multi Thread Time: {end - start:.4f} seconds")

# Notice how multi_thread_test is often slower or only marginally faster than single_thread_test
# due to the overhead of acquiring and releasing the GIL.

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# For I/O bound tasks, the GIL is released during I/O operations (like sleep, network requests),
# allowing true concurrency.

def io_bound_task():
    time.sleep(1) # Simulates an I/O operation

def multi_thread_io_test():
    start = time.time()
    threads = []
    for _ in range(5):
        t = threading.Thread(target=io_bound_task)
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
    end = time.time()
    print(f"Multi Thread I/O Time for 5 sleeps: {end - start:.4f} seconds")
    # This takes roughly 1 second, not 5 seconds!

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistakes:
# - Using multithreading to speed up heavy mathematical computations (CPU-bound).
# - Assuming that standard data structures are completely thread-safe without locks just because of the GIL.

# Best Practices:
# - Use multithreading for I/O-bound tasks (network, file I/O).
# - Use the `multiprocessing` module for CPU-bound tasks, as it creates separate memory spaces and bypasses the GIL.
# - Be aware of Python C extensions (like NumPy) which often release the GIL internally for computations.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q: What is the GIL in Python?
# A: The Global Interpreter Lock is a mutex in CPython that ensures only one thread executes Python bytecode at a time.

# Q: Why does CPython have a GIL?
# A: It simplifies memory management (reference counting) and makes integrating with non-thread-safe C libraries easier.

# Q: Does multithreading in Python provide true parallelism?
# A: For Python bytecode execution, no. However, for I/O operations or C extensions that release the GIL, it provides concurrency that feels like parallelism.

# Q: How can you bypass the GIL for CPU-bound tasks?
# A: By using the `multiprocessing` module, which creates separate processes, each with its own Python interpreter and memory space, effectively giving each process its own GIL.

# Q: Is the GIL present in all Python implementations?
# A: No, it's specific to CPython. Jython and IronPython do not have a GIL.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a script that compares the performance of threading vs multiprocessing for calculating prime numbers.
# Exercise 2: Demonstrate how an I/O bound task like downloading web pages benefits from multithreading.
# Exercise 3: Use the `sys.getswitchinterval()` to see how often Python switches between threads.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge:
# Create a hybrid application. Use a process pool (multiprocessing) to perform heavy calculations,
# and a thread pool (multithreading) inside the main process to handle logging the results to a file asynchronously.

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - The GIL restricts CPython to executing one thread at a time.
# - It primarily impacts CPU-bound multithreaded applications.
# - I/O-bound multithreaded applications still see significant performance gains.
# - Multiprocessing is the standard workaround for CPU-bound performance issues in Python.

if __name__ == "__main__":
    print("Running Single Thread (CPU-bound)...")
    single_thread_test()
    print("Running Multi Thread (CPU-bound)...")
    multi_thread_test()
    print("Running Multi Thread (I/O-bound)...")
    multi_thread_io_test()
