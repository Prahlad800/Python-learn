"""
Topic: Truthiness and Falsiness
Chapter: 5
Level: Intermediate

Description:
    In Python, every object can be evaluated in a boolean context (like an `if` statement). 
    Objects are considered "Truthy" if they evaluate to True, and "Falsy" if they evaluate to False. 
    You do not need to explicitly compare an object to `True` or `False`.

Real-Life Analogy:
    Looking at a bank account. You don't ask "Is the balance exactly equal to zero?" 
    You just ask, "Is there money?" (Truthy = Yes, Falsy = Empty/Zero).

Key Concepts:
    - Falsy Values: None, False, zeros (0, 0.0), and empty sequences/collections ("", [], {}, set()).
    - Truthy Values: Everything else (most objects, non-empty strings, numbers other than 0).
    - Implicit Conversion: Python automatically uses `bool()` in conditions.
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_truthiness_examples():
    print("--- Section 1: Truthiness and Falsiness ---")
    
    # Falsy Values Demo
    falsy_items = [0, 0.0, "", [], {}, set(), None, False]
    
    print("Evaluating Falsy values:")
    for item in falsy_items:
        if not item:
            print(f"  {repr(item)} is Falsy")

    # Truthy Values Demo
    truthy_items = [1, -5, "Hello", [1, 2], {"a": 1}, True]
    
    print("\nEvaluating Truthy values:")
    for item in truthy_items:
        if item:
            print(f"  {repr(item)} is Truthy")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    print("\n--- Section 2: Practical Examples ---")

    # Example 1: Checking for empty strings
    username = ""
    # Instead of: if username == "":
    if not username:
        print("Username is empty! Please enter a name.")

    # Example 2: Checking for empty lists
    shopping_cart = []
    # Instead of: if len(shopping_cart) == 0:
    if not shopping_cart:
        print("Your cart is empty.")
        
    shopping_cart.append("Apple")
    if shopping_cart:
        print("You have items in your cart.")

    # Example 3: Fallback assignments using `or`
    # The `or` operator returns the first Truthy value
    user_input = ""
    default_name = "Guest"
    
    final_name = user_input or default_name
    print(f"Welcome, {final_name}!")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

class CustomObject:
    def __init__(self, value):
        self.value = value
        
    # We can override how our object evaluates in a boolean context
    def __bool__(self):
        return self.value > 0

def advanced_usage():
    print("\n--- Section 3: Advanced Usage (Custom __bool__) ---")
    
    obj1 = CustomObject(5)
    obj2 = CustomObject(0)
    
    if obj1:
        print("obj1 is Truthy (value > 0)")
        
    if not obj2:
        print("obj2 is Falsy (value not > 0)")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Common Mistakes:
# 1. Explicitly checking lengths against 0 (`if len(my_list) == 0:`). It's un-Pythonic.
# 2. Confusing `None` with `False`. While both are Falsy, they are different types. 
#    Sometimes you MUST check `if x is None:` if `0` or `""` are valid, Truthy-like answers in your context.

# Best Practices:
# - Rely on implicit boolean evaluation. Use `if my_list:` instead of `if len(my_list) > 0:`.
# - Use `if var is not None:` ONLY when you specifically need to distinguish `None` from other Falsy values like `0`.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What makes a value "Falsy" in Python?
# A1: A value is Falsy if it evaluates to False in a boolean context. Examples include numeric zeros (0, 0.0), empty sequences/collections ([], "", {}), None, and False.

# Q2: Why is `if my_list:` preferred over `if len(my_list) > 0:`?
# A2: It is more Pythonic, concise, and often slightly faster. It directly utilizes the Truthiness of the object.

# Q3: Is the string `"False"` Truthy or Falsy?
# A3: It is Truthy, because it is a non-empty string.

# Q4: How does the `or` operator work with Truthiness in assignments?
# A4: `a = b or c`. Python evaluates `b`. If `b` is Truthy, `a` becomes `b`. If `b` is Falsy, `a` becomes `c`. It returns the actual objects, not just True/False.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write an if statement relying on truthiness to check if a dictionary `data` has any keys.
# Exercise 2: Given a variable `num = 0`, write logic to print "Zero" if it's Falsy, and "Non-Zero" if it's Truthy.
# Exercise 3: Use the `or` operator to assign the value of `db_result` to `data`, but fallback to an empty list `[]` if `db_result` is None.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    print("\n--- Section 7: Mini Challenge ---")
    # You are processing a user registration form. 
    # Check if the user provided a first_name, last_name, and age.
    # Print an error specifically if a field is Falsy.
    
    form_data = {
        "first_name": "John",
        "last_name": "",
        "age": 0
    }
    
    for field, value in form_data.items():
        if not value:
            print(f"Error: {field} cannot be empty or zero.")
        else:
            print(f"Success: {field} = {value}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Python evaluates any object in a boolean context as Truthy or Falsy.
# - Falsy values include None, zero, and empty collections.
# - Relying on Truthiness makes code more readable and idiomatic (Pythonic).
# - Custom objects can define their truthiness via the `__bool__` or `__len__` methods.

if __name__ == "__main__":
    basic_truthiness_examples()
    practical_examples()
    advanced_usage()
    mini_challenge()
