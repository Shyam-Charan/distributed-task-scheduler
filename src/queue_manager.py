"""Thread-safe priority queue for tasks."""
import heapq
import itertools
import threading


class TaskQueue:
    def __init__(self):
        self._heap = []
        self._counter = itertools.count()
        self._condition = threading.Condition()

    def put(self, task, priority=0):
        with self._condition:
            heapq.heappush(self._heap, (-priority, next(self._counter), task))
            self._condition.notify()

    def get(self, timeout=None):
        with self._condition:
            if not self._heap and not self._condition.wait(timeout):
                return None
            if not self._heap:
                return None
            return heapq.heappop(self._heap)[2]

    def __len__(self):
        with self._condition:
            return len(self._heap)
