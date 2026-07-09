"""
Topic: Thread Locks (Mutexes)
Chapter: 20
Level: Intermediate

Description:
    When multiple threads access and modify shared data simultaneously, a race condition can occur, leading to unpredictable results.
    A Lock (or Mutex) prevents this by ensuring that only one thread can execute a specific section of code at a time.

Real-Life Analogy:
    Imagine a shared bathroom with a single key. Only one person can have the key and use the bathroom at a time. 
    Others must wait until the key is returned (unlocked) before they can enter.

Key Concepts:
    - Race Conditions
    - threading.Lock
    - acquire() and release()
    - Deadlocks
    - Context Managers for Locks
"""

import threading
import time

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# A shared resource
counter = 0

def increment_without_lock():
    global counter
    for _ in range(100000):
        counter += 1

def section_1():
    print("--- Section 1: Basic Syntax (The Problem) ---")
    global counter
    counter = 0
    
    t1 = threading.Thread(target=increment_without_lock)
    t2 = threading.Thread(target=increment_without_lock)
    
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    print(f"Expected 200000, got: {counter} (Notice it might be less due to race condition)")
    print("Section 1 finished.\n")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

safe_counter = 0
lock = threading.Lock()

def increment_with_lock():
    global safe_counter
    for _ in range(100000):
        # Using context manager is the best practice for locks
        with lock:
            safe_counter += 1
            
        # The above is equivalent to:
        # lock.acquire()
        # try:
        #     safe_counter += 1
        # finally:
        #     lock.release()

def section_2():
    print("--- Section 2: Practical Examples (The Solution) ---")
    global safe_counter
    safe_counter = 0
    
    t1 = threading.Thread(target=increment_with_lock)
    t2 = threading.Thread(target=increment_with_lock)
    
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    print(f"Expected 200000, got: {safe_counter} (Thread-safe!)")
    print("Section 2 finished.\n")

# ============================================================
# SECTION 3: ADVANCED USAGE (RLock)
# ============================================================

# RLock (Reentrant Lock) allows the SAME thread to acquire the lock multiple times without deadlocking.

rlock = threading.RLock()

def recursive_function(n):
    with rlock:
        if n == 0:
            return 0
        else:
            return n + recursive_function(n - 1)

def section_3():
    print("--- Section 3: Advanced Usage (RLock) ---")
    result = recursive_function(5)
    print(f"Recursive sum of 5 using RLock: {result}")
    print("Section 3 finished.\n")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Forgetting to release a lock, leading to a Deadlock. Other threads will wait forever.
# Best Practice: ALWAYS use the `with` statement (context manager) when acquiring locks. It guarantees the lock is released even if an exception occurs.
# Mistake: Acquiring a standard Lock multiple times in the same thread (causes deadlock). Use RLock if you need reentrant behavior.

def section_4():
    print("--- Section 4: Common Mistakes ---")
    print("Avoid acquiring multiple locks in different orders across threads to prevent Deadlocks.\n")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# 1. What is a race condition?
# A: It occurs when two or more threads can access shared data and they try to change it at the same time, leading to unpredictable outcomes.
#
# 2. What is a Lock?
# A: A synchronization primitive that allows only one thread to execute a block of code at a time.
#
# 3. What is a Deadlock?
# A: A situation where two or more threads are blocked forever, waiting for each other to release locks.
#
# 4. What is the difference between Lock and RLock?
# A: A Lock can only be acquired once. If the same thread tries to acquire it again, it blocks. An RLock (Reentrant Lock) can be acquired multiple times by the SAME thread.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Create a BankAccount class with a balance. Implement deposit and withdraw methods. Create multiple threads that deposit and withdraw concurrently, and protect the balance with a Lock.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Implement a thread-safe Singleton class using a Lock.
# Only one instance of the class should ever be created, even if multiple threads try to instantiate it at the exact same time.

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                time.sleep(0.1)  # Simulate initialization delay
                cls._instance = super(ThreadSafeSingleton, cls).__new__(cls)
        return cls._instance

def create_instance(results, index):
    obj = ThreadSafeSingleton()
    results[index] = id(obj)

def run_challenge():
    print("--- Section 7: Mini Challenge ---")
    threads = []
    results = [None] * 5
    
    for i in range(5):
        t = threading.Thread(target=create_instance, args=(results, i))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    print(f"Instance IDs: {results}")
    print(f"All IDs are the same: {len(set(results)) == 1}")
    print("Challenge completed.\n")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Locks prevent race conditions by enforcing mutual exclusion.
# - Use the `with` statement to acquire and automatically release locks.
# - RLock is needed if a thread might need to acquire the same lock multiple times recursively.
# - Be wary of deadlocks when dealing with multiple locks.

if __name__ == "__main__":
    section_1()
    section_2()
    section_3()
    section_4()
    run_challenge()
