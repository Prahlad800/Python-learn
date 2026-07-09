"""
Topic: Iterators Project
Chapter: 19
Level: Advanced

Description:
    In this comprehensive project, we will build a Data Stream Processing pipeline using custom iterators and the itertools module. The project simulates reading a massive, continuous stream of temperature sensor data, filtering out anomalies, smoothing the data using a moving average, and detecting significant temperature spikes—all using lazy evaluation to ensure minimal memory usage.

Real-Life Analogy:
    Think of a water filtration plant. The river water (data stream) flows in continuously. It passes through a coarse filter (anomaly removal), then a chemical treatment tank (moving average), and finally a quality check station (spike detection). The water never stops flowing, and the plant only processes what's currently in the pipes (lazy evaluation), rather than holding the entire river in a giant tank.

Key Concepts:
    - Custom Iterators
    - Iterator Chaining and Pipelining
    - Lazy Evaluation
    - Yielding stateful calculations (Moving Average)
"""

import random
import itertools
from typing import Iterator, Iterable

# ============================================================
# SECTION 1: DATA SOURCE GENERATION (THE STREAM)
# ============================================================

class SensorStream:
    """
    An infinite iterator that simulates a temperature sensor.
    Generates temperatures mostly around 20-25C, with occasional extreme anomalies.
    """
    def __iter__(self):
        return self
        
    def __next__(self) -> float:
        # 5% chance of a sensor error (anomaly)
        if random.random() < 0.05:
            return random.uniform(-50.0, 100.0)
        # Normal fluctuation
        return random.uniform(20.0, 25.0)


# ============================================================
# SECTION 2: FILTERING OUT ANOMALIES
# ============================================================

def anomaly_filter(stream: Iterable[float]) -> Iterator[float]:
    """
    A generator that lazily filters out impossible temperature readings.
    Assume valid room temperatures are between 10C and 40C.
    """
    for temp in stream:
        if 10.0 <= temp <= 40.0:
            yield temp
        else:
            # We log the anomaly but don't yield it downstream
            # In a real system, you might yield to an error log stream
            pass


# ============================================================
# SECTION 3: SMOOTHING DATA (MOVING AVERAGE)
# ============================================================

class MovingAverageIterator:
    """
    A custom iterator that maintains a sliding window to calculate
    the moving average of the data stream.
    """
    def __init__(self, stream: Iterable[float], window_size: int = 3):
        self.stream = iter(stream)
        self.window_size = window_size
        self.window = []
        
    def __iter__(self):
        return self
        
    def __next__(self) -> float:
        # Read from the upstream iterator
        val = next(self.stream)
        self.window.append(val)
        
        # Maintain window size
        if len(self.window) > self.window_size:
            self.window.pop(0)
            
        # Return average of current window
        return sum(self.window) / len(self.window)


# ============================================================
# SECTION 4: DETECTING SPIKES
# ============================================================

def detect_spikes(stream: Iterable[float], threshold: float = 2.0) -> Iterator[str]:
    """
    Analyzes the smoothed stream and yields an alert if the temperature
    jumps by more than `threshold` degrees between consecutive readings.
    """
    stream_iter = iter(stream)
    
    try:
        prev_temp = next(stream_iter)
    except StopIteration:
        return

    for current_temp in stream_iter:
        diff = current_temp - prev_temp
        if diff > threshold:
            yield f"ALERT! Rapid temp rise detected: +{diff:.2f}C (Current: {current_temp:.2f}C)"
        elif diff < -threshold:
            yield f"ALERT! Rapid temp drop detected: {diff:.2f}C (Current: {current_temp:.2f}C)"
        else:
            yield f"Stable: {current_temp:.2f}C"
            
        prev_temp = current_temp


# ============================================================
# SECTION 5: PIPELINE EXECUTION (MAIN PROJECT RUN)
# ============================================================

def run_project() -> None:
    print("--- Starting Data Processing Pipeline Project ---")
    random.seed(42) # For reproducible output
    
    # 1. Initialize the infinite data source
    raw_sensor = SensorStream()
    
    # 2. Connect the filter (Pipeline stage 1)
    clean_sensor = anomaly_filter(raw_sensor)
    
    # 3. Connect the moving average (Pipeline stage 2)
    smoothed_sensor = MovingAverageIterator(clean_sensor, window_size=5)
    
    # 4. Connect the spike detector (Pipeline stage 3)
    final_output = detect_spikes(smoothed_sensor, threshold=1.0)
    
    # 5. Consume the pipeline
    # Because it's an infinite stream, we MUST limit the consumption
    # We use itertools.islice to safely consume exactly 20 items from the final pipeline
    print("Fetching 20 processed readings:")
    
    for alert_or_status in itertools.islice(final_output, 20):
        print(alert_or_status)


# ============================================================
# SECTION 6: COMMON MISTAKES AND BEST PRACTICES (IN PIPELINES)
# ============================================================
"""
Mistakes in Pipeline Design:
1. Converting an intermediate stream to a list (e.g., `list(clean_sensor)`). This breaks laziness and, for infinite streams, causes a memory crash.
2. Forgetting that downstream iterators consume upstream iterators. If you branch the stream, one branch will "steal" data from the other.

Best Practices:
- Keep each iterator/generator focused on a single responsibility (Single Responsibility Principle).
- Use `itertools.islice` when testing infinite pipelines.
- Use generator functions (`yield`) for simple stateless mappings/filters, and Custom Iterator classes when you need to maintain internal state (like the Moving Average window).
"""

# ============================================================
# SECTION 7: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: Why is this pipeline approach better than putting all logic in one massive `for` loop?
A1: Modularity and testing. Each stage (filter, smooth, alert) can be tested independently and reused in different combinations.

Q2: What happens if `anomaly_filter` drops a value? Does `MovingAverageIterator` break?
A2: No. `MovingAverageIterator` simply calls `next()` on the filter. The filter handles the skipping internally and only yields valid values. The downstream stages don't even know data was dropped.
"""

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- Iterators can be chained together to form powerful data processing pipelines.
- The pipeline pulls data lazily; computations only happen when the final output is consumed.
- Custom iterator classes are excellent for stateful operations (like sliding windows).
- Generator functions are great for simple transformations and filtering.
"""

if __name__ == "__main__":
    run_project()
