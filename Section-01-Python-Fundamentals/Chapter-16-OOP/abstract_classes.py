"""
Topic: Abstract Classes (ABC)
Chapter: 16
Level: Advanced

Description:
    Abstract Base Classes (ABCs) provide a blueprint for other classes. They define a common 
    interface but leave the implementation to their subclasses. You cannot instantiate an 
    abstract class directly. They enforce that derived classes must implement specific methods.

Real-Life Analogy:
    Think of a generic "Vehicle" concept. You can't go to a dealership and buy a generic "Vehicle". 
    You buy a specific implementation: a Car, a Truck, or a Motorcycle. The "Vehicle" blueprint 
    mandates that every specific vehicle must have a `start_engine()` method, but each type 
    implements that engine start differently.

Key Concepts:
    - The `abc` module (`ABC`, `abstractmethod`)
    - Preventing direct instantiation
    - Enforcing method implementation in subclasses
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

from abc import ABC, abstractmethod

# Abstract Base Class inherits from ABC
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        """Must be implemented by subclasses."""
        pass
        
    @abstractmethod
    def perimeter(self):
        """Must be implemented by subclasses."""
        pass
        
    # Normal methods are also allowed in ABCs
    def display_info(self):
        print(f"I am a {type(self).__name__}")

class Square(Shape):
    def __init__(self, side: float):
        self.side = side
        
    def area(self) -> float:
        return self.side ** 2
        
    def perimeter(self) -> float:
        return self.side * 4

def basic_syntax_examples():
    print("--- Basic Syntax ---")
    # shape = Shape()  # TypeError: Can't instantiate abstract class with abstract methods
    
    sq = Square(5)
    sq.display_info()
    print(f"Area: {sq.area()}, Perimeter: {sq.perimeter()}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

class DataProcessor(ABC):
    
    @abstractmethod
    def read_data(self):
        pass
        
    @abstractmethod
    def process_data(self):
        pass
        
    # Template Method Pattern: Defines the skeleton of an algorithm
    def run_pipeline(self):
        print("Starting pipeline...")
        data = self.read_data()
        result = self.process_data(data)
        print(f"Pipeline finished. Result: {result}")

class CSVProcessor(DataProcessor):
    def read_data(self):
        return "row1,row2,row3"
        
    def process_data(self, data):
        return data.split(',')

def practical_examples():
    print("\n--- Practical Examples ---")
    processor = CSVProcessor()
    processor.run_pipeline()

# ============================================================
# SECTION 3: ADVANCED USAGE (ABSTRACT PROPERTIES)
# ============================================================

class Animal(ABC):
    
    @property
    @abstractmethod
    def diet(self):
        """Subclasses must define this property."""
        pass

class Lion(Animal):
    @property
    def diet(self):
        return "Carnivore"

def advanced_usage():
    print("\n--- Advanced Usage ---")
    simba = Lion()
    print(f"Simba is a {simba.diet}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Forgetting to inherit from ABC
class FakeAbstract:
    @abstractmethod
    def do_something(self):
        pass
# You can still instantiate FakeAbstract because it doesn't inherit from ABC!

# Best Practice: Always inherit from `abc.ABC` when creating abstract classes.
# Best Practice: Use ABCs to define strict interfaces for plugins or complex systems where 
# multiple developers are creating subclasses and must adhere to a specific structure.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: What is an Abstract Base Class (ABC)?
A: A class that cannot be instantiated and is designed to be subclassed. It defines a blueprint for subclasses.

Q2: How do you create an abstract method in Python?
A: By importing `abstractmethod` from the `abc` module and using it as a decorator `@abstractmethod`. The class itself must also inherit from `abc.ABC`.

Q3: What happens if a subclass fails to implement an abstract method?
A: Python will raise a `TypeError` when you attempt to instantiate that subclass.

Q4: Can an abstract class have concrete (normal) methods?
A: Yes. An ABC can provide shared concrete methods while forcing subclasses to implement other specific abstract methods.

Q5: Can you decorate a property as abstract?
A: Yes, you can stack `@property` and `@abstractmethod` decorators to force subclasses to implement a specific property.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
"""
Exercise 1: Create an ABC `PaymentGateway` with an abstract method `process_payment(amount)`.
Exercise 2: Create subclasses `StripeGateway` and `PayPalGateway` that implement the method. Try instantiating a class that misses the implementation to see the error.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

class NotificationService(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str):
        pass
        
class EmailService(NotificationService):
    def send(self, recipient: str, message: str):
        print(f"Emailing {recipient}: {message}")
        
class SMSService(NotificationService):
    def send(self, recipient: str, message: str):
        print(f"Texting {recipient}: {message}")

def notify_all(service: NotificationService, users: list, msg: str):
    for user in users:
        service.send(user, msg)

def mini_challenge():
    print("\n--- Mini Challenge ---")
    users = ["alice@example.com", "bob@example.com"]
    email_sys = EmailService()
    
    notify_all(email_sys, users, "Server going down in 5 mins!")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- Import `ABC` and `abstractmethod` from the `abc` module.
- Abstract classes cannot be instantiated directly.
- They enforce a strict contract: subclasses MUST implement all abstract methods.
- Useful for large architectures and defining clear interfaces.
"""

if __name__ == "__main__":
    basic_syntax_examples()
    practical_examples()
    advanced_usage()
    mini_challenge()
