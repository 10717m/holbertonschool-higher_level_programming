#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase."""
    for char in str:
        diff = 32 if 'a' <= char <= 'z' else 0
        print("{:c}".format(ord(char) - diff), end="")
    print()
