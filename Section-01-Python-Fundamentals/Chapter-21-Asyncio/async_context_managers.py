"""
Topic: Async Context Managers
Chapter: 21
Level: Intermediate

Description:
    Async context managers allow you to manage resources asynchronously. They use `async with` instead of `with`. They are implemented using `__aenter__` and `__aexit__` magic methods, which are coroutines themselves.

Real-Life Analogy:
    Think of renting a hotel room. `__aenter__` is the check-in process where the receptionist (asynchronously) verifies your booking and hands you the keys. `__aexit__` is the check-out process where they (asynchronously) inspect the room and process your payment. You stay in the room (execute code block) in between.

Key Concepts:
    - async with
    - __aenter__ and __aexit__
    - Managing async resources (e.g., database connections, network sessions)
    - contextlib.asynccontextmanager
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================
import asyncio

class AsyncConnection:
    def __init__(self, host):
        self.host = host
        
    async def __aenter__(self):
        print(f"Connecting to {self.host}...")
        await asyncio.sleep(1) # Simulate network delay
        print("Connected!")
        return self # Often returns an object to be used in the `as` clause
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Disconnecting...")
        await asyncio.sleep(0.5)
        print("Disconnected!")
        # If an exception occurred, we can handle it here or let it propagate

    async def fetch_data(self):
        await asyncio.sleep(0.5)
        return f"Data from {self.host}"

async def use_connection():
    # The 'async with' statement manages the async setup and teardown
    async with AsyncConnection("db.example.com") as conn:
        data = await conn.fetch_data()
        print(f"Received: {data}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

import time
from contextlib import asynccontextmanager

# Using the asynccontextmanager decorator (easier than writing a class)
@asynccontextmanager
async def async_timer(label):
    start = time.time()
    try:
        yield # This is where the body of the 'async with' block executes
    finally:
        end = time.time()
        print(f"{label} took {end - start:.4f} seconds")

async def timed_task():
    async with async_timer("Network Request"):
        await asyncio.sleep(1.2)

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Handling exceptions within an async context manager
class SafeAsyncResource:
    async def __aenter__(self):
        print("Acquiring safe resource...")
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Releasing safe resource...")
        if exc_type is not None:
            print(f"Handled exception: {exc_type.__name__}: {exc_val}")
            return True # Suppress the exception (prevents it from propagating)
        return False

async def error_handling_demo():
    async with SafeAsyncResource():
        print("Working with resource...")
        raise ValueError("Something went wrong!")
    print("Execution continues normally because exception was suppressed.")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistakes:
# - Using standard `with` for an object that only supports `async with` (AttributeError on __enter__).
# - Doing blocking synchronous operations inside `__aenter__` or `__aexit__`.

# Best Practices:
# - Use async context managers for all async resources that need explicit cleanup (sessions, sockets, db pools).
# - Use `@asynccontextmanager` from `contextlib` for simple cases to avoid writing boilerplate classes.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q: What is the difference between `with` and `async with`?
# A: `with` calls `__enter__` and `__exit__` synchronously. `async with` awaits `__aenter__` and `__aexit__`, allowing setup and teardown to perform asynchronous I/O.

# Q: Can you use an async context manager inside a regular synchronous function?
# A: No, `async with` requires the `await` keyword conceptually, so it must be used inside an `async def` function.

# Q: What does `@asynccontextmanager` do?
# A: It's a decorator that transforms an async generator function into an async context manager, yielding control to the `async with` block at the `yield` statement.

# Q: How do you suppress exceptions in an async context manager?
# A: By returning `True` from the `__aexit__` method.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Create an async context manager class that simulates acquiring and releasing a lock.
# Exercise 2: Use `@asynccontextmanager` to create a context manager that temporarily sets a global variable to a specific value and restores it afterwards.
# Exercise 3: Write an `async with` block that raises a `KeyError` and observe how a normal `__aexit__` handles it (if it doesn't return True).

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge:
# Simulate an HTTP Session manager.
# Create an async context manager `MockSession` that prints "Session started" and "Session closed".
# It should yield an object with an async method `get(url)`.
# In the main function, use `async with MockSession() as session:` to fetch 3 URLs sequentially.

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Async context managers handle setup and teardown of asynchronous resources.
# - They use the `async with` syntax.
# - Implemented via `__aenter__` and `__aexit__` coroutines.
# - `contextlib.asynccontextmanager` provides a simplified way to create them using generators.

if __name__ == "__main__":
    print("Running use_connection:")
    asyncio.run(use_connection())
    
    print("\nRunning timed_task:")
    asyncio.run(timed_task())
    
    print("\nRunning error_handling_demo:")
    asyncio.run(error_handling_demo())
