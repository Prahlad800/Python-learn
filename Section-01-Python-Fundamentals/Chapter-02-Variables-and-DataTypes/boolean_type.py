"""
Topic: Boolean Type
Chapter: 2
Level: Beginner

Description:
    The Boolean data type represents one of two possible states: True or False. 
    It is heavily used in programming for logic, conditions, and control flow.
    In Python, Booleans are essentially a subclass of integers, where True is 1 and False is 0.

Real-Life Analogy:
    A Boolean is like a light switch. It can only be in one of two states: ON (True) or OFF (False). 
    There is no in-between state.

Key Concepts:
    - True and False keywords
    - Comparison Operators (==, !=, >, <, >=, <=)
    - Logical Operators (and, or, not)
    - Truthiness (Falsy and Truthy values)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_booleans() -> None:
    """Demonstrates basic boolean creation and types."""
    print("--- Basic Booleans ---")
    
    is_active = True
    is_admin = False
    
    print(f"is_active: {is_active} (Type: {type(is_active)})")
    print(f"is_admin: {is_admin}")
    
    # Because bool is a subclass of int:
    print(f"True + True = {True + True}") # Evaluates to 1 + 1 = 2

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def comparison_operators() -> None:
    """Shows how booleans are generated via comparisons."""
    print("\n--- Comparison Operators ---")
    
    a = 10
    b = 20
    
    print(f"{a} == {b} : {a == b}")
    print(f"{a} != {b} : {a != b}")
    print(f"{a} < {b}  : {a < b}")
    print(f"{a} >= {b} : {a >= b}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def logical_operators() -> None:
    """Demonstrates logical combinations of booleans."""
    print("\n--- Logical Operators ---")
    
    has_ticket = True
    is_vip = False
    
    # AND: Both must be True
    print(f"Can enter VIP area (AND): {has_ticket and is_vip}")
    
    # OR: At least one must be True
    print(f"Can enter general area (OR): {has_ticket or is_vip}")
    
    # NOT: Reverses the boolean
    print(f"Is NOT VIP: {not is_vip}")

def truthiness() -> None:
    """Explains how non-boolean values evaluate to True or False."""
    print("\n--- Truthiness ---")
    # Falsy values in Python: 0, 0.0, "", [], (), {}, set(), None, False
    # Everything else is generally Truthy
    
    empty_list = []
    name = "Alice"
    
    print(f"Empty list is Truthy? {bool(empty_list)}")
    print(f"String '{name}' is Truthy? {bool(name)}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes() -> None:
    """Highlights common errors with Booleans."""
    print("\n--- Common Mistakes and Best Practices ---")
    
    # Pitfall: Using 'true' or 'false' (lowercase)
    # python uses capitalized True and False. Lowercase will result in a NameError.
    
    # Pitfall: Comparing boolean to True using ==
    # Bad practice: if is_active == True:
    # Good practice: if is_active:
    is_ready = True
    if is_ready:
        print("System is ready. (Checked without using == True)")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
1. What are the two boolean values in Python?
   Answer: True and False (must be capitalized).

2. Is a boolean an integer in Python?
   Answer: Yes, the bool class is a subclass of the int class. True behaves as 1, and False behaves as 0 in arithmetic contexts.

3. What are "falsy" values in Python?
   Answer: Values that evaluate to False when converted to boolean. Examples include 0, empty strings "", empty lists [], and None.

4. Explain the difference between '==' and 'is'.
   Answer: '==' checks for value equality, while 'is' checks for object identity (whether they point to the exact same location in memory).
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Create a variable `temperature`. Write a boolean expression that evaluates to True if it's between 20 and 30 inclusive.
Exercise 2: Write an expression using `not` and `or` that evaluates to True.
Exercise 3: Test the truthiness of the integer 0, the string "0", and an empty dictionary.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge() -> None:
    """Challenge implementing login logic."""
    print("\n--- Mini Challenge ---")
    
    # User state
    username_entered = "admin"
    password_entered = "secret123"
    account_locked = False
    
    # Database values
    db_user = "admin"
    db_pass = "secret123"
    
    # Logic
    credentials_match = (username_entered == db_user) and (password_entered == db_pass)
    can_login = credentials_match and not account_locked
    
    print(f"Credentials Match: {credentials_match}")
    print(f"Account Locked: {account_locked}")
    print(f"Login Successful: {can_login}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
Summary:
- Booleans represent True or False states.
- They are fundamental for logical operations and control flow.
- Logical operators (and, or, not) combine booleans.
- Understanding "truthiness" allows for concise and Pythonic conditional checks.
"""

if __name__ == "__main__":
    basic_booleans()
    comparison_operators()
    logical_operators()
    truthiness()
    common_mistakes()
    mini_challenge()
