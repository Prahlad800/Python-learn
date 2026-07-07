# Topic: Locks
# Explanation: Locks protect shared resources from concurrent writes.

# Syntax:
# import threading

lock = threading.Lock()

def safe_print():
    with lock:
        print("Locked section")

thread = threading.Thread(target=safe_print)
thread.start()
thread.join()

# Examples:
# import threading

lock = threading.Lock()

def safe_print():
    with lock:
        print("Locked section")

thread = threading.Thread(target=safe_print)
thread.start()
thread.join()

# Practice Programs:
# 1. Create a lock and use it around shared data.
2. Prevent race conditions.

# Interview Questions:
# Q: Why use a lock?
A: It ensures thread safety for shared resources.

# Expected Output:
# Locked section

import threading

lock = threading.Lock()

def safe_print():
    with lock:
        print("Locked section")

thread = threading.Thread(target=safe_print)
thread.start()
thread.join()
