# Note 29

## Calculator

The goal of the next project is to develop a calculator that has the following
capabilities:

* Evaluate simple arithmetic expressions
* Support four operations: integer addition, subtraction, multiplication, and
  division
* Support two types of operands: integer literals and variables
* Store generated values into variables

For simplicity, we will make the following assumptions:

* All expressions are valid (e.g., we don't need to check for mismatched
  parentheses).
* An expression is either an operand or a left parenthesis followed by an
  expression followed by an operator followed by another expression followed by
  a right parenthesis.
* Operators, parentheses, and operands are separated by at least one space.
* An uninitialized variable returns the value `0`.

Here is an example interaction:

```
>>> 5
5
>>> ( 5 + 48 )
53
>>> ( 5 + ( 48 / 3 ) )
21
>>> ( ( 5 + 48 ) / 3 )
17
>>> a = ( ( 5 + 48 ) / 3 )
>>> a
17
>>> ( a + a )
34
```

## Decomposition

How should we decompose this problem into smaller components?
