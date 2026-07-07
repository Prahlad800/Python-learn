"""Learning file for async and await."""

# Topic Name: async and await
# Level: Advanced
# async defines coroutines and await pauses them until awaited work is ready.
# Read the theory first, then run this file and modify examples.

# Theory
# async defines coroutines and await pauses them until awaited work is ready.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# async def fetch():
#     await operation()

# Practice Programs
# 1. Create coroutines for fake API calls.
# 2. Run multiple tasks with gather.
# 3. Build a small async status checker.

# Mini Project
# Build a tiny program that uses async and await
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What is a coroutine?
# A1. A function declared with async def that can pause with await.
# Q2. When is asyncio useful?
# A2. It is useful for many concurrent I/O tasks without creating many threads.

# Examples and practice implementations start below.
import asyncio


async def fetch_user(user_id):
    await asyncio.sleep(0.01)
    return {"id": user_id, "name": "Asha"}


async def example_async_await():
    user = await fetch_user(1)
    print("User:", user)


async def practice_upper(text):
    await asyncio.sleep(0.01)
    return text.upper()


async def main_async():
    print("--- async and await ---")
    await example_async_await()
    print("Upper:", await practice_upper("python"))


def main():
    asyncio.run(main_async())


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- async and await ---
# User: {'id': 1, 'name': 'Asha'}
# Upper: PYTHON
# End Expected Output
