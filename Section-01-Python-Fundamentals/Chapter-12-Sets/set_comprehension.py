"""
Topic: Set Comprehension
Chapter: 12
Level: Intermediate

Description:
    Set comprehensions offer a concise way to create sets based on existing iterables. They follow the same syntax as list comprehensions but use curly braces `{}` instead of square brackets `[]`.

Real-Life Analogy:
    Imagine filtering through a basket of mixed fruits and putting only the unique, ripe apples into a new bowl. Set comprehension does this filtering and unique collection in one quick step.

Key Concepts:
    - {expression for item in iterable}
    - Conditional filtering
    - Mapping and transformation
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_syntax():
    # Traditional way to create a set from squares
    squares_loop = set()
    for x in range(5):
        squares_loop.add(x**2)
        
    # Using set comprehension
    squares_comp = {x**2 for x in range(5)}
    
    print("Traditional:", squares_loop)
    print("Comprehension:", squares_comp)

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    # Example 1: Removing duplicates and transforming text
    words = ["hello", "WORLD", "Hello", "Python"]
    unique_lower = {w.lower() for w in words}
    print("Unique lowercased:", unique_lower)

    # Example 2: Filtering with if condition
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens = {n for n in numbers if n % 2 == 0}
    print("Even numbers set:", evens)

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    # Multiple conditionals / Nested loops
    # Create a set of tuples from two lists where items are not equal
    list_a = [1, 2]
    list_b = [2, 3]
    
    pairs = {(a, b) for a in list_a for b in list_b if a != b}
    print("Pairs:", pairs)
    
    # Using functions in the expression
    def categorize(n):
        return "even" if n % 2 == 0 else "odd"
        
    categories = {categorize(n) for n in range(5)}
    print("Categories:", categories)

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def mistakes_and_best_practices():
    # Mistake: Confusing set comprehension with dictionary comprehension
    # {k: v for ...} creates a dict, {v for ...} creates a set.
    
    my_set = {x for x in range(3)}
    my_dict = {x: x**2 for x in range(3)}
    
    print(type(my_set))
    print(type(my_dict))
    
    # Best Practice: Keep comprehensions readable. If they span multiple lines 
    # with complex nested logic, a standard loop might be clearer.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: How does a set comprehension handle duplicate results?
# A: It automatically ignores duplicates since the result is built as a set.
#
# Q2: Can you use nested if-else in a set comprehension?
# A: Yes, inline if-else operates on the expression, while trailing if acts as a filter.
#
# Q3: Is set comprehension faster than a for-loop with .add()?
# A: Yes, typically comprehensions run faster as they are optimized in C underneath.
#
# Q4: What happens if the expression yields an unhashable type?
# A: A TypeError is raised at runtime.
#
# Q5: How do you create an empty set with comprehension?
# A: You can't directly. Use set().

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

def practice():
    # Given a string, use set comprehension to find all unique vowels in it
    text = "education and programming"
    vowels = {char for char in text if char in 'aeiou'}
    print("Vowels found:", vowels)

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    # You have a list of file names. Extract just the unique extensions.
    files = ["script.py", "style.css", "index.html", "main.py", "app.js", "util.py"]
    
    extensions = {f.split('.')[-1] for f in files}
    return extensions

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
# - Syntax: {expression for item in iterable if condition}
# - Used to efficiently create sets and filter data simultaneously.
# - Highly readable and concise compared to loops.

if __name__ == "__main__":
    print("--- Section 1 ---")
    basic_syntax()
    print("\n--- Section 2 ---")
    practical_examples()
    print("\n--- Section 3 ---")
    advanced_usage()
    print("\n--- Section 4 ---")
    mistakes_and_best_practices()
    print("\n--- Section 6 ---")
    practice()
    print("\n--- Section 7 ---")
    print("Unique extensions:", mini_challenge())
