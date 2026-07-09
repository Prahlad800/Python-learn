"""
Topic: Introduction to Coroutines (Legacy Generators)
Chapter: 18
Level: Advanced

Description:
    Before `async` and `await` were introduced in Python 3.5, asynchronous programming 
    was achieved using generator-based coroutines. By using `.send()`, generators act 
    as basic coroutines, consuming data and cooperating to yield control back to an event loop.
    Understanding this is crucial for understanding how modern `asyncio` works under the hood.

Real-Life Analogy:
    Imagine two workers sharing a single desk. Worker A starts a task, realizes they need 
    to wait for glue to dry, and yields the desk to Worker B. Worker B works for a bit, 
    yields the desk back to A, and so on. They cooperatively multitask.

Key Concepts:
    - Generators as Coroutines
    - Cooperative Multitasking
    - The @coroutine decorator pattern (historical)
"""
from typing import Generator, Any
from functools import wraps

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def coroutine_decorator(func):
    """
    A classic decorator used to auto-prime coroutines.
    This saves us from calling next(gen) manually every time.
    """
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)  # Prime the generator
        return gen
    return primer

@coroutine_decorator
def simple_receiver() -> Generator[None, str, None]:
    """A coroutine that receives and prints messages."""
    print("Receiver ready!")
    while True:
        msg = yield
        print(f"Received: {msg}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

@coroutine_decorator
def string_filter(target_word: str, next_coroutine: Generator) -> Generator[None, str, None]:
    """Filters strings and passes matches to the next coroutine."""
    while True:
        text = yield
        if target_word in text:
            next_coroutine.send(text)

@coroutine_decorator
def string_sink() -> Generator[None, str, None]:
    """The final destination for filtered strings."""
    try:
        while True:
            text = yield
            print(f"Sink Saved: {text}")
    except GeneratorExit:
        print("Sink closed gracefully.")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Simulating an event loop that alternates execution between two coroutines.

def task_a() -> Generator[str, None, None]:
    yield "Task A Step 1"
    yield "Task A Step 2"
    yield "Task A Done"

def task_b() -> Generator[str, None, None]:
    yield "Task B Step 1"
    yield "Task B Step 2"
    yield "Task B Done"

def event_loop(tasks: list[Generator]):
    """A naive cooperative multitasking event loop."""
    while tasks:
        current_task = tasks.pop(0)
        try:
            result = next(current_task)
            print(f"Event Loop received: {result}")
            tasks.append(current_task) # Put it back in queue to run again later
        except StopIteration:
            print("A task finished.")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Confusing generator coroutines with native `async def` coroutines.
# Correction: Modern Python uses `async def` for coroutines. Generator-based 
# coroutines are mostly legacy, but they are the foundational concept behind `asyncio`.

# Best Practice: Use a priming decorator if you are writing heavily send-based generators 
# to avoid boilerplate `next()` calls.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What makes a generator a coroutine?
# A1: When a generator uses `.send()` to consume values from the caller, it acts as a coroutine.
#
# Q2: What is cooperative multitasking?
# A2: A system where tasks voluntarily yield control periodically (via `yield`), allowing 
#     other tasks to run on the same thread.
#
# Q3: Why do we prime a coroutine?
# A3: Because the generator must execute up to the first `yield` expression to be ready 
#     to receive a value via `.send()`.
#
# Q4: How is `GeneratorExit` triggered?
# A4: By calling the `.close()` method on the generator object.
#
# Q5: How did generator coroutines evolve in Python?
# A5: They evolved into native coroutines defined by `async def` and `await` in Python 3.5.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a coroutine that receives integers and keeps a running product.
# Exercise 2: Chain three coroutines: input -> double value -> print value.
# Exercise 3: Write a simple event loop that handles three separate countdown generators.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge: Create a routing coroutine that receives a dictionary `{"type": "error", "msg": "..."}` 
# and routes the message to either an `error_sink` coroutine or an `info_sink` coroutine based on the type.

@coroutine_decorator
def info_sink() -> Generator[None, dict, None]:
    while True:
        data = yield
        print(f"INFO SINK: {data['msg']}")

@coroutine_decorator
def error_sink() -> Generator[None, dict, None]:
    while True:
        data = yield
        print(f"ERROR SINK: {data['msg']}")

@coroutine_decorator
def router(info_target: Generator, error_target: Generator) -> Generator[None, dict, None]:
    while True:
        data = yield
        if data.get("type") == "error":
            error_target.send(data)
        else:
            info_target.send(data)

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Coroutines use `yield` to pause and receive data.
# - They require priming (`next()`) before receiving the first value.
# - They allow cooperative multitasking on a single thread.
# - They are the conceptual predecessors to modern `asyncio`.

if __name__ == "__main__":
    print("--- Simple Receiver ---")
    recv = simple_receiver()
    recv.send("Hello")
    recv.send("World")
    
    print("\n--- Pipeline of Coroutines ---")
    sink = string_sink()
    filt = string_filter("Python", sink)
    
    filt.send("I love Java")
    filt.send("Python is great")
    filt.send("C++ is fast")
    filt.send("Learning Python generators")
    sink.close()
    
    print("\n--- Event Loop ---")
    t1 = task_a()
    t2 = task_b()
    event_loop([t1, t2])
    
    print("\n--- Mini Challenge (Router) ---")
    i_sink = info_sink()
    e_sink = error_sink()
    msg_router = router(i_sink, e_sink)
    
    msg_router.send({"type": "info", "msg": "System booted."})
    msg_router.send({"type": "error", "msg": "Failed to connect to DB."})
    msg_router.send({"type": "info", "msg": "User logged in."})
