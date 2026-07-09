"""
Topic: Dictionary Access Patterns & Defensive Programming
Chapter: 11
Level: Intermediate

Description:
    When working with dictionaries, especially data from external sources (APIs, JSON files),
    we often encounter missing keys or unpredictable structures. This file explores patterns 
    to safely access data without crashing the program with KeyErrors.

Real-Life Analogy:
    Imagine an online form where only "Email" is required, but "Phone Number" and "Address" are optional.
    When reading the submitted form, you can't assume "Phone Number" exists. You must check first or 
    have a safe fallback, otherwise the process crashes.

Key Concepts:
    - EAFP (Easier to Ask for Forgiveness than Permission) vs LBYL (Look Before You Leap)
    - Safe nested dictionary access
    - Default values
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

api_response = {
    "status": "success",
    "data": {
        "user": {
            "id": 42,
            "username": "admin"
            # Note: 'profile' key is missing
        }
    }
}

# The dangerous way (causes KeyError)
# print(api_response["data"]["user"]["profile"]["bio"])

# LBYL (Look Before You Leap) - Checking explicitly
if "data" in api_response and "user" in api_response["data"]:
    user_data = api_response["data"]["user"]
    if "profile" in user_data and "bio" in user_data["profile"]:
        print(user_data["profile"]["bio"])
    else:
        print("Bio not found (LBYL)")

# EAFP (Easier to Ask for Forgiveness than Permission) - Try/Except
try:
    print(api_response["data"]["user"]["profile"]["bio"])
except KeyError:
    print("Bio not found (EAFP)")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Example 1: Chaining .get() for safe nested access
# This is a very common and pythonic pattern.
# We supply an empty dictionary {} as the default fallback for intermediate steps.

bio = api_response.get("data", {}).get("user", {}).get("profile", {}).get("bio", "No Bio")
print(f"\nSafe access using .get(): {bio}")

# Example 2: Parsing varying schemas
users = [
    {"name": "Alice", "email": "alice@email.com"},
    {"name": "Bob", "phone": "555-1234"},
    {"name": "Charlie"}
]

print("\nContact Info:")
for u in users:
    # Coalescing: Check email, if not check phone, else Unknown
    contact = u.get("email") or u.get("phone") or "Unknown"
    print(f"{u['name']}: {contact}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Advanced Example: A utility function for deep nested fetching
def deep_get(dictionary, keys, default=None):
    """
    Fetches a value from a nested dictionary using a list of keys.
    Returns default if any key in the path is missing.
    """
    for key in keys:
        if isinstance(dictionary, dict):
            dictionary = dictionary.get(key, default)
        else:
            return default
    return dictionary

keys_to_bio = ["data", "user", "profile", "bio"]
keys_to_name = ["data", "user", "username"]

print(f"\nDeep get bio: {deep_get(api_response, keys_to_bio, 'N/A')}")
print(f"Deep get name: {deep_get(api_response, keys_to_name, 'N/A')}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Using .get() but forgetting the fallback for nested dictionaries
# BAD: my_dict.get("level1").get("level2") 
# If "level1" is missing, .get() returns None. Then it tries None.get("level2"), which raises AttributeError!
# CORRECTION: my_dict.get("level1", {}).get("level2")

# Best Practice: In Python, the EAFP (try/except) approach is generally preferred over 
# complex LBYL (if-statements) for dictionary access, as it is often faster and more readable.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: Explain EAFP vs LBYL in the context of dictionaries.
A: EAFP means trying to access the key directly (dict[key]) and catching the KeyError if it fails. LBYL means checking if the key exists first (if key in dict:). Python culture generally favors EAFP.

Q2: How do you safely navigate a deeply nested dictionary where intermediate keys might be missing?
A: You can chain `.get(key, {})`, use a custom recursive/iterative fetch function, or wrap the direct access in a `try...except KeyError`.

Q3: What does `dict.get(key) or "default"` do if the key exists but its value is empty string `""`?
A: Because `""` is falsy, the `or` operator will evaluate to `"default"`. If you want to accept falsy values, you must use `dict.get(key, "default")`.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Write a try-except block to access dict['address']['zip']. Print 'Zip missing' if it fails.
Exercise 2: Rewrite the logic from Exercise 1 using chained `.get()` methods.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: Data normalizer
    Given a list of raw event payloads, extract the 'user_id' and 'event_type'.
    If 'user_id' is missing in 'payload', check 'metadata'. If still missing, skip.
    """
    events = [
        {"event": "click", "payload": {"user_id": 123}},
        {"event": "view", "payload": {}, "metadata": {"user_id": 456}},
        {"event": "scroll", "payload": {}} # Missing entirely
    ]
    
    processed = []
    for evt in events:
        event_type = evt.get("event")
        # Try payload first, then metadata
        u_id = evt.get("payload", {}).get("user_id")
        if u_id is None:
            u_id = evt.get("metadata", {}).get("user_id")
            
        if u_id is not None:
            processed.append({"user_id": u_id, "event": event_type})
            
    print("\nProcessed Events:")
    for p in processed:
        print(p)

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Avoid direct `dict[key]` access unless you are 100% certain the key exists.
- Use EAFP (try/except KeyError) for clean and pythonic error handling.
- Use chained `.get(key, {})` for safely navigating nested dictionaries.
- Be careful with `dict.get() or fallback` if valid values can be falsy (like `0`, `False`, `""`).
"""

if __name__ == "__main__":
    mini_challenge()
