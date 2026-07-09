"""
Topic: Assertions
Chapter: 14
Level: Intermediate

Description:
    The `assert` statement exists to test conditions that should *never* happen in your code if it's correct.
    It is a debugging aid that tests a condition; if the condition is true, it does nothing. If false, it raises an AssertionError.

Real-Life Analogy:
    An assertion is like a structural safety inspection for a bridge. If the inspector finds a crack (assertion fails), the bridge is immediately closed down (program crashes). It's a preventative measure to stop catastrophic failure later.

Key Concepts:
    - assert statement
    - AssertionError
    - Disabling assertions (-O flag)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Syntax: assert condition, "Optional Error Message"

def calculate_discount(price, discount):
    # The discount should logically never be less than 0 or more than the price
    assert 0 <= discount <= price, "Discount must be between 0 and the price"
    return price - discount

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def process_order(cart):
    # We should not be processing an empty cart
    assert len(cart) > 0, "Cannot process an empty cart."
    print("Processing items:", cart)

def get_first_element(my_list):
    # Developer explicitly asserts that my_list is actually a list
    assert isinstance(my_list, list), "Expected a list object"
    return my_list[0] if my_list else None

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def complex_state_validation(user):
    """Using assertions to validate complex internal states during development."""
    assert "role" in user, "User dictionary is missing 'role' key"
    assert user["role"] in ["admin", "editor", "viewer"], f"Unknown role: {user.get('role')}"
    
    # Process user
    print(f"Processing {user['role']} user.")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Using assertions for data validation or business logic (like user input validation).
# def login(username, password):
#     assert password == "secret", "Invalid password!" # TERRIBLE IDEA

# Why? Because assertions can be globally disabled in Python by running the script with the `-O` (optimize) flag: `python -O script.py`.
# If assertions are disabled, the security check is completely skipped!

# Best Practice: Use exceptions (ValueError, TypeError) for user input validation.
# Use assertions ONLY for checking internal invariants and finding bugs during development.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What does the `assert` statement do?
# A1: It tests a boolean condition. If the condition is False, it raises an `AssertionError`.
#
# Q2: Should you use `assert` to validate user input? Why or why not?
# A2: No. Assertions can be disabled globally at runtime using the `-O` flag. If disabled, validation is bypassed. Use standard exceptions like `ValueError` for input validation.
#
# Q3: What is the syntax for adding an error message to an assertion?
# A3: `assert condition, "Error message here"`
#
# Q4: Can you catch an AssertionError?
# A4: Yes, like any other exception, you can catch it with a `try-except` block, though this is rarely done because assertions represent unrecoverable bugs in logic.
#
# Q5: What is the main purpose of assertions?
# A5: They serve as internal self-checks for developers to catch bugs early by stating "this condition MUST be true at this point in the program".

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write an assertion that checks if a variable `temperature` is above absolute zero (-273.15).
# Exercise 2: Create a function that calculates the area of a rectangle. Add assertions to ensure length and width are positive numbers.
# Exercise 3: Run your script with `python -O script_name.py` and observe what happens to failed assertions.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def apply_promotional_code(user_data, promo_code):
    """
    Mini Challenge: Use assertions to verify the internal state of `user_data` before applying a code.
    Check that user_data is a dictionary, contains 'is_active', and 'is_active' is True.
    """
    assert isinstance(user_data, dict), "user_data must be a dictionary"
    assert "is_active" in user_data, "user_data must contain 'is_active' key"
    assert user_data["is_active"] is True, "User must be active to apply promo codes"
    
    print(f"Applied {promo_code} to user account.")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - `assert` is for internal consistency checks.
# - Raises `AssertionError` if the condition is False.
# - DO NOT use for user input validation, as they can be stripped out by the interpreter (-O flag).
# - Useful for self-documenting code and failing early during development.

if __name__ == "__main__":
    print(f"Discounted price: {calculate_discount(100, 20)}")
    
    try:
        calculate_discount(100, 150) # Will fail assertion
    except AssertionError as e:
        print(f"Assertion Caught: {e}")

    process_order(["apple", "banana"])
    
    user = {"role": "admin"}
    complex_state_validation(user)
    
    active_user = {"is_active": True}
    apply_promotional_code(active_user, "SAVE20")
