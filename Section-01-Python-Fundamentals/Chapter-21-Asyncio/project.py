"""Learning file for Asyncio Mini Project."""

# Topic Name: Asyncio Mini Project
# Level: Advanced
# An asyncio mini project combines coroutines, tasks, gather, and structured result handling.
# Read the theory first, then run this file and modify examples.

# Theory
# An asyncio mini project combines coroutines, tasks, gather, and structured result handling.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# async def fetch_user(user_id):
# await asyncio.gather(*tasks)

# Practice Programs
# 1. Create coroutines for fake API calls.
# 2. Run multiple tasks with gather.
# 3. Build a small async status checker.

# Mini Project
# Build a tiny program that uses asyncio mini project
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What is a coroutine?
# A1. A function declared with async def that can pause with await.
# Q2. When is asyncio useful?
# A2. It is useful for many concurrent I/O tasks without creating many threads.

# Examples and practice implementations start below.
import asyncio


async def check_service(name, delay, online=True):
    await asyncio.sleep(delay)
    return {"service": name, "online": online}


async def run_health_check():
    checks = [
        check_service("api", 0.01, True),
        check_service("database", 0.02, True),
        check_service("cache", 0.01, False),
    ]
    return await asyncio.gather(*checks)


def summarize(results):
    online = [item["service"] for item in results if item["online"]]
    offline = [item["service"] for item in results if not item["online"]]
    return {"online": online, "offline": offline}


async def main_async():
    print("--- Asyncio Mini Project ---")
    results = await run_health_check()
    print("Results:", results)
    print("Summary:", summarize(results))


def main():
    asyncio.run(main_async())


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Asyncio Mini Project ---
# Results: [{'service': 'api', 'online': True}, {'service': 'database', 'online': True}, {'service': 'cache', 'online': False}]
# Summary: {'online': ['api', 'database'], 'offline': ['cache']}
# End Expected Output
