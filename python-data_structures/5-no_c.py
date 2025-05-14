#!/usr/bin/python3
def no_c(my_string):
    """Remove all characters c and C from a string"""
    result = []
    for char in my_string:
        if char not in ('c', 'C'):
            result.append(char)
    return "".join(result)
