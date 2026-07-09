"""
Topic: Custom Modules
Chapter: 13
Level: Beginner

Description:
    While Python comes with a vast standard library, you will inevitably need to organize your own code.
    You can create custom modules simply by saving Python code in a `.py` file. These can then be imported
    into other scripts in the same directory (or path).

Real-Life Analogy:
    Think of custom modules as creating your own specialized toolboxes. You might have one toolbox for 
    plumbing (handling database connections) and another for electrical work (handling API requests). 
    You grab the toolbox you need when you need it.

Key Concepts:
    - Creating a `.py` file
    - Importing from local files
    - The `if __name__ == "__main__":` idiom
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# To create a custom module, just write some functions in a file, say `my_math.py`:
# def add(a, b): return a + b
#
# Then in another file:
# import my_math
# print(my_math.add(2, 3))

def mock_custom_module_function(text: str) -> str:
    """Mock function representing a custom module's functionality."""
    return text.upper()

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Example 1: Creating utility functions
def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculates final price after applying a discount."""
    return price * (1 - discount_percent / 100)

def format_currency(amount: float) -> str:
    """Formats a float as currency."""
    return f"${amount:,.2f}"

# Pretend these are in a separate `utils.py` module.
original_price = 1500.0
discount = 15.0
final = calculate_discount(original_price, discount)
print(f"Original: {format_currency(original_price)}, Final: {format_currency(final)}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# The __name__ attribute is crucial in custom modules.
# When a module is imported, __name__ is set to the module's name.
# When a module is run directly, __name__ is set to "__main__".

def test_module():
    """Function meant to be run only if the script is executed directly."""
    print("Testing custom module functionality...")
    assert calculate_discount(100, 10) == 90.0
    print("All tests passed.")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Circular imports. Module A imports Module B, and Module B imports Module A.
# Correction: Refactor the shared code into a third module, or move imports inside functions.

# Mistake 2: Putting executable code at the module level.
# If you put `print("Hello")` outside a function, it will print as soon as someone imports the module.
# Best Practice: Use `if __name__ == "__main__":` to guard executable code.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: How do you create a custom module?
# A: By saving Python code in a `.py` file. The filename (without .py) becomes the module name.

# Q2: What is the purpose of `if __name__ == "__main__":`?
# A: It prevents code block execution when the module is imported, allowing the file to be both 
#    a reusable module and a standalone script.

# Q3: How does Python find your custom module?
# A: Python searches in the current directory first, then in the directories listed in `sys.path`.

# Q4: Can a module contain classes?
# A: Yes, modules can contain functions, classes, variables, and executable statements.

# Q5: What happens if two modules have the same name in different directories?
# A: Python loads the first one it finds based on the order in `sys.path`.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Imagine creating a `string_utils.py` file with a function to reverse a string.
def reverse_string(s: str) -> str:
    return s[::-1]

# Exercise 2: Imagine importing it.
print(f"Reversed 'hello': {reverse_string('hello')}")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Create a mock module structure using functions.
# Create a dictionary representing an inventory.
# Write functions to add_item, remove_item, and display_inventory.

class InventoryModule:
    """Mock module for inventory management."""
    def __init__(self):
        self.inventory = {}
        
    def add_item(self, item: str, qty: int):
        self.inventory[item] = self.inventory.get(item, 0) + qty
        
    def remove_item(self, item: str, qty: int):
        if item in self.inventory:
            self.inventory[item] = max(0, self.inventory[item] - qty)
            
    def display(self):
        print("Inventory:")
        for item, qty in self.inventory.items():
            print(f"- {item}: {qty}")

def run_challenge():
    inv_mod = InventoryModule()
    inv_mod.add_item("Apple", 50)
    inv_mod.add_item("Banana", 30)
    inv_mod.remove_item("Apple", 10)
    inv_mod.display()

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Custom modules are just regular Python files.
# - They help organize code into logical, reusable components.
# - Use the `__name__ == "__main__"` idiom to allow files to be both imported and run standalone.
# - Watch out for circular dependencies when structuring your modules.

if __name__ == "__main__":
    print(mock_custom_module_function("hello modules"))
    test_module()
    run_challenge()
