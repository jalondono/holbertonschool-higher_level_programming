#!/usr/bin/python3
class Rectangle:
    """Create a Rectangle class"""

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        Return:
            - width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Set the width value
            ARGS:
                - value
        """
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Return:
            - height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height value
        ARGS:
            - value
        """
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Return the area of a rectangle
        Return:
            - Area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Return the perimeter of a rectangle
        Return:
            - perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)
