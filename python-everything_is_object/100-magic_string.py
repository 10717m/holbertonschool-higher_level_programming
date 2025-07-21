#!/usr/bin/python3
def magic_string():
    setattr(magic_string, "num", getattr(magic_string, "num", -1) + 1)
    return "BestSchool, " * magic_string.num + "BestSchool"
