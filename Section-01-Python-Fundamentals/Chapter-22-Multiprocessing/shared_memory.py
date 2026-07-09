"""
Topic: Shared Memory (Value and Array)
Chapter: 22
Level: Advanced

Description:
    While Queues and Pipes pass copies of data (messages) between processes, multiprocessing also allows actual shared memory for primitive data types. `Value` and `Array` allow processes to directly read and write to the same memory addresses.

Real-Life Analogy:
    Instead of sending letters (Pipes) to each other, you and your colleagues are looking at and editing the same whiteboard (Shared Memory). 

Key Concepts:
    - multiprocessing.Value
    - multiprocessing.Array
    - Data Types (ctypes)
    - Concurrency and Race Conditions
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

import multiprocessing
import time
import ctypes

def update_value(shared_val: multiprocessing.Value) -> None:
    """Updates a shared Value."""
    print(f"Child process read value: {shared_val.value}")
    shared_val.value = 3.14
    print(f"Child process updated value to: {shared_val.value}")

def basic_shared_value() -> None:
    """Demonstrates using multiprocessing.Value."""
    # 'd' stands for double precision float. Initialize with 0.0
    val = multiprocessing.Value('d', 0.0)
    
    p = multiprocessing.Process(target=update_value, args=(val,))
    p.start()
    p.join()
    
    # The parent process can see the update!
    print(f"Main process sees final value: {val.value}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def square_array(shared_arr: multiprocessing.Array) -> None:
    """Squares each element in a shared Array in-place."""
    for i in range(len(shared_arr)):
        shared_arr[i] = shared_arr[i] ** 2

def array_example() -> None:
    """Demonstrates using multiprocessing.Array."""
    # 'i' stands for integer. Initialize with a sequence.
    arr = multiprocessing.Array('i', [1, 2, 3, 4, 5])
    
    print(f"Array before: {list(arr)}")
    
    p = multiprocessing.Process(target=square_array, args=(arr,))
    p.start()
    p.join()
    
    print(f"Array after: {list(arr)}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def unsafe_increment(shared_val: multiprocessing.Value, iterations: int) -> None:
    """Increments a shared value WITHOUT synchronization. Will cause race conditions."""
    for _ in range(iterations):
        # This operation is NOT atomic!
        # It reads, adds, and writes. Another process might interrupt.
        shared_val.value += 1

def race_condition_demo() -> None:
    """Shows why shared memory is dangerous without locks."""
    val = multiprocessing.Value('i', 0)
    iterations = 10000
    
    p1 = multiprocessing.Process(target=unsafe_increment, args=(val, iterations))
    p2 = multiprocessing.Process(target=unsafe_increment, args=(val, iterations))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    # We expect 20000, but it will likely be less due to race conditions.
    print(f"Expected: {iterations * 2}")
    print(f"Actual Value: {val.value} (Notice it is less than expected!)")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Assuming `shared_val.value += 1` is atomic and safe across processes.
# Correction: It is not. You must use `multiprocessing.Lock()` to synchronize access to shared memory if multiple processes are writing to it.

# Mistake: Trying to store complex Python objects (like lists of dictionaries) in `Value` or `Array`.
# Correction: `Value` and `Array` only support C-type primitives (int, float, char). For complex objects, use a `multiprocessing.Manager`.

# Best Practice: Prefer Queues/Pipes over Shared Memory when possible. Message passing is generally safer and less prone to concurrency bugs than shared state.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: What are `multiprocessing.Value` and `Array`?
A: They are wrappers around ctypes objects allocated in shared memory, allowing distinct processes to read and write to the same exact memory locations.

Q2: What is the 'typecode' in `Value('i', 0)`?
A: The typecode is a character indicating the C-type of the data. 'i' is an integer, 'd' is a double float, 'c' is a character.

Q3: Why did the race condition demo result in a number less than expected?
A: Because two processes read the value simultaneously, both incremented it, and both wrote it back. One update overwrote the other, effectively losing an increment operation.

Q4: How do you fix a race condition in shared memory?
A: By using a synchronization primitive like `multiprocessing.Lock()` to ensure only one process accesses the shared variable at a time.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Create a shared `Value('d', 100.0)`. Create a process that subtracts 10 from it, and another process that divides it by 2. (Ignore race conditions for this exercise).
Exercise 2: Create a shared `Array('c', b"hello")`. Create a process that changes the first letter to "H".
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

"""
Challenge:
Use `multiprocessing.Manager().dict()` to create a shared dictionary (this is an alternative to Value/Array for complex objects).
Spawn 3 processes. Each process should add a key-value pair to the dictionary: the key being the process name, and the value being its PID.
Print the dictionary in the main process after all processes join.
"""

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Shared memory bypasses the need to serialize and copy data between processes.
- `Value` holds a single variable; `Array` holds a sequence.
- Both use C-type primitives.
- Extremely susceptible to Race Conditions when multiple processes write.
- Consider `multiprocessing.Manager` for sharing complex Python objects (lists, dicts).
"""

if __name__ == "__main__":
    print("--- Basic Shared Value ---")
    basic_shared_value()
    
    print("\n--- Shared Array ---")
    array_example()
    
    print("\n--- Race Condition Demo ---")
    race_condition_demo()
