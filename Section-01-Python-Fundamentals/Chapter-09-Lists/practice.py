"""
Topic: Practice File
Chapter: 9
Level: Beginner to Advanced

Description:
    This file contains a compilation of varied practice exercises designed to test all concepts learned in the Lists chapter, including basics, comprehensions, methods, slicing, and nested lists.

Real-Life Analogy:
    Like a final exam or a workout session that combines cardio, weightlifting, and flexibility to test your overall fitness in list manipulation.

Key Concepts:
    - Applying basic list operations
    - Using list methods effectively
    - Slicing and indexing
    - Nested structures
    - Comprehensions
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_exercises():
    print("--- Section 1: Basic Exercises ---")
    # EXERCISE 1: Create a list of 5 colors. Print the first and last color.
    colors = ["Red", "Green", "Blue", "Yellow", "Purple"]
    print(f"First color: {colors[0]}, Last color: {colors[-1]}")
    
    # EXERCISE 2: Replace the middle color with "Black"
    colors[2] = "Black"
    print(f"Updated colors: {colors}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_exercises():
    print("\n--- Section 2: Practical Exercises ---")
    # EXERCISE 3: You have a list of prices. Add a 10% tax to each price using a standard loop.
    prices = [10.0, 25.50, 5.0, 100.0]
    taxed_prices = []
    for price in prices:
        taxed = price * 1.10
        taxed_prices.append(round(taxed, 2))
    print(f"Prices with tax: {taxed_prices}")

    # EXERCISE 4: Use list methods to add "Python" to the end of the list, 
    # insert "Java" at the beginning, and remove "C++".
    languages = ["C++", "Ruby", "JavaScript"]
    languages.append("Python")
    languages.insert(0, "Java")
    if "C++" in languages:
        languages.remove("C++")
    print(f"Updated languages: {languages}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_exercises():
    print("\n--- Section 3: Advanced Exercises ---")
    # EXERCISE 5: Use a list comprehension to create a list of even numbers from 1 to 20.
    evens = [x for x in range(1, 21) if x % 2 == 0]
    print(f"Evens up to 20: {evens}")

    # EXERCISE 6: Given a 2D list (matrix), extract the diagonal elements (top-left to bottom-right)
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    diagonal = [matrix[i][i] for i in range(len(matrix))]
    print(f"Diagonal elements: {diagonal}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes_practice():
    print("\n--- Section 4: Fixing Mistakes ---")
    # Fix the mistake in the following code:
    # We want a 2x2 grid of zeros.
    # Bad code:
    # grid = [[0] * 2] * 2
    # grid[0][0] = 1
    
    # Fixed code:
    grid = [[0] * 2 for _ in range(2)]
    grid[0][0] = 1
    print(f"Properly initialized grid: {grid}")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Practice explaining these out loud:
1. When should you use a list comprehension vs a regular for-loop?
2. Explain the difference between .append() and .extend(). Provide an example.
3. How do you copy a list in Python, and why shouldn't you just use `list2 = list1`?
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# The file itself serves as the practice exercises.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def final_challenge():
    print("\n--- Section 7: Final Challenge ---")
    """
    Challenge: Build a simple To-Do List manager.
    Given an initial list of tasks:
    1. Add "Buy groceries".
    2. Mark "Clean room" as done by removing it.
    3. The user wants the list sorted alphabetically.
    4. Print the tasks with numbers (1., 2., 3., etc.) using a loop.
    """
    tasks = ["Wash car", "Clean room", "Pay bills"]
    
    # 1. Add
    tasks.append("Buy groceries")
    
    # 2. Remove
    if "Clean room" in tasks:
        tasks.remove("Clean room")
        
    # 3. Sort (Assuming list sorting will be covered)
    tasks.sort()
    
    # 4. Print
    print("My To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Regular practice is essential for mastering list operations.
- Always be aware of mutability and referencing when dealing with lists.
- Comprehensions make your code Pythonic but should be kept readable.
"""

if __name__ == "__main__":
    basic_exercises()
    practical_exercises()
    advanced_exercises()
    common_mistakes_practice()
    final_challenge()
