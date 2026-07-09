"""
Topic: Context Managers (The 'with' statement)
Chapter: 14
Level: Intermediate

Description:
    Context managers provide a clean way to allocate and release resources safely.
    The `with` statement guarantees that clean-up operations (like closing a file or network connection) occur even if exceptions are raised within the block.
    It replaces standard `try...finally` boilerplate.

Real-Life Analogy:
    A context manager is like renting a hotel room.
    Enter: You check in and get the key.
    Body: You stay in the room (do operations).
    Exit: You check out and hand the key back. Even if you get sick during your stay (an exception), hotel rules ensure you are checked out properly eventually.

Key Concepts:
    - The `with` statement
    - Resource acquisition and release
    - __enter__ and __exit__ magic methods
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def traditional_file_handling():
    """Without a context manager, you must use try/finally to ensure the file closes."""
    f = open("temp_test_file.txt", "w")
    try:
        f.write("Hello, World!")
    finally:
        f.close()

def context_manager_handling():
    """With a context manager, __exit__ automatically closes the file."""
    with open("temp_test_file.txt", "w") as f:
        f.write("Hello, Context Manager!")
    # f is automatically closed here, even if f.write() raised an exception!

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

import sqlite3

def database_context_manager():
    """Using 'with' for database connections ensures they are closed automatically."""
    # Create an in-memory SQLite database
    with sqlite3.connect(":memory:") as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE users (id INTEGER, name TEXT)")
        cursor.execute("INSERT INTO users VALUES (1, 'Alice')")
        
        # We can read it back
        cursor.execute("SELECT * FROM users")
        print("Database Row:", cursor.fetchone())
    # Connection is automatically managed!

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# You can create your own custom context managers using classes
class CustomTimer:
    """A custom context manager to measure code execution time."""
    import time
    
    def __enter__(self):
        # Called when entering the 'with' block
        self.start_time = self.time.time()
        return self # The returned object is bound to the 'as' variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Called when exiting the 'with' block, regardless of exceptions
        end_time = self.time.time()
        print(f"Elapsed Time: {end_time - self.start_time:.4f} seconds")
        
        # If we return True here, it suppresses any exceptions that occurred inside the block.
        # Returning False (or None, which is the default) lets the exception propagate.
        return False

def use_custom_timer():
    print("\nTiming a loop:")
    with CustomTimer() as timer:
        total = sum(range(1000000))
    print("Loop finished.")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Forgetting to use 'with' when opening files, leading to file descriptor leaks.
# file = open("data.txt", "r")
# data = file.read()
# # If we forget file.close() or if an error happens, the file remains locked!

# Best Practice: Use `with` for files, locks, database connections, and any resource that requires explicit setup and teardown phases.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is the main benefit of the `with` statement?
# A1: It guarantees that resources are properly cleaned up (like closing files) regardless of whether an exception occurs in the block.
#
# Q2: Which two magic methods must an object implement to be used as a context manager?
# A2: `__enter__()` and `__exit__()`.
#
# Q3: What happens to an exception if `__exit__()` returns `True`?
# A3: The exception is suppressed (swallowed), and execution continues after the `with` block.
#
# Q4: What does the `as` keyword do in a `with` statement?
# A4: It assigns the value returned by the `__enter__()` method to a specific variable for use inside the block.
#
# Q5: Can you manage multiple resources in a single `with` statement?
# A5: Yes. e.g., `with open('a.txt') as a, open('b.txt') as b:`

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Open two files using a single `with` statement, reading from one and writing to the other.
# Exercise 2: Create a custom class-based context manager `SilentErrorHandler` that suppresses `ValueError` but lets other exceptions propagate.
# Exercise 3: Research the `contextlib` module and see how `@contextmanager` decorators can create context managers from generator functions.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

class SafeFileEditor:
    """
    Mini Challenge: Create a context manager that safely edits a file.
    It writes to a temporary file first. If no exceptions occur, it renames the temp file to the target file.
    If an exception occurs, it deletes the temp file and leaves the original file untouched.
    """
    import os
    
    def __init__(self, filename):
        self.filename = filename
        self.temp_filename = filename + ".tmp"
        self.file_obj = None

    def __enter__(self):
        self.file_obj = open(self.temp_filename, "w")
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()
        if exc_type is None:
            # Success! Replace original file with temporary file
            self.os.replace(self.temp_filename, self.filename)
            print(f"Successfully saved to {self.filename}")
        else:
            # Failure! Clean up temporary file
            if self.os.path.exists(self.temp_filename):
                self.os.remove(self.temp_filename)
            print(f"Error occurred. Changes discarded. {exc_type.__name__}")
        return False # Propagate exception

def test_safe_editor():
    print("\n--- Testing SafeFileEditor ---")
    try:
        with SafeFileEditor("important_data.txt") as f:
            f.write("This is critical data.\n")
            # Simulate a crash before finishing
            raise RuntimeError("System crash simulated!")
    except RuntimeError:
        pass
    import os
    # The temp file should be gone, and important_data.txt shouldn't exist because it crashed
    print("Does original exist?", os.path.exists("important_data.txt"))
    print("Does temp exist?", os.path.exists("important_data.txt.tmp"))

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Context managers (`with` statement) safely handle resource allocation/release.
# - They implement `__enter__` and `__exit__`.
# - They replace verbose `try...finally` blocks.
# - Returning `True` from `__exit__` suppresses exceptions.

if __name__ == "__main__":
    traditional_file_handling()
    context_manager_handling()
    database_context_manager()
    use_custom_timer()
    test_safe_editor()
    
    # Cleanup temp test file
    import os
    if os.path.exists("temp_test_file.txt"):
        os.remove("temp_test_file.txt")
