"""
Topic: OS Module File Handling
Chapter: 15
Level: Intermediate

Description:
    The `os` module provides a portable way of using operating system dependent functionality. While `pathlib` is preferred for modern path manipulation, `os` and `os.path` remain crucial for environment variables, executing shell commands, process management, and legacy codebases.

Real-Life Analogy:
    If `pathlib` is a modern GPS for navigating files, the `os` module is the steering wheel, pedals, and engine controls of your car. It interacts directly with the operating system environment to make things happen.

Key Concepts:
    - os.getcwd(), os.chdir()
    - os.listdir(), os.walk()
    - os.path.join(), os.path.exists()
    - os.environ
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================
import os

print("--- Section 1 ---")
# Get current working directory
current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")

# List files and directories in a path
contents = os.listdir(current_directory)
print(f"First 3 items in directory: {contents[:3]}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES (os.path)
# ============================================================

print("\n--- Section 2 ---")
# Using os.path (The older string-based way of path manipulation)

folder = "my_folder"
filename = "data.txt"

# Joining paths (handles slashes correctly based on OS)
full_path = os.path.join(current_directory, folder, filename)
print(f"Constructed path: {full_path}")

# Checking existence
print(f"Does the constructed path exist? {os.path.exists(full_path)}")

# Splitting paths
dir_name, file_name = os.path.split(full_path)
print(f"Directory: {dir_name}")
print(f"File Name: {file_name}")

# ============================================================
# SECTION 3: ADVANCED USAGE (os.walk)
# ============================================================

print("\n--- Section 3 ---")
# os.walk() generates the file names in a directory tree by walking the tree top-down.
# Let's create a tiny tree to walk
os.makedirs("test_walk/sub1", exist_ok=True)
os.makedirs("test_walk/sub2", exist_ok=True)
with open("test_walk/file_a.txt", "w") as f: f.write("a")
with open("test_walk/sub1/file_b.txt", "w") as f: f.write("b")

print("Walking 'test_walk' directory:")
for dirpath, dirnames, filenames in os.walk("test_walk"):
    print(f"Directory: {dirpath}")
    for name in filenames:
        print(f"  File: {name}")

# Cleanup
import shutil
shutil.rmtree("test_walk")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Hardcoding slashes in paths
# INCORRECT: path = "folder1/folder2/file.txt" (might break on Windows)
# CORRECT: path = os.path.join("folder1", "folder2", "file.txt")

# Mistake 2: Not handling errors when creating directories
# INCORRECT: os.mkdir("new_folder") # Fails if it already exists
# CORRECT: os.makedirs("new_folder", exist_ok=True)

# Best Practice: Use `pathlib` for new projects when dealing with paths.
# Keep `os` for environment variables (`os.environ`), system calls, and `os.walk`.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is the difference between `os.mkdir()` and `os.makedirs()`?
# A: `os.mkdir()` creates a single directory. If parent directories don't exist, it fails. `os.makedirs()` creates all necessary intermediate directories (like `mkdir -p` in bash).

# Q2: How does `os.walk()` work?
# A: It yields a 3-tuple `(dirpath, dirnames, filenames)` for each directory it visits, recursively traversing the directory tree.

# Q3: How do you access an environment variable in Python?
# A: Using `os.environ.get('VARIABLE_NAME')` or `os.getenv('VARIABLE_NAME')`.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

def list_txt_files(directory: str) -> list:
    """Returns a list of all .txt files in the given directory using os."""
    txt_files = []
    if os.path.exists(directory):
        for f in os.listdir(directory):
            if f.endswith(".txt") and os.path.isfile(os.path.join(directory, f)):
                txt_files.append(f)
    return txt_files

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge: Write a function `find_large_files(start_path, min_bytes)`
# that uses os.walk to find and return a list of all absolute file paths
# under `start_path` that are larger than `min_bytes`.

def find_large_files(start_path: str, min_bytes: int) -> list[str]:
    large_files = []
    for dirpath, _, filenames in os.walk(start_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                # Get file size in bytes
                size = os.path.getsize(file_path)
                if size > min_bytes:
                    large_files.append(os.path.abspath(file_path))
            except OSError:
                pass # Skip files we can't access
    return large_files

print("\n--- Mini Challenge ---")
# Find files larger than 1MB in the current directory (just a demo)
print(f"Found {len(find_large_files('.', 1_000_000))} large files.")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - `os` provides OS-dependent functionality (cwd, environment vars).
# - `os.path` handles string manipulation of paths (`join`, `split`, `exists`).
# - `os.walk` is powerful for recursively traversing directory trees.
# - Prefer `os.makedirs(path, exist_ok=True)` to avoid errors when creating folders.
# - For new code, `pathlib` is generally preferred over `os.path` for path operations.

if __name__ == "__main__":
    pass
