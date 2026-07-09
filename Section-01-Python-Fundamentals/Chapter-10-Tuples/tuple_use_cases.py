"""
Topic: Tuple Use Cases
Chapter: 10
Level: Intermediate

Description:
    While lists are the go-to for many collections, tuples shine in specific architectural 
    patterns. This file explores common real-world use cases where tuples are preferred, 
    such as multiple return values, dictionary keys, and string formatting.

Real-Life Analogy:
    Using tuples is like using unchangeable standard IDs (like a passport number) to look 
    up records, or handing someone a sealed envelope containing exactly three documents 
    that they are meant to read but not alter.

Key Concepts:
    - Multiple Return Values
    - Tuples as Dictionary Keys
    - String Formatting with Tuples
    - Passing variable length arguments (*args)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_use_cases() -> None:
    # 1. Multiple return values from a function
    def min_max(numbers: list) -> tuple:
        return min(numbers), max(numbers)
        
    low, high = min_max([5, 2, 9, 1, 7])
    print(f"Low: {low}, High: {high}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples() -> None:
    # 2. Tuples as Dictionary Keys for multi-dimensional data
    # (Since lists are unhashable, tuples are required here)
    
    # Representing a 2D grid/board (e.g., Chess, Game of Life, Map)
    grid = {}
    grid[(0, 0)] = "Start"
    grid[(1, 2)] = "Obstacle"
    grid[(5, 5)] = "Treasure"
    
    player_pos = (1, 2)
    if player_pos in grid:
        print(f"At {player_pos} you found: {grid[player_pos]}")

    # 3. String formatting (Older style % formatting requires tuples)
    name = "Alice"
    age = 30
    formatted = "My name is %s and I am %d years old." % (name, age)
    print(formatted)

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage() -> None:
    # 4. Using *args to accept a tuple of positional arguments in functions
    def log_message(level, *args):
        # args is packed into a tuple automatically
        print(f"args type: {type(args)}")
        message = " ".join(str(a) for a in args)
        print(f"[{level}] {message}")
        
    log_message("WARNING", "Disk space low:", 5, "GB remaining")
    
    # 5. Using tuples to swap multiple variables safely and concurrently
    a, b, c = 1, 2, 3
    # Shift them right
    a, b, c = c, a, b
    print(f"Shifted: a={a}, b={b}, c={c}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes() -> None:
    # Mistake: Returning a list when returning fixed data
    def bad_get_coordinates():
        return [40.7128, -74.0060] # Bad practice if coords shouldn't change
        
    # Best Practice: Return tuples for data that represents a single composite value
    def good_get_coordinates():
        return (40.7128, -74.0060)
        
    # Best Practice: Name tuple elements immediately via unpacking for readability
    lat, lng = good_get_coordinates()

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: Why do we use tuples as dictionary keys instead of lists?
A: Tuples are immutable and hashable. Dictionaries require hashable keys to compute the memory address for storage and lookup.

Q2: When a Python function has multiple comma-separated return values, what type is actually returned?
A: A single tuple containing those values.

Q3: What is `*args` in a function definition?
A: It allows the function to accept an arbitrary number of positional arguments, which are packed into a tuple named `args`.

Q4: Can you use a tuple containing a list as a dictionary key?
A: No, because a list is unhashable, making the entire tuple unhashable.

Q5: In modern Python, is % string formatting with tuples still the standard?
A: No, f-strings (`f"{var}"`) or `.format()` are preferred, but you will still see `%` formatting in legacy code or logging frameworks.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
def practice_exercises() -> None:
    """
    Exercise 1: Write a function `divide_and_remainder` that takes two numbers and returns their quotient and remainder as a tuple.
    Exercise 2: Create a dictionary where the keys are (FirstName, LastName) tuples and values are ages.
    """
    def divide_and_remainder(a: int, b: int) -> tuple:
        return a // b, a % b
        
    q, r = divide_and_remainder(10, 3)
    print(f"10 / 3 = {q} with remainder {r}")
    
    people = {
        ("John", "Doe"): 45,
        ("Jane", "Smith"): 32
    }
    print(f"John Doe's age: {people[('John', 'Doe')]}")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================
def mini_challenge() -> None:
    """
    Challenge: You are tracking flights between cities.
    Create a dictionary where keys are (Source, Destination) tuples, and values are prices.
    Write a function that looks up the price given a source and destination, 
    returning "Route not found" if it doesn't exist.
    """
    flights = {
        ("JFK", "LAX"): 350,
        ("LAX", "ORD"): 200,
        ("ORD", "JFK"): 180
    }
    
    def get_price(src: str, dest: str) -> str:
        route = (src, dest)
        if route in flights:
            return f"${flights[route]}"
        return "Route not found"
        
    print(f"JFK to LAX: {get_price('JFK', 'LAX')}")
    print(f"MIA to JFK: {get_price('MIA', 'JFK')}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- **Multiple Returns:** Python functions return tuples when separating values by commas.
- **Dict Keys:** Tuples are the standard way to create multi-dimensional dictionary keys (e.g., coordinate mapping).
- ***args:** Variable positional arguments are passed to functions as tuples.
- **Data Integrity:** Use tuples over lists when returning internal state that shouldn't be tampered with by the caller.
"""

if __name__ == "__main__":
    basic_use_cases()
    practical_examples()
    advanced_usage()
    common_mistakes()
    practice_exercises()
    mini_challenge()
