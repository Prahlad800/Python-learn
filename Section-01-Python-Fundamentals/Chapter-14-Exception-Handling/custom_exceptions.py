"""
Topic: Custom Exceptions
Chapter: 14
Level: Intermediate

Description:
    While Python provides many built-in exceptions, complex applications often require custom error types.
    You can create your own exception classes by inheriting from Python's built-in `Exception` class.

Real-Life Analogy:
    A hospital has a general "Emergency Code" (built-in Exception). But they also create custom codes like "Code Blue" (Cardiac Arrest) or "Code Red" (Fire) to provide more specific, context-aware alerts.

Key Concepts:
    - Inheriting from Exception
    - Naming conventions
    - Adding custom attributes to exceptions
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Creating a basic custom exception
class ValueTooHighError(Exception):
    """Raised when an input value is unacceptably high."""
    pass

def check_value(val):
    if val > 100:
        raise ValueTooHighError(f"Value {val} is too high! Max is 100.")
    print(f"Value {val} is acceptable.")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Creating a custom exception with extra attributes for better debugging
class InsufficientFundsError(Exception):
    """Raised when a user tries to withdraw more than their balance."""
    
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        self.message = f"Cannot withdraw ${amount}. Current balance is only ${balance}."
        super().__init__(self.message)

def withdraw(amount, balance):
    if amount > balance:
        raise InsufficientFundsError(amount, balance)
    return balance - amount

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Creating a Base Class for a specific module or package
class PaymentError(Exception):
    """Base class for all payment-related errors."""
    pass

class ExpiredCardError(PaymentError):
    """Raised when a credit card is expired."""
    pass

class FraudDetectedError(PaymentError):
    """Raised when a transaction looks suspicious."""
    pass

def process_payment(status):
    if status == "expired":
        raise ExpiredCardError("The credit card provided has expired.")
    elif status == "fraud":
        raise FraudDetectedError("Fraudulent activity detected! Transaction blocked.")
    else:
        print("Payment processed successfully.")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Inheriting from BaseException instead of Exception
# class BadError(BaseException): pass  # Bad practice

# Best Practice:
# 1. Always inherit from Exception or its subclasses.
# 2. Name your custom exceptions with the suffix "Error" (e.g., TimeoutError).
# 3. Provide clear docstrings explaining when the error is raised.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: How do you create a custom exception in Python?
# A1: By creating a class that inherits from the built-in `Exception` class or one of its subclasses.
#
# Q2: Why should custom exceptions inherit from `Exception` and not `BaseException`?
# A2: `BaseException` includes system-exiting signals. Catching it broadly might prevent scripts from exiting correctly. `Exception` is strictly for application-level errors.
#
# Q3: Can custom exceptions have their own methods and attributes?
# A3: Yes. Since they are standard Python classes, you can define an `__init__` method to accept specific arguments, store them, and format custom error messages.
#
# Q4: Why create a base custom exception for a package (e.g., `MyPackageError`)?
# A4: It allows users of your package to easily catch all errors specific to your library with a single `except MyPackageError:` block.
#
# Q5: What is the naming convention for custom exceptions?
# A5: They should typically end with the word "Error", mirroring built-in exceptions like `ValueError` or `TypeError`.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Create an `InvalidEmailError` exception and a function that raises it if an email doesn't contain an '@' symbol.
# Exercise 2: Create a hierarchy of errors for a game: `GameError` -> `GameOverError` and `InvalidMoveError`.
# Exercise 3: Add a custom attribute `attempt_number` to an `AuthenticationError`.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

class UserAgeError(Exception):
    """Base exception for age validation."""
    pass

class TooYoungError(UserAgeError):
    def __init__(self, age, required_age=18):
        super().__init__(f"User is {age}. Must be at least {required_age}.")

class TooOldError(UserAgeError):
    def __init__(self, age, max_age=120):
        super().__init__(f"User is {age}. Must be younger than {max_age}.")

def register_user(name, age):
    """Mini Challenge: Register a user with strict age requirements using custom exceptions."""
    try:
        if age < 18:
            raise TooYoungError(age)
        if age > 120:
            raise TooOldError(age)
        print(f"User '{name}' registered successfully.")
    except UserAgeError as e:
        print(f"Registration failed for '{name}': {e}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Custom exceptions make code more readable and self-documenting.
# - Inherit from `Exception`.
# - Use the `Error` suffix.
# - Add custom attributes via `__init__` to carry context about the failure.

if __name__ == "__main__":
    try:
        check_value(150)
    except ValueTooHighError as e:
        print(f"Caught custom error: {e}")

    try:
        withdraw(500, 100)
    except InsufficientFundsError as e:
        print(f"Transaction failed: {e.message} (Tried to withdraw {e.amount})")

    try:
        process_payment("fraud")
    except PaymentError as e:
        print(f"Payment system error: {e}")

    print("\n--- Mini Challenge ---")
    register_user("Alice", 25)
    register_user("Bob", 15)
    register_user("Charlie", 150)
