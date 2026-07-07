# Topic: Generator Expressions
# Explanation: Generator expressions are compact one-line generators.

# Syntax:
# squares = (x * x for x in range(3))
print(next(squares))

# Examples:
# squares = (x * x for x in range(3))
print(next(squares))
print(next(squares))

# Practice Programs:
# 1. Create a generator expression for even numbers.
2. Use next() to consume values.

# Interview Questions:
# Q: How is a generator expression different from a list comprehension?
A: It is lazy and does not store all values at once.

# Expected Output:
# 0
1

squares = (x * x for x in range(3))
print(next(squares))
print(next(squares))
