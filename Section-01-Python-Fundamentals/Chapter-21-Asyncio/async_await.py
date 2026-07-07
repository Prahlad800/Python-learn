# Topic: async and await
# Explanation: async defines a coroutine and await pauses it until another coroutine completes.

# Syntax:
# import asyncio

async def greet():
    print("Hello")
    await asyncio.sleep(0)
    print("World")

asyncio.run(greet())

# Examples:
# import asyncio

async def greet():
    print("Hello")
    await asyncio.sleep(0)
    print("World")

asyncio.run(greet())

# Practice Programs:
# 1. Create two coroutines and await them.
2. Print messages in sequence.

# Interview Questions:
# Q: What does await do?
A: It suspends execution until the awaited coroutine finishes.

# Expected Output:
# Hello
World

import asyncio

async def greet():
    print("Hello")
    await asyncio.sleep(0)
    print("World")

asyncio.run(greet())
