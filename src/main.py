"""Runnable scheduler demo."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.scheduler import Scheduler


def square(x):
    return x * x


def main():
    scheduler = Scheduler(workers=2)
    scheduler.submit(square, 3, priority=1)
    scheduler.submit(square, 5, priority=10)
    futures = [scheduler.run_once(), scheduler.run_once()]
    print([future.result() for future in futures])
    scheduler.shutdown()


if __name__ == "__main__":
    main()
