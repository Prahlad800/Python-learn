"""
Topic: F-Strings (Formatted String Literals)
Chapter: 4
Level: Beginner

Description:
    F-strings, introduced in Python 3.6, provide a concise and readable way to embed expressions inside string literals. By prefixing a string with 'f' or 'F', you can place variables and expressions directly into the string using curly braces {}.

Real-Life Analogy:
    Think of f-strings like a fill-in-the-blanks form. The text of the form is pre-written, and wherever there is a blank {variable}, you just drop in the required information dynamically.

Key Concepts:
    - F-string syntax: f"string {variable}"
    - Expression evaluation inside braces
    - Multiline f-strings
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Basic f-string usage
name = "Alice"
age = 30

# Simply prefix the string with an 'f' and use {} for variables
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)

# F-strings can evaluate expressions directly
print(f"In 5 years, {name} will be {age + 5} years old.")

# Using functions inside f-strings
print(f"My name in uppercase is {name.upper()}.")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    item = "Laptop"
    price = 999.99
    quantity = 3
    
    # Calculating total inside an f-string
    receipt = f"Bought {quantity} {item}s for ${price * quantity} total."
    print(receipt)
    
    # Accessing dictionary values
    user = {"username": "john_doe", "role": "admin"}
    print(f"User {user['username']} logged in with role: {user['role']}.")
    
    # Calling custom functions
    def greet(n):
        return f"Greetings, {n}!"
    print(f"System Message: {greet(name)}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    import datetime
    
    # Formatting dates
    now = datetime.datetime.now()
    print(f"Current time: {now:%Y-%m-%d %H:%M:%S}")
    
    # F-string debugging feature (Python 3.8+)
    x = 10
    y = 20
    print(f"{x=}, {y=}, {x*y=}") # Prints x=10, y=20, x*y=200
    
    # Multiline f-strings
    message = (
        f"Name: {name}\n"
        f"Age: {age}\n"
        f"Status: Active"
    )
    print(message)

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Forgetting the 'f' prefix
# print("Hello {name}") # Prints literally "Hello {name}"

# Mistake: Using the same quote marks inside and outside
# user = {"name": "Bob"}
# f"User is {user["name"]}" # SyntaxError

# Correction: Use different quotes
user_dict = {"name": "Bob"}
print(f"User is {user_dict['name']}")

# Best Practice: Keep expressions inside f-strings simple. 
# If it's too complex, compute it before the f-string.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q: When were f-strings introduced in Python?
A: Python 3.6.

Q: How do f-strings compare to .format() in terms of performance?
A: F-strings are generally faster because they are evaluated at runtime rather than as a method call.

Q: Can you execute arbitrary Python code inside an f-string?
A: Yes, any valid Python expression can be placed inside the curly braces.

Q: How do you print literal curly braces in an f-string?
A: By escaping them with double curly braces: f"{{hello}}".

Q: What is the '=' specifier in f-strings?
A: Introduced in Python 3.8, it prints the variable name and its value, useful for debugging (e.g., f"{x=}").
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

def practice_exercises():
    # 1. Create variables for a city and temperature, then print a weather report using an f-string.
    city = "London"
    temp = 15
    print(f"The temperature in {city} is {temp}°C.")
    
    # 2. Write an f-string that prints the length of a given string.
    word = "Python"
    print(f"The length of the word '{word}' is {len(word)}.")
    
    # 3. Use the debugging feature to print two variables.
    a, b = 5, 10
    print(f"{a=}, {b=}")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: Create an invoice printer. Given a list of item prices,
    print out each item price and the total with a 10% tax added using f-strings.
    """
    prices = [100, 250, 50]
    subtotal = sum(prices)
    tax = subtotal * 0.10
    total = subtotal + tax
    
    print("--- INVOICE ---")
    for i, p in enumerate(prices, 1):
        print(f"Item {i}: ${p}")
    print("---------------")
    print(f"Subtotal: ${subtotal}")
    print(f"Tax(10%): ${tax}")
    print(f"Total:    ${total}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- F-strings start with 'f' or 'F'.
- They allow embedding of variables and expressions using {}.
- They are fast, readable, and less prone to errors compared to older formatting methods.
- Support advanced features like debugging (=) and format specifiers.
"""

if __name__ == "__main__":
    practical_examples()
    advanced_usage()
    practice_exercises()
    mini_challenge()
