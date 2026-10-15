"""Cursor tracking module for managing caret position and boundaries."""

__author__ = 'YOUR NAME HERE'

from typing import Tuple

class Cursor:
    """Tracks and bounds cursor position within a line-and-column coordinate
    space.

    Attributes:

        line : int

            Current 0-indexed line position

        column : int

            Current 0-indexed column position
    """

    def __init__(self, line : int = 0, column : int = 0) -> None:
        """Initialize cursor at a specific coordinate.

        Args:
            line: Initial 0-indexed line index
            column: Initial 0-indexed column index
        """
        return

    def move_left(self) -> None:
        """Move cursor one column left, clamping to column 0."""
        pass

    def move_right(self, line_length : int) -> None:
        """Move cursor one column right, bounded by line length.

        Args:
            line_length: Length of current line to prevent moving past end
        """
        pass

    def move_up(self) -> None:
        """Move cursor one line up, clamping to line 0."""
        pass

    def move_down(self, total_lines : int) -> None:
        """Move cursor one line down, bounded by total line count.

        Args:
            total_lines: Total number of lines in current buffer
        """
        pass

    def get_position(self) -> Tuple[int, int]:
        """Get current (line, column) pair.

        Returns:
            Pair containing (line, column)
        """
        pass
