#!/usr/bin/python3
def add_integer(a, b=98):
    if type(a) is float or type(a) is int:
        c = int(a)
    else:
        raise TypeError("a must be an integer")
    if type(b) is float or type(b) is int:
        d = int(b)
    else:
        raise TypeError("b must be an integer")
    return c + d
