# Assignment #4: ATM: Implementation

## Purpose

This assignment consists of the final stage in developing our application. We
finally get to write the complete program.

## Readings

* "Your first program," Pythonorama, last modified July 6, 2025,
  [https://github.com/alainkaegi/pythonorama/blob/main/control_structures/your_first_program.md](https://github.com/alainkaegi/pythonorama/blob/main/control_structures/your_first_program.md)

* "Test-driven development," Wikipedia, last modified August 9, 2026,
  [https://en.wikipedia.org/wiki/Test-driven_development](https://en.wikipedia.org/wiki/Test-driven_development)

* "Visual Studio Code," Pythonorama, last modified July 6, 2025,
  [https://github.com/alainkaegi/pythonorama/blob/main/development_tools/vs_code.md](https://github.com/alainkaegi/pythonorama/blob/main/development_tools/vs_code.md)

* "Documentation," Pythonorama, last modified August 20, 2024,
  [https://github.com/alainkaegi/pythonorama/blob/main/style/documentation.md](https://github.com/alainkaegi/pythonorama/blob/main/style/documentation.md)

* "Names," Pythonorama, last modified October 6, 2025,
  [https://github.com/alainkaegi/pythonorama/blob/main/style/names.md](https://github.com/alainkaegi/pythonorama/blob/main/style/names.md)

* "PEP 257 – Docstring Conventions," Python Enhanced Proposals, created on May,
  29, 2001,
  [https://peps.python.org/pep-0257/](https://peps.python.org/pep-0257/)

## What you will be able to do

1. Develop the minimal amount of code to make a function's implementation pass
   the unit tests.

2. Describe the Test-driven Development (TDD) strategy and list the specific
   steps mandated by this approach.

3. Explain how ab Integrated Development Environment (IDE) such as Visual Studio
   Code supports TDD.

4. Write code following typical Python conventions including use of good names
   for functions and variables, and proper documentation using docstrings.

## Core concepts

* **Test-driven development**. Test-driven development is a software development
  technique that involves (1) identifying a feature, (2) for that feature, write
  a unit test that fails, and (3) write just enough code to make the unit test
  pass.

* **Documentation**. Code is not just for the computer. It's also read by other
  people who need to understand how it works, debug it, or add new features.
  Unless it is thoroughly documented, even your own code will be completely
  mysterious to you if you haven't looked at it in a few months. In particular,
  Python developed a convention around the concept of docstrings.

* **Naming**. Programmers are constantly called upon to name variables,
  functions/methods, classes, and other things. Choosing names carefully can
  vastly improve the legibility (and therefore maintainability) of code.

## Assignment

By this stage you should have a list of functions (or
features, the goal of assignment [s2](../s2/README.md)) and a set of unit tests
(the goal of assignment [s3](../s3/README.md).

This assignment consists of two steps:

1. Given the list of functions for which you have a unit test, write the
   minimal amount of code for all these function to make their associated unit
   tests pass.

2. Recall that not all functions are necessarily amenable to unit testing. This
   is the case for those "driver," high-level functions such as
   `process_user_session` and `run_atm_system` identified in assignment
   [s2](../s2/README.md). Write these functions to complete the ATM application.

## Grading

Rubric        | Description                                  | Scale
-|-|-
Functionality | The program implements the required features | 0-3
Style         | The program adheres to Python conventions    | 0-3
Comments      | The program is sufficiently documented       | 0-3

Points | Description
-|-
3      | Full submission with perhaps a small detail or two missing
2      | Full submission with several minor details missing
1      | A major detail missing
0      | No submission

## What to hand in

Your update `atm.py` and upload it to Google Classroom. If you have made changes
to your unit tests, upload `atm_test.py` as well.
