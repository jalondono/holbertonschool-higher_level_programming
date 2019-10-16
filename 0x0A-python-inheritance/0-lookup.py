#!/usr/bin/python3
"""class"""


def lookup(obj):
    """"
    get list of available attributes and methods of an object:
    :return:
        - return list of  class used by this class
    """
    return dir(obj)
