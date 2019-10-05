#!/usr/bin/python3
"""Module to print a square with the character #
    Args:
        size (int): size length of the square
"""


def print_square(size):
    """Function that prints a square with the character #
        Return: printed square
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
