#!/usr/bin/python3

"""
This is the "4-print_square" module.
The 4-print_square module supplies one function, print_square(size).
"""


def print_square(size):
    """print_square function
        Args:  size is the size length of the square
        Prints:  a square """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("must be an integer")
    if size == 0:
        pass
    size = int(size)
    for i in range(0, size):
        for j in range(0, size):
            print("#", end='')
        print()
