"""
Topic: Docstrings
Chapter: 7
Level: Beginner

Description:
    Docstrings (documentation strings) are string literals that appear right after the definition of a function, method, class, or module. They are used to explain what the code does, making it easier for others (and yourself) to understand and use it later.

Real-Life Analogy:
    A docstring is like an instruction manual included inside the box of a new gadget. It tells you what the gadget does, what buttons to press (arguments), and what to expect when it turns on (return values).

Key Concepts:
    - Triple quotes (\"\"\" or ''')
    - Standard conventions (PEP 257)
    - Accessing docstrings via `__doc__` or `help()`
    - Google, NumPy, and Sphinx docstring styles
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def simple_function():
    """This is a simple one-line docstring."""
    pass

print("--- Section 1 ---")
# Accessing the docstring programmatically
print(f"Docstring of simple_function:\n{simple_function.__doc__}")

# Multi-line docstring
def complex_function(name):
    """
    This is a summary of the function.
    
    This function takes a name and does absolutely nothing with it.
    It is just an example to demonstrate multi-line docstrings.
    """
    pass

print(f"\nDocstring of complex_function:\n{complex_function.__doc__}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES (DOCSTRING FORMATS)
# ============================================================

# While you can write whatever you want in a docstring, standard formats are preferred.

# Example 1: Google Style (Very common and readable)
def fetch_data(url: str, timeout: int = 10) -> dict:
    """
    Fetches JSON data from a given URL.

    Args:
        url (str): The URL to fetch data from.
        timeout (int, optional): Seconds to wait before timing out. Defaults to 10.

    Returns:
        dict: The parsed JSON data as a dictionary.

    Raises:
        ConnectionError: If the server cannot be reached.
    """
    return {"status": "success", "data": []}

# Example 2: NumPy / SciPy Style (Great for extensive documentation)
def calculate_velocity(distance, time):
    """
    Calculates velocity given distance and time.

    Parameters
    ----------
    distance : float
        The distance traveled in meters.
    time : float
        The time taken in seconds.

    Returns
    -------
    float
        The calculated velocity in m/s.
    """
    return distance / time if time > 0 else 0.0

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

print("\n--- Section 3 ---")

# Using the built-in help() function
# help() parses the docstrings and formats them nicely for the terminal.
# Uncomment the line below to see it in action:
# help(fetch_data)

# Documenting Modules and Classes
# You can also put docstrings at the very top of a file, or under a class definition.

class Robot:
    """
    A class representing a simple Robot.
    
    Attributes:
        name (str): The name of the robot.
    """
    
    def __init__(self, name):
        """Initializes the Robot with a name."""
        self.name = name

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Using # comments instead of docstrings for function documentation
def bad_func():
    # This function does XYZ. (WRONG! This is just a comment)
    # help(bad_func) will not show this comment.
    pass

# Mistake 2: Missing the summary line
def another_bad_func():
    """
    Args:
       x: an integer
    """
    # PEP 257 says the first line should be a concise summary.
    pass

# Best Practice (PEP 257):
# 1. Always use triple double quotes `"""`.
# 2. One-line docstrings should fit on one line completely.
# 3. Multi-line docstrings should consist of a summary line, a blank line, and a more detailed description.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is the difference between a comment and a docstring?
# A: Comments (#) are ignored by Python and are for developers reading the code. Docstrings (""") are retained at runtime as an attribute of the object (`__doc__`) and can be accessed by IDEs and functions like `help()`.

# Q2: Where should a docstring be placed?
# A: As the very first statement inside a function, class, or module.

# Q3: Which PEP outlines the conventions for writing docstrings?
# A: PEP 257.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a proper Google-style docstring for the following function.
def calculate_area(length, width):
    """
    Calculates the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
        
    Returns:
        float: The calculated area (length * width).
    """
    return length * width

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge:
# Write a function `process_list` that takes a list of integers and returns a list of unique, sorted integers.
# Write a complete Numpy-style docstring for it.

def process_list(numbers):
    """
    Removes duplicates from a list of integers and returns a sorted list.

    Parameters
    ----------
    numbers : list of int
        The input list containing integer values.

    Returns
    -------
    list of int
        A new list containing unique, sorted integers.
    """
    return sorted(list(set(numbers)))

print("\n--- Mini Challenge ---")
print(process_list.__doc__)

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Docstrings are written using triple quotes `"""` immediately after definitions.
# - They document what a function/class/module does.
# - They can be accessed via `__doc__` or the `help()` function.
# - Standard styles like Google or NumPy help maintain consistency and work well with documentation generators like Sphinx.

if __name__ == "__main__":
    pass
