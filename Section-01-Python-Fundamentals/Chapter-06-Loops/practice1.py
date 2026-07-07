"""Learning file for Loop Challenge Practice."""

# Topic Name: Loop Challenge Practice
# Level: Beginner
# Loop Challenge Practice reinforces the chapter with runnable examples.
# Read the theory first, then run this file and modify examples.

# Theory
# Loop Challenge Practice reinforces the chapter with runnable examples.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# # See the runnable examples below for the topic syntax.

# Practice Programs
# 1. Print multiplication tables.
# 2. Find the sum of digits of a number.
# 3. Print triangle and square patterns.

# Mini Project
# Build a tiny program that uses loop challenge practice
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. When do you use for instead of while?
# A1. Use for when iterating over a known iterable; use while when repeating until a condition changes.
# Q2. What does continue do?
# A2. It skips the rest of the current loop iteration.

# Examples and practice implementations start below.
def fizz_buzz(limit):
    output = []
    for number in range(1, limit + 1):
        if number % 15 == 0:
            output.append("FizzBuzz")
        elif number % 3 == 0:
            output.append("Fizz")
        elif number % 5 == 0:
            output.append("Buzz")
        else:
            output.append(str(number))
    return output


def find_prime_numbers(limit):
    primes = []
    for candidate in range(2, limit + 1):
        for divisor in range(2, candidate):
            if candidate % divisor == 0:
                break
        else:
            primes.append(candidate)
    return primes


def practice_reverse_number(number):
    reversed_digits = 0
    while number > 0:
        reversed_digits = reversed_digits * 10 + number % 10
        number //= 10
    return reversed_digits


def main():
    print("--- Loop Challenge Practice ---")
    print("FizzBuzz:", fizz_buzz(15))
    print("Primes:", find_prime_numbers(10))
    print("Reverse:", practice_reverse_number(1234))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Loop Challenge Practice ---
# FizzBuzz: ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
# Primes: [2, 3, 5, 7]
# Reverse: 4321
# End Expected Output
