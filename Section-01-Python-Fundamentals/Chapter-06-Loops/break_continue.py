# Topic: break and continue
# Explanation: break exits the loop, and continue skips the current iteration.

# Syntax:
# for i in range(5):
    if i == 3:
        continue
    print(i)

# Examples:
# for i in range(5):
    if i == 3:
        continue
    print(i)

# Practice Programs:
# 1. Skip printing the number 2.
2. Stop when you reach 7.

# Interview Questions:
# Q: When would you use continue?
A: When you want to skip some iterations but continue the loop.

# Expected Output:
# 0
1
2
4

for i in range(5):
    if i == 3:
        continue
    print(i)
