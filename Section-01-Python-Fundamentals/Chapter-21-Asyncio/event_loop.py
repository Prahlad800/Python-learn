"""
Topic: Event Loop
Chapter: 21
Level: Intermediate

Description:
    The event loop is the core of every asyncio application. It runs asynchronous tasks and callbacks, performs network IO operations, and manages subprocesses. It is the maestro coordinating all the coroutines.

Real-Life Analogy:
    Imagine a traffic controller at a busy intersection. The controller (event loop) decides which cars (coroutines) get to go and which must wait. When a car has to stop for a pedestrian (I/O wait), the controller signals another car to move, ensuring continuous flow.

Key Concepts:
    - Event loop lifecycle
    - asyncio.run() vs manual loop management
    - Scheduling callbacks
    - Getting the running loop
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================
import asyncio
import time

async def simple_task():
    print("Simple task running")
    await asyncio.sleep(0.5)
    print("Simple task done")

# Historically (before Python 3.7), you had to manage the loop manually:
# loop = asyncio.get_event_loop()
# try:
#     loop.run_until_complete(simple_task())
# finally:
#     loop.close()

# Now, `asyncio.run()` abstracts this away:
# asyncio.run(simple_task())

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def sync_callback():
    print("Sync callback executed!")

async def loop_interaction():
    # Getting the current running loop
    loop = asyncio.get_running_loop()
    
    # You can schedule synchronous functions to run on the next iteration of the loop
    loop.call_soon(sync_callback)
    
    # Or schedule them with a delay
    loop.call_later(1.0, lambda: print("Delayed callback executed!"))
    
    print("Main coroutine continues...")
    await asyncio.sleep(2) # Give callbacks time to execute
    print("Main coroutine finished.")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Running blocking code in the event loop (avoiding freezing it)
import concurrent.futures

def blocking_io():
    print(f"Blocking I/O started... (simulating file read/write)")
    time.sleep(1.5) # A real blocking operation!
    print(f"Blocking I/O finished.")
    return "File contents"

async def async_wrapper():
    loop = asyncio.get_running_loop()
    
    print("Starting wrapper.")
    # Run the blocking function in a separate thread pool so the loop isn't blocked
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, blocking_io)
    
    print(f"Got result: {result}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistakes:
# - Running blocking operations (like requests.get() or time.sleep()) directly in an async function, which freezes the entire event loop.
# - Calling `asyncio.run()` from inside an already running event loop (e.g., inside an async function).

# Best Practices:
# - Always use `run_in_executor` for unavoidable blocking sync code.
# - Keep the event loop clean. Don't run long CPU-bound tasks directly on it.
# - Use `asyncio.run(main())` exactly once in your script.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q: What is the event loop?
# A: An endless loop that checks for and dispatches events or messages in a program. In asyncio, it manages the execution of coroutines and I/O operations.

# Q: How do you get the currently running event loop?
# A: By using `asyncio.get_running_loop()` inside a coroutine.

# Q: Can you have multiple event loops running in the same thread?
# A: No, you can only have one running event loop per thread.

# Q: What happens if a coroutine blocks the thread?
# A: The event loop is blocked. No other coroutines can run, and the application becomes unresponsive.

# Q: How do you integrate a blocking third-party library into an asyncio app?
# A: By running it in a separate thread or process using `loop.run_in_executor()`.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Use `call_soon` to schedule 5 different print statements. Observe the order of execution relative to an awaited sleep.
# Exercise 2: Write a CPU-intensive synchronous function (e.g., calculating Fibonacci). Use `run_in_executor` with a ProcessPoolExecutor to run it without blocking.
# Exercise 3: Try to call asyncio.run() inside an async function and observe the RuntimeError.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge:
# Create an async program that simulates a web server handling requests.
# Most requests are fast (asyncio.sleep(0.1)), but some require heavy processing (time.sleep(1.0)).
# Ensure the heavy processing requests don't block the fast ones by using executors.

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - The event loop manages coroutines and I/O.
# - `asyncio.run()` is the preferred way to start the loop.
# - Synchronous, blocking code must be delegated to executors to avoid halting the loop.
# - Callbacks can be scheduled directly onto the loop using `call_soon` or `call_later`.

if __name__ == "__main__":
    print("Running simple task:")
    asyncio.run(simple_task())
    
    print("\nRunning loop interaction:")
    asyncio.run(loop_interaction())
    
    print("\nRunning async wrapper with executor:")
    asyncio.run(async_wrapper())
