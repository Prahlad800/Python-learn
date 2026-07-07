# Topic: asyncio.gather()
# Explanation: gather() runs multiple coroutines concurrently and waits for all of them.

# Syntax:
# import asyncio

async def one():
    return 1

async def two():
    return 2

async def main():
    result = await asyncio.gather(one(), two())
    print(result)

asyncio.run(main())

# Examples:
# import asyncio

async def one():
    return 1

async def two():
    return 2

async def main():
    result = await asyncio.gather(one(), two())
    print(result)

asyncio.run(main())

# Practice Programs:
# 1. Gather two coroutines.
2. Print their results.

# Interview Questions:
# Q: Why use gather()?
A: It runs multiple coroutines concurrently and simplifies waiting.

# Expected Output:
# [1, 2]

import asyncio

async def one():
    return 1

async def two():
    return 2

async def main():
    result = await asyncio.gather(one(), two())
    print(result)

asyncio.run(main())
