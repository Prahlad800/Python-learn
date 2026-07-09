"""
Topic: Keywords and Identifiers
Chapter: 01
Level: Beginner

Description:
    Keywords are reserved words in Python that have special meaning to the interpreter 
    (like `if`, `for`, `def`). Identifiers are the names you give to variables, functions, 
    classes, etc. You cannot use a keyword as an identifier.

Real-Life Analogy:
    Keywords are like reserved road signs ("STOP", "YIELD", "ONE WAY"). You can't name your 
    street "STOP Street" without confusing everyone. Identifiers are like the names you give 
    to your pets or cars—you can pick almost anything, as long as it follows some basic rules.

Key Concepts:
    - Reserved words (keywords)
    - Naming rules for identifiers
    - PEP 8 naming conventions
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

import keyword

def list_keywords():
    # Printing a few keywords just to see them
    kw_list = keyword.kwlist
    print(f"Python has {len(kw_list)} keywords. Here are a few:")
    print(kw_list[:5])

# Valid identifiers
user_name = "Alice"
age2 = 30
_internal_value = 10

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def identifier_rules():
    print("Identifier Rules:")
    print("1. Can contain letters, numbers, and underscores (A-z, 0-9, and _).")
    print("2. Cannot start with a number.")
    print("3. Case-sensitive (age, Age, and AGE are different variables).")
    print("4. Cannot be a reserved keyword.")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def checking_identifiers():
    # Python has a built-in string method to check if a string is a valid identifier
    test_str1 = "valid_name1"
    test_str2 = "1invalid"
    
    print(f"Is '{test_str1}' valid? {test_str1.isidentifier()}")
    print(f"Is '{test_str2}' valid? {test_str2.isidentifier()}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistakes:
# - Trying to use a keyword as a variable name: `class = 5` (SyntaxError)
# - Starting a variable with a number: `1st_place = "John"` (SyntaxError)
# - Using built-in function names as variables: `print = 5` (Destroys the print function)

# Best Practices:
# - Use snake_case for variables and functions (e.g., calculate_total).
# - Use CamelCase (PascalCase) for classes (e.g., ShoppingCart).
# - Use descriptive names (`user_age` instead of `ua`).

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is a Python identifier?
# A: A name used to identify a variable, function, class, module, or other object.
#
# Q2: Can an identifier begin with an underscore?
# A: Yes. e.g., `_my_var`. This often conventionally indicates a private or internal variable.
#
# Q3: Are Python identifiers case-sensitive?
# A: Yes. `Variable` and `variable` are two entirely different identifiers.
#
# Q4: How can you check the list of keywords in Python?
# A: By importing the `keyword` module and accessing `keyword.kwlist`.
#
# Q5: What happens if you assign a value to a built-in like `list`?
# A: You shadow the built-in function, meaning you can no longer use `list()` to create a list in that scope.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write down 3 valid identifiers and 3 invalid identifiers.
# Exercise 2: Use the `keyword` module to check if "True" is a keyword.
# Hint: keyword.iskeyword("True")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: Create well-named variables for a shopping cart item.
    """
    item_name = "Laptop"
    item_price = 1200.50
    item_quantity = 2
    is_in_stock = True
    
    print(f"Item: {item_name}, Total: ${item_price * item_quantity}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Keywords are reserved and define the language syntax.
# - Identifiers are names you create.
# - Follow naming rules (no numbers at start, no spaces).
# - Follow naming conventions (snake_case) for readability.

if __name__ == "__main__":
    list_keywords()
    print()
    identifier_rules()
    print()
    checking_identifiers()
    print()
    mini_challenge()
