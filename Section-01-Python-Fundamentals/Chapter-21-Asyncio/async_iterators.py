"""
Topic: Async Iterators and Generators
Chapter: 21
Level: Intermediate

Description:
    Async iterators and generators allow you to asynchronously iterate over data. They use `async for` instead of `for`. This is incredibly useful when the process of fetching the next item in a sequence involves I/O operations, such as reading lines from a network stream or fetching pages from an API.

Real-Life Analogy:
    Think of a conveyor belt at a sushi restaurant. A standard iterator is a chef placing 10 plates on the belt at once, and you eat them one by one. An async iterator is the chef making one plate, putting it on the belt, and while you eat it, they prepare the next one. You wait (asynchronously) for the next plate to arrive.

Key Concepts:
    - async for
    - __anext__ and __aiter__
    - Async generators (using yield inside async def)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================
import asyncio

# Creating an async generator is the easiest way to make an async iterator.
# Just use `yield` inside an `async def` function.
async def async_counter(limit):
    for i in range(1, limit + 1):
        await asyncio.sleep(0.5) # Simulate asynchronous work to get the next item
        yield i

async def basic_usage():
    print("Starting basic async iteration:")
    # We use `async for` to iterate over an async iterable
    async for number in async_counter(3):
        print(f"Got number: {number}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Simulating paginated API requests
async def fetch_page(page_num):
    await asyncio.sleep(1) # Network delay
    if page_num <= 3:
        return [f"Item {page_num}-A", f"Item {page_num}-B"]
    return [] # Empty list indicates no more pages

async def paginated_api_iterator():
    page = 1
    while True:
        print(f"Fetching page {page}...")
        data = await fetch_page(page)
        if not data:
            break
        for item in data:
            yield item
        page += 1

async def practical_example():
    print("\nStarting paginated API iteration:")
    async for item in paginated_api_iterator():
        print(f"Processed: {item}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Creating an async iterator class manually (less common than generators)
class AsyncTicker:
    def __init__(self, delay, ticks):
        self.delay = delay
        self.ticks = ticks
        self.current = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current >= self.ticks:
            raise StopAsyncIteration # Signals the end of iteration
        
        await asyncio.sleep(self.delay)
        self.current += 1
        return f"Tick {self.current}"

async def class_based_iterator():
    print("\nStarting class-based async iterator:")
    ticker = AsyncTicker(0.3, 4)
    async for tick in ticker:
        print(tick)

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistakes:
# - Using standard `for` loop on an async generator. It will result in a TypeError.
# - Yielding from a synchronous function and expecting it to be an async generator.

# Best Practices:
# - Use async generators (`yield` in `async def`) for most use cases, as they are simpler than writing custom `__aiter__`/`__anext__` classes.
# - Use async comprehensions (e.g., `[x async for x in async_gen()]`) to gather all items if memory permits.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q: How do you consume an async generator?
# A: By using an `async for` loop or an async comprehension inside a coroutine.

# Q: What exception stops an `async for` loop?
# A: `StopAsyncIteration`. (Normal `for` loops use `StopIteration`).

# Q: Can you use `yield` inside an `async def` function?
# A: Yes, this creates an asynchronous generator.

# Q: Can you use `await` inside a regular (synchronous) generator?
# A: No, `await` is only valid inside an `async def` function.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write an async generator that yields random numbers every 0.5 seconds, stopping if the number is greater than 90.
# Exercise 2: Use an async list comprehension to collect the first 5 values from the async_counter generator.
# Exercise 3: Create an async iterator class that reads lines from a mock file (list of strings) with a delay between each line.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge:
# Create an async generator `stream_data()` that yields 10 chunks of data, taking 0.2s each.
# Write a consumer coroutine that uses `async for` to read these chunks, but if a chunk contains the word "ERROR", it breaks the loop early.

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Async iterators produce data asynchronously.
# - They are consumed using `async for`.
# - Async generators are created by using `yield` in an `async def` function.
# - They are ideal for streaming data or handling paginated network requests.

if __name__ == "__main__":
    asyncio.run(basic_usage())
    asyncio.run(practical_example())
    asyncio.run(class_based_iterator())
