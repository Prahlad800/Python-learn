"""
Topic: Multiprocessing vs. Threading
Chapter: 22
Level: Advanced

Description:
    Python offers both threading and multiprocessing. Choosing the right one depends on whether your task is CPU-Bound (heavy calculations) or I/O-Bound (waiting for network, files, databases). This file compares their performance.

Real-Life Analogy:
    CPU-Bound (Multiprocessing): Solving complex math problems. You need more brains (processors).
    I/O-Bound (Threading): Waiting for water to boil. You don't need a second chef; one chef can put the water on the stove and chop vegetables while waiting.

Key Concepts:
    - CPU-Bound Tasks
    - I/O-Bound Tasks
    - Global Interpreter Lock (GIL)
    - Performance Benchmarking
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

import time
import threading
import multiprocessing
import requests # Requires 'requests' library, mocking for example

def cpu_bound_task(n: int) -> int:
    """A heavy computation task (e.g., counting, factoring)."""
    count = 0
    for i in range(n):
        count += i
    return count

def io_bound_task(url: str) -> None:
    """A task that waits for external resources (e.g., network)."""
    # Simulating a network request delay to avoid requiring external libraries
    # In reality, this would be requests.get(url)
    time.sleep(1)

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES (BENCHMARKING CPU)
# ============================================================

def run_threads_cpu(n: int, iterations: int):
    threads = []
    for _ in range(iterations):
        t = threading.Thread(target=cpu_bound_task, args=(n,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

def run_processes_cpu(n: int, iterations: int):
    processes = []
    for _ in range(iterations):
        p = multiprocessing.Process(target=cpu_bound_task, args=(n,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()

def benchmark_cpu():
    """Benchmarking CPU bound tasks."""
    n = 10_000_000
    iterations = 4
    
    print("Benchmarking CPU-Bound Task (Heavy Math)")
    
    start = time.time()
    run_threads_cpu(n, iterations)
    print(f"Threading time: {time.time() - start:.2f}s (Notice it's slow due to GIL)")
    
    start = time.time()
    run_processes_cpu(n, iterations)
    print(f"Multiprocessing time: {time.time() - start:.2f}s (Faster, bypassing GIL)")

# ============================================================
# SECTION 3: ADVANCED USAGE (BENCHMARKING I/O)
# ============================================================

def run_threads_io(url: str, iterations: int):
    threads = []
    for _ in range(iterations):
        t = threading.Thread(target=io_bound_task, args=(url,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

def run_processes_io(url: str, iterations: int):
    processes = []
    for _ in range(iterations):
        p = multiprocessing.Process(target=io_bound_task, args=(url,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()

def benchmark_io():
    """Benchmarking I/O bound tasks."""
    url = "http://example.com"
    iterations = 4
    
    print("\nBenchmarking I/O-Bound Task (Simulated Network)")
    
    start = time.time()
    run_threads_io(url, iterations)
    print(f"Threading time: {time.time() - start:.2f}s (Fast, GIL doesn't block I/O)")
    
    start = time.time()
    run_processes_io(url, iterations)
    print(f"Multiprocessing time: {time.time() - start:.2f}s (Fast, but high overhead to spawn processes)")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Using Multiprocessing for downloading 100 web pages.
# Correction: Process creation is expensive (high memory and time overhead). Threading is vastly superior for I/O bound tasks.

# Mistake: Using Threading for image processing or heavy calculations.
# Correction: Because of the GIL, threads cannot execute Python bytecodes in parallel. It will actually be slower than running it synchronously due to context switching overhead. Use Multiprocessing.

# Best Practice: 
# Math / Data Crunching = Multiprocessing.
# Network / File I/O = Threading or Asyncio.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: What is the GIL?
A: The Global Interpreter Lock. It's a mutex in CPython that protects access to Python objects, preventing multiple threads from executing Python bytecodes at once.

Q2: Why does multiprocessing bypass the GIL?
A: Multiprocessing creates entirely separate Python interpreter processes. Each process has its own memory space and its own GIL, allowing true parallelism across multiple CPU cores.

Q3: Why is threading still useful in Python despite the GIL?
A: When a thread performs an I/O operation (like network request or file read), it releases the GIL. This allows other threads to run while the first thread is waiting for the external resource.

Q4: Which has higher overhead: Threading or Multiprocessing?
A: Multiprocessing. It requires the OS to allocate new memory spaces and duplicate resources. Threads are lightweight.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Write a script that reads 5 large text files. Experiment using a single thread, ThreadPoolExecutor, and ProcessPoolExecutor. Note the time differences.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

"""
Challenge:
Create a hybrid architecture. You have 20 image URLs to download and process (convert to grayscale).
Use `threading` to download the images efficiently.
Once downloaded, pass the image data to a `multiprocessing.Pool` to handle the CPU-heavy image processing.
"""

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- CPU-Bound: Use `multiprocessing` to utilize multiple cores and bypass GIL.
- I/O-Bound: Use `threading` to handle wait times concurrently with low overhead.
- Profiling and benchmarking are essential before deciding on concurrency models.
"""

if __name__ == "__main__":
    benchmark_cpu()
    benchmark_io()
