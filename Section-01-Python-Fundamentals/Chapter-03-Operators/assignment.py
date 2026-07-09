"""
Topic: Assignment Operators
Chapter: 3
Level: Beginner

Description:
    Assignment operators are used to assign values to variables.
    Python also provides compound assignment operators that perform an operation and assign the result in one step.

Real-Life Analogy:
    Imagine a bank account. A simple assignment is setting your balance to $100. A compound assignment is like depositing $50 into your account (Balance += $50).

Key Concepts:
    - Basic Assignment (=)
    - Compound Addition/Subtraction (+=, -=)
    - Compound Multiplication/Division (*=, /=)
    - Other Compound Operators (//=, %=, **=, &=, |=, ^=, <<=, >>=)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_assignment():
    print("--- Section 1: Basic Assignment ---")
    # Basic assignment
    x = 10
    print(f"Initial x: {x}")

    # Compound addition
    x += 5  # Equivalent to x = x + 5
    print(f"After x += 5: {x}")

    # Compound subtraction
    x -= 3  # Equivalent to x = x - 3
    print(f"After x -= 3: {x}")

    # Compound multiplication
    x *= 2  # Equivalent to x = x * 2
    print(f"After x *= 2: {x}")

    # Compound division
    x /= 4  # Equivalent to x = x / 4 (results in a float)
    print(f"After x /= 4: {x}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    print("\n--- Section 2: Practical Examples ---")
    # Example 1: Updating a counter in a loop
    counter = 0
    for i in range(3):
        counter += 1
    print(f"Final counter value: {counter}")

    # Example 2: Accumulating a string
    message = "Hello"
    message += " "
    message += "World!"
    print(f"Accumulated string: {message}")

    # Example 3: Applying a discount
    price = 100.0
    discount = 0.20
    price *= (1 - discount)  # Apply 20% discount
    print(f"Price after discount: ${price:.2f}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    print("\n--- Section 3: Advanced Usage ---")
    # Bitwise compound assignment
    flags = 0b0001
    print(f"Initial flags: {bin(flags)}")
    
    # Set a bit (OR)
    flags |= 0b0010
    print(f"After |= 0b0010: {bin(flags)}")
    
    # Toggle a bit (XOR)
    flags ^= 0b0011
    print(f"After ^= 0b0011: {bin(flags)}")

    # Shift left
    flags <<= 2
    print(f"After <<= 2: {bin(flags)}")

    # Multiple assignment
    a = b = c = 42
    print(f"Multiple assignment: a={a}, b={b}, c={c}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================
# Common Mistakes:
# 1. Confusing `=` (assignment) with `==` (comparison).
# 2. Trying to use compound assignment in an expression (e.g., `print(x += 1)` is invalid in Python).
# 3. Assuming `x += y` always creates a new object (it modifies mutable objects like lists in-place).
#
# Best Practices:
# 1. Use compound assignment for cleaner, more readable code.
# 2. Remember that lists behave differently with `+=` than with `+`. `list1 += list2` modifies list1 in place (like extend).

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
# Q1: What is the difference between `=` and `==`?
# A: `=` is an assignment operator used to assign a value to a variable. `==` is a comparison operator used to check if two values are equal.
#
# Q2: Can you do `x++` or `x--` in Python?
# A: No, Python does not have increment (`++`) or decrement (`--`) operators. You must use `x += 1` or `x -= 1`.
#
# Q3: What happens when you use `+=` on a list vs `+`?
# A: `my_list += [1]` modifies the list in place (calls `__iadd__`). `my_list = my_list + [1]` creates a new list and reassigns it (calls `__add__`).
#
# Q4: Is assignment an expression in Python?
# A: In older versions, no. With Python 3.8+, the walrus operator (`:=`) introduced assignment expressions.
#
# Q5: What is tuple unpacking in assignment?
# A: It allows assigning multiple variables at once from an iterable: `a, b = 1, 2`.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
# 1. Initialize a variable `balance` to 1000. Simulate 3 deposits and 2 withdrawals using compound assignment operators.
# 2. Initialize a string. Use `+=` to add three different words to it sequentially.
# 3. Write a small script that halves a number repeatedly until it's less than 1, using `/=`.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================
def mini_challenge():
    print("\n--- Section 7: Mini Challenge ---")
    # Simulate a basic tamagotchi's stats
    hunger = 50
    happiness = 50
    energy = 50
    
    print(f"Initial: Hunger={hunger}, Happiness={happiness}, Energy={energy}")
    
    # Action: Feed
    hunger -= 20
    energy += 5
    
    # Action: Play
    happiness += 30
    energy -= 15
    hunger += 10
    
    # Action: Sleep
    energy += 40
    hunger += 15
    
    print(f"Final: Hunger={hunger}, Happiness={happiness}, Energy={energy}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
# - Assignment sets a value.
# - Compound assignment performs an operation and reassigns in one step (e.g., +=, *=).
# - Python lacks ++ and --, so += 1 and -= 1 are the standard alternatives.
# - Be aware of how += behaves with mutable objects like lists.

if __name__ == "__main__":
    basic_assignment()
    practical_examples()
    advanced_usage()
    mini_challenge()
