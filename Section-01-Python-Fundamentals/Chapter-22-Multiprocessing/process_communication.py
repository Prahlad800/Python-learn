"""
Topic: Process Communication (Queues and Pipes)
Chapter: 22
Level: Intermediate

Description:
    Because processes have independent memory spaces, they cannot easily share variables. Python provides IPC (Inter-Process Communication) mechanisms like Queues and Pipes to send messages and data between processes safely.

Real-Life Analogy:
    Queues are like a conveyor belt in a factory. One worker puts items on the belt (put), and another takes them off (get).
    Pipes are like a telephone line between two specific people. You talk on one end, they listen on the other.

Key Concepts:
    - multiprocessing.Queue
    - multiprocessing.Pipe
    - Producer-Consumer Pattern
    - IPC (Inter-Process Communication)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

import multiprocessing
import time
import os
import queue

def producer_task(q: multiprocessing.Queue) -> None:
    """Produces data and puts it into the queue."""
    for i in range(3):
        item = f"Item-{i}"
        print(f"[Producer PID {os.getpid()}] Creating {item}")
        q.put(item)
        time.sleep(0.5)
    
    # Send a sentinel value to indicate completion
    q.put(None)
    print("[Producer] Finished.")

def consumer_task(q: multiprocessing.Queue) -> None:
    """Consumes data from the queue."""
    while True:
        item = q.get()
        if item is None: # Check for sentinel
            print("[Consumer] Sentinel received. Exiting.")
            break
        print(f"[Consumer PID {os.getpid()}] Processing {item}")
        time.sleep(1)

def queue_example() -> None:
    """Demonstrates basic Queue usage for process communication."""
    # Create a Queue
    q = multiprocessing.Queue()
    
    producer_proc = multiprocessing.Process(target=producer_task, args=(q,))
    consumer_proc = multiprocessing.Process(target=consumer_task, args=(q,))
    
    producer_proc.start()
    consumer_proc.start()
    
    producer_proc.join()
    consumer_proc.join()

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def sender_pipe(conn: multiprocessing.connection.Connection) -> None:
    """Sends messages through a pipe."""
    messages = ["Hello", "How are you?", "Goodbye"]
    for msg in messages:
        print(f"[Sender] Sending: {msg}")
        conn.send(msg)
        time.sleep(0.5)
    conn.close()

def receiver_pipe(conn: multiprocessing.connection.Connection) -> None:
    """Receives messages from a pipe."""
    try:
        while True:
            # recv() blocks until there is data to read
            msg = conn.recv()
            print(f"[Receiver] Received: {msg}")
    except EOFError:
        print("[Receiver] Pipe closed by sender. Exiting.")

def pipe_example() -> None:
    """Demonstrates Pipe for point-to-point communication."""
    # Pipe returns two connection objects (ends of the pipe)
    parent_conn, child_conn = multiprocessing.Pipe()
    
    # We pass one end to the child process, keep the other in the parent
    sender_proc = multiprocessing.Process(target=sender_pipe, args=(child_conn,))
    sender_proc.start()
    
    # Run the receiver in the main process for demonstration
    receiver_pipe(parent_conn)
    
    sender_proc.join()

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def multi_producer_consumer() -> None:
    """Multiple producers and a single consumer using Queue."""
    def fast_producer(q: multiprocessing.Queue, p_id: int):
        for i in range(2):
            q.put(f"Fast Data {i} from Producer {p_id}")
            time.sleep(0.2)
            
    def slow_consumer(q: multiprocessing.Queue):
        # Consume until queue is empty and producers are done
        while True:
            try:
                # get with timeout to avoid blocking forever if producers are done
                data = q.get(timeout=2)
                print(f"[Consumer] Got: {data}")
                time.sleep(0.5)
            except queue.Empty:
                print("[Consumer] Queue empty. Shutting down.")
                break

    q = multiprocessing.Queue()
    producers = [multiprocessing.Process(target=fast_producer, args=(q, i)) for i in range(3)]
    consumer = multiprocessing.Process(target=slow_consumer, args=(q,))
    
    for p in producers:
        p.start()
    consumer.start()
    
    for p in producers:
        p.join()
    consumer.join()

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Using a standard `queue.Queue` for multiprocessing.
# Correction: Standard `queue.Queue` only works for threads. Use `multiprocessing.Queue` for processes.

# Mistake: Forgetting to close pipes.
# Correction: Always close the pipe connections when done to prevent resource leaks and allow the other end to receive an EOFError.

# Best Practice: Use a Sentinel value (like `None` or a special string "DONE") to signal a consumer that the producer has finished generating data.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: What is Inter-Process Communication (IPC)?
A: IPC refers to mechanisms that allow separate processes to share data and synchronize actions, overcoming their isolated memory spaces.

Q2: When would you use a Pipe vs a Queue?
A: A Pipe is best for fast, two-way communication between exactly two processes. A Queue is thread/process-safe and supports multiple producers and multiple consumers, making it better for complex architectures.

Q3: Does reading from an empty `multiprocessing.Queue` block?
A: Yes, by default `q.get()` blocks until an item is available. You can use `q.get(block=False)` or `q.get(timeout=X)` to change this.

Q4: What error is raised when `recv()` is called on a Pipe and the other end is closed?
A: An `EOFError`.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Create a Queue. Have Process A put 5 random numbers into it. Have Process B read the numbers and print their square roots.
Exercise 2: Create a bidirectional Pipe. Process A sends a message. Process B receives it, converts it to uppercase, and sends it back to Process A.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

"""
Challenge: Log Aggregator
Create a `log_queue`. Start 3 worker processes that represent web servers. 
Each worker generates 5 log messages (e.g., "INFO: Request served by Server 1") with random delays and puts them into the queue.
Start 1 logger process that continuously reads from the queue and writes the messages to a text file.
Use a sentinel value from the main process to tell the logger when to stop.
"""

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Processes cannot share standard variables.
- `multiprocessing.Queue` is a FIFO queue safe for multiple processes.
- `multiprocessing.Pipe` offers a connection between two endpoints.
- Sentinels are a robust way to signal completion over IPC.
"""

if __name__ == "__main__":
    print("--- Queue Example ---")
    queue_example()
    
    print("\n--- Pipe Example ---")
    pipe_example()
    
    print("\n--- Multi-Producer Consumer ---")
    multi_producer_consumer()
