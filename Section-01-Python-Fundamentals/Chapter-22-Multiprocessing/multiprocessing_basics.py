"""
Topic: Multiprocessing Basics
Chapter: 22
Level: Beginner

Description:
    Multiprocessing allows a program to run multiple processes simultaneously, each with its own memory space and Python interpreter (bypassing the Global Interpreter Lock, or GIL). This is ideal for CPU-bound tasks.

Real-Life Analogy:
    Think of a restaurant kitchen. Instead of one chef trying to cook everything (multithreading), you have multiple kitchens, each with its own chef, cooking different dishes simultaneously.

Key Concepts:
    - Process Creation
    - Starting and Joining Processes
    - Process IDs (PID)
    - Multiprocessing Module
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

import multiprocessing
import os
import time

def worker_task(name: str) -> None:
    """A simple worker function that prints its process ID."""
    print(f"Worker '{name}' starting in process: {os.getpid()}")
    time.sleep(1)
    print(f"Worker '{name}' finishing.")

def basic_multiprocessing() -> None:
    """Demonstrates how to create and start multiple processes."""
    print(f"Main process ID: {os.getpid()}")
    
    # Create process objects
    p1 = multiprocessing.Process(target=worker_task, args=("Alpha",))
    p2 = multiprocessing.Process(target=worker_task, args=("Beta",))
    
    # Start the processes
    p1.start()
    p2.start()
    
    # Wait for the processes to complete
    p1.join()
    p2.join()
    
    print("Main process finished basic multiprocessing.")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def calculate_square(numbers: list[int]) -> None:
    """Calculates the square of numbers and prints them."""
    for n in numbers:
        time.sleep(0.1) # Simulate computation
        print(f"Square of {n} is {n * n} (PID: {os.getpid()})")

def calculate_cube(numbers: list[int]) -> None:
    """Calculates the cube of numbers and prints them."""
    for n in numbers:
        time.sleep(0.1) # Simulate computation
        print(f"Cube of {n} is {n * n * n} (PID: {os.getpid()})")

def practical_math_example() -> None:
    """Run two CPU-bound tasks in parallel."""
    numbers = [1, 2, 3, 4, 5]
    
    start_time = time.time()
    
    p1 = multiprocessing.Process(target=calculate_square, args=(numbers,))
    p2 = multiprocessing.Process(target=calculate_cube, args=(numbers,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    end_time = time.time()
    print(f"Practical example took {end_time - start_time:.2f} seconds.")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

class CustomProcess(multiprocessing.Process):
    """Subclassing multiprocessing.Process to create custom workers."""
    
    def __init__(self, name: str, iterations: int):
        super().__init__()
        self.process_name = name
        self.iterations = iterations
        
    def run(self) -> None:
        """This method is executed when the process starts."""
        print(f"CustomProcess '{self.process_name}' (PID {os.getpid()}) started.")
        for i in range(self.iterations):
            print(f"[{self.process_name}] Working on iteration {i+1}...")
            time.sleep(0.2)
        print(f"CustomProcess '{self.process_name}' finished.")

def subclassing_example() -> None:
    """Demonstrates using custom Process classes."""
    proc1 = CustomProcess("WorkerA", 3)
    proc2 = CustomProcess("WorkerB", 3)
    
    proc1.start()
    proc2.start()
    
    proc1.join()
    proc2.join()

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Not using the `if __name__ == '__main__':` block.
# Correction: On Windows, creating a process imports the script. If the creation is not shielded, it causes an infinite recursive loop of process creations.

# Mistake 2: Thinking variables are shared by default.
# Correction: Each process has its own memory space. Global variables modified in a child process will NOT affect the parent process.

# Best Practice: Always `join()` your processes to clean up resources and ensure they finish before the main program exits.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: What is the main difference between multithreading and multiprocessing in Python?
A: Multithreading runs threads in the same memory space but is limited by the GIL (Global Interpreter Lock), making it only good for I/O bound tasks. Multiprocessing creates separate memory spaces and processes, bypassing the GIL, making it ideal for CPU-bound tasks.

Q2: Why is the `if __name__ == '__main__':` block mandatory in Python multiprocessing on Windows?
A: Windows lacks the `fork` system call, so it uses `spawn` instead. `spawn` imports the main module to create a new process. Without the block, it would recursively execute the process creation code indefinitely.

Q3: Do global variables retain changes made in a child process?
A: No, because each process has its own memory address space.

Q4: What method is used to wait for a process to finish?
A: The `.join()` method.

Q5: What is a zombie process?
A: A process that has finished execution but still has an entry in the process table because its parent hasn't called `join()` to read its exit status.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Create a program that spawns 3 processes. Each process should count down from 5 to 1, printing its PID and the countdown number, pausing for 0.5s between counts.
Exercise 2: Write a class `DownloadProcess` that inherits from `multiprocessing.Process` and simulates downloading a file by sleeping for a random amount of time.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

"""
Challenge:
Write a script that creates a list of URLs (mock them as strings). 
Use multiprocessing to spawn 4 processes. Divide the URLs among the processes. 
Each process should "fetch" the URL by printing a message and sleeping for 1 second.
"""

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Multiprocessing runs tasks in truly separate parallel processes.
- Excellent for CPU-bound tasks (math, data processing).
- Each process has its own memory; no shared state by default.
- You must use `if __name__ == "__main__":` to safely spawn processes on Windows.
- Subclassing `multiprocessing.Process` provides an OOP way to define workers.
"""

if __name__ == "__main__":
    print("--- Basic Multiprocessing ---")
    basic_multiprocessing()
    
    print("\n--- Practical Math Example ---")
    practical_math_example()
    
    print("\n--- Subclassing Example ---")
    subclassing_example()
