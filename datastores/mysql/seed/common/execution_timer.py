import time
from contextlib import contextmanager

@contextmanager
def execution_timer(label = ""):
    start = time.perf_counter()
    yield
    end = time.perf_counter()

    time_taken = end - start
    print(f"{label} | {time_taken:.3f}s")
