# Note 13

## Recursion

* Algorithmically: Solving a problem by a *divide-and-conquer* or
  *decrease-and-conquer* strategy

* Semantically: A function that calls itself (directly or indirectly)

## Pitfalls of recursion

* Missing base case
* No guarantee of convergence
* Excessive recomputation
* Excessive memory requirements

## Call graph

According to [this](https://en.wikipedia.org/wiki/Call_graph) Wikipedia article,
a *call graph* [...] represents the relationships between functions in a
computer program.

## Fibonacci sequence

```python
def fib(n : int) -> int:
    """Return the nth member of the Fibonacci sequence."""
    if n == 0: return 0
    if n == 1: return 1
    return fib(n - 1) + fib(n - 2)
```
