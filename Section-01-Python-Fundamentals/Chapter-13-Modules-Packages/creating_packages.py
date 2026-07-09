"""
Topic: Creating Packages
Chapter: 13
Level: Intermediate

Description:
    A Python package is simply a directory containing multiple Python modules (files) and a special 
    `__init__.py` file. Packages allow you to organize your modules hierarchically, making large 
    codebases easier to manage and distribute.

Real-Life Analogy:
    If a module is a single toolbox, a package is a large cabinet with many drawers (sub-packages) 
    and smaller toolboxes (modules) inside. The `__init__.py` file is the label on the cabinet 
    that tells Python it's an organized toolbox collection, not just a random pile of boxes.

Key Concepts:
    - Directories as packages
    - __init__.py file
    - Dot notation for imports
    - Relative vs. Absolute imports
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# To create a package named `ecommerce`, you create a folder structure like this:
#
# ecommerce/
# ├── __init__.py
# ├── products.py
# ├── payments.py
# └── users/
#     ├── __init__.py
#     └── authentication.py

# In another file, you import using dot notation:
# import ecommerce.products
# from ecommerce.payments import process_payment

def simulate_package_structure():
    """Mocks how a package might look conceptually."""
    print("Conceptual Package Structure:")
    print("my_package/")
    print("  __init__.py")
    print("  module_a.py")
    print("  module_b.py")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Let's mock the behavior of importing from a package.

class MockPaymentsModule:
    @staticmethod
    def process(amount: float):
        print(f"Processing payment of ${amount:.2f}")

class MockProductsModule:
    @staticmethod
    def list_products():
        print("Listing all products...")

# Simulating `from ecommerce import payments, products`
ecommerce_payments = MockPaymentsModule()
ecommerce_products = MockProductsModule()

ecommerce_products.list_products()
ecommerce_payments.process(49.99)

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# The __init__.py file
# - In older Python versions, it was required.
# - In Python 3.3+, folders without it are "Namespace Packages", but regular packages still use it.
# - It's executed when the package is imported. You can use it to initialize state or simplify imports.

# E.g., inside ecommerce/__init__.py:
# from .payments import process_payment
# This allows: `from ecommerce import process_payment` directly.

def explain_init_py():
    """Explains the role of __init__.py"""
    role = (
        "The __init__.py file can be empty, or it can contain initialization code "
        "for the package, and set the __all__ variable to control what is imported "
        "with 'from package import *'."
    )
    print(role)

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Confusing relative and absolute imports.
# Absolute: `from ecommerce.users import auth`
# Relative: `from .users import auth` (used inside the package itself)
# Relative imports can fail if you run a script directly within the package instead of importing it.

# Best Practice: Keep __init__.py mostly empty unless you are explicitly defining a public API 
# for your package using `__all__` or exposing key functions at the package level.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What makes a directory a Python package?
# A: Primarily, the presence of an `__init__.py` file (though Python 3.3+ introduced namespace packages).

# Q2: What is the purpose of `__init__.py`?
# A: It indicates that the directory is a Python package, and it can contain initialization code or 
#    define the package's public API.

# Q3: What is the difference between a module and a package?
# A: A module is a single `.py` file. A package is a directory of modules.

# Q4: Explain `from . import sibling_module`.
# A: This is a relative import. It imports `sibling_module` from the same directory as the current file.

# Q5: What does the `__all__` list do in an `__init__.py` file?
# A: It defines a list of module names that should be imported when a user does `from package import *`.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise: Write a pseudo-script that simulates an `__init__.py` file that gathers 
# functions from submodules to create a clean public API.

def mock_submodule_a(): return "Data A"
def mock_submodule_b(): return "Data B"

# Inside __init__.py
__all__ = ["get_all_data"]

def get_all_data():
    return f"{mock_submodule_a()} and {mock_submodule_b()}"

print(f"Calling package level function: {get_all_data()}")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Create a class that acts as a "Package Builder" to conceptually demonstrate building a package.
# It should store a package name, and a list of modules.

class PackageBuilder:
    def __init__(self, name: str):
        self.name = name
        self.modules = []
        
    def add_module(self, module_name: str):
        self.modules.append(module_name)
        
    def build(self):
        print(f"Building package '{self.name}'...")
        print(f"- Creating {self.name}/__init__.py")
        for mod in self.modules:
            print(f"- Creating {self.name}/{mod}.py")
        print("Package build complete.")

def run_challenge():
    builder = PackageBuilder("data_pipeline")
    builder.add_module("extract")
    builder.add_module("transform")
    builder.add_module("load")
    builder.build()

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Packages are directories containing modules.
# - They use `__init__.py` to declare themselves as packages.
# - They are imported using dot notation (`package.module`).
# - `__init__.py` can be used to flatten the namespace for easier importing.

if __name__ == "__main__":
    simulate_package_structure()
    explain_init_py()
    run_challenge()
