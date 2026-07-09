"""
Topic: Thread Safety
Chapter: 20
Level: Advanced

Description:
    Thread safety implies that an object or block of code can be accessed concurrently by multiple threads without causing unintended behaviors or race conditions.
    Understanding what operations are atomic (indivisible) in Python is crucial for writing thread-safe code.

Real-Life Analogy:
    A shared whiteboard. If two people try to write on the exact same spot at the exact same time without coordinating (not thread-safe), the result is illegible scribbles.

Key Concepts:
    - Atomicity in Python
    - Mutable vs Immutable shared state
    - Thread-local data
    - Identifying non-thread-safe operations
"""

import threading
import time

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# In Python (CPython), some operations are atomic due to the Global Interpreter Lock (GIL), like appending to a list.
# However, operations like += on integers are NOT atomic because they involve read, modify, and write steps.

shared_list = []
shared_int = 0

def non_atomic_add():
    global shared_int
    for _ in range(100000):
        # NOT thread-safe: read shared_int, add 1, write back to shared_int
        shared_int += 1

def atomic_append():
    global shared_list
    for i in range(100000):
        # Thread-safe in CPython: appending to a list is an atomic operation
        shared_list.append(i)

def section_1():
    print("--- Section 1: Atomicity ---")
    t1 = threading.Thread(target=non_atomic_add)
    t2 = threading.Thread(target=non_atomic_add)
    t1.start(); t2.start()
    t1.join(); t2.join()
    print(f"Expected int: 200000, Got: {shared_int} (Not safe)")
    
    t3 = threading.Thread(target=atomic_append)
    t4 = threading.Thread(target=atomic_append)
    t3.start(); t4.start()
    t3.join(); t4.join()
    print(f"Expected list length: 200000, Got: {len(shared_list)} (Safe in CPython)")
    print("Section 1 finished.\n")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES (Thread-Local Data)
# ============================================================

# Sometimes you don't want to share state. You want each thread to have its own isolated copy of data.
thread_local_data = threading.local()

def process_data(name):
    # This attribute 'value' is unique to the current thread
    thread_local_data.value = name
    time.sleep(0.1)
    print(f"Thread {threading.current_thread().name} sees value: {thread_local_data.value}")

def section_2():
    print("--- Section 2: Thread-Local Data ---")
    threads = []
    for i in range(3):
        t = threading.Thread(target=process_data, args=(f"Data-{i}",), name=f"Worker-{i}")
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
    print("Section 2 finished.\n")

# ============================================================
# SECTION 3: ADVANCED USAGE (Designing a Thread-Safe Class)
# ============================================================

class ThreadSafeCounter:
    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()
        
    def increment(self):
        with self._lock:
            self._value += 1
            
    def get_value(self):
        with self._lock:
            return self._value

def increment_worker(counter):
    for _ in range(10000):
        counter.increment()

def section_3():
    print("--- Section 3: Thread-Safe Class ---")
    counter = ThreadSafeCounter()
    threads = [threading.Thread(target=increment_worker, args=(counter,)) for _ in range(5)]
    
    for t in threads: t.start()
    for t in threads: t.join()
        
    print(f"Final counter value: {counter.get_value()}")
    print("Section 3 finished.\n")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Assuming that because Python has the GIL, all your code is automatically thread-safe. It is not.
# Mistake: Sharing mutable state (like dicts or objects) across threads without synchronization when multiple threads are modifying it.
# Best Practice: Minimize shared state. If threads don't share data, you don't need locks. Use Queues to pass data instead of sharing it directly.

def section_4():
    print("--- Section 4: Common Mistakes ---")
    print("The GIL does NOT protect you from race conditions in your own logic!\n")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# 1. What does it mean for an operation to be atomic?
# A: It means the operation completes in a single step relative to other threads; it cannot be interrupted halfway through.
#
# 2. What is threading.local() used for?
# A: To create data that is specific to the thread that is accessing it. Other threads cannot see or modify it.
#
# 3. How do you make a custom class thread-safe?
# A: By encapsulating shared state and protecting all read/modify/write access to that state with internal Locks.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Create a non-thread-safe banking class where withdrawals subtract from a balance. Demonstrate a race condition where the balance drops below zero incorrectly.
# Exercise 2: Fix the banking class using threading.Lock.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Create a Thread-Safe Cache class.
# It should act like a dictionary where you can `set(key, value)` and `get(key)`.
# Multiple threads will try to write and read from it simultaneously.

class ThreadSafeCache:
    def __init__(self):
        self._cache = {}
        self._lock = threading.RLock()
        
    def set(self, key, value):
        with self._lock:
            self._cache[key] = value
            
    def get(self, key):
        with self._lock:
            return self._cache.get(key, None)

def cache_writer(cache, idx):
    cache.set(f"key_{idx}", f"value_{idx}")
    
def cache_reader(cache, idx):
    time.sleep(0.01)
    val = cache.get(f"key_{idx}")
    if val is None:
        print(f"Missed key_{idx}")

def run_challenge():
    print("--- Section 7: Mini Challenge ---")
    cache = ThreadSafeCache()
    threads = []
    
    # Start writers and readers concurrently
    for i in range(50):
        threads.append(threading.Thread(target=cache_writer, args=(cache, i)))
        threads.append(threading.Thread(target=cache_reader, args=(cache, i)))
        
    for t in threads:
        t.start()
    for t in threads:
        t.join()
        
    print("All reads/writes completed safely.")
    print(f"Cache size: {len(cache._cache)}")
    print("Challenge completed.\n")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Thread safety is required when threads share mutable state.
# - The `+=` operation is not atomic in Python.
# - Use threading.local() for thread-specific data.
# - Build thread-safe classes by internalizing Locks and protecting state mutations.

if __name__ == "__main__":
    section_1()
    section_2()
    section_3()
    section_4()
    run_challenge()
