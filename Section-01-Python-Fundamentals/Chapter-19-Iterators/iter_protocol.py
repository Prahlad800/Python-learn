"""
Topic: Iterator Protocol
Chapter: 19
Level: Beginner

Description:
    The Iterator Protocol is the foundation of iteration in Python. It consists of two essential methods: `__iter__()` and `__next__()`. When you use a `for` loop, Python automatically handles these methods behind the scenes. Understanding how to use `iter()` and `next()` manually gives you deeper insight into how loops work in Python.

Real-Life Analogy:
    Imagine a Pez dispenser. The dispenser itself is the object (the iterable). When you pull back the head to get a piece of candy, you are asking for the next item. The dispenser gives you one piece at a time (`__next__()`), and when it's empty, it stops dispensing (raises StopIteration).

Key Concepts:
    - iter() function calling __iter__()
    - next() function calling __next__()
    - StopIteration exception
    - Consuming an iterator
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_iterator_demo() -> None:
    """Demonstrate the fundamental use of iter() and next()."""
    print("--- Section 1: Basic Iterator Demo ---")
    
    # Let's start with a simple list, which is an iterable
    my_list = [10, 20, 30]
    
    # We get an iterator from the iterable using iter()
    my_iterator = iter(my_list)
    print(f"List type: {type(my_list)}")
    print(f"Iterator type: {type(my_iterator)}")
    
    # We retrieve the next item using next()
    item1 = next(my_iterator)
    print(f"First item: {item1}")
    
    item2 = next(my_iterator)
    print(f"Second item: {item2}")
    
    item3 = next(my_iterator)
    print(f"Third item: {item3}")
    
    # The iterator is now exhausted. Calling next() again will raise StopIteration
    try:
        next(my_iterator)
    except StopIteration:
        print("StopIteration caught! The iterator is empty.")


# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def file_reading_example() -> None:
    """Demonstrate how iterators are used for reading files line by line."""
    print("\n--- Section 2: Practical Examples ---")
    
    # Creating a temporary file for the example
    with open("temp_iter_file.txt", "w") as f:
        f.write("Line 1: Hello\nLine 2: World\nLine 3: Python")
        
    # File objects are iterators themselves
    with open("temp_iter_file.txt", "r") as f:
        print("Reading first line using next():", next(f).strip())
        print("Reading second line using next():", next(f).strip())
        print("Reading third line using next():", next(f).strip())
        
        try:
            next(f)
        except StopIteration:
            print("Reached end of file.")


def default_values_with_next() -> None:
    """Show how to use default values with next() to avoid StopIteration."""
    colors = ["red", "green"]
    color_iter = iter(colors)
    
    print(f"Next color: {next(color_iter, 'black')}")  # prints red
    print(f"Next color: {next(color_iter, 'black')}")  # prints green
    # Doesn't raise StopIteration because default 'black' is provided
    print(f"Next color: {next(color_iter, 'black')}")  # prints black


# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def simulating_a_for_loop() -> None:
    """Simulate exactly how a for loop uses the iterator protocol internally."""
    print("\n--- Section 3: Advanced Usage (Simulating for-loop) ---")
    
    numbers = [1, 2, 3, 4, 5]
    
    # This is what python does when you write: for num in numbers:
    
    # 1. Get the iterator
    iterator = iter(numbers)
    
    # 2. Start an infinite loop
    while True:
        try:
            # 3. Get the next item
            item = next(iterator)
            
            # 4. Execute the loop body
            print(f"Processed: {item * 10}")
            
        except StopIteration:
            # 5. Break out of the loop when empty
            break

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes() -> None:
    """Illustrate common pitfalls when working with iterators."""
    print("\n--- Section 4: Common Mistakes ---")
    
    # Mistake 1: Trying to reuse an exhausted iterator
    nums = [1, 2, 3]
    num_iter = iter(nums)
    
    print("First pass:")
    for n in num_iter:
        print(n, end=" ")
    print()
        
    print("Second pass (will be empty):")
    for n in num_iter:  # This loop won't execute because num_iter is exhausted
        print(n, end=" ")
    print()
    
    # Best Practice: Always recreate the iterator or iterate over the iterable directly
    print("Correct second pass:")
    for n in nums:
        print(n, end=" ")
    print()

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: What are the two methods that form the iterator protocol?
A1: __iter__() and __next__(). __iter__() returns the iterator object itself, and __next__() returns the next value.

Q2: How does a `for` loop work internally in Python?
A2: A `for` loop calls `iter()` on the object to get an iterator, then repeatedly calls `next()` to get values until a `StopIteration` exception is raised, which it catches silently to end the loop.

Q3: What happens when an iterator is exhausted?
A3: It raises a `StopIteration` exception on any subsequent calls to `next()`.

Q4: Can you restart an iterator?
A4: No, standard iterators in Python are one-way and cannot be restarted or reset. You must create a new iterator from the original iterable.

Q5: What is the difference between an iterable and an iterator?
A5: An iterable is an object that has an `__iter__()` method which returns an iterator. An iterator is an object that has both `__iter__()` and `__next__()` methods.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
"""
Exercise 1: 
Create a string "Python". Use `iter()` to get an iterator for the string, and manually call `next()` to print each character one by one. Catch the StopIteration.

Exercise 2:
Write a function `safe_next(iterator, default)` that takes an iterator and a default value, and returns the next item or the default if empty, without using the built-in default argument of `next()`. (Use try/except).
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================
"""
Challenge: Write a function `chunk_iterator(iterable, chunk_size)` that takes an iterable and yields lists of size `chunk_size` manually using the iterator protocol (without using generators if possible, or simulating it with manual iter/next calls).
"""

def chunk_iterator_demo() -> None:
    print("\n--- Section 7: Mini Challenge Demo ---")
    data = [1, 2, 3, 4, 5, 6, 7, 8]
    chunk_size = 3
    
    it = iter(data)
    while True:
        chunk = []
        try:
            for _ in range(chunk_size):
                chunk.append(next(it))
            print(f"Chunk: {chunk}")
        except StopIteration:
            if chunk:
                print(f"Final partial chunk: {chunk}")
            break


# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- The iterator protocol consists of `__iter__()` and `__next__()`.
- `iter()` fetches an iterator from an iterable.
- `next()` fetches the next element from an iterator.
- When no more items are available, a `StopIteration` exception is raised.
- Iterators are consumed upon iteration and cannot be reused.
"""

if __name__ == "__main__":
    basic_iterator_demo()
    file_reading_example()
    default_values_with_next()
    simulating_a_for_loop()
    common_mistakes()
    chunk_iterator_demo()
    
    # Cleanup temp file
    import os
    if os.path.exists("temp_iter_file.txt"):
        os.remove("temp_iter_file.txt")
