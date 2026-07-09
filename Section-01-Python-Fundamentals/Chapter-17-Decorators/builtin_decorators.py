"""
Topic: Built-in Decorators
Chapter: 17
Level: Beginner

Description:
    Python comes with several built-in decorators that are commonly used in object-oriented programming. 
    The most frequently used are `@property`, `@classmethod`, and `@staticmethod`.

Real-Life Analogy:
    Imagine a company (Class).
    - Instance Method: A task an employee does (requires the specific employee).
    - @classmethod: A task the HR department does (requires the company itself).
    - @staticmethod: A task like a calculator on a desk (belongs to the company but doesn't require company resources to run).
    - @property: Asking for an employee's age, which is calculated on the fly rather than stored on paper.

Key Concepts:
    - `@property` for getters/setters.
    - `@classmethod` for methods that take `cls` as the first argument.
    - `@staticmethod` for methods that don't take `self` or `cls`.
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

class Circle:
    def __init__(self, radius):
        self._radius = radius

    # @property turns a method into a "getter" for a read-only attribute
    @property
    def radius(self):
        """Getter for radius."""
        return self._radius

    # This allows setting the attribute with validation
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

    @property
    def area(self):
        """Computed property. Calculated on the fly."""
        import math
        return math.pi * (self._radius ** 2)

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

class DateUtils:
    
    @staticmethod
    def is_weekend(day_number):
        """
        Static method. It doesn't need access to instance (self) or class (cls).
        It just logically belongs to DateUtils.
        """
        return day_number in [6, 7]

class Employee:
    company_name = "TechCorp"
    
    def __init__(self, name):
        self.name = name
        
    @classmethod
    def change_company_name(cls, new_name):
        """
        Class method. Takes 'cls' instead of 'self'.
        Can modify class state that applies to all instances.
        """
        cls.company_name = new_name
        
    @classmethod
    def from_string(cls, employee_string):
        """Class methods are often used as alternative constructors."""
        name = employee_string.strip()
        return cls(name)

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
        
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
        
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9
        
    @fahrenheit.deleter
    def fahrenheit(self):
        print("Deleting temperature...")
        del self._celsius

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Forgetting `@staticmethod` on a method that doesn't use `self`. 
# This causes Python to pass the instance as the first argument, resulting in a TypeError.

# Mistake: Using `@property` for operations that take a long time to compute or have side effects.
# Properties should feel like accessing a variable. Fast and side-effect free.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is the difference between @staticmethod and @classmethod?
# A1: A classmethod takes the class (`cls`) as its first argument and can access class attributes. A staticmethod takes neither `self` nor `cls` and behaves like a regular function placed inside a class for namespace organization.

# Q2: When would you use a classmethod?
# A2: When you need to modify class-level data or create alternative constructors (e.g., `dict.fromkeys()`).

# Q3: Why use @property instead of getter and setter methods like in Java?
# A3: It provides a cleaner syntax (`obj.x` instead of `obj.get_x()`) while still allowing encapsulated logic for validation or computation.

# Q4: Can you have a @property setter without a getter?
# A4: No, you must define the getter `@property` first, and then the setter `@name.setter`.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise: Create a `BankAccount` class with a `_balance` property.
# Add a getter and a setter that prevents setting a negative balance.

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance  # Uses the setter
        
    @property
    def balance(self):
        return self._balance
        
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = amount

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge: Combine these concepts. 
# Create a class `MathConfig` with a classmethod to change the default precision.
# Create a staticmethod to calculate a square root.

class MathConfig:
    precision = 2
    
    @classmethod
    def set_precision(cls, new_precision):
        cls.precision = new_precision
        
    @staticmethod
    def sqrt(number):
        return number ** 0.5
        
    @classmethod
    def format_result(cls, number):
        return f"{number:.{cls.precision}f}"

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - `@property`: Turns method into an attribute access. Good for encapsulation.
# - `@classmethod`: Receives `cls`. Good for alternative constructors.
# - `@staticmethod`: Receives nothing. Good for utility functions inside a class.

if __name__ == "__main__":
    print("--- Basic Syntax ---")
    c = Circle(5)
    print(f"Radius: {c.radius}")
    print(f"Area: {c.area:.2f}")
    c.radius = 10
    print(f"New Area: {c.area:.2f}")
    
    print("\n--- Practical Examples ---")
    print(f"Is 6 a weekend? {DateUtils.is_weekend(6)}")
    
    emp1 = Employee("Alice")
    Employee.change_company_name("MegaCorp")
    print(f"{emp1.name} works at {emp1.company_name}")
    
    emp2 = Employee.from_string("Bob ")
    print(f"Alternative constructor created: {emp2.name}")
    
    print("\n--- Advanced Usage ---")
    t = Temperature(0)
    print(f"0C in F: {t.fahrenheit}")
    t.fahrenheit = 212
    print(f"212F in C: {t._celsius}")
    
    print("\n--- Practice Exercises ---")
    acc = BankAccount(100)
    try:
        acc.balance = -50
    except ValueError as e:
        print(f"Error caught: {e}")
        
    print("\n--- Mini Challenge ---")
    result = MathConfig.sqrt(10)
    print(MathConfig.format_result(result))
    MathConfig.set_precision(4)
    print(MathConfig.format_result(result))
