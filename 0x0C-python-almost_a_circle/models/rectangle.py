#!/usr/bin/python3
"""
Rectangle class inherit from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        constructor method
        :param width:
        :param height:
        :param x:
        :param y:
        :param id:
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        getter width
        :return:
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter width
        :param value:
        :return:
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        getter height
        :return:
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter height
        :param value:
        :return:
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        getter x
        :return:
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter x
        :param value:
        :return:
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        getter y
        :return:
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter y
        :param value:
        :return:
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        return the area
        :return:
        """
        return self.__height * self.__width

    def __str__(self):
        """
        print
        :return:
        """
        return ("[Rectangle] " + "(" + str(self.id) + ") " +
                str(self.__x) + "/" + str(self.__y) + " - " +
                str(self.__width) + "/" + str(self.__height))

    def display(self):
        """
        print a rectagle made with #
        :return:
        """
        for verOffset in range(0, self.__y):
            print()
        for vert in range(0, self.__height):
            for horz in range(0, self.__width + self.__x):
                if horz < self.__x:
                    print(' ', end='')
                else:
                    print("#", end='')
            print()

    def update(self, *args, **kwargs):
        """
        update attributes
        :param args:
        :param kwargs:
        :return:
        """
        var = ['id', 'width', 'height', 'x', 'y']
        for idx in range(min(len(args), len(var))):
            if idx >= len(args):
                break
            setattr(self, var[idx], args[idx])
        if len(args) == 0:
            for idx in kwargs.keys():
                if idx in var:
                    setattr(self, idx, kwargs[idx])
        else:
            pass

    def to_dictionary(self):
        """
        convert into a dictionary
        :return:
        """
        keys = ['id', 'width', 'height', 'x', 'y']
        attr = [self.id, self.width, self.height, self.x, self.y]
        return dict(zip(keys, attr))
