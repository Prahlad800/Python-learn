"""
Topic: Tuple Operations
Chapter: 10
Level: Beginner

Description:
    While tuples are immutable, they still support a variety of operations that generate 
    new tuples or evaluate their contents. These operations include concatenation, repetition, 
    membership testing, and iteration.

Real-Life Analogy:
    Think of tuple operations like working with train cars. You can connect two different 
    trains together (concatenation) or duplicate a train's cars (repetition), but doing so 
    creates a completely new, longer train rather than modifying the original ones.

Key Concepts:
    - Concatenation (+)
    - Repetition (*)
    - Membership (in, not in)
    - Iteration (for loops)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_operations() -> None:
    t1 = (1, 2, 3)
    t2 = (4, 5, 6)
    
    # Concatenation: Joins two tuples into a new tuple
    t3 = t1 + t2
    print(f"Concatenated tuple: {t3}")
    
    # Repetition: Repeats the tuple elements N times
    t_repeated = t1 * 3
    print(f"Repeated tuple: {t_repeated}")
    
    # Membership testing
    print(f"Is 2 in t1? {2 in t1}")
    print(f"Is 99 not in t1? {99 not in t1}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples() -> None:
    # Using concatenation to build paths or sequences
    base_path = ("usr", "local")
    sub_path = ("bin", "script.sh")
    full_path = base_path + sub_path
    
    print(f"Full path tuple: {full_path}")
    print(f"Formatted path: /" + "/".join(full_path))
    
    # Iteration over a tuple
    settings = ("Dark Mode", "Auto-Save", "Notifications On")
    print("User Settings:")
    for setting in settings:
        print(f"- {setting}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage() -> None:
    # Concatenation with assignment (Creates a NEW tuple, doesn't mutate)
    t = (10, 20)
    original_id = id(t)
    
    t += (30, 40)  # Rebinds 't' to a new tuple (10, 20, 30, 40)
    new_id = id(t)
    
    print(f"Original ID: {original_id}, New ID: {new_id}")
    print(f"Are they the same object in memory? {original_id == new_id}")
    print(f"Updated t: {t}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes() -> None:
    # Mistake: Trying to concatenate a tuple with a non-tuple
    t = (1, 2)
    try:
        # t = t + 3  # TypeError! Must be a tuple.
        t = t + (3,) # Correct way
        print(f"Correct concatenation: {t}")
    except TypeError as e:
        print(f"Error: {e}")

    # Best Practice: Avoid concatenating tuples inside large loops.
    # It creates a new tuple every iteration, which is memory-inefficient.
    # Use lists for dynamic building, then convert to tuple at the end.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: Does the `+` operator change the original tuple?
A: No, it creates and returns a completely new tuple containing elements from both operands.

Q2: How can you check if an item exists in a tuple?
A: Use the `in` operator, e.g., `item in my_tuple`.

Q3: What happens if you multiply a tuple by a negative number?
A: It results in an empty tuple `()`.

Q4: Can you iterate over a tuple?
A: Yes, tuples are iterables and can be used in `for` loops.

Q5: Why is `tuple += (item,)` considered bad practice in a loop?
A: Because tuples are immutable, this operation creates a new tuple object in memory during every iteration, leading to O(N^2) time complexity.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
def practice_exercises() -> None:
    """
    Exercise 1: Create a tuple of even numbers (2,4) and odd numbers (1,3). Concatenate them.
    Exercise 2: Create a tuple of a single repeating value (e.g., 0) repeated 10 times.
    Exercise 3: Check if the number 5 is in the concatenated tuple from Exercise 1.
    """
    evens = (2, 4)
    odds = (1, 3)
    combined = evens + odds
    print(f"Combined: {combined}")
    
    zeros = (0,) * 10
    print(f"Zeros: {zeros}")
    
    print(f"Is 5 in combined? {5 in combined}")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================
def mini_challenge() -> None:
    """
    Challenge: Write a function that takes an unknown number of string tuples and
    returns a single combined tuple containing all elements.
    """
    def combine_tuples(*args: tuple) -> tuple:
        result: tuple = ()
        for t in args:
            result += t
        return result
        
    res = combine_tuples(("a", "b"), ("c", "d"), ("e",))
    print(f"Challenge result: {res}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- Use `+` to concatenate two or more tuples into a new tuple.
- Use `*` to repeat a tuple's elements multiple times.
- The `in` and `not in` operators allow efficient membership checking.
- Tuples are fully iterable and work seamlessly with `for` loops.
- Remember: All these operations generate NEW tuples rather than modifying existing ones.
"""

if __name__ == "__main__":
    basic_operations()
    practical_examples()
    advanced_usage()
    common_mistakes()
    practice_exercises()
    mini_challenge()
