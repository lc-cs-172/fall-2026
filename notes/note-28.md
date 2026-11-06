# Note 28

## Anatomy of a `for` loop

```python
for var in iterable:
    ...
```

Abstracting some details, a Python "foreach" loop consists of (1) the `for`
keyword, followed by (2) a variable name, followed by (3) the `in` keyword,
followed by (4) an iterable data collection, followed by (5) a colon, and ending
with (6) the body of the loop.

Its flow is:

1. If there are no values in iterable that haven't been visited yet, stop.
2. Assign variable to the next value in iterable.
3. Execute the statements in the body of the loop.
4. Go back to step 1.

## Iterator

An iterator is an object that makes it possible for data collections of your own
design to be used in "foreach" loops. Making your data collection iterable
requires defining two magic methods: `__iter__` and `__next__`. The former
returns an iterator object. The latter returns the next element in the
collection raising the `StopIteration` if there are no more.
