# Node 24

## Lambda functions

Lambda functions are nameless functions. These functions are introduced by the
keyword `lambda` followed by a list of comma-separated formal arguments,
followed by a colon (`:`) followed by an expression.

```
lambda x, y, z, ... : expression
```

Here is a lambda function that returns the square of its argument:

```python
lambda x : x**2
```

Here is the same lambda function applied to argument 10:

```python
(lambda x : x**2)(10)
```

Such function definitions are useful when you only need them for a single use.

The name of this abstraction comes from the lambda calculus, a mathematical
formalization created to reason about what it means to be computable.
