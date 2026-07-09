"""
Topic: Conditional Statements Practice
Chapter: 5
Level: Beginner / Intermediate

Description:
    This file contains general practice exercises covering `if`, `elif`, `else`, nested conditions, 
    and ternary operators. It aims to solidify the foundational understanding of control flow.

Real-Life Analogy:
    Like solving a crossword puzzle, applying these concepts in various combinations strengthens your 
    problem-solving muscles.

Key Concepts:
    - Combining conditionals.
    - Implementing logic from word problems.
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# (Practice files focus on implementation rather than introducing syntax)

def practice_basics():
    print("--- Practice: Basics ---")
    # Task 1: Check if a number is positive, negative, or zero.
    num = 15
    if num > 0:
        print(f"{num} is positive.")
    elif num < 0:
        print(f"{num} is negative.")
    else:
        print(f"{num} is zero.")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practice_intermediate():
    print("\n--- Practice: Intermediate ---")
    # Task 2: FizzBuzz Logic for a single number
    # If divisible by 3 -> "Fizz"
    # If divisible by 5 -> "Buzz"
    # If divisible by both -> "FizzBuzz"
    
    n = 15
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def practice_advanced():
    print("\n--- Practice: Advanced (Ternary & Truthiness) ---")
    # Task 3: Use a ternary expression to check if a year is a leap year.
    # Logic: Divisible by 4, but NOT by 100 UNLESS also divisible by 400.
    
    year = 2024
    is_leap = True if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else False
    
    print(f"Is {year} a leap year? {is_leap}")
    
    # Task 4: Truthiness fallback
    user_input = None
    final_value = user_input or "Default Value"
    print(f"Resolved value: {final_value}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# When practicing, remember to:
# - Avoid redundant checks (e.g., if a number is not > 0 and not < 0, it IS 0, no need to check `== 0`).
# - Keep ternary operators simple.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# (Review previous files for specific Q&A, practice files focus on coding)

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Challenge for the user:
# Write a function that takes a temperature and a unit ("C" or "F").
# Convert it to the other unit using conditionals.
# Formula C to F: (C * 9/5) + 32
# Formula F to C: (F - 32) * 5/9

def temperature_converter(temp, unit):
    if unit.upper() == "C":
        converted = (temp * 9/5) + 32
        return f"{temp}°C is {converted}°F"
    elif unit.upper() == "F":
        converted = (temp - 32) * 5/9
        return f"{temp}°F is {converted}°C"
    else:
        return "Invalid unit."

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    print("\n--- Section 7: Mini Challenge ---")
    # Print the result of the converter
    print(temperature_converter(0, "C"))
    print(temperature_converter(212, "F"))

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Practice combining logical operators (and, or) within if statements.
# - Ensure order of execution is correct in elif chains (like in FizzBuzz).

if __name__ == "__main__":
    practice_basics()
    practice_intermediate()
    practice_advanced()
    mini_challenge()
