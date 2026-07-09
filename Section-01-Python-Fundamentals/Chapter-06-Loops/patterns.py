"""
Topic: Loop Patterns
Chapter: 06
Level: Beginner

Description:
    Pattern printing involves using nested loops to print stars or numbers in a specific format (e.g., triangles, squares, pyramids). This is a classical programming exercise to strengthen understanding of nested iterations.

Real-Life Analogy:
    Think of a bricklayer building a wall. The outer loop controls which row of the wall they are working on, and the inner loop controls how many bricks they lay on that specific row.

Key Concepts:
    - Nested loops (for and while)
    - Controlling line breaks (end parameter in print)
    - Row and column indexing
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_patterns():
    print("--- Square Pattern ---")
    # Outer loop for rows
    for i in range(3):
        # Inner loop for columns
        for j in range(3):
            # Print star without a newline
            print("*", end=" ")
        # Move to the next line after each row
        print()
        
    print("\n--- Right-Angled Triangle ---")
    # Increasing number of columns per row
    for i in range(1, 5):
        for j in range(i):
            print("*", end=" ")
        print()

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def number_patterns():
    print("--- Number Triangle ---")
    # Using the row number as the character to print
    for i in range(1, 5):
        for j in range(i):
            print(i, end=" ")
        print()

    print("\n--- Floyd's Triangle ---")
    count = 1
    for i in range(1, 5):
        for j in range(i):
            print(count, end=" ")
            count += 1
        print()

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_patterns():
    print("--- Pyramid Pattern ---")
    n = 5
    for i in range(n):
        # Print spaces
        for j in range(n - i - 1):
            print(" ", end="")
        # Print stars
        for k in range(2 * i + 1):
            print("*", end="")
        print()

    print("\n--- Diamond Pattern ---")
    n = 4
    # Upper half
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    # Lower half
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Common Mistakes:
# 1. Forgetting the `print()` at the end of the outer loop, causing everything to print on one line.
# 2. Confusing the variables for rows (often i) and columns (often j).
# 3. Off-by-one errors in `range()` limits.

# Best Practices:
# 1. Start by defining `n`, the size of the pattern.
# 2. Understand the mathematical relationship between the row number and the number of characters/spaces to print.
# 3. Break down complex patterns (like a diamond) into simpler parts (top triangle, bottom triangle).

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: How do you print characters on the same line in Python?
A: Use the `end` parameter in the `print` function: `print("Hello", end=" ")`.

Q2: What is the time complexity of printing an N x N square pattern?
A: O(N^2), because there is an outer loop running N times and an inner loop running N times.

Q3: How do you invert a right-angled triangle pattern?
A: Loop backwards or change the inner loop range to `range(n - i)`.

Q4: Can we draw patterns using a single loop in Python?
A: Yes, by using string multiplication: `for i in range(1, n+1): print("*" * i)`.

Q5: Why is pattern printing taught in programming?
A: It tests logical thinking and mastery of nested loops and coordinate geometry concepts.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

def practice_exercises():
    # Exercise 1: Print an inverted right-angle triangle.
    # Hint: for i in range(5, 0, -1)
    pass

    # Exercise 2: Print a hollow square pattern.
    # Hint: Only print '*' when i or j is at the boundary.
    pass

    # Exercise 3: Print a Pascal's Triangle using numbers.
    pass

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: Create an hourglass pattern with stars.
    Example for n = 3:
    *****
     ***
      *
     ***
    *****
    """
    print("--- Hourglass Challenge ---")
    n = 3
    # Top half
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    # Bottom half (skip the single star row to avoid duplication)
    for i in range(2, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Loop patterns use nested loops to format output spatially.
- The outer loop typically controls the rows.
- The inner loop controls the columns (characters printed on that row).
- Using string multiplication `print("*" * count)` can simplify or even eliminate inner loops in Python.
"""

if __name__ == "__main__":
    basic_patterns()
    number_patterns()
    advanced_patterns()
    mini_challenge()
