"""
Topic: Multiple Inheritance and MRO
Chapter: 16
Level: Advanced

Description:
    Multiple inheritance allows a subclass to inherit from more than one parent class. 
    While powerful, it can lead to complexity, especially when multiple parent classes share 
    the same method names (the "Diamond Problem"). Python resolves this using the 
    Method Resolution Order (MRO).

Real-Life Analogy:
    A "Smartwatch" might inherit capabilities from both a "Watch" class (keeping time) 
    and a "Smartphone" class (receiving notifications). It is a hybrid of multiple parent types.

Key Concepts:
    - Inheriting from multiple classes
    - The Diamond Problem
    - Method Resolution Order (MRO) using C3 Linearization
    - The `__mro__` attribute and `mro()` method
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

class Flyer:
    def fly(self):
        return "Flying high!"

class Swimmer:
    def swim(self):
        return "Swimming deep!"

# Multiple Inheritance
class FlyingFish(Flyer, Swimmer):
    pass

def basic_syntax_examples():
    print("--- Basic Syntax ---")
    nemo = FlyingFish()
    # Inherits from both Flyer and Swimmer
    print(nemo.fly())
    print(nemo.swim())

# ============================================================
# SECTION 2: THE DIAMOND PROBLEM AND MRO
# ============================================================
# The Diamond Problem occurs when Class D inherits from Class B and Class C, 
# both of which inherit from Class A. Which version of a shared method does D get?

class A:
    def speak(self):
        print("A speaks")

class B(A):
    def speak(self):
        print("B speaks")

class C(A):
    def speak(self):
        print("C speaks")

class D(B, C):
    pass

def practical_examples():
    print("\n--- Practical Examples (MRO) ---")
    obj = D()
    # Which speak() will be called? B's or C's?
    obj.speak() 
    
    # Python searches from left to right in the inheritance list: D -> B -> C -> A -> object
    print("Method Resolution Order (MRO) for D:")
    for cls in D.__mro__:
        print(f" - {cls.__name__}")

# ============================================================
# SECTION 3: ADVANCED USAGE (SUPER() WITH MULTIPLE INHERITANCE)
# ============================================================

class Logger:
    def log(self, message):
        print(f"[LOG] {message}")

class DatabaseProcessor:
    def save(self):
        print("Saving to database...")

# Mixin Pattern: A class that provides methods to other classes but isn't considered a base class itself.
class LoggedProcessor(DatabaseProcessor, Logger):
    def save(self):
        self.log("Attempting to save")
        super().save() # Calls DatabaseProcessor.save() because of MRO
        self.log("Save successful")

def advanced_usage():
    print("\n--- Advanced Usage (Mixins) ---")
    processor = LoggedProcessor()
    processor.save()

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Conflicting `__init__` signatures in multiple inheritance
class Engine:
    def __init__(self, hp):
        self.hp = hp

class Radio:
    def __init__(self, brand):
        self.brand = brand

# class Car(Engine, Radio):
#     def __init__(self, hp, brand):
#         super().__init__(hp) # This will fail to pass 'brand' to Radio due to MRO complexities
        
# Best Practice: Avoid multiple inheritance of complex classes if possible. Prefer Composition.
# Best Practice: If using multiple inheritance, use the Mixin pattern where auxiliary classes 
# (Mixins) only provide specific functionality and don't maintain complex state (`__init__`).

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: Does Python support multiple inheritance?
A: Yes, a class can inherit from multiple parent classes (e.g., `class Child(Parent1, Parent2):`).

Q2: What is the Diamond Problem?
A: An ambiguity that arises when two classes B and C inherit from A, and class D inherits from both B and C. If there is a method in A that B and C have overridden, and D does not override it, which version does D inherit?

Q3: How does Python solve the Diamond Problem?
A: By using the Method Resolution Order (MRO) algorithm (specifically C3 Linearization). It searches left-to-right, depth-first, while ensuring no class is checked before its subclasses.

Q4: How can you view the MRO of a class?
A: By accessing the `__mro__` attribute or calling the `mro()` method on the class.

Q5: What is a Mixin?
A: A class designed to provide specific functionality to multiple other classes via multiple inheritance, without being meant for standalone instantiation.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
"""
Exercise 1: Create classes `Camera` and `Phone`. Create a `SmartPhone` that inherits from both.
Exercise 2: Add a `take_picture()` method to `Camera` and a `make_call()` to `Phone`. Call both from `SmartPhone`. Print the `__mro__` of `SmartPhone`.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

class Printer:
    def print_doc(self):
        print("Printing document...")

class Scanner:
    def scan_doc(self):
        print("Scanning document...")

class FaxMachine:
    def send_fax(self):
        print("Sending fax...")

# Multi-function device utilizing multiple inheritance
class MFD(Printer, Scanner, FaxMachine):
    def self_test(self):
        print("Running MFD Self-Test...")
        self.print_doc()
        self.scan_doc()
        self.send_fax()

def mini_challenge():
    print("\n--- Mini Challenge ---")
    office_machine = MFD()
    office_machine.self_test()
    print(MFD.mro())

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- Python supports inheriting from multiple parents.
- MRO determines the order Python searches for methods and attributes.
- Use `ClassName.__mro__` to debug inheritance hierarchies.
- Multiple inheritance should be used sparingly; prefer Mixins or Composition to avoid complexity.
"""

if __name__ == "__main__":
    basic_syntax_examples()
    practical_examples()
    advanced_usage()
    mini_challenge()
