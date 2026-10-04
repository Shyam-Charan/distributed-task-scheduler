import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.queue_manager import TaskQueue
from src.scheduler import Scheduler


def test_priority_queue_orders_high_priority_first():
    q = TaskQueue()
    q.put("low", priority=1)
    q.put("high", priority=10)
    q.put("medium", priority=5)
    assert q.get() == "high"
    assert q.get() == "medium"
    assert q.get() == "low"


def test_scheduler_executes_task_and_returns_future():
    scheduler = Scheduler(workers=2)
    try:
        scheduler.submit(lambda x: x * x, 7, priority=3)
        future = scheduler.run_once()
        assert future.result(timeout=2) == 49
    finally:
        scheduler.shutdown()


def test_scheduler_empty_queue_returns_none():
    scheduler = Scheduler(workers=1)
    try:
        assert scheduler.run_once(timeout=0) is None
    finally:
        scheduler.shutdown()


def test_equal_priority_tasks_are_fifo():
    q = TaskQueue()
    for name in ["first", "second", "third"]:
        q.put(name, priority=5)
    assert [q.get(), q.get(), q.get()] == ["first", "second", "third"]
