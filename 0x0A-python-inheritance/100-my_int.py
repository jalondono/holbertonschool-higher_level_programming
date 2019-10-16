#!/usr/bin/python3
"""class"""


class MyInt(int):
    """Constructor"""
    def __init__(self, a):
        self.__a = a

    def __eq__(self, other):
        """overloading method"""
        return int(self) != int(other)

    def __ne__(self, other):
        """overloading method"""
        return int(self) == int(other)
