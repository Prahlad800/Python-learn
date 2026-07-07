"""Learning file for asyncio gather."""

# Topic Name: asyncio gather
# Level: Advanced
# gather runs awaitables concurrently and collects their results in order.
# Read the theory first, then run this file and modify examples.

# Theory
# gather runs awaitables concurrently and collects their results in order.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# results = await asyncio.gather(coro1(), coro2())

# Practice Programs
# 1. Create coroutines for fake API calls.
# 2. Run multiple tasks with gather.
# 3. Build a small async status checker.

# Mini Project
# Build a tiny program that uses asyncio gather
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What is a coroutine?
# A1. A function declared with async def that can pause with await.
# Q2. When is asyncio useful?
# A2. It is useful for many concurrent I/O tasks without creating many threads.

# Examples and practice implementations start below.
import asyncio


async def fetch_score(name, score):
    await asyncio.sleep(0.01)
    return name, score


async def example_gather():
    results = await asyncio.gather(
        fetch_score("Asha", 92),
        fetch_score("Ravi", 85),
        fetch_score("Meera", 98),
    )
    print("Results:", results)


async def practice_total():
    values = await asyncio.gather(fetch_score("A", 10), fetch_score("B", 20))
    return sum(score for _, score in values)


async def main_async():
    print("--- asyncio gather ---")
    await example_gather()
    print("Total:", await practice_total())


def main():
    asyncio.run(main_async())


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- asyncio gather ---
# Results: [('Asha', 92), ('Ravi', 85), ('Meera', 98)]
# Total: 30
# End Expected Output
