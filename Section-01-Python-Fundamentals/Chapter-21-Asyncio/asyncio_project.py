"""
Topic: Asyncio Project
Chapter: 21
Level: Advanced

Description:
    This project combines various asyncio concepts into a practical application: an asynchronous web scraper and link checker. It uses queues for producer/consumer patterns, semaphores for rate limiting, and tasks for concurrency.

Real-Life Analogy:
    Imagine managing a team of website testers. The manager (producer) finds pages to test and puts them in a to-do box (queue). The testers (consumers) grab pages from the box and test them. The manager makes sure no more than 3 testers are working at the exact same time (semaphore) to avoid overloading the office network.

Key Concepts:
    - asyncio.Queue
    - asyncio.Semaphore
    - Producer-Consumer architecture
    - Graceful shutdown
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================
import asyncio
import time
import random

# We will build a pipeline that checks the "health" of a list of URLs.

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

async def check_url(url, semaphore):
    """Simulates an HTTP request to check if a URL is alive."""
    # The semaphore limits how many check_url coroutines can execute this block concurrently
    async with semaphore:
        print(f"Checking {url}...")
        # Simulate network latency
        await asyncio.sleep(random.uniform(0.5, 1.5))
        
        # Simulate a 10% chance of a dead link
        is_alive = random.random() > 0.1
        status = "ALIVE" if is_alive else "DEAD"
        print(f"Result for {url}: {status}")
        return url, is_alive

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

async def producer(queue, urls):
    """Puts URLs into the queue."""
    for url in urls:
        await queue.put(url)
        print(f"Producer added {url} to queue.")
        await asyncio.sleep(0.1) # Simulate time taken to discover URLs

async def consumer(worker_id, queue, semaphore, results):
    """Takes URLs from the queue and checks them."""
    while True:
        try:
            # Wait for an item in the queue. 
            url = await queue.get()
            
            # Process the item
            _, is_alive = await check_url(url, semaphore)
            results[url] = is_alive
            
            # Tell the queue that the item has been processed
            queue.task_done()
        except asyncio.CancelledError:
            # Handle task cancellation gracefully
            break

async def main():
    urls_to_check = [f"http://example.com/page{i}" for i in range(1, 16)]
    
    # 1. Setup
    queue = asyncio.Queue()
    # Limit to 5 concurrent connections to avoid overloading the server
    semaphore = asyncio.Semaphore(5)
    results = {}
    
    # 2. Start the consumer workers
    num_workers = 3
    workers = []
    for i in range(num_workers):
        worker = asyncio.create_task(consumer(i, queue, semaphore, results))
        workers.append(worker)
        
    # 3. Start the producer
    producer_task = asyncio.create_task(producer(queue, urls_to_check))
    
    # 4. Wait for producer to finish adding all items
    await producer_task
    
    # 5. Wait for the queue to be fully processed (all task_done() called)
    await queue.join()
    
    # 6. Shut down workers (since the queue is empty and they are stuck in a while True loop)
    for worker in workers:
        worker.cancel()
        
    # Wait for them to actually cancel
    await asyncio.gather(*workers, return_exceptions=True)
    
    # 7. Print results
    print("\n--- Final Report ---")
    alive_count = sum(1 for v in results.values() if v)
    print(f"Total checked: {len(results)}")
    print(f"Alive: {alive_count}")
    print(f"Dead: {len(results) - alive_count}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistakes:
# - Forgetting `queue.task_done()`. If missed, `queue.join()` will block forever.
# - Creating thousands of tasks without a Semaphore. This can crash the program due to "Too many open files" (socket exhaustion).

# Best Practices:
# - Use `asyncio.Queue` to decouple producers and consumers safely.
# - Always use `asyncio.Semaphore` when making outbound network requests concurrently to be a good netizen and prevent resource exhaustion.
# - Cancel long-running background workers explicitly during shutdown.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q: What is an asyncio.Queue?
# A: It's an asynchronous queue used to pass data between coroutines safely, similar to queue.Queue for threads.

# Q: What does asyncio.Semaphore do?
# A: It manages an internal counter. When a coroutine enters an `async with semaphore:` block, the counter decreases. If it hits zero, other coroutines block until one exits the block and increments the counter. It's used for rate-limiting.

# Q: Why do we need `queue.task_done()` and `queue.join()`?
# A: `task_done()` indicates that a previously enqueued task is complete. `join()` blocks until all items in the queue have been gotten and processed (i.e., `task_done()` has been called for every `put()`).

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Modify the consumer to write dead URLs to a local file asynchronously (you can use a mock async file write function).
# Exercise 2: Change the semaphore limit to 1 and observe how the program executes sequentially.
# Exercise 3: Add a timeout to the `check_url` function using `asyncio.wait_for`.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge:
# Create a pipeline where Producer -> Queue1 -> Processor -> Queue2 -> Saver.
# Producer generates random numbers. Processor squares them. Saver prints them.
# Implement clean shutdown for both Processor and Saver workers.

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Advanced asyncio applications often use the Producer-Consumer pattern.
# - Queues handle communication between tasks safely.
# - Semaphores protect external resources from being overwhelmed.
# - Explicitly cancelling worker tasks is necessary for a clean program exit.

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    print(f"Project completed in {time.time() - start_time:.2f} seconds.")
