"""Learning file for asyncio Tasks."""

# Topic Name: asyncio Tasks
# Level: Advanced
# Tasks schedule coroutines so they can make progress concurrently.
# Read the theory first, then run this file and modify examples.

# Theory
# Tasks schedule coroutines so they can make progress concurrently.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# task = asyncio.create_task(coro())
# await task

# Practice Programs
# 1. Create coroutines for fake API calls.
# 2. Run multiple tasks with gather.
# 3. Build a small async status checker.

# Mini Project
# Build a tiny program that uses asyncio tasks
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What is a coroutine?
# A1. A function declared with async def that can pause with await.
# Q2. When is asyncio useful?
# A2. It is useful for many concurrent I/O tasks without creating many threads.

# Examples and practice implementations start below.
import asyncio


async def work(name, delay):
    await asyncio.sleep(delay)
    return f"{name} done"


async def example_tasks():
    task_one = asyncio.create_task(work("task-1", 0.02))
    task_two = asyncio.create_task(work("task-2", 0.01))
    print(await task_one)
    print(await task_two)


async def practice_task_result():
    task = asyncio.create_task(work("practice", 0.01))
    return await task


async def main_async():
    print("--- asyncio Tasks ---")
    await example_tasks()
    print("Practice:", await practice_task_result())


def main():
    asyncio.run(main_async())


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- asyncio Tasks ---
# task-1 done
# task-2 done
# Practice: practice done
# End Expected Output
