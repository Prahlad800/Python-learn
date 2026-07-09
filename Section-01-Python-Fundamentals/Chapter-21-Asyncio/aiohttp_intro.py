"""
Topic: Aiohttp Introduction
Chapter: 21
Level: Intermediate

Description:
    `aiohttp` is an asynchronous HTTP client/server framework for asyncio. While the standard `requests` library is synchronous and blocks the event loop, `aiohttp` allows you to make hundreds of HTTP requests concurrently without blocking.

Real-Life Analogy:
    Using `requests` is like placing a phone call to order pizza, staying on the line until it's delivered, and then calling the next place. Using `aiohttp` is like sending 10 text messages to 10 different pizza places and handling the deliveries as they arrive.

Key Concepts:
    - ClientSession
    - Asynchronous HTTP GET/POST requests
    - Handling JSON responses
    - Concurrency with aiohttp
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================
import asyncio
import time
import json

# Note: You need to install aiohttp to run this script:
# pip install aiohttp

# We'll mock aiohttp if it's not installed for demonstration purposes,
# but in a real environment, you'd import it.
try:
    import aiohttp
    HAS_AIOHTTP = True
except ImportError:
    HAS_AIOHTTP = False
    print("aiohttp not installed. Running in mock mode.")

# Mocking for the sake of making the file executable without dependencies
class MockResponse:
    def __init__(self, url):
        self.url = url
        self.status = 200
    async def __aenter__(self): return self
    async def __aexit__(self, *args): pass
    async def json(self):
        await asyncio.sleep(0.5)
        return {"url": self.url, "data": "Mock data"}
    async def text(self):
        await asyncio.sleep(0.5)
        return f"Mock text from {self.url}"

class MockSession:
    async def __aenter__(self): return self
    async def __aexit__(self, *args): pass
    def get(self, url): return MockResponse(url)

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

async def fetch_single_url():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    
    # In real code: async with aiohttp.ClientSession() as session:
    SessionClass = aiohttp.ClientSession if HAS_AIOHTTP else MockSession
    
    async with SessionClass() as session:
        print(f"Fetching {url}...")
        async with session.get(url) as response:
            data = await response.json()
            print(f"Status: {response.status}")
            print(f"Data: {data}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Fetching multiple URLs concurrently
async def fetch_multiple_urls():
    urls = [
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/todos/2",
        "https://jsonplaceholder.typicode.com/todos/3"
    ]
    
    SessionClass = aiohttp.ClientSession if HAS_AIOHTTP else MockSession
    
    async with SessionClass() as session:
        # Create a list of tasks
        tasks = []
        for url in urls:
            # We define an inline coroutine function to handle the response
            async def fetch(u):
                async with session.get(u) as resp:
                    return await resp.json()
            
            tasks.append(asyncio.create_task(fetch(url)))
        
        # Run them all concurrently
        start_time = time.time()
        results = await asyncio.gather(*tasks)
        end_time = time.time()
        
        print(f"\nFetched {len(results)} URLs in {end_time - start_time:.2f} seconds.")
        for res in results:
            # Safely print a snippet
            print(str(res)[:50] + "...")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistakes:
# - Creating a new `ClientSession` for every single request. This is highly inefficient.
# - Using the `requests` library inside an `async def` function without `run_in_executor`.

# Best Practices:
# - Create a single `ClientSession` and share it across all requests in your application.
# - Use `async with` for both the session and the response to ensure resources (connections) are properly released.
# - Implement concurrency limits (using `asyncio.Semaphore`) if making thousands of requests to avoid overwhelming the server or your OS file descriptors.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q: Why use `aiohttp` instead of `requests` in an asyncio application?
# A: `requests` is synchronous and blocks the event loop. `aiohttp` is asynchronous, allowing the event loop to run other tasks while waiting for HTTP responses.

# Q: What is the purpose of `ClientSession` in `aiohttp`?
# A: It maintains a pool of connections (keep-alive) and keeps track of cookies, making multiple requests to the same host much faster and more efficient.

# Q: How do you parse a JSON response in `aiohttp`?
# A: By using `await response.json()`. Note the `await`, as reading the body and parsing it is an asynchronous operation.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write an aiohttp script that fetches 5 different pokemon from the PokeAPI (https://pokeapi.co/api/v2/pokemon/{id}).
# Exercise 2: Add an `asyncio.Semaphore` to the previous exercise to ensure no more than 2 concurrent requests are made at a time.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge:
# Build an async web scraper. Given a list of 10 dummy URLs, fetch them all concurrently.
# If a request fails or times out (simulate this randomly if mocking), catch the exception and log "Failed", 
# while allowing the other requests to complete successfully.

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - `aiohttp` is the go-to library for async HTTP in Python.
# - It uses `async with` for sessions and responses.
# - A single `ClientSession` should be reused for multiple requests.
# - Combined with `asyncio.gather`, it enables massive concurrency for web scraping and API consumption.

if __name__ == "__main__":
    print("Running single fetch:")
    asyncio.run(fetch_single_url())
    
    print("\nRunning concurrent fetch:")
    asyncio.run(fetch_multiple_urls())
