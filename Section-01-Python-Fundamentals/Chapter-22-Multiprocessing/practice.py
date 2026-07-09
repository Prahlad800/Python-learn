"""
Topic: Practice Exercises
Chapter: 22
Level: Beginner to Advanced

Description:
    This file contains solutions and structures for practicing Multiprocessing concepts including Process creation, Pools, Queues, and Synchronization.
"""

import multiprocessing
import time
import os

# ============================================================
# EXERCISE 1: BASIC PROCESSES
# ============================================================
# Goal: Spawn 3 processes. Each counts down from 5 to 1.

def countdown(proc_num: int) -> None:
    for i in range(5, 0, -1):
        print(f"[Proc-{proc_num} PID {os.getpid()}] Countdown: {i}")
        time.sleep(0.3)

def run_exercise_1():
    print("\n--- Exercise 1 ---")
    procs = []
    for i in range(3):
        p = multiprocessing.Process(target=countdown, args=(i+1,))
        procs.append(p)
        p.start()
        
    for p in procs:
        p.join()

# ============================================================
# EXERCISE 2: PROCESS POOLS
# ============================================================
# Goal: Calculate factorials for numbers 1 to 10 using a Pool.

def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def run_exercise_2():
    print("\n--- Exercise 2 ---")
    numbers = list(range(1, 11))
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(factorial, numbers)
    print(f"Factorials of 1-10: {results}")

# ============================================================
# EXERCISE 3: QUEUES
# ============================================================
# Goal: Process A puts 5 random numbers in Queue. Process B prints squares.

def queue_producer(q: multiprocessing.Queue):
    import random
    for _ in range(5):
        num = random.randint(1, 20)
        print(f"Produced: {num}")
        q.put(num)
        time.sleep(0.1)
    q.put("DONE")

def queue_consumer(q: multiprocessing.Queue):
    while True:
        item = q.get()
        if item == "DONE":
            break
        print(f"Consumed and Squared: {item**2}")

def run_exercise_3():
    print("\n--- Exercise 3 ---")
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=queue_producer, args=(q,))
    p2 = multiprocessing.Process(target=queue_consumer, args=(q,))
    
    p1.start()
    p2.start()
    p1.join()
    p2.join()

# ============================================================
# EXERCISE 4: LOCKS
# ============================================================
# Goal: Use a Lock to prevent scrambled printing.

def locked_print(lock: multiprocessing.Lock, word: str):
    with lock:
        for char in word:
            print(char, end='', flush=True)
            time.sleep(0.05)
        print()

def run_exercise_4():
    print("\n--- Exercise 4 ---")
    lock = multiprocessing.Lock()
    words = ["Python", "Concurrency", "Multiprocessing"]
    procs = [multiprocessing.Process(target=locked_print, args=(lock, w)) for w in words]
    
    for p in procs:
        p.start()
    for p in procs:
        p.join()

if __name__ == "__main__":
    run_exercise_1()
    run_exercise_2()
    run_exercise_3()
    run_exercise_4()
