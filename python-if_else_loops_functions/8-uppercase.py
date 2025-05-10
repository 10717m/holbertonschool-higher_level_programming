#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase."""
    for char in str:
        print("{:c}".format(ord(char) - 32 if 'a' <= char <= 'z' else ord(char)), end="")
    print()
