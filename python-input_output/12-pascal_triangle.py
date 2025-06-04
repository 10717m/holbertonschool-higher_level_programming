#!/usr/bin/python3
"""
Module that generates Pascal's Triangle of n
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal’s triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        prev_row = triangle[-1]
        # Construct the current row
        row = [1]  # Start with 1
        for j in range(1, len(prev_row)):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # End with 1
        triangle.append(row)

    return triangle
