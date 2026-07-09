"""
Topic: Default Parameters
Chapter: 7
Level: Intermediate

Description:
    Default parameters allow you to specify a default value for a parameter in a function definition. If the caller does not provide an argument for that parameter, the default value is used.

Real-Life Analogy:
    When you order a burger, the default is to include cheese. If you don't say anything, you get cheese. But if you specifically ask for "no cheese", that overrides the default.

Key Concepts:
    - Defining default values using '='
    - Omitting arguments during function calls
    - The danger of mutable default arguments
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Defining a default value for 'greeting'
def greet(name: str, greeting: str = "Hello") -> None:
    """Greets a person with a default or specified greeting."""
    print(f"{greeting}, {name}!")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Example 1: Creating a user with a default status
def create_user(username: str, role: str = "user", active: bool = True) -> dict:
    """Creates a user dictionary with default role and status."""
    return {
        "username": username,
        "role": role,
        "active": active
    }

# Example 2: Sending an email with default cc/bcc
def send_email(to: str, subject: str, cc: str = "", bcc: str = "") -> str:
    """Simulates sending an email."""
    details = f"Sending to {to} | Subject: {subject}"
    if cc: details += f" | CC: {cc}"
    if bcc: details += f" | BCC: {bcc}"
    return details

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Dealing with the mutable default argument trap
# Advanced workaround using 'None'

def add_item_safe(item: str, target_list: list[str] | None = None) -> list[str]:
    """Safely adds an item to a list without mutable default issues."""
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list

# Using dynamically generated default values (computed at call time)
import time
def log_event(event: str, timestamp: float | None = None) -> None:
    """Logs an event. If timestamp is None, use current time."""
    if timestamp is None:
        timestamp = time.time()
    print(f"[{timestamp}] Event: {event}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# THE MUTABLE DEFAULT ARGUMENT MISTAKE (DO NOT DO THIS)
def add_item_dangerous(item: str, target_list: list = []) -> list:
    # The list is created ONLY ONCE when the function is defined.
    # Subsequent calls without target_list will share the SAME list!
    target_list.append(item)
    return target_list

# Mistake: Putting parameters without defaults AFTER parameters with defaults
# def invalid_func(a=1, b):  # SyntaxError: non-default argument follows default argument
#     pass

# Best Practices:
# 1. ALWAYS use `None` as a default value for mutable objects (lists, dicts, sets),
#    and instantiate them inside the function.
# 2. Keep required parameters first, and optional (default) parameters last.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is a default parameter in Python?
# A: It's a parameter in a function definition that takes a predefined value if no 
#    argument is provided by the caller.

# Q2: Can you place a parameter without a default after one with a default?
# A: No. In Python, all parameters with default values must appear after all 
#    parameters without default values in the function signature.

# Q3: Explain the "mutable default argument" problem.
# A: Default argument expressions are evaluated only once when the function is defined, 
#    not each time it's called. If you use a mutable object like a list or dictionary, 
#    it retains its state between function calls, causing unexpected behavior.

# Q4: How do you fix the mutable default argument problem?
# A: Set the default value to `None`, and inside the function, check if the argument 
#    is `None`. If it is, create a new instance of the mutable object.

# Q5: When is the default value of a parameter evaluated?
# A: It is evaluated exactly once, at function definition time (when the `def` 
#    statement is executed).

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a function `make_coffee` that takes `size` and `sugar` (default 0).
# Return a string describing the coffee.
def make_coffee(size: str, sugar: int = 0) -> str:
    return f"{size} coffee with {sugar} sugars."

# Exercise 2: Create a function `format_name` with `first_name`, `last_name`, and 
# an optional `middle_name` (default empty string).
def format_name(first_name: str, last_name: str, middle_name: str = "") -> str:
    if middle_name:
        return f"{first_name} {middle_name} {last_name}"
    return f"{first_name} {last_name}"

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge: Configuration Builder
# Build a function `build_config` that accepts a filename (required), 
# retries (default 3), timeout (default 30.0), and a dictionary of extra_settings (default None).
# It should return a dictionary combining all these settings.
def build_config(filename: str, retries: int = 3, timeout: float = 30.0, extra_settings: dict | None = None) -> dict:
    config = {
        "filename": filename,
        "retries": retries,
        "timeout": timeout
    }
    if extra_settings is not None:
        config.update(extra_settings)
    return config

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Default parameters make functions more flexible by making some arguments optional.
# - Non-default arguments must precede default arguments.
# - Default values are evaluated once at definition time.
# - Never use mutable default arguments like `[]` or `{}`. Use `None` instead.

if __name__ == "__main__":
    # Calling with and without default parameter
    greet("Alice")
    greet("Bob", "Hi")
    
    print(create_user("charlie99"))
    print(create_user("admin_dave", role="admin"))
    
    # Demonstrating safe vs dangerous mutable defaults
    print("\n--- Mutable Default Danger ---")
    list1 = add_item_dangerous("apple")
    list2 = add_item_dangerous("banana")
    print(f"Dangerous List 1: {list1}") # Expected ['apple'], got ['apple', 'banana']
    
    print("\n--- Safe Mutable Defaults ---")
    safe_list1 = add_item_safe("apple")
    safe_list2 = add_item_safe("banana")
    print(f"Safe List 1: {safe_list1}") # Correct: ['apple']
    print(f"Safe List 2: {safe_list2}") # Correct: ['banana']
    
    # Challenge
    print("\n--- Challenge ---")
    print(build_config("app.yaml"))
    print(build_config("db.json", retries=5, extra_settings={"debug": True}))
