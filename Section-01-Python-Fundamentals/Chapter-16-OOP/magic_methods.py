# Topic: Magic Methods
# Explanation: Magic methods let objects integrate with Python syntax.

# Syntax:
# class Book:
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f"Book({self.title})"

print(Book("Python"))

# Examples:
# class Book:
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f"Book({self.title})"

print(Book("Python"))

# Practice Programs:
# 1. Implement __repr__ for a class.
2. Implement __len__ for a class.

# Interview Questions:
# Q: What are magic methods?
A: They are special methods with double underscores used by Python internals.

# Expected Output:
# Book(Python)

class Book:
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f"Book({self.title})"

print(Book("Python"))
