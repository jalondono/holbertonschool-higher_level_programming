#!/usr/bin/python3
import json
import csv
import turtle


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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        lista = []
        with open(cls.__name__ + '.json', 'w', encoding='utf-8')as myFile:
            if list_objs is None:
                myFile.write(cls.to_json_string([]))
            for obj in list_objs:
                lista.append(obj.to_dictionary())
            myFile.write(cls.to_json_string(lista))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy_instance = cls(1, 1, 0, 0)
        cls.update(dummy_instance, **dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        my_list = []
        try:
            with open(cls.__name__ + '.json', 'r', encoding="utf-8")as myFile:

                file = myFile.read()
                listFromJson = cls.from_json_string(file)
                for elem in listFromJson:
                    my_Object = cls.create(**elem)
                    my_list.append(my_Object)
                return my_list
        except:
            return my_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        columnsReactangle = ['id', 'width', 'height', 'x', 'y']
        columnsSquare = ['id', 'size', 'x', 'y']
        auxdict = {}
        with open(cls.__name__ + '.csv', 'w')as csvFile:
            if list_objs is None:
                return []
            if cls.__name__ == 'Rectangle':
                writer = csv.DictWriter(csvFile, fieldnames=columnsReactangle)
            else:
                writer = csv.DictWriter(csvFile, fieldnames=columnsSquare)
            writer.writeheader()
            for dicti in list_objs:
                auxdict = dicti.to_dictionary()
                writer.writerow(auxdict)

    @classmethod
    def load_from_file_csv(cls):
        my_list = []
        with open(cls.__name__ + '.csv')as myFile:
            reader = csv.DictReader(myFile, delimiter=',')
            for row in reader:
                # my_object = cls.create(**row)
                my_list.append(dict(row))
        return my_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        idx = 0
        my_list = []
        shapes_list = []
        def draw_rectangle(width, height, x, y):
            turtle.up()
            turtle.goto(x, y)
            turtle.down()
            for i in range(2):
                turtle.forward(width)
                turtle.left(90)
                turtle.forward(height)
                turtle.left(90)

        for rec in list_rectangles:
            idx = 0
            auxbook = rec.__dict__
            if len(auxbook) < 2:
                continue
            for value in auxbook.values():
                if idx >= 1:
                    my_list.append(value)
                idx += 1
            shapes_list.append(my_list.copy())
            my_list.clear()
        for shape in shapes_list:
            draw_rectangle(shape[0], shape[1], shape[2], shape[3])

        for rec in list_squares:
            idx = 0
            auxbook = rec.__dict__
            if len(auxbook) < 1:
                continue
            for value in auxbook.values():
                if idx >= 1:
                    my_list.append(value)
                idx += 1
            shapes_list.append(my_list.copy())
            my_list.clear()
        for shape in shapes_list:
            draw_rectangle(shape[0], shape[0], shape[1], shape[2])
