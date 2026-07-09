"""
Topic: Logical Operators
Chapter: 3
Level: Beginner

Description:
    Logical operators are used to combine conditional statements.
    They evaluate expressions and return True or False based on the truthfulness of the operands.

Real-Life Analogy:
    Imagine buying a movie ticket. 
    You get a discount if you are a student AND under 25. 
    You can enter the movie if you have a ticket OR are accompanied by staff.
    You can't enter if you are NOT wearing shoes.

Key Concepts:
    - and
    - or
    - not
    - Short-circuit evaluation
    - Truthiness/Falsiness
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================
def basic_syntax():
    print("--- Section 1: Basic Syntax ---")
    x = True
    y = False

    # AND operator: True only if BOTH are True
    print(f"{x} and {x} = {x and x}")
    print(f"{x} and {y} = {x and y}")

    # OR operator: True if AT LEAST ONE is True
    print(f"{x} or {y}  = {x or y}")
    print(f"{y} or {y}  = {y or y}")

    # NOT operator: Reverses the boolean value
    print(f"not {x}     = {not x}")
    print(f"not {y}     = {not y}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================
def practical_examples():
    print("\n--- Section 2: Practical Examples ---")
    # Example 1: Combining conditions (AND)
    age = 22
    has_license = True
    can_rent_car = (age >= 21) and has_license
    print(f"Can rent car? {can_rent_car}")

    # Example 2: Fallback options (OR)
    is_weekend = False
    is_holiday = True
    can_sleep_in = is_weekend or is_holiday
    print(f"Can sleep in? {can_sleep_in}")

    # Example 3: Reversing a condition (NOT)
    is_raining = False
    go_outside = not is_raining
    print(f"Go outside? {go_outside}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================
def advanced_usage():
    print("\n--- Section 3: Advanced Usage ---")
    # Short-circuit evaluation
    # AND returns the first falsy value, or the last value if all are truthy
    result_and = 10 and 20 and 0 and 30
    print(f"10 and 20 and 0 and 30 = {result_and}") # Returns 0

    # OR returns the first truthy value, or the last value if all are falsy
    result_or = 0 or "" or "Hello" or 50
    print(f'0 or "" or "Hello" or 50 = {result_or}') # Returns "Hello"

    # Avoiding errors using short-circuiting
    my_list = []
    # If the list is empty, `len(my_list) > 0` is False, so `my_list[0] == 5` is NEVER evaluated, preventing IndexError.
    is_first_five = len(my_list) > 0 and my_list[0] == 5
    print(f"Is first element 5? {is_first_five}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================
# Common Mistakes:
# 1. Confusing bitwise (`&`, `|`) with logical (`and`, `or`).
# 2. Writing `if x == True:` instead of just `if x:`.
# 3. Not understanding truthy/falsy values (0, "", [], {}, None are falsy; almost everything else is truthy).
#
# Best Practices:
# 1. Use short-circuiting intentionally to guard against exceptions (e.g., `if obj and obj.method():`).
# 2. Rely on truthiness for cleaner code (e.g., `if not my_list:` instead of `if len(my_list) == 0:`).

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
# Q1: What is short-circuit evaluation?
# A: It means Python stops evaluating logical expressions as soon as the result is determined. For `A or B`, if A is True, B is never evaluated.
#
# Q2: What will `print("A" and "B")` output?
# A: `"B"`. `and` evaluates to the last truthy value if all are truthy.
#
# Q3: What will `print([] or 5)` output?
# A: `5`. `[]` is falsy, so `or` moves to the next value, returning the first truthy one.
#
# Q4: Are logical operators lazy?
# A: Yes, because of short-circuit evaluation, they only evaluate expressions if necessary.
#
# Q5: Can you chain `not`?
# A: Yes, `not not x` converts `x` into its strict boolean representation (True/False).

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
# 1. Write an expression that checks if a number is between 10 and 20 (inclusive) OR is exactly 0.
# 2. Test the short-circuiting of `or` by placing a division by zero as the second operand when the first operand is True.
# 3. Use `and` and `or` to write a default-value assignment expression (e.g., assign `user_input` if it's truthy, otherwise assign `"default"`).

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================
def mini_challenge():
    print("\n--- Section 7: Mini Challenge ---")
    # You have an API response that might be None, an empty dictionary, or a populated dictionary.
    # Write a check to safely extract the user's name, defaulting to "Guest" if it's missing or invalid.
    responses = [
        {"user": {"name": "Alice"}},
        {"user": {}},
        {},
        None
    ]
    
    for i, resp in enumerate(responses):
        # Safe extraction using logical operators and truthiness
        # We use .get() which returns None if key doesn't exist, preventing KeyError
        name = (resp and resp.get("user") and resp.get("user").get("name")) or "Guest"
        print(f"Response {i+1} Name: {name}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
# - `and` requires all conditions to be true.
# - `or` requires at least one condition to be true.
# - `not` inverts the truth value.
# - Python uses short-circuit evaluation, which can be leveraged for safe data access and default values.
# - Non-boolean values have truthy or falsy states.

if __name__ == "__main__":
    basic_syntax()
    practical_examples()
    advanced_usage()
    mini_challenge()
