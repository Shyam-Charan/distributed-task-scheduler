"""Priority scheduler backed by a worker pool."""
from .queue_manager import TaskQueue
from .worker import WorkerPool


class Scheduler:
    def __init__(self, workers=4):
        self.queue = TaskQueue()
        self.pool = WorkerPool(workers)

    def submit(self, fn, *args, priority=0, **kwargs):
        self.queue.put((fn, args, kwargs), priority)

    def run_once(self, timeout=0):
        item = self.queue.get(timeout)
        if item is None:
            return None
        fn, args, kwargs = item
        return self.pool.submit(fn, *args, **kwargs)

    def shutdown(self):
        self.pool.shutdown()
