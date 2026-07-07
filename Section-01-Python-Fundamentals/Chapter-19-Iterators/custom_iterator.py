"""Learning file for Custom Iterators."""

# Topic Name: Custom Iterators
# Level: Advanced
# Custom iterators define __iter__ and __next__ to control iteration behavior.
# Read the theory first, then run this file and modify examples.

# Theory
# Custom iterators define __iter__ and __next__ to control iteration behavior.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# def __iter__(self): return self
# def __next__(self): ...

# Practice Programs
# 1. Use iter() and next() manually.
# 2. Build a countdown iterator.
# 3. Explain StopIteration in your own words.

# Mini Project
# Build a tiny program that uses custom iterators
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What protocol powers for loops?
# A1. The iterator protocol: __iter__ returns an iterator and __next__ returns values.
# Q2. What ends iteration?
# A2. Raising StopIteration.

# Examples and practice implementations start below.
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


def example_custom_iterator():
    print("Countdown:", list(Countdown(3)))


def practice_range_iterator(start, stop):
    class SimpleRange:
        def __init__(self, start_value, stop_value):
            self.current = start_value
            self.stop = stop_value

        def __iter__(self):
            return self

        def __next__(self):
            if self.current >= self.stop:
                raise StopIteration
            value = self.current
            self.current += 1
            return value

    return list(SimpleRange(start, stop))


def main():
    print("--- Custom Iterators ---")
    example_custom_iterator()
    print("Range:", practice_range_iterator(2, 5))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Custom Iterators ---
# Countdown: [3, 2, 1, 0]
# Range: [2, 3, 4]
# End Expected Output
