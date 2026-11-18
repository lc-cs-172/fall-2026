# Assignment #10: Calculator

Your aunt Tia needs a calculator for evaluating simple arithmetic expressions.
She appreciates clarity and wants to be able to save values for later retrieval.
She has tasked you to build such an application using functional decomposition,
object-oriented programming, and test-driven development methodology.

## User interaction

Tia wants the calculator to handle two types of entries. On one hand, she wants
to be able to enter an expression. In that case, the calculator outputs the
result of evaluating that expression. On the other hand, she also wants to be
able to save the result of an expression for later retrieval. In that second
case, Tia will enter the name of a variable followed by an equal sign (`=`)
followed by an expression. The calculator will evaluate the expression and store
the result in the named variable. In this case, the calculator will not output
anything.

## Sample interaction

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

## Assumptions

* An entry must be appear entirely on its own line.
* All expressions are valid (e.g., we don't need to check for mismatched
  parentheses).
* An expression is either an operand or a left parenthesis followed by an
  expression followed by an operator followed by another expression followed by
  a right parenthesis.
* Operators, parentheses, and operands are separated by at least one space.
* Operators are addition (`+`), subtraction (`-`), multiplication (`*`), and
  integer division (`\`).
* An uninitialized variable returns the value `0`.
* Integer literals must be non-negative.
* A variable is a non-empty string of lowercase letters only (e.g., 'a', 'aa').
* Once started the calculator never stops (i.e., do not implement something to
  make the applicator stop).

## Decomposition

As discussed in class, you will decompose this problem into the following
components:

* `main.py`: The main driver
* `mem.py`: The memory component implementing a class called `Mem` implementing
  two methods (`lookup` and `update`)
* `scanner.py`: Implement a class called `Scanner`, an instance of which can
  read a line of input and deliver the content of that line one token at a time
  through three methods (`is_assignment`, `is_empty` and `next`)
* `eval.py`: Implement a class called `Eval`, an instance of which can evaluate
  user entries (including assignment with the equal sign) through a method
  called `eval` that takes an instance of `Scanner` and an instance of `Mem` as
  parameter.

### Expression evaluation

The algorithm used to evaluate expression in `eval.py` is the one I described
in class and which is due to E. W. Dijkstra. It is based on two stacks. To
implement this algorithm use either `array-stack.py` or `linked-stack.py` that
we covered in class.

### Memory component

The memory component should use one of the list data structures you have
developed in the previous assignment (i.e., either `array-list.py` or
`linked-list.py`). You are not allowed to use any other data structure to build
the memory component.

## Expectations

* Use object-oriented programming technique
* Develop test cases for all modules except `main.py`
* Use test-driven development (i.e., write the tests first; that will help you
  understand what each component should do)

## What to hand in

* `main.py`
* `mem.py` and `mem_test.py`
* `eval.py` and `eval_test.py`
* `scanner.py` and `scanner_test.py`
* the stack module you used
* the list module you used
