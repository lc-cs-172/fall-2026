# Note 10

## Import statement

Many programming languages provide the ability for a program, file, or module,
call it P, to *import* a library, another file or module, call it L. What it
typically means is that named items defined in L are brought into the scope of
P. In other words, P, after importing L, can refer to items defined in L by
their names. For instance, if a Python program needs to use the `sine` function
or refer to `pi` (the irrational number) the program can import the math library

```python
import math
```

and then refer to these items with a prefix

```python
math.sine(math.pi)
```

### Import syntaxes

Python supports different import styles. The table below summarizes some of the
most important styles.

Style     | Syntax                        | Example                     | How to refer to an item
-|-|-|-
Standard  | `import <module>`             | `import math`               | Requires module prefix: `math.pi`
Alias     | `import <module> as <alias>`  | `import numpy as np`        | Requires alias prefix: `np.array([1, 2])`
Specific  | `from <module> import <item>` | `from math import pi, sine` | Direct: `sine(pi)`
Wild card | `from <module> import *`      | `from math import *`        | Direct: `sine(pi)`

## `main`

The equivalent of the following C program that you could have written in CS1

```c
#include <stdio.h>

int main() {
    printf("hello, world!\n");
}
```

is canonically written as follows in Python

```python
def main():
    print('hello, world!')

if __name__ == '__main__':
    main()
```

## `input`

To get input from a user, a Python program can use the function called `input`.
From its documentation:

> `def input(prompt='') -> str`
>
> Read a string from standard input. The trailing newline is stripped.
>
> The prompt string, if given, is printed to standard output without a trailing
> newline before reading input.

Note that `input` returns a string (indicated by `-> str` that follows the
function signature). If you an integer value you must first convert the inputed
string. Here is a simple example:

```python
user_id = int(input('Enter account id: '))
```
