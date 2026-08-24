# Distributed Task Scheduler

A lightweight Python task scheduler that combines **priority-based scheduling**, a **thread-safe task queue**, and a **concurrent worker pool**.

## Architecture

```text
submit(task, priority)
        |
        v
+-------------------+
| Priority TaskQueue|
| heap + Condition  |
+-------------------+
        |
        v
+-------------------+
| Scheduler         |
| dispatches tasks  |
+-------------------+
        |
        v
+-------------------+
| WorkerPool        |
| ThreadPoolExecutor|
+-------------------+
        |
        v
     Future
```

## Components

- `queue_manager.py` — max-priority queue implemented with `heapq`; equal-priority tasks preserve FIFO insertion order.
- `scheduler.py` — accepts tasks, assigns priorities and dispatches work.
- `worker.py` — concurrent execution using `ThreadPoolExecutor`.
- `main.py` — runnable example.

## Run

```bash
python -m src.main
```

## Example

```python
from src.scheduler import Scheduler

scheduler = Scheduler(workers=4)
future = scheduler.submit(pow, 2, 10, priority=5)
print(future.result())
scheduler.shutdown()
```

The queue uses a condition variable so workers can wait for work without busy-spinning. Scheduler submission is separated from execution, making the components independently testable.
