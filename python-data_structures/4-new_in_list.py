#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace element in a list copy without modifying original"""
    new_list = my_list.copy()
    if idx < 0 or idx >= len(new_list):
        return new_list
    new_list[idx] = element
    return new_list
