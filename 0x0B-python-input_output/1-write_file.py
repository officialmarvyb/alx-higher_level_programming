#!/usr/bin/python3
"""
Function that that writes a string
to a text file (UTF8) and returns
the number of characters written.
"""


def write_file(filename="", text=""):
    """Return the number of lines in a text file."""
    lines = 0
    with open(filename) as f:
        for line in f:
            lines += 1
    return lines
