"""
Topic: Set Methods
Chapter: 12
Level: Intermediate

Description:
    Sets in Python provide several built-in methods to modify sets in place or check relationships between sets. These methods alter the original set instead of creating a new one or return booleans regarding subset/superset relations.

Real-Life Analogy:
    Consider updating a club's guest list. Instead of printing a new list every time a new group arrives (which is like union returning a new set), you just append the new names to your existing clipboard (update methods).

Key Concepts:
    - In-place modifications (*_update methods)
    - Subsets and Supersets
    - Disjoint sets
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def relationship_methods():
    set_a = {1, 2, 3}
    set_b = {1, 2, 3, 4, 5}
    set_c = {6, 7, 8}

    # issubset: Checks if all elements of a are in b
    print(f"Is {set_a} a subset of {set_b}? {set_a.issubset(set_b)}")
    print(f"Subset using operator (<=): {set_a <= set_b}")

    # issuperset: Checks if b contains all elements of a
    print(f"Is {set_b} a superset of {set_a}? {set_b.issuperset(set_a)}")
    print(f"Superset using operator (>=): {set_b >= set_a}")

    # isdisjoint: Checks if sets have no elements in common
    print(f"Are {set_a} and {set_c} disjoint? {set_a.isdisjoint(set_c)}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def update_methods():
    base_set = {1, 2, 3}
    
    # update: In-place union
    base_set.update([3, 4, 5])
    print("After update:", base_set)
    
    # intersection_update: In-place intersection
    base_set.intersection_update({4, 5, 6})
    print("After intersection_update:", base_set)
    
    # difference_update: In-place difference
    base_set.difference_update({5})
    print("After difference_update:", base_set)
    
    # symmetric_difference_update: In-place symmetric diff
    base_set.symmetric_difference_update({4, 9, 10})
    print("After symmetric_difference_update:", base_set)

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    # Checking for proper subsets (<) and proper supersets (>)
    # A proper subset means all elements of A are in B, but A != B
    a = {1, 2}
    b = {1, 2}
    c = {1, 2, 3}
    
    print(f"Is {a} a proper subset of {b}? {a < b}")
    print(f"Is {a} a proper subset of {c}? {a < c}")
    
    # Multiple iterables in update
    s = set()
    s.update([1, 2], (3, 4), "56")
    print("Update with multiple iterables:", s)

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def mistakes_and_best_practices():
    # Mistake: Expecting update methods to return a new set.
    # Update methods return None and modify the set in-place.
    s = {1, 2}
    result = s.update({3})
    print("Result of s.update() is:", result) # None
    print("The set s is now:", s) # {1, 2, 3}
    
    # Best Practice: Use update methods when you want to avoid the memory 
    # overhead of creating new sets, especially with large datasets.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What does isdisjoint() do?
# A: Returns True if two sets have a null intersection (no common elements).
#
# Q2: Why use intersection_update instead of intersection?
# A: intersection_update modifies the set in-place, which saves memory.
#
# Q3: What does the <= operator do for sets?
# A: It checks if the left set is a subset of the right set.
#
# Q4: Can update() take a dictionary?
# A: Yes, it will add the dictionary's keys to the set.
#
# Q5: Does a set count as a subset of itself?
# A: Yes, A <= A is True. But it is not a proper subset (A < A is False).

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

def practice():
    # Verify if all elements of required_skills are present in candidate_skills
    required_skills = {"python", "sql"}
    candidate_skills = {"python", "django", "sql", "git"}
    
    is_match = required_skills.issubset(candidate_skills)
    print("Candidate matches requirements:", is_match)

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    # You manage a set of active users. Update the set with new logins, 
    # remove banned users in-place, and check if specific admins are online.
    active = {"user1", "user2"}
    new_logins = ["user3", "admin1"]
    banned = {"user2"}
    admins = {"admin1", "admin2"}
    
    active.update(new_logins)
    active.difference_update(banned)
    
    admins_online = not active.isdisjoint(admins)
    
    return active, admins_online

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
# - Relationship methods: issubset, issuperset, isdisjoint.
# - In-place methods: update, intersection_update, difference_update, symmetric_difference_update.
# - These methods optimize memory by not creating new set objects.

if __name__ == "__main__":
    print("--- Section 1 ---")
    relationship_methods()
    print("\n--- Section 2 ---")
    update_methods()
    print("\n--- Section 3 ---")
    advanced_usage()
    print("\n--- Section 4 ---")
    mistakes_and_best_practices()
    print("\n--- Section 6 ---")
    practice()
    print("\n--- Section 7 ---")
    active, has_admins = mini_challenge()
    print(f"Active users: {active}, Admins online: {has_admins}")
