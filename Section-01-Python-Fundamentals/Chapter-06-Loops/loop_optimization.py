"""
Topic: Loop Optimization and Performance
Chapter: 06
Level: Advanced

Description:
    Optimizing loops means reducing the execution time and memory footprint of iterations. 
    Since code inside a loop runs repeatedly, small inefficiencies inside the loop multiply rapidly, becoming massive bottlenecks.

Real-Life Analogy:
    If a factory worker takes 1 extra second to assemble a part, it doesn't matter for 10 parts. 
    But for 1,000,000 parts, that's an extra 11.5 days of work. Loop optimization is about trimming that 1 extra second.

Key Concepts:
    - Moving computations outside the loop (Hoisting)
    - Avoiding expensive function calls (like dot lookups) inside loops
    - Using built-in functions (C implementations)
    - Leveraging comprehensions and generators
"""

import time
import math

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def loop_hoisting():
    print("--- Loop Invariant Code Motion (Hoisting) ---")
    # Bad: Calculating the length of 'data' on every iteration implicitly or doing redundant math
    data = list(range(1000))
    multiplier = 5.5
    offset = 2.1
    
    start_time = time.time()
    result1 = []
    for num in data:
        # multiplier * offset is calculated 1000 times!
        result1.append(num * (multiplier * offset))
    print(f"Unoptimized time: {time.time() - start_time:.6f}s")
    
    start_time = time.time()
    result2 = []
    # Good: Calculate once outside the loop
    constant_factor = multiplier * offset
    for num in data:
        result2.append(num * constant_factor)
    print(f"Optimized time:   {time.time() - start_time:.6f}s")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def dot_lookup_optimization():
    print("\n--- Dot Lookup Optimization ---")
    data = list(range(50000))
    
    start_time = time.time()
    result1 = []
    for x in data:
        # Python has to look up the .append attribute of result1 50,000 times!
        result1.append(math.sqrt(x))
    print(f"With dot lookup:    {time.time() - start_time:.6f}s")

    start_time = time.time()
    result2 = []
    # Assigning the method to a local variable avoids the lookup
    append_method = result2.append
    sqrt_method = math.sqrt
    for x in data:
        append_method(sqrt_method(x))
    print(f"Without dot lookup: {time.time() - start_time:.6f}s")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def builtins_vs_loops():
    print("\n--- Built-ins vs Manual Loops ---")
    data = list(range(100000))
    
    # Manual loop
    start_time = time.time()
    total = 0
    for num in data:
        total += num
    print(f"Manual sum loop time: {time.time() - start_time:.6f}s")
    
    # Built-in sum (implemented in C)
    start_time = time.time()
    total = sum(data)
    print(f"Built-in sum() time:  {time.time() - start_time:.6f}s")

def map_and_comprehension():
    print("\n--- Comprehensions and Map ---")
    data = list(range(50000))
    
    # Standard loop
    start_time = time.time()
    res1 = []
    for x in data:
        res1.append(x * 2)
    loop_time = time.time() - start_time
    
    # List comprehension
    start_time = time.time()
    res2 = [x * 2 for x in data]
    comp_time = time.time() - start_time
    
    # Map function
    start_time = time.time()
    res3 = list(map(lambda x: x * 2, data))
    map_time = time.time() - start_time
    
    print(f"Standard Loop: {loop_time:.6f}s")
    print(f"Comprehension: {comp_time:.6f}s")
    print(f"Map function:  {map_time:.6f}s")
    # Note: For simple operations, comprehension is usually faster than map+lambda.

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Common Mistakes:
# 1. Opening/Closing files or establishing database connections INSIDE a loop.
# 2. Doing string concatenation `string += new_string` inside a loop (creates new string object each time). Use `''.join(list_of_strings)`.
# 3. Premature optimization: making code unreadable to save 1 millisecond on a loop that runs 10 times.

# Best Practices:
# 1. Lift redundant calculations outside the loop (Loop Hoisting).
# 2. Use local variables for function/method references if called thousands of times inside the loop.
# 3. Rely on built-in functions (`sum`, `max`, `min`) and libraries like NumPy for heavy numerical looping.
# 4. Use list comprehensions or generators instead of `.append()` in a for-loop.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: Why is string concatenation inside a loop inefficient in Python?
A: Strings are immutable in Python. `s += "a"` creates an entirely new string object in memory and copies the old contents, resulting in O(N^2) complexity.

Q2: What is Loop Invariant Code Motion?
A: It is moving calculations that yield the same result on every iteration to the outside of the loop.

Q3: Why is resolving a dot notation (like `list.append`) inside a loop slow?
A: The interpreter must perform a dictionary lookup to find the method on the object's class on every iteration.

Q4: Are list comprehensions always faster than for loops?
A: Usually yes, because the loop is executed in C, but if the comprehension logic is complex, it might consume more memory or read worse.

Q5: When should you NOT optimize a loop?
A: When the data size is trivially small or the optimization makes the code severely unreadable. Profile the code first.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

def practice_exercises():
    # Exercise 1: Identify the inefficiency in this loop and optimize it.
    # length = 0
    # for word in word_list:
    #     length += len(word_list)
    pass

    # Exercise 2: Refactor a manual search loop into one using the `in` operator.
    pass

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: 
    You are given a list of strings representing numbers.
    Write the most optimized way to parse them to integers, square them, 
    and return the sum of all squares. Compare your optimized way with a naive loop.
    """
    str_nums = [str(i) for i in range(10000)]
    
    print("\n--- Optimization Challenge ---")
    
    # Naive Way
    start = time.time()
    total = 0
    for s in str_nums:
        val = int(s)
        total += val * val
    naive_time = time.time() - start
    
    # Optimized Way (Generator expression inside sum)
    start = time.time()
    # sum() consumes the generator directly without building a list
    total_opt = sum(int(s)**2 for s in str_nums)
    opt_time = time.time() - start
    
    print(f"Naive Time:     {naive_time:.6f}s")
    print(f"Optimized Time: {opt_time:.6f}s")
    print(f"Results match: {total == total_opt}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Loop optimization trims micro-inefficiencies that scale exponentially.
- Lift invariants, cache methods, and use built-ins.
- Prefer list comprehensions and generators over `append()`.
- Use the `time` module to profile code before and after optimizing.
"""

if __name__ == "__main__":
    loop_hoisting()
    dot_lookup_optimization()
    builtins_vs_loops()
    map_and_comprehension()
    mini_challenge()
