"""
Topic: Thread Synchronization (Events & Conditions)
Chapter: 20
Level: Intermediate

Description:
    Besides protecting shared data with Locks, threads often need to coordinate their actions. 
    Synchronization primitives like Events, Conditions, Barriers, and Semaphores allow threads to wait for certain states or signals from other threads.

Real-Life Analogy:
    Event: A starting gun at a race. All runners (threads) wait for the gun to fire (Event is set) before they start running.
    Semaphore: A nightclub with a capacity limit. Only a certain number of people (threads) can enter. As someone leaves, another can enter.

Key Concepts:
    - threading.Event
    - threading.Condition
    - threading.Semaphore
    - threading.Barrier
"""

import threading
import time
import random

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION (EVENTS)
# ============================================================

# Event provides a simple mechanism for communication between threads: one thread signals an event and other threads wait for it.

start_event = threading.Event()

def runner(name):
    print(f"{name} is ready and waiting for the signal...")
    start_event.wait()  # Block until the event is set
    print(f"{name} is running!")

def section_1():
    print("--- Section 1: Events ---")
    threads = [threading.Thread(target=runner, args=(f"Runner-{i}",)) for i in range(3)]
    
    for t in threads:
        t.start()
        
    time.sleep(1)
    print("Ready, Set, GO!")
    start_event.set()  # Signals all waiting threads to continue
    
    for t in threads:
        t.join()
    print("Section 1 finished.\n")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES (SEMAPHORES)
# ============================================================

# A Semaphore manages an internal counter which is decremented by each acquire() and incremented by each release().
# It is useful for limiting access to a resource with limited capacity.

max_connections = 2
pool_sema = threading.Semaphore(max_connections)

def access_database(thread_id):
    print(f"Thread {thread_id} waiting to access DB...")
    with pool_sema:
        print(f"-> Thread {thread_id} CONNECTED to DB.")
        time.sleep(random.uniform(0.5, 1.0))
        print(f"<- Thread {thread_id} DISCONNECTED from DB.")

def section_2():
    print("--- Section 2: Semaphores ---")
    threads = [threading.Thread(target=access_database, args=(i,)) for i in range(5)]
    
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("Section 2 finished.\n")

# ============================================================
# SECTION 3: ADVANCED USAGE (BARRIERS & CONDITIONS)
# ============================================================

# A Barrier ensures that a specified number of threads all reach a certain point before any of them are allowed to proceed.
barrier = threading.Barrier(3)

def worker(worker_id):
    print(f"Worker {worker_id} doing initial setup...")
    time.sleep(random.uniform(0.1, 0.5))
    print(f"Worker {worker_id} waiting at barrier...")
    barrier.wait()
    print(f"Worker {worker_id} passed the barrier and is continuing work.")

def section_3():
    print("--- Section 3: Barriers ---")
    threads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]
    
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("Section 3 finished.\n")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Using a loop with sleep to check for a condition (busy waiting) instead of using an Event.
# Bad:
# while not flag:
#     time.sleep(0.1)
# Good:
# event.wait()
#
# Best Practice: Use the highest level synchronization primitive that fits your need. Events are simpler than Conditions. Semaphores are simpler for resource pools than building your own with Locks.

def section_4():
    print("--- Section 4: Common Mistakes ---")
    print("Avoid busy-waiting. Use proper synchronization primitives.\n")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# 1. What is the difference between a Lock and a Semaphore?
# A: A Lock allows only one thread to access a resource. A Semaphore allows a specified number of threads to access a resource concurrently.
#
# 2. When would you use a threading.Event?
# A: When you need one or more threads to wait until another thread completes an action or reaches a specific state, and then broadcast a signal to all waiting threads.
#
# 3. What does threading.Barrier do?
# A: It synchronizes a fixed number of threads, making them wait at a designated barrier point until all threads have reached that point.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Use an Event to create a pause/resume functionality for a worker thread that is continuously printing numbers.
# Exercise 2: Use a Semaphore to simulate a parking lot with 5 spaces and 10 cars trying to park.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Simulate a download manager. 
# You have 1 "Downloader" thread that downloads chunks of data, and 2 "Processor" threads that wait until the Downloader signals that a chunk is ready via a Condition variable.
# (Note: For simplicity, we use Event here, but Condition is also suitable).

def run_challenge():
    print("--- Section 7: Mini Challenge ---")
    data_ready_event = threading.Event()
    
    def downloader():
        print("Downloader: Downloading data...")
        time.sleep(1)
        print("Downloader: Data is ready!")
        data_ready_event.set()
        
    def processor(pid):
        print(f"Processor {pid}: Waiting for data...")
        data_ready_event.wait()
        print(f"Processor {pid}: Processing data.")
        
    t1 = threading.Thread(target=downloader)
    p1 = threading.Thread(target=processor, args=(1,))
    p2 = threading.Thread(target=processor, args=(2,))
    
    p1.start(); p2.start(); t1.start()
    t1.join(); p1.join(); p2.join()
    print("Challenge completed.\n")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Events are great for signaling between threads (e.g., start/stop signals).
# - Semaphores are perfect for limiting access to a pool of resources.
# - Barriers synchronize a group of threads to start a phase simultaneously.
# - Avoiding busy-waiting by using these primitives is crucial for performance.

if __name__ == "__main__":
    section_1()
    section_2()
    section_3()
    section_4()
    run_challenge()
