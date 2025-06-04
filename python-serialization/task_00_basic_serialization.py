#!/usr/bin/env python3
"""
Basic Serialization Module
This module provides functions to serialize a dictionary to a JSON file
and deserialize JSON data from a file back to a dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The name of the file to save the JSON data in.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads and deserializes JSON data from a file to a Python dictionary.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
