"""
Topic: Elif Statements
Chapter: 5
Level: Beginner / Intermediate

Description:
    The `elif` (short for "else if") statement allows you to check multiple expressions for Truthiness 
    and execute a block of code as soon as one of the conditions evaluates to True. It is used in 
    conjunction with `if` and `else` to form a chain of conditions.

Real-Life Analogy:
    Grading a test: "If the score is >= 90, grade is A. Else if score >= 80, grade is B. 
    Else if score >= 70, grade is C. Else, grade is F." You evaluate options sequentially until one fits.

Key Concepts:
    - Sequential Evaluation: Conditions are evaluated top-to-bottom.
    - Short-circuiting: Once an `if` or `elif` condition is True, the rest of the chain is skipped.
    - Multiple Branches: Allows handling more than two possible outcomes.
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_elif_examples():
    print("--- Section 1: Basic Elif Statements ---")
    
    # Syntax:
    # if condition1:
    #     # Code if condition1 is True
    # elif condition2:
    #     # Code if condition2 is True
    # else:
    #     # Code if all above are False

    # Example 1: Simple Number Range
    number = 0
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    print("\n--- Section 2: Practical Examples ---")

    # Example 1: Traffic Light System
    light_color = "yellow"
    if light_color == "green":
        print("Go!")
    elif light_color == "yellow":
        print("Slow down!")
    elif light_color == "red":
        print("Stop!")
    else:
        print("Invalid light color.")

    # Example 2: Menu Selection
    choice = 2
    if choice == 1:
        print("Starting New Game...")
    elif choice == 2:
        print("Loading Saved Game...")
    elif choice == 3:
        print("Opening Settings...")
    else:
        print("Quitting Game.")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    print("\n--- Section 3: Advanced Usage ---")

    # Example 1: Elif with overlapping conditions (Order Matters!)
    # If the score is 95, it triggers the first True condition it hits.
    score = 95
    if score >= 60:
        print("Pass")
    elif score >= 90:
        # This will NEVER be reached because 95 is >= 60, triggering the first block.
        print("A Grade") 
    # Correcting the order:
    print("Correct Evaluation Order:")
    if score >= 90:
        print("A Grade")
    elif score >= 60:
        print("Pass")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Common Mistakes:
# 1. Order of conditions: Placing broader conditions before more specific ones will mask the specific ones.
# 2. Using multiple `if` statements instead of `elif` when conditions are mutually exclusive. 
#    Multiple `if`s evaluate all conditions, wasting performance and potentially causing bugs.

# Best Practices:
# - Always evaluate specific conditions before general conditions.
# - Use an `else` block at the end of an `elif` chain to catch unexpected values or handle defaults.
# - If you have a massive chain of `elif` statements checking exact equality, consider using `match-case` or dictionaries.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is the difference between multiple `if` statements and an `if-elif` chain?
# A1: Multiple `if` statements evaluate every condition independently, even if previous ones were True. 
#     An `if-elif` chain stops evaluating as soon as one condition is True.

# Q2: Can you have an `elif` without an `else`?
# A2: Yes, the `else` block is optional. If no conditions are True, the program simply continues past the chain.

# Q3: Can you have an `else` before an `elif`?
# A3: No. `else` must always be the final block in the conditional chain.

# Q4: Why might dictionary mapping be preferred over a long `elif` chain?
# A4: Dictionary mapping is more concise, faster (O(1) lookup vs O(N) evaluation), and cleaner for exact value matching.

# Q5: Does Python have a `switch` statement like C++ or Java?
# A5: Historically, no. Python used `elif` chains or dictionaries. However, Python 3.10 introduced structural pattern matching (`match-case`), which serves a similar purpose.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write an if-elif chain that prints the season based on the month (e.g., Dec-Feb = Winter, Mar-May = Spring).
# Exercise 2: Categorize a person's age into: "Child" (<13), "Teenager" (13-19), "Adult" (20-64), "Senior" (65+).
# Exercise 3: Create a basic calculator logic that takes an operator ('+', '-', '*', '/') and performs the correct operation.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    print("\n--- Section 7: Mini Challenge ---")
    # Write a script to calculate shipping cost based on package weight.
    # Weight <= 2kg: $5
    # Weight <= 5kg: $10
    # Weight <= 10kg: $15
    # Above 10kg: $20
    
    weight = 7.5
    cost = 0
    
    if weight <= 2:
        cost = 5
    elif weight <= 5:
        cost = 10
    elif weight <= 10:
        cost = 15
    else:
        cost = 20
        
    print(f"Shipping cost for {weight}kg package is ${cost}.")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - `elif` provides a way to evaluate multiple mutually exclusive conditions sequentially.
# - The evaluation stops at the first True condition.
# - The order of conditions is critical to ensure proper logic flow.

if __name__ == "__main__":
    basic_elif_examples()
    practical_examples()
    advanced_usage()
    mini_challenge()
