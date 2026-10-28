"""File I/O utility module for reading and writing document files."""

__author__ = 'Alain Kägi and Gemini 3.1 Pro'

from typing import Optional

class FileHandler:
    """Handles loading and saving text files safely."""

    @staticmethod
    def load_file(filepath: str) -> Optional[str]:
        """Read content from a text file.

        Args:
            filepath: Path to the file to read.

        Returns:
            File content as a string, or None if read operation failed.
        """
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()

    @staticmethod
    def save_file(filepath: str, content: str) -> bool:
        """Write string content to a text file.

        Args:
            filepath: Target file path.
            content: Text string to write.

        Returns:
            True if save succeeded, False otherwise.
        """
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
