"""
Topic: Encapsulation
Chapter: 16
Level: Intermediate

Description:
    Encapsulation is the bundling of data (attributes) and methods that operate on that data 
    into a single unit (a class). More importantly, it involves restricting direct access to 
    some of the object's components to prevent unintended modification, often referred to as data hiding.

Real-Life Analogy:
    A capsule of medicine. The chemicals are hidden inside the shell. You swallow the capsule, 
    but you don't interact directly with the raw chemicals. Similarly, a car's engine is hidden 
    under the hood; you use the steering wheel and pedals (the public interface) rather than 
    tinkering with the pistons directly.

Key Concepts:
    - Public attributes (accessible from anywhere)
    - Protected attributes (denoted by `_prefix`, convention only)
    - Private attributes (denoted by `__prefix`, name mangling applied)
    - Getter and Setter methods
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

class Safe:
    def __init__(self):
        self.public_item = "Public Info"
        self._protected_item = "Protected Info (Convention)"
        self.__private_item = "Private Info (Name Mangled)"

def basic_syntax_examples():
    print("--- Basic Syntax ---")
    my_safe = Safe()
    
    # Public: Accessible directly
    print(my_safe.public_item)
    
    # Protected: Accessible, but convention says "don't touch"
    print(my_safe._protected_item) 
    
    # Private: Direct access raises AttributeError
    try:
        print(my_safe.__private_item)
    except AttributeError as e:
        print(f"Error accessing private member: {e}")
        
    # How to access private attributes (Name Mangling)
    # Python renames it to _ClassName__AttributeName
    print(my_safe._Safe__private_item)

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

class BankAccount:
    """Demonstrating encapsulation with getters and setters."""
    def __init__(self, owner: str, initial_balance: float):
        self.owner = owner
        # Encapsulate the balance
        self.__balance = initial_balance
        
    # Getter method
    def get_balance(self) -> float:
        return self.__balance
        
    # Setter method with validation
    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")
            
    def withdraw(self, amount: float):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")

def practical_examples():
    print("\n--- Practical Examples ---")
    acc = BankAccount("Alice", 1000)
    
    # We cannot directly modify the balance
    # acc.__balance = 5000000  # This creates a new variable, doesn't change internal balance
    
    # We must use the provided public methods
    acc.deposit(500)
    acc.withdraw(200)
    print(f"Current Balance: ${acc.get_balance()}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

class UserProfile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.__password = password # Private
        
    def check_password(self, pwd_attempt: str) -> bool:
        return self.__password == pwd_attempt
        
    def change_password(self, old_pwd: str, new_pwd: str):
        if self.check_password(old_pwd):
            if len(new_pwd) >= 8:
                self.__password = new_pwd
                print("Password successfully updated.")
            else:
                print("New password must be at least 8 characters.")
        else:
            print("Authentication failed. Cannot change password.")

def advanced_usage():
    print("\n--- Advanced Usage ---")
    user = UserProfile("admin", "secure123")
    user.change_password("wrongpass", "newpass123")
    user.change_password("secure123", "short")
    user.change_password("secure123", "better_password!")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Relying on name mangling for absolute security
# Python's encapsulation is based on convention and name mangling, not strict access control 
# like Java or C++. Malicious or poorly written code can still access private members.

# Best Practice: Use `_` for internal variables to signal to other developers that the 
# attribute is not part of the public API. Use `__` only when you need to avoid naming 
# collisions in subclasses.
# Best Practice: Use the `@property` decorator (covered in a later file) instead of 
# explicit get_x() and set_x() methods for cleaner syntax.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: What is encapsulation?
A: Encapsulation is the bundling of data and methods into a class and restricting direct access to the internal data.

Q2: How do you make an attribute private in Python?
A: By prefixing the attribute name with double underscores (`__`).

Q3: Is true data hiding possible in Python?
A: No, Python does not have strict access modifiers like `private` or `protected` in Java. It uses name mangling (`_ClassName__attribute`) to make it harder to accidentally access, but it can still be accessed directly if known.

Q4: What is name mangling?
A: The mechanism where the Python interpreter changes the name of variables starting with `__` to include the class name, preventing accidental overriding in subclasses.

Q5: Why should we use getters and setters?
A: They allow you to add validation logic before changing an attribute and control how an attribute is accessed.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
"""
Exercise 1: Create a `Thermostat` class with a private `__temperature` attribute. Provide a setter that ensures the temperature stays between 50 and 90 degrees Fahrenheit.
Exercise 2: Create a `Employee` class with public name, protected department, and private salary. Add a method to calculate an annual bonus based on the private salary.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

class ShoppingCart:
    def __init__(self):
        self.__items = {} # Private dictionary of item: price
        
    def add_item(self, item_name: str, price: float):
        if price >= 0:
            self.__items[item_name] = price
            print(f"Added {item_name} for ${price}")
        else:
            print("Price cannot be negative.")
            
    def get_total(self) -> float:
        return sum(self.__items.values())
        
    def display_cart(self):
        print("Cart Contents:")
        for item, price in self.__items.items():
            print(f"- {item}: ${price}")

def mini_challenge():
    print("\n--- Mini Challenge ---")
    cart = ShoppingCart()
    cart.add_item("Apple", 1.50)
    cart.add_item("Bread", 3.00)
    cart.add_item("Error", -5.00) # Should fail
    cart.display_cart()
    print(f"Total: ${cart.get_total()}")
    
    # cart.__items is hidden from direct access

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- Encapsulation hides the internal state of an object.
- `_` prefix implies an attribute is protected (internal use).
- `__` prefix triggers name mangling, making the attribute 'private'.
- Use getters and setters to validate and control access to internal state.
"""

if __name__ == "__main__":
    basic_syntax_examples()
    practical_examples()
    advanced_usage()
    mini_challenge()
