"""
Topic: Variables and Data Types Practice 3
Chapter: 2
Level: Beginner

Description:
    This file contains practice exercises focusing on Booleans, logical operators, and the None type.
    It builds foundational logic skills necessary for control flow and conditionally running code.

Real-Life Analogy:
    Like a security checkpoint verifying multiple conditions (ID valid? AND Ticket present? AND NOT blacklisted?).
    If the ticket isn't ready yet, it's marked as 'None' (missing/pending).

Key Concepts:
    - Boolean logic (and, or, not)
    - Truthiness of objects
    - `is None` checks
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def boolean_expressions() -> None:
    """Practice writing complex boolean expressions."""
    print("--- Exercise 1: Boolean Logic ---")
    
    age = 22
    has_license = True
    
    can_rent_car = (age >= 21) and has_license
    print(f"Age {age}, Has License: {has_license}")
    print(f"Can rent car: {can_rent_car}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def truthiness_practice() -> None:
    """Evaluating truthiness of different structures."""
    print("\n--- Exercise 2: Truthiness ---")
    
    cart = []          # Empty list
    username = "Bob"   # Non-empty string
    balance = 0.0      # Zero float
    
    print(f"Cart is active? {bool(cart)}")
    print(f"Username is active? {bool(username)}")
    print(f"Balance is active? {bool(balance)}")
    
    # Practical usage
    if not cart:
        print("Your shopping cart is empty!")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def none_handling() -> None:
    """Practicing the None type for missing data."""
    print("\n--- Exercise 3: Handling None ---")
    
    # Imagine querying a database for a user's phone number
    phone_number = None
    
    # Check if we have the number
    if phone_number is None:
        print("Phone number is missing. Prompting user...")
        # Simulate user providing number
        phone_number = "555-0199"
        
    print(f"Contacting user at: {phone_number}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def short_circuit_evaluation() -> None:
    """Understanding how 'and' / 'or' evaluate left-to-right."""
    print("\n--- Exercise 4: Short Circuiting ---")
    
    def log_and_return_true():
        print("Function executed!")
        return True
        
    # In an 'or' statement, if the first part is True, it doesn't evaluate the second part.
    print("Testing 'True or log_and_return_true()':")
    result = True or log_and_return_true() 
    print(f"Result: {result} (Notice the function did not execute)")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
1. What does the expression `[] and "Hello"` evaluate to?
   Answer: `[]`. The `and` operator returns the first falsy value, or the last value if all are truthy. Since `[]` is falsy, it returns `[]`.

2. What does `None is False` evaluate to?
   Answer: False. None is a distinct type, it is not the boolean False, even though it evaluates to false in an if-statement.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Practice on your own:
1. Create a variable `user_role` set to "guest". Write an expression that evaluates to True if the role is "admin" or "moderator".
2. Create a function that accepts an optional `discount_code`. Set the default to None. If it is not None, print "Discount applied!".
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge() -> None:
    """Feature flag system."""
    print("\n--- Mini Challenge: Feature Flags ---")
    
    is_premium_user = True
    beta_feature_enabled = None # None means the server hasn't responded yet
    
    # We only show the feature if they are premium AND the feature is explicitly enabled (True)
    if beta_feature_enabled is None:
        print("Checking beta status...")
        beta_feature_enabled = False # Server returned false
        
    show_feature = is_premium_user and beta_feature_enabled
    print(f"Display Beta Feature to User: {show_feature}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
Summary:
- Booleans control logic gates in Python.
- Truthiness allows concise checking of empty collections or zero values.
- `None` safely represents missing or uninitialized data.
- Short-circuiting is an optimization trick in Python logical operators.
"""

if __name__ == "__main__":
    boolean_expressions()
    truthiness_practice()
    none_handling()
    short_circuit_evaluation()
    mini_challenge()
