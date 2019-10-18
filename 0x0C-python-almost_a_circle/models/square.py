#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[{}]({:d}) {:d} / {:d} - {:d}" \
            .format(self.__class__.__name__,
                    self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size
