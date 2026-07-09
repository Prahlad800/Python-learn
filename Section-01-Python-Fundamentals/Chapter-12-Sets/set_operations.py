"""
Topic: Set Operations
Chapter: 12
Level: Intermediate

Description:
    Python sets support mathematical operations like union, intersection, difference, and symmetric difference. These operations can be performed using dedicated set methods or specialized operators.

Real-Life Analogy:
    Imagine two overlapping circles in a Venn diagram representing two groups of friends. Union is everyone in both groups, intersection is friends common to both groups, and difference is friends strictly in one group.

Key Concepts:
    - Union (|)
    - Intersection (&)
    - Difference (-)
    - Symmetric Difference (^)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_operations():
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}

    # Union: All unique elements from both sets
    print("Union (|):", set_a | set_b)
    print("Union method:", set_a.union(set_b))

    # Intersection: Elements common to both sets
    print("Intersection (&):", set_a & set_b)
    print("Intersection method:", set_a.intersection(set_b))

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    engineers = {"Alice", "Bob", "Charlie"}
    managers = {"Bob", "David", "Eve"}

    # Difference: Elements in engineers but NOT in managers
    print("Only engineers (-):", engineers - managers)
    print("Difference method:", engineers.difference(managers))

    # Symmetric Difference: Elements in either set, but not both
    print("Engineers or managers, but not both (^):", engineers ^ managers)
    print("Symmetric Diff method:", engineers.symmetric_difference(managers))

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    # You can perform operations on multiple sets at once
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    set3 = {5, 6, 7}
    
    # Chaining operators
    print("Union of 3 sets:", set1 | set2 | set3)
    print("Intersection of 3 sets:", set1 & set2 & set3)
    
    # Set operations with other iterables
    # Methods can take any iterable, operators require sets
    print("Union with list:", set1.union([8, 9]))
    try:
        print("Operator with list:", set1 | [8, 9])
    except TypeError as e:
        print("Operator requires set:", e)

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def mistakes_and_best_practices():
    # Mistake: Confusing difference order. set_a - set_b is NOT set_b - set_a
    set_a = {1, 2}
    set_b = {2, 3}
    print("a - b:", set_a - set_b)
    print("b - a:", set_b - set_a)
    
    # Best Practice: Use operators for readability when working with sets, 
    # but use methods when you need to perform operations with other iterables like lists.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is the difference between set.union() and the | operator?
# A: The method accepts any iterable, while the | operator strictly requires both operands to be sets.
#
# Q2: How do you find elements that are unique to each set?
# A: Using symmetric difference (^) or symmetric_difference().
#
# Q3: Does set intersection modify the original set?
# A: No, normal intersection returns a new set.
#
# Q4: Can you chain set operations?
# A: Yes, e.g., a | b | c.
#
# Q5: What is the time complexity of union?
# A: O(len(s1) + len(s2)).

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

def practice():
    # Find common elements in three sets
    s1 = {10, 20, 30, 40}
    s2 = {20, 30, 50}
    s3 = {30, 60}
    
    common = s1 & s2 & s3
    print("Common elements:", common)

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    # You have two lists of student IDs enrolled in Math and Science.
    # Find students enrolled in BOTH and students enrolled in ONLY ONE.
    math_ids = [101, 102, 103, 104, 105]
    science_ids = [103, 104, 105, 106, 107]
    
    math_set = set(math_ids)
    science_set = set(science_ids)
    
    both = math_set & science_set
    only_one = math_set ^ science_set
    
    return both, only_one

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
# - Union (|): combines elements.
# - Intersection (&): finds common elements.
# - Difference (-): finds elements in first but not second.
# - Symmetric Difference (^): finds elements not shared.

if __name__ == "__main__":
    print("--- Section 1 ---")
    basic_operations()
    print("\n--- Section 2 ---")
    practical_examples()
    print("\n--- Section 3 ---")
    advanced_usage()
    print("\n--- Section 4 ---")
    mistakes_and_best_practices()
    print("\n--- Section 6 ---")
    practice()
    print("\n--- Section 7 ---")
    both, only_one = mini_challenge()
    print(f"Students in both: {both}")
    print(f"Students in only one: {only_one}")
