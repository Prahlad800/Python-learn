"""
Topic: Number Systems
Chapter: 2
Level: Intermediate

Description:
    Python allows you to write integers in different number systems besides the standard base-10 (Decimal).
    You can represent numbers in Binary (base-2), Octal (base-8), and Hexadecimal (base-16) using specific prefixes.
    This is especially useful in lower-level programming, networking, bitwise operations, and color representations.

Real-Life Analogy:
    Think of number systems like different languages expressing the same concept. 
    The concept of "ten items" can be written as '10' in Decimal (English), '1010' in Binary (Computer code), 
    or 'A' in Hexadecimal (Color codes). They all represent the same underlying quantity.

Key Concepts:
    - Decimal (Base-10): No prefix
    - Binary (Base-2): Prefix '0b' or '0B'
    - Octal (Base-8): Prefix '0o' or '0O'
    - Hexadecimal (Base-16): Prefix '0x' or '0X'
    - Conversion functions: bin(), oct(), hex(), int()
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_number_systems() -> None:
    """Demonstrates defining numbers in various bases."""
    print("--- Number Systems Syntax ---")
    
    decimal_num = 25
    binary_num = 0b11001   # 25 in binary
    octal_num = 0o31       # 25 in octal
    hex_num = 0x19         # 25 in hex
    
    print(f"Decimal: {decimal_num}")
    # Note that Python prints them in decimal format by default
    print(f"Binary 0b11001 evaluated: {binary_num}")
    print(f"Octal 0o31 evaluated: {octal_num}")
    print(f"Hex 0x19 evaluated: {hex_num}")
    
    # Proving they are all equal
    print(f"Are they all equal? {decimal_num == binary_num == octal_num == hex_num}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def conversions() -> None:
    """Shows how to convert between bases using built-in functions."""
    print("\n--- Conversions ---")
    
    num = 255
    
    # These functions return string representations
    print(f"Decimal 255 to Binary: {bin(num)}")
    print(f"Decimal 255 to Octal: {oct(num)}")
    print(f"Decimal 255 to Hexadecimal: {hex(num)}")
    
    # Converting back to decimal from string representations
    # int(string, base)
    print(f"String 'FF' (base 16) back to integer: {int('FF', 16)}")
    print(f"String '11111111' (base 2) back to integer: {int('11111111', 2)}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def formatting_numbers() -> None:
    """Demonstrates using f-strings to format numbers in different bases."""
    print("\n--- Formatting with f-strings ---")
    
    num = 42
    
    # Using format specifiers in f-strings (b: binary, o: octal, x: hex lower, X: hex upper)
    print(f"Decimal: {num}")
    print(f"Binary : {num:b}")
    print(f"Octal  : {num:o}")
    print(f"Hex    : {num:x} or {num:X}")
    
    # Adding padding and prefixes
    print(f"Hex with prefix and padding: {num:#06x}") # e.g. 0x002a

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes() -> None:
    """Highlights common errors when working with number systems."""
    print("\n--- Common Mistakes and Best Practices ---")
    
    # Pitfall: Using incorrect digits for a base
    # Example: 0b102 (SyntaxError, binary can only have 0 and 1)
    # Example: 0o89 (SyntaxError, octal can only have 0-7)
    
    # Pitfall: Forgetting that bin(), oct(), and hex() return STRINGS, not integers.
    result = hex(255)
    print(f"Type of hex(255) is {type(result)}, you cannot add it mathematically to an int without converting.")
    
    # Best Practice: Use format strings (f"{num:x}") for display purposes instead of the hex() function if you want clean output without the '0x' prefix.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
1. What prefixes are used for binary, octal, and hexadecimal numbers in Python?
   Answer: 0b (Binary), 0o (Octal), and 0x (Hexadecimal).

2. Do bin(), oct(), and hex() return numeric data types?
   Answer: No, they return string representations of the numbers including the prefix.

3. How would you convert the hexadecimal string "A1" into an integer?
   Answer: Using the int() function with a base argument: int("A1", 16).

4. Are binary and hexadecimal variables a different type than decimal variables in Python?
   Answer: No, they are all stored as standard integer (int) objects in memory. The prefixes are just a way to author them in the code.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Write the number 15 in decimal, binary, octal, and hexadecimal. Assign them to variables and sum them up. Print the result.
Exercise 2: Write a program that converts the binary string "101010" to an integer.
Exercise 3: Format the integer 1024 as a hexadecimal string using an f-string.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge() -> None:
    """Simulate parsing color codes (hex to RGB)."""
    print("\n--- Mini Challenge ---")
    
    # A standard web color code
    color_hex = "#34A853"
    
    # Strip the '#'
    hex_val = color_hex.lstrip('#')
    
    # Convert segments to decimal
    # Indexing: RR=0:2, GG=2:4, BB=4:6
    red = int(hex_val[0:2], 16)
    green = int(hex_val[2:4], 16)
    blue = int(hex_val[4:6], 16)
    
    print(f"Hex Color: {color_hex}")
    print(f"RGB Values: Red={red}, Green={green}, Blue={blue}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
Summary:
- Python supports writing integers in binary, octal, and hexadecimal using prefixes.
- Under the hood, they are all just integers.
- Use `bin()`, `oct()`, and `hex()` to convert integers to base-string representations.
- Use `int(string, base)` to convert string representations back to integers.
- F-strings provide powerful formatting options for number systems.
"""

if __name__ == "__main__":
    basic_number_systems()
    conversions()
    formatting_numbers()
    common_mistakes()
    mini_challenge()
