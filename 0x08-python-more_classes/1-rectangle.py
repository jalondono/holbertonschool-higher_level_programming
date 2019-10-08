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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
