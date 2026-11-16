# Note 30

## More on references

Recall the Python mantra:

> Everything is a reference

What that means is that if you store a value in a variable, function parameter,
or class attribute what you are really storing is a reference to that value.

### Parameter passing strategy

In particular, in Python, all values passed as parameters to functions (and
methods) are passed through a reference:

```python
def f(arg):
    print(id(arg))

num = 17
print(id(num))
f(num)          # the last two lines print the same number (the id of `num`)
```

### Side effects

Because values are passed to functions through references, functions may modify
the content of the references such that the caller will see these modifications.
We say that such functions have a **side effect**.

Observe the following sequence of statements:

```python
def f(a):
    a.append(17)

lst = [1, 2, 3]
print(id(lst))
f(lst)
print(lst)      # prints `[1, 2, 3, 17]`
print(id(lst))  # but the id remains the same as before
```
