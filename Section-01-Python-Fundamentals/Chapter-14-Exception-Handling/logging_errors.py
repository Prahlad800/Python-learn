"""
Topic: Logging Errors
Chapter: 14
Level: Intermediate/Advanced

Description:
    While `print()` is useful for quick debugging, production applications use the `logging` module.
    Logging allows you to record errors, warnings, and information to files with timestamps and severity levels.
    When exceptions occur, logging them (especially with tracebacks) is critical for diagnosing issues.

Real-Life Analogy:
    `print()` is like whispering to yourself while working. `logging` is like maintaining an official, timestamped captain's logbook on a ship. If the ship sinks (program crashes), investigators read the logbook to find out why.

Key Concepts:
    - The `logging` module
    - Log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    - logging.exception() for capturing tracebacks
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

import logging

# Basic configuration for logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def basic_logging_example():
    logging.debug("This is a debug message (won't show up with level=INFO).")
    logging.info("System initialized correctly.")
    logging.warning("Disk space is running low.")
    logging.error("Failed to save file.")
    logging.critical("Database connection lost! System shutting down.")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def divide_with_logs(a, b):
    try:
        result = a / b
        logging.info(f"Successfully divided {a} by {b}.")
        return result
    except ZeroDivisionError as e:
        # logging.error logs the message, but NOT the traceback
        logging.error(f"Attempted to divide {a} by zero: {e}")
        return None

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def fetch_data_with_traceback():
    """Using logging.exception() to capture the full stack trace."""
    try:
        # Simulate a deep error
        my_dict = {}
        value = my_dict["missing_key"]
    except KeyError:
        # logging.exception automatically appends the traceback to the log!
        # It should ONLY be called from within an except handler.
        logging.exception("A critical error occurred while fetching data.")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Using print() for error handling in production.
# try:
#     1 / 0
# except Exception as e:
#     print(f"Error: {e}") # This information is lost when the terminal closes.

# Best Practice: Always use logging. Set up a FileHandler to write logs to a file so they persist.
# Best Practice: Use `logging.exception("msg")` instead of `logging.error("msg")` when you want the full traceback included in the log.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: Why use `logging` instead of `print()`?
# A1: `logging` allows you to route messages to different destinations (files, network), include timestamps, filter by severity levels, and format outputs uniformly. `print()` only outputs to stdout.
#
# Q2: What are the 5 standard logging levels in Python?
# A2: DEBUG, INFO, WARNING, ERROR, CRITICAL.
#
# Q3: What is the difference between `logging.error()` and `logging.exception()`?
# A3: `logging.error()` logs an error message. `logging.exception()` logs an error message AND automatically appends the exception traceback to the log. It must be called within an `except` block.
#
# Q4: How do you log to a file instead of the console?
# A4: By configuring `logging.basicConfig(filename='app.log')` or adding a `FileHandler` to a logger instance.
#
# Q5: Can you configure logging to show the module name and line number?
# A5: Yes, by using formatters like `%(module)s` and `%(lineno)d` in the `format` string of `basicConfig`.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Reconfigure the basicConfig to log to a file named 'errors.log'.
# Exercise 2: Write a function that opens a non-existent file and logs the error using `logging.error`.
# Exercise 3: Write a function that triggers an IndexError and logs it using `logging.exception` to see the traceback.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def process_batch(batch):
    """
    Mini Challenge: Iterate over a list of items (batch).
    Convert each item to an integer.
    Log INFO for success, WARNING if a ValueError occurs (and continue), 
    and log EXCEPTION if a TypeError occurs (and abort).
    """
    logging.info("Starting batch processing.")
    for item in batch:
        try:
            num = int(item)
            logging.info(f"Successfully processed {num}")
        except ValueError:
            logging.warning(f"Invalid format, skipping: {item}")
        except TypeError:
            logging.exception(f"Fatal type error encountered with: {item}. Aborting batch.")
            break
    logging.info("Batch processing complete.")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - The `logging` module is essential for production Python code.
# - Levels control verbosity (DEBUG to CRITICAL).
# - Use `logging.error()` for general errors.
# - Use `logging.exception()` inside `except` blocks to capture tracebacks.

if __name__ == "__main__":
    print("--- Basic Logging ---")
    basic_logging_example()
    
    print("\n--- Divide with Logs ---")
    divide_with_logs(10, 2)
    divide_with_logs(10, 0)
    
    print("\n--- Fetch Data with Traceback ---")
    fetch_data_with_traceback()
    
    print("\n--- Process Batch ---")
    process_batch(["10", "20", "invalid", "30", None, "40"])
