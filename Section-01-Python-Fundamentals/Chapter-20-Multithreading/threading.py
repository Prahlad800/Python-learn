"""Learning file for Threading Basics."""

# Topic Name: Threading Basics
# Level: Advanced
# Threads run multiple tasks concurrently inside one process, often for I/O-bound work.
# Read the theory first, then run this file and modify examples.

# Theory
# Threads run multiple tasks concurrently inside one process, often for I/O-bound work.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# thread = threading.Thread(target=work)
# thread.start()
# thread.join()

# Practice Programs
# 1. Run three simulated downloads concurrently.
# 2. Protect a counter with a lock.
# 3. Use a thread pool for independent I/O tasks.

# Mini Project
# Build a tiny program that uses threading basics
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. When are threads useful in Python?
# A1. They are useful for I/O-bound tasks such as downloads and file operations.
# Q2. Why are locks needed?
# A2. Locks prevent race conditions when threads share mutable data.

# Examples and practice implementations start below.
import importlib.util
import sys
import sysconfig
from pathlib import Path


def load_standard_threading():
    """Load stdlib threading even though this chapter has threading.py."""
    loaded = sys.modules.get("threading")
    loaded_file = str(getattr(loaded, "__file__", "")) if loaded else ""
    if loaded and "Chapter-20-Multithreading" not in loaded_file:
        return loaded

    threading_path = Path(sysconfig.get_path("stdlib")) / "threading.py"
    spec = importlib.util.spec_from_file_location("threading", threading_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["threading"] = module
    spec.loader.exec_module(module)
    return module


threading = load_standard_threading()

import time


def worker(name, delay):
    time.sleep(delay)
    print(f"{name} finished")


def example_threads():
    threads = [
        threading.Thread(target=worker, args=("download-1", 0.01)),
        threading.Thread(target=worker, args=("download-2", 0.02)),
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def practice_thread_names():
    return [threading.Thread(name=f"worker-{index}").name for index in range(1, 4)]


def main():
    print("--- Threading Basics ---")
    example_threads()
    print("Names:", practice_thread_names())


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Threading Basics ---
# download-1 finished
# download-2 finished
# Names: ['worker-1', 'worker-2', 'worker-3']
# End Expected Output
