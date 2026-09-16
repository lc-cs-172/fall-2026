# Assignment #3: ATM: Unit Testing

## Purpose

This assignment is an exercise in writing unit tests for those functions defined
in the previous assignment that return a value or alter the content of an array.

## Readings

* "Testing," Pythonorama, last modified January 20, 2025,
  [https://github.com/alainkaegi/pythonorama/blob/main/software_development/testing.md](https://github.com/alainkaegi/pythonorama/blob/main/software_development/testing.md)

* "Test-driven development," Wikipedia, last modified August 9, 2026,
  [https://en.wikipedia.org/wiki/Test-driven_development](https://en.wikipedia.org/wiki/Test-driven_development)

* "Unit testing," Wikipedia, August 20, 2026,
  [https://en.wikipedia.org/wiki/Unit_testing](https://en.wikipedia.org/wiki/Unit_testing)

## What you will be able to do

1. Write a test at the level of an individual function to validate its expected
   behavior.

2. Describe the various conventions relied upon by `pytest`, a framework for
   automating unit tests in Python.

3. Understand how to configure and to run unit tests from an integrated
   development environment such as Visual Studio Code.

## Core concepts

* **Unit testing**. Unit testing tests individual parts of the program (e.g.,
  methods). Unit testing has two big advantages over other types of testing.
  First, it can happen a lot earlier, before the entire system has been built.
  This is important because it gives you a chance to fix one bug before
  introducing the next one. Second, if a bug is found, unit testing gives a
  strong indication of where it is.

* **Test-driven development**. Test-driven development is a software development
  technique that involves (1) identifying a feature, (2) for that feature, write
  a unit test that fails, and (3) write just enough code to make the unit test
  pass.

## Assignment

For each of those functions identified in the previous assignment, that returns
a value or alter the content of an array, write a unit test that fails.

Of the decomposition I proposed in the previous assignment, I suggest that one
writes one or more unit tests for the following functions:

* `find_account_index`
* `authenticate_user`
* `check_balance`
* `deposit_cash`
* `withdraw_cash`

I want to stress again that you are *not* to write any actual code in the
functions in `atm.py` (possibly besides a return statement to make the tests
fail).

## Grading

Rubric        | Description                                | Scale
-|-|-
Unit tests    | A full set of tests is provided            | 0-3
Coverage      | Provide a decent coverage of failure modes | 0-3
Python        | Python runs all tests and they all fail    | 0-3

Points | Description
-|-
3      | Full submission with perhaps a small detail or two missing
2      | Full submission with several minor details missing
1      | A major detail missing
0      | No submission

## What to hand in

Write your unit tests in a file called `atm_test.py` and upload it to Google
Classroom.
