#!/usr/bin/python3

"""
This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer().
"""


def add_integer(a, b=98):
    """
    This is the "0-add_integer" module.
    The 0-add_integer module supplies one function, add_integer().
    """
    if type(a) is float or type(a) is int:
        c = int(a)
    else:
        raise TypeError("a must be an integer")
    if type(b) is float or type(b) is int:
        d = int(b)
    else:
        raise TypeError("b must be an integer")
    return c + d
