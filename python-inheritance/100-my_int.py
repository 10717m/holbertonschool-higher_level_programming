#!/usr/bin/python3
"""MyInt class that inherits from int with inverted == and != operators."""

class MyInt(int):
    """MyInt class inherits from int with inverted equality operators."""

    def __eq__(self, other):
        return int(self) != other

    def __ne__(self, other):
        return int(self) == other
