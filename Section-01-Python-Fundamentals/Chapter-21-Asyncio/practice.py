"""
Topic: Asyncio Practice and Exercises
Chapter: 21
Level: Intermediate

Description:
    This file contains practice problems that consolidate your understanding of asyncio concepts, including coroutines, tasks, event loops, and synchronization primitives.

Real-Life Analogy:
    This is like a flight simulator for pilots. You've learned the theory of flying (asyncio concepts), now it's time to sit in the mock cockpit and handle various scenarios (practice exercises) before flying a real plane (building production apps).

Key Concepts:
    - Bringing it all together
    - Debugging async code
    - Handling concurrency edge cases
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================
import asyncio
import time
import random

# Helper function for exercises
async def mock_io_task(name, duration, fail=False):
    print(f"Task {name} started (duration: {duration}s)")
    await asyncio.sleep(duration)
    if fail:
        print(f"Task {name} FAILED!")
        raise RuntimeError(f"Task {name} encountered an error.")
    print(f"Task {name} completed.")
    return f"Result of {name}"

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES (EXERCISES)
# ============================================================

# EXERCISE 1: The Race
# Run three tasks concurrently. Only print the result of the one that finishes FIRST.
# Hint: Use asyncio.wait with return_when=asyncio.FIRST_COMPLETED
async def exercise_1():
    print("\n--- Exercise 1 ---")
    tasks = [
        asyncio.create_task(mock_io_task("Slow", 3)),
        asyncio.create_task(mock_io_task("Fast", 1)),
        asyncio.create_task(mock_io_task("Medium", 2))
    ]
    
    # TODO: Implement the logic to wait for the first completed task
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    for task in done:
        print(f"The winner is: {task.result()}")
        
    # Cancel the remaining tasks so they don't keep running in the background
    for task in pending:
        task.cancel()

# ============================================================
# SECTION 3: ADVANCED USAGE (EXERCISES)
# ============================================================

# EXERCISE 2: Resilient Execution
# Run multiple tasks where some might fail. Use asyncio.gather, but ensure that 
# one failing task doesn't crash the whole gather operation.
# Hint: Look at the `return_exceptions` parameter of asyncio.gather.
async def exercise_2():
    print("\n--- Exercise 2 ---")
    tasks = [
        mock_io_task("A", 1),
        mock_io_task("B", 1.5, fail=True), # This one fails
        mock_io_task("C", 2)
    ]
    
    # TODO: Run tasks and handle exceptions in the results list
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    for i, res in enumerate(results):
        if isinstance(res, Exception):
            print(f"Task {i} resulted in an error: {res}")
        else:
            print(f"Task {i} succeeded: {res}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# EXERCISE 3: Fixing the deadlock
# The following code has a logical flaw that causes it to hang indefinitely.
# Identify the problem and fix it. (Uncomment to test, but be prepared to force quit).

async def bad_producer(queue):
    for i in range(3):
        await queue.put(i)
        print(f"Put {i}")
    # FIX: The producer never tells the consumer it's done!
    # In a real scenario, you either need queue.join() in main, 
    # or put a sentinel value (like None) into the queue.

async def bad_consumer(queue):
    while True:
        item = await queue.get()
        if item is None: # Added sentinel check for graceful exit
            break
        print(f"Got {item}")
        queue.task_done()

async def exercise_3_fixed():
    print("\n--- Exercise 3 ---")
    q = asyncio.Queue()
    
    consumer_task = asyncio.create_task(bad_consumer(q))
    
    await bad_producer(q)
    
    # Wait for the queue to be processed
    await q.join() 
    
    # Stop consumer
    await q.put(None)
    await consumer_task
    print("Exercise 3 completed successfully without hanging.")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q: How do you handle a scenario where you want to timeout a specific coroutine?
# A: Wrap it with `asyncio.wait_for(coro, timeout=seconds)`.

# Q: If `asyncio.gather` fails with an exception by default, what happens to the other running tasks?
# A: They continue running in the background unless explicitly cancelled, even though `gather` immediately raises the exception.

# Q: What is an async lock used for?
# A: To prevent multiple coroutines from modifying shared mutable state concurrently, similar to threading locks, although race conditions are less common in asyncio due to cooperative multitasking.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# (The exercises are integrated into the sections above for this practice file)

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge: Rate-Limited Retries
# Create an async function `fetch_with_retry(url)` that simulates fetching a URL.
# It should fail 70% of the time.
# Implement a retry mechanism that tries up to 3 times, with an exponential backoff (e.g., sleep 1s, then 2s, then 4s) between retries.

async def fetch_with_retry():
    print("\n--- Mini Challenge ---")
    for attempt in range(1, 4):
        print(f"Attempt {attempt}...")
        await asyncio.sleep(0.5)
        success = random.random() > 0.7
        if success:
            print("Success!")
            return True
        else:
            print("Failed.")
            if attempt < 3:
                delay = 2 ** (attempt - 1)
                print(f"Waiting {delay}s before next attempt...")
                await asyncio.sleep(delay)
    
    print("All attempts failed.")
    return False

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Practice is essential for mastering asynchronous flows.
# - Managing task lifecycle (creation, awaiting, cancellation) is a core skill.
# - Handling exceptions concurrently requires careful use of `return_exceptions`.
# - Avoiding deadlocks requires understanding how `Queue` and `join()` interact.

async def main():
    await exercise_1()
    await exercise_2()
    await exercise_3_fixed()
    await fetch_with_retry()

if __name__ == "__main__":
    asyncio.run(main())
