"""
Topic: Composition vs Inheritance
Chapter: 16
Level: Advanced

Description:
    "Favor object composition over class inheritance."
    Inheritance models an "IS-A" relationship (a Car IS-A Vehicle). Composition models a 
    "HAS-A" relationship (a Car HAS-A Engine). Composition involves building complex objects 
    by combining simpler, independent objects. It often leads to more flexible and maintainable code.

Real-Life Analogy:
    Inheritance: A Smartphone is a Telephone. It's permanently tied to the Telephone blueprint.
    Composition: A PC has a CPU, RAM, and a hard drive. You can easily swap out the CPU 
    for a better one without redesigning the whole computer.

Key Concepts:
    - "IS-A" vs "HAS-A" relationships
    - Building classes with instances of other classes
    - Delegation (passing work from the main object to its components)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

class Engine:
    def start(self):
        return "Engine starting: Vroom!"

class Wheels:
    def roll(self):
        return "Wheels are rolling."

# Composition: Car HAS an Engine and HAS Wheels
class Car:
    def __init__(self):
        # The Car class is composed of instances of other classes
        self.engine = Engine()
        self.wheels = Wheels()
        
    def drive(self):
        # Delegation: The Car delegates the starting action to the Engine
        print(self.engine.start())
        print(self.wheels.roll())
        print("Car is moving.")

def basic_syntax_examples():
    print("--- Basic Syntax ---")
    my_car = Car()
    my_car.drive()

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES (FLEXIBILITY)
# ============================================================

# Why Composition is more flexible: We can inject different components easily.

class V8Engine:
    def start(self):
        return "V8 Engine ROARS!"

class ElectricMotor:
    def start(self):
        return "Electric motor whirs silently."

class Vehicle:
    # Dependency Injection: We pass the engine in, rather than hardcoding it
    def __init__(self, engine_type):
        self.engine = engine_type
        
    def start_vehicle(self):
        print(self.engine.start())

def practical_examples():
    print("\n--- Practical Examples ---")
    muscle_car = Vehicle(V8Engine())
    tesla = Vehicle(ElectricMotor())
    
    muscle_car.start_vehicle()
    tesla.start_vehicle()
    
    # We achieved vastly different behaviors without needing a massive inheritance tree!

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

class Logger:
    def log(self, msg):
        print(f"Log: {msg}")

class Database:
    def save(self, data):
        print(f"Saving {data} to database.")

class Application:
    # App is composed of a Logger and a Database
    def __init__(self, logger: Logger, db: Database):
        self.logger = logger
        self.db = db
        
    def process_data(self, data):
        self.logger.log("Starting data process.")
        self.db.save(data)
        self.logger.log("Data process complete.")

def advanced_usage():
    print("\n--- Advanced Usage ---")
    app = Application(Logger(), Database())
    app.process_data("User Profile")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Using inheritance when composition makes more sense
# E.g., `class User(DatabaseConnection):` -> A user is NOT a database connection. A user HAS a connection.

# Best Practice: Favor Composition over Inheritance. If you are deeply nesting inheritance 
# (e.g., more than 3 levels deep), you should probably be using composition. 
# Use inheritance only when the "IS-A" relationship is strict and behavior is shared fundamentally.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: What is the difference between Inheritance and Composition?
A: Inheritance is an "IS-A" relationship where a child class derives from a parent. Composition is a "HAS-A" relationship where a class contains instances of other classes.

Q2: Why is Composition often preferred over Inheritance?
A: It provides greater flexibility. You can swap components at runtime (like changing an engine type) without altering the class structure. It also prevents the rigid, deeply nested hierarchies that inheritance can cause.

Q3: What is Delegation?
A: When an object receives a request and forwards it to one of its component objects to do the actual work (e.g., `Car` asking `Engine` to `start()`).

Q4: Give an example where Inheritance is wrong but Composition is right.
A: `class Employee(List):` is wrong because an Employee IS NOT a List. `class Employee:` that HAS a `self.tasks = []` attribute is right.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
"""
Exercise 1: Create a `CPU` and `Memory` class. Create a `Computer` class composed of both.
Exercise 2: Write a `run_program()` method in `Computer` that delegates tasks to `CPU` and `Memory`.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

class Weapon:
    def __init__(self, name: str, damage: int):
        self.name = name
        self.damage = damage
        
    def attack(self):
        return f"swings {self.name} for {self.damage} damage!"

class Armor:
    def __init__(self, name: str, defense: int):
        self.name = name
        self.defense = defense

class Hero:
    # Hero is composed of a Weapon and Armor
    def __init__(self, name: str, weapon: Weapon, armor: Armor):
        self.name = name
        self.weapon = weapon
        self.armor = armor
        
    def battle_cry(self):
        print(f"{self.name} {self.weapon.attack()} (Defense: {self.armor.defense})")

def mini_challenge():
    print("\n--- Mini Challenge ---")
    sword = Weapon("Excalibur", 50)
    shield = Armor("Steel Shield", 20)
    
    knight = Hero("Arthur", sword, shield)
    knight.battle_cry()
    
    # Easy to swap components!
    knight.weapon = Weapon("Rusty Dagger", 5)
    knight.battle_cry()

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- Inheritance = "IS-A". Composition = "HAS-A".
- Composition builds complex classes using simpler components.
- It offers extreme flexibility through Dependency Injection.
- Reduces tight coupling compared to deep inheritance trees.
"""

if __name__ == "__main__":
    basic_syntax_examples()
    practical_examples()
    advanced_usage()
    mini_challenge()
