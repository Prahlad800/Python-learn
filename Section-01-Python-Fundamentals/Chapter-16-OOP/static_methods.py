"""
Topic: Static Methods
Chapter: 16
Level: Intermediate

Description:
    Static methods are methods that are nested in a class but do not have access to either 
    instance state (`self`) or class state (`cls`). They act like regular functions but belong 
    to the class's namespace because they have some logical connection to the class.

Real-Life Analogy:
    Imagine a Calculator class. A method that calculates the area of a circle based on a given 
    radius doesn't need to know anything about the calculator's brand, model, or history. 
    It just takes an input and returns an output. It's grouped inside the Calculator class for 
    organization, not because it needs access to the Calculator's internal data.

Key Concepts:
    - The `@staticmethod` decorator
    - No implicit first argument (`self` or `cls`)
    - Namespace grouping
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

class MathUtilities:
    
    @staticmethod
    def add(x: float, y: float) -> float:
        # Notice no 'self' or 'cls' parameter
        return x + y
        
    @staticmethod
    def is_even(number: int) -> bool:
        return number % 2 == 0

def basic_syntax_examples():
    print("--- Basic Syntax ---")
    # Can be called on the class itself
    print(f"5 + 7 = {MathUtilities.add(5, 7)}")
    print(f"Is 4 even? {MathUtilities.is_even(4)}")
    
    # Can also be called on an instance (though less common)
    utils = MathUtilities()
    print(f"Is 7 even? {utils.is_even(7)}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

class StringFormatter:
    
    @staticmethod
    def to_title_case(text: str) -> str:
        """Utility function grouped in a class context."""
        return text.title()
        
    @staticmethod
    def remove_vowels(text: str) -> str:
        vowels = "aeiouAEIOU"
        return "".join(char for char in text if char not in vowels)

def practical_examples():
    print("\n--- Practical Examples ---")
    msg = "hello world"
    print(f"Title case: {StringFormatter.to_title_case(msg)}")
    print(f"No vowels: {StringFormatter.remove_vowels(msg)}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        
    def get_details(self):
        return f"{self.name} earns ${self.salary}"
        
    @staticmethod
    def is_workday(day: str) -> bool:
        # This method is related to Employee logic, but doesn't need to know 
        # about a specific employee's name or the company name.
        weekend = ["Saturday", "Sunday"]
        return day not in weekend

def advanced_usage():
    print("\n--- Advanced Usage ---")
    day = "Monday"
    if Employee.is_workday(day):
        print(f"{day} is a work day.")
    else:
        print(f"{day} is the weekend!")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Using a static method when you need to access class variables.
class Config:
    timeout = 30
    
    @staticmethod
    def get_timeout():
        # return cls.timeout  # Error! cls is not defined
        return Config.timeout # Hardcoding the class name is bad practice. Use @classmethod instead.

# Best Practice: If a method doesn't use `self` and doesn't use `cls`, it should be a `@staticmethod`.
# Best Practice: If a static method gets too complex or independent, consider moving it out of the class to become a standalone module-level function.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: What is a static method in Python?
A: A method bound to a class that doesn't take an implicit first argument (like `self` or `cls`). It cannot access instance or class state.

Q2: How is it different from a class method?
A: A class method receives the class as the first argument (`cls`) and can modify class state. A static method does not receive `cls`.

Q3: Why use static methods?
A: To group utility functions within a class namespace when those functions logically belong to the class's domain but don't need to access its internal data.

Q4: Can an instance of a class call a static method?
A: Yes, static methods can be called on the class itself or on any instance of the class.

Q5: Should I use a static method or a module-level function?
A: If the function is conceptually tightly coupled to the class, use a static method. If it's a general-purpose utility, use a module-level function.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
"""
Exercise 1: Create a `TemperatureConverter` class with two static methods: `celsius_to_fahrenheit` and `fahrenheit_to_celsius`.
Exercise 2: Create a `Validator` class with a static method `is_valid_email(email: str)` that checks if an email contains an '@' symbol.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

class PasswordManager:
    
    @staticmethod
    def generate_strong_password() -> str:
        import random
        import string
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        return "".join(random.choice(chars) for _ in range(12))
        
    @staticmethod
    def check_strength(password: str) -> bool:
        if len(password) < 8:
            return False
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        return has_upper and has_digit

def mini_challenge():
    print("\n--- Mini Challenge ---")
    new_pwd = PasswordManager.generate_strong_password()
    print(f"Generated Password: {new_pwd}")
    print(f"Is strong? {PasswordManager.check_strength(new_pwd)}")
    
    weak_pwd = "password123"
    print(f"Is 'password123' strong? {PasswordManager.check_strength(weak_pwd)}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- Defined using the `@staticmethod` decorator.
- Do not take `self` or `cls` as arguments.
- Cannot modify object or class state.
- Used for utility functions that belong in a class's namespace conceptually.
"""

if __name__ == "__main__":
    basic_syntax_examples()
    practical_examples()
    advanced_usage()
    mini_challenge()
