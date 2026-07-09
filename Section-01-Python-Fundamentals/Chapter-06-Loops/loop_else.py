"""
Topic: The for-else and while-else Constructs
Chapter: 06
Level: Intermediate

Description:
    Python allows an optional `else` clause at the end of `for` and `while` loops. 
    The `else` block executes *only if the loop completes normally* (i.e., without encountering a `break` statement).

Real-Life Analogy:
    Searching for your keys. You check the kitchen, the bedroom, and the living room (the loop). 
    If you don't find them, you conclude they are lost (the else block). 
    If you find them midway, you stop looking (`break`), and you don't conclude they are lost (skip else block).

Key Concepts:
    - Loop completion vs Loop termination
    - The `break` statement preventing `else`
    - Avoiding the use of "flag" variables
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_for_else():
    print("--- For-Else Syntax ---")
    items = [1, 2, 3, 4, 5]
    target = 6
    
    for item in items:
        if item == target:
            print("Target found!")
            break
    else:
        # This executes because break was NOT encountered
        print("Target NOT found in the list.")

def basic_while_else():
    print("\n--- While-Else Syntax ---")
    count = 3
    while count > 0:
        print(f"Counting down... {count}")
        count -= 1
    else:
        # Executes when the condition (count > 0) becomes false
        print("Blastoff! (Loop completed normally)")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def prime_checker():
    print("\n--- Prime Number Checker ---")
    num = 29
    
    # Traditional way uses a boolean flag (is_prime = True)
    # The for-else way is cleaner:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not prime. Divisible by {i}.")
            break
    else:
        print(f"{num} is a prime number.")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def nested_loop_else():
    print("\n--- Nested Loop Else ---")
    # Finding the first list that doesn't contain a zero
    matrix = [
        [1, 2, 0],
        [4, 0, 6],
        [7, 8, 9]
    ]
    
    for row in matrix:
        for item in row:
            if item == 0:
                print(f"Row {row} contains a zero. Skipping to next row.")
                break
        else:
            print(f"Row {row} does NOT contain any zeros! Target found.")
            break # Break outer loop since we found what we wanted

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Common Mistakes:
# 1. Thinking `else` executes if the loop *doesn't* run (like an if-else). It actually means "no break occurred".
# 2. Placing the `else` inside the loop indentation instead of aligned with the `for` or `while` keyword.
# 3. Using `return` or `raise` inside the loop without `break`, rendering the `else` clause irrelevant because the function exits entirely.

# Best Practices:
# 1. Use loop-else when searching for an item in an iterable. It eliminates the need for `found = False` flags.
# 2. Read `else` on a loop as `nobreak` mentally to prevent confusion.
# 3. Don't overuse it if it makes the code harder for beginners to read, but know it for elegant Pythonic solutions.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: When does the `else` block of a loop execute?
A: When the loop naturally exhausts its iterable (in a `for` loop) or the condition becomes false (in a `while` loop) without hitting a `break` statement.

Q2: What happens if an exception is raised inside the loop? Does the `else` block run?
A: No. The exception terminates the block entirely and transfers control to an exception handler.

Q3: Does a `continue` statement prevent the `else` block from running?
A: No, only `break` prevents the `else` block from running.

Q4: If the iterable in a for loop is empty, does the `else` block execute?
A: Yes, because the loop completes without hitting a `break`.

Q5: Why is the keyword `else` used instead of a more descriptive keyword like `nobreak`?
A: It was an architectural design choice in Python to reuse keywords rather than adding new ones, though Guido van Rossum has stated he might have reconsidered it if done over again.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

def practice_exercises():
    # Exercise 1: Write a program that searches for the word "Python" in a list of words.
    # If found, break. If not found, use the else clause to print an error message.
    pass

    # Exercise 2: Validate a password string. Check if it contains at least one number.
    # If no number is found after checking all characters, print "Invalid password" using loop-else.
    pass

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: 
    Given a list of lists containing employee data [Name, Age, Department].
    Search for an employee named "Alice". If found, print her department.
    If not found in the entire directory, print "Employee not found."
    Do this WITHOUT using an `is_found` boolean variable.
    """
    employees = [
        ["John", 30, "HR"],
        ["Bob", 25, "Engineering"],
        ["Charlie", 35, "Marketing"]
    ]
    
    print("\n--- Employee Search ---")
    search_name = "Alice"
    
    for emp in employees:
        if emp[0] == search_name:
            print(f"{search_name} works in {emp[2]}.")
            break
    else:
        print(f"Employee '{search_name}' not found in directory.")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Loop-else executes only if the loop does NOT encounter a `break`.
- It replaces the need for "flag" variables when performing search operations.
- Conceptually, it is better to read `else` as `nobreak`.
"""

if __name__ == "__main__":
    basic_for_else()
    basic_while_else()
    prime_checker()
    nested_loop_else()
    mini_challenge()
