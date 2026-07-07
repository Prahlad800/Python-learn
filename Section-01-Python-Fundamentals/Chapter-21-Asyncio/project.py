# Topic: Asyncio Mini Project
# Explanation: Create a small asynchronous project with multiple tasks.

# Syntax:
# import asyncio

async def task(name):
    await asyncio.sleep(0.1)
    return f"Done {name}"

async def main():
    results = await asyncio.gather(task("A"), task("B"))
    print(results)

asyncio.run(main())

# Examples:
# import asyncio

async def task(name):
    await asyncio.sleep(0.1)
    return f"Done {name}"

async def main():
    results = await asyncio.gather(task("A"), task("B"))
    print(results)

asyncio.run(main())

# Practice Programs:
# 1. Create three async tasks.
2. Gather them and print the results.

# Interview Questions:
# Q: How does asyncio help in real projects?
A: It improves efficiency for network and I/O-heavy applications.

# Expected Output:
# ['Done A', 'Done B']

import asyncio

async def task(name):
    await asyncio.sleep(0.1)
    return f"Done {name}"

async def main():
    results = await asyncio.gather(task("A"), task("B"))
    print(results)

asyncio.run(main())
