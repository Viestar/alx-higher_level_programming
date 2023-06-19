#!/usr/bin/python3
"""Base Class Documentation"""


import json
import csv
import turtle


class Base:
    """Base class Creation"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation (Creating Base Class Objects)
        Args:
            id (int): Unique number for the instance
        """

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string of a list of dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): list of instances which inherits from Base
        """
        filename = cls.__name__ + ".json"
        list_objects = []
        if list_objs is not None:
            for x in list_objs:
                list_objects.append(cls.to_dictionary(x))
        with open(filename, 'w', encoding='utf-8') as myFile:
            myFile.write(cls.to_json_string(list_objects))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set

        Args:
            dictionary (dict): Attributes to set
        Return:
            the instance with all the attributes set
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Returns instances list from a file with JSON object

        Return:
            the instance list object with all instances initialized
        """
        filename = cls.__name__ + ".json"
        json_from_list = []
        try:
            with open(filename, 'r', encoding='utf-8') as myFile:
                json_from_list = cls.from_json_string(myFile.read())
            for x, y in enumerate(json_from_list):
                json_from_list[x] = cls.create(**json_from_list[x])
        except:
            pass
        return json_from_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialises.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Square":
                    holders = ["id", "size", "x", "y"]
                else:
                    holders = ["id", "width", "height", "x", "y"]
                csv_written = csv.DictWriter(csv_file, holders=holders)
                for obj in list_objs:
                    csv_written.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Deserialises.
        Returns:
            an empty list or a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csv_file:
                if cls.__name__ == "Square":
                    holders = ["id", "size", "x", "y"]
                else:
                    holders = ["id", "width", "height", "x", "y"]
                csv_read = csv.DictReader(csv_file, holders=holders)
                csv_read = [dict([k, int(v)] for k, v in d.items())
                            for d in csv_read]
                return [cls.create(**d) for d in csv_read]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Uses turtle module to draw Rectangles and Squares.
        Args:
            list_rectangles (list): Properties to draw.
            list_squares (list): Properties to draw.
        """

        window = turtle.Turtle()
        window.pensize(4)
        window.shape("square")
        window.screen.bgcolor("#F5F5F5")
        window.color("#BF7609")

        window.color("#7D0552")
        for drawer in list_rectangles:
            window.showturtle()
            window.up()
            window.goto(drawer.x, drawer.y)
            window.down()
            for index in range(2):
                window.forward(drawer.width)
                window.left(90)
                window.forward(drawer.height)
                window.left(90)
            window.hideturtle()

        window.color("#461B7E")
        for drawer in list_squares:
            window.showturtle()
            window.up()
            window.goto(drawer.x, drawer.y)
            window.down()
            for index in range(2):
                window.forward(drawer.width)
                window.left(90)
                window.forward(drawer.height)
                window.left(90)
            window.hideturtle()

        turtle.exitonclick()
