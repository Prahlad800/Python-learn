# Topic: Generators
# Explanation: Generators produce values one at a time and save memory.

# Syntax:
# def count_up(n):
    for i in range(n):
        yield i

for value in count_up(3):
    print(value)

# Examples:
# def count_up(n):
    for i in range(n):
        yield i

for value in count_up(3):
    print(value)

# Practice Programs:
# 1. Create a generator for even numbers.
2. Iterate over it.

# Interview Questions:
# Q: What is the advantage of generators?
A: They save memory by producing values lazily.

# Expected Output:
# 0
1
2

def count_up(n):
    for i in range(n):
        yield i

for value in count_up(3):
    print(value)
