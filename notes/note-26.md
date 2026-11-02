# Note 26

## Array-based structures

Python uses lists as its default linear structures. Lower-level languages like C
instead use primitive arrays. Key differences include:

* An array's size is set when it is created; it cannot change.

* Python list features, such as slicing and methods like count, are not directly
  available for primitive arrays.

This note helps you understand how to build various linear structures out of
Python lists masquerading as primitive arrays. While you would normally just use
Python's lists, sets, and so on, this is worthy of study because:

* Understanding the underlying data structures and algorithms clarifies the
  performance of Python's fancier data structures. For example, it will help you
  understand why adding something to the beginning of a long list is much more
  expensive than adding something to the end.

* You may someday be working in a language that uses primitive arrays.

* You may need to build a data structure that is slightly different from what
  Python provides.

## Simulating primitive arrays

To use Python's convenient list syntax while limiting yourself to what a
primitive array can do, use only the following features:

Operation                       | Syntax
-|-
Allocate an array of length $n$ | `a = [None] * n`
Access element $i$              | `a[i]`
Set element $i$ to $x$          | `a[i] = x`
Get the length of an array      | `len(a)`

All of these operations clearly take constant time except allocation which, as
defined above, takes linear time.  Note that in C you can allocate an array in
constant time, but its content is not initialized, creating a security risk.
