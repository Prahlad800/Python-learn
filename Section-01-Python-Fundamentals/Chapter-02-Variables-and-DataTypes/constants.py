"""
Topic: Constants
Chapter: 2
Level: Beginner

Description:
    Unlike some other programming languages (like C++ or Java), Python does not have built-in support for constants.
    A constant is a type of variable whose value cannot be changed. In Python, constants are typically declared and assigned 
    on a module level. The naming convention is to use all capital letters with underscores to indicate that a variable 
    is intended to be a constant and should not be modified.

Real-Life Analogy:
    Think of the speed of light or the value of Pi. These are universally accepted values that do not change. 
    In a recipe, while you might adjust the amount of sugar (a variable), the boiling point of water 
    remains a constant.

Key Concepts:
    - Convention for Naming Constants (ALL_CAPS)
    - Defining constants at the module level
    - Typing with typing.Final (Python 3.8+)
"""

from typing import Final

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# By convention, we use UPPERCASE letters to define a constant.
# Note: Python does NOT enforce this; it's a gentleman's agreement among programmers.
PI: float = 3.14159
GRAVITY: float = 9.81
MAX_USERS = 100

def use_constants() -> None:
    """Demonstrates the usage of constants."""
    print("--- Basic Constants ---")
    print(f"The value of Pi is {PI}")
    print(f"Earth's gravity is {GRAVITY} m/s^2")
    
    # We *can* change them (but we shouldn't!)
    # PI = 3.14 # BAD PRACTICE

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Using typing.Final for better static type checking (Python 3.8+)
# Tools like mypy will flag reassignments to Final variables as errors.
DATABASE_URI: Final[str] = "postgresql://localhost:5432/mydb"
TIMEOUT_SECONDS: Final[int] = 30

def connect_to_db() -> None:
    """Simulates a database connection using constants."""
    print("\n--- Practical Examples ---")
    print(f"Connecting to database at: {DATABASE_URI}")
    print(f"Connection will timeout after {TIMEOUT_SECONDS} seconds.")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Constants in classes
class PhysicsConfig:
    SPEED_OF_LIGHT: Final[int] = 299792458
    PLANCK_CONSTANT: Final[float] = 6.62607015e-34

def advanced_class_constants() -> None:
    """Shows constants grouped in a class structure."""
    print("\n--- Advanced Usage ---")
    print(f"Speed of Light: {PhysicsConfig.SPEED_OF_LIGHT} m/s")
    print(f"Planck Constant: {PhysicsConfig.PLANCK_CONSTANT} J*s")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def best_practices() -> None:
    """Discusses best practices for defining constants."""
    print("\n--- Common Mistakes and Best Practices ---")
    
    # Pitfall: Modifying a variable that is supposed to be constant.
    # Example:
    # MAX_CONNECTIONS = 5
    # MAX_CONNECTIONS = 10  # This defeats the purpose of a constant!
    
    # Best Practice: Always use ALL_CAPS for constants so other developers know not to change them.
    # Best Practice: Group related constants in a separate file (e.g., config.py) for larger projects.
    print("Always use ALL_CAPS for constants to signal immutability to other developers.")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
1. Does Python support true constants?
   Answer: No, Python does not have a native constant type that enforces immutability. It relies on naming conventions (ALL_CAPS) to signify constants.

2. How can you indicate to a static type checker that a variable should not be reassigned?
   Answer: Use typing.Final (introduced in Python 3.8).

3. Where should constants generally be defined in a Python script?
   Answer: At the module level (top of the file, right after imports), or grouped inside a dedicated config class/module.

4. What happens if you reassign a constant in Python?
   Answer: The Python interpreter will allow it, but it violates coding conventions and might cause a static type checker (like mypy) to emit an error if Final is used.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Define a constant for the boiling point of water in Celsius. Write a function that checks if a given temperature has reached the boiling point.
Exercise 2: Create a `MathConstants` class that stores mathematical constants like EULER (2.718) and GOLDEN_RATIO (1.618). Access and print them.
Exercise 3: Import `Final` from `typing` and define a constant `MAX_LOGIN_ATTEMPTS = 3`.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

VAT_RATE: Final[float] = 0.20  # 20% Value Added Tax

def calculate_total_price(net_price: float) -> None:
    """Calculates total price including tax using a constant VAT rate."""
    print("\n--- Mini Challenge ---")
    tax_amount = net_price * VAT_RATE
    total = net_price + tax_amount
    
    print(f"Net Price: ${net_price:.2f}")
    print(f"VAT (20%): ${tax_amount:.2f}")
    print(f"Total:     ${total:.2f}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
Summary:
- Constants are variables whose values shouldn't change.
- Python uses an ALL_CAPS naming convention to denote constants.
- True immutability is not enforced by Python at runtime.
- Use `typing.Final` to enforce constant behavior with static type checkers.
"""

if __name__ == "__main__":
    use_constants()
    connect_to_db()
    advanced_class_constants()
    best_practices()
    calculate_total_price(150.00)
