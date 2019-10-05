#!/usr/bin/python3
"""Module to print My name is <first name> <last name>
    Args:
        first name (str): first string
        last name (str): second string
"""


def say_my_name(first_name, last_name=""):
    """Function that prints My name is <first name> <last name>
        Return: printed name
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print('My name is {:s} {:s}'.format(first_name, last_name))
