"""
Topic: Advanced String Formatting
Chapter: 4
Level: Intermediate

Description:
    Advanced string formatting allows you to precisely control how data is displayed. You can specify widths, alignment, padding characters, decimal precision, and number bases (like hex or binary) inside formatting expressions.

Real-Life Analogy:
    Formatting text is like a typesetter aligning articles in a newspaper. Some columns are right-aligned (like prices), some are centered (like titles), and some are padded with specific characters.

Key Concepts:
    - Alignment (<, >, ^)
    - Padding
    - Floating-point precision (.2f)
    - Number formatting (binary, hex, commas)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Specifying widths and basic alignment using f-strings
text = "Python"
print(f"|{text:<15}|") # Left align, width 15
print(f"|{text:>15}|") # Right align, width 15
print(f"|{text:^15}|") # Center align, width 15

# Adding padding characters
print(f"|{text:-^15}|") # Center align, pad with '-'
print(f"|{text:*>15}|") # Right align, pad with '*'

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    # Formatting numbers with commas
    large_number = 1000000000
    print(f"Population: {large_number:,}")
    
    # Formatting floating-point numbers to specific decimal places
    pi = 3.1415926535
    print(f"Pi to 2 decimal places: {pi:.2f}")
    print(f"Pi to 4 decimal places: {pi:.4f}")
    
    # Percentages
    success_rate = 0.875
    print(f"Success Rate: {success_rate:.1%}") # Prints 87.5%

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    number = 255
    
    # Number bases
    print(f"Decimal: {number:d}")
    print(f"Binary:  {number:b}")
    print(f"Hex:     {number:x}")
    print(f"Octal:   {number:o}")
    
    # Combining alignment, padding, and precision
    price = 45.6
    print(f"Total Cost: {price:0>8.2f}") # Padded with zeros, right aligned, 2 decimals
    
    # Dynamic formatting options
    width = 10
    precision = 3
    value = 12.3456
    print(f"Dynamic: {value:{width}.{precision}f}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Confusing the order of formatting specifiers.
# The correct order is: [fill][align][sign][#][0][width][grouping_option][.precision][type]
# e.g., f"{val:-^10.2f}"

# Mistake: Using .2f on a string
# f"{'hello':.2f}" # ValueError: Format specifier missing precision

# Best Practice: Use commas for large numbers to improve readability.
# Best Practice: When presenting tabular data, consistently use alignment options to make columns straight.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q: How do you format a number as currency with two decimal places?
A: Using the '.2f' format specifier, e.g., f"${price:.2f}".

Q: How do you add commas as thousands separators?
A: Use the ',' format specifier, e.g., f"{value:,}".

Q: How can you pad a number with leading zeros to a width of 5?
A: f"{number:05}" or f"{number:0>5}".

Q: What happens if the specified width is less than the length of the string?
A: Python ignores the width and prints the entire string without truncating.

Q: How do you center-align text with a specific character padding?
A: f"{text:^width}" where you can replace the space before '^' with any character, e.g., f"{text:*^10}".
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

def practice_exercises():
    # 1. Print the number 1234567.89 with commas and 2 decimal places.
    num = 1234567.89
    print(f"{num:,.2f}")
    
    # 2. Print the word "Title" centered in a 20-character wide field, padded with '='.
    title = "Title"
    print(f"{title:=^20}")
    
    # 3. Print the number 42 in binary, hex, and decimal.
    val = 42
    print(f"Bin: {val:b}, Hex: {val:x}, Dec: {val:d}")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: Print a formatted table of students and their grades.
    Names should be left-aligned (width 10).
    Grades should be right-aligned (width 5, 1 decimal place).
    """
    students = [("Alice", 95.5), ("Bob", 82), ("Charlie", 100)]
    
    print(f"{'Name':<10} | {'Grade':>6}")
    print("-" * 19)
    for name, grade in students:
        print(f"{name:<10} | {grade:>6.1f}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Formatting specifiers are placed after a colon (:) inside curly braces.
- Controls include alignment (<, >, ^), padding (characters before alignment), and width.
- Numeric formatting includes precision (.Nf), commas (,), and bases (b, x, o).
- Dynamic formatting allows using variables for widths and precisions.
"""

if __name__ == "__main__":
    practical_examples()
    advanced_usage()
    practice_exercises()
    mini_challenge()
