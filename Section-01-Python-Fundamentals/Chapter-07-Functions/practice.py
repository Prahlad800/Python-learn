"""
Topic: Chapter 7 Practice & Exercises
Chapter: 7
Level: Intermediate

Description:
    This file combines the concepts learned in Chapter 7: Functions, Lambdas, Recursion, Scope, Closures, Higher-Order Functions, Docstrings, and Annotations.

Instructions:
    Implement the functions according to their docstrings and type hints.
"""

from typing import List, Callable, Dict, Optional

# ============================================================
# EXERCISE 1: Type Hints, Docstrings, and Basic Functions
# ============================================================

def filter_strings(items: List[str], min_length: int = 3) -> List[str]:
    """
    Filters a list of strings, returning only those with a length
    greater than or equal to min_length.

    Args:
        items (List[str]): The list of strings to filter.
        min_length (int): The minimum length required. Defaults to 3.

    Returns:
        List[str]: A new list containing the filtered strings.
    """
    return [item for item in items if len(item) >= min_length]

# ============================================================
# EXERCISE 2: Lambda and Higher-Order Functions
# ============================================================

def sort_inventory(inventory: List[Dict[str, float]]) -> List[Dict[str, float]]:
    """
    Sorts a list of inventory items based on their 'price' key in descending order.
    MUST use the `sorted()` function with a lambda function for the `key` argument.
    
    Example input: [{"name": "apple", "price": 1.2}, {"name": "banana", "price": 0.5}]
    """
    return sorted(inventory, key=lambda item: item["price"], reverse=True)

# ============================================================
# EXERCISE 3: Recursion
# ============================================================

def sum_digits(n: int) -> int:
    """
    Recursively sums the digits of a positive integer.
    Example: sum_digits(456) -> 4 + 5 + 6 = 15
    
    Args:
        n (int): A positive integer.
        
    Returns:
        int: The sum of the digits.
    """
    if n < 10:
        return n
    return (n % 10) + sum_digits(n // 10)

# ============================================================
# EXERCISE 4: Closures and State
# ============================================================

def make_password_validator(min_length: int, require_special: bool) -> Callable[[str], bool]:
    """
    Creates a closure that validates passwords.
    
    Args:
        min_length (int): Minimum required length for the password.
        require_special (bool): If True, password must contain at least one of: !@#$%^&*
        
    Returns:
        A function that takes a string password and returns a boolean indicating if it is valid.
    """
    special_chars = "!@#$%^&*"
    
    def validator(password: str) -> bool:
        if len(password) < min_length:
            return False
            
        if require_special:
            has_special = any(char in special_chars for char in password)
            if not has_special:
                return False
                
        return True
        
    return validator

# ============================================================
# EXERCISE 5: Scope
# ============================================================

# Modify the `update_config` function to correctly update the global config variable.
APP_CONFIG = {"debug": False, "version": "1.0"}

def update_config(key: str, value: str | bool) -> None:
    """Updates the global APP_CONFIG dictionary."""
    global APP_CONFIG
    APP_CONFIG[key] = value

# ============================================================
# TESTING BLOCK
# ============================================================

if __name__ == "__main__":
    print("--- Testing Exercise 1 ---")
    words = ["a", "apple", "be", "cat", "dog", "elephant"]
    print(filter_strings(words)) # Expected: ['apple', 'cat', 'dog', 'elephant']

    print("\n--- Testing Exercise 2 ---")
    items = [{"name": "A", "price": 10}, {"name": "B", "price": 50}, {"name": "C", "price": 5}]
    print(sort_inventory(items)) # Expected: B, A, C

    print("\n--- Testing Exercise 3 ---")
    print(sum_digits(12345)) # Expected: 15

    print("\n--- Testing Exercise 4 ---")
    is_valid = make_password_validator(min_length=8, require_special=True)
    print(f"Testing 'short!': {is_valid('short!')}") # Expected: False
    print(f"Testing 'longenough': {is_valid('longenough')}") # Expected: False
    print(f"Testing 'LongEnough!123': {is_valid('LongEnough!123')}") # Expected: True

    print("\n--- Testing Exercise 5 ---")
    update_config("debug", True)
    print(APP_CONFIG) # Expected debug to be True
