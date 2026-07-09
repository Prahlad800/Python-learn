"""
Topic: Finally and Else Clauses
Chapter: 14
Level: Beginner

Description:
    In addition to `try` and `except`, Python provides `else` and `finally` clauses.
    The `else` block runs only if no exception was raised in the `try` block.
    The `finally` block runs no matter what, whether an exception occurred or not.

Real-Life Analogy:
    Imagine baking a cake.
    Try: Baking the cake.
    Except: The cake burns, so you order a pizza.
    Else: The cake is perfect, so you frost it.
    Finally: You clean the kitchen, regardless of whether you baked a cake or ordered pizza.

Key Concepts:
    - else clause
    - finally clause
    - resource cleanup
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_else_finally(success=True):
    try:
        print("Trying an operation...")
        if not success:
            raise ValueError("Something went wrong!")
    except ValueError as e:
        print(f"Except block caught: {e}")
    else:
        # Runs ONLY if NO exception was raised
        print("Else block: Success! No exceptions were raised.")
    finally:
        # Runs ALWAYS
        print("Finally block: Cleaning up resources...\n")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
    else:
        print(f"The division was successful. Result is {result}")
    finally:
        print("Execution of divide_numbers complete.\n")

def read_file_safely(filepath):
    f = None
    try:
        f = open(filepath, 'r')
        content = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    else:
        print(f"File read successfully. Length: {len(content)} characters.")
    finally:
        if f:
            f.close()
            print("File closed safely.")
        print("Finished file operation.\n")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def return_in_finally():
    """
    Demonstrates a tricky behavior: a return statement in a finally block
    overrides any return statement in the try or except blocks!
    """
    try:
        return "Returned from TRY"
    finally:
        return "Returned from FINALLY (Overrides TRY!)"

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Putting code that shouldn't run on failure inside the try block.
# try:
#     result = dangerous_operation()
#     print("Success!") # Should be in else block
# except Exception:
#     print("Failed!")

# Best Practice: Keep the try block as short as possible. Use else for code
# that depends on the try block succeeding.
# try:
#     result = dangerous_operation()
# except Exception:
#     print("Failed!")
# else:
#     print("Success!")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: When does the `else` block execute in a try-except structure?
# A1: The `else` block executes only if the `try` block completes without raising any exceptions.
#
# Q2: When does the `finally` block execute?
# A2: The `finally` block always executes, regardless of whether an exception was raised, caught, or not.
#
# Q3: Why is the `finally` block commonly used?
# A3: It is primarily used for cleaning up resources, such as closing files, network connections, or database connections.
#
# Q4: What happens if there's a `return` statement in both `try` and `finally`?
# A4: The `return` statement in the `finally` block will override the one in the `try` block.
#
# Q5: Can you use `else` without `except`?
# A5: No, an `else` block must be preceded by at least one `except` block.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a function that takes a list and an index, tries to print the element, uses else to print "Element found", and finally to print "Search complete".
# Exercise 2: Open a file, write to it, and ensure it is closed using the finally block.
# Exercise 3: Create a script that raises an error randomly, handling it with try-except-else-finally.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def database_transaction_simulation(should_fail=False):
    """
    Mini Challenge: Simulate a database transaction.
    Try to "commit", except if it fails (simulate with an exception), else print "Transaction successful",
    finally "Close database connection".
    """
    print("--- Database Transaction ---")
    try:
        print("Connecting to database...")
        print("Executing SQL query...")
        if should_fail:
            raise ConnectionError("Database connection lost during execution.")
    except ConnectionError as e:
        print(f"Transaction Failed: {e}")
        print("Rolling back changes...")
    else:
        print("Transaction Successful! Changes committed.")
    finally:
        print("Closing database connection.\n")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - `try`: Code that might cause an error.
# - `except`: Code that runs if an error occurs.
# - `else`: Code that runs if NO error occurs. Keeps try block clean.
# - `finally`: Code that ALWAYS runs, useful for cleanup.

if __name__ == "__main__":
    basic_else_finally(success=True)
    basic_else_finally(success=False)
    
    divide_numbers(10, 2)
    divide_numbers(10, 0)
    
    print(return_in_finally())
    print("\n")
    
    database_transaction_simulation(should_fail=False)
    database_transaction_simulation(should_fail=True)
