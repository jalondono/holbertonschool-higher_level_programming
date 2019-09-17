#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t = (0, 0)
    sizea = len(tuple_a)
    sizeb = len(tuple_b)
    if sizea == 1:
        a = tuple_a[0]
        c = 0
    elif sizea == 0:
        a = 0
        c = 0
    else:
        a = tuple_a[0]
        c = tuple_a[1]
    if sizeb == 1:
        b = tuple_b[0]
        d = 0
    elif sizeb == 0:
        b = 0
        d = 0
    else:
        b = tuple_b[0]
        d = tuple_b[1]
    t = ((a + b), (c + d))
    return t
