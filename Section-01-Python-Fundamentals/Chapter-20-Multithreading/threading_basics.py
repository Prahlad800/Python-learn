"""
Topic: Threading Basics
Chapter: 20
Level: Beginner

Description:
    Multithreading allows a program to run multiple operations concurrently within the same process space. 
    It is particularly useful for I/O-bound tasks such as downloading files or reading from a database, as it helps prevent the program from blocking.

Real-Life Analogy:
    Imagine a restaurant kitchen. If one chef does everything sequentially (prep, cook, serve), it takes a long time. 
    If multiple chefs work at the same time (one preps, one cooks, one serves), the overall process is much faster.

Key Concepts:
    - Thread Creation
    - Starting and Joining Threads
    - Main Thread vs Child Threads
    - Daemon Threads
"""

import threading
import time

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def simple_task():
    print(f"Task started by {threading.current_thread().name}")
    time.sleep(1)
    print(f"Task finished by {threading.current_thread().name}")

def section_1():
    print("--- Section 1: Basic Syntax ---")
    # Creating a basic thread
    t1 = threading.Thread(target=simple_task, name="WorkerThread-1")
    t1.start()  # Start the thread execution
    t1.join()   # Wait for the thread to finish before moving on
    print("Main thread finished section 1.\n")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def download_file(filename, duration):
    print(f"Downloading {filename}...")
    time.sleep(duration)
    print(f"Finished downloading {filename}!")

def section_2():
    print("--- Section 2: Practical Examples ---")
    files_to_download = [("file1.zip", 1), ("file2.zip", 2), ("file3.zip", 1.5)]
    threads = []
    
    # Start all downloads concurrently
    for file, duration in files_to_download:
        t = threading.Thread(target=download_file, args=(file, duration))
        threads.append(t)
        t.start()
        
    # Wait for all threads to complete
    for t in threads:
        t.join()
        
    print("All downloads completed!\n")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def background_task():
    while True:
        print("Daemon thread running in background...")
        time.sleep(0.5)

def section_3():
    print("--- Section 3: Advanced Usage ---")
    # Daemon threads automatically exit when the main program finishes
    daemon_thread = threading.Thread(target=background_task, daemon=True)
    daemon_thread.start()
    
    time.sleep(1.2)  # Let it run for a bit
    print("Main thread exiting Section 3. Daemon thread will be killed if program ends.\n")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Forgetting to start() a thread or calling the target function directly instead of passing it to target=.
# Wrong: threading.Thread(target=my_func()) <- This executes the function immediately in the main thread!
# Right: threading.Thread(target=my_func)
#
# Best Practice: Always use .join() if your main program needs the results of the threads before continuing.
# Best Practice: Use daemon threads for background tasks like logging or telemetry that shouldn't block shutdown.

def section_4():
    print("--- Section 4: Common Mistakes ---")
    print("Ensure you don't use parenthesis when assigning the target function to a Thread!\n")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# 1. What is a thread in Python?
# A: A thread is the smallest unit of execution within a process. Multiple threads can run concurrently within a single process.
#
# 2. How is multithreading different from multiprocessing?
# A: Multithreading shares the same memory space, while multiprocessing creates separate memory spaces.
#
# 3. What does the join() method do?
# A: It blocks the calling thread (usually the main thread) until the thread whose join() method is called is terminated.
#
# 4. What is a daemon thread?
# A: A daemon thread is a background thread that does not prevent the program from exiting if all non-daemon threads have finished.
#
# 5. Why should you use threads?
# A: To improve performance and responsiveness, especially in I/O bound tasks like network requests or file reading.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Create a function that prints numbers 1 to 5 with a 0.2s delay. Run two instances of this function in separate threads.
# Exercise 2: Modify the above to make one thread a daemon thread, and see what happens if the main thread finishes before the daemon.

def practice_exercises():
    pass

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Create a simple multi-threaded countdown timer.
# It should accept a list of starting times, and count down to 0 concurrently, printing the progress.

def countdown(name, start):
    while start > 0:
        print(f"{name}: {start}")
        time.sleep(0.5)
        start -= 1
    print(f"{name} finished!")

def run_challenge():
    print("--- Section 7: Mini Challenge ---")
    timers = [("Timer A", 3), ("Timer B", 5)]
    threads = []
    for name, start in timers:
        t = threading.Thread(target=countdown, args=(name, start))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
    print("Challenge completed.\n")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Multithreading allows concurrent execution of functions.
# - threading.Thread is the primary class used.
# - Always start() a thread and join() it if you need to wait for its completion.
# - Daemon threads are useful for continuous background tasks.

if __name__ == "__main__":
    section_1()
    section_2()
    section_3()
    section_4()
    run_challenge()
