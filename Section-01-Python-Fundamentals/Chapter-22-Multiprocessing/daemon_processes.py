"""
Topic: Daemon Processes
Chapter: 22
Level: Intermediate

Description:
    A Daemon Process runs in the background. Unlike normal processes, the main program will NOT wait for daemon processes to finish before it exits. Once the main program terminates, all its daemon processes are forcefully killed.

Real-Life Analogy:
    A normal process is a core team member; the office doesn't close until they finish work. A daemon process is the night janitor; if the building gets locked down and closed, they are forced to stop working immediately.

Key Concepts:
    - Daemon Flag
    - Background Tasks
    - Process Termination
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

import multiprocessing
import time
import os

def background_task() -> None:
    """A task meant to run continuously in the background."""
    print(f"Daemon process {os.getpid()} starting.")
    while True:
        print("[Daemon] Doing background maintenance...")
        time.sleep(1)

def standard_task() -> None:
    """A normal task."""
    print(f"Standard process {os.getpid()} starting.")
    time.sleep(3)
    print("Standard process finished.")

def basic_daemon_example() -> None:
    """Demonstrates setting a process as a daemon."""
    daemon_proc = multiprocessing.Process(target=background_task)
    # Set the daemon flag BEFORE starting the process
    daemon_proc.daemon = True 
    
    standard_proc = multiprocessing.Process(target=standard_task)
    
    daemon_proc.start()
    standard_proc.start()
    
    # We do NOT join the daemon process.
    # We only join the standard process.
    standard_proc.join()
    
    print("Main program ending. Daemon process will be killed instantly.")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def heartbeat_monitor(status_dict: dict) -> None:
    """Simulates a background health checker."""
    while True:
        status_dict['last_check'] = time.ctime()
        time.sleep(2)

def daemon_manager_example() -> None:
    """Uses a Manager dict updated by a daemon."""
    with multiprocessing.Manager() as manager:
        shared_status = manager.dict()
        shared_status['status'] = 'Running'
        
        monitor = multiprocessing.Process(target=heartbeat_monitor, args=(shared_status,))
        monitor.daemon = True
        monitor.start()
        
        print("Main process doing primary work...")
        for i in range(3):
            time.sleep(2.5)
            print(f"Main check: Status dict is {shared_status}")
            
        print("Main work done.")
        # When context manager exits, the manager shuts down, killing the daemon.

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def bad_daemon() -> None:
    """A daemon trying to spawn its own children (not allowed)."""
    print("Daemon trying to spawn a child...")
    try:
        child = multiprocessing.Process(target=standard_task)
        child.start()
    except AssertionError as e:
        print(f"Error caught: {e}")

def daemon_children_rule() -> None:
    """Demonstrates that daemons cannot create child processes."""
    p = multiprocessing.Process(target=bad_daemon)
    p.daemon = True
    p.start()
    p.join() # We can join it just to see the error output

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Trying to set `p.daemon = True` after calling `p.start()`.
# Correction: The daemon flag must be set before the process starts.

# Mistake: Daemons modifying files or databases.
# Correction: Since daemons are killed abruptly when the main program ends, they might leave files corrupted or transactions incomplete. Use them only for stateless background tasks (like monitoring or garbage collection).

# Best Practice: Use standard processes with `Event` signals to shut down background tasks gracefully, rather than relying on the harsh termination of daemons if data integrity is important.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: What is a daemon process?
A: A background process that is automatically terminated when the main program finishes executing.

Q2: Can a daemon process create its own child processes?
A: No, Python enforces a rule that daemon processes are not allowed to create child processes. Otherwise, those children could become orphaned when the daemon is killed.

Q3: When should you NOT use a daemon process?
A: When the process is performing operations that need to be closed safely, such as writing to files or interacting with a database, because they are killed abruptly without cleanup.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Create a daemon process that prints the current time every 1 second. Run a main process that sleeps for 5 seconds and then prints "Done". Observe the output.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

"""
Challenge:
Write a main program that simulates downloading a large file (sleep for 5 seconds).
Start a daemon process that acts as a progress bar, printing "." every 0.5 seconds to stdout.
Once the download finishes, the main program exits, and the dots should stop automatically.
"""

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- `p.daemon = True` creates a background process.
- The main program exits without waiting for daemons.
- Daemons are terminated forcefully; avoid using them for stateful I/O.
- Daemons cannot spawn children.
"""

if __name__ == "__main__":
    print("--- Basic Daemon Example ---")
    basic_daemon_example()
    
    print("\n--- Daemon Manager Example ---")
    daemon_manager_example()
    
    print("\n--- Daemon Children Rule ---")
    daemon_children_rule()
