#!/usr/bin/python3


"""
say_my_name module:
contains a function that prints "My name is"
"""


def say_my_name(first_name, last_name=""):
    """
    prints "My name is"
    Parameters
    ----------
    first_name : string
    last_name : string
    Returns
    -------
    Nothing. Just prints a string.
    """

    # first_name and last_name should be strings
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    elif type(last_name) is not str:
        raise TypeError('last_name must be a string')

    # if no last_name is given, don't print the space after first_name
    print('My name is' + ' ' + first_name + ' ' + last_name)
