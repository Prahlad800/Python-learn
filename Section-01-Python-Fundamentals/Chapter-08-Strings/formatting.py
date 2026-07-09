"""
Topic: String Formatting
Chapter: 8
Level: Intermediate

Description:
    String formatting is the process of injecting dynamic variables or values into a string.
    Python provides multiple ways to format strings, from older `%` formatting to modern f-strings.

Real-Life Analogy:
    Imagine a fill-in-the-blank template for a formal letter. Formatting is like filling in those blanks with the recipient's name and details.

Key Concepts:
    - % formatting (legacy)
    - str.format() method
    - f-strings (Formatted String Literals, Python 3.6+)
    - Number formatting, padding, alignment
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def legacy_and_format():
    """Older ways of string formatting."""
    name = "Alice"
    age = 30
    
    # 1. % formatting (C-style)
    print("Name: %s, Age: %d" % (name, age))
    
    # 2. str.format() method
    print("Name: {}, Age: {}".format(name, age))
    print("Name: {0}, Age: {1}. {0} is great.".format(name, age))
    print("Name: {n}, Age: {a}".format(n=name, a=age))

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def f_strings_example():
    """Modern f-strings are the preferred method."""
    item = "Coffee"
    price = 4.5
    
    # Direct variable injection
    print(f"Item: {item}, Price: ${price}")
    
    # Expressions inside f-strings
    print(f"Total for 3 coffees: ${price * 3}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_formatting():
    """Padding, alignment, and numerical formatting."""
    # Number formatting
    pi = 3.14159265
    print(f"Pi rounded to 2 decimal places: {pi:.2f}")
    
    # Padding and alignment
    text = "Status"
    print(f"|{text:<15}|") # Left align
    print(f"|{text:>15}|") # Right align
    print(f"|{text:^15}|") # Center align
    
    # Leading zeros
    number = 42
    print(f"ID: {number:05d}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Mixing up positional and keyword arguments in str.format()
# format("Hello {1}, I am {name}", "John", name="Doe") # valid, but can be confusing.
# format("Hello {name}, I am {0}", "John", name="Doe") # SyntaxError: positional argument follows keyword argument

# Best Practice: Always use f-strings for readability and performance if using Python 3.6+.
# Best Practice: Use `str.format()` if the format string is defined dynamically at runtime.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q: Which string formatting method is the fastest?
A: f-strings (formatted string literals) are evaluated at runtime and are optimized, making them the fastest option.

Q: How do you format a float to display exactly two decimal places using f-strings?
A: Using the `: .2f` specifier, e.g., `f"{value:.2f}"`.

Q: What does the `{x=}` syntax do in an f-string?
A: Introduced in Python 3.8, it prints the variable name and its value. E.g., `f"{x=}"` outputs `x=10`.

Q: Is `%` formatting deprecated?
A: No, it's not deprecated, but it's generally discouraged for new code in favor of f-strings or `str.format()`.

Q: Can you call functions inside an f-string?
A: Yes, any valid Python expression can be evaluated inside an f-string's curly braces.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# 1. Use an f-string to print a dictionary's values: `user = {"name": "Bob", "age": 25}`.
# 2. Format a large number with comma separators (e.g., 1000000 -> 1,000,000).
# 3. Create a receipt format showing Item, Quantity, and Price lined up neatly.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """Print a neatly formatted table using f-strings."""
    data = [
        ("Apples", 5, 2.5),
        ("Bananas", 12, 1.2),
        ("Cherries", 30, 0.15)
    ]
    
    print(f"{'Item':<15} | {'Qty':^5} | {'Price':>8}")
    print("-" * 34)
    for item, qty, price in data:
        print(f"{item:<15} | {qty:^5} | ${price:>7.2f}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- % formatting is the oldest style.
- `str.format()` is flexible and allows re-using arguments.
- f-strings (`f"..."`) are the most readable and fastest method (Python 3.6+).
- Format specifiers (`:.2f`, `:>10`) control decimal places, alignment, and padding.
"""

if __name__ == "__main__":
    legacy_and_format()
    f_strings_example()
    advanced_formatting()
    mini_challenge()
