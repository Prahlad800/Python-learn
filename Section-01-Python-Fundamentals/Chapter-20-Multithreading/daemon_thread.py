"""Learning file for Daemon Threads."""

# Topic Name: Daemon Threads
# Level: Advanced
# Daemon threads run in the background and do not keep the process alive.
# Read the theory first, then run this file and modify examples.

# Theory
# Daemon threads run in the background and do not keep the process alive.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# thread.daemon = True
# threading.Thread(target=work, daemon=True)

# Practice Programs
# 1. Run three simulated downloads concurrently.
# 2. Protect a counter with a lock.
# 3. Use a thread pool for independent I/O tasks.

# Mini Project
# Build a tiny program that uses daemon threads
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


def background_logger(events):
    time.sleep(0.01)
    events.append("background completed")


def example_daemon_thread():
    events = []
    thread = threading.Thread(target=background_logger, args=(events,), daemon=True)
    thread.start()
    thread.join(timeout=0.05)
    print("Events:", events)
    print("Daemon:", thread.daemon)


def practice_make_daemon(target):
    thread = threading.Thread(target=target, daemon=True)
    return thread.daemon


def main():
    print("--- Daemon Threads ---")
    example_daemon_thread()
    print("Practice daemon:", practice_make_daemon(lambda: None))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Daemon Threads ---
# Events: ['background completed']
# Daemon: True
# Practice daemon: True
# End Expected Output
