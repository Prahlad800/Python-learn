"""
Topic: OOP Practice
Chapter: 16
Level: Intermediate

Description:
    This file provides a comprehensive set of practice exercises combining various OOP concepts: 
    Classes, Objects, Inheritance, Encapsulation, and Polymorphism. It serves as a practical 
    review of the chapter.

Real-Life Analogy:
    Reading about how to ride a bike is different from actually riding one. This file is your 
    training ground to practice balancing and pedaling with Python's OOP tools.

Key Concepts:
    - Bringing all OOP concepts together
    - System design and modeling
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================
# Practice: Define a basic class

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_read = False
        
    def mark_as_read(self):
        self.is_read = True
        
    def __str__(self):
        status = "Read" if self.is_read else "Unread"
        return f"'{self.title}' by {self.author} ({status})"

def basic_syntax_examples():
    print("--- Practice: Basic Class ---")
    b = Book("Dune", "Frank Herbert")
    print(b)
    b.mark_as_read()
    print(b)

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================
# Practice: Inheritance and Method Overriding

class Employee:
    def __init__(self, name: str, base_salary: float):
        self.name = name
        self.base_salary = base_salary
        
    def calculate_pay(self) -> float:
        return self.base_salary

class CommissionEmployee(Employee):
    def __init__(self, name: str, base_salary: float, commission: float):
        super().__init__(name, base_salary)
        self.commission = commission
        
    def calculate_pay(self) -> float:
        return self.base_salary + self.commission

def practical_examples():
    print("\n--- Practice: Inheritance ---")
    e1 = Employee("Alice", 5000)
    e2 = CommissionEmployee("Bob", 3000, 2500)
    
    print(f"{e1.name} Pay: ${e1.calculate_pay()}")
    print(f"{e2.name} Pay: ${e2.calculate_pay()}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================
# Practice: Encapsulation and Properties

class TemperatureSensor:
    def __init__(self):
        self.__temp_celsius = 0.0
        
    @property
    def celsius(self):
        return self.__temp_celsius
        
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is impossible.")
        self.__temp_celsius = value
        
    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32

def advanced_usage():
    print("\n--- Practice: Encapsulation ---")
    sensor = TemperatureSensor()
    sensor.celsius = 25
    print(f"C: {sensor.celsius}, F: {sensor.fahrenheit}")
    try:
        sensor.celsius = -300
    except ValueError as e:
        print(f"Error caught: {e}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================
# Practice: Checking types correctly
# Mistake: Using type(obj) == Class for inheritance checks.
# Best Practice: Use isinstance() to respect polymorphism.

def process_employee(emp):
    if isinstance(emp, Employee):
        print(f"Processing pay for {emp.name}: ${emp.calculate_pay()}")
    else:
        print("Not an employee object.")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
This section is for self-review. Ensure you can explain:
1. The 4 pillars of OOP (Encapsulation, Abstraction, Inheritance, Polymorphism).
2. The difference between `__init__` and `__new__` (advanced).
3. How Python handles multiple inheritance (MRO).
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
"""
Exercise: Create a `BankAccount` system.
- Base class `Account` with `deposit` and `withdraw`.
- Subclass `SavingsAccount` that adds interest.
- Subclass `CheckingAccount` that allows overdrafts up to a limit.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = []
        
    def add(self, product: Product):
        self.items.append(product)
        print(f"Added {product.name} to cart.")
        
    def total(self):
        return sum(item.price for item in self.items)

def mini_challenge():
    print("\n--- Mini Challenge: E-commerce ---")
    p1 = Product("Laptop", 1200)
    p2 = Product("Mouse", 25)
    
    cart = Cart()
    cart.add(p1)
    cart.add(p2)
    print(f"Total: ${cart.total()}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- Practice makes perfect.
- Modeling real-world objects helps solidify OOP concepts.
- Always consider if Composition is better than Inheritance.
- Protect data using Encapsulation (@property).
"""

if __name__ == "__main__":
    basic_syntax_examples()
    practical_examples()
    advanced_usage()
    mini_challenge()
