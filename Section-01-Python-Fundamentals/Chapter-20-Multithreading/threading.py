# Topic: Threading Basics
# Explanation: Multithreading allows multiple tasks to run concurrently.

# Syntax:
# import threading

def worker():
    print("Thread running")

thread = threading.Thread(target=worker)
thread.start()
thread.join()

# Examples:
# import threading

def worker():
    print("Thread running")

thread = threading.Thread(target=worker)
thread.start()
thread.join()

# Practice Programs:
# 1. Create two threads that print messages.
2. Join them.

# Interview Questions:
# Q: What is a thread?
A: A thread is a lightweight unit of execution within a process.

# Expected Output:
# Thread running

import threading

def worker():
    print("Thread running")

thread = threading.Thread(target=worker)
thread.start()
thread.join()
