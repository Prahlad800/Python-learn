"""
Topic: Thread Communication (Queues)
Chapter: 20
Level: Intermediate

Description:
    When multiple threads need to exchange data safely without stepping on each other's toes, Python's `queue` module provides thread-safe data structures.
    These queues automatically handle all the necessary locking under the hood.

Real-Life Analogy:
    A fast-food drive-thru. Customers (producer threads) place orders into a queue. 
    The kitchen staff (consumer threads) take orders from the queue one by one and process them.

Key Concepts:
    - queue.Queue (FIFO)
    - queue.LifoQueue (LIFO)
    - queue.PriorityQueue
    - q.put() and q.get()
    - q.task_done() and q.join()
"""

import threading
import queue
import time
import random

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def worker_basic(q, worker_id):
    while True:
        try:
            # get(block=False) raises queue.Empty if the queue is empty
            item = q.get(block=False)
            print(f"Worker {worker_id} processing {item}")
            time.sleep(0.1)
            q.task_done()
        except queue.Empty:
            break

def section_1():
    print("--- Section 1: Basic Queue ---")
    q = queue.Queue()
    
    for i in range(5):
        q.put(f"Task-{i}")
        
    threads = [threading.Thread(target=worker_basic, args=(q, i)) for i in range(2)]
    
    for t in threads:
        t.start()
        
    # Block until all tasks in the queue have been processed
    q.join()
    
    for t in threads:
        t.join()
    print("Section 1 finished.\n")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES (Different Queue Types)
# ============================================================

def section_2():
    print("--- Section 2: LIFO and Priority Queues ---")
    
    # 1. LifoQueue (Stack)
    lifo_q = queue.LifoQueue()
    lifo_q.put("First")
    lifo_q.put("Second")
    lifo_q.put("Third")
    
    print("LIFO Queue popping order:")
    while not lifo_q.empty():
        print(lifo_q.get())
        
    print("\nPriority Queue popping order:")
    # 2. PriorityQueue (Lowest number = highest priority)
    pq = queue.PriorityQueue()
    pq.put((3, "Low Priority Task"))
    pq.put((1, "High Priority Task"))
    pq.put((2, "Medium Priority Task"))
    
    while not pq.empty():
        priority, task = pq.get()
        print(f"Priority {priority}: {task}")
        
    print("Section 2 finished.\n")

# ============================================================
# SECTION 3: ADVANCED USAGE (Blocking and Timeouts)
# ============================================================

def consumer(q):
    while True:
        try:
            # Block for at most 2 seconds waiting for an item
            item = q.get(timeout=2)
            print(f"Consumed: {item}")
            q.task_done()
        except queue.Empty:
            print("Consumer timed out waiting for items. Exiting.")
            break

def section_3():
    print("--- Section 3: Advanced Usage ---")
    q = queue.Queue()
    t = threading.Thread(target=consumer, args=(q,))
    t.start()
    
    time.sleep(0.5)
    q.put("Item 1")
    time.sleep(0.5)
    q.put("Item 2")
    
    # Consumer will wait 2 seconds after Item 2 and then exit
    t.join()
    print("Section 3 finished.\n")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Using a standard list for thread communication. A list is not inherently thread-safe for complex operations.
# Mistake: Forgetting to call q.task_done() after processing an item if you intend to use q.join(). If you forget, q.join() blocks forever!
# Best Practice: Always use queue.Queue for producer-consumer patterns in multithreading.

def section_4():
    print("--- Section 4: Common Mistakes ---")
    print("Always call task_done() if you are using queue.join()!\n")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# 1. Why use queue.Queue instead of a normal list?
# A: queue.Queue is designed specifically for thread-safe communication and handles locking internally.
#
# 2. What does queue.join() do?
# A: It blocks until all items that have been put into the queue have been retrieved and processed (indicated by calling task_done()).
#
# 3. What happens if you call get() on an empty queue?
# A: By default, it blocks indefinitely until an item is available. You can use block=False or specify a timeout.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Create a system where one thread puts random numbers into a queue, and another thread calculates their squares and prints them.
# Exercise 2: Modify the above to use a PriorityQueue where even numbers have higher priority than odd numbers.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Build a log processor.
# Producer: Generates log messages with different severity levels (ERROR, WARN, INFO) and puts them in a PriorityQueue (ERROR first).
# Consumer: Reads messages and prints them.

def log_producer(q):
    logs = [
        (3, "INFO: User logged in"),
        (1, "ERROR: Database connection failed"),
        (2, "WARN: High memory usage"),
        (3, "INFO: File uploaded")
    ]
    for log in logs:
        q.put(log)
        time.sleep(0.1)

def log_consumer(q):
    while True:
        try:
            priority, message = q.get(timeout=1)
            print(f"Processed: {message}")
            q.task_done()
        except queue.Empty:
            break

def run_challenge():
    print("--- Section 7: Mini Challenge ---")
    log_queue = queue.PriorityQueue()
    
    prod = threading.Thread(target=log_producer, args=(log_queue,))
    cons = threading.Thread(target=log_consumer, args=(log_queue,))
    
    prod.start()
    cons.start()
    
    prod.join()
    cons.join()
    print("Challenge completed.\n")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Python's queue module provides thread-safe data structures.
# - Queue (FIFO), LifoQueue (Stack), and PriorityQueue are available.
# - Use put() to add and get() to retrieve items safely across threads.
# - task_done() and join() are useful for knowing when all work is finished.

if __name__ == "__main__":
    section_1()
    section_2()
    section_3()
    section_4()
    run_challenge()
