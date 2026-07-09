"""
Topic: Producer-Consumer Pattern
Chapter: 20
Level: Advanced

Description:
    The Producer-Consumer pattern is a classic concurrency design pattern. Producers generate data and put it into a buffer (queue). 
    Consumers take data from the buffer and process it. This decouples the generation of data from its processing.

Real-Life Analogy:
    A factory assembly line. Machines (producers) build car parts and place them on a conveyor belt (queue). 
    Workers further down the line (consumers) take the parts off the belt to assemble the car.

Key Concepts:
    - Decoupling tasks
    - Managing backpressure (maxsize queues)
    - Graceful shutdown (poison pills)
"""

import threading
import queue
import time
import random

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def producer(q, num_items):
    for i in range(num_items):
        item = f"Item-{i}"
        print(f"Producer created {item}")
        q.put(item)
        time.sleep(random.uniform(0.1, 0.3))

def consumer(q):
    while True:
        item = q.get()
        if item is None:  # Poison pill to stop the consumer
            q.task_done()
            break
        print(f"Consumer processed {item}")
        time.sleep(random.uniform(0.2, 0.5))
        q.task_done()

def section_1():
    print("--- Section 1: Basic Producer-Consumer ---")
    q = queue.Queue()
    
    prod = threading.Thread(target=producer, args=(q, 5))
    cons = threading.Thread(target=consumer, args=(q,))
    
    cons.start()
    prod.start()
    
    prod.join()  # Wait for producer to finish making items
    q.put(None)  # Send poison pill to stop consumer
    
    q.join()     # Wait for all items to be processed
    cons.join()
    print("Section 1 finished.\n")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES (Backpressure)
# ============================================================

# If producers are faster than consumers, the queue can grow infinitely, consuming all memory.
# By setting `maxsize`, we create backpressure: the producer will block when the queue is full.

def fast_producer(q, num_items):
    for i in range(num_items):
        print(f"Fast Producer trying to put Item-{i}")
        q.put(f"Item-{i}") # Will block if queue size == maxsize
        print(f"Fast Producer successfully put Item-{i}")

def slow_consumer(q):
    while True:
        item = q.get()
        if item is None:
            q.task_done()
            break
        print(f"  Slow Consumer processing {item}")
        time.sleep(0.5) # Consumer is much slower
        q.task_done()

def section_2():
    print("--- Section 2: Managing Backpressure ---")
    # Queue can hold a maximum of 3 items at a time
    bounded_q = queue.Queue(maxsize=3)
    
    prod = threading.Thread(target=fast_producer, args=(bounded_q, 6))
    cons = threading.Thread(target=slow_consumer, args=(bounded_q,))
    
    cons.start()
    prod.start()
    
    prod.join()
    bounded_q.put(None)
    bounded_q.join()
    cons.join()
    print("Section 2 finished.\n")

# ============================================================
# SECTION 3: ADVANCED USAGE (Multiple Producers & Consumers)
# ============================================================

def multi_producer(q, p_id):
    for i in range(3):
        q.put(f"Task from P{p_id}-{i}")
        time.sleep(0.1)

def multi_consumer(q, c_id):
    while True:
        item = q.get()
        if item == "STOP":
            q.task_done()
            break
        print(f"Consumer {c_id} handled {item}")
        time.sleep(0.2)
        q.task_done()

def section_3():
    print("--- Section 3: Multiple Producers and Consumers ---")
    q = queue.Queue()
    
    producers = [threading.Thread(target=multi_producer, args=(q, i)) for i in range(2)]
    consumers = [threading.Thread(target=multi_consumer, args=(q, i)) for i in range(3)]
    
    for c in consumers: c.start()
    for p in producers: p.start()
        
    for p in producers: p.join()
        
    # We have 3 consumers, so we need 3 stop signals
    for _ in range(3):
        q.put("STOP")
        
    q.join()
    for c in consumers: c.join()
    print("Section 3 finished.\n")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Forgetting to send a "poison pill" or stop signal. The consumer threads will wait on q.get() forever (deadlock at exit).
# Best Practice: Always send as many poison pills as there are active consumer threads.
# Best Practice: Use maxsize on queues if producers can significantly outpace consumers to prevent out-of-memory errors.

def section_4():
    print("--- Section 4: Common Mistakes ---")
    print("Always ensure consumers have a way to gracefully exit their infinite loop.\n")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# 1. What is the Producer-Consumer pattern?
# A: A concurrency pattern where one or more threads create data (producers) and put it into a shared buffer, while one or more threads pull data from the buffer to process it (consumers).
#
# 2. What is a 'poison pill' in this context?
# A: A specific value (like None or "STOP") put into the queue that signals a consumer thread to exit its processing loop.
#
# 3. How do you prevent memory exhaustion if producers are faster than consumers?
# A: By using a bounded queue (queue.Queue(maxsize=N)). The producer's put() method will block until there is space in the queue.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Implement a web crawler architecture. Producers find URLs and put them in a queue. Consumers take URLs, download the page, and parse it.
# Exercise 2: Modify the pattern so that consumers can also act as producers (e.g., if a parsed page contains more URLs, the consumer puts them back into the queue).

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Build a simple data pipeline.
# Stage 1 (Producer): Generates raw strings.
# Stage 2 (Worker): Cleans the strings (e.g., uppercase them) and passes them to the next queue.
# Stage 3 (Consumer): Prints the final strings.

def raw_producer(q_out):
    for word in ["hello", "world", "python", "threading"]:
        q_out.put(word)
    q_out.put(None)

def cleaner_worker(q_in, q_out):
    while True:
        item = q_in.get()
        if item is None:
            q_out.put(None)
            q_in.task_done()
            break
        cleaned = item.upper()
        q_out.put(cleaned)
        q_in.task_done()

def final_consumer(q_in):
    while True:
        item = q_in.get()
        if item is None:
            q_in.task_done()
            break
        print(f"Final output: {item}")
        q_in.task_done()

def run_challenge():
    print("--- Section 7: Mini Challenge ---")
    q1 = queue.Queue()
    q2 = queue.Queue()
    
    t_prod = threading.Thread(target=raw_producer, args=(q1,))
    t_work = threading.Thread(target=cleaner_worker, args=(q1, q2))
    t_cons = threading.Thread(target=final_consumer, args=(q2,))
    
    t_cons.start()
    t_work.start()
    t_prod.start()
    
    t_prod.join()
    t_work.join()
    t_cons.join()
    print("Challenge completed.\n")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - The Producer-Consumer pattern separates data creation from data processing.
# - Use queue.Queue to pass data safely between threads.
# - Use maxsize to apply backpressure.
# - Send poison pills to shut down consumer threads cleanly.

if __name__ == "__main__":
    section_1()
    section_2()
    section_3()
    section_4()
    run_challenge()
