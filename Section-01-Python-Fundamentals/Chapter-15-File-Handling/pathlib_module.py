"""
Topic: Pathlib Module
Chapter: 15
Level: Beginner / Intermediate

Description:
    The `pathlib` module in Python provides an object-oriented approach to handling file system paths. Instead of manipulating strings like we do with `os.path`, `pathlib` provides Path objects that have intuitive methods for file and directory operations.

Real-Life Analogy:
    Instead of giving someone a piece of paper with an address written on it (string path), you give them a smart GPS device (Path object). The GPS knows how to navigate, check if the location exists, tell you what's nearby, and give you specific details about the destination.

Key Concepts:
    - Path object
    - Navigating paths (`/` operator)
    - File metadata (exists, is_file, is_dir)
    - Reading/Writing text via Path objects
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================
from pathlib import Path

# Create a Path object for the current directory
current_dir = Path(".")
print(f"Current directory path: {current_dir}")

# Create an absolute path
absolute_current = current_dir.resolve()
print(f"Absolute path: {absolute_current}")

# The magical `/` operator for joining paths!
# Instead of os.path.join(dir, subdir, file), you do this:
my_file_path = current_dir / "data" / "user_info.txt"
print(f"Constructed Path: {my_file_path}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Let's create a temporary directory and file to play with
test_dir = Path("pathlib_test_dir")
test_file = test_dir / "hello.txt"

# Create a directory (exist_ok=True prevents error if it already exists)
test_dir.mkdir(exist_ok=True)
print(f"\nCreated directory: {test_dir.exists()}")

# Writing text directly using pathlib
test_file.write_text("Hello World from pathlib!", encoding="utf-8")
print(f"Wrote to file: {test_file.exists()}")

# Reading text directly
content = test_file.read_text(encoding="utf-8")
print(f"Read from file: '{content}'")

# Examining Path properties
print(f"\nFile details for: {test_file.name}")
print(f"Parent directory: {test_file.parent}")
print(f"Stem (name without extension): {test_file.stem}")
print(f"Suffix (extension): {test_file.suffix}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

print("\n--- Section 3: Advanced ---")
# 1. Iterating through a directory (rglob for recursive)
# Let's create some dummy files to find
(test_dir / "file1.csv").touch()
(test_dir / "file2.csv").touch()
(test_dir / "script.py").touch()

print("Finding CSV files in the directory:")
for csv_file in test_dir.glob("*.csv"):
    print(f" - Found: {csv_file.name}")

# 2. Checking path types
print(f"\nIs {test_dir} a directory? {test_dir.is_dir()}")
print(f"Is {test_file} a file? {test_file.is_file()}")
print(f"Is {test_dir} a file? {test_dir.is_file()}")

# Cleanup: Deleting the files and directory we created
for f in test_dir.iterdir():
    f.unlink() # Deletes the file
test_dir.rmdir() # Deletes the empty directory
print("\nCleaned up test directory and files.")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Using string methods on Path objects
# p = Path("data.txt")
# p.replace(".txt", ".csv")  # This might replace text, but doesn't change the path suffix properly
# Best Practice: Use Path methods like with_suffix()
# new_p = p.with_suffix(".csv")

# Mistake 2: Sticking to os.path when pathlib is available
# Best Practice: Prefer pathlib over os.path for modern Python (3.4+). It is much more readable and robust.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is the main advantage of `pathlib` over `os.path`?
# A: `pathlib` treats paths as objects rather than strings, allowing for chainable, intuitive methods (like the `/` operator) and making the code more readable and robust across different operating systems.

# Q2: How do you join paths using pathlib?
# A: By using the forward slash `/` operator between Path objects or between a Path object and a string. (e.g., `Path("folder") / "subfolder" / "file.txt"`)

# Q3: How do you read the entire contents of a file as a string using a Path object?
# A: Use the `.read_text()` method on the Path object.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

def get_python_files(directory_path: str) -> list[str]:
    """
    Given a directory path string, use pathlib to return a list of 
    names of all .py files in that directory.
    """
    p = Path(directory_path)
    if not p.is_dir():
        return []
    return [file.name for file in p.glob("*.py")]

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge: Write a function that takes a directory path, and creates a backup
# directory next to it called "[dirname]_backup". It doesn't need to copy files,
# just create the new directory using pathlib.

def create_backup_dir(target_dir: str) -> Path:
    target = Path(target_dir)
    # Construct new path: parent_dir / "target_backup"
    backup_path = target.parent / f"{target.name}_backup"
    backup_path.mkdir(exist_ok=True)
    return backup_path

print("\n--- Mini Challenge ---")
backup = create_backup_dir("my_important_folder")
print(f"Created backup directory: {backup}")
backup.rmdir() # Cleanup

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - `pathlib.Path` represents a file system path as an object.
# - Use the `/` operator to easily join paths regardless of the OS.
# - Easily access parts of a path using `.name`, `.stem`, `.suffix`, `.parent`.
# - Check path existence and types with `.exists()`, `.is_file()`, `.is_dir()`.
# - Use `.read_text()` and `.write_text()` for quick file operations without `open()`.

if __name__ == "__main__":
    pass
