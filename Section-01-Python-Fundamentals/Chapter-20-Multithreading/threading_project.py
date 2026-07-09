"""
Topic: Multithreading Project
Chapter: 20
Level: Advanced

Description:
    This project demonstrates the practical application of multithreading in Python. It simulates a data scraping and processing pipeline where multiple threads work cooperatively to fetch and parse data efficiently.

Real-Life Analogy:
    Imagine a news agency where several reporters (threads) are out in the field gathering stories concurrently. They all send their raw notes back to an editor who compiles them into a single newspaper, significantly reducing the total time required compared to having just one reporter.

Key Concepts:
    - Thread Pools
    - Thread synchronization using Queues
    - Producer-Consumer Pattern
    - Handling thread termination gracefully
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================
import threading
import time
import random
import queue

# We will build a producer-consumer model where producer threads fetch mock data,
# and consumer threads process it. This is a common pattern in I/O bound tasks.

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

class DataFetcher(threading.Thread):
    def __init__(self, thread_id, data_queue, url_list):
        super().__init__()
        self.thread_id = thread_id
        self.data_queue = data_queue
        self.url_list = url_list
        self.daemon = True # Daemon thread ends when main thread ends

    def run(self):
        print(f"Fetcher-{self.thread_id} starting.")
        for url in self.url_list:
            time.sleep(random.uniform(0.1, 0.5)) # Simulate network delay
            data = f"Data from {url}"
            self.data_queue.put(data)
            print(f"Fetcher-{self.thread_id} fetched: {url}")
        print(f"Fetcher-{self.thread_id} finished.")

class DataProcessor(threading.Thread):
    def __init__(self, thread_id, data_queue, result_list, lock):
        super().__init__()
        self.thread_id = thread_id
        self.data_queue = data_queue
        self.result_list = result_list
        self.lock = lock
        self.daemon = True

    def run(self):
        print(f"Processor-{self.thread_id} starting.")
        while True:
            try:
                # Wait for data for a short time
                data = self.data_queue.get(timeout=2)
                time.sleep(random.uniform(0.1, 0.3)) # Simulate processing
                processed_data = data.upper()
                
                with self.lock:
                    self.result_list.append(processed_data)
                
                self.data_queue.task_done()
                print(f"Processor-{self.thread_id} processed data.")
            except queue.Empty:
                # Break the loop if queue is empty for too long
                print(f"Processor-{self.thread_id} timed out waiting for data.")
                break

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def run_pipeline():
    urls = [f"http://example.com/page{i}" for i in range(1, 11)]
    data_queue = queue.Queue()
    result_list = []
    lock = threading.Lock()

    # Split URLs between two fetchers
    fetcher1 = DataFetcher(1, data_queue, urls[:5])
    fetcher2 = DataFetcher(2, data_queue, urls[5:])

    # Create multiple processors
    processors = [DataProcessor(i, data_queue, result_list, lock) for i in range(1, 4)]

    # Start all threads
    fetcher1.start()
    fetcher2.start()
    for p in processors:
        p.start()

    # Wait for fetchers to finish
    fetcher1.join()
    fetcher2.join()

    # Wait for the queue to be empty (all tasks processed)
    data_queue.join()

    print("\nPipeline complete. Results:")
    for res in result_list:
        print(res)

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistakes:
# - Forgetting to call `task_done()` on a queue when using `queue.join()`, causing a deadlock.
# - Using busy waiting (`while True: pass`) instead of blocking calls or timeouts.

# Best Practices:
# - Use `queue.Queue` for thread-safe communication.
# - Use daemon threads for background tasks that shouldn't block program exit.
# - Always protect shared mutable state with locks.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q: What is the producer-consumer pattern?
# A: It's a design pattern where one or more threads produce data and place it in a queue, while other threads consume that data.

# Q: Why use queue.Queue instead of a standard list for thread communication?
# A: queue.Queue is thread-safe, meaning it internally handles locks to prevent race conditions during put and get operations.

# Q: What happens if you don't call task_done() after processing a queue item?
# A: If you call queue.join(), it will block indefinitely, causing a deadlock, because it waits for all put items to have a corresponding task_done() call.

# Q: How do daemon threads differ from regular threads?
# A: The Python program exits when all non-daemon threads have completed. Daemon threads are abruptly stopped when the program exits.

# Q: Can multithreading speed up CPU-bound tasks in Python?
# A: Generally no, due to the Global Interpreter Lock (GIL). Multiprocessing is better for CPU-bound tasks.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Modify the DataFetcher to occasionally raise an exception, and handle it gracefully.
# Exercise 2: Add a mechanism to shut down the processors immediately instead of waiting for a timeout.
# Exercise 3: Use concurrent.futures.ThreadPoolExecutor instead of manual threading.Thread for the same task.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge:
# Build a log analyzer. One thread reads log entries from a mock list (producer), 
# and multiple threads (consumers) check if the log entry contains "ERROR". 
# They should write any errors to a shared list safely.

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Multithreading is powerful for I/O bound pipelines.
# - Queues provide a robust, thread-safe way to pass data between producers and consumers.
# - Joining threads and queues ensures the main program waits for work to complete.
# - Thread synchronization and shared resource management require careful attention.

if __name__ == "__main__":
    print("Starting Multithreading Project...")
    run_pipeline()
