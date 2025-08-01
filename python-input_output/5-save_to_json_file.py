#!/usr/bin/python3
"""
Module that defines a function to save object to file using JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation

    Args:
        my_obj: Object to be serialized
        filename (str): Name of the file to write to
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
