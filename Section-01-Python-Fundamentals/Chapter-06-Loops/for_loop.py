"""
Topic: For Loops in Python
Chapter: 6
Level: Beginner

Description:
    A `for` loop in Python is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string) or any other iterable object. 
    It allows you to execute a block of code repeatedly for each item in the sequence.

Real-Life Analogy:
    Imagine you are a teacher checking exam papers. You take one paper from the stack, grade it, and move on to the next. 
    You repeat this process for every paper until the stack is empty.

Key Concepts:
    - Iterables (lists, strings, tuples, etc.)
    - The `in` keyword
    - The `range()` function
    - Loop scope and variables
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_syntax():
    """Demonstrates basic syntax of for loops."""
    print("--- Basic Syntax ---")
    
    # 1. Iterating over a string
    # The loop variable 'char' takes the value of each character in the string sequentially.
    print("String iteration:")
    for char in "Python":
        print(f"Letter: {char}")
        
    # 2. Iterating over a list
    colors = ['Red', 'Green', 'Blue']
    print("\nList iteration:")
    for color in colors:
        print(f"Color: {color}")
        
    # 3. Using the range() function
    # range(start, stop, step)
    print("\nUsing range(5):")
    for i in range(5):  # Generates numbers from 0 to 4
        print(f"Number: {i}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    """Real-world use cases for 'for' loops."""
    print("\n--- Practical Examples ---")
    
    # 1. Summing values
    sales = [150.50, 200.00, 50.25, 300.00]
    total_sales = 0
    for sale in sales:
        total_sales += sale
    print(f"Total sales: ${total_sales:.2f}")
    
    # 2. Filtering a list
    temperatures = [72, 85, 60, 90, 68]
    hot_days = []
    for temp in temperatures:
        if temp > 80:
            hot_days.append(temp)
    print(f"Temperatures above 80: {hot_days}")

    # 3. Iterating over a dictionary
    student_grades = {"Alice": "A", "Bob": "B", "Charlie": "A-"}
    print("\nStudent Grades:")
    for student, grade in student_grades.items():
        print(f"{student} received a {grade}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    """Advanced concepts and edge cases."""
    print("\n--- Advanced Usage ---")
    
    # 1. Modifying elements using range and len
    numbers = [1, 2, 3, 4, 5]
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** 2
    print(f"Squared numbers: {numbers}")
    
    # 2. Multiple variables iteration
    coordinates = [(0, 0), (1, 5), (3, 8)]
    for x, y in coordinates:
        print(f"X: {x}, Y: {y}")

    # 3. Skipping elements with step in range
    print("\nEven numbers using range step:")
    for i in range(0, 10, 2):
        print(i, end=" ")
    print()

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def mistakes_and_practices():
    """Common pitfalls and best practices."""
    print("\n--- Common Mistakes & Best Practices ---")
    
    # MISTAKE: Modifying a list while iterating over it
    # This can lead to skipped elements.
    items = [1, 2, 3, 4]
    # for item in items:
    #     if item == 2:
    #         items.remove(item) # DON'T DO THIS
    
    # BEST PRACTICE: Iterate over a copy or use list comprehensions
    filtered_items = [item for item in items if item != 2]
    print(f"Correctly filtered list: {filtered_items}")

    # BEST PRACTICE: Use descriptive loop variables
    # BAD: for i in users: print(i.name)
    # GOOD: for user in users: print(user.name)

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
1. Q: What is the difference between an iterable and an iterator?
   A: An iterable is an object that has an __iter__ method and can be looped over (e.g., list, string). An iterator is an object that has a __next__ method and produces the next value in the sequence.

2. Q: Can you modify the loop variable in a for loop?
   A: Yes, but it will be overwritten in the next iteration. It does NOT modify the original sequence.

3. Q: How do you iterate backward using a for loop?
   A: You can use `reversed(sequence)` or `range(start, stop, -1)`.

4. Q: How does `range()` work in Python 3 compared to Python 2?
   A: In Python 3, `range()` returns an immutable sequence type (a lazy generator-like object) rather than a list, making it highly memory efficient.

5. Q: What happens if you loop over a dictionary directly?
   A: You iterate over its keys by default.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Write a for loop that prints the first 10 multiples of 3.
Hint: Use range() with a step, or multiply the loop variable by 3.

Exercise 2: Given a list of words, print only the words that have more than 5 characters.

Exercise 3: Write a loop to count the number of vowels in a given string.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: Write a program that takes a string of words, counts the frequency
    of each word, and prints the result.
    """
    print("\n--- Mini Challenge ---")
    text = "apple banana apple orange banana apple"
    words = text.split()
    word_counts = {}
    
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
            
    print("Word frequencies:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- For loops iterate over iterables like lists, strings, and ranges.
- `range(start, stop, step)` generates a sequence of numbers.
- Unpacking allows you to iterate over multiple values simultaneously.
- Avoid modifying a sequence directly while iterating over it.
"""

if __name__ == "__main__":
    basic_syntax()
    practical_examples()
    advanced_usage()
    mistakes_and_practices()
    mini_challenge()
