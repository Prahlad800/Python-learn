"""
Topic: Comprehensive Decorator Project
Chapter: 17
Level: Advanced

Description:
    This file combines all the concepts learned in this chapter into a small, realistic project.
    We will build a simple Web API Mock System using decorators for routing, authentication, and validation.

Real-Life Analogy:
    Building a custom web framework (like a mini-Flask). 
    Decorators will act as the traffic cops, security guards, and data inspectors for our fake web endpoints.

Key Concepts:
    - Decorator registries (routing).
    - Stacked decorators.
    - Parameter validation.
    - Preserving metadata.
"""

import functools
import json

# ============================================================
# SECTION 1: SYSTEM SETUP (THE REGISTRY)
# ============================================================

# Our application "router"
ROUTES = {}
CURRENT_USER = None  # Mock session state

def route(path):
    """Registers a function to a specific URL path."""
    def decorator(func):
        ROUTES[path] = func
        return func
    return decorator

# ============================================================
# SECTION 2: MIDDLEWARE DECORATORS
# ============================================================

def require_auth(func):
    """Ensures a user is logged in before accessing the endpoint."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not CURRENT_USER:
            return {"status": 401, "error": "Unauthorized"}
        return func(*args, **kwargs)
    return wrapper

def json_response(func):
    """Formats the output of the function as a JSON string."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, dict) and "status" in result:
            return json.dumps(result, indent=2)
        # Wrap normal responses
        return json.dumps({"status": 200, "data": result}, indent=2)
    return wrapper

def validate_json_body(*required_keys):
    """Validates that the provided dictionary contains the required keys."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(body, *args, **kwargs):
            if not isinstance(body, dict):
                return {"status": 400, "error": "Invalid payload format. Expected dict."}
            
            missing = [key for key in required_keys if key not in body]
            if missing:
                return {"status": 400, "error": f"Missing required fields: {missing}"}
            
            return func(body, *args, **kwargs)
        return wrapper
    return decorator

# ============================================================
# SECTION 3: BUILDING THE ENDPOINTS
# ============================================================

# Unprotected route
@route("/api/status")
@json_response
def get_status():
    """Returns the API status."""
    return {"server": "online", "version": "1.0.0"}

# Protected route requiring authentication
@route("/api/user/profile")
@json_response
@require_auth
def get_profile():
    """Returns the profile of the current user."""
    return {"id": 1, "username": CURRENT_USER, "role": "admin"}

# Complex POST route
@route("/api/user/create")
@json_response
@require_auth
@validate_json_body("username", "password", "email")
def create_user(body):
    """Creates a new user based on the JSON body."""
    # Simulation of DB save
    return {"message": f"User {body['username']} created successfully."}

# ============================================================
# SECTION 4: MOCK SERVER ENGINE
# ============================================================

def simulate_request(path, method="GET", body=None):
    """Simulates an incoming HTTP request."""
    print(f"\n---> [{method}] {path}")
    
    if path not in ROUTES:
        print(json.dumps({"status": 404, "error": "Not Found"}, indent=2))
        return
        
    endpoint = ROUTES[path]
    
    if method == "POST":
        response = endpoint(body)
    else:
        response = endpoint()
        
    print(response)

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: In the `create_user` endpoint, what happens if we put `@route` below `@json_response`?
# A1: If `@route` is below `@json_response`, the router registers the unwrapped original function instead of the fully decorated, JSON-formatted wrapper!

# Q2: Why is `@functools.wraps` crucial in web frameworks like Flask?
# A2: Because Flask uses the function name (via `__name__`) as the identifier for building URLs and routes. Without it, all endpoints might be named `wrapper`.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise: Add a new decorator `@log_request` that prints the path and method before executing.
# Add it to the endpoint below.

def log_request(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[SYSTEM LOG] Executing {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@route("/api/test")
@log_request
@json_response
def test_endpoint():
    return "Test successful"

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge: Test the API flow!

def run_challenge():
    global CURRENT_USER
    
    # 1. Unauthenticated request to protected route
    simulate_request("/api/user/profile")
    
    # 2. Login
    CURRENT_USER = "john_doe"
    print("\n(System: User logged in as john_doe)")
    
    # 3. Authenticated request
    simulate_request("/api/user/profile")
    
    # 4. POST request missing a field
    simulate_request("/api/user/create", method="POST", body={"username": "alice", "email": "a@a.com"})
    
    # 5. Successful POST request
    simulate_request("/api/user/create", method="POST", body={"username": "alice", "email": "a@a.com", "password": "123"})
    
    # 6. Test logging endpoint
    simulate_request("/api/test")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Decorators are incredibly powerful for aspect-oriented programming.
# - They cleanly separate business logic from infrastructure (auth, validation, formatting).
# - Stacking order is critical in frameworks!

if __name__ == "__main__":
    print("--- Starting Mock Server ---")
    simulate_request("/api/status")
    
    print("\n--- Running API Challenge ---")
    run_challenge()
