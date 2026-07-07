"""Learning file for Thread Pool Executor."""

# Topic Name: Thread Pool Executor
# Level: Advanced
# ThreadPoolExecutor manages a reusable group of worker threads.
# Read the theory first, then run this file and modify examples.

# Theory
# ThreadPoolExecutor manages a reusable group of worker threads.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# with ThreadPoolExecutor(max_workers=3) as executor:
# executor.map(function, items)

# Practice Programs
# 1. Run three simulated downloads concurrently.
# 2. Protect a counter with a lock.
# 3. Use a thread pool for independent I/O tasks.

# Mini Project
# Build a tiny program that uses thread pool executor
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

from concurrent.futures import ThreadPoolExecutor


def fetch_page(page_number):
    return f"page-{page_number}"


def example_thread_pool():
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(fetch_page, [1, 2, 3]))
    print("Results:", results)


def practice_square_all(numbers):
    with ThreadPoolExecutor(max_workers=2) as executor:
        return list(executor.map(lambda number: number ** 2, numbers))


def main():
    print("--- Thread Pool Executor ---")
    example_thread_pool()
    print("Squares:", practice_square_all([1, 2, 3, 4]))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Thread Pool Executor ---
# Results: ['page-1', 'page-2', 'page-3']
# Squares: [1, 4, 9, 16]
# End Expected Output
