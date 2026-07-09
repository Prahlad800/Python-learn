"""
Topic: Process Synchronization (Locks, Semaphores, Events)
Chapter: 22
Level: Advanced

Description:
    When processes share resources (like memory, files, or stdout), they can step on each other's toes, leading to corrupted data or scrambled output. Synchronization primitives ensure orderly access to these shared resources.

Real-Life Analogy:
    A Lock is like the key to a single-occupancy bathroom. Only one person can hold the key and use the bathroom at a time.
    A Semaphore is a bathroom with 3 stalls and 3 keys.
    An Event is like a traffic light. All cars wait on red, and all proceed when the light turns green.

Key Concepts:
    - multiprocessing.Lock
    - multiprocessing.Semaphore
    - multiprocessing.Event
    - Critical Sections
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

import multiprocessing
import time
import os

def safe_printer(lock: multiprocessing.Lock, text: str) -> None:
    """Uses a lock to prevent stdout from getting scrambled."""
    # Acquire the lock. Other processes will block here until released.
    lock.acquire()
    try:
        # Critical Section
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)
        print() # New line
    finally:
        # Always release the lock in a finally block
        lock.release()

def lock_example() -> None:
    """Demonstrates using a Lock."""
    lock = multiprocessing.Lock()
    
    # Without a lock, these words would print interleaved (e.g., HWeorllldo)
    p1 = multiprocessing.Process(target=safe_printer, args=(lock, "Hello"))
    p2 = multiprocessing.Process(target=safe_printer, args=(lock, "World"))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def database_connection(semaphore: multiprocessing.Semaphore, worker_id: int) -> None:
    """Uses a semaphore to limit simultaneous connections."""
    print(f"Worker {worker_id} is waiting for a connection...")
    
    with semaphore: # Context manager automatically acquires/releases
        print(f"--> Worker {worker_id} ACQUIRED connection. Working...")
        time.sleep(1)
        print(f"<-- Worker {worker_id} RELEASED connection.")

def semaphore_example() -> None:
    """Demonstrates a Semaphore limiting access to a pool of resources."""
    # Allow a maximum of 2 simultaneous accesses
    semaphore = multiprocessing.Semaphore(2)
    
    processes = [multiprocessing.Process(target=database_connection, args=(semaphore, i)) for i in range(5)]
    
    for p in processes:
        p.start()
    for p in processes:
        p.join()

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def wait_for_event(event: multiprocessing.Event, name: str) -> None:
    """Waits for a global event to be set before proceeding."""
    print(f"[{name}] Waiting for the green light...")
    event.wait() # Blocks until event.is_set() is True
    print(f"[{name}] Green light! Executing task.")

def event_example() -> None:
    """Demonstrates an Event to coordinate multiple processes."""
    event = multiprocessing.Event()
    
    p1 = multiprocessing.Process(target=wait_for_event, args=(event, "Worker 1"))
    p2 = multiprocessing.Process(target=wait_for_event, args=(event, "Worker 2"))
    
    p1.start()
    p2.start()
    
    print("[Main] Initializing system (takes 2 seconds)...")
    time.sleep(2)
    
    print("[Main] System ready. Setting event!")
    event.set() # Wake up all processes waiting on this event
    
    p1.join()
    p2.join()

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Forgetting to release a lock. If an exception occurs in the critical section, the lock is never released, causing a Deadlock.
# Correction: ALWAYS use `lock.acquire()` and `lock.release()` inside a `try...finally` block, or use the `with lock:` context manager.

# Mistake: Deadlocks. When Process 1 holds Lock A and waits for Lock B, while Process 2 holds Lock B and waits for Lock A. Both wait forever.
# Best Practice: Acquire multiple locks in a consistent, defined order across all processes to avoid deadlocks.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: What is a Critical Section?
A: A segment of code that accesses shared resources (like memory or files) and must not be concurrently executed by more than one process/thread.

Q2: How does a Semaphore differ from a Lock?
A: A Lock allows only ONE process to enter the critical section. A Semaphore allows N processes to enter simultaneously, useful for connection pools or rate limiting.

Q3: What does `event.wait()` do?
A: It pauses the execution of the process until another process calls `event.set()`. 

Q4: What is a Deadlock?
A: A state where two or more processes are blocked indefinitely, each waiting for a resource that the other process holds.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Fix the race condition in `shared_memory.py` by passing a `multiprocessing.Lock` to the increment function and using a `with lock:` block around the += 1 operation.
Exercise 2: Use an Event to simulate a starting gun for a race. Create 3 "runner" processes that wait for the event, and a main process that sets it after 3 seconds.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

"""
Challenge: File Writer
Create a text file. Spawn 5 processes. Each process should write its PID 10 times to the file.
Use a `multiprocessing.Lock` to ensure that each process writes its 10 lines continuously without being interrupted by other processes writing their lines.
"""

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Synchronization is crucial when multiple processes access shared state.
- `Lock` prevents simultaneous access to a resource.
- `Semaphore` limits concurrent access to a set number.
- `Event` is used to broadcast state changes and trigger actions across processes.
- Context managers (`with` statement) are the safest way to handle locks.
"""

if __name__ == "__main__":
    print("--- Lock Example ---")
    lock_example()
    
    print("\n--- Semaphore Example ---")
    semaphore_example()
    
    print("\n--- Event Example ---")
    event_example()
