"""
Topic: Generator send() Method
Chapter: 18
Level: Advanced

Description:
    Generators don't just produce values; they can also consume them. The `.send()` method
    allows you to pass a value back into the generator at the exact point where it yielded.
    This bidirectional communication turns generators into basic coroutines.

Real-Life Analogy:
    Imagine a chef (generator) passing a dish (yield) to a waiter (caller). The waiter
    takes the dish, but also hands the chef a new ingredient (send) to use in the next dish.

Key Concepts:
    - Yield as an expression: val = yield
    - generator.send(value)
    - Priming the generator with next() or send(None)
"""
from typing import Generator

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def simple_coroutine() -> Generator[str, str, None]:
    """A generator that receives data via send()."""
    print("Coroutine started.")
    # The yield acts as an expression. It pauses, yields "Ready", 
    # and waits for a value to be sent back.
    received = yield "Ready"
    print(f"Coroutine received: {received}")
    
    yield "Done"

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def math_coroutine() -> Generator[int, int, None]:
    """A coroutine that multiplies received values."""
    print("Math coroutine started.")
    result = 0
    while True:
        # Yield the current result, wait for an input multiplier
        multiplier = yield result
        if multiplier is None:
            break
        result += multiplier * 10

def average_coroutine() -> Generator[float, float, None]:
    """Calculates running average based on sent values."""
    total = 0.0
    count = 0
    average = 0.0
    while True:
        new_val = yield average
        if new_val is None:
            break
        total += new_val
        count += 1
        average = total / count

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def controlled_robot() -> Generator[str, str, None]:
    """A state machine controlled via send()."""
    state = "IDLE"
    while True:
        command = yield state
        if command == "START":
            state = "RUNNING"
        elif command == "STOP":
            state = "IDLE"
        elif command == "DIE":
            state = "DEAD"
            yield state
            break
        else:
            state = "UNKNOWN COMMAND"

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Using .send(value) before priming the generator.
# Correction: You MUST prime the generator first by calling `next(gen)` or `gen.send(None)`.
# Otherwise, there is no `yield` expression waiting to receive the value.

# Best Practice: Always handle termination gracefully, often by listening for a specific
# sentinel value (like None) to break the loop.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is the purpose of `.send()` in a generator?
# A1: It allows the caller to pass data back into the paused generator.
#
# Q2: What must you do before calling `.send(value)` for the first time?
# A2: You must prime the generator by calling `next()` or `.send(None)`.
#
# Q3: What happens if you call `.send()` on a generator that just started?
# A3: It raises a TypeError: can't send non-None value to a just-started generator.
#
# Q4: What does `.close()` do to a generator?
# A4: It raises a GeneratorExit exception inside the generator at the yield point, terminating it.
#
# Q5: How is a generator with `.send()` different from a regular generator?
# A5: Regular generators only produce data. Generators using `.send()` consume and produce data.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a coroutine that receives strings and yields their uppercase versions.
# Exercise 2: Write a coroutine that maintains a list of items. Send items to add them, and yield the list length.
# Exercise 3: Create a generator that toggles between adding and subtracting sent values.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge: Write a coroutine `bank_account(balance)` that allows deposits and withdrawals.
# Send positive integers to deposit, negative to withdraw. Yield the current balance.

def bank_account(balance: int) -> Generator[int, int, None]:
    """A bank account coroutine."""
    while True:
        transaction = yield balance
        if transaction is None:
            break
        balance += transaction

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - `yield` can be used as an expression (e.g., val = yield).
# - `.send(val)` passes data into the generator.
# - Generators must be primed with `next()` before receiving data.
# - This forms the foundation for coroutines and asynchronous programming in Python.

if __name__ == "__main__":
    print("--- Simple Coroutine ---")
    gen = simple_coroutine()
    print("Yielded:", next(gen))  # Prime the generator
    print("Yielded:", gen.send("Hello from caller!"))
    
    print("\n--- Math Coroutine ---")
    m_gen = math_coroutine()
    next(m_gen) # Prime
    print(m_gen.send(2)) # 20
    print(m_gen.send(5)) # 70
    
    print("\n--- Running Average Coroutine ---")
    avg_gen = average_coroutine()
    next(avg_gen) # Prime
    print("Sent 10, Avg:", avg_gen.send(10))
    print("Sent 20, Avg:", avg_gen.send(20))
    print("Sent 30, Avg:", avg_gen.send(30))
    
    print("\n--- Mini Challenge (Bank Account) ---")
    account = bank_account(100)
    print("Initial Balance:", next(account)) # Prime
    print("Deposit 50. Balance:", account.send(50))
    print("Withdraw 20. Balance:", account.send(-20))
    account.close()
