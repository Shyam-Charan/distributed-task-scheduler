"""Concurrent worker pool."""
from concurrent.futures import ThreadPoolExecutor


class WorkerPool:
    def __init__(self, workers=4):
        if workers < 1:
            raise ValueError("workers must be >= 1")
        self.executor = ThreadPoolExecutor(max_workers=workers)

    def submit(self, fn, *args, **kwargs):
        return self.executor.submit(fn, *args, **kwargs)

    def shutdown(self, wait=True):
        self.executor.shutdown(wait=wait)
