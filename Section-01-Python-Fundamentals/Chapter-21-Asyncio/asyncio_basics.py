"""
Topic: Asyncio Basics
Chapter: 21
Level: Beginner

Description:
    `asyncio` is a library to write concurrent code using the async/await syntax. It's designed to handle a large number of concurrent I/O-bound tasks using a single thread and an event loop.

Real-Life Analogy:
    Think of a single waiter in a restaurant. Instead of waiting for one table to finish eating before serving the next (synchronous), the waiter takes an order, goes to the kitchen, and while the food is cooking, takes orders from other tables. They juggle multiple tasks without being blocked by waiting.

Key Concepts:
    - Asynchronous programming
    - `async` and `await` keywords
    - The Event Loop
    - Non-blocking I/O
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================
import asyncio
import time

# To define an asynchronous function (coroutine), use the `async def` syntax.
async def greet():
    print("Hello...")
    # `await` yields control back to the event loop while waiting for the operation to complete.
    await asyncio.sleep(1) 
    print("...World!")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Running multiple coroutines concurrently
async def task_1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 finished")
    return "Result 1"

async def task_2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 finished")
    return "Result 2"

async def main():
    print(f"Main started at {time.strftime('%X')}")
    
    # asyncio.gather runs awaitables concurrently and waits for all of them
    results = await asyncio.gather(
        task_1(),
        task_2()
    )
    
    print(f"Main finished at {time.strftime('%X')}")
    print(f"Results: {results}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Handling timeouts with asyncio
async def slow_operation():
    await asyncio.sleep(3)
    return "Done"

async def timeout_example():
    try:
        # We wait for maximum 1.5 seconds. If it takes longer, a TimeoutError is raised.
        result = await asyncio.wait_for(slow_operation(), timeout=1.5)
        print(result)
    except asyncio.TimeoutError:
        print("Operation timed out!")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistakes:
# - Using blocking time.sleep() instead of await asyncio.sleep() in a coroutine. This blocks the whole event loop.
# - Forgetting to use `await` when calling an `async def` function. It returns a coroutine object, but doesn't execute it.

# Best Practices:
# - Keep event loop iterations short.
# - Use asyncio libraries for I/O (e.g., aiohttp for requests).
# - Use `asyncio.run(main())` as the main entry point to your async application.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q: What is the main difference between threading and asyncio?
# A: Threading uses multiple OS threads (preemptive multitasking), while asyncio uses a single thread and cooperatively yields control via the event loop.

# Q: What does `async def` do?
# A: It defines a coroutine function. When called, it doesn't run the code but returns a coroutine object.

# Q: Why shouldn't you use `time.sleep()` in an async function?
# A: `time.sleep()` blocks the entire thread, halting the event loop. `asyncio.sleep()` only suspends the current coroutine, allowing the event loop to run other tasks.

# Q: What is `asyncio.gather` used for?
# A: It's used to run multiple awaitables concurrently and aggregate their results into a list.

# Q: Can you mix synchronous and asynchronous code easily?
# A: It requires care. You can run synchronous code in an executor (thread/process pool) using `loop.run_in_executor` to avoid blocking the event loop.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write an async function that counts from 1 to 5, waiting 0.5 seconds between each print.
# Exercise 2: Create three async functions with different delays. Use gather to run them and print when all are done.
# Exercise 3: Intentionally use time.sleep() in one task and observe how it affects another concurrent task.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge:
# Write a script that simulates downloading 5 files. Each download takes a random time between 1 and 3 seconds.
# Start all downloads concurrently. Print when each finishes, and finally print the total time taken.

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Asyncio is Python's standard library for cooperative multitasking.
# - `async` defines coroutines, and `await` yields control.
# - `asyncio.run()` is used to start the event loop and run the top-level coroutine.
# - It is highly efficient for heavy I/O-bound workloads.

if __name__ == "__main__":
    # asyncio.run is the standard way to run an async main function in Python 3.7+
    print("Running greet:")
    asyncio.run(greet())
    
    print("\nRunning multiple tasks:")
    asyncio.run(main())
    
    print("\nRunning timeout example:")
    asyncio.run(timeout_example())
