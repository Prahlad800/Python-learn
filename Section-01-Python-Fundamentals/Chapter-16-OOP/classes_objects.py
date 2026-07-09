"""
Topic: Classes and Objects
Chapter: 16
Level: Beginner

Description:
    Classes are the blueprints for creating objects. They encapsulate data (attributes) and 
    behavior (methods) into a single entity, forming the foundation of Object-Oriented Programming.

Real-Life Analogy:
    A class is like an architectural blueprint for a house. The blueprint defines the design, 
    but you can't live in it. When you build a house based on that blueprint, that physical house 
    is an object (or instance) of the class. You can build multiple houses (objects) from the same blueprint.

Key Concepts:
    - Class definition and `__init__` method
    - Instance attributes vs Class attributes
    - Instance methods and the `self` parameter
    - Object instantiation
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Defining a class using the 'class' keyword
class SimpleDog:
    # The __init__ method is the constructor, called when creating a new object
    def __init__(self, name: str, breed: str):
        # self refers to the instance being created
        # Instance attributes
        self.name = name
        self.breed = breed
        
    # Instance method
    def bark(self) -> str:
        return f"{self.name} says Woof!"

# Creating objects (instances) of the class
def basic_syntax_examples():
    print("--- Basic Syntax ---")
    dog1 = SimpleDog("Buddy", "Golden Retriever")
    dog2 = SimpleDog("Max", "German Shepherd")
    
    print(dog1.bark())
    print(f"Dog 2 is a {dog2.breed}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

class BankAccount:
    """A simple bank account class demonstrating attributes and methods."""
    
    # Class attribute - shared across all instances
    bank_name = "Global Trust Bank"
    
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount: float) -> None:
        """Deposits money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
            
    def withdraw(self, amount: float) -> bool:
        """Withdraws money if sufficient funds exist."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
            return True
        print("Insufficient funds or invalid amount.")
        return False
        
    def display_info(self) -> None:
        print(f"Account Owner: {self.owner}, Balance: ${self.balance:.2f}")

def practical_examples():
    print("\n--- Practical Examples ---")
    account = BankAccount("Alice Smith", 500.0)
    account.display_info()
    account.deposit(250.0)
    account.withdraw(100.0)
    
    # Accessing class attribute
    print(f"Bank Name: {BankAccount.bank_name}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

class DynamicProduct:
    """Demonstrates dynamic attribute creation and deletion."""
    
    def __init__(self, product_id: int, name: str):
        self.product_id = product_id
        self.name = name

def advanced_usage():
    print("\n--- Advanced Usage ---")
    prod = DynamicProduct(101, "Laptop")
    
    # Adding an attribute dynamically
    prod.price = 999.99
    print(f"Product {prod.name} costs ${prod.price}")
    
    # Using getattr and setattr
    setattr(prod, "stock", 50)
    print(f"Stock level: {getattr(prod, 'stock')}")
    
    # Deleting an attribute
    del prod.price
    # print(prod.price) # This would now raise an AttributeError

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Forgetting 'self' in method definition
class BadClass:
    def __init__(self, value):
        self.value = value
        
    # def print_value():  # TypeError: print_value() takes 0 positional arguments but 1 was given
    def print_value(self): # Corrected
        print(self.value)

# Best Practice: Use docstrings and type hints for clarity.
# Best Practice: Keep classes focused on a single responsibility.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: What is the difference between a class and an object?
A: A class is a template or blueprint, while an object is a specific instance of that class with actual data.

Q2: What is the purpose of the `self` keyword?
A: `self` represents the instance of the class. By using the `self` keyword, we can access the attributes and methods of the class in python.

Q3: What is the `__init__` method?
A: It is a special method (constructor) automatically called when a new object of a class is created. It's used to initialize the object's state.

Q4: Can we create a class without any methods?
A: Yes, you can use the `pass` statement to create an empty class. (e.g. `class Empty: pass`)

Q5: What are class attributes vs instance attributes?
A: Class attributes are shared by all instances of the class. Instance attributes are unique to each instance.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
"""
Exercise 1: Create a `Car` class with attributes `make`, `model`, and `year`. Add a method `start_engine()` that prints a message.
Exercise 2: Create a `Student` class with a list of grades. Add methods to `add_grade()` and `get_average()`.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

class LibraryBook:
    """A class to manage a library book."""
    
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_checked_out = False
        
    def check_out(self) -> None:
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"'{self.title}' has been checked out.")
        else:
            print(f"Sorry, '{self.title}' is already checked out.")
            
    def return_book(self) -> None:
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not checked out.")

def mini_challenge():
    print("\n--- Mini Challenge ---")
    book = LibraryBook("1984", "George Orwell")
    book.check_out()
    book.check_out() # Should indicate already checked out
    book.return_book()

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- Classes act as blueprints for objects.
- Objects are instances of classes.
- `__init__` initializes new objects.
- `self` binds attributes and methods to specific instances.
- Class attributes are shared, while instance attributes are unique to the object.
"""

if __name__ == "__main__":
    basic_syntax_examples()
    practical_examples()
    advanced_usage()
    mini_challenge()
