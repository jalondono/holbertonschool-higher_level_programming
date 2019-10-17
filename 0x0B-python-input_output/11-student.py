#!/usr/bin/python3
class Student:
    """
    consturtor
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last = last_name
        self.age = age

    def to_json(self):
        """
        function
        :param obj:
        :return:
        """
        return self.__dict__
