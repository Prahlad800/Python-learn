"""
Topic: String Encoding and Decoding
Chapter: 8
Level: Advanced

Description:
    In Python 3, all strings are sequences of Unicode characters. To save these to disk or send them over a network, they must be encoded into bytes (e.g., UTF-8).
    Conversely, bytes received must be decoded back into strings.

Real-Life Analogy:
    A string is an abstract thought. Encoding is translating that thought into spoken words (audio waves or bytes). Decoding is a listener taking those audio waves and turning them back into a thought.

Key Concepts:
    - str vs bytes
    - encode() method
    - decode() method
    - UTF-8 encoding
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_encoding():
    """Encoding strings to bytes and vice versa."""
    text = "Hello, Python! 🐍"
    print(f"Original String: {text} (type: {type(text)})")
    
    # Encode string to bytes
    encoded_bytes = text.encode("utf-8")
    print(f"Encoded Bytes: {encoded_bytes} (type: {type(encoded_bytes)})")
    
    # Decode bytes to string
    decoded_text = encoded_bytes.decode("utf-8")
    print(f"Decoded String: {decoded_text}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def handling_errors():
    """Dealing with decoding errors."""
    # Let's create some invalid bytes
    invalid_bytes = b"\xff\xfeH\x00e\x00l\x00l\x00o\x00" # UTF-16 bytes
    
    # Decoding with wrong encoding raises UnicodeDecodeError
    try:
        invalid_bytes.decode("utf-8")
    except UnicodeDecodeError as e:
        print("Error decoding:", e)
        
    # Handling errors gracefully
    safe_decode = invalid_bytes.decode("utf-8", errors="replace")
    print("Safe Decode (with replace):", safe_decode)
    
    safe_ignore = invalid_bytes.decode("utf-8", errors="ignore")
    print("Safe Decode (with ignore):", safe_ignore)

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def different_encodings():
    """Working with ASCII and UTF-16."""
    text = "Café"
    
    # ASCII encoding (fails on non-ASCII characters)
    try:
        text.encode("ascii")
    except UnicodeEncodeError as e:
        print("Cannot encode to ASCII:", e)
        
    # But it works with replacement
    print("ASCII with replacement:", text.encode("ascii", errors="replace"))
    
    # UTF-16 encoding
    print("UTF-16 encoding:", text.encode("utf-16"))

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Mixing up strings (text data) and bytes (binary data). 
# You cannot concatenate a string and a bytes object.
# b"Hello" + " World" # Raises TypeError

# Best Practice: Always explicitly use UTF-8 as the encoding when reading/writing files or networking.
# Best Practice: The "Unicode Sandwich" model - Decode bytes as early as possible on input, work with strings in the app, and encode to bytes as late as possible on output.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q: What is the difference between a string and a bytes object in Python 3?
A: Strings (`str`) are sequences of Unicode characters. Bytes (`bytes`) are sequences of 8-bit integers representing binary data.

Q: What is the default encoding for `encode()` and `decode()`?
A: `utf-8`.

Q: What does the `b""` prefix do?
A: It defines a bytes literal instead of a string literal.

Q: How do you handle characters that cannot be decoded?
A: Use the `errors="ignore"` or `errors="replace"` arguments in the `decode()` method.

Q: Why is UTF-8 universally preferred?
A: It is backward compatible with ASCII and can represent any Unicode character efficiently.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# 1. Encode your name into UTF-8 bytes and print the bytes object.
# 2. Take a bytes object `b'Hello\xc2\xa0World'` and decode it using UTF-8.
# 3. Create a string with an emoji, encode it to UTF-16, and then decode it back.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """Convert a list of string messages into a single bytes payload, then parse it back."""
    messages = ["System OK", "Cpu 45%", "Warning: 🛑"]
    
    # Serialize: join with newline, then encode
    joined = "\n".join(messages)
    payload = joined.encode("utf-8")
    print("Transmitted payload:", payload)
    
    # Deserialize: decode, then split
    received = payload.decode("utf-8").split("\n")
    print("Received messages:", received)

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Strings (`str`) are for text; bytes (`bytes`) are for binary data.
- `encode()` converts string to bytes.
- `decode()` converts bytes to string.
- UTF-8 is the standard and default encoding.
- Handle encoding/decoding exceptions using the `errors` parameter.
"""

if __name__ == "__main__":
    basic_encoding()
    handling_errors()
    different_encodings()
    mini_challenge()
