"""
Topic: Polymorphism
Chapter: 16
Level: Intermediate

Description:
    Polymorphism (from Greek "many forms") allows objects of different classes to be treated 
    as objects of a common superclass. It provides a way to perform a single action in 
    different ways depending on the object invoking it.

Real-Life Analogy:
    Consider a universal remote control. Pressing the 'Power' button (the method) has a 
    different effect depending on the device (the object) it's pointed at. It might turn on 
    a TV, a DVD player, or a stereo system. The action is the same, but the behavior is polymorphic.

Key Concepts:
    - Duck Typing ("If it walks like a duck and quacks like a duck, it's a duck")
    - Method Overriding (Dynamic Polymorphism)
    - Operator Overloading (Polymorphism with built-in operators)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

class Bird:
    def fly(self):
        return "I can fly!"

class Penguin:
    # Notice this class doesn't inherit from Bird, but has the same method name
    def fly(self):
        return "I cannot fly, but I can swim!"

class Airplane:
    def fly(self):
        return "I fly using engines."

def let_it_fly(entity):
    # This function expects an object with a 'fly' method (Duck Typing)
    print(entity.fly())

def basic_syntax_examples():
    print("--- Basic Syntax ---")
    sparrow = Bird()
    tux = Penguin()
    jet = Airplane()
    
    # Polymorphism in action: calling the same function with different object types
    let_it_fly(sparrow)
    let_it_fly(tux)
    let_it_fly(jet)

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

import math

class Square:
    def __init__(self, side: float):
        self.side = side
        
    def calculate_area(self) -> float:
        return self.side ** 2

class Circle:
    def __init__(self, radius: float):
        self.radius = radius
        
    def calculate_area(self) -> float:
        return math.pi * (self.radius ** 2)

class Triangle:
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height
        
    def calculate_area(self) -> float:
        return 0.5 * self.base * self.height

def practical_examples():
    print("\n--- Practical Examples ---")
    shapes = [Square(4), Circle(3), Triangle(5, 6)]
    
    # Iterating through different objects and calling the same method name
    for shape in shapes:
        print(f"Area of {type(shape).__name__}: {shape.calculate_area():.2f}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Polymorphism with built-in functions
def advanced_usage():
    print("\n--- Advanced Usage (Built-in Polymorphism) ---")
    # The len() function is polymorphic
    print(f"Length of string: {len('hello')}")
    print(f"Length of list: {len([1, 2, 3, 4])}")
    print(f"Length of dictionary: {len({'a': 1, 'b': 2})}")

    # The '+' operator is polymorphic (Operator Overloading)
    print(f"Integer addition: {5 + 10}")
    print(f"String concatenation: {'Hello ' + 'World'}")
    print(f"List merging: {[1, 2] + [3, 4]}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Checking types explicitly instead of relying on duck typing
def bad_polymorphism(obj):
    if isinstance(obj, Square):
        return obj.calculate_area()
    elif isinstance(obj, Circle):
        return obj.calculate_area()
    # This defeats the purpose of polymorphism.

# Best Practice: Embrace duck typing in Python. Try calling the method and handle 
# the AttributeError if the object doesn't support it, or use abstract base classes (ABCs) 
# to enforce method implementation.

def good_polymorphism(obj):
    try:
        return obj.calculate_area()
    except AttributeError:
        print(f"{type(obj).__name__} does not have a calculate_area method.")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: What is polymorphism in Python?
A: Polymorphism allows different object classes to share the same method name, and those methods can behave differently based on the object calling them.

Q2: What is Duck Typing?
A: Duck typing is a concept where the type or class of an object is less important than the methods it defines. "If it walks like a duck and quacks like a duck, it must be a duck."

Q3: Does Python support method overloading (methods with same name but different signatures)?
A: No, Python does not support traditional method overloading. The last defined method overwrites previous ones. However, you can use default arguments or variable-length arguments (`*args`, `**kwargs`) to achieve similar behavior.

Q4: Give an example of built-in polymorphism in Python.
A: The `len()` function and the `+` operator.

Q5: Why is polymorphism useful?
A: It makes the code more flexible and easier to maintain. You can write generic code that works with any object that implements a required interface.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
"""
Exercise 1: Create classes `AudioFile`, `VideoFile`, and `ImageFile`. Each should have a `play()` method. Create a list of these files and loop through them, calling `play()`.
Exercise 2: Write a function that accepts any object and calls its `save()` method. Test it with different custom classes.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

class Notification:
    def send(self, message: str):
        raise NotImplementedError("Subclasses must implement this method")

class EmailNotification(Notification):
    def send(self, message: str):
        print(f"Sending Email: {message}")

class SMSNotification(Notification):
    def send(self, message: str):
        print(f"Sending SMS: {message}")

class PushNotification(Notification):
    def send(self, message: str):
        print(f"Sending Push Notification: {message}")

def notify_user(notifier: Notification, msg: str):
    notifier.send(msg)

def mini_challenge():
    print("\n--- Mini Challenge ---")
    notifiers = [EmailNotification(), SMSNotification(), PushNotification()]
    for notifier in notifiers:
        notify_user(notifier, "Your order has been shipped!")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- Polymorphism allows treating different objects uniformly.
- Python strongly relies on Duck Typing.
- Built-in functions like `len()` and operators like `+` exhibit polymorphic behavior.
- Polymorphism reduces the need for extensive `if/else` type checking.
"""

if __name__ == "__main__":
    basic_syntax_examples()
    practical_examples()
    advanced_usage()
    mini_challenge()
