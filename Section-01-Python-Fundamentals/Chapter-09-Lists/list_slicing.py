"""
Topic: List Slicing
Chapter: 9
Level: Beginner

Description:
    List slicing allows you to extract a portion (a sub-list) of a list using a specific syntax. It is a powerful way to access multiple elements simultaneously.

Real-Life Analogy:
    Imagine a loaf of bread. Indexing is picking out exactly one slice (e.g., the 3rd slice). Slicing is cutting out a chunk of several slices at once (e.g., from the 3rd to the 7th slice).

Key Concepts:
    - Slicing Syntax: `list[start:stop:step]`
    - Default values for start, stop, and step
    - Negative slicing
    - Modifying lists using slices
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_syntax():
    print("--- Section 1: Basic Syntax ---")
    # Syntax: my_list[start:stop:step]
    # start is INCLUSIVE, stop is EXCLUSIVE
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    
    # Extract elements from index 2 up to (but not including) index 5
    slice_1 = letters[2:5] 
    print(f"letters[2:5] -> {slice_1}")  # ['c', 'd', 'e']

    # Omitting 'start' defaults to the beginning (index 0)
    slice_2 = letters[:3]
    print(f"letters[:3] -> {slice_2}")   # ['a', 'b', 'c']

    # Omitting 'stop' defaults to the end of the list
    slice_3 = letters[4:]
    print(f"letters[4:] -> {slice_3}")   # ['e', 'f', 'g']

    # Omitting both creates a shallow copy of the entire list
    full_copy = letters[:]
    print(f"letters[:] -> {full_copy}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    print("\n--- Section 2: Practical Examples ---")
    # Using the 'step' parameter
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Extract every 2nd number (even indices)
    evens = numbers[::2]
    print(f"Every 2nd number: {evens}")

    # Extract every 3rd number from index 1 to 8
    weird_slice = numbers[1:8:3]
    print(f"numbers[1:8:3]: {weird_slice}")

    # Reversing a list using slicing
    # A step of -1 means "step backwards"
    reversed_nums = numbers[::-1]
    print(f"Reversed list: {reversed_nums}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    print("\n--- Section 3: Advanced Usage ---")
    # Negative indexing with slicing
    data = [10, 20, 30, 40, 50, 60]
    
    # Get the last 3 elements
    last_three = data[-3:]
    print(f"Last three elements: {last_three}")

    # Extract excluding the first and last elements
    middle = data[1:-1]
    print(f"Middle elements: {middle}")

    # Modifying lists via slicing
    # We can replace a chunk of a list with another iterable
    data[1:3] = [99, 100]
    print(f"List after slice assignment: {data}")

    # We can even delete chunks using slices
    del data[2:4]
    print(f"List after deleting a slice: {data}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes():
    print("\n--- Section 4: Common Mistakes & Best Practices ---")
    # Mistake: Confusing index out of range with slicing out of bounds
    items = [1, 2, 3]
    try:
        print(items[10]) # This throws IndexError
    except IndexError as e:
        print(f"Indexing out of bounds error: {e}")

    # Slicing is forgiving! It won't throw an error if bounds are exceeded
    safe_slice = items[1:100]
    print(f"Slicing out of bounds (Safe): {safe_slice}")

    # Best Practice: Use slice assignment carefully, as replacing a slice 
    # with a list of a different length changes the total list size.
    temp = [1, 2, 3, 4]
    temp[1:3] = [9] # Replaces two elements with one
    print(f"Slice replaced with different length: {temp}")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: How do you reverse a list using slicing?
A: By using a step of -1, e.g., `my_list[::-1]`.

Q2: Is the 'stop' index in slicing inclusive or exclusive?
A: It is exclusive. `my_list[0:2]` returns elements at index 0 and 1, but not 2.

Q3: What happens if you slice beyond the length of the list?
A: Python handles it gracefully and just returns up to the end of the list, without raising an IndexError.

Q4: What does `my_list[:]` do?
A: It returns a shallow copy of the entire list.

Q5: Can you assign a new list to a slice?
A: Yes, slice assignment (e.g., `my_list[1:3] = [10, 20]`) is allowed and modifies the list in place.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Given `my_list = [10, 20, 30, 40, 50, 60]`, extract `[30, 40, 50]`.
Exercise 2: Get all odd-indexed elements from `[0, 1, 2, 3, 4, 5]`.
Exercise 3: Replace the first three elements of a list with the string "START".
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    print("\n--- Section 7: Mini Challenge ---")
    """
    Challenge: You are given a string formatted as a list of characters representing a URL.
    Extract the domain name from it.
    URL: ['h','t','t','p',':','/','/','w','w','w','.','g','o','o','g','l','e','.','c','o','m']
    Extract just the letters "google".
    """
    url_chars = ['h','t','t','p',':','/','/','w','w','w','.','g','o','o','g','l','e','.','c','o','m']
    
    # We know "www." ends at index 10.
    # The "." before "com" is at index -4.
    domain_slice = url_chars[11:-4]
    
    # Join them together to show the result
    domain = "".join(domain_slice)
    print(f"Extracted domain: {domain}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Slicing uses the format `[start:stop:step]`.
- It creates a new list (a sub-list) from the original list.
- `start` is inclusive, `stop` is exclusive.
- It fails gracefully if indices are out of bounds.
- It can be used for copying, reversing, and modifying chunks of lists.
"""

if __name__ == "__main__":
    basic_syntax()
    practical_examples()
    advanced_usage()
    common_mistakes()
    mini_challenge()
