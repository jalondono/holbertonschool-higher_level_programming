#!/usr/bin/python3
class BaseGeometry:
    """
    Base class
    """

    def area(self):
        """
        not implemented
        :return:
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validate arguments of methods
        :param name:
        :param value:
        :return:
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
