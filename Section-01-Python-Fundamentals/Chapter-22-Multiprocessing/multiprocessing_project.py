"""
Topic: Multiprocessing Mini Project
Chapter: 22
Level: Advanced

Description:
    This project integrates Queues, Process Pools, and Synchronization.
    Scenario: An Image Processing Pipeline.
    1. A Producer process scans a directory and finds image paths.
    2. A Pool of Worker processes resizes/filters the images.
    3. A Consumer process takes the processed images and logs the results to a file using a Lock.

Real-Life Analogy:
    A mail room. One person sorts incoming packages (Producer), a team of workers opens and inspects them (Pool), and one manager writes down the inventory log (Consumer).
"""

import multiprocessing
import time
import os
import random

# ============================================================
# HELPER FUNCTIONS (Mocking real image processing)
# ============================================================

def process_image(image_name: str) -> dict:
    """Mock function to simulate CPU-heavy image processing."""
    print(f"[Worker PID {os.getpid()}] Started processing {image_name}")
    # Simulate processing time based on image size
    processing_time = random.uniform(0.5, 1.5)
    time.sleep(processing_time)
    
    return {
        "image": image_name,
        "status": "Success",
        "time_taken": round(processing_time, 2)
    }

# ============================================================
# PIPELINE COMPONENTS
# ============================================================

def image_finder(task_queue: multiprocessing.Queue, num_images: int):
    """Producer: Finds images and adds them to the queue."""
    print("[Finder] Scanning for images...")
    for i in range(1, num_images + 1):
        img = f"vacation_photo_{i}.jpg"
        task_queue.put(img)
        print(f"[Finder] Added {img} to queue.")
        time.sleep(0.1)
    
    # Add sentinels for the pool workers (assuming 3 workers)
    for _ in range(3):
        task_queue.put(None)
    print("[Finder] Done adding images.")

def worker_pool_handler(task_queue: multiprocessing.Queue, result_queue: multiprocessing.Queue):
    """Worker: Pulls from task queue, processes, puts in result queue."""
    while True:
        img = task_queue.get()
        if img is None:
            # Sentinel received, shut down this worker
            result_queue.put(None) 
            break
            
        # Process the image
        result = process_image(img)
        
        # Send result downstream
        result_queue.put(result)

def result_logger(result_queue: multiprocessing.Queue, file_lock: multiprocessing.Lock):
    """Consumer: Logs results safely."""
    active_workers = 3
    
    print("[Logger] Started logging service...")
    
    # Open file with 'w' mode initially to clear it, then append
    with open("processing_log.txt", "w") as f:
        f.write("--- Image Processing Log ---\n")
        
    while active_workers > 0:
        result = result_queue.get()
        
        if result is None:
            active_workers -= 1
            continue
            
        # Safely write to file
        with file_lock:
            with open("processing_log.txt", "a") as f:
                log_entry = f"{result['image']} | {result['status']} | {result['time_taken']}s\n"
                f.write(log_entry)
                print(f"[Logger] Logged: {result['image']}")

# ============================================================
# MAIN EXECUTION
# ============================================================

def main():
    print("=== Starting Image Processing Pipeline ===")
    
    # Queues for IPC
    task_queue = multiprocessing.Queue()
    result_queue = multiprocessing.Queue()
    
    # Lock for file writing
    file_lock = multiprocessing.Lock()
    
    # 1. Start Logger (Consumer)
    logger_proc = multiprocessing.Process(target=result_logger, args=(result_queue, file_lock))
    logger_proc.start()
    
    # 2. Start Workers (Pool)
    workers = []
    for i in range(3):
        p = multiprocessing.Process(target=worker_pool_handler, args=(task_queue, result_queue))
        workers.append(p)
        p.start()
        
    # 3. Start Finder (Producer)
    # Note: We can run this in the main process, but let's make it a separate process
    finder_proc = multiprocessing.Process(target=image_finder, args=(task_queue, 10))
    finder_proc.start()
    
    # Wait for Finder to finish
    finder_proc.join()
    
    # Wait for Workers to finish
    for w in workers:
        w.join()
        
    # Wait for Logger to finish
    logger_proc.join()
    
    print("=== Pipeline Complete ===")
    
    # Display the log file
    if os.path.exists("processing_log.txt"):
        print("\n--- Log File Contents ---")
        with open("processing_log.txt", "r") as f:
            print(f.read())
            
        # Cleanup
        os.remove("processing_log.txt")

if __name__ == "__main__":
    main()
