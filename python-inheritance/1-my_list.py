#!/usr/bin/python3
"""
Module 1-my_list
Contains class MyList that inherits from list
with a public instance method print_sorted()
"""


class MyList(list):
    """
    A class that inherits from list with additional functionality

    Methods:
        print_sorted(): prints the list in ascending sorted order
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order

        Assumes all elements are of type int
        Doesn't modify the original list
        """
        print(sorted(self))
