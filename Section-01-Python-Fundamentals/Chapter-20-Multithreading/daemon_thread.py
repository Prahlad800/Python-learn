# Topic: Daemon Threads
# Explanation: Daemon threads run in the background and do not block program shutdown.

# Syntax:
# import threading

thread = threading.Thread(target=lambda: print("Background task"), daemon=True)
thread.start()
thread.join()

# Examples:
# import threading

thread = threading.Thread(target=lambda: print("Background task"), daemon=True)
thread.start()
thread.join()

# Practice Programs:
# 1. Create a daemon thread.
2. Observe that it exits with the main thread.

# Interview Questions:
# Q: What is a daemon thread?
A: It is a background thread that stops when the main program exits.

# Expected Output:
# Background task

import threading

thread = threading.Thread(target=lambda: print("Background task"), daemon=True)
thread.start()
thread.join()
