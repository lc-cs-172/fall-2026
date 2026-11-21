# Note 33

## Searching

Suppose you are given the task to write a function

```python
def search(haystack, needle) -> int:
```

that searches the array `haystack` for the value `needle`.  It returns either
`-1`, if it cannot find the value or returns the index of an occurrence of
`needle` in `haystack`.

What is the runtime of `search` as a function of the number of elements in
`haystack`?

### Puzzle

Is this the best you can do?

Can you improve the runtime, if the values in `haystack` are in sorted order?

## Order of growth

In some situation, the efficiency of an algorithm depends not just on $n$ (the
size of the problem) but also on data content. In such situation, you must
clarify whether a statement is about best-case, average, or worst-case
performance.

For instance, the search function above would find the `needle` on the first
check, if `needle` appears first in `haystack`. In such case, you would say that
`search` is $O(1)$ in the *best case*. If the `needle` is located at the end of
the array or if it is entirely absent, then you would need to make $n$ checks,
where $n$ is the number of elements in the array. In this case, you would say
that `search` is $O(n)$ in the *worst case*.

To study average performance you must make some assumptions about the
distribution of data. One plausible assumption is to state that `needle` is
present somewhere, appears only once, and its actual location in the array is
uniformly distributed (i.e., it is equally likely to appear anywhere in the
array). With some analysis, it is relatively easy to determine that the
performance, under these assumptions, of `search` is $O(n)$ on *average*.
