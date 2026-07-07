# Topic: Identity Operators
# Explanation: Identity operators check whether two variables point to the same object.

# Syntax:
# a = [1, 2]
b = a
print(a is b)

# Examples:
# a = [1, 2]
b = a
c = [1, 2]
print(a is b)
print(a is c)

# Practice Programs:
# 1. Compare two equal integers using is.
2. Compare two different lists.

# Interview Questions:
# Q: What is the difference between == and is?
A: == checks equality of values, while is checks object identity.

# Expected Output:
# True
False

a = [1, 2]
b = a
c = [1, 2]
print(a is b)
print(a is c)
