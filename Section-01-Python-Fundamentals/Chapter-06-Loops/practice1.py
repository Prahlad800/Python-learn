"""
Topic: Advanced Loop Practice Exercises
Chapter: 06
Level: Intermediate

Description:
    This file builds upon foundational loops, introducing more complex logic, nested loops with data structures, and algorithmic problems. 

Real-Life Analogy:
    Think of a warehouse worker taking inventory. They not only need to count items (basic loop), but they must organize items by category, handle missing labels, and identify the most valuable assets (advanced looping logic).

Key Concepts:
    - Nested iterations with complex conditions
    - Algorithms involving loops
    - String and List manipulation algorithms
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def matrix_traversal():
    print("--- Matrix Traversal ---")
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    # Iterating through rows and columns
    for row in matrix:
        for item in row:
            print(f"{item}", end=" ")
        print()

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def unique_elements():
    print("\n--- Finding Unique Elements ---")
    items = [1, 2, 2, 3, 4, 4, 5]
    unique_items = []
    
    for item in items:
        if item not in unique_items:
            unique_items.append(item)
            
    print(f"Original: {items}")
    print(f"Unique: {unique_items}")

def character_frequency():
    print("\n--- Character Frequency ---")
    text = "hello world"
    freq = {}
    
    for char in text:
        if char == " ":
            continue
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
            
    print(f"Frequency map: {freq}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def anagram_check():
    print("\n--- Anagram Checker (Loop-based) ---")
    word1 = "listen"
    word2 = "silent"
    
    # Simple loop approach without sorting
    is_anagram = True
    if len(word1) != len(word2):
        is_anagram = False
    else:
        # Create a copy as a list to remove matched characters
        list2 = list(word2)
        for char1 in word1:
            found = False
            for i, char2 in enumerate(list2):
                if char1 == char2:
                    list2.pop(i)
                    found = True
                    break
            if not found:
                is_anagram = False
                break
                
    print(f"Are '{word1}' and '{word2}' anagrams? {is_anagram}")

def bubble_sort():
    print("\n--- Bubble Sort Implementation ---")
    arr = [64, 34, 25, 12, 22, 11, 90]
    n = len(arr)
    
    # Outer loop for passes
    for i in range(n):
        swapped = False
        # Inner loop for comparisons
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no elements were swapped in the inner loop, array is sorted
        if not swapped:
            break
            
    print("Sorted array:", arr)

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Common Mistakes:
# 1. High Time Complexity: Using a loop inside another loop on large lists can lead to O(N^2) performance.
# 2. Duplicate code: Using loops for operations that standard library functions can do efficiently (like `set()` for unique items).

# Best Practices:
# 1. Optimize inner loops; do the heavy lifting outside if possible.
# 2. Break out early. If you find what you are looking for, use `break` to save execution time.
# 3. Consider using dictionaries (Hash Maps) to count or track occurrences instead of nested list loops.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: What is the time complexity of the bubble sort algorithm provided above?
A: In the worst case, O(N^2). With the `swapped` optimization, best case (already sorted) is O(N).

Q2: Why use `enumerate()` instead of `range(len())`?
A: `enumerate()` is more pythonic, readable, and slightly faster when you need both the index and the value.

Q3: Can an anagram checker be implemented in O(N) time?
A: Yes, by using a hash map (dictionary) to count character frequencies of both strings and comparing the maps.

Q4: What is list popping inside a loop dangerous?
A: Modifying the length of the list while iterating through its indices leads to IndexError or skipping elements.

Q5: When should you prefer a list comprehension over a traditional for-loop?
A: When you are creating a new list based on an existing iterable and the logic is simple enough to be readable in one line.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

def practice_exercises():
    # Exercise 1: Implement Selection Sort using nested loops.
    pass

    # Exercise 2: Find the first non-repeating character in a string.
    pass

    # Exercise 3: Flatten a 2D list into a 1D list using a loop.
    pass

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: 
    Given a list of numbers, find two numbers that sum up to a target value.
    Return their indices.
    """
    nums = [2, 7, 11, 15]
    target = 9
    
    print("\n--- Two Sum Challenge ---")
    
    # Naive O(N^2) approach using nested loops
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print(f"Indices: {i}, {j} (Values: {nums[i]}, {nums[j]})")
                return

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Advanced loops often involve manipulating multiple data structures simultaneously.
- Optimization becomes important (using break, dictionaries, and optimal algorithms).
- Algorithmic foundations like sorting and searching heavily rely on complex loop constructs.
"""

if __name__ == "__main__":
    matrix_traversal()
    unique_elements()
    character_frequency()
    anagram_check()
    bubble_sort()
    mini_challenge()
