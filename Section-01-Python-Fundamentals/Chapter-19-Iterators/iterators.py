# Topic: Iterators
# Explanation: Iterators traverse collections one element at a time.

# Syntax:
# nums = [1, 2, 3]
iterator = iter(nums)
print(next(iterator))

# Examples:
# nums = [1, 2, 3]
iterator = iter(nums)
print(next(iterator))
print(next(iterator))

# Practice Programs:
# 1. Create an iterator from a tuple.
2. Use next() multiple times.

# Interview Questions:
# Q: What is the difference between an iterable and an iterator?
A: An iterable can produce an iterator; an iterator holds the current position.

# Expected Output:
# 1
2

nums = [1, 2, 3]
iterator = iter(nums)
print(next(iterator))
print(next(iterator))
