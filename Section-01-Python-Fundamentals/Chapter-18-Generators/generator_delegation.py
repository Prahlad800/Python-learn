"""
Topic: Generator Delegation (yield from)
Chapter: 18
Level: Advanced

Description:
    The `yield from` statement allows a generator to delegate part of its operations to 
    another generator or iterable. It establishes a transparent bidirectional connection 
    between the caller and the sub-generator, automatically handling `next()`, `send()`, 
    `throw()`, and `close()`.

Real-Life Analogy:
    Imagine a manager (main generator) delegating a task to an employee (sub-generator). 
    Whenever a client asks for updates (next), the manager transparently forwards the 
    request to the employee. Any feedback (send) from the client goes directly to the employee.

Key Concepts:
    - Yielding from an iterable
    - Sub-generators
    - Two-way delegation channels
"""
from typing import Iterator, Generator, Any

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def simple_generator() -> Iterator[int]:
    """Without yield from."""
    for i in range(3):
        yield i

def delegated_generator() -> Iterator[int]:
    """With yield from."""
    # This automatically yields all values from the range
    yield from range(3)

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def flatten_list(nested_list: list) -> Iterator[Any]:
    """Recursively flattens a nested list using yield from."""
    for item in nested_list:
        if isinstance(item, list):
            # Recursively delegate to the sub-list
            yield from flatten_list(item)
        else:
            yield item

def read_files(filenames: list[str]) -> Iterator[str]:
    """Delegates yielding lines to file objects."""
    # Simulating file objects with lists of strings
    mock_files = {
        "file1.txt": ["line 1", "line 2"],
        "file2.txt": ["line 3", "line 4"]
    }
    
    for filename in filenames:
        if filename in mock_files:
            # Iterating through the file lines directly
            yield from mock_files[filename]

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# yield from establishes a transparent 2-way pipe for .send()

def sub_coroutine() -> Generator[str, str, str]:
    """A sub-generator that receives values."""
    result = ""
    while True:
        received = yield "Waiting for data..."
        if received is None:
            break
        result += received
    # The return value of a generator becomes the value of the `yield from` expression
    return f"Final Data: {result}"

def main_coroutine() -> Generator[str, str, None]:
    """Delegates to the sub-generator."""
    print("Main coroutine started.")
    
    # Blocks here, delegating all yield/send to sub_coroutine.
    # When sub_coroutine returns, the result is captured.
    final_result = yield from sub_coroutine()
    
    print(f"Main coroutine received result: {final_result}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Using a loop instead of `yield from` when yielding from another generator.
# Correction: Replace `for item in gen: yield item` with `yield from gen`. It is cleaner 
# and handles edge cases (like .send() and exceptions) automatically.

# Best Practice: Use `yield from` when writing recursive generators (like walking a directory tree).

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is the main advantage of `yield from`?
# A1: It replaces boilerplate nested loops and establishes a transparent bidirectional 
#     channel between the caller and sub-generator.
#
# Q2: Can `yield from` be used on any iterable?
# A2: Yes, it can be used on lists, strings, ranges, and other generators.
#
# Q3: How do you capture the `return` value of a generator using `yield from`?
# A3: By assigning it: `result = yield from sub_gen()`.
#
# Q4: What happens if the caller calls `.send()` on the main generator during `yield from`?
# A4: The value is sent directly into the sub-generator.
#
# Q5: Does `yield from` handle `StopIteration` automatically?
# A5: Yes, it catches `StopIteration` and extracts the return value.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a generator that yields from a string, a list, and a tuple consecutively.
# Exercise 2: Use `yield from` to write a generator that yields all permutations of a string.
# Exercise 3: Create a recursive generator using `yield from` to extract values from nested dictionaries.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge: Write a generator `chain_iterables(*iterables)` that takes an arbitrary number
# of iterables and yields all their elements sequentially using `yield from`.

def chain_iterables(*iterables: Iterable) -> Iterator[Any]:
    """Chains multiple iterables together."""
    for iterable in iterables:
        yield from iterable

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - `yield from` simplifies yielding items from an iterable or sub-generator.
# - It is highly useful for recursive generators.
# - It automatically pipes `.send()`, `.throw()`, and `.close()` to the sub-generator.
# - It can capture the `return` value of a sub-generator.

if __name__ == "__main__":
    from typing import Iterable
    
    print("--- Basic Delegation ---")
    print(list(delegated_generator()))
    
    print("\n--- Flatten List ---")
    nested = [1, [2, 3, [4, 5]], 6, [7]]
    print(list(flatten_list(nested)))
    
    print("\n--- Two-way Delegation ---")
    main_gen = main_coroutine()
    print(next(main_gen)) # Prime, output: Waiting for data...
    print(main_gen.send("A"))
    print(main_gen.send("B"))
    try:
        main_gen.send(None) # Signal termination
    except StopIteration:
        pass
        
    print("\n--- Mini Challenge ---")
    print(list(chain_iterables("ABC", [1, 2, 3], (4.4, 5.5))))
