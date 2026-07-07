# Topic: Thread Pools
# Explanation: Thread pools manage worker threads efficiently.

# Syntax:
# from concurrent.futures import ThreadPoolExecutor

def task(value):
    return value * 2

with ThreadPoolExecutor(max_workers=2) as executor:
    result = executor.submit(task, 5).result()
    print(result)

# Examples:
# from concurrent.futures import ThreadPoolExecutor

def task(value):
    return value * 2

with ThreadPoolExecutor(max_workers=2) as executor:
    result = executor.submit(task, 5).result()
    print(result)

# Practice Programs:
# 1. Submit multiple tasks to a thread pool.
2. Collect the results.

# Interview Questions:
# Q: Why use a thread pool?
A: It reduces the overhead of creating and destroying threads repeatedly.

# Expected Output:
# 10

from concurrent.futures import ThreadPoolExecutor

def task(value):
    return value * 2

with ThreadPoolExecutor(max_workers=2) as executor:
    result = executor.submit(task, 5).result()
    print(result)
