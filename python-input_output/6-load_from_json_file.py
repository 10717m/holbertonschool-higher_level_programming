#!/usr/bin/python3
"""
Module that defines a function to load an object from a JSON file
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file

    Args:
        filename (str): Path to the JSON file

    Returns:
        Python object decoded from JSON file
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
