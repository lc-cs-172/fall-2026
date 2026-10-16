# Note 18

## Optional arguments

Python support optional arguments to functions (or methods). An argument is made
optional if it is given a default value with the assignment operator. Optional
arguments must follow non-optional ones.

Below is a function definition illustrating use of this feature.

```python
def str_to_int(digits : str, base : int = 10):
    """Convert a string of digits to an integer assuming the given base. If the
    base is not explicitly specified, it default to base 10. The value returned
    is undefined for non-sensical arguments.
    """
    v = 0
    for d in digits:
        v = base*v + int(d)
    return v
```

This function can be called in the following ways.

```python
str_to_int('1010', 10)  # Explicitly specify the base
str_to_int('1010')      # Use the default value for the base (10)
str_to_int('1010', 2)   # Use an alternate base
```

Optional arguments can be used for any functions including those defined inside
classes (when they are often referred to as methods).
