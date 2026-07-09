"""
Topic: If Statements
Chapter: 5
Level: Beginner

Description:
    An `if` statement is the most fundamental control flow tool in Python. 
    It allows a program to execute a block of code only when a specified condition is true, making the program capable of decision-making.

Real-Life Analogy:
    Imagine walking outside and checking the weather. "If it is raining, I will take an umbrella." 
    The action (taking the umbrella) only happens if the condition (it is raining) is true.

Key Concepts:
    - Condition Evaluation: Expressions evaluate to True or False.
    - Indentation: Code blocks belonging to an `if` statement must be indented.
    - Boolean Context: Any expression can be used in an `if` statement (relies on truthiness).
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_if_examples():
    print("--- Section 1: Basic If Statements ---")
    
    # Syntax:
    # if condition:
    #     # Code to execute if condition is true

    # Example 1: Simple comparison
    age = 18
    if age >= 18:
        print("You are an adult.")

    # Example 2: Checking equality
    name = "Alice"
    if name == "Alice":
        print("Hello, Alice!")

    # Example 3: Multiple conditions (using and)
    is_weekend = True
    has_homework = False
    if is_weekend and not has_homework:
        print("You can play video games!")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    print("\n--- Section 2: Practical Examples ---")

    # Example 1: Validating user input (simulated)
    username = "admin_user"
    if len(username) > 5:
        print(f"Username '{username}' is valid in length.")

    # Example 2: Shopping cart discount threshold
    cart_total = 120.50
    if cart_total > 100.00:
        print("You qualify for free shipping!")

    # Example 3: File extension check
    filename = "report.pdf"
    if filename.endswith(".pdf"):
        print("This is a PDF document.")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    print("\n--- Section 3: Advanced Usage ---")

    # Example 1: Using functions that return booleans directly in if
    def is_even(num):
        return num % 2 == 0

    number = 42
    if is_even(number):
        print(f"{number} is an even number.")

    # Example 2: In-line assignments (Walrus operator :=) Python 3.8+
    # Evaluates the length and assigns it to 'n' simultaneously.
    data = [1, 2, 3, 4, 5]
    if (n := len(data)) > 3:
        print(f"List is long enough, it has {n} elements.")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Common Mistakes:
# 1. Using a single equals '=' (assignment) instead of double '==' (comparison).
#    if x = 5:  # SyntaxError
#    if x == 5: # Correct
#
# 2. Forgetting the colon ':' at the end of the if statement line.
#    if condition # SyntaxError
#
# 3. Incorrect indentation of the block following the if statement.

# Best Practices:
# - Keep conditions simple and readable.
# - Extract complex conditions into well-named variables or functions.
# - Use truthiness instead of explicit comparisons (e.g., `if my_list:` instead of `if len(my_list) > 0:`).

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is the difference between '=' and '==' in Python if statements?
# A1: '=' is the assignment operator, used to bind values to variables. 
#     '==' is the equality operator, used to compare if two values are equal.

# Q2: Can an `if` statement exist without an `else`?
# A2: Yes. The `if` statement evaluates independently; if the condition is false, 
#     it just skips the block and continues execution.

# Q3: What happens if the code inside an `if` block is not indented?
# A3: Python will raise an IndentationError.

# Q4: Explain the Walrus Operator in the context of an `if` statement.
# A4: The walrus operator (`:=`) allows assigning a value to a variable as part of an expression. 
#     It's useful in `if` statements to evaluate a condition and retain the calculated value for use inside the block.

# Q5: How does Python evaluate multiple conditions joined by `and`?
# A5: Python uses short-circuit evaluation. If the first condition in an `and` expression is False, 
#     it doesn't evaluate the second condition because the overall result must be False.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write an if statement that checks if a variable `temperature` is above 30, and prints "It's hot outside!".
# Exercise 2: Check if a string `password` is exactly 8 characters long. If so, print "Password length is acceptable."
# Exercise 3: Use an if statement to verify if a list `guests` contains the name "John".

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    print("\n--- Section 7: Mini Challenge ---")
    # Write a script that checks a user's account balance and their requested withdrawal amount.
    # If the balance is greater than or equal to the withdrawal amount AND the withdrawal amount is a multiple of 10,
    # print "Transaction approved."
    
    balance = 500
    withdrawal = 120
    
    if balance >= withdrawal and withdrawal % 10 == 0:
        print("Transaction approved. Dispensing cash.")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - The `if` statement executes a block of code only if its condition evaluates to True.
# - Code inside an `if` block must be indented.
# - Comparison operators (==, !=, >, <, >=, <=) and logical operators (and, or, not) are commonly used.
# - Python 3.8+ introduced the walrus operator (`:=`) for assignment expressions within conditionals.

if __name__ == "__main__":
    basic_if_examples()
    practical_examples()
    advanced_usage()
    mini_challenge()
