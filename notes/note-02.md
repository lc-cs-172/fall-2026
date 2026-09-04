# Note 02

## Type signature

From Wikipedia:

> [T]ype signature or type annotation defines the inputs and outputs of a
> function (or method). A type signature includes the number, types, and order
> of the function's arguments.

## Docstring

From (PEP 257)[https://peps.python.org/pep-0257/] - Docstring Conventions:

> A docstring is a string literal that occurs as the first statement in a
> module, function, class, or method definition. Such a docstring becomes the
> `__doc__` special attribute of that object.

> All modules should normally have docstrings, and all functions and classes
> exported by a module should also have docstrings.

A docstring for a function should be something like:

```python
def function(a, b):
    """Do X and return a list."""
