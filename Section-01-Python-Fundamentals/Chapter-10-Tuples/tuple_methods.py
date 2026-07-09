"""
Topic: Tuple Methods
Chapter: 10
Level: Beginner

Description:
    Because tuples are immutable, they have very few built-in methods compared to lists. 
    Specifically, tuples only have two methods: `count()` and `index()`. These methods 
    are used for querying the contents of the tuple without modifying it.

Real-Life Analogy:
    Imagine looking at a static photograph of a crowd. You cannot add or remove people 
    from the photo. However, you can count how many people are wearing red hats (`count`), 
    and you can point out the exact position of a specific person (`index`).

Key Concepts:
    - tuple.count(value)
    - tuple.index(value, [start, [stop]])
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_methods() -> None:
    numbers = (1, 2, 3, 2, 4, 2, 5)
    
    # count(): Returns the number of times a value appears in the tuple
    twos_count = numbers.count(2)
    print(f"The number 2 appears {twos_count} times.")
    
    # index(): Returns the first index of the given value
    first_index_of_2 = numbers.index(2)
    print(f"The first occurrence of 2 is at index {first_index_of_2}.")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples() -> None:
    # Practical use case: Analyzing survey responses
    responses = ("yes", "no", "yes", "maybe", "yes", "no", "yes")
    
    total_yes = responses.count("yes")
    total_no = responses.count("no")
    
    print(f"Survey Results - Yes: {total_yes}, No: {total_no}")
    
    # Finding the position of a specific event
    system_states = ("INIT", "LOADING", "READY", "ERROR", "REBOOT")
    
    if "ERROR" in system_states:
        error_pos = system_states.index("ERROR")
        print(f"System encountered an ERROR at state sequence #{error_pos}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage() -> None:
    # index() with start and stop arguments
    # tuple.index(value, start, stop)
    t = (10, 20, 30, 20, 40, 50, 20)
    
    # Find the first '20'
    first_idx = t.index(20)
    print(f"First 20 at: {first_idx}")
    
    # Find the next '20' by starting the search after the first one
    second_idx = t.index(20, first_idx + 1)
    print(f"Second 20 at: {second_idx}")
    
    # Limit the search range
    try:
        # Search for 20 only between index 1 and 3 (exclusive of 3)
        # This will fail because index 1 is 20, wait, index 1 is 20, so it will succeed.
        # Let's search between 2 and 3
        t.index(20, 2, 3)
    except ValueError as e:
        print(f"Value not found in range: {e}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes() -> None:
    # Mistake: Using .index() on a value that doesn't exist raises a ValueError
    t = ("apple", "banana")
    
    try:
        idx = t.index("cherry")
    except ValueError as e:
        print(f"Expected Error: {e}")
        
    # Best Practice: Always check if the item exists first!
    search_item = "cherry"
    if search_item in t:
        print(f"Found at {t.index(search_item)}")
    else:
        print(f"'{search_item}' is not in the tuple.")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: How many built-in methods does a Python tuple have, and what are they?
A: Only two: `count()` and `index()`.

Q2: What does `tuple.index(x)` return if `x` is in the tuple multiple times?
A: It returns the index of the *first* occurrence of `x`.

Q3: What happens if `tuple.index(x)` cannot find `x`?
A: It raises a `ValueError`.

Q4: Why does a tuple not have `.append()` or `.remove()` methods?
A: Because tuples are immutable; their size and contents cannot be changed after creation.

Q5: Can `tuple.count(x)` raise an exception?
A: No, if the item is not found, it simply returns `0`.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
def practice_exercises() -> None:
    """
    Exercise 1: Create a tuple of random grades (A, B, C, A, A, B).
    Exercise 2: Count how many 'A' grades there are.
    Exercise 3: Find the index of the first 'C' grade.
    """
    grades = ("A", "B", "C", "A", "A", "B")
    
    num_a = grades.count("A")
    print(f"Number of A's: {num_a}")
    
    index_c = grades.index("C")
    print(f"Index of first C: {index_c}")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================
def mini_challenge() -> None:
    """
    Challenge: Write a function `find_all_indices(tup, val)` that returns a list of 
    all indices where `val` appears in `tup`.
    """
    def find_all_indices(tup: tuple, val: any) -> list:
        indices = []
        start = 0
        while True:
            try:
                idx = tup.index(val, start)
                indices.append(idx)
                start = idx + 1
            except ValueError:
                break
        return indices
        
    sample = (1, 2, 1, 3, 1, 4)
    print(f"All indices of 1: {find_all_indices(sample, 1)}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- Tuples have exactly two methods: `count()` and `index()`.
- `count(val)` returns the frequency of a value.
- `index(val)` returns the first position of a value.
- Always use the `in` keyword before `index()` to prevent `ValueError`s.
- These limited methods reflect the immutable, read-only nature of tuples.
"""

if __name__ == "__main__":
    basic_methods()
    practical_examples()
    advanced_usage()
    common_mistakes()
    practice_exercises()
    mini_challenge()
