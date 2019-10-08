#!/usr/bin/python3
class Rectangle:
    """Create a Rectangle class"""

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')

        if width < 0:
            raise ValueError('width must be >= 0')

        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

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

    def __str__(self):
        """
        convert Python objects into strings
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                print("#", end='')
            if i != self.__height - 1:
                print()
        return ''

    def __repr__(self):
        """return the return value
        would be a valid string objec
        """
        return "Rectangle(%d, %d)" % (self.__height, self.__width)
