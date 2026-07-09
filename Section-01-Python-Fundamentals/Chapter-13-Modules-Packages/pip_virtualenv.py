"""
Topic: pip and Virtual Environments
Chapter: 13
Level: Intermediate

Description:
    `pip` is the package installer for Python, used to download and install packages from PyPI.
    A Virtual Environment (`venv`) is an isolated Python environment that allows you to install 
    packages for one specific project without affecting the global Python installation or other projects.

Real-Life Analogy:
    A virtual environment is like having a separate workshop for every project you build. 
    If you need metric tools for one project and imperial tools for another, you keep them in separate 
    workshops so they don't get mixed up. `pip` is the delivery service that brings the tools to your workshop.

Key Concepts:
    - python -m venv
    - Activating/Deactivating environments
    - pip install, uninstall, freeze
    - requirements.txt
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# NOTE: These are terminal commands, not Python code. We present them as strings to illustrate.

terminal_commands = {
    "create_venv": "python -m venv myenv",
    "activate_windows": r"myenv\\Scripts\\activate",
    "activate_mac_linux": "source myenv/bin/activate",
    "deactivate": "deactivate",
    "install_package": "pip install requests",
    "freeze_deps": "pip freeze > requirements.txt",
    "install_from_reqs": "pip install -r requirements.txt"
}

def print_commands():
    print("Essential Virtual Environment Commands:")
    for action, cmd in terminal_commands.items():
        print(f"{action.ljust(22)}: {cmd}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Simulating how requirements might be checked in a Python script
import sys

def in_virtual_environment() -> bool:
    """Checks if the script is running inside a virtual environment."""
    # sys.prefix points to the environment where Python is running.
    # sys.base_prefix points to the global Python installation.
    # If they are different, we are in a virtual environment.
    return hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)

print(f"Is running in a virtual environment? {in_virtual_environment()}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Checking pip version programmatically (for advanced scripting)
import subprocess

def get_pip_version():
    """Runs a subprocess to check the installed pip version."""
    try:
        result = subprocess.run([sys.executable, "-m", "pip", "--version"], 
                                capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return "Pip is not installed or accessible."

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Forgetting to activate the virtual environment before installing packages.
# Result: Packages get installed globally, leading to version conflicts.

# Mistake 2: Committing the `venv` directory to Git.
# Result: Bloated repository with system-dependent binaries.
# Best Practice: Always add your virtual environment folder (e.g., `venv/`, `env/`) to your `.gitignore`.

# Best Practice: Create a new virtual environment for EVERY new Python project.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: Why do we need virtual environments in Python?
# A: To avoid dependency conflicts between projects. It ensures that upgrading a package in Project A 
#    doesn't break Project B.

# Q2: How do you create and activate a virtual environment?
# A: `python -m venv env_name`. Activate via `env_name/Scripts/activate` (Windows) or `source env_name/bin/activate` (Mac/Linux).

# Q3: What is the purpose of `requirements.txt`?
# A: It lists all the third-party dependencies (and their versions) required to run a project, allowing others 
#    to easily recreate the environment using `pip install -r requirements.txt`.

# Q4: How does a virtual environment actually work under the hood?
# A: It creates a folder containing a copy/symlink of the Python executable and modifies environment variables (like PATH) 
#    so that running `python` or `pip` uses the local environment instead of the global one.

# Q5: What is the difference between `pip` and `conda`?
# A: `pip` is a package manager for Python packages. `conda` is a cross-platform, language-agnostic package manager 
#    and environment manager that can install Python, C libraries, and more.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise: Write a script that checks if `requests` is installed, and prints advice based on the result.

def check_dependencies():
    try:
        import requests
        print("Dependency 'requests' is installed.")
    except ImportError:
        print("Dependency 'requests' is missing!")
        print("Run: pip install requests")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Write a utility function that formats a string to be written to a .gitignore file, 
# ensuring common virtual environment names are ignored.

def generate_gitignore_content() -> str:
    common_venvs = ["venv/", "env/", ".venv/", ".env/"]
    content = "# Virtual Environments\n"
    for v in common_venvs:
        content += f"{v}\n"
    content += "\n# Python Cache\n__pycache__/\n*.pyc\n"
    return content

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - `pip` installs packages. `venv` isolates them.
# - Always activate your environment before working on a project.
# - Use `pip freeze > requirements.txt` to save your state.
# - Never commit your virtual environment folder to version control.

if __name__ == "__main__":
    print_commands()
    print(f"Pip info: {get_pip_version()}")
    check_dependencies()
    print("\nGenerated .gitignore content:")
    print(generate_gitignore_content())
