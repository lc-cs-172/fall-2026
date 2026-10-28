# Assignment #8: Editor

This assignment concludes our project to develop a simple text editor.

## Details

This assignment builds upon the modules written in the previous two assignments.
The modules that remain to be built are `main`, `FileHandler`, and `View`. These
modules rely on particulars of how Python handles input/output (I/O) and can be
rather repetitive. The specifics of Python I/O, in particular, are beyond the
scope of this class. So I'm providing most of the remaining code leaving out
some simple sections for you to fill out.

## Editor's user guide

The arrows move the cursor around the edited text. Typing regular characters and
the "enter" key add the corresponding characters to the text. Pressing "Ctrl-O"
opens a new file. Pressing "Ctrl-S" saves the content of the file. Closing the
window stops the editor.

The files I provide make some assumptions about the naming of modules,
attributes, and methods that you have written in the past two assignments. You
may need to make some adjustments to `view.py` and `main.py` to make them work
with your `cursor.py` and `buffer.py`. If you have followed the "separation of
concern" mantra, you shouldn't have to touch `file_io.py` at all. 

The files I provide implement enough functionality that you can load a text,
save a text, and move the cursor down (only *down*). You will need to add code
to support moving the cursor in the remaining directions and to handle regular
characters that the user can type.

## Steps

1. I'm providing `main.py`, `file_io.py`, and `view.py`.

2. You have developed `cursor.py` and `buffer.py` in the previous two
   assignments.

3. Bring all these files together in a single folder.

4. Run the editor to try to load a text and move the cursor down. You may need
   to edit `view.py` to fix any discrepancy between your implementation and the
   assumptions that `view.py` makes. Don't proceed until you  have completed
   this step. To run the editor you can type `python3 main.py` from the terminal
   or you can click on the "run" button found in the top-right corner of Visual
   Studio Code.

5. Comments with the word "TODO" identifies the four methods that you must fill
   out. The comments also give hints to help you fill the blanks. Fill those
   missing sections and make sure you can load a text file, move the cursor in
   all directions, type new text, delete characters, and save the content.

## What to hand in

Upload to Google Classroom a zip file with all *five* Python files that comprise
the editor (`main.py`, `cursor.py`, `buffer.py`, `file_io.py`, and `view.py`).
It is fine if the zip file includes other miscellaneous files such as
`__pycache__`.
