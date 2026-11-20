"""Measure the time its take to compute some function."""

from itertools import accumulate
import random
import time
from linear import search

def time_search(n : int) -> float:
    """Run a doubling experiment."""
    xs = list(accumulate(random.randint(1, 10) for _ in range(n)))
    start = time.time()
    search(xs, -1)
    end = time.time()
    return end - start

def main():
    n = 1024
    t_prev = time_search(n)
    print('{:>8s} {:>8s} {:>8s}'.format('size', 'time', 'ratio'))
    while True:
        n *= 2
        t = time_search(n)
        print('{:8d} {:8.1f} {:8.2f}'.format(n, t, t/t_prev))
        t_prev = t

if __name__ == '__main__':
    main()
