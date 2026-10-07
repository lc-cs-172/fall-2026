# Note 15

In the ATM assignment, many of you had a function that might have looked as
follows:

```python
def deposit(balances : list[float], index : int, amount : float):
    """Deposit `amount` of dollars in the array of `balances` belonging to
    account at index `index` of the array.
    """
    balances[index] += amount
```

In retrospect, it seems silly to pass as an argument to `deposit` the balances
of *all* accounts when this function only cares about one *particular* account.

Instead, wouldn't it be more logical to group all data belonging to a particular
account holder in one place:

* Perhaps as a list: [‹account number›, ‹pin›, ‹balance›]
* Or perhaps as a tuple: (‹account number›, ‹pin›, ‹balance›)

Suppose then that variable `client_sam` holds such a list for an account holder
named Sam. To access Sam's balance, we would then write

```python
client_sam[2]        # Balance is held at index 2
```

Not bad, but really, wouldn't it be much clearer and cleaner if we could write

```python
client_sam.balance  # No need for a comment here
```

to access Sam's information?

That's what object-oriented programming is all about. We will learn how to
organize data in classes and define behaviors on this data.
