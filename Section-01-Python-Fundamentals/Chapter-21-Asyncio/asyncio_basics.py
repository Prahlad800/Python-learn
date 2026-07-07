"""Learning file for asyncio Basics."""

# Topic Name: asyncio Basics
# Level: Advanced
# asyncio runs concurrent I/O tasks on a single-threaded event loop.
# Read the theory first, then run this file and modify examples.

# Theory
# asyncio runs concurrent I/O tasks on a single-threaded event loop.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# asyncio.run(main())
# await asyncio.sleep(1)

# Practice Programs
# 1. Create coroutines for fake API calls.
# 2. Run multiple tasks with gather.
# 3. Build a small async status checker.

# Mini Project
# Build a tiny program that uses asyncio basics
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What is a coroutine?
# A1. A function declared with async def that can pause with await.
# Q2. When is asyncio useful?
# A2. It is useful for many concurrent I/O tasks without creating many threads.

# Examples and practice implementations start below.
import asyncio


async def say_after(delay, message):
    await asyncio.sleep(delay)
    return message


async def example_asyncio():
    result = await say_after(0.01, "hello async")
    print(result)


async def practice_status():
    await asyncio.sleep(0.01)
    return "ready"


async def main_async():
    print("--- asyncio Basics ---")
    await example_asyncio()
    print("Status:", await practice_status())


def main():
    asyncio.run(main_async())


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- asyncio Basics ---
# hello async
# Status: ready
# End Expected Output
