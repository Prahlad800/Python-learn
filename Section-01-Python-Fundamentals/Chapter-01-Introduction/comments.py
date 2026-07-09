"""
Topic: Comments and Docstrings
Chapter: 01
Level: Beginner

Description:
    Comments are text in a program that the interpreter ignores. They are used to explain code,
    leave notes, or temporarily disable parts of a script. Docstrings are special strings 
    used to document modules, classes, functions, and methods.

Real-Life Analogy:
    Comments are like margin notes in a recipe book. They don't change how the dish is cooked 
    (the code execution), but they help the chef (the programmer) remember why certain ingredients 
    were used or warn them about a tricky step.

Key Concepts:
    - Single-line comments (`#`)
    - Inline comments
    - Docstrings (`\"\"\"`)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# This is a single-line comment. Python ignores this completely.
def basic_comments():
    print("Comments are useful!")  # This is an inline comment explaining this specific line.

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def calculate_discount(price: float, discount_percent: float) -> float:
    """
    Calculate the final price after applying a discount.
    
    This is a docstring. It explains what the function does, its parameters, and its return value.
    Docstrings can be accessed via the __doc__ attribute.
    """
    # Convert percentage to a decimal
    discount_amount = price * (discount_percent / 100)
    
    # Subtract discount from the original price
    final_price = price - discount_amount
    return final_price

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_comment_usage():
    # You can use comments to temporarily disable code (commenting out code)
    # print("This line will not run")
    
    print("Function docstring:", calculate_discount.__doc__.strip())

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistakes:
# - Writing redundant comments (e.g., x = 5 # Assigns 5 to x).
# - Failing to update comments when code changes, leading to misleading information.
# - Using multi-line strings (""") purely as multi-line comments outside of functions/classes.

# Best Practices:
# - Comment "why" something is done, not "what" is done, unless the "what" is extremely complex.
# - Always write docstrings for public modules, functions, classes, and methods.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: How do you create a comment in Python?
# A: Using the hash symbol (#) for single-line comments.
#
# Q2: What is the difference between a comment and a docstring?
# A: Comments are completely ignored by the interpreter. Docstrings are parsed and attached to the object's __doc__ attribute, making them accessible at runtime.
#
# Q3: Does Python have block comments?
# A: Python does not have a specific block comment syntax (like /* */ in C). You must use a # on each line, or use an unassigned multi-line string.
#
# Q4: Why should you avoid redundant comments?
# A: They clutter the code and make it harder to read without adding any value.
#
# Q5: What tool is often used to extract docstrings into documentation?
# A: Sphinx, pydoc, and other automatic documentation generators.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a function with a detailed docstring explaining its purpose.
# Exercise 2: Take a block of code and comment out half of it. Run it to see the effect.
# Exercise 3: Add an inline comment to a print statement.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    This function demonstrates proper commenting techniques.
    It calculates the square of a number.
    """
    # Define the target number
    num = 8
    # Calculate square
    square = num ** 2
    print(f"The square of {num} is {square}")  # Output the result

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Use `#` for single-line and inline comments.
# - Use `"""` for docstrings immediately after function/class definitions.
# - Comments explain the "why", code explains the "how".

if __name__ == "__main__":
    basic_comments()
    price = calculate_discount(100.0, 15.0)
    print(f"Discounted price: ${price}")
    advanced_comment_usage()
    mini_challenge()
