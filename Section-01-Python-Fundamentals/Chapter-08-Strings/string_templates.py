"""
Topic: String Templates (string.Template)
Chapter: 8
Level: Intermediate

Description:
    The `string` module provides a `Template` class for simpler, safer string substitutions.
    It is especially useful for user-provided formats where `.format()` or f-strings could expose security risks (like code injection).

Real-Life Analogy:
    A form letter with variables like $name and $date. It only replaces exactly what it recognizes, ignoring other complex logic.

Key Concepts:
    - string.Template class
    - substitute() method
    - safe_substitute() method
    - Variable placeholders using $
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

from string import Template

def basic_templates():
    """Using string.Template for basic substitution."""
    t = Template('Hello, $name! Welcome to $place.')
    
    # Substitute using keyword arguments
    result = t.substitute(name='Alice', place='Wonderland')
    print("Result:", result)
    
    # Substitute using a dictionary
    data = {'name': 'Bob', 'place': 'the Builder'}
    print("Result from dict:", t.substitute(data))

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def template_safety():
    """Demonstrating safe_substitute."""
    t = Template('Item: $item, Price: $$ $price, Tax: $tax')
    
    # Using $$ escapes the dollar sign to a literal $
    
    # If a value is missing, substitute() raises KeyError
    try:
        t.substitute(item='Book', price='10')
    except KeyError as e:
        print("Missing key in substitute:", e)
        
    # safe_substitute() leaves the placeholder intact if data is missing
    safe_res = t.safe_substitute(item='Book', price='10')
    print("Safe substitute result:", safe_res)

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_templates():
    """Customizing the delimiter."""
    # We can subclass Template to change the delimiter
    class CustomTemplate(Template):
        delimiter = '%' # Using % instead of $
        
    t = CustomTemplate('User: %user | Role: %role')
    print("Custom template:", t.substitute(user='admin', role='superuser'))

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Confusing `Template` with `.format()`. Template uses `$` while format uses `{}`.
# Mistake: Forgetting that a literal `$` must be written as `$$` in the template string.

# Best Practice: Use `Template` when formatting strings provided by users to avoid security vulnerabilities inherent in `eval()` or complex `.format()` attacks.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q: Why use `string.Template` when f-strings exist?
A: f-strings require variables to be in scope at runtime and evaluate expressions. `string.Template` is safer for user-supplied templates (like config files) because it prevents arbitrary code execution and attribute access.

Q: How do you write a literal dollar sign in a `string.Template`?
A: By using two dollar signs: `$$`.

Q: What is the difference between `substitute()` and `safe_substitute()`?
A: `substitute()` raises a KeyError if a placeholder's value is missing. `safe_substitute()` leaves the placeholder unchanged in the string without raising an error.

Q: How do you disambiguate a variable name from adjacent text?
A: Enclose the variable name in braces: `${name}s` to ensure 's' isn't considered part of the variable name.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# 1. Create a template for an email body: "Dear $customer, your order #$order_id is shipped."
# 2. Populate the email template using a dictionary.
# 3. Try to populate the template with a missing 'order_id' using `safe_substitute()`.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """Create an HTML templating engine clone using string.Template."""
    html_template = Template("""
    <html>
        <head><title>$title</title></head>
        <body>
            <h1>Hello, $username</h1>
            <p>${message}</p>
        </body>
    </html>
    """)
    
    user_data = {
        'title': 'User Dashboard',
        'username': 'john_doe',
        'message': 'You have 5 new notifications.'
    }
    
    print(html_template.substitute(user_data))

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- `string.Template` is a simpler, safer alternative for string formatting.
- It uses `$` for placeholders (e.g., `$var` or `${var}`).
- Use `$$` for a literal dollar sign.
- `substitute()` requires all variables; `safe_substitute()` handles missing variables gracefully.
- Excellent for handling user-defined formats securely.
"""

if __name__ == "__main__":
    basic_templates()
    template_safety()
    advanced_templates()
    mini_challenge()
