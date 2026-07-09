"""
Topic: Loop Practice Exercises
Chapter: 06
Level: Beginner / Intermediate

Description:
    This file contains standard loops practice problems to help solidify foundational concepts such as iterations, conditions inside loops, and aggregating values over a loop.

Real-Life Analogy:
    Imagine a repetitive daily task like washing dishes. You loop through each dirty dish, wash it, and put it on the rack until the sink is empty.

Key Concepts:
    - Iteration over sequences
    - Accumulator variables
    - Conditional logic within loops
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_loop_examples():
    print("--- Sum of Numbers ---")
    total = 0
    # Summing numbers from 1 to 5
    for i in range(1, 6):
        total += i
    print(f"Sum of 1 to 5 is: {total}")

    print("\n--- Counting Evens ---")
    evens = 0
    # Counting even numbers between 1 and 10
    for num in range(1, 11):
        if num % 2 == 0:
            evens += 1
    print(f"There are {evens} even numbers from 1 to 10")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_exercises():
    print("--- Reverse a String ---")
    word = "Python"
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    print(f"'{word}' reversed is '{reversed_word}'")

    print("\n--- Factorial Calculation ---")
    n = 5
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"The factorial of {n} is {factorial}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_exercises():
    print("--- Fibonacci Sequence ---")
    # Print the first 10 numbers in the Fibonacci sequence
    a, b = 0, 1
    fib_seq = []
    for _ in range(10):
        fib_seq.append(a)
        a, b = b, a + b
    print("First 10 Fibonacci numbers:", fib_seq)

    print("\n--- Finding Prime Numbers ---")
    limit = 20
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    print(f"Prime numbers up to {limit}:", primes)

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Common Mistakes:
# 1. Modifying the list while iterating over it (can cause infinite loops or skipped items).
# 2. Forgetting to update loop variables in `while` loops, causing infinite loops.
# 3. Off-by-one errors with `range(start, end)`.

# Best Practices:
# 1. Use descriptive variable names (`for student in students:` rather than `for s in students:`).
# 2. Initialize accumulator variables (like total = 0, product = 1) before the loop starts.
# 3. Use built-in functions like `sum()` or `reversed()` when suitable, rather than writing a manual loop for trivial tasks.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: How do you reverse a string without using a loop?
A: Using string slicing: `word[::-1]`.

Q2: What is the purpose of an accumulator variable?
A: To collect and store a cumulative value (e.g., sum, product, or concatenated string) during the iterations of a loop.

Q3: Why shouldn't you remove items from a list while iterating over it with a for loop?
A: It shifts the indices of the remaining elements, causing the loop to skip the next element. Use list comprehensions or iterate over a copy of the list.

Q4: What happens if `range(5, 0)` is used without a step?
A: It creates an empty sequence, and the loop won't execute. It needs a negative step: `range(5, 0, -1)`.

Q5: Is it possible to have an empty loop?
A: Yes, but you must put a `pass` statement inside it to avoid a SyntaxError.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

def practice_exercises():
    # Exercise 1: Calculate the sum of digits of a given number (e.g., 123 -> 6).
    pass

    # Exercise 2: Print the multiplication table of a given number.
    pass

    # Exercise 3: Given a list of integers, find the largest and smallest number without using max() or min().
    pass

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: 
    Given a list of words, create a dictionary where keys are the words 
    and values are their lengths. Ignore words that start with the letter 'a'.
    """
    words = ["apple", "banana", "cherry", "avocado", "date"]
    word_lengths = {}
    
    for word in words:
        if word.lower().startswith('a'):
            continue
        word_lengths[word] = len(word)
        
    print("Challenge Result:", word_lengths)

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Loops are crucial for processing sequences of data.
- Accumulators track running totals or sequences.
- Flags (like is_prime = True) help track boolean states across loop iterations.
- Mastering these patterns is essential for almost all coding algorithms.
"""

if __name__ == "__main__":
    basic_loop_examples()
    practical_exercises()
    advanced_exercises()
    mini_challenge()
