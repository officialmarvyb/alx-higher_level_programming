#!/usr/bin/python3
"""
 Append to a file module
"""


def write_file(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        if f.write(text):
            return len(text)
