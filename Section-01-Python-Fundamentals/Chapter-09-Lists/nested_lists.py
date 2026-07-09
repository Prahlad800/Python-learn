"""
Topic: Nested Lists
Chapter: 9
Level: Intermediate

Description:
    A nested list is simply a list that contains other lists as its elements. This is commonly used to represent 2D structures like matrices, grids, or tables.

Real-Life Analogy:
    Think of a nested list like an egg carton or a spreadsheet. The main list is the whole carton (rows), and each inner list represents the slots in that row (columns).

Key Concepts:
    - Creating 2D Lists
    - Accessing elements in nested lists `list[row][col]`
    - Iterating through nested lists
    - Modifying nested lists
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_syntax():
    print("--- Section 1: Basic Syntax ---")
    # A simple 2D list (3x3 grid)
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(f"Full matrix: {matrix}")

    # Accessing the first row
    first_row = matrix[0]
    print(f"First row: {first_row}")

    # Accessing a specific element (Row 1, Column 2 -> the number 6)
    # Remember: 0-based indexing!
    element = matrix[1][2]
    print(f"Element at row 1, col 2: {element}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    print("\n--- Section 2: Practical Examples ---")
    # A list of student records: [Name, Age, Grade]
    students = [
        ["Alice", 20, "A"],
        ["Bob", 22, "B"],
        ["Charlie", 19, "A"]
    ]

    # Iterating through a nested list
    print("Student Records:")
    for student in students:
        name = student[0]
        grade = student[2]
        print(f"{name} got an {grade}")

    # Modifying a nested element
    # Bob improved his grade to an 'A'
    students[1][2] = "A"
    print(f"Updated Bob's record: {students[1]}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    print("\n--- Section 3: Advanced Usage ---")
    # 3D Lists (A list of lists of lists)
    # Useful for representing something like an RGB image or 3D space
    cube = [
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]]
    ]
    
    # Accessing the number 7
    # 2nd block, 2nd row, 1st element
    num_7 = cube[1][1][0]
    print(f"Extracted from 3D list: {num_7}")

    # Flattening a 2D list into a 1D list using nested loops
    grid = [[1, 2], [3, 4], [5, 6]]
    flat = []
    for row in grid:
        for item in row:
            flat.append(item)
    print(f"Flattened grid: {flat}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes():
    print("\n--- Section 4: Common Mistakes & Best Practices ---")
    # Mistake: Creating nested lists using multiplication
    # This creates multiple references to the SAME inner list!
    bad_grid = [[0] * 3] * 3
    bad_grid[0][0] = 99  # You expect only one 99, but all rows change!
    print(f"Bad Grid (Reference issue): {bad_grid}")

    # Best Practice: Use a list comprehension to create independent inner lists
    good_grid = [[0] * 3 for _ in range(3)]
    good_grid[0][0] = 99
    print(f"Good Grid (Independent rows): {good_grid}")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: How do you access the last element of the last inner list in a 2D list?
A: You can use double negative indexing: my_list[-1][-1].

Q2: Why does `[[0]*3]*3` cause issues when you try to modify it?
A: Because the outer multiplication copies the reference to the single inner list three times. Modifying one row modifies all of them. Use `[[0]*3 for _ in range(3)]` instead.

Q3: How would you transpose a 2D matrix (swap rows and columns)?
A: A common Pythonic way is `[[row[i] for row in matrix] for i in range(len(matrix[0]))]`, or using `zip(*matrix)`.

Q4: What is a ragged or jagged list?
A: A nested list where the inner lists do not all have the same length. Example: `[[1, 2], [3, 4, 5], [6]]`.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Create a 3x3 Tic-Tac-Toe board filled with empty strings ("").
Exercise 2: Write a loop to print the 3x3 board row by row.
Exercise 3: Place an "X" in the center square of the board.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    print("\n--- Section 7: Mini Challenge ---")
    """
    Challenge: Calculate the sum of all numbers in a 2D list.
    """
    data = [
        [10, 20],
        [30, 40],
        [50, 60]
    ]
    
    total_sum = 0
    for row in data:
        for num in row:
            total_sum += num
            
    print(f"The total sum of the 2D list is: {total_sum}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Nested lists are lists within lists.
- They are accessed using multiple brackets `[row][col]`.
- Be careful when initializing nested lists with multiplication; use list comprehension to avoid reference sharing.
- You can iterate through them using nested for-loops.
"""

if __name__ == "__main__":
    basic_syntax()
    practical_examples()
    advanced_usage()
    common_mistakes()
    mini_challenge()
