"""
Topic: Types of Methods (Instance, Class, Static)
Chapter: 16
Level: Intermediate

Description:
    Python classes support three main types of methods: Instance methods, Class methods, 
    and Static methods. Understanding the difference between them and when to use each 
    is crucial for designing well-structured object-oriented systems.

Real-Life Analogy:
    Imagine a Franchise Restaurant (the Class).
    - Instance Method: Cooking a meal for a specific customer. It depends on that customer's order (the object).
    - Class Method: Changing the corporate menu. It affects all restaurants in the franchise, not just one order.
    - Static Method: A clock on the restaurant wall. It provides a utility (time) but doesn't interact with the menu or the customers directly.

Key Concepts:
    - Instance Methods (`self`)
    - Class Methods (`cls`, `@classmethod`)
    - Static Methods (`@staticmethod`)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

class MyClass:
    
    # Instance Method (the default)
    def instance_method(self):
        return f"Instance method called. Has access to object state via {self}"
        
    # Class Method
    @classmethod
    def class_method(cls):
        return f"Class method called. Has access to class state via {cls}"
        
    # Static Method
    @staticmethod
    def static_method():
        return "Static method called. No access to object or class state."

def basic_syntax_examples():
    print("--- Basic Syntax ---")
    obj = MyClass()
    
    print(obj.instance_method())
    print(MyClass.class_method())
    print(MyClass.static_method())

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

class Pizza:
    radius = 12 # Class attribute (default size)
    
    def __init__(self, toppings):
        self.toppings = toppings # Instance attribute
        
    # INSTANCE METHOD: Modifies the specific object
    def add_topping(self, topping):
        self.toppings.append(topping)
        
    # CLASS METHOD: Modifies the class state (affects all future pizzas) or acts as a factory
    @classmethod
    def change_default_size(cls, new_radius):
        cls.radius = new_radius
        
    # STATIC METHOD: Utility function related to pizzas but independent of state
    @staticmethod
    def calculate_area(r):
        import math
        return math.pi * (r ** 2)

def practical_examples():
    print("\n--- Practical Examples ---")
    p1 = Pizza(["cheese"])
    p1.add_topping("pepperoni")
    print(f"P1 toppings: {p1.toppings}, Size: {p1.radius}")
    
    Pizza.change_default_size(14)
    p2 = Pizza(["mushrooms"])
    print(f"P2 toppings: {p2.toppings}, Size: {p2.radius}") # Size is now 14
    
    area = Pizza.calculate_area(p2.radius)
    print(f"P2 Area: {area:.2f}")

# ============================================================
# SECTION 3: ADVANCED USAGE (FACTORY PATTERN)
# ============================================================

class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        
    def __str__(self):
        return f"{self.name} - {self.role}"
        
    # Class methods are excellent for Alternative Constructors
    @classmethod
    def new_manager(cls, name):
        return cls(name, "Manager")
        
    @classmethod
    def new_developer(cls, name):
        return cls(name, "Developer")

def advanced_usage():
    print("\n--- Advanced Usage ---")
    emp1 = Employee.new_manager("Alice")
    emp2 = Employee.new_developer("Bob")
    print(emp1)
    print(emp2)

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Passing `self` to a `@staticmethod` or `cls` to an instance method without realizing what they mean.

# Best Practice Guide:
# 1. Do you need to access or modify the object's unique data (`self.name`)? -> Use an Instance Method.
# 2. Do you need to access or modify class-wide data (`cls.count`) or create a new instance? -> Use a Class Method.
# 3. Do you need neither object nor class data, but the logic belongs here conceptually? -> Use a Static Method.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: What is the main difference between an instance method and a class method?
A: An instance method takes `self` as the first argument and acts on a specific object. A class method takes `cls` as the first argument and acts on the class itself.

Q2: When should you use a static method?
A: When you have a utility function that logically belongs in the class namespace but does not require access to instance or class attributes.

Q3: Can you call a class method from an instance?
A: Yes, `obj.class_method()` works, but it's generally clearer to call it on the class itself `MyClass.class_method()`.

Q4: Can an instance method call a static method?
A: Yes, by using `self.static_method()` or `MyClass.static_method()`.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
"""
Exercise 1: Create a `Book` class. Use an instance method to `read_page()`, a class method to `set_publisher()`, and a static method to `is_valid_isbn(isbn)`.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

class User:
    active_users = 0
    
    def __init__(self, username):
        self.username = username
        User.active_users += 1
        
    def logout(self):
        User.active_users -= 1
        print(f"{self.username} logged out.")
        
    @classmethod
    def get_active_count(cls):
        return cls.active_users
        
    @staticmethod
    def validate_username(username):
        return len(username) >= 3 and username.isalnum()

def mini_challenge():
    print("\n--- Mini Challenge ---")
    if User.validate_username("a1"):
        u1 = User("a1")
    else:
        print("Invalid username format.")
        
    if User.validate_username("john_doe"):
        print("Valid, but _ is not alnum, wait...")
    
    if User.validate_username("alice123"):
        u2 = User("alice123")
        print("Created alice123")
        
    print(f"Active users: {User.get_active_count()}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- Instance Methods: Act on objects (`self`).
- Class Methods: Act on classes (`cls`), great for factories.
- Static Methods: Independent utilities grouped in the class namespace.
"""

if __name__ == "__main__":
    basic_syntax_examples()
    practical_examples()
    advanced_usage()
    mini_challenge()
