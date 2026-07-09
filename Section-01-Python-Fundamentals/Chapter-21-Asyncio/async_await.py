"""
Topic: Async and Await Keywords
Chapter: 21
Level: Beginner

Description:
    The `async` and `await` keywords are the foundation of modern asynchronous programming in Python. `async` declares that a function is a coroutine, and `await` is used to pause the execution of that coroutine until a specified awaitable completes.

Real-Life Analogy:
    Imagine giving a presentation. `async` is the badge that says you are a presenter. `await` is when you ask the audience a question and pause your presentation, waiting for someone to answer before you continue speaking.

Key Concepts:
    - async def
    - await expressions
    - Awaitable objects (Coroutines, Tasks, Futures)
    - Execution flow
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================
import asyncio

# The 'async' keyword turns a regular function into a coroutine function.
async def simple_greeter():
    print("Hello")
    # The 'await' keyword pauses simple_greeter until asyncio.sleep finishes.
    # Control is handed back to the event loop.
    await asyncio.sleep(1)
    print("World")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

async def fetch_user(user_id):
    print(f"Fetching user {user_id} from database...")
    await asyncio.sleep(0.5) # Simulate DB lookup
    return {"id": user_id, "name": f"User_{user_id}"}

async def fetch_user_posts(user_id):
    print(f"Fetching posts for user {user_id}...")
    await asyncio.sleep(0.8) # Simulate DB lookup
    return ["Post 1", "Post 2"]

async def display_user_dashboard(user_id):
    # We must await the results because they are async functions
    user = await fetch_user(user_id)
    posts = await fetch_user_posts(user_id)
    
    print(f"\nDashboard for {user['name']}:")
    for post in posts:
        print(f"- {post}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# You can only use 'await' inside an 'async def' block.
# However, you can create helper classes with `__await__` methods to make custom objects awaitable.

class Delay:
    def __init__(self, seconds):
        self.seconds = seconds
        
    def __await__(self):
        # We delegate the actual waiting to asyncio.sleep
        return asyncio.sleep(self.seconds).__await__()

async def custom_awaitable_demo():
    print("Wait for it...")
    await Delay(2) # Using our custom awaitable
    print("Done!")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistakes:
# - Using `await` outside of an `async` function (SyntaxError).
# - Forgetting `await` when calling a coroutine. It returns a coroutine object instead of executing, causing silent failures.
# - Awaiting a synchronous function (TypeError: object NoneType can't be used in 'await' expression).

# Best Practices:
# - Prefix async functions with `async_` if it helps your team distinguish them from sync functions, though IDEs usually highlight them.
# - Ensure that any function performing I/O is asynchronous if you are writing an async application.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q: What happens exactly when Python encounters the `await` keyword?
# A: The current coroutine suspends its execution. Control is yielded back to the event loop, which will run other tasks until the awaited object is resolved.

# Q: What is an "awaitable"?
# A: Any object that can be used in an `await` expression. The main types are Coroutines, Tasks, and Futures.

# Q: Can you use `await` in a regular Python shell (REPL)?
# A: Yes, starting from Python 3.8, the standard REPL supports top-level `await` using `python -m asyncio`.

# Q: What does a coroutine function return when called without `await`?
# A: It returns a coroutine object.

# Q: Can an `async` function contain zero `await` statements?
# A: Yes, but it will execute synchronously and completely block the event loop until it finishes. It defeats the purpose of async.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write an async function that accepts a string, awaits 1 second, and returns the reversed string.
# Exercise 2: Call the function from Exercise 1 without `await` and print the result. What do you see?
# Exercise 3: Fix Exercise 2 by properly awaiting the function.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge:
# Create a sequence of 3 async functions:
# A: returns 5 after 1 second.
# B: takes a number, adds 10 after 1 second.
# C: takes a number, multiplies by 2 after 1 second.
# Write a main function that chains them together (A -> B -> C) using `await` and prints the final result.

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - `async` marks a function as a coroutine.
# - `await` suspends execution until the awaitable is complete.
# - They must be used together; `await` is only valid inside `async def`.
# - They enable writing asynchronous code that looks and behaves like synchronous code.

if __name__ == "__main__":
    print("Running simple_greeter:")
    asyncio.run(simple_greeter())
    
    print("\nRunning display_user_dashboard:")
    asyncio.run(display_user_dashboard(101))
    
    print("\nRunning custom_awaitable_demo:")
    asyncio.run(custom_awaitable_demo())
