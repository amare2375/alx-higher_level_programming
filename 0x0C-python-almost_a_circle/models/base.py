#!/usr/bin/python3
"""module for Base class"""
import json
import io
import os.path
import turtle


class Base:
    """Base is the base class of all future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """method for initializing instances of Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of lists of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries, skipkeys=True)

    @classmethod
    def save_to_file(cls, list_objs):
        """write JSON string repr of a list of all instances to a file"""
        with open("{}.json".format(cls.__name__), 'wt') as file:
            if list_objs is None:
                file.write('[]')
            else:
                l = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """return list of the JSON string repr"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            a = cls(4, 2)
        elif cls.__name__ == 'Square':
            a = cls(4)
        a.update(**dictionary)
        return a

    @classmethod
    def load_from_file(cls):
        """return a list of instances from a JSON file"""
        if not os.path.isfile("{}.json".format(cls.__name__)):
            return []
        with open(cls.__name__ + '.json', 'rt') as file:
            list_output = cls.from_json_string(file.read())
            ret = []
            for item in list_output:
                ret.append(cls.create(**item))
            return ret

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to csv file"""
        pass

    @classmethod
    def load_from_file_csv(cls):
        """deserialize from csv file"""
        pass

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draws all rectangles and squares in lists"""
        for rectangle in list_rectangles + list_squares:
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            turtle.setheading(0)
            turtle.forward(rectangle.width)
            turtle.left(90)
            turtle.forward(rectangle.height)
            turtle.left(90)
            turtle.forward(rectangle.width)
            turtle.left(90)
            turtle.forward(rectangle.height)
            turtle.left(90)
