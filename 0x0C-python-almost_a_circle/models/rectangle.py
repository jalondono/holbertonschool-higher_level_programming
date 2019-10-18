#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return "[{}] ({:d}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.__class__.__name__, self.id,
                    self.__x, self.__y, self.__width, self.__height)

    def display(self):
        for verOffset in range(0, self.__y):
            print()
        for vert in range(0, self.__height):
            for horz in range(0, self.__width + self.__x):
                if horz < self.__x:
                    print(' ', end='')
                else:
                    print("#", end='')
            print()

    def update(self, *args):
        for idx in range(0, len(args)):
            if idx == 0:
                self.id = args[idx]
            elif idx == 1:
                self.__width = args[idx]
            elif idx == 2:
                self.__height = args[idx]
            elif idx == 3:
                self.__x = args[idx]
            elif idx == 4:
                self.__y = args[idx]
            else:
                pass
