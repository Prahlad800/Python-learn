"""
Topic: Set Algorithms
Chapter: 12
Level: Advanced

Description:
    Sets are a cornerstone in many efficient algorithms due to their O(1) average time complexity for lookups, insertions, and deletions. They are widely used in algorithm design for tracking seen elements and optimizing nested loops.

Real-Life Analogy:
    Think of a security guard keeping a mental note of every license plate that enters a parking lot. Instead of checking a long logbook every time a car arrives, they instantly recognize if they've seen a plate before.

Key Concepts:
    - Two Sum problem optimization
    - Finding duplicates
    - Graph traversal tracking (DFS/BFS)
    - Sliding window with unique elements
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def finding_duplicates(arr):
    # Using a set to find the first duplicate in an array
    # Time Complexity: O(N), Space Complexity: O(N)
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return None

def section_1_demo():
    nums = [1, 2, 3, 4, 3, 5]
    print(f"First duplicate in {nums}: {finding_duplicates(nums)}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def two_sum(arr, target):
    # Find two numbers that add up to target
    # Brute force is O(N^2), but sets reduce this to O(N)
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen.add(num)
    return None

def section_2_demo():
    nums = [10, 15, 3, 7]
    target = 17
    print(f"Two sum for target {target} in {nums}: {two_sum(nums, target)}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def longest_unique_substring(s):
    # Sliding window approach using a set to track characters
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
        
    return max_len

def section_3_demo():
    text = "abcabcbb"
    print(f"Longest unique substring length in '{text}': {longest_unique_substring(text)}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def mistakes_and_best_practices():
    # Mistake: Using a list instead of a set for tracking "visited" nodes 
    # in graph algorithms. Checking 'if node in list' is O(N), making the 
    # overall algorithm O(V*E) instead of O(V+E).
    
    # Best Practice: Always initialize `visited = set()` for DFS or BFS.
    visited = set()
    visited.add("Node_A")
    print("Graph tracking with set initialized.")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: How does a set improve the Two Sum algorithm?
# A: By allowing O(1) lookups for the complement of the current number.
#
# Q2: Can you use a set to find the intersection of two large arrays?
# A: Yes, convert one array to a set (O(N)), then iterate through the other checking membership (O(M)). Total time O(N+M).
#
# Q3: What is the worst-case time complexity of set insertion in Python?
# A: O(N) due to hash collisions requiring resizing, but this is extremely rare.
#
# Q4: How do you use a set in a sliding window problem?
# A: Maintain the set to represent elements in the current window. Add when expanding, remove when shrinking.
#
# Q5: Why is finding a duplicate in an array O(N) with a set?
# A: Because we iterate through the array once, and each insertion/lookup takes O(1) time.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

def practice():
    # Write a function that checks if an array contains any duplicates.
    # Return True if any value appears at least twice, else False.
    def contains_duplicate(nums):
        return len(nums) != len(set(nums))
        
    print("Contains duplicate [1,2,3,1]:", contains_duplicate([1,2,3,1]))
    print("Contains duplicate [1,2,3]:", contains_duplicate([1,2,3]))

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    # Find the missing number in an array containing n distinct numbers taken from 0, 1, 2, ..., n
    # (Do this using sets, though math/XOR is technically better space-wise)
    def find_missing(nums):
        n = len(nums)
        full_set = set(range(n + 1))
        nums_set = set(nums)
        return list(full_set - nums_set)[0]
        
    nums = [3, 0, 1]
    return find_missing(nums)

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
# - Sets drastically reduce time complexity from O(N^2) to O(N) for lookups.
# - Ideal for Two Sum, duplicate finding, and graph traversal.
# - Can be used dynamically in sliding window algorithms.

if __name__ == "__main__":
    print("--- Section 1 ---")
    section_1_demo()
    print("\n--- Section 2 ---")
    section_2_demo()
    print("\n--- Section 3 ---")
    section_3_demo()
    print("\n--- Section 4 ---")
    mistakes_and_best_practices()
    print("\n--- Section 6 ---")
    practice()
    print("\n--- Section 7 ---")
    print(f"Missing number: {mini_challenge()}")
