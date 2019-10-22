#!/usr/bin/python3
"""
class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        constructor square
        :param size:
        :param x:
        :param y:
        :param id:
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        print the instance
        :return:
        """
        return "[{}] ({:d}) {:d}/{:d} - {:d}" \
            .format(self.__class__.__name__,
                    self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        getter size
        :return:
        """
        return self.height

    @size.setter
    def size(self, size):
        """
        setter size
        :param size:
        :return:
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        update value to attributes
        :param args:
        :param kwargs:
        :return:
        """
        var = ['id', 'size', 'x', 'y']
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
        keys = ['id', 'size', 'x', 'y']
        attr = [self.id, self.size, self.x, self.y]
        return dict(zip(keys, attr))
