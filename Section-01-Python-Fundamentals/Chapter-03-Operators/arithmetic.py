"""
Topic: Arithmetic Operators
Chapter: 3
Level: Beginner

Description:
    Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, and division.
    They are the fundamental building blocks for mathematical logic in programming.

Real-Life Analogy:
    Think of a basic calculator. When you press '+', '-', '*', or '/', you are using arithmetic operators to compute a result from numbers.

Key Concepts:
    - Basic operations (+, -, *, /)
    - Floor division (//)
    - Modulo (%)
    - Exponentiation (**)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_operations():
    print("--- Section 1: Basic Operations ---")
    a = 15
    b = 4

    # Addition
    print(f"{a} + {b} = {a + b}")

    # Subtraction
    print(f"{a} - {b} = {a - b}")

    # Multiplication
    print(f"{a} * {b} = {a * b}")

    # True Division (always returns a float)
    print(f"{a} / {b} = {a / b}")

    # Floor Division (returns integer if operands are integers, rounds down)
    print(f"{a} // {b} = {a // b}")

    # Modulo (remainder)
    print(f"{a} % {b} = {a % b}")

    # Exponentiation (power)
    print(f"{a} ** {b} = {a ** b}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    print("\n--- Section 2: Practical Examples ---")
    # Example 1: Calculating total cost with tax
    price = 50
    tax_rate = 0.08
    total_cost = price + (price * tax_rate)
    print(f"Total cost with tax: ${total_cost:.2f}")

    # Example 2: Distributing items evenly
    total_candies = 23
    children = 5
    candies_per_child = total_candies // children
    leftover_candies = total_candies % children
    print(f"Each child gets {candies_per_child} candies. {leftover_candies} candies are left over.")

    # Example 3: Checking if a number is even or odd
    number = 42
    is_even = (number % 2 == 0)
    print(f"Is {number} even? {is_even}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    print("\n--- Section 3: Advanced Usage ---")
    # Floating point precision issues
    print(f"0.1 + 0.2 = {0.1 + 0.2} (Notice the small precision error)")

    # Exponentiation with fractional powers (roots)
    square_root_of_16 = 16 ** 0.5
    cube_root_of_27 = 27 ** (1/3)
    print(f"Square root of 16: {square_root_of_16}")
    print(f"Cube root of 27: {cube_root_of_27}")

    # Negative modulo (Python follows floor division semantics)
    print(f"-5 % 3 = {-5 % 3}") # The result takes the sign of the divisor

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================
# Common Mistakes:
# 1. Using `/` instead of `//` when an integer result is expected.
# 2. Forgetting that modulo with negative numbers works differently in Python than in C/C++.
# 3. Dividing by zero (ZeroDivisionError).
#
# Best Practices:
# 1. Use the `math` module for complex mathematical operations.
# 2. Be careful with floating-point comparisons due to precision issues.
# 3. Handle potential ZeroDivisionErrors using try-except blocks.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
# Q1: What is the difference between `/` and `//` in Python 3?
# A: `/` performs true division and returns a float, while `//` performs floor division and returns an integer (if operands are integers) representing the quotient rounded down.
#
# Q2: How do you find the last digit of an integer?
# A: By using modulo 10: `last_digit = num % 10`.
#
# Q3: What is the output of `9 % -2` in Python?
# A: `-1`. Python's modulo operator has the same sign as the divisor. 9 // -2 is -5. So 9 - (-2 * -5) = 9 - 10 = -1.
#
# Q4: How do you swap two numbers without using a temporary variable?
# A: In Python, you can use tuple unpacking: `a, b = b, a`. Using arithmetic: `a = a + b; b = a - b; a = a - b`.
#
# Q5: Why is `0.1 + 0.2` not equal to `0.3`?
# A: Because of the way floating-point numbers are represented in binary (IEEE 754 standard), causing small rounding errors.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
# 1. Write a program to calculate the area of a circle given its radius.
# 2. Write a program to convert Celsius to Fahrenheit using the formula F = C * 9/5 + 32.
# 3. Given a number of seconds, convert it into hours, minutes, and remaining seconds.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================
def mini_challenge():
    print("\n--- Section 7: Mini Challenge ---")
    # Build a simple currency converter and cash register.
    # Given an amount of money and a cost, calculate change.
    # Then figure out how many $10, $5, and $1 bills to give back.
    cost = 23
    paid = 50
    change = paid - cost
    print(f"Total Change: ${change}")
    
    tens = change // 10
    change = change % 10
    
    fives = change // 5
    change = change % 5
    
    ones = change
    print(f"Bills returned - $10s: {tens}, $5s: {fives}, $1s: {ones}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
# - Arithmetic operators allow basic math computations.
# - Remember the difference between true division (/) and floor division (//).
# - Modulo (%) is extremely useful for checking even/odd, cyclical patterns, and remainders.
# - Exponentiation is done via `**`.

if __name__ == "__main__":
    basic_operations()
    practical_examples()
    advanced_usage()
    mini_challenge()
