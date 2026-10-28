"""Graphical UI module implemented with Tkinter."""

__author__ = 'Alain Kägi, Gemini 3.1 Pro, and YOUR NAME HERE'

import tkinter as tk
from tkinter import filedialog, messagebox
from typing import Callable, Optional
from buffer import Buffer
from file_io import FileHandler

class View:
    """Manages the GUI components, layout, and user input bindings."""

    def __init__(self, root : tk.Tk, buffer, cursor) -> None:
        """Initialize main window widgets and menus.

        Args:
            root: Root Tkinter window handle.
            buffer: Buffer holding text being edited.
            cursor: Cursor position tracker.
        """
        self.root = root
        self.buffer = buffer
        self.cursor = cursor
        self.current_filepath = None

        # Setup Tkinter widgets (Text widget, Scrollbar, Status bar, etc.)
        self._setup_ui()
        self._bind_events()

    def _setup_ui(self) -> None:
        """Initializes GUI widgets and window layout."""
        self.root.title('CS2 Text Editor - Untitled')
        self.root.geometry('600x400')

        # Pack the status bar FIRST at the bottom
        self.status_bar = tk.Label(self.root, text = 'Line 1, Col 0', anchor = 'w')
        self.status_bar.pack(fill = 'x', side = 'bottom')

        # Pack the text area SECOND so it fills remaining space
        self.text_area = tk.Text(
            self.root,
            wrap = 'none',
            undo = False,
            insertbackground = 'black',  # Cursor color
            insertwidth = 2,             # Cursor width in pixels
            insertofftime = 300,         # Blink off time (ms)
            insertontime = 600           # Blink on time (ms)
        )
        self.text_area.pack(side = 'top', fill = 'both', expand = True)

        # Force focus so the cursor is visible immediately upon startup
        self.text_area.focus_set()

    def _bind_events(self) -> None:
        """Binds keyboard shortcuts to view actions."""
        # Bind Ctrl+O and Ctrl+S to open and save a file, respectively
        self.root.bind('<Control-o>', lambda event: self.open_file())
        self.root.bind('<Control-s>', lambda event: self.save_file())

        # Navigation keys
        self.text_area.bind('<Left>', self._handle_left)
        self.text_area.bind('<Right>', self._handle_right)
        self.text_area.bind('<Up>', self._handle_up)
        self.text_area.bind('<Down>', self._handle_down)

        # Editing keys
        self.text_area.bind('<BackSpace>', self._handle_backspace)
        self.text_area.bind('<Return>', self._handle_return)
        self.text_area.bind('<Key>', self._handle_type)

    def set_content(self, text : str) -> None:
        """Update display widget text.

        Args:
            text: Complete text to display.
        """
        self.text_area.delete('1.0', tk.END)
        self.text_area.insert('1.0', text)

    def update_title(self) -> None:
        """Updates the window title, adding an asterisk if there are unsaved
        changes.
        """
        filename = self.current_filepath if self.current_filepath else "Untitled"
        dirty_indicator = '*' if self.buffer.is_dirty() else '-'
        self.root.title(f"CS2 Text Editor {dirty_indicator} {filename}")

    def update_status(self, line : int, column : int) -> None:
        """Update status bar label message.

        Args:
            line: Current line coordinate.
            column: Current column coordinate.
        """
        self.status_bar.config(text = f'Line {line + 1}, Col {column}')

    def open_file(self) -> None:
        """Prompts the user for a file, loads its content into the model and
        view.
        """
        filepath = filedialog.askopenfilename(
            title = 'Open File',
            filetypes = [('Text Files', '*.txt'), ('All Files', '*.*')]
        )

        # If the user cancels the dialog, filepath will be an empty string
        if not filepath:
            return

        try:
            # Read raw text from disk using FileHandler
            text = FileHandler.load_file(filepath)

            # Reset the buffer model with new content
            self.buffer = Buffer(text)  # Re-initialize or reset buffer
            self.buffer.mark_clean()

            # Reset the cursor tracker model back to line 0, col 0
            self.cursor.line = 0
            self.cursor.column = 0

            # Update the View presentation
            self.set_content(text)
            self.update_status(self.cursor.line, self.cursor.column)
            self.move_cursor_visual(self.cursor.line, self.cursor.column)
            self.current_filepath = filepath
            self.root.title(f'CS2 Text Editor - {filepath}')

        except Exception as e:
            messagebox.showerror('Error Opening File', f'Could not open file:\n{e}')

    def save_file(self) -> None:
        """Saves the buffer content to disk.

        Prompts for a destination path if saving a new document for the first time.
        """
        # If no file is associated yet, ask the user where to save
        if not self.current_filepath:
            filepath = filedialog.asksaveasfilename(
                title = 'Save File',
                defaultextension = '.txt',
                filetypes = [('Text Files', '*.txt'), ('All Files', '*.*')]
            )
            if not filepath:
                return  # User cancelled the save dialog
            self.current_filepath = filepath

        try:
            # Get string content from buffer model
            content = self.buffer.get_text()

            # Write content to disk via FileHandler
            FileHandler.save_file(self.current_filepath, content)

            # Update dirty state and window title
            self.buffer.mark_clean()
            self.root.title(f'CS2 Text Editor - {self.current_filepath}')

        except Exception as e:
            messagebox.showerror('Error Saving File', f'Could not save file:\n{e}')

    def move_cursor_visual(self, line : int, column : int) -> None:
        """Synchronizes Tkinter's visual insert cursor with the Cursor model
        coordinates.

        Args:
            line: 0-based line index from Cursor
            column: 0-based column index from Cursor
        """
        # Tkinter lines are 1-based, but columns are 0-based
        tk_index = f'{line + 1}.{column}'

        # Move Tkinter's visual insertion caret
        self.text_area.mark_set('insert', tk_index)

        # Ensure the visual cursor stays in view if the document scrolls
        self.text_area.see('insert')

        # Keep the status bar in sync
        self.update_status(line, column)

    def _handle_left(self, event) -> str:
        # TODO: Replace this comment with *two* lines of code based on the
        # behavior of `_handle_down`.
        return 'break'  # Prevent Tkinter's native cursor move

    def _handle_right(self, event) -> str:
        # TODO: Replace this comment with *two* lines of code based on the
        # behavior of `_handle_down`.
        return 'break'

    def _handle_up(self, event) -> str:
        # TODO: Replace this comment with *five* lines of code (not including
        # any comments) based on the behavior of `_handle_down`.
        return 'break'

    def _handle_down(self, event) -> str:
        self.cursor.move_down(total_lines = len(self.buffer._lines))
        # Clamp column if moving to a shorter line
        target_line_len = len(self.buffer._lines[self.cursor.line])
        if self.cursor.column > target_line_len:
            self.cursor.column = target_line_len
        self.move_cursor_visual(self.cursor.line, self.cursor.column)
        return 'break'

    def _handle_type(self, event) -> str | None:
        # Ignore control keys, modifier keys, and special event keys
        if len(event.char) == 1 and ord(event.char) >= 32:
            # TODO: Replace this comment with *five* lines of code based on the
            # behavior of `_handle_return`.
            return 'break'
        return None  # Let shortcut key combinations (like Ctrl+O) pass through

    def _handle_return(self, event) -> str:
        self.buffer.insert_char('\n', self.cursor.line, self.cursor.column)
        self.cursor.line += 1
        self.cursor.column = 0
        self.set_content(self.buffer.get_text())
        self.move_cursor_visual(self.cursor.line, self.cursor.column)
        self.update_title()
        return 'break'

    def _handle_backspace(self, event) -> str:
        if self.cursor.column > 0:
            # Deleting character within same line
            self.buffer.delete_char(self.cursor.line, self.cursor.column)
            self.cursor.column -= 1
        elif self.cursor.line > 0:
            # Backspacing at start of line: merge with line above
            prev_line_len = len(self.buffer._lines[self.cursor.line - 1])
            self.buffer.delete_char(self.cursor.line, self.cursor.column)
            self.cursor.line -= 1
            self.cursor.column = prev_line_len

        self.set_content(self.buffer.get_text())
        self.move_cursor_visual(self.cursor.line, self.cursor.column)
        self.update_title()
        return 'break'
