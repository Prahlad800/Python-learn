"""
Topic: String Formatting Methods (.format() and % formatting)
Chapter: 4
Level: Intermediate

Description:
    Before f-strings were introduced in Python 3.6, developers used the `.format()` method and the older `%` (modulo) formatting. While f-strings are preferred now, it's essential to understand these older methods as they appear heavily in legacy code and still have specific use cases.

Real-Life Analogy:
    Using `.format()` is like using mail merge in Word. You have a template document with placeholders, and you provide a list of data to be injected into those specific slots.

Key Concepts:
    - .format() method
    - Positional and keyword arguments in .format()
    - % string formatting (printf-style)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# 1. The .format() method
template = "Hello, {}. Welcome to {}."
print(template.format("Alice", "Pythonville"))

# 2. % Formatting (Old Style)
old_template = "Hello, %s. Welcome to %s."
print(old_template % ("Bob", "JavaTown"))

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    # Positional arguments with .format()
    # You can reuse the same argument multiple times
    print("{0} is learning {1}. {0} loves {1}!".format("Dave", "C++"))
    
    # Keyword arguments with .format()
    print("Product: {name}, Price: ${price}".format(name="Monitor", price=200))
    
    # Unpacking a dictionary
    user = {"name": "Eve", "age": 28}
    print("User {name} is {age} years old.".format(**user))

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    # Accessing list elements inside .format()
    items = ["Apple", "Banana", "Cherry"]
    print("First: {0[0]}, Second: {0[1]}".format(items))
    
    # Accessing object attributes
    class Person:
        def __init__(self, name):
            self.name = name
    p = Person("Frank")
    print("Person's name is {0.name}".format(p))
    
    # Formatting numbers with % (C-style)
    pi = 3.14159
    print("Pi is approximately %.2f" % pi)
    print("Hex of 255 is %x" % 255)

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Providing fewer arguments than placeholders.
# "{}, {}, {}".format(1, 2) # IndexError: tuple index out of range

# Mistake: Mixing manual and automatic numbering in .format() (in Python 3.1+)
# "{} {1}".format(1, 2) # ValueError: cannot switch from automatic field numbering to manual

# Best Practice: Use f-strings for new code. Use .format() when the template string is defined elsewhere (e.g., loaded from a file).
# Best Practice: Avoid % formatting for complex strings as it gets difficult to read and is prone to type errors.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q: What is the main difference between % formatting and .format()?
A: .format() is a method that is more powerful, readable, and supports keyword arguments and object attributes. % formatting is older, C-style, and less flexible.

Q: How do you unpack a dictionary into .format()?
A: By using double asterisks: string.format(**my_dict).

Q: Can you mix positional and keyword arguments in .format()?
A: Yes, e.g., "{0} is {age}".format("John", age=30). Positional arguments must come first.

Q: Why might someone still use .format() instead of f-strings?
A: When the string template is not known at compile time (e.g., read from a database or configuration file), f-strings cannot be used directly, making .format() the best choice.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

def practice_exercises():
    # 1. Use .format() to print a sentence with positional arguments in reverse order.
    print("{2} {1} {0}".format("first", "second", "third"))
    
    # 2. Use % formatting to print an integer and a float.
    print("Integer: %d, Float: %.1f" % (10, 5.5))

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: You have a list of dictionaries representing employees.
    Use .format() to print a neat summary for each employee.
    """
    employees = [
        {"name": "Alice", "role": "Developer", "salary": 90000},
        {"name": "Bob", "role": "Designer", "salary": 75000}
    ]
    
    template = "{name:<10} | {role:<15} | ${salary:,}"
    for emp in employees:
        print(template.format(**emp))

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- % formatting is the oldest method, similar to C's printf.
- .format() is more powerful, allowing reordering, keyword arguments, and attribute access.
- F-strings are generally preferred over both for new code.
- .format() remains crucial for dynamically loaded templates.
"""

if __name__ == "__main__":
    practical_examples()
    advanced_usage()
    practice_exercises()
    mini_challenge()
