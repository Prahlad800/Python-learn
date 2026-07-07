"""Learning file for Thread Locks."""

# Topic Name: Thread Locks
# Level: Advanced
# Locks protect shared data from race conditions when multiple threads update it.
# Read the theory first, then run this file and modify examples.

# Theory
# Locks protect shared data from race conditions when multiple threads update it.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# lock = threading.Lock()
# with lock:
#     shared_data += 1

# Practice Programs
# 1. Run three simulated downloads concurrently.
# 2. Protect a counter with a lock.
# 3. Use a thread pool for independent I/O tasks.

# Mini Project
# Build a tiny program that uses thread locks
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

def example_lock():
    lock = threading.Lock()
    counter = {"value": 0}

    def increment():
        for _ in range(1000):
            with lock:
                counter["value"] += 1

    threads = [threading.Thread(target=increment) for _ in range(3)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("Counter:", counter["value"])


def practice_safe_append(values, item, lock):
    with lock:
        values.append(item)
    return values


def main():
    print("--- Thread Locks ---")
    example_lock()
    print("Append:", practice_safe_append([], "Python", threading.Lock()))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Thread Locks ---
# Counter: 3000
# Append: ['Python']
# End Expected Output
