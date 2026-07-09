"""
Topic: Ternary Expressions (Conditional Expressions)
Chapter: 5
Level: Intermediate

Description:
    A ternary expression (or conditional expression) allows you to write a simple `if-else` statement 
    in a single line. It is highly useful for concisely assigning values to variables based on a condition.

Real-Life Analogy:
    "I will wear a jacket if it's cold, otherwise a t-shirt." 
    Instead of full sentences, you just say: "Jacket if cold, else t-shirt."

Key Concepts:
    - One-Liner: Condenses an `if-else` block into a single expression.
    - Evaluation Order: `value_if_true if condition else value_if_false`.
    - Returns a Value: Unlike an `if` statement, a ternary expression evaluates to a value that can be assigned or returned.
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_ternary_examples():
    print("--- Section 1: Basic Ternary Expressions ---")
    
    # Syntax: 
    # variable = [value_if_true] if [condition] else [value_if_false]

    # Example 1: Standard if-else vs Ternary
    
    # Traditional way:
    age = 20
    if age >= 18:
        status = "Adult"
    else:
        status = "Minor"
        
    # Ternary way:
    status_ternary = "Adult" if age >= 18 else "Minor"
    
    print(f"Traditional: {status} | Ternary: {status_ternary}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    print("\n--- Section 2: Practical Examples ---")

    # Example 1: Formatting text based on quantity (pluralization)
    items_count = 1
    label = "item" if items_count == 1 else "items"
    print(f"You have {items_count} {label} in your cart.")
    
    items_count = 5
    label = "item" if items_count == 1 else "items"
    print(f"You have {items_count} {label} in your cart.")

    # Example 2: Default values or fallbacks
    user_input = ""
    # Use user_input if it's truthy, otherwise use "Guest"
    username = user_input if user_input else "Guest"
    print(f"Welcome, {username}!")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    print("\n--- Section 3: Advanced Usage ---")

    # Example 1: Nested Ternary Operators (Use with caution!)
    # While possible, they can be hard to read.
    score = 85
    # Translates to: If score >= 90 'A', else if score >= 80 'B', else 'C'
    grade = "A" if score >= 90 else ("B" if score >= 80 else "C")
    print(f"Score {score} yields grade {grade}")

    # Example 2: Using ternary inside a list comprehension or lambda
    numbers = [1, 2, 3, 4, 5]
    # Replace odd numbers with 0
    modified = [x if x % 2 == 0 else 0 for x in numbers]
    print(f"Modified list: {modified}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Common Mistakes:
# 1. Overusing nested ternary operators, which destroys code readability.
# 2. Using ternary expressions for complex logic or when you need to execute multiple statements.

# Best Practices:
# - Use ternary expressions solely for simple assignments and short conditional returns.
# - If the expression spans multiple lines or becomes hard to read, revert to a standard `if-else` block.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is a ternary operator in Python?
# A1: It is a one-line conditional expression that evaluates a condition and returns one of two values. 
#     Syntax: `x if condition else y`.

# Q2: Can a ternary expression omit the `else` clause?
# A2: No. A ternary expression MUST have both an `if` and an `else` part because it must guarantee a return value.

# Q3: How is a ternary expression fundamentally different from an `if` statement?
# A3: An `if` statement is a control flow structure that dictates execution. A ternary expression is an expression that evaluates to a single value.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a ternary expression that assigns "Even" or "Odd" to a variable based on a number.
# Exercise 2: Given a variable `is_logged_in`, use a ternary expression to print "Dashboard" if True, else "Login Page".
# Exercise 3: Use a ternary expression to find the maximum of two variables `a` and `b`.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    print("\n--- Section 7: Mini Challenge ---")
    # Write a script that checks a battery percentage.
    # Assign the string "Charging needed" if battery < 20, otherwise "Battery OK".
    # Print the result. Do this entirely in two lines (one for assignment, one for print).
    
    battery = 15
    status = "Charging needed" if battery < 20 else "Battery OK"
    print(status)

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Ternary expressions concisely assign a value based on a condition.
# - The syntax is: `value_if_true if condition else value_if_false`.
# - They improve readability for simple assignments but hinder it if overused or nested.

if __name__ == "__main__":
    basic_ternary_examples()
    practical_examples()
    advanced_usage()
    mini_challenge()
