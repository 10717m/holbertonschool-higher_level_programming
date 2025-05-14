#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns tuple with length and first character"""
    if not sentence:
        return (0, None)
    return (len(sentence), sentence[0])
