"""
Topic: String Performance (join vs +)
Chapter: 8
Level: Advanced

Description:
    Because strings are immutable in Python, operations that modify strings actually create new objects.
    Understanding how this impacts memory and performance is crucial for writing efficient Python code, especially with large datasets.

Real-Life Analogy:
    Imagine carving a statue out of stone (immutable). Every time you want to make a change, you have to throw away the statue and carve a completely new one from scratch.

Key Concepts:
    - String Immutability and memory overhead
    - Using `+` operator in loops
    - Using `str.join()` for efficient concatenation
    - Using `io.StringIO`
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

import time

def bad_concatenation(n):
    """Using + in a loop creates many intermediate strings."""
    result = ""
    for i in range(n):
        result += str(i) # Creates a new string every iteration
    return result

def good_concatenation(n):
    """Using join() is much more efficient."""
    parts = []
    for i in range(n):
        parts.append(str(i))
    return "".join(parts) # Creates the string once at the end

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def performance_comparison():
    """Comparing execution time of + vs join."""
    n = 100000
    
    start = time.time()
    bad_concatenation(n)
    end = time.time()
    print(f"Using '+': {(end - start):.4f} seconds")
    
    start = time.time()
    good_concatenation(n)
    end = time.time()
    print(f"Using 'join': {(end - start):.4f} seconds")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

import io

def using_stringio():
    """StringIO provides file-like interface for string buffers."""
    buffer = io.StringIO()
    buffer.write("Hello")
    buffer.write(" ")
    buffer.write("World")
    
    # Retrieve the entire string
    result = buffer.getvalue()
    buffer.close()
    
    print("Result from StringIO:", result)

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Using `+=` to build a large string line by line.
# Best Practice: Collect lines in a list, then return `'\\n'.join(lines)`.

# Best Practice: If you need to write to strings like files (e.g., for mock objects or generating large logs), use `io.StringIO`.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q: Why is concatenating strings with `+` in a loop considered bad practice in Python?
A: Strings are immutable. `+=` creates a new string object and copies the old content every iteration, leading to O(N^2) time complexity.

Q: Why is `join()` faster?
A: `join()` calculates the total memory needed for the final string beforehand and allocates it once, resulting in O(N) time complexity.

Q: Does Python optimize `+=`?
A: CPython does have an optimization for `+=` if there are no other references to the string, making it sometimes behave like an in-place operation, but it is not guaranteed across implementations (like PyPy or Jython) and shouldn't be relied upon for large scale.

Q: What is `io.StringIO`?
A: An in-memory file-like object for reading and writing strings.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# 1. Write a function using list comprehension and `join()` to concatenate the alphabet a thousand times.
# 2. Refactor a loop that uses `+=` to build an HTML list (`<ul><li>...</li></ul>`) to use `.join()`.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """Generate a CSV string of 1000 rows efficiently."""
    headers = ["ID", "Name", "Score"]
    
    # Efficient approach
    rows = [",".join(headers)]
    
    for i in range(1, 1000):
        # We can mix f-strings and lists!
        row = f"{i},User{i},{i*10}"
        rows.append(row)
        
    final_csv = "\n".join(rows)
    print("CSV generation complete. Length:", len(final_csv))

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Avoid `+=` for string concatenation in large loops.
- Use `"".join(list_of_strings)` for O(N) performance.
- Use list comprehensions or generators in conjunction with `join()`.
- Use `io.StringIO` for complex memory-buffer string writing.
"""

if __name__ == "__main__":
    performance_comparison()
    using_stringio()
    mini_challenge()
