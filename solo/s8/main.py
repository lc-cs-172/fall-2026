"""Application entry point and controller glue logic."""

__author__ = 'Alain Kägi and Gemini 3.1 Pro'

import tkinter as tk
from buffer import Buffer
from cursor import Cursor
from file_io import FileHandler
from view import View

def main() -> None:
    """Initialize model components and start Tkinter event loop."""
    root = tk.Tk()
    buffer = Buffer()
    cursor = Cursor()
    view = View(root, buffer, cursor)

    root.mainloop()

if __name__ == "__main__":
    main()
