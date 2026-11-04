"""Doubling test implementation inspired by Sedgewick and Wayne."""

import random
import time

def count_triples(xs : list[int]) -> int:
    """Return the number of distinct triples (i, j, k) such that
    xs[i] + xs[j] + xs[k] = 0.
    """
    count = 0
    n = len(xs)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if xs[i] + xs[j] + xs[k] == 0:
                    count += 1
    return count

def gen_array_of_random_ints(n : int) -> list[int]:
    xs = []
    for _ in range(n):
        xs.append(random.randint(-100_000, +100_000))
    return xs

def time_count_triples(n : int) -> float:
    """Return the number of seconds that it takes to count the number of triples
    in an array of `n` integers.
    """
    xs = gen_array_of_random_ints(n)
    start = time.time()
    count_triples(xs)
    end = time.time()
    return end - start

def main():
    """Display the impact on a function's running time when doubling the input
    size.
    """
    n = 16
    prev = time_count_triples(n)
    print('{:>9} {:>6}'.format('n', 'ratio'))
    while True:
        n *= 2
        next = time_count_triples(n)
        print('{:-9} {:-6.1f}'.format(n, next/prev))
        prev = next

if __name__ == '__main__':
    main()
