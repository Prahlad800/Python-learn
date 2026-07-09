"""
Topic: Comparison Operators
Chapter: 3
Level: Beginner

Description:
    Comparison operators (also called relational operators) are used to compare two values.
    They always evaluate to a boolean value: True or False.

Real-Life Analogy:
    Imagine checking prices in a store. You compare the price of a shirt ($20) to your budget ($30). Since $20 < $30, the statement "I can afford it" is True.

Key Concepts:
    - Equal to (==)
    - Not equal to (!=)
    - Greater than (>)
    - Less than (<)
    - Greater than or equal to (>=)
    - Less than or equal to (<=)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================
def basic_syntax():
    print("--- Section 1: Basic Syntax ---")
    x = 10
    y = 20

    print(f"x = {x}, y = {y}")
    print(f"x == y (Equal to): {x == y}")
    print(f"x != y (Not equal to): {x != y}")
    print(f"x > y  (Greater than): {x > y}")
    print(f"x < y  (Less than): {x < y}")
    print(f"x >= 10 (Greater than or equal to 10): {x >= 10}")
    print(f"y <= 15 (Less than or equal to 15): {y <= 15}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================
def practical_examples():
    print("\n--- Section 2: Practical Examples ---")
    # Example 1: Checking login credentials
    entered_password = "password123"
    actual_password = "password123"
    is_authenticated = (entered_password == actual_password)
    print(f"Login successful? {is_authenticated}")

    # Example 2: Checking age requirements
    age = 16
    driving_age = 18
    can_drive = (age >= driving_age)
    print(f"Can a {age}-year-old drive? {can_drive}")

    # Example 3: String comparison (Lexicographical/Alphabetical)
    word1 = "apple"
    word2 = "banana"
    print(f"Does '{word1}' come before '{word2}' alphabetically? {word1 < word2}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================
def advanced_usage():
    print("\n--- Section 3: Advanced Usage ---")
    # Chaining comparison operators
    # Python allows chaining to check multiple conditions simultaneously
    score = 85
    # Equivalent to: score >= 80 and score < 90
    is_B_grade = 80 <= score < 90
    print(f"Is {score} a B grade? {is_B_grade}")

    # Comparing different types (Be careful!)
    try:
        print("apple" > 5)
    except TypeError as e:
        print(f"TypeError caught: {e}")

    # Comparing floats (Precision issues)
    # Using math.isclose is safer than == for floats
    import math
    f1 = 0.1 + 0.2
    f2 = 0.3
    print(f"f1 == f2 using ==: {f1 == f2}")
    print(f"f1 == f2 using math.isclose: {math.isclose(f1, f2)}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================
# Common Mistakes:
# 1. Using single `=` (assignment) instead of `==` (comparison).
# 2. Comparing floating-point numbers with `==`.
# 3. Comparing strings of different cases ("Apple" == "apple" is False).
#
# Best Practices:
# 1. Chain comparisons when checking ranges (e.g., `0 < x < 10`).
# 2. Use `.lower()` or `.casefold()` when comparing strings case-insensitively.
# 3. Avoid comparing mixed types (e.g., int and string) in Python 3, as it raises a TypeError.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
# Q1: How does string comparison work in Python?
# A: Strings are compared lexicographically (character by character) using their Unicode/ASCII integer values (e.g., 'a' is 97, 'A' is 65).
#
# Q2: Can you chain comparison operators?
# A: Yes, e.g., `1 < x < 10` is valid and evaluates to `1 < x and x < 10`.
#
# Q3: What happens if you compare an int and a float?
# A: Python will attempt to compare their numeric values. So `5 == 5.0` is True.
#
# Q4: Why is `math.isclose` recommended for float comparisons?
# A: Floating-point arithmetic has tiny precision errors (e.g., 0.1 + 0.2 = 0.30000000000000004), so strict equality often fails.
#
# Q5: Does `None == False` evaluate to True?
# A: No. `None` is a special object of type NoneType, and it does not equal False or 0.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
# 1. Write a program that checks if a user's input string is equal to a secret code, case-insensitively.
# 2. Create a variable `temperature` and use chained comparisons to check if it's between 60 and 80 degrees.
# 3. Write code to test if the length of a list is strictly greater than 5.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================
def mini_challenge():
    print("\n--- Section 7: Mini Challenge ---")
    # Write a simple function that checks the status of a package delivery.
    # It takes current_weight, max_weight, current_volume, and max_volume.
    # It prints True if the package is strictly under BOTH weight and volume limits.
    def is_package_valid(c_weight, m_weight, c_volume, m_volume):
        weight_valid = c_weight < m_weight
        volume_valid = c_volume < m_volume
        return weight_valid and volume_valid

    print(f"Package 1 (10kg, 5L) valid? {is_package_valid(10, 20, 5, 10)}")
    print(f"Package 2 (25kg, 5L) valid? {is_package_valid(25, 20, 5, 10)}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
# - Comparison operators evaluate to booleans (True or False).
# - They include ==, !=, <, >, <=, >=.
# - You can chain them: 1 < x < 5.
# - Be cautious comparing floats and mixed types.

if __name__ == "__main__":
    basic_syntax()
    practical_examples()
    advanced_usage()
    mini_challenge()
