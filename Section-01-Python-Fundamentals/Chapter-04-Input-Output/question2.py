#Write a program that take a user input of three angles and will find out whether it can form a triangle or not.
a =int(input("enter point a angle \n"))
b=int(input("enter point b angle \n"))
c = int(input("enter point c angle \n"))

isTriangle= a + b + c

if 180 >= isTriangle:
    print(" triangle hai")
else:
    print("is not triagle hai")



# Problem 3: Profit or Loss

cost_price = float(input("Enter Cost Price: "))
selling_price = float(input("Enter Selling Price: "))

if selling_price > cost_price:
    print("Profit =", selling_price - cost_price)

elif cost_price > selling_price:
    print("Loss =", cost_price - selling_price)

else:
    print("No Profit No Loss")

# Problem 4: Menu Driven Program

while True:
    print("\n1. cm to ft")
    print("2. km to miles")
    print("3. USD to INR")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cm = float(input("Enter cm: "))
        ft = cm / 30.48
        print("Feet =", ft)

    elif choice == 2:
        km = float(input("Enter km: "))
        miles = km * 0.621371
        print("Miles =", miles)

    elif choice == 3:
        usd = float(input("Enter USD: "))
        inr = usd * 83   # Approx rate
        print("INR =", inr)

    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")

# Problem 5: Fibonacci Series up to 10 terms

a = 0
b = 1

print(a, end=" ")
print(b, end=" ")

for i in range(8):
    c = a + b
    print(c, end=" ")
    a = b
    b = c

# Problem 6: Factorial of a Number

num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)

# Problem 7: Reverse an Integer

num = int(input("Enter number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse =", reverse)

# Problem 8: Sum from 1 to N (skip divisible by 5, stop if sum > 300)

n = int(input("Enter N: "))

i = 1
total = 0

while i <= n:

    if i % 5 == 0:
        i += 1
        continue

    total += i

    if total > 300:
        break

    i += 1

print(total)

# Problem 9: Sum and Average until user enters 0

total = 0
count = 0

while True:
    num = int(input("Enter number: "))

    if num == 0:
        break

    total += num
    count += 1

if count > 0:
    average = total / count
else:
    average = 0

print("Sum =", total)
print("Average =", average)

# Problem 9: Numbers divisible by 7 but not multiple of 5

for i in range(2000, 3201):

    if i % 7 == 0 and i % 5 != 0:
        print(i, end=",")

# Problem 10: Numbers whose every digit is even

for num in range(1000, 3001):

    temp = str(num)

    if (int(temp[0]) % 2 == 0 and
        int(temp[1]) % 2 == 0 and
        int(temp[2]) % 2 == 0 and
        int(temp[3]) % 2 == 0):

        print(num, end=" ")

# Problem 11: Robot Distance from Origin

import math

x = 0
y = 0

while True:

    move = input()

    if move == "!":
        break

    direction, steps = move.split()
    steps = int(steps)

    if direction == "UP":
        y += steps

    elif direction == "DOWN":
        y -= steps

    elif direction == "LEFT":
        x -= steps

    elif direction == "RIGHT":
        x += steps

distance = math.sqrt(x**2 + y**2)

print(round(distance))

# Problem 12: Prime Number Check

num = int(input("Enter number: "))

if num <= 1:
    print("Not Prime")

else:
    prime = True

    for i in range(2, num):

        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime")

    else:
        print("Not Prime")

# Problem 13: Armstrong Numbers in a Range

start = int(input("Enter start: "))
end = int(input("Enter end: "))

for num in range(start, end + 1):

    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp = temp // 10

    if total == num:
        print(num)

# Problem 14: Angle Between Hour and Minute Hand

hour = int(input("Enter Hour: "))
minute = int(input("Enter Minute: "))

hour_angle = (hour * 30) + (minute * 0.5)
minute_angle = minute * 6

angle = abs(hour_angle - minute_angle)

final_angle = min(angle, 360 - angle)

print(int(final_angle))

# Problem 15: Rectangle Overlap Check

# Rectangle 1
l1x = int(input("Enter L1 x: "))
l1y = int(input("Enter L1 y: "))
r1x = int(input("Enter R1 x: "))
r1y = int(input("Enter R1 y: "))

# Rectangle 2
l2x = int(input("Enter L2 x: "))
l2y = int(input("Enter L2 y: "))
r2x = int(input("Enter R2 x: "))
r2y = int(input("Enter R2 y: "))

if l1x > r2x or l2x > r1x:
    print("Not Overlapping")

elif r1y > l2y or r2y > l1y:
    print("Not Overlapping")

else:
    print("Overlapping")

