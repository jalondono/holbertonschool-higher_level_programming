#!/usr/bin/python3
"""class"""


def is_same_class(obj, a_class):
    """
    function to identify to which class belong an object
    :param obj:
    :param a_class:
    :return:
    """
    if type(obj) is a_class:
        return True
    return False
