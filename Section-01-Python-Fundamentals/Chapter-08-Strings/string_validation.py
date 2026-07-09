"""
Topic: String Validation (isalnum, isalpha, etc.)
Chapter: 8
Level: Beginner

Description:
    Python strings provide several methods that return boolean values (True or False) to validate the contents of the string.
    These are useful for form validation, parsing data, and ensuring data integrity.

Real-Life Analogy:
    Like a bouncer at a club checking an ID. They ask: "Is this person 18+?" (is numeric?), "Are they on the list?" (is alphabetical?).

Key Concepts:
    - isalpha()
    - isdigit(), isnumeric(), isdecimal()
    - isalnum()
    - isspace()
    - islower(), isupper()
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_validation():
    """Using basic validation methods."""
    alpha = "Python"
    num = "12345"
    alnum = "Python123"
    
    print(f"'{alpha}' isalpha? {alpha.isalpha()}")
    print(f"'{num}' isdigit? {num.isdigit()}")
    print(f"'{alnum}' isalnum? {alnum.isalnum()}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_validation():
    """Validating user input."""
    # Simulating user input
    user_age = "twenty"
    
    if user_age.isdigit():
        print("Valid age entered.")
    else:
        print("Invalid input! Please enter numbers only.")
        
    password = "   "
    if password.isspace() or not password:
        print("Password cannot be empty or just spaces.")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_validation():
    """Differences between digit validation methods."""
    # isdecimal() - characters that are strictly decimal (0-9)
    # isdigit() - decimals + digits like superscripts (²)
    # isnumeric() - digits + fractions/roman numerals (½)
    
    fraction = "½"
    superscript = "²"
    
    print(f"'{fraction}' isdecimal? {fraction.isdecimal()}")
    print(f"'{fraction}' isnumeric? {fraction.isnumeric()}")
    
    print(f"'{superscript}' isdigit? {superscript.isdigit()}")
    print(f"'{superscript}' isdecimal? {superscript.isdecimal()}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Using `isalpha()` to check for names and failing on spaces.
# "John Doe".isalpha() returns False because of the space!
# Fix: Remove spaces first or use regex.

# Best Practice: Use `isdecimal()` when checking if a string can be converted to an integer cleanly in Python, as it's the strictest.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q: What does `isalnum()` check for?
A: It returns True if all characters are alphanumeric (letters or numbers) and there is at least one character. Spaces will return False.

Q: What is the difference between `isdigit()`, `isdecimal()`, and `isnumeric()`?
A: `isdecimal()` is strictly 0-9. `isdigit()` includes superscripts/subscripts. `isnumeric()` includes fractions and roman numerals representing numbers in Unicode.

Q: How can you check if a string contains only whitespace?
A: Using the `isspace()` method.

Q: Will `"".isalpha()` (empty string) return True or False?
A: False. The string must have at least one character.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# 1. Ask for a user's pin code. Print "Valid" if it contains only digits and is 4 characters long.
# 2. Check if the string "HELLO WORLD" is uppercase using a built-in method.
# 3. Create a function that takes a string and returns True if it's a valid variable name (alphanumeric but cannot start with a number).

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def is_valid_variable_name(name: str) -> bool:
    """Check if a string is a valid Python variable name, basic validation."""
    if not name:
        return False
    # Can only contain letters, numbers, underscores
    clean_name = name.replace("_", "")
    if not clean_name.isalnum() and clean_name != "":
        return False
    # Cannot start with a number
    if name[0].isdigit():
        return False
    return True

def mini_challenge():
    """Test variable name validation."""
    tests = ["valid_var", "1invalid", "_hidden", "invalid-var"]
    for t in tests:
        # We can also just use the built-in isidentifier()!
        print(f"'{t}' is valid? Custom: {is_valid_variable_name(t)} | Built-in: {t.isidentifier()}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- String validation methods return True or False.
- `isalpha()`, `isdigit()`, `isalnum()` are common.
- Spaces fail `isalpha()` and `isalnum()`.
- Python differentiates between decimals, digits, and numerics based on Unicode character types.
- Empty strings always return False for these methods.
"""

if __name__ == "__main__":
    basic_validation()
    practical_validation()
    advanced_validation()
    mini_challenge()
