"""
Topic: Class Methods
Chapter: 16
Level: Intermediate

Description:
    Class methods are methods that are bound to the class rather than its objects. They take 
    the class itself as the first parameter (commonly named `cls` instead of `self`). 
    They can access and modify class state that applies across all instances of the class.

Real-Life Analogy:
    If a class is a factory that makes cars (instances), regular instance methods are actions 
    on a specific car (honk the horn). A class method is an action on the factory itself, 
    like changing the total number of cars the factory is allowed to produce today, or 
    creating a car using a specific pre-set configuration.

Key Concepts:
    - The `@classmethod` decorator
    - The `cls` parameter
    - Alternative Constructors
    - Modifying class state
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

class Employee:
    # Class attribute
    company_name = "Tech Solutions Inc."
    
    def __init__(self, name: str):
        self.name = name
        
    @classmethod
    def change_company_name(cls, new_name: str):
        # cls refers to the Employee class itself
        cls.company_name = new_name
        print(f"Company name changed to {cls.company_name}")

def basic_syntax_examples():
    print("--- Basic Syntax ---")
    emp1 = Employee("Alice")
    emp2 = Employee("Bob")
    
    print(f"Before: emp1 company -> {emp1.company_name}")
    
    # Calling the class method on the class
    Employee.change_company_name("Global Tech Corp")
    
    # The change affects all instances because the class attribute was modified
    print(f"After: emp1 company -> {emp1.company_name}")
    print(f"After: emp2 company -> {emp2.company_name}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES (ALTERNATIVE CONSTRUCTORS)
# ============================================================
# The most common use case for class methods is creating alternative constructors.

class Date:
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day
        
    def display(self):
        print(f"{self.year}-{self.month:02d}-{self.day:02d}")
        
    @classmethod
    def from_string(cls, date_string: str):
        """Creates a Date object from a string format YYYY-MM-DD."""
        year, month, day = map(int, date_string.split('-'))
        # Return a new instance of the class
        return cls(year, month, day)

def practical_examples():
    print("\n--- Practical Examples (Alternative Constructors) ---")
    # Standard instantiation
    date1 = Date(2023, 10, 25)
    date1.display()
    
    # Using the class method as an alternative constructor
    date2 = Date.from_string("2024-01-15")
    date2.display()

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

class Counter:
    _count = 0  # Class attribute to keep track of instances
    
    def __init__(self):
        # We must use the class name or the class method to update it
        Counter.increment_count()
        
    @classmethod
    def increment_count(cls):
        cls._count += 1
        
    @classmethod
    def get_count(cls) -> int:
        return cls._count

def advanced_usage():
    print("\n--- Advanced Usage ---")
    print(f"Initial count: {Counter.get_count()}")
    
    c1 = Counter()
    c2 = Counter()
    c3 = Counter()
    
    print(f"Final count: {Counter.get_count()}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Using 'self' instead of 'cls' in a class method
class BadClass:
    @classmethod
    def bad_method(self): # Incorrect parameter name, confusing to read
        pass
        
# Best Practice: Always use `cls` as the first argument to a class method.
# Best Practice: Use class methods to provide factory functions (alternative constructors).

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: What is a class method?
A: A method bound to the class rather than an object. It can modify class state that applies across all instances.

Q2: What decorator is used to define a class method?
A: `@classmethod`

Q3: What is the first argument of a class method conventionally named?
A: `cls`, representing the class itself.

Q4: What is a common use case for class methods?
A: Creating alternative constructors (factory methods) to instantiate objects from different formats (e.g., parsing a string to create an object).

Q5: Can a class method access instance attributes?
A: No, because a class method does not have a reference to a specific instance (`self`). It can only access class-level attributes.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
"""
Exercise 1: Create a `User` class with a class attribute `active_users` (int). Increment it in `__init__`. Create a class method to return the active count.
Exercise 2: Add a class method `from_csv_row(cls, row_string)` to the `User` class that splits a string "username,email" and returns a `User` object.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

class Pizza:
    def __init__(self, ingredients: list):
        self.ingredients = ingredients
        
    def __str__(self):
        return f"Pizza with {', '.join(self.ingredients)}"
        
    @classmethod
    def margherita(cls):
        """Alternative constructor for Margherita."""
        return cls(["mozzarella", "tomatoes", "basil"])
        
    @classmethod
    def pepperoni(cls):
        """Alternative constructor for Pepperoni."""
        return cls(["mozzarella", "tomatoes", "pepperoni"])

def mini_challenge():
    print("\n--- Mini Challenge ---")
    # Custom pizza
    custom_pizza = Pizza(["mushrooms", "onions", "olives"])
    print(custom_pizza)
    
    # Factory methods
    classic = Pizza.margherita()
    meat_lovers = Pizza.pepperoni()
    
    print(classic)
    print(meat_lovers)

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- Defined using the `@classmethod` decorator.
- Take `cls` as the first parameter (the class itself).
- Can access and modify class-level attributes.
- Cannot access instance-level attributes (`self`).
- Excellent for creating alternative constructors (factory methods).
"""

if __name__ == "__main__":
    basic_syntax_examples()
    practical_examples()
    advanced_usage()
    mini_challenge()
