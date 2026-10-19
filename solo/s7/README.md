# Assignment #7: Buffer Module

With this assignment we are continuing to build modules towards implementing a
simple text editor. This week, we are implementing the module buffering the
entire text being edited. This assignment will also give you additional practice
defining objects.

## Details

You will define one class named *Buffer* in a file called `buffer.py` which has
two attributes:

1. An array (or list) of strings corresponding to the entire text that is held
   in the buffer. Each entry of the array corresponds to exactly one line of the
   text loaded into the buffer. No array entry should contain the newline
   character (`\n`).

2. A Boolean that indicates if the text loaded into the buffer has been edited
   since it was last saved.

The class must also implement the following methods:

1. An initializer that can take an optional initial text as an argument. This
   argument is one big string with newline characters indicating where the line
   breaks are. You will need to find these newline characters to break the
   initial string into distinct lines and strip away the newline characters.

2. A method that returns the content of the buffer as a single string with the
   newline character delimiting each line.

3. A method to insert a character at the given location. If the inserted
   character is a newline, you will need to create a new entry in the array of
   strings.

4. A method to delete a character at the given location. If the cursor is
   located at column 0 of a line, this method should merge the current line with
   the previous one.

5. A method that returns a Boolean indicating if the buffer is dirty (i.e., has
   been modified).

6. A method that marks the buffer clean (to be called whenever the content of
   the buffer has been saved to disk).

## Hints

I am not giving you any templates for this assignment. You will be writing two
files:

* `buffer.py` for the class definition.
* `buffer_test.py` for all the unit tests.

You are responsible for:

* Identifying the author of the files with the variable `__author__` at the top
  of each file.
* Thorough documentation (docstrings for the module, for the class, and for each
  of the methods). The tests may not need much documentation if they are short
  and named appropriately.
* Your tests should check typical operations as well as edge cases (e.g., adding
  a newline character; deleting from column 0; deleting from line 0, column 0,
  etc,).
* Follow typical Python and pytest coding conventions (e.g., class name in
  Pascal case, method names all lowercase with underscores between words,
  constants in screaming uppercase, etc.).

Again there is no main program here. You are just defining a module that will be
a building block for our text editor.

Follow the test-driven development methodology. Write the signatures of all the
needed methods and have them return `None`. Then write the tests. They should
all fail. Then, finally, write enough of the body of each of the methods to make
them pass the tests.

## What to hand in

Upload `buffer.py` and `buffer_test.py` to Google Classroom.
