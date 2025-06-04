#!/usr/bin/python3
"""
Module that inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line
    containing a specific string.

    Args:
        filename (str): Name of the file to read/write.
        search_string (str): String to search for in each line.
        new_string (str): String to insert after each matched line.
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
