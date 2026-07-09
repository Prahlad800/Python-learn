"""
Topic: Binary Files
Chapter: 15
Level: Advanced

Description:
    Binary files contain data that is not formatted as human-readable text. This includes images, compiled programs, audio files, and serialized Python objects (like pickles). Reading and writing binary files requires using the 'b' flag in the file mode.

Real-Life Analogy:
    A text file is like a handwritten letter; you can read it directly. A binary file is like a vinyl record; you need a specific machine (program) to decode and understand the grooves (bytes).

Key Concepts:
    - 'rb', 'wb', 'ab' modes
    - Bytes and Bytearrays
    - Reading and writing images/data chunks
    - The `pickle` module for object serialization
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Writing bytes to a binary file
# Note the 'wb' mode and the 'b' prefix on the string
with open("data.bin", "wb") as f:
    f.write(b"Hello, Binary World!")
    f.write(bytes([120, 121, 122])) # Writes 'xyz'

# Reading bytes from a binary file
print("Reading Binary Data:")
with open("data.bin", "rb") as f:
    content = f.read()
    print("Raw Bytes:", content)
    print("Decoded to string:", content.decode('utf-8'))

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Example 1: Copying an image (or any binary file)
# We read chunks of bytes to avoid memory overload for large files.

def copy_binary_file(source, destination):
    try:
        # Create a dummy "image" for this example
        with open(source, "wb") as dummy:
            import os
            dummy.write(os.urandom(1024)) # 1KB of random bytes

        with open(source, "rb") as src, open(destination, "wb") as dest:
            chunk_size = 256
            while True:
                chunk = src.read(chunk_size)
                if not chunk:
                    break
                dest.write(chunk)
        print(f"\nSuccessfully copied {source} to {destination}")
    except FileNotFoundError:
        print("Source file not found.")

copy_binary_file("source_image.bin", "copy_image.bin")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Example 2: Serializing Python objects with Pickle
# Pickle converts Python objects into a byte stream
import pickle

data_structure = {"username": "admin", "id": 101, "roles": ["super", "user"]}

# Saving object to a binary file
with open("user_profile.pkl", "wb") as f:
    pickle.dump(data_structure, f)

# Loading object from a binary file
print("\nUnpickling data:")
with open("user_profile.pkl", "rb") as f:
    loaded_data = pickle.load(f)
    print("Loaded Data Type:", type(loaded_data))
    print("Loaded Content:", loaded_data)

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Trying to write a standard string to a binary file.
# Correction: You must encode strings into bytes (e.g., `text.encode('utf-8')`) or use the `b'...'` prefix.

# Mistake 2: Unpickling data from untrusted sources.
# Correction: NEVER unpickle data from a source you don't trust. The pickle module can execute arbitrary code during deserialization!

# Best Practice: Process large binary files in chunks (e.g., 4096 bytes at a time) to prevent excessive memory consumption.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What does the 'b' stand for in 'wb' or 'rb'?
# A: Binary mode.

# Q2: How do you convert a string to bytes in Python?
# A: By calling `.encode('utf-8')` on the string, or prefixing it with `b`.

# Q3: What is the `pickle` module used for?
# A: Serializing and deserializing Python objects to and from byte streams.

# Q4: Why is it dangerous to unpickle data from an unknown source?
# A: Because the unpickling process can construct malicious objects that execute harmful code on your machine.

# Q5: What happens if you try to open a binary file in 'r' (text) mode?
# A: You will likely get a UnicodeDecodeError, as Python tries to interpret raw bytes as text characters.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a script that writes the byte values 0 to 255 to a binary file.

# Exercise 2: Read the binary file from Exercise 1 and print the first 10 bytes.

# Exercise 3: Create a complex Python dictionary, pickle it to a file, unpickle it, and assert it equals the original.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def file_encryptor(filename, key):
    """
    Mini Challenge: Write a basic XOR encryptor for a binary file.
    Read the bytes, XOR each byte with a key (integer 0-255), and save it.
    Running it twice with the same key encrypts and then decrypts the file.
    """
    with open(filename, "wb") as f:
        f.write(b"Secret Message")

    # Read original
    with open(filename, "rb") as f:
        data = bytearray(f.read())
    
    # Encrypt
    for i in range(len(data)):
        data[i] ^= key
        
    with open(filename + ".enc", "wb") as f:
        f.write(data)
        
    # Decrypt
    with open(filename + ".enc", "rb") as f:
        enc_data = bytearray(f.read())
        
    for i in range(len(enc_data)):
        enc_data[i] ^= key
        
    print(f"\nDecrypted Message: {enc_data.decode('utf-8')}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Binary files store raw bytes, not encoded text.
# - Use 'rb' and 'wb' to handle binary data.
# - Strings must be encoded into bytes before writing.
# - Pickle is powerful for saving Python states, but unsafe for untrusted data.

if __name__ == "__main__":
    file_encryptor("secret.bin", 42)
