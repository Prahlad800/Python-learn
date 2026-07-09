"""
Topic: If-Else Statements
Chapter: 5
Level: Beginner

Description:
    The `if-else` statement extends the `if` statement by allowing you to execute an alternative block of code 
    when the `if` condition evaluates to False. It guarantees that exactly one of the two code blocks will run.

Real-Life Analogy:
    Approaching a fork in the road: "If the left path is open, I will take it. Else, I will take the right path." 
    You are guaranteed to take one path based on a single condition.

Key Concepts:
    - Branching: Splitting code execution into two distinct paths.
    - Mutually Exclusive: Both blocks can never run during the same execution.
    - Fallback: The `else` block acts as a default action if the condition isn't met.
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_if_else_examples():
    print("--- Section 1: Basic If-Else Statements ---")
    
    # Syntax:
    # if condition:
    #     # Code if True
    # else:
    #     # Code if False

    # Example 1: Basic check
    is_raining = False
    if is_raining:
        print("Take an umbrella.")
    else:
        print("Wear sunglasses.")

    # Example 2: Number check
    number = 7
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    print("\n--- Section 2: Practical Examples ---")

    # Example 1: Authentication Simulation
    user_password = "secure123"
    input_password = "password"
    
    if input_password == user_password:
        print("Access Granted.")
    else:
        print("Access Denied. Incorrect password.")

    # Example 2: E-commerce Stock Check
    item_stock = 0
    if item_stock > 0:
        print("Item added to cart.")
    else:
        print("Out of stock. Please try again later.")

    # Example 3: Value fallback
    user_city = ""
    if user_city:
        city = user_city
    else:
        city = "Unknown City"
    print(f"Shipping to: {city}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    print("\n--- Section 3: Advanced Usage ---")

    # Example 1: Assigning variables based on condition (without ternary)
    score = 85
    if score >= 60:
        status = "Pass"
    else:
        status = "Fail"
    print(f"Student status: {status}")

    # Example 2: Handling API responses or dictionary lookups safely
    api_response = {"status": "error", "data": None}
    
    if api_response.get("status") == "success":
        print("Processing data:", api_response["data"])
    else:
        print("Failed to fetch data. Falling back to cache.")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Common Mistakes:
# 1. Putting a condition on the `else` statement. 
#    `else x == 5:` -> SyntaxError. `else` takes no condition.
# 2. Indentation errors causing the `else` to match with the wrong `if` (in nested scenarios).

# Best Practices:
# - Use `if-else` when there are exactly two possible outcomes.
# - If you find yourself assigning to a variable in both blocks, consider a ternary expression (covered later).
# - Keep the logic straightforward. The `else` block should logically complement the `if` block.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: Can an `else` statement have a condition?
# A1: No, `else` acts as a catch-all when the `if` condition fails. It does not accept a condition.

# Q2: Is it mandatory to use `else` with an `if` statement?
# A2: No, `else` is optional. 

# Q3: What happens if the `if` condition and `else` block both contain return statements in a function?
# A3: The function will terminate at whichever block executes, returning the specified value, guaranteeing an exit.

# Q4: How is an `if-else` statement evaluated?
# A4: Python evaluates the `if` expression. If it is Truthy, the `if` block executes, and `else` is skipped. 
#     If it is Falsy, the `if` block is skipped, and the `else` block executes.

# Q5: What is a common refactoring technique for an `if-else` that assigns a single variable?
# A5: Replacing it with a conditional expression (ternary operator): `var = value_if_true if condition else value_if_false`.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write an if-else block that prints "Positive" if a number is > 0, else prints "Non-positive".
# Exercise 2: Given a variable `age`, write an if-else that prints "Eligible to vote" if age is >= 18, else "Not eligible".
# Exercise 3: Check if a string `email` contains the "@" character. If it does, print "Valid email format", else print "Invalid format".

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    print("\n--- Section 7: Mini Challenge ---")
    # You have a list of permitted IP addresses.
    # Check if a user's IP is in the list.
    # If yes, print "Connection allowed", otherwise print "Connection blocked".
    
    permitted_ips = ["192.168.1.1", "10.0.0.5", "172.16.0.2"]
    user_ip = "192.168.1.100"
    
    if user_ip in permitted_ips:
        print(f"Connection allowed for IP: {user_ip}")
    else:
        print(f"Connection blocked for IP: {user_ip}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - `if-else` structures handle two mutually exclusive paths of execution.
# - The `else` keyword does not take a condition.
# - It is crucial for fallback logic and default behaviors when conditions aren't met.

if __name__ == "__main__":
    basic_if_else_examples()
    practical_examples()
    advanced_usage()
    mini_challenge()
