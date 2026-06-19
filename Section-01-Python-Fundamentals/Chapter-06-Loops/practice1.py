# =========================
# ALL LOOPS IN PYTHON
# =========================


# =========================
# 1. FOR LOOP
# =========================

print("FOR LOOP")

for i in range(1, 6):
    print(i)


# =========================
# 2. WHILE LOOP
# =========================

print("\nWHILE LOOP")

num = 1

while num <= 5:
    print(num)
    num += 1


# =========================
# 3. NESTED LOOP
# =========================

print("\nNESTED LOOP")

for i in range(1, 4):

    for j in range(1, 4):
        print(i, j)


# =========================
# 4. LOOP WITH STRING
# =========================

print("\nSTRING LOOP")

name = "Python"

for char in name:
    print(char)


# =========================
# 5. LOOP WITH LIST
# =========================

print("\nLIST LOOP")

numbers = [10, 20, 30, 40]

for item in numbers:
    print(item)


# =========================
# 6. BREAK
# =========================

print("\nBREAK")

for i in range(1, 10):

    if i == 5:
        break

    print(i)


# =========================
# 7. CONTINUE
# =========================

print("\nCONTINUE")

for i in range(1, 10):

    if i == 5:
        continue

    print(i)


# =========================
# 8. PASS
# =========================

print("\nPASS")

for i in range(1, 5):

    if i == 3:
        pass

    print(i)


# =========================
# 9. ELSE WITH LOOP
# =========================

print("\nELSE WITH LOOP")

for i in range(1, 5):
    print(i)

else:
    print("Loop Finished")


# =========================
# 10. INFINITE WHILE LOOP
# =========================

# WARNING:
# Ye loop kabhi stop nahi hota
# CTRL + C se band karna padega

# while True:
#     print("Running...")


# =========================
# 11. REVERSE LOOP
# =========================

print("\nREVERSE LOOP")

for i in range(10, 0, -1):
    print(i)


# =========================
# 12. ENUMERATE LOOP
# =========================

print("\nENUMERATE LOOP")

fruits = ["Apple", "Banana", "Mango"]

for index, value in enumerate(fruits):
    print(index, value)


# =========================
# 13. ZIP LOOP
# =========================

print("\nZIP LOOP")

names = ["Ram", "Shyam", "Mohan"]
marks = [80, 90, 70]

for n, m in zip(names, marks):
    print(n, m)


# =========================
# 14. LOOP WITH DICTIONARY
# =========================

print("\nDICTIONARY LOOP")

student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python"
}

for key, value in student.items():
    print(key, value)