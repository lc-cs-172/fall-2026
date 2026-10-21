# Node 21

## `__str__` vs. `__repr__`

Both of these magic methods return a string representation of an object.
[Alex Martelli](https://stackoverflow.com/users/95810/alex-martelli) summarizes
the difference between these two methods as follows:

* The goal for `__repr__` is to be unambiguous
* The goal for `__str__` is be readable

For many classes, you will usually want both methods to do the same thing. Since
by default `__str__` just calls `__repr__`, if you only want to define one,
define `__repr__`.

`str` and `repr` are wrappers for `__str__` and `__repr__`.

## Attributes naming convention

A Python naming convention exists whereby attributes or methods that should not
be used by client code have a name starting with a single underscore (`_`).
