"""
Topic: Bitwise Operators
Chapter: 3
Level: Advanced

Description:
    Bitwise operators perform operations on numbers at the binary level (bit by bit).
    These are fast, low-level operations often used in cryptography, graphics, and network programming.

Real-Life Analogy:
    Think of a row of light switches. A bitwise operation is like applying a rule to multiple switches simultaneously, such as "flip all switches" (NOT) or "only keep the switch on if both corresponding switches in two other rooms are on" (AND).

Key Concepts:
    - AND (&)
    - OR (|)
    - XOR (^)
    - NOT (~)
    - Left Shift (<<)
    - Right Shift (>>)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================
def basic_syntax():
    print("--- Section 1: Basic Syntax ---")
    a = 10  # In binary: 1010
    b = 4   # In binary: 0100

    print(f"a = {a} (binary: {bin(a)})")
    print(f"b = {b}  (binary: {bin(b)})")

    # Bitwise AND
    print(f"a & b  = {a & b}   (binary: {bin(a & b)})")

    # Bitwise OR
    print(f"a | b  = {a | b}  (binary: {bin(a | b)})")

    # Bitwise XOR
    print(f"a ^ b  = {a ^ b}  (binary: {bin(a ^ b)})")

    # Bitwise NOT (Inverts bits: ~x = -x - 1)
    print(f"~a     = {~a}  (binary: {bin(~a)})")

    # Left Shift (Multiplies by 2^n)
    print(f"a << 1 = {a << 1}  (binary: {bin(a << 1)})")

    # Right Shift (Divides by 2^n)
    print(f"a >> 1 = {a >> 1}   (binary: {bin(a >> 1)})")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================
def practical_examples():
    print("\n--- Section 2: Practical Examples ---")
    # Example 1: Checking if a number is even or odd using Bitwise AND
    num = 42
    is_odd = (num & 1) == 1
    print(f"Is {num} odd? {is_odd}")

    # Example 2: Swapping two variables without a temporary variable using XOR
    x = 15
    y = 25
    print(f"Before swap: x={x}, y={y}")
    x = x ^ y
    y = x ^ y
    x = x ^ y
    print(f"After swap: x={x}, y={y}")

    # Example 3: Using bit masks to extract color components (RGB)
    color = 0xFF5733 # Hex color
    red = (color >> 16) & 0xFF
    green = (color >> 8) & 0xFF
    blue = color & 0xFF
    print(f"Hex: {hex(color)} -> R:{red}, G:{green}, B:{blue}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================
def advanced_usage():
    print("\n--- Section 3: Advanced Usage ---")
    # Setting a specific bit
    flags = 0b0000
    bit_to_set = 2
    flags |= (1 << bit_to_set)
    print(f"Set bit 2: {bin(flags)}")

    # Clearing a specific bit
    flags &= ~(1 << bit_to_set)
    print(f"Clear bit 2: {bin(flags)}")

    # Toggling a specific bit
    flags ^= (1 << 1)
    print(f"Toggle bit 1: {bin(flags)}")

    # Checking if a specific bit is set
    is_set = (flags & (1 << 1)) != 0
    print(f"Is bit 1 set? {is_set}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================
# Common Mistakes:
# 1. Confusing logical operators (`and`, `or`) with bitwise operators (`&`, `|`).
# 2. Forgetting operator precedence (bitwise operators have higher precedence than comparisons in some cases, but lower than arithmetic). Always use parentheses.
# 3. Not understanding that bitwise NOT `~` returns two's complement.
#
# Best Practices:
# 1. Use hexadecimal (0xFF) or binary (0b1010) literals when working with bitwise operations for clarity.
# 2. Use parentheses to explicitly show the order of operations.
# 3. Comment bitwise hacks, as they can be hard to read for beginners.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
# Q1: How do you determine if a number is a power of 2 using bitwise operators?
# A: `(n & (n - 1)) == 0` and `n != 0`.
#
# Q2: What is the difference between `and` and `&` in Python?
# A: `and` is a logical operator for booleans (short-circuiting). `&` is a bitwise operator for integers (operates on bits) or set intersections.
#
# Q3: How do you multiply a number by 4 using bitwise operators?
# A: Left shift by 2: `num << 2`.
#
# Q4: Why does `~5` result in `-6`?
# A: Because Python integers are conceptually infinitely wide two's complement numbers. `~x` is strictly equivalent to `-(x + 1)`.
#
# Q5: Can bitwise operators be used on floats?
# A: No, bitwise operators in Python only apply to integers (and boolean types, which are a subclass of integers).

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
# 1. Write a function to count the number of '1's in the binary representation of an integer.
# 2. Use bitwise shifts to implement a function that divides a number by 8.
# 3. Write a bitwise operation to flip the 3rd bit of a given number.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================
def mini_challenge():
    print("\n--- Section 7: Mini Challenge ---")
    # Implement a simple permissions system using bitwise flags.
    # Define flags
    READ = 0b100    # 4
    WRITE = 0b010   # 2
    EXECUTE = 0b001 # 1
    
    # User starts with no permissions
    user_perm = 0b000
    
    # Grant READ and EXECUTE
    user_perm |= (READ | EXECUTE)
    print(f"Granted READ and EXECUTE. Perms: {bin(user_perm)}")
    
    # Check if user can WRITE
    can_write = (user_perm & WRITE) != 0
    print(f"Can user write? {can_write}")
    
    # Grant WRITE
    user_perm |= WRITE
    print(f"Granted WRITE. Perms: {bin(user_perm)}")
    
    # Revoke EXECUTE
    user_perm &= ~EXECUTE
    print(f"Revoked EXECUTE. Perms: {bin(user_perm)}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
# - Bitwise operations work directly on binary digits.
# - & (AND), | (OR), ^ (XOR), ~ (NOT).
# - Shifts (<<, >>) are fast ways to multiply or divide by powers of two.
# - Extremely useful in low-level programming, cryptography, and handling flags/permissions.

if __name__ == "__main__":
    basic_syntax()
    practical_examples()
    advanced_usage()
    mini_challenge()
