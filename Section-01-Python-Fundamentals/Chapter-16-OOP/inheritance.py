"""
Topic: Inheritance
Chapter: 16
Level: Beginner

Description:
    Inheritance is a fundamental concept in Object-Oriented Programming where a new class 
    (child/subclass) derives properties and behaviors from an existing class (parent/superclass). 
    It promotes code reusability and establishes a logical hierarchy.

Real-Life Analogy:
    Think of a family tree. A child inherits characteristics (like eye color or height) from 
    their parents. In programming, a 'Car' class can inherit basic properties (wheels, engine) 
    from a broader 'Vehicle' class, while adding its own specific features (AC, radio).

Key Concepts:
    - Parent Class (Superclass) and Child Class (Subclass)
    - Method Overriding
    - The `super()` function
    - `isinstance()` and `issubclass()` built-in functions
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Parent Class
class Animal:
    def __init__(self, name: str):
        self.name = name
        
    def speak(self) -> str:
        return "Some generic animal sound"
        
    def eat(self) -> str:
        return f"{self.name} is eating."

# Child Class inheriting from Animal
class Dog(Animal):
    # Method overriding: redefining the parent's method
    def speak(self) -> str:
        return "Woof!"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"

def basic_syntax_examples():
    print("--- Basic Syntax ---")
    generic_animal = Animal("Creature")
    dog = Dog("Rex")
    cat = Cat("Whiskers")
    
    print(f"Animal says: {generic_animal.speak()}")
    print(f"Dog says: {dog.speak()} and {dog.eat()}") # Inherited eat() method
    print(f"Cat says: {cat.speak()}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

class Employee:
    """Base class for all employees."""
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        
    def get_details(self) -> str:
        return f"Employee: {self.name}, Salary: ${self.salary}"

class Manager(Employee):
    """Subclass representing a manager, utilizing super()."""
    def __init__(self, name: str, salary: float, department: str):
        # Call the parent class's __init__ method using super()
        super().__init__(name, salary)
        self.department = department
        
    def get_details(self) -> str:
        # Extend the parent method's functionality
        base_details = super().get_details()
        return f"{base_details}, Department: {self.department}"

def practical_examples():
    print("\n--- Practical Examples ---")
    emp = Employee("John Doe", 50000)
    mgr = Manager("Jane Smith", 80000, "Engineering")
    
    print(emp.get_details())
    print(mgr.get_details())
    
    # Checking inheritance relationships
    print(f"Is mgr an Employee? {isinstance(mgr, Employee)}")
    print(f"Is Manager a subclass of Employee? {issubclass(Manager, Employee)}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        
    def area(self) -> float:
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
        import math
        self.math = math
        
    def area(self) -> float:
        return self.math.pi * (self.radius ** 2)

def advanced_usage():
    print("\n--- Advanced Usage ---")
    shapes = [Rectangle(4, 5), Circle(3)]
    for shape in shapes:
        print(f"Area of {shape.__class__.__name__}: {shape.area():.2f}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Forgetting to call super().__init__() when overriding __init__
class BrokenManager(Employee):
    def __init__(self, name: str, salary: float, department: str):
        # Missing super().__init__(name, salary)
        self.department = department
        # This will fail if we try to access self.name

# Best Practice: Always use `super()` instead of naming the parent class explicitly 
# (e.g., `Employee.__init__(self, name, salary)`) to support multiple inheritance properly.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: What is inheritance in Python?
A: Inheritance allows a class (subclass) to acquire the properties and methods of another class (superclass).

Q2: What is method overriding?
A: It is a feature that allows a subclass to provide a specific implementation of a method that is already provided by its superclass.

Q3: What does the `super()` function do?
A: `super()` returns a proxy object that allows you to refer to parent class by invoking its methods and avoiding explicit base class names.

Q4: Does Python support multiple inheritance?
A: Yes, a Python class can inherit from multiple parent classes.

Q5: What is the difference between `isinstance()` and `type()`?
A: `isinstance(obj, Class)` checks if an object is an instance of a class OR any of its subclasses. `type(obj) == Class` only checks for the exact class, ignoring inheritance.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
"""
Exercise 1: Create a `Vehicle` parent class and `Car` / `Motorcycle` subclasses. Implement overriding for a `honk()` method.
Exercise 2: Create a `Person` class and a `Student` subclass. Use `super()` in the `Student`'s `__init__` to handle the `name` and `age` attributes.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

class Device:
    def __init__(self, brand: str):
        self.brand = brand
        self.is_on = False
        
    def turn_on(self):
        self.is_on = True
        print(f"{self.brand} device turned on.")

class Smartphone(Device):
    def __init__(self, brand: str, model: str):
        super().__init__(brand)
        self.model = model
        
    def call(self, number: str):
        if self.is_on:
            print(f"Calling {number} from {self.brand} {self.model}...")
        else:
            print("Cannot call, device is off.")

def mini_challenge():
    print("\n--- Mini Challenge ---")
    phone = Smartphone("Apple", "iPhone 14")
    phone.call("555-1234")
    phone.turn_on()
    phone.call("555-1234")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- Inheritance allows reusing code from a parent class.
- Subclasses can override parent methods to provide specific behavior.
- `super()` is used to call methods (especially `__init__`) of the parent class.
- Built-in functions like `isinstance()` and `issubclass()` help navigate class hierarchies.
"""

if __name__ == "__main__":
    basic_syntax_examples()
    practical_examples()
    advanced_usage()
    mini_challenge()
