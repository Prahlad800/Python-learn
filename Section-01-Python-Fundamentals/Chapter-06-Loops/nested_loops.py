"""
Topic: Nested Loops
Chapter: 6
Level: Intermediate

Description:
    A nested loop is a loop inside the body of another loop. 
    For every single iteration of the "outer" loop, the "inner" loop executes all its iterations completely.

Real-Life Analogy:
    Think of a digital clock. The "hours" act as the outer loop and the "minutes" as the inner loop.
    For every single hour that passes (outer loop moves by 1), the minutes go from 0 to 59 completely (inner loop finishes all iterations).

Key Concepts:
    - Inner and outer loops
    - Multi-dimensional data processing
    - Computational complexity (O(N^2))
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_syntax():
    """Demonstrate basic syntax of nested loops."""
    print("--- Basic Syntax ---")
    
    # A simple nested for loop
    for i in range(3):          # Outer loop
        for j in range(2):      # Inner loop
            print(f"Outer: {i}, Inner: {j}")
            
    print("\n--- Nested While and For ---")
    x = 0
    while x < 2:
        for char in "AB":
            print(f"While: {x}, For: {char}")
        x += 1

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    """Real-world use cases for nested loops."""
    print("\n--- Practical Examples ---")
    
    # 1. Working with 2D lists (matrices)
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Printing matrix elements:")
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print() # Newline after each row

    # 2. Generating combinations
    colors = ["Red", "Blue"]
    items = ["Shirt", "Hat"]
    print("\nCombinations:")
    for color in colors:
        for item in items:
            print(f"{color} {item}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    """Advanced scenarios and edge cases."""
    print("\n--- Advanced Usage ---")
    
    # 1. Flattening a 2D list
    matrix = [[1, 2], [3, 4], [5, 6]]
    flat_list = []
    for row in matrix:
        for item in row:
            flat_list.append(item)
    print(f"Flattened list: {flat_list}")

    # 2. Multi-level nesting (3 levels)
    # Caution: This can get slow and hard to read quickly!
    print("\n3D Coordinate generation:")
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print(f"({x}, {y}, {z})")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def mistakes_and_practices():
    """Common pitfalls and best practices."""
    print("\n--- Common Mistakes & Best Practices ---")
    
    # MISTAKE: Reusing loop variable names
    # for i in range(5):
    #     for i in range(3): # BAD! Overwrites the outer 'i'
    #         pass
    
    # BEST PRACTICE: Be mindful of performance
    # If the outer loop runs N times and the inner loop runs M times,
    # the total operations are N * M. This can lead to O(N^2) time complexity.
    
    # BEST PRACTICE: Limit nesting depth
    # If you find yourself nesting 3 or 4 loops deep, consider refactoring 
    # the inner logic into a separate function.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
1. Q: How many times does the inner loop execute if the outer loop runs 5 times and the inner runs 10 times?
   A: The inner loop executes a total of 50 times (5 * 10).

2. Q: Can you break out of both inner and outer loops simultaneously using one `break` statement?
   A: No, `break` only exits the innermost loop. To break multiple loops, you need to use flags, exception handling, or refactor into a function and use `return`.

3. Q: What is the time complexity of a simple nested loop iterating over a list of size N in both loops?
   A: O(N^2) (Quadratic time).
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Print an multiplication table from 1 to 5.
(e.g., 1x1=1, 1x2=2, ..., 5x5=25).

Exercise 2: Create a nested loop that finds common elements between two lists.
list1 = [1, 2, 3, 4], list2 = [3, 4, 5, 6]

Exercise 3: Given a list of strings, write a nested loop to count the total number of vowels across all strings.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: Create a simple seating chart generator.
    You have 3 rows and 4 seats per row. Print out a map of seats 
    labeled like "Row 1 - Seat A", "Row 1 - Seat B", etc.
    """
    print("\n--- Mini Challenge ---")
    rows = range(1, 4)
    seats = ['A', 'B', 'C', 'D']
    
    for row in rows:
        print(f"Row {row}: ", end="")
        for seat in seats:
            print(f"[{row}{seat}] ", end="")
        print() # Move to the next row

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Nested loops are loops within loops.
- The inner loop completely restarts and finishes for every single step of the outer loop.
- They are essential for processing multi-dimensional data (like matrices or grids).
- Use them cautiously as they increase time complexity rapidly (O(N^2) or worse).
"""

if __name__ == "__main__":
    basic_syntax()
    practical_examples()
    advanced_usage()
    mistakes_and_practices()
    mini_challenge()
