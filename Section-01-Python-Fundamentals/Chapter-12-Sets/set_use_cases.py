"""
Topic: Set Use Cases
Chapter: 12
Level: Intermediate

Description:
    Sets are incredibly versatile for data processing tasks. Their unique properties make them the ideal choice for deduplication, fast membership testing, and analyzing relationships between datasets.

Real-Life Analogy:
    A set is like a highly efficient filing system. If you want to know if a document exists, or if you need to merge two filing cabinets while keeping only one copy of each file, the set does this instantly.

Key Concepts:
    - Data deduplication
    - Membership testing
    - Finding overlaps and differences
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_deduplication():
    # The most common use case: deduplicating a list
    raw_data = ["apple", "banana", "apple", "cherry", "banana"]
    clean_data = list(set(raw_data))
    
    print("Original:", raw_data)
    print("Deduplicated:", clean_data) # Note: Order is lost

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def membership_testing():
    # Scenario: Checking if an IP is blocklisted
    blocklist_list = ["192.168.1.1", "10.0.0.5", "172.16.0.2"]
    blocklist_set = set(blocklist_list)
    
    incoming_ip = "10.0.0.5"
    
    # O(N) time complexity
    is_blocked_list = incoming_ip in blocklist_list
    
    # O(1) time complexity - Much better for large datasets!
    is_blocked_set = incoming_ip in blocklist_set
    
    print(f"IP {incoming_ip} blocked? {is_blocked_set}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def analytical_use_cases():
    # Comparing configurations or permissions
    default_permissions = {"read", "write"}
    user_permissions = {"read", "write", "execute", "delete"}
    
    # What extra permissions does the user have?
    extra = user_permissions - default_permissions
    print("Extra permissions:", extra)
    
    # Are the user's permissions valid based on a master list?
    master_list = {"read", "write", "execute", "delete", "admin"}
    print("Permissions valid?", user_permissions <= master_list)

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def mistakes_and_best_practices():
    # Mistake: Using list(set(data)) when order matters
    data = [1, 5, 2, 5, 1, 9]
    print("Loss of order:", list(set(data)))
    
    # Correction: If order matters, use dict.fromkeys() instead
    print("Preserved order:", list(dict.fromkeys(data)))

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: Why use a set over a list for checking if an item exists?
# A: Checking membership in a list takes O(N) time because it requires scanning. In a set, it takes O(1) average time due to hashing.
#
# Q2: How can you find duplicate elements in a list using sets?
# A: Compare the length of the list to the length of the list converted to a set.
#
# Q3: Can sets be used for sorting data?
# A: No, sets are inherently unordered.
#
# Q4: How do sets handle boolean values?
# A: True is treated as 1, False as 0. So {1, True} evaluates to {1}.
#
# Q5: What is the most efficient way to find common items in multiple lists?
# A: Convert the first list to a set, then use intersection with the other lists.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

def practice():
    # Check if two lists have any items in common
    list_a = [1, 2, 3, 4]
    list_b = [4, 5, 6, 7]
    
    has_common = not set(list_a).isdisjoint(list_b)
    print("Lists have common items:", has_common)

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    # You are building a tagging system for a blog.
    # Write code to:
    # 1. Deduplicate the submitted tags.
    # 2. Find tags that are not in the 'approved_tags' list.
    
    submitted_tags = ["python", "coding", "Python", "dev", "coding"]
    approved_tags = {"python", "dev", "tutorial"}
    
    # Standardize casing and deduplicate
    clean_tags = {tag.lower() for tag in submitted_tags}
    
    unapproved = clean_tags - approved_tags
    return clean_tags, unapproved

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
# - Sets are the go-to structure for deduplication.
# - Use sets for O(1) membership testing (the `in` operator).
# - Mathematical operations make sets ideal for comparing datasets.

if __name__ == "__main__":
    print("--- Section 1 ---")
    basic_deduplication()
    print("\n--- Section 2 ---")
    membership_testing()
    print("\n--- Section 3 ---")
    analytical_use_cases()
    print("\n--- Section 4 ---")
    mistakes_and_best_practices()
    print("\n--- Section 6 ---")
    practice()
    print("\n--- Section 7 ---")
    clean, unapp = mini_challenge()
    print(f"Clean tags: {clean}, Unapproved: {unapp}")
