"""
Topic: Tempfile Module
Chapter: 15
Level: Intermediate

Description:
    The `tempfile` module is used to create temporary files and directories. These are useful when you need to store data temporarily during the execution of your program, and you want the OS to clean them up automatically when they are no longer needed.

Real-Life Analogy:
    Imagine a scratchpad or sticky note you use to jot down numbers while doing mental math. Once you get the final answer, you throw the sticky note away. Temporary files serve the exact same purpose for your programs.

Key Concepts:
    - TemporaryFile
    - NamedTemporaryFile
    - TemporaryDirectory
    - Automatic cleanup
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================
import tempfile
import os

print("--- Section 1 ---")

# TemporaryFile creates a file that has no visible name in the file system.
# It is destroyed as soon as it is closed.
with tempfile.TemporaryFile(mode='w+t') as temp_file:
    # Write to it
    temp_file.write("This data is temporary.\n")
    temp_file.write("It will vanish soon.")
    
    # Seek back to the beginning to read
    temp_file.seek(0)
    content = temp_file.read()
    print("Contents of TemporaryFile:")
    print(content)
    
# Once outside the 'with' block, the file is automatically deleted.

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

print("\n--- Section 2 ---")

# NamedTemporaryFile has a visible name in the file system, which is useful
# if you need to pass the file to another program or process.
with tempfile.NamedTemporaryFile(mode='w+t', delete=True) as named_temp:
    print(f"Created named temporary file at: {named_temp.name}")
    named_temp.write("Hello Named Temp File")
    
    # Prove it exists on the OS
    print(f"Does it exist? {os.path.exists(named_temp.name)}")

# Because delete=True (the default), it's gone now.
print(f"Does it exist after closing? {os.path.exists(named_temp.name)}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

print("\n--- Section 3 ---")

# TemporaryDirectory creates an entire folder that cleans itself up.
with tempfile.TemporaryDirectory() as temp_dir:
    print(f"Created temporary directory at: {temp_dir}")
    
    # You can put files inside it
    file_path = os.path.join(temp_dir, "test.txt")
    with open(file_path, "w") as f:
        f.write("Data inside a temp dir.")
        
    print(f"Files in temp dir: {os.listdir(temp_dir)}")

print(f"Does the dir exist after closing? {os.path.exists(temp_dir)}")

# Getting the system's default temp directory
sys_temp_dir = tempfile.gettempdir()
print(f"System default temp directory: {sys_temp_dir}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Opening NamedTemporaryFile twice on Windows
# On Windows, a NamedTemporaryFile created with delete=True cannot be opened
# again by another process (or sometimes the same process) while it is still open.
# Workaround: Set delete=False, close it, let the other process use it, then manually delete it.

# Mistake 2: Forgetting to seek(0)
# If you write to a temp file and immediately call read(), you'll get nothing
# because the file pointer is at the end of the file. Always `seek(0)` before reading.

# Best Practice: Always use the `with` statement (context managers) when working
# with temp files/dirs to ensure proper cleanup even if exceptions occur.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is the difference between TemporaryFile and NamedTemporaryFile?
# A: `TemporaryFile` has no visible name in the filesystem and is strictly for the current process. `NamedTemporaryFile` has a path on the OS and can be accessed by other programs while it exists.

# Q2: How do you ensure temporary files are cleaned up?
# A: By using them within a `with` block (context manager).

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise: Write a function that accepts a list of strings, writes them to a
# NamedTemporaryFile (one per line), and returns the path of that file. 
# Make sure it does NOT delete automatically (delete=False).

def write_to_temp(lines: list[str]) -> str:
    # Using delete=False so the file persists after the function returns
    temp = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix=".txt")
    for line in lines:
        temp.write(line + "\n")
    temp.close() # Close it so the data flushes to disk
    return temp.name

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge:
# 1. Create a TemporaryDirectory.
# 2. Inside it, create a file "secret.txt" containing "42".
# 3. Read the file back, assert the content is "42".
# 4. Let the context manager clean it up.

def secret_temp_test():
    with tempfile.TemporaryDirectory() as t_dir:
        file_path = os.path.join(t_dir, "secret.txt")
        
        # Write
        with open(file_path, "w") as f:
            f.write("42")
            
        # Read
        with open(file_path, "r") as f:
            data = f.read()
            
        print(f"Data read from temp file: {data}")
        assert data == "42"

print("\n--- Mini Challenge ---")
secret_temp_test()
print("Test completed successfully.")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - `tempfile` provides secure creation of temporary files and directories.
# - TemporaryFiles are great for intermediate data that doesn't need to be shared.
# - NamedTemporaryFiles have a path and can be passed to other tools.
# - TemporaryDirectories are useful for generating multiple related files safely.
# - Always use context managers (`with` blocks) to guarantee cleanup.

if __name__ == "__main__":
    pass
