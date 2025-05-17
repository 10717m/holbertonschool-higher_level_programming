#!/usr/bin/python3
"""This module provides a function for text indentation."""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?', and ':'.

    Args:
        text: The text to print (must be a string)

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            # Skip any spaces immediately after the punctuation
            while i + 1 < len(text) and text[i+1] == ' ':
                i += 1
        i += 1
