"""
Topic: Coroutines
Chapter: 21
Level: Intermediate

Description:
    Coroutines are a generalized form of subroutines (functions). While a normal function has a single entry point and returns once, a coroutine can suspend its execution (yielding control) and be resumed later. They are the building blocks of asyncio.

Real-Life Analogy:
    Think of reading a book. You read a chapter (execute code), put in a bookmark and close the book to do something else (suspend execution), and later open the book at the bookmark to continue reading exactly where you left off (resume).

Key Concepts:
    - Coroutine objects
    - Suspending and resuming execution
    - Awaitables
    - Returning values from coroutines
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================
import asyncio

async def my_coroutine():
    print("Coroutine started.")
    await asyncio.sleep(1)
    print("Coroutine finished.")
    return 42

# Calling `my_coroutine()` does not execute it. It returns a coroutine object.
coro_obj = my_coroutine()
print(f"Object type: {type(coro_obj)}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

async def fetch_data(id: int, delay: float):
    print(f"Fetching data {id}...")
    await asyncio.sleep(delay)
    print(f"Finished fetching data {id}.")
    return {"id": id, "data": f"Sample data {id}"}

async def process_data():
    # You can await a coroutine inside another coroutine
    result1 = await fetch_data(1, 1.5)
    print(f"Processed: {result1}")
    
    result2 = await fetch_data(2, 0.5)
    print(f"Processed: {result2}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Chaining coroutines
async def compute_square(x: int):
    await asyncio.sleep(0.5)
    return x * x

async def compute_cube(x: int):
    await asyncio.sleep(0.5)
    return x * x * x

async def advanced_chaining(val: int):
    # Running them sequentially
    square = await compute_square(val)
    cube = await compute_cube(square) # use result of first
    print(f"Value: {val}, Square: {square}, Cube of square: {cube}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistakes:
# - Forgetting to use `await` in front of a coroutine. It will result in a RuntimeWarning: coroutine was never awaited.
# - Trying to `await` a regular, synchronous function.

# Best Practices:
# - Understand that coroutines are cooperatively scheduled. They must explicitly yield control (e.g., via await).
# - Keep coroutines focused on a single task, just like regular functions.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q: What is a coroutine?
# A: A specialized function that can pause and resume execution, allowing for cooperative multitasking.

# Q: What does calling an `async def` function return?
# A: It returns a coroutine object, not the result of the function.

# Q: How do you actually run a coroutine object?
# A: You must `await` it inside another coroutine, or schedule it on an event loop using methods like `asyncio.run()`, `asyncio.create_task()`, etc.

# Q: Can a coroutine return a value?
# A: Yes, when awaited, it evaluates to the returned value.

# Q: What is an 'awaitable'?
# A: An object that can be used in an `await` expression. Coroutines, Tasks, and Futures are all awaitables.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Create a coroutine that simulates checking a database connection and returns True/False.
# Exercise 2: Create a coroutine that awaits the database connection coroutine, and if True, awaits another coroutine to fetch records.
# Exercise 3: Run the chained coroutines using asyncio.run().

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge:
# Build a simple authentication flow.
# Coroutine 1: `verify_user(username)` - takes 1 second, returns True if username is "admin".
# Coroutine 2: `get_token(username)` - takes 0.5 seconds, returns a random string.
# Main Coroutine: check if user is valid, if so, get token, else print "Access Denied".

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Coroutines pause execution and yield control back to the event loop.
# - They are defined using `async def`.
# - They must be awaited to execute.
# - They allow sequential-looking code to run asynchronously.

if __name__ == "__main__":
    print("Running basic coroutine:")
    asyncio.run(my_coroutine())
    
    print("\nRunning process_data:")
    asyncio.run(process_data())
    
    print("\nRunning advanced chaining:")
    asyncio.run(advanced_chaining(3))
