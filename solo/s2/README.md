# Assignment #2: ATM: Functional Decomposition

## Purpose

This assignment is an exercise in decomposing a problem into simpler and simpler
functions.

## Readings

* "Decomposition (computer science)," Wikipedia, last modified October, 25 2025,
  [https://en.wikipedia.org/wiki/Decomposition_(computer_science)](https://en.wikipedia.org/wiki/Decomposition_(computer_science))

* "Type signature," Wikipedia, June 27, 2026,
  [https://en.wikipedia.org/wiki/Type_signature](https://en.wikipedia.org/wiki/Type_signature)

* "Docstrings," Pythonorama, last modified September 16, 2023,
  [https://github.com/alainkaegi/pythonorama/blob/main/style/documentation.md#docstrings](https://github.com/alainkaegi/pythonorama/blob/main/style/documentation.md#docstrings)

## What you will be able to do

1. Break a complex problem into small, manageable functions.

2. Assign each of the identified, small functions a type signature.

3. Describe the purpose of each of the identified small functions with a
   docstring.

## Core concepts

* **Application Programming Interface (API)**. An API is a set of rules and
  protocols that describe how a software library is to be used. Think back about
  the graphics library that you might have used in your first computer science
  class. That library came with a list of functions (e.g., initialization,
  draw a line, draw a circle) and conventions dictating how to use them (e.g.,
  a drawing canvas must first be created and initialized before any object can
  be drawn, drawing a circle requires specifying a location on the canvas).

* **Functional decomposition**. Functional decomposition is the process of
  breaking a problem into small functions.

* **Type signature**. Specifically for a function, its type signature includes
  the name of the function, the number of arguments it takes, the name of those
  arguments, the type of these arguments, and the type of the value returned.
  Unfortunately, Python makes it difficult to specify the types of the arguments
  and the return value. But we will learn to live with those limitations.

* **Documentation**. It is key to document what a function does, particularly if
  it is part of a larger API. A lot can already be achieved by choosing good
  names for its name and its arguments, and by choosing good types for its
  arguments and the return value.

## Assignment

Your goal is to design a text-based ATM program that handles user PIN
authentication, balance inquiries, cash deposits, and cash withdrawals. For
a sample interaction with the program see the example at the assignment of this
text.

Your submission, in a file called `atm.py`, is to list all the functions
required to implement the ATM program. Each of these functions must come with
its name, the names of its arguments, and a docstring. The docstring must come
with a succinct description of what the associated function does and at least
two examples of how the function is to be used. Think about all the details
that were given when solving the CodingBat exercises.

This is *not* a programming exercise in the normal sense. We are writing a
Python file with legal syntax for defining functions using the `def` keyword.
But these functions will be empty except for a `return` statement returning a
bogus value of a type that is appropriate for the return type of those
functions. If the function is supposed to return an integer, return the value
zero, if the function is supposed to return a string, return the empty string.
The goal for these functions to be runnable (e.g., Python will not complain
about a syntax error) and guaranteed to return the wrong value in the general
case.

Below is an example of what I am looking for:

```python
def find_account_index(account_ids, target_id):
    """Searches for `target_id` in the array `account_ids`. Returns the index if
    found, or -1.

    find_account_index([100, 101, 102], 100) -> 0
    find_account_index([100, 101, 102], 102) -> 2
    find_account_index([100, 101, 102], 0) -> -1
    """
    return -1
```

## Possible decomposition

I suggest the following decomposition. But this particular decomposition is only
a suggestion.

* `find_account_index`
* `authenticate_user`
* `check_balance`
* `deposit_cash`
* `withdraw_cash`
* `process_user_session`
* `run_atm_system`

I do not expect a perfect answer. Functional decomposition is an iterative
process. It is not rare that early choices are reconsidered as we progress
towards a full implementation. In other words, you do not need a flawless
submission to receive full credits.

## Grading

Rubric        | Description                                      | Scale
-|-|-
Decomposition | A full decomposition is provided                 | 0-3
Python        | Python can load submission w/o errors            | 0-3
Naming        | Names of functions and parameters are meaningful | 0-3
Documentation | Docstrings are provided                          | 0-3

Points | Description
-|-
3      | Full submission with perhaps a small detail or two missing
2      | Full submission with several minor details missing
1      | A major detail missing
0      | No submission

## What to hand in

Write your functions in a file called `atm.py` and upload it to Google
Classroom.

## Sample interaction

As a reminder, here is a sample interaction with the planned program:

```
====================================
      WELCOME TO CS BANK ATM        
====================================

--- Main Login Screen ---
Enter Account ID (or -1 to power down): 101
Enter PIN: 1234

[SUCCESS] Login successful! Welcome Account #101.

--- ATM Menu ---
1. Check Balance
2. Deposit Cash
3. Withdraw Cash
4. Log Out
Select an option (1-4): 2
Enter deposit amount: $40
[SUCCESS] Deposited $40.0. New balance: $290.0

--- ATM Menu ---
1. Check Balance
2. Deposit Cash
3. Withdraw Cash
4. Log Out
Select an option (1-4): 4

Logging out... Thank you for using CS Bank!

--- Main Login Screen ---
Enter Account ID (or -1 to power down): -1
Shutting down ATM system. Goodbye!
```
