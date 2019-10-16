#!/usr/bin/python3
"""
This is the "101-add_attribute" module.
The 101-add_attribute module supplies one function, add_attribute.
"""


def add_attribute(obj, name, value):
    """add an atribute to a object only if its posible"""
    if hasattr(obj, name):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
