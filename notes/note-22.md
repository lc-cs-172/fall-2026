# Note 22

## Puzzle

What is the value returned by evaluating the Python expression `3 * 0.1 == 0.3'?

## References

In Python *everything* is a reference.

According to
[wikipedia](https://en.wikipedia.org/wiki/Reference_(computer_science)),
*reference* is

> a value that enables a program to indirectly access a particular datum.

### Immutable types

When say that a type is *immutable* when the following condition is true when a
new value of that type is created:

> The new value is bound to a *fixed* reference for the rest of its lifetime.

Types                  | Immutable?
-|-
`int`, `float`, `bool` | Yes
`str`                  | Yes
`tuple`                | Yes
`list`, `set`, `dict`  | No

### Pitfalls

The following functions do not necessarily do what you expect.

```python
class Complex:
    def __init__(self, real0 : float, imag0 : float) -> None:
        self.real = real0
        self.imag = imag0

    def __repr__(self) -> str:
        """Return a string representation of this instance of Complex."""
        return str(self.real) + ' + ' + str(self.imag) + 'i'

    def __add__(self, other):
        """Return the sum of self and other (danger!)."""
        self.real += other.real
        self.imag += other.imag
        return self

def create_matrix(n : int, m : int) -> List[List[float]]:
    """Returns an n x m matrix filled with 0.0."""
    row = [0.0]*m
    mat = []
    for i in range(n):
        mat.append(row)
    return mat
```
