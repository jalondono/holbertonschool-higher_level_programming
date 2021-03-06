#!/usr/bin/python3
"""class"""


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


class Rectangle(BaseGeometry):
    """
     class Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
