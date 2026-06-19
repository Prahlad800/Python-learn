# =========================
# CONDITIONAL OPERATORS IN PYTHON
# =========================

a = 10
b = 20

# 1. Equal To (==)
print("Equal To")
print(a == b)   # False

# 2. Not Equal To (!=)
print("Not Equal To")
print(a != b)   # True

# 3. Greater Than (>)
print("Greater Than")
print(a > b)    # False

# 4. Less Than (<)
print("Less Than")
print(a < b)    # True

# 5. Greater Than or Equal To (>=)
print("Greater Than or Equal To")
print(a >= b)   # False

# 6. Less Than or Equal To (<=)
print("Less Than or Equal To")
print(a <= b)   # True



# =========================
# CONDITIONAL STATEMENTS
# =========================

age = 18

# 1. if condition
if age >= 18:
    print("Adult")


# 2. if else condition
num = 5

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 3. if elif else condition
marks = 75

if marks >= 90:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")


# =========================
# LOGICAL OPERATORS
# =========================

x = 15

# AND operator
if x > 10 and x < 20:
    print("x is between 10 and 20")


# OR operator
if x < 5 or x > 10:
    print("Condition True")


# NOT operator
is_logged_in = False

if not is_logged_in:
    print("Please Login")


# =========================
# NESTED IF
# =========================

salary = 50000
experience = 3

if salary > 30000:

    if experience >= 2:
        print("Eligible")

    else:
        print("Experience Required")

else:
    print("Low Salary")