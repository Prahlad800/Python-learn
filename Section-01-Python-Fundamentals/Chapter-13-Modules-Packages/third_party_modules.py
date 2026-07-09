"""
Topic: Third Party Modules
Chapter: 13
Level: Intermediate

Description:
    While the standard library is massive, it doesn't cover everything. Third-party modules are packages 
    created by the community to extend Python's functionality into areas like web development, data science, 
    and machine learning. These are typically installed via tools like `pip`.

Real-Life Analogy:
    Your smartphone comes with standard apps, but you go to the App Store (PyPI for Python) to download 
    games, specialized productivity tools, or social media apps created by other developers.

Key Concepts:
    - PyPI (Python Package Index)
    - pip (Package installer for Python)
    - Virtual Environments
    - Popular libraries (requests, pandas, numpy)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Note: The following imports will only work if the packages are installed in your environment.
# Normally you'd run: `pip install requests` in your terminal.

# Try importing a third party module safely.
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False
    print("The 'requests' module is not installed.")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def fetch_joke():
    """Fetches a random joke using the requests library, if available."""
    if not HAS_REQUESTS:
        return "Could not fetch joke. 'requests' is not installed."
    
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return f"{data['setup']} - {data['punchline']}"
        return "Failed to get a good response."
    except Exception as e:
        return f"An error occurred: {e}"

print(fetch_joke())

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Dependency management and versioning
# When installing packages, it is crucial to manage versions to ensure reproducibility.
# A `requirements.txt` file is commonly used.
# Format:
# requests==2.31.0
# pandas>=1.5.0
# numpy<2.0.0

def mock_parse_requirements(req_string: str):
    """Mocks parsing a requirements.txt file."""
    requirements = []
    for line in req_string.strip().split('\n'):
        if line and not line.startswith('#'):
            requirements.append(line.strip())
    return requirements

sample_reqs = """
requests==2.31.0
numpy>=1.20.0
# pandas==2.0.0
"""
print(f"Parsed Requirements: {mock_parse_requirements(sample_reqs)}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Installing third-party packages globally.
# This can cause version conflicts between different projects.
# Best Practice: Always use Virtual Environments (venv, conda) for projects.

# Mistake 2: Not pinning dependency versions in requirements.txt.
# If you just write `requests`, pip installs the latest version, which might introduce breaking changes later.

# Best Practice: Use `pip freeze > requirements.txt` to capture exact versions.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is PyPI?
# A: The Python Package Index, a repository of software for the Python programming language.

# Q2: What is `pip`?
# A: The standard package installer for Python, used to install and manage packages not part of the standard library.

# Q3: Why is a virtual environment important when using third-party modules?
# A: It isolates project dependencies, preventing conflicts where Project A needs version 1.0 of a library 
#    and Project B needs version 2.0.

# Q4: How do you list all installed packages in your environment?
# A: By running `pip list` or `pip freeze` in the terminal.

# Q5: If a third-party package has a vulnerability, how do you fix it?
# A: Update the package to a patched version using `pip install --upgrade package_name`.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise: Write a pseudo-function to simulate checking if a specific version of a package is installed.

def is_compatible_version(installed_version: str, required_major: int) -> bool:
    """Checks if the installed major version matches the required one."""
    try:
        major = int(installed_version.split(".")[0])
        return major == required_major
    except ValueError:
        return False

print(f"Is 2.31.0 compatible with major 2? {is_compatible_version('2.31.0', 2)}")
print(f"Is 1.5.0 compatible with major 2? {is_compatible_version('1.5.0', 2)}")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Create a function that attempts to use an external library (like pandas).
# If the library is not installed, gracefully catch the ImportError and return a fallback message.

def try_import_data_tool():
    try:
        import pandas as pd
        df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
        return f"Pandas is installed! DataFrame shape: {df.shape}"
    except ImportError:
        return "Pandas is not installed. Please install it using 'pip install pandas' to unlock data tools."

print(try_import_data_tool())

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Third-party modules immensely expand Python's capabilities.
# - Use `pip` to install packages from PyPI.
# - Always use virtual environments to isolate project dependencies.
# - Keep a `requirements.txt` to track what your project needs.

if __name__ == "__main__":
    pass
