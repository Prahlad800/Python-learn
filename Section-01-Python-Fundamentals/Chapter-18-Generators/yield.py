# Topic: yield Keyword
# Explanation: yield pauses a function and returns a value.

# Syntax:
# def simple_generator():
    yield "A"
    yield "B"

for item in simple_generator():
    print(item)

# Examples:
# def simple_generator():
    yield "A"
    yield "B"

for item in simple_generator():
    print(item)

# Practice Programs:
# 1. Write a generator that yields vowels.
2. Consume it with a loop.

# Interview Questions:
# Q: What does yield do?
A: It produces a value and pauses execution until the next request.

# Expected Output:
# A
B

def simple_generator():
    yield "A"
    yield "B"

for item in simple_generator():
    print(item)
