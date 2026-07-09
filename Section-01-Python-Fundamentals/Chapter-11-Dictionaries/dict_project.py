"""
Topic: Dictionary Capstone Project
Chapter: 11
Level: Advanced

Description:
    This project combines everything learned about dictionaries: creation, methods, 
    nesting, comprehensions, and defensive programming. We will build a Contact 
    Management System (CRM).

Real-Life Analogy:
    Building a mini-application that mimics the backend of a phone book or CRM system.

Key Concepts:
    - CRUD operations (Create, Read, Update, Delete) using dictionaries
    - Data validation
    - Complex nested state management
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# We will use a nested dictionary as our "database".
# Keys will be unique IDs (e.g., email addresses).
# Values will be dictionaries containing user details.

# Example DB Structure:
# db = {
#     "alice@email.com": {"name": "Alice", "phone": "123", "tags": ["friend"]},
#     "bob@email.com": {"name": "Bob", "phone": "456", "tags": ["work"]}
# }

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES (PROJECT IMPLEMENTATION)
# ============================================================

class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, email, name, phone, tags=None):
        """Create operation"""
        if email in self.contacts:
            return False, "Contact already exists."
        
        self.contacts[email] = {
            "name": name,
            "phone": phone,
            "tags": tags or []
        }
        return True, "Contact added successfully."

    def get_contact(self, email):
        """Read operation"""
        # Defensive programming with .get()
        return self.contacts.get(email, "Contact not found.")

    def update_contact(self, email, **kwargs):
        """Update operation (Merging/Updating)"""
        if email not in self.contacts:
            return False, "Contact not found."
            
        # Update the specific contact dictionary
        self.contacts[email].update(kwargs)
        return True, "Contact updated."

    def delete_contact(self, email):
        """Delete operation"""
        if email in self.contacts:
            del self.contacts[email]
            return True, "Contact deleted."
        return False, "Contact not found."

# ============================================================
# SECTION 3: ADVANCED USAGE (QUERIES)
# ============================================================

    def search_by_tag(self, tag):
        """Find all contacts that have a specific tag using dictionary comprehension."""
        # Advanced: Dictionary comprehension filtering based on a list membership
        return {
            email: details for email, details in self.contacts.items() 
            if tag in details.get("tags", [])
        }

    def get_summary_stats(self):
        """Returns statistics about the contacts."""
        total = len(self.contacts)
        
        # Count frequency of all tags across all users
        tag_counts = {}
        for details in self.contacts.values():
            for tag in details.get("tags", []):
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
                
        return {
            "total_contacts": total,
            "tag_distribution": tag_counts
        }

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Best Practice: Encapsulating dictionary operations inside a Class (like we did here) 
# is much safer than passing a global dictionary around various functions.

# Best Practice: Use `kwargs` for updating dictionaries. It allows the user to pass 
# flexible arguments like `update_contact("alice@a.com", phone="999", city="NY")`.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: Why use a dictionary for the contact DB instead of a list of dictionaries?
A: Because looking up a user by email (ID) is O(1) in a dictionary. In a list, you would have to loop through every user (O(N) time) to find a specific email.

Q2: How does `self.contacts[email].update(kwargs)` work safely?
A: `kwargs` is caught as a dictionary. `.update()` merges it into the existing contact dictionary, overwriting existing keys and adding new ones, without destroying data that wasn't mentioned in kwargs.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise: Add a `search_by_name(name)` method to the ContactManager.
Hint: You'll need to iterate through `self.contacts.values()` and check if the name matches.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE / MAIN EXECUTION
# ============================================================

def run_project():
    print("--- Starting Contact Manager CRM ---\n")
    crm = ContactManager()
    
    # 1. Create
    crm.add_contact("john@doe.com", "John Doe", "555-0001", ["family", "vip"])
    crm.add_contact("jane@doe.com", "Jane Doe", "555-0002", ["work"])
    crm.add_contact("smith@co.com", "Agent Smith", "555-0099", ["work", "vip"])
    
    # 2. Read
    print("Fetch John:", crm.get_contact("john@doe.com"))
    
    # 3. Update
    print("\nUpdating Jane's phone...")
    crm.update_contact("jane@doe.com", phone="555-9999", title="Manager")
    print("Fetch Jane:", crm.get_contact("jane@doe.com"))
    
    # 4. Search by Tag (Comprehension in action)
    print("\nSearching VIPs:")
    vips = crm.search_by_tag("vip")
    for email, data in vips.items():
        print(f"  {data['name']} ({email})")
        
    # 5. Stats
    print("\nCRM Stats:")
    print(crm.get_summary_stats())

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Dictionaries are powerful enough to act as in-memory databases.
- Combining CRUD operations, `.get()`, `.update()`, and comprehensions allows for robust data management.
- Wrapping dictionary logic inside classes prevents unwanted side effects and builds cleaner APIs.
"""

if __name__ == "__main__":
    run_project()
