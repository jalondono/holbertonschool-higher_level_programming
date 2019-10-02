#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        """ Creates a private instance attribute, size(int)
                Args:
                    - size: size of square
                    - position position square
                Raises:
                    - TypeError: must be an int
                    - ValueError: must be >= 0
                    - TypeError: if not a tuple of 2 positive integers
        """
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.position = position
        self.size = size

    @property
    def size(self):
        """ return size
            Return:
                - size
        """
        return int(self.__size)

    @size.setter
    def size(self, value):
        """ set de value
        ARGS:
            - value(int): value to set size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns position of the square
               position.setter:
                   resets the position of the square
               Args:
                   value(int): size of the square
               Raises:
                   TypeError: if not a tuple of 2 positive integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ set de value
                ARGS:
                    - value(tuple): value to set position
        """
        if ((value[0] < 0 or value[1] < 0) or not isinstance(value, tuple)
                or not isinstance(value[0], int, ) or not isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Calculate the area of squeare
        Return:
             - Area of square
        """
        return int(self.__size) * int(self.__size)

    def my_print(self):
        """ Prints a square of a certain size at a position
               self.size:
                   calls size from the getter
               note:
                   if you have a setter and getter you don't need to interact
                   with private so that you don't mess up the values
        """
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                if self.__position[0] >= self.__position[1]:
                    for k in range(0, self.__position[0]):
                        print(" ", end='')
                for j in range(0, self.__size):
                    print("#", end='')
                print()
