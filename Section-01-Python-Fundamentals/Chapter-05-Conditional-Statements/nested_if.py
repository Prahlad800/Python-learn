"""
Topic: Nested If Statements
Chapter: 5
Level: Intermediate

Description:
    A nested `if` statement is an `if` statement placed inside another `if`, `elif`, or `else` block. 
    It allows you to check for secondary conditions only when a primary condition evaluates to True.

Real-Life Analogy:
    Imagine entering a secure building. 
    Condition 1: "Do you have an ID?" (If Yes, proceed inside)
    Condition 2 (Nested): "Is your ID cleared for Level 2 access?" (If Yes, open door).

Key Concepts:
    - Scoping and Indentation: Each nested block adds a new level of indentation.
    - Dependent Logic: Inner conditions are only evaluated if outer conditions are met.
    - Code Readability: Deep nesting can make code hard to read.
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_nested_examples():
    print("--- Section 1: Basic Nested If Statements ---")
    
    # Syntax:
    # if outer_condition:
    #     if inner_condition:
    #         # Executes if both outer and inner are True

    # Example 1: Basic Nesting
    has_ticket = True
    is_vip = True

    if has_ticket:
        print("You can enter the concert.")
        if is_vip:
            print("You also get access to the backstage VIP lounge!")
    else:
        print("You need a ticket to enter.")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    print("\n--- Section 2: Practical Examples ---")

    # Example 1: Multi-step Validation
    username = "admin"
    password = "password123"

    input_user = "admin"
    input_pass = "password123"

    if input_user == username:
        if input_pass == password:
            print("Login successful!")
        else:
            print("Incorrect password.")
    else:
        print("User not found.")

    # Example 2: Loan Eligibility
    income = 60000
    credit_score = 750

    if income > 50000:
        if credit_score > 700:
            print("Loan Approved.")
        else:
            print("Loan Denied: Credit score too low.")
    else:
        print("Loan Denied: Income requirement not met.")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    print("\n--- Section 3: Advanced Usage ---")

    # Example: Replacing Nested Ifs with Logical Operators
    # Sometimes nested ifs can be flattened using `and`
    
    age = 25
    has_license = True
    
    # Nested approach:
    if age >= 18:
        if has_license:
            print("You can rent a car. (Nested)")
            
    # Flattened approach (often preferred for simplicity):
    if age >= 18 and has_license:
        print("You can rent a car. (Flattened)")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Common Mistakes:
# 1. Over-nesting (Arrow Code): Creating 4 or 5 levels of nested `if`s makes code unreadable and hard to maintain.
# 2. Indentation Errors: Losing track of which block an `else` belongs to.

# Best Practices:
# - Avoid deep nesting. If you go beyond 2 or 3 levels, consider refactoring.
# - Use logical operators (`and`) to flatten simple nested conditions.
# - Use Guard Clauses (early returns) in functions to avoid nesting entirely (covered in a dedicated file).

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is a nested `if` statement?
# A1: An `if` statement inside another `if`, `elif`, or `else` block.

# Q2: How do you avoid deep nesting?
# A2: You can combine conditions using boolean operators (`and`), extract logic into helper functions, or use guard clauses (early returns).

# Q3: Can an inner `if` have its own `else` block?
# A3: Yes, every `if` block, whether nested or not, can have its own `elif` and `else` branches.

# Q4: How does Python determine which `if` an `else` belongs to?
# A4: Python uses strict indentation. An `else` belongs to the `if` that is exactly at the same indentation level.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Create a nested if to check if a number is positive. If so, check if it's even or odd.
# Exercise 2: Simulate an ATM. If the pin is correct, check if the withdrawal amount is less than the balance.
# Exercise 3: Rewrite a nested `if` statement checking two conditions into a single `if` statement using `and`.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    print("\n--- Section 7: Mini Challenge ---")
    # A theme park ride requires a height of at least 120cm.
    # If the rider is tall enough, they must pay $12 if under 18, and $18 if 18 or older.
    # Write nested if statements to simulate this logic.
    
    height = 140
    age = 16
    
    if height >= 120:
        print("Tall enough to ride.")
        if age < 18:
            print("Ticket price is $12.")
        else:
            print("Ticket price is $18.")
    else:
        print("Not tall enough to ride.")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Nested `if`s allow evaluation of dependent conditions.
# - Indentation determines the structure and scope of the nesting.
# - While useful, excessive nesting degrades readability and should be flattened when possible.

if __name__ == "__main__":
    basic_nested_examples()
    practical_examples()
    advanced_usage()
    mini_challenge()
