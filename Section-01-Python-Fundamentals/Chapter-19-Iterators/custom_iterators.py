"""
Topic: Custom Iterators
Chapter: 19
Level: Intermediate

Description:
    While Python provides many built-in iterators, you can also define your own custom iterators by creating classes that implement both `__iter__()` and `__next__()` methods. This allows you to create memory-efficient objects that generate values on the fly, which is perfect for representing infinite sequences or large datasets.

Real-Life Analogy:
    Imagine a custom ticket machine at a bakery. The machine itself is the iterator. It remembers the last ticket number it gave out (its state). When you press the button (`__next__()`), it increments the number, gives you the new ticket, and remembers this new state for the next customer.

Key Concepts:
    - Implementing `__iter__()` (returns `self`)
    - Implementing `__next__()`
    - Managing internal state
    - Raising `StopIteration`
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

class Counter:
    """A custom iterator that counts from a start value to an end value."""
    def __init__(self, start: int, end: int):
        self.current = start
        self.end = end
        
    def __iter__(self):
        # An iterator must return itself in __iter__
        return self
        
    def __next__(self):
        # If we have passed the end, stop iterating
        if self.current > self.end:
            raise StopIteration
            
        # Otherwise, save the current value, increment state, and return the value
        value = self.current
        self.current += 1
        return value

def basic_custom_iterator_demo() -> None:
    print("--- Section 1: Basic Custom Iterator ---")
    counter = Counter(1, 5)
    
    # We can use our custom iterator in a standard for loop
    for num in counter:
        print(num, end=" ")
    print("\n")


# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

class FibIterator:
    """An iterator that generates Fibonacci numbers up to a certain maximum limit."""
    def __init__(self, max_limit: int):
        self.max_limit = max_limit
        self.a = 0
        self.b = 1
        
    def __iter__(self):
        return self
        
    def __next__(self):
        fib = self.a
        if fib > self.max_limit:
            raise StopIteration
            
        # Update state for the next calculation
        self.a, self.b = self.b, self.a + self.b
        return fib

def practical_examples() -> None:
    print("--- Section 2: Practical Examples ---")
    print("Fibonacci sequence up to 50:")
    fib_gen = FibIterator(50)
    for num in fib_gen:
        print(num, end=" ")
    print("\n")


# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

class InfinitePowerOfTwo:
    """An infinite iterator generating powers of two."""
    def __init__(self):
        self.exponent = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        result = 2 ** self.exponent
        self.exponent += 1
        return result

def advanced_infinite_iterator() -> None:
    print("--- Section 3: Advanced Usage (Infinite Iterators) ---")
    powers = InfinitePowerOfTwo()
    
    print("First 8 powers of two:")
    for _ in range(8):
        print(next(powers), end=" ")
    print("\n")
    # Note: Using this in a for loop without a break condition would run forever!


# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes() -> None:
    print("--- Section 4: Common Mistakes ---")
    
    # Mistake: Forgetting to return self in __iter__
    class BrokenIterator:
        def __init__(self):
            self.val = 0
        def __iter__(self):
            pass # Forgot to return self!
        def __next__(self):
            self.val += 1
            if self.val > 3: raise StopIteration
            return self.val
            
    try:
        b = BrokenIterator()
        for i in b:
            print(i)
    except TypeError as e:
        print(f"Error caught due to missing return self: {e}")

    # Best Practice: Always ensure __iter__ returns self, and __next__ handles StopIteration.


# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: How do you make a custom class iterable and behave like an iterator?
A1: You must implement both the `__iter__()` method (which should return `self`) and the `__next__()` method (which calculates and returns the next value, or raises `StopIteration`).

Q2: Why must an iterator's `__iter__` method return `self`?
A2: Because many Python constructs (like `for` loops) call `iter()` on the object first. By returning `self`, the iterator tells Python "I am already an iterator, use me directly."

Q3: What happens if `__next__` does not raise `StopIteration`?
A3: The iterator will become an infinite iterator. A `for` loop consuming it will run forever unless it contains a `break` statement.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
"""
Exercise 1:
Create a custom iterator `EvenNumbers` that takes a `max_val`. It should yield all even numbers from 0 up to `max_val`.

Exercise 2:
Create an iterator `ReverseString` that takes a string and yields its characters in reverse order.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================
"""
Challenge: Build a `PrimeIterator` that generates prime numbers indefinitely. 
Use it to print the first 10 prime numbers.
"""

class PrimeIterator:
    def __init__(self):
        self.current = 2
        
    def __iter__(self):
        return self
        
    def _is_prime(self, n: int) -> bool:
        if n < 2: return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0: return False
        return True
        
    def __next__(self):
        while not self._is_prime(self.current):
            self.current += 1
        
        prime_to_return = self.current
        self.current += 1
        return prime_to_return

def mini_challenge() -> None:
    print("\n--- Section 7: Mini Challenge Demo ---")
    primes = PrimeIterator()
    print("First 10 primes:")
    for _ in range(10):
        print(next(primes), end=" ")
    print()


# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- Custom iterators allow you to define custom iteration logic and memory-efficient sequences.
- You must implement `__iter__()` (returning `self`) and `__next__()`.
- State is maintained using instance variables initialized in `__init__()`.
- Infinite iterators are possible and useful, provided you control their consumption.
"""

if __name__ == "__main__":
    basic_custom_iterator_demo()
    practical_examples()
    advanced_infinite_iterator()
    common_mistakes()
    mini_challenge()
