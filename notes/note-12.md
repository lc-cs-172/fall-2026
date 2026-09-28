# Note 12

## Puzzle

Write a function that computes the following product:

n × (n−1) × (n−2) × ... × 2 × 1

## Recursion

> To understand recursion, you must first understand recursion

![I don't often repeat myself, but when I do I use
recursion](recursion.png)

(From https://medium.com/@leog7one/to-understand-recursion-you-must-first-understand-recursion-recursion-explained-c574245cf788)

### Factorial

Product:

n! = n × (n−1) × (n−2) × ... × 2 × 1

Recurrence relation:

n! = 1 if n = 0
<br/>
n! = (n − 1)! × n if n > 0

Iterative:

```python
def factorial(n : int) -> int:
    fact = 1
    i = 1
    while i <= n:
        fact *= i
        i += 1
    return fact
```

Recursive:

```python
def factorial(n : int) -> int:
    if n == 0:
        return 1
    return factorial(n - 1) * n
```

## Type signature

From [Wikipedia](https://en.wikipedia.org/wiki/Type_signature):

> A type signature or type annotation defines the inputs and outputs of a
> function. A type signature includes the number, types, and order of the
> function's arguments.

An example from
[python.org](https://typing.python.org/en/latest/spec/annotations.html):

```python
def greeting(name: str) -> str:
    return 'Hello ' + name
```

This states that the expected type of the name argument is `str`. Analogically,
the expected return type is `str`.
