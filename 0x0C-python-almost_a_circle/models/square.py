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

    def update(self, *args, **kwargs):
        def update(self, *args, **kwargs):
            var = ['id', 'width', 'height', 'x', 'y']
            for idx in range(0, len(args)):
                if idx >= len(args):
                    break
                setattr(self, var[idx], args[idx])
            if len(args) == 0:
                for idx in kwargs.keys():
                    if idx in var:
                        setattr(self, idx, kwargs[idx])
            else:
                pass