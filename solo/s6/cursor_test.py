"""Unit tests for the Cursor module."""

__author__ = 'Alain Kägi and Gemini 3.1 Pro'

from cursor import Cursor

def test_cursor_initialization_default():
    """Cursor should start at line 0, column 0 by default."""
    cursor = Cursor()
    assert cursor.line == 0
    assert cursor.column == 0

def test_cursor_initialization_custom():
    """Cursor should start at the specified position."""
    cursor = Cursor(4, 2)
    assert cursor.line == 4
    assert cursor.column == 2

def test_cursor_get_position():
    """Get position should return the specified position."""
    cursor = Cursor(2, 7)
    assert cursor.get_position() == (2, 7)

def test_move_right_within_bounds():
    """Moving right increments the column."""
    cursor = Cursor(line = 0, column = 0)
    cursor.move_right(line_length = 5)
    assert cursor.get_position() == (0, 1)

def test_move_right_at_boundary():
    """Cursor should not move right past the end of the line."""
    cursor = Cursor(line = 0, column = 5)
    cursor.move_right(line_length = 5)
    assert cursor.get_position() == (0, 5)

def test_move_left_within_bounds():
    """Moving left decrements the column."""
    cursor = Cursor(line = 0, column = 3)
    cursor.move_left()
    assert cursor.get_position() == (0, 2)

def test_move_left_at_boundary():
    """Cursor should not move left past column 0."""
    cursor = Cursor(line = 0, column = 0)
    cursor.move_left()
    assert cursor.get_position() == (0, 0)

def test_move_down_within_bounds():
    """Moving down increments the line."""
    cursor = Cursor(line = 0, column = 0)
    cursor.move_down(total_lines = 3)
    assert cursor.get_position() == (1, 0)

def test_move_down_at_boundary():
    """Cursor should not move down past the last line (total_lines - 1)."""
    cursor = Cursor(line = 2, column = 0)
    cursor.move_down(total_lines = 3)
    assert cursor.get_position() == (2, 0)

def test_move_up_within_bounds():
    """Moving up decrements the line."""
    cursor = Cursor(line = 2, column = 0)
    cursor.move_up()
    assert cursor.get_position() == (1, 0)

def test_move_up_at_boundary():
    """Cursor should not move up past line 0."""
    cursor = Cursor(line = 0, column = 0)
    cursor.move_up()
    assert cursor.get_position() == (0, 0)
