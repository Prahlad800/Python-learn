# Topic: Custom Iterators
# Explanation: You can define your own iterator using __iter__ and __next__.

# Syntax:
# class Counter:
    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        if self.a < 3:
            self.a += 1
            return self.a
        raise StopIteration

for value in Counter():
    print(value)

# Examples:
# class Counter:
    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        if self.a < 3:
            self.a += 1
            return self.a
        raise StopIteration

for value in Counter():
    print(value)

# Practice Programs:
# 1. Build an iterator that yields 1, 2, 3.
2. Stop iteration properly.

# Interview Questions:
# Q: What is __next__ used for?
A: It returns the next value and signals completion by raising StopIteration.

# Expected Output:
# 1
2
3

class Counter:
    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        if self.a < 3:
            self.a += 1
            return self.a
        raise StopIteration

for value in Counter():
    print(value)
