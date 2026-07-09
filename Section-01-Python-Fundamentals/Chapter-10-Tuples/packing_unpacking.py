"""
Topic: Packing and Unpacking
Chapter: 10
Level: Intermediate

Description:
    Tuple packing is the process of grouping multiple values into a single tuple. 
    Tuple unpacking is the reverse process, extracting those values back into separate 
    variables. This feature allows for elegant and concise code assignments.

Real-Life Analogy:
    Packing is like putting your laptop, notebook, and pen into a single backpack 
    to carry them easily. Unpacking is when you arrive at your desk and take them 
    out of the backpack to place them on your desk as separate items.

Key Concepts:
    - Tuple Packing
    - Tuple Unpacking
    - The Asterisk (*) Operator for unpacking
    - Swapping variables
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_packing_unpacking() -> None:
    # Packing: assigning multiple values to one variable creates a tuple
    packed_tuple = "Alice", 25, "Engineer"
    print(f"Packed tuple: {packed_tuple}")

    # Unpacking: assigning a tuple to multiple variables
    name, age, profession = packed_tuple
    print(f"Unpacked: Name={name}, Age={age}, Profession={profession}")

    # Swapping variables without a temporary variable!
    a = 10
    b = 20
    print(f"Before swap: a={a}, b={b}")
    
    a, b = b, a  # This is packing and unpacking happening simultaneously
    print(f"After swap: a={a}, b={b}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples() -> None:
    # Functions returning multiple values actually return a packed tuple
    def get_user_stats():
        return 1500, 42, 99.5  # Returns a tuple

    # Unpacking the returned tuple immediately
    views, likes, engagement = get_user_stats()
    print(f"Stats: {views} views, {likes} likes, {engagement}% engagement")

    # Unpacking in for loops
    # List of tuples (e.g., coordinates)
    points = [(1, 2), (3, 4), (5, 6)]
    for x, y in points:
        print(f"X: {x}, Y: {y}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage() -> None:
    # Using the Asterisk (*) operator to unpack remaining elements
    # Useful when a tuple has more elements than variables
    grades = (95, 82, 76, 88, 91, 100)
    
    # Grab the first grade, the last grade, and group the rest in the middle
    first, *middle, last = grades
    
    print(f"First: {first}")
    print(f"Middle (List): {middle}")
    print(f"Last: {last}")

    # Asterisk can be used anywhere
    *top_three, lowest = (10, 9, 8, 3)
    print(f"Top 3: {top_three}, Lowest: {lowest}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes() -> None:
    # Mistake 1: Value count mismatch
    t = (1, 2, 3)
    try:
        x, y = t  # Error: too many values to unpack (expected 2)
    except ValueError as e:
        print(f"Unpacking Error: {e}")

    # Best Practice: Use a dummy variable (underscore _) for values you don't need
    record = ("Jane Doe", "jane@email.com", "555-1234", "Admin")
    name, _, _, role = record
    print(f"Role of {name} is {role}")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: What happens if you try to unpack a tuple into fewer variables than its length?
A: A `ValueError` is raised, complaining about "too many values to unpack", unless you use the `*` operator.

Q2: What type is the variable prefixed with `*` during unpacking?
A: It is always a list, even if it captures zero or one element.

Q3: Can you have multiple `*` variables in a single unpacking assignment?
A: No, Python allows only one starred expression in an assignment.

Q4: Explain `a, b = b, a`. How does it work?
A: Python first evaluates the right side `b, a` and packs it into a tuple. Then it unpacks that tuple into the targets `a, b` on the left.

Q5: Is unpacking exclusive to tuples?
A: No, you can unpack any iterable (lists, strings, sets, dictionaries).
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
def practice_exercises() -> None:
    """
    Exercise 1: Pack 4 string values into a tuple.
    Exercise 2: Unpack the first value into `head` and the rest into a variable `tail`.
    """
    # 1
    tech_stack = "Python", "Docker", "AWS", "React"
    
    # 2
    head, *tail = tech_stack
    print(f"Head: {head}, Tail: {tail}")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================
def mini_challenge() -> None:
    """
    Challenge: Write a function `process_data(data)` that takes a tuple of 
    (Name, Age, Score1, Score2, Score3). 
    Use unpacking to extract the name and a list of scores. 
    Print the name and the average of the scores.
    """
    def process_data(data: tuple) -> None:
        name, age, *scores = data
        avg = sum(scores) / len(scores)
        print(f"Student: {name}, Age: {age}, Average Score: {avg:.2f}")
        
    process_data(("Charlie", 20, 85, 90, 95))

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- Packing allows assignment of multiple values to a single tuple without parentheses.
- Unpacking assigns tuple elements to multiple distinct variables.
- Swapping variables is easily done via `a, b = b, a`.
- Use the `*` operator to capture an arbitrary number of unpacked elements into a list.
- Use `_` as a dummy variable for values you want to ignore.
"""

if __name__ == "__main__":
    basic_packing_unpacking()
    practical_examples()
    advanced_usage()
    common_mistakes()
    practice_exercises()
    mini_challenge()
