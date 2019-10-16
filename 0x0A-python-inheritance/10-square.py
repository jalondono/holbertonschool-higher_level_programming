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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
     class Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        constructor method
        :param width:
        :param height:
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        calculate the area of rectangle
        :return: the area
        """
        return self.__height * self.__width

    def __str__(self):
        """
        print in a given format
        :return:
        """
        nameobj = self.__class__.__name__
        return "[{}] {:d}/{:d}".format(nameobj, self.__width, self.__height)


class Square(Rectangle):
    """
    a class Square that inherits from Rectangle
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
