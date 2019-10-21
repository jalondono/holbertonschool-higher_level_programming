#!/usr/bin/python3
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open(cls.__name__+'.json', 'w', encoding='utf-8')as myFile:
            if list_objs is None:
                myFile.write("[]")
            for obj in list_objs:
                result = cls.to_json_string([obj.to_dictionary()])
                myFile.write(result)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy_instance = cls(1, 1, 1, 1)
        for key, value in dictionary.items():
            setattr(dummy_instance, key, value)
        return dummy_instance
