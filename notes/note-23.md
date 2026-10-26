# Note 23

## Data collection building blocks

In this class, in terms of data structures, we will focus on linear data
collections. We have already seen a few of these collections: arrays, lists, and
tuples. In the course of this semester, we will look at few more: sets, stacks,
and queues.

This note focuses on how one might build any such a collection. There are at
least two approaches:

1. Use a primitive array (the kind that C supports, distinct from Python's list)
2. Build upon references

The building block for the latter is as follows:

```python
from __future__ import annotations
from typing import Any

class Node:
    """A building block for constructing some data collection."""
    def __init__(self, item : Any, next : Node):
        self.item = item  # any data
        self.next = next  # a reference to another Node
```

Now we can link two objects together as follows:

```
o1 = Object()        # Create some object
n  = Node(o1, None)  # Wrap it in a Node
o2 = Object()        # Create another object
n  = Node(02, n)     # Wrap it in a Node and link it to the preceding one
```
