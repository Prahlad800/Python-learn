# Topic: Tasks
# Explanation: Tasks are scheduled coroutines that run concurrently within the event loop.

# Syntax:
# import asyncio

async def worker():
    print("Task running")

async def main():
    task = asyncio.create_task(worker())
    await task

asyncio.run(main())

# Examples:
# import asyncio

async def worker():
    print("Task running")

async def main():
    task = asyncio.create_task(worker())
    await task

asyncio.run(main())

# Practice Programs:
# 1. Create a task and await it.
2. Run multiple tasks.

# Interview Questions:
# Q: What is a task in asyncio?
A: It is a wrapper around a coroutine that can be scheduled.

# Expected Output:
# Task running

import asyncio

async def worker():
    print("Task running")

async def main():
    task = asyncio.create_task(worker())
    await task

asyncio.run(main())
