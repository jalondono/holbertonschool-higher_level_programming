#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance of a class
    that inherited (directly or indirectly)
    :param obj:
    :param a_class:
    :return:
    """
    if issubclass(type(obj), a_class):
        if type(obj) == a_class:
            return False
        return True
    return False
