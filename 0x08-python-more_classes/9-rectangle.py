#!/usr/bin/python3
class Rectangle:
    """Create a Rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

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
                print(self.print_symbol, end='')
            if i != self.__height - 1:
                print()
        return ''

    def __repr__(self):
        """return the return value
        would be a valid string object
        """
        repr_str = self.__class__.__name__
        return "{}({}, {})".format(repr_str, self.__width, self.__height)

    def __del__(self):
        """
        print a message when an instance is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        static method to calculate
        if anyone is bigger than other
        :param rect_1:
        :param rect_2:
        :return:
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.height * rect_1.width) >= (rect_2.width * rect_2.height):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0)
        return cls(height=size, width=size)
