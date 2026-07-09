"""
Topic: Asyncio Tasks
Chapter: 21
Level: Beginner

Description:
    Tasks are a way to schedule coroutines concurrently. When a coroutine is wrapped into a Task with functions like `asyncio.create_task()`, the coroutine is automatically scheduled to run soon on the event loop.

Real-Life Analogy:
    A coroutine is like a recipe. A Task is like giving that recipe to a chef and telling them, "Please start cooking this as soon as you have a free burner." You can then go do other things and occasionally check on the chef's progress.

Key Concepts:
    - asyncio.create_task()
    - Task objects
    - Concurrency
    - Cancelling tasks
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================
import asyncio
import time

async def make_tea():
    print("Starting tea...")
    await asyncio.sleep(1)
    print("Tea is ready!")
    return "Earl Grey"

async def main_intro():
    # Creating a task schedules it on the event loop immediately
    task = asyncio.create_task(make_tea())
    
    print("Doing other things while tea is brewing...")
    await asyncio.sleep(0.5) # Tea continues brewing in the background
    print("Waiting for tea to finish...")
    
    # Await the task to get its result
    result = await task
    print(f"Got my {result}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

async def fetch_page(url: str):
    print(f"Requesting {url}")
    await asyncio.sleep(1) # Simulate network delay
    print(f"Downloaded {url}")
    return f"Content of {url}"

async def batch_fetch():
    urls = ["site1.com", "site2.com", "site3.com"]
    
    # Create tasks for all URLs
    tasks = [asyncio.create_task(fetch_page(url)) for url in urls]
    
    print("All tasks created and scheduled.")
    
    # We can await them individually...
    # for task in tasks:
    #     await task
        
    # Or use gather to wait for all of them at once
    results = await asyncio.gather(*tasks)
    print(f"All done! Results: {results}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Cancelling tasks
async def long_running_operation():
    try:
        print("Starting long operation...")
        for i in range(10):
            await asyncio.sleep(1)
            print(f"Working... {i}")
    except asyncio.CancelledError:
        print("Operation was cancelled!")
        # Perform cleanup here if needed
        raise # Re-raise is best practice, or at least acknowledge cancellation

async def cancel_example():
    task = asyncio.create_task(long_running_operation())
    
    await asyncio.sleep(3) # Let it run for a bit
    print("Decided to cancel the task.")
    
    task.cancel() # Request cancellation
    
    try:
        await task # Awaiting a cancelled task raises CancelledError in the caller
    except asyncio.CancelledError:
        print("Main caught the cancellation.")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistakes:
# - Awaiting a coroutine directly when you meant to run it concurrently (e.g., `await coro1(); await coro2()` runs sequentially).
# - Creating tasks but never awaiting them or keeping a reference to them (Python's garbage collector might destroy them mid-execution).

# Best Practices:
# - Always keep a reference to background tasks (e.g., in a set) to prevent them from being garbage collected.
# - Handle `asyncio.CancelledError` gracefully if your task holds resources that need cleanup.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q: What is the difference between a coroutine and a Task?
# A: A coroutine is just a generator-like object that defines the async logic. A Task wraps a coroutine and schedules it to run on the event loop.

# Q: Does `asyncio.create_task()` block execution?
# A: No, it returns immediately with a Task object while scheduling the coroutine to run in the background.

# Q: How do you cancel a running task?
# A: By calling the `.cancel()` method on the Task object.

# Q: What exception is raised inside a coroutine when its task is cancelled?
# A: `asyncio.CancelledError`.

# Q: Why should you keep strong references to tasks?
# A: If the only reference to a task is the event loop, the garbage collector might destroy the task before it finishes, leading to silent failures or warnings.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Create a script that starts 5 tasks, each printing a message after a random delay.
# Exercise 2: Modify the cancel_example to catch the CancelledError, print a custom message, and NOT re-raise it. Observe the difference.
# Exercise 3: Use `asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)` to wait for only the fastest task among several.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge:
# Build a "Task Manager". Create a background task that constantly prints a heartbeat every 2 seconds.
# Create another task that waits 7 seconds and then cancels the heartbeat task.
# The main program should wait for everything to conclude gracefully.

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - `asyncio.create_task()` is used to run coroutines concurrently.
# - Tasks can be cancelled using `.cancel()`.
# - Proper cancellation handling requires catching `asyncio.CancelledError`.
# - Always hold references to your created tasks.

if __name__ == "__main__":
    print("Running main_intro:")
    asyncio.run(main_intro())
    
    print("\nRunning batch_fetch:")
    asyncio.run(batch_fetch())
    
    print("\nRunning cancel_example:")
    asyncio.run(cancel_example())
