"""
Topic: Concurrent Futures
Chapter: 20
Level: Intermediate

Description:
    The `concurrent.futures` module provides a high-level interface for asynchronously executing callables. 
    It abstracts away the low-level details of thread creation and queue management, providing a cleaner API than the `threading` module directly.

Real-Life Analogy:
    Ordering food at a busy restaurant. You place your order and receive a buzzer (a Future). 
    You don't need to stand by the kitchen and wait. You can do other things until the buzzer goes off, indicating your food (the result) is ready.

Key Concepts:
    - concurrent.futures.ThreadPoolExecutor
    - Futures (Future objects)
    - executor.submit()
    - executor.map()
    - as_completed()
"""

import concurrent.futures
import time
import random

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def slow_task(name):
    print(f"Task {name} starting...")
    time.sleep(1)
    return f"Task {name} finished"

def section_1():
    print("--- Section 1: Basic Syntax ---")
    # Context manager automatically manages the thread pool and waits for tasks to finish
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # submit() schedules the callable to be executed and returns a Future object
        future1 = executor.submit(slow_task, "A")
        future2 = executor.submit(slow_task, "B")
        
        # result() blocks until the future is completed and returns the value
        print(future1.result())
        print(future2.result())
    print("Section 1 finished.\n")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES (using map)
# ============================================================

def process_item(item):
    time.sleep(random.uniform(0.1, 0.5))
    return item * item

def section_2():
    print("--- Section 2: Using map() ---")
    items = [1, 2, 3, 4, 5]
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # map() applies the function to the iterable, similar to the built-in map()
        # It returns results in the exact same order as the input iterable
        results = executor.map(process_item, items)
        
        for result in results:
            print(f"Result: {result}")
            
    print("Section 2 finished.\n")

# ============================================================
# SECTION 3: ADVANCED USAGE (as_completed)
# ============================================================

def fetch_data(id):
    sleep_time = random.uniform(0.5, 1.5)
    time.sleep(sleep_time)
    return f"Data {id} (took {sleep_time:.2f}s)"

def section_3():
    print("--- Section 3: as_completed() ---")
    # as_completed yields futures as they complete, regardless of the order they were submitted
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # List comprehension to submit all tasks
        futures = [executor.submit(fetch_data, i) for i in range(1, 6)]
        
        # Iterate over them as they finish
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
            
    print("Section 3 finished.\n")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Calling .result() immediately after .submit() in a loop. This completely eliminates concurrency because you block on each task before starting the next.
# Bad:
# for i in range(5):
#     res = executor.submit(func, i).result() # Blocks here!
#
# Best Practice: Store all futures in a list first, THEN iterate over them (or use as_completed) to get results.

def section_4():
    print("--- Section 4: Common Mistakes ---")
    print("Don't block on .result() inside the submission loop!\n")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# 1. What is a Future object?
# A: It represents the execution of a callable that may not have completed yet. It allows checking status, waiting for completion, and retrieving the result or exception.
#
# 2. What is the difference between executor.map() and as_completed()?
# A: map() returns results in the order the inputs were provided. as_completed() yields results as soon as they finish, which might be out of order.
#
# 3. Why prefer concurrent.futures over the raw threading module?
# A: It provides a higher-level, cleaner, and more robust API for managing pools of threads and retrieving return values from threaded functions.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Create a list of URLs (can be mock strings). Use ThreadPoolExecutor and map() to simulate downloading them concurrently.
# Exercise 2: Modify the above to use submit() and as_completed() so you can print a message the exact moment each download finishes.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Build a concurrent status checker.
# Given a list of server IPs, check their status (simulate with a random success/failure and delay).
# Collect the results as they finish and print a final summary of how many succeeded vs failed.

def check_server(ip):
    time.sleep(random.uniform(0.1, 1.0))
    if random.choice([True, False]):
        return (ip, "ONLINE")
    else:
        return (ip, "OFFLINE")

def run_challenge():
    print("--- Section 7: Mini Challenge ---")
    servers = [f"192.168.1.{i}" for i in range(1, 11)]
    online = 0
    offline = 0
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(check_server, ip): ip for ip in servers}
        
        for future in concurrent.futures.as_completed(futures):
            ip, status = future.result()
            print(f"Checked {ip}: {status}")
            if status == "ONLINE":
                online += 1
            else:
                offline += 1
                
    print(f"Summary -> Online: {online}, Offline: {offline}")
    print("Challenge completed.\n")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - concurrent.futures is the modern way to handle multithreading in Python.
# - ThreadPoolExecutor manages the pool lifecycle easily with context managers.
# - executor.submit() schedules a single task and returns a Future.
# - concurrent.futures.as_completed() is excellent for processing results as soon as they are ready.

if __name__ == "__main__":
    section_1()
    section_2()
    section_3()
    section_4()
    run_challenge()
