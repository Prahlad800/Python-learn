"""
Topic: Property Decorators (@property)
Chapter: 16
Level: Intermediate

Description:
    The `@property` decorator allows you to define methods that can be accessed like attributes. 
    It provides an elegant way to implement getters, setters, and deleters, allowing you to 
    encapsulate data and add validation logic without changing the public interface of your class.

Real-Life Analogy:
    Think of a digital thermostat. It displays the current temperature (an attribute). 
    When you turn the dial to change it, the thermostat silently runs complex logic to adjust 
    the HVAC system. You just interact with the "temperature" dial, but under the hood, 
    validation and mechanics are happening (the property setter).

Key Concepts:
    - `@property` (Getter)
    - `@attribute.setter` (Setter)
    - `@attribute.deleter` (Deleter)
    - Calculated/computed properties
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

class Circle:
    def __init__(self, radius: float):
        self._radius = radius
        
    # The property decorator turns this method into a getter
    @property
    def radius(self) -> float:
        return self._radius

    # The setter decorator binds to the property name
    @radius.setter
    def radius(self, value: float):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

def basic_syntax_examples():
    print("--- Basic Syntax ---")
    c = Circle(5)
    
    # Accessed like an attribute, not a method! (No parentheses)
    print(f"Radius is: {c.radius}")
    
    # Modified like an attribute! (Calls the setter method)
    c.radius = 10
    print(f"New radius is: {c.radius}")
    
    try:
        c.radius = -5 # This will trigger the ValueError in the setter
    except ValueError as e:
        print(f"Error: {e}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES (COMPUTED PROPERTIES)
# ============================================================

class Employee:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        
    @property
    def email(self) -> str:
        # A computed property. It doesn't exist as a physical attribute,
        # but is calculated dynamically based on other attributes.
        return f"{self.first_name.lower()}.{self.last_name.lower()}@company.com"
        
    @property
    def fullname(self) -> str:
        return f"{self.first_name} {self.last_name}"

def practical_examples():
    print("\n--- Practical Examples ---")
    emp = Employee("John", "Doe")
    
    # Accessing computed properties
    print(f"Name: {emp.fullname}")
    print(f"Email: {emp.email}")
    
    # If we change an underlying attribute, the computed property updates automatically
    emp.first_name = "Jane"
    print(f"New Name: {emp.fullname}")
    print(f"New Email: {emp.email}")

# ============================================================
# SECTION 3: ADVANCED USAGE (SETTERS AND DELETERS)
# ============================================================

class Person:
    def __init__(self, full_name: str):
        self.name = full_name # This will actually call the setter immediately!
        
    @property
    def name(self) -> str:
        return f"{self.first_name} {self.last_name}"
        
    @name.setter
    def name(self, value: str):
        # Allow setting the full name, but split it internally
        parts = value.split(' ')
        self.first_name = parts[0]
        self.last_name = parts[-1] if len(parts) > 1 else ""
        
    @name.deleter
    def name(self):
        print("Deleting Name!")
        self.first_name = None
        self.last_name = None

def advanced_usage():
    print("\n--- Advanced Usage ---")
    p = Person("Bruce Wayne")
    print(f"First: {p.first_name}, Last: {p.last_name}")
    
    p.name = "Clark Kent" # Calls setter
    print(f"First: {p.first_name}, Last: {p.last_name}")
    
    del p.name # Calls deleter
    print(f"First: {p.first_name}, Last: {p.last_name}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Infinite recursion in getters or setters
class BrokenClass:
    def __init__(self, value):
        self.value = value # Calls the setter
        
    @property
    def value(self):
        return self.value # ERROR! Calls itself recursively. Should be self._value
        
    @value.setter
    def value(self, val):
        self.value = val # ERROR! Calls itself recursively. Should be self._value = val

# Best Practice: The internal variable should have an underscore (e.g., `_value`) 
# to avoid infinite recursion with the property name (e.g., `value`).
# Best Practice: Use properties to refactor code later. Start with public attributes. 
# If you later need validation, convert them to properties without breaking APIs.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: What does the `@property` decorator do?
A: It transforms a method into an attribute-like getter. It allows you to access a method as if it were a regular attribute.

Q2: Why use `@property` instead of explicit getters and setters (e.g., `get_val()`)?
A: It provides a cleaner, more Pythonic syntax. You can add validation logic while keeping the dot notation (`obj.val`) interface intact.

Q3: What is a computed property?
A: A property that doesn't store data directly, but calculates its return value based on other attributes on the fly.

Q4: How do you define a setter for a property?
A: Using the `@property_name.setter` decorator over a method with the same name.

Q5: What happens if you define a `@property` but no setter, and try to assign a value to it?
A: Python will raise an `AttributeError: can't set attribute`. This makes the property effectively read-only.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
"""
Exercise 1: Create a `Product` class with a `price` property. Ensure the setter doesn't allow prices below 0.
Exercise 2: Create a `Rectangle` class with `width` and `height`. Add a read-only `@property` for `area`.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

class BankAccount:
    def __init__(self, initial_balance: float):
        self._balance = initial_balance
        
    @property
    def balance(self) -> float:
        return self._balance
        
    @balance.setter
    def balance(self, new_balance: float):
        if new_balance < 0:
            print("Alert: Overdraft protection active. Balance cannot be negative.")
        else:
            self._balance = new_balance

def mini_challenge():
    print("\n--- Mini Challenge ---")
    account = BankAccount(100)
    print(f"Current Balance: ${account.balance}")
    
    account.balance = 200
    print(f"Current Balance: ${account.balance}")
    
    account.balance = -50 # Should print alert and not change balance
    print(f"Current Balance: ${account.balance}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- `@property` creates a getter, allowing method access like an attribute.
- `@name.setter` allows defining validation logic for assignments.
- Computed properties calculate values dynamically.
- Read-only properties can be created by omitting the setter.
- Prevents breaking API changes when attributes need to be refactored into methods.
"""

if __name__ == "__main__":
    basic_syntax_examples()
    practical_examples()
    advanced_usage()
    mini_challenge()
