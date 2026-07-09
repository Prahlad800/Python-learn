"""
Topic: Variables and Data Types Practice 4
Chapter: 2
Level: Intermediate

Description:
    This file serves as the final practice for Chapter 2, focusing on Number Systems 
    and integrating all the concepts learned so far (Variables, Constants, Types, Casting, etc.).

Real-Life Analogy:
    This is the final exam of the chapter where you must assemble a full device 
    using all the individual components you've learned about.

Key Concepts:
    - Number Systems Conversion
    - Data Structure manipulation
    - Constants and Data Typing integration
"""

from typing import Final

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def number_bases() -> None:
    """Practice reading and converting bases."""
    print("--- Exercise 1: Number Bases ---")
    
    binary_val = 0b1010  # 10
    hex_val = 0xA        # 10
    
    print(f"Binary 0b1010 in Decimal: {binary_val}")
    print(f"Hex 0xA in Decimal: {hex_val}")
    print(f"Are they equal? {binary_val == hex_val}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def data_type_assembly() -> None:
    """Building a complex data structure representing a server."""
    print("\n--- Exercise 2: Data Assembly ---")
    
    server_info = {
        "hostname": "db-server-01",
        "ip_address": "192.168.1.100",
        "port": 5432,
        "is_active": True,
        "backup_server": None,
        "supported_protocols": {"tcp", "udp"} # Set
    }
    
    print("Server Configuration:")
    for key, value in server_info.items():
        # Using type() to show we understand the contents
        print(f"  {key}: {value} ({type(value).__name__})")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

MAX_CONNECTIONS: Final[int] = 100

def constant_and_casting() -> None:
    """Simulate reading config and applying limits."""
    print("\n--- Exercise 3: Constants and Casting ---")
    
    # Read from a simulated config file (always string)
    config_current_connections = "85"
    
    # Cast to integer
    active_conns = int(config_current_connections)
    
    remaining = MAX_CONNECTIONS - active_conns
    print(f"Active: {active_conns}/{MAX_CONNECTIONS}. Remaining slots: {remaining}")
    
    # Boolean logic to check capacity
    is_at_capacity = active_conns >= MAX_CONNECTIONS
    print(f"Is server at capacity? {is_at_capacity}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def base_conversion_pitfalls() -> None:
    """Handling base conversions safely."""
    print("\n--- Exercise 4: Base Conversion Pitfalls ---")
    
    hex_string = "FF"
    
    # Pitfall: int("FF") will throw an error because it assumes base 10.
    # Correction: specify base 16
    try:
        decimal_val = int(hex_string, 16)
        print(f"Correctly parsed hex '{hex_string}' to {decimal_val}")
    except ValueError as e:
        print(f"Failed: {e}")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
1. Can you store a hexadecimal number in a Python dictionary?
   Answer: Yes, you can store `0xFF` in a dictionary, but it will be stored and printed internally as its decimal equivalent `255` unless formatted otherwise.

2. Combine type casting, booleans, and none: what does `bool(int(None))` do?
   Answer: It throws a TypeError. `int(None)` is invalid because `NoneType` cannot be cast to an integer.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Practice on your own:
1. Write a function that takes a binary string (e.g., "1100") and a hex string (e.g., "A"), converts both to integers, and returns their sum.
2. Create a list containing an int, a float, a string, a boolean, and None. Loop through and print their types.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge() -> None:
    """Final Chapter 2 Integration Challenge."""
    print("\n--- Final Mini Challenge: System Diagnostics ---")
    
    # 1. Variables & Types
    sys_name = "Mainframe"
    memory_gb = 64.0
    
    # 2. Number systems (Error code in hex)
    last_error_code = 0x404
    
    # 3. None Type
    pending_updates = None
    
    # 4. Casting & User Input Simulation
    simulated_cpu_usage_input = "78.5"
    cpu_usage = float(simulated_cpu_usage_input)
    
    # 5. Booleans
    is_healthy = cpu_usage < 90.0 and last_error_code == 0
    
    print(f"System: {sys_name}")
    print(f"Memory: {memory_gb}GB | CPU: {cpu_usage}%")
    print(f"Last Error Code: {last_error_code} (Hex: {hex(last_error_code)})")
    
    if pending_updates is None:
        print("Update Status: Unknown (None)")
        
    print(f"System Healthy: {is_healthy}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
Summary:
- Number systems provide flexibility in representing binary and hex data.
- Constants ensure configuration limits are respected.
- Type casting and truthiness are required to cleanly process parsed data.
- This concludes the core foundational knowledge of Python variables and data types!
"""

if __name__ == "__main__":
    number_bases()
    data_type_assembly()
    constant_and_casting()
    base_conversion_pitfalls()
    mini_challenge()
