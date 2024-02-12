#!/usr/bin/python3

"""This module contains Base class"""

import json
import csv
import turtle


class Base:
    """
    This Is the base class for other classes
    Attributes:
    __nb_objects (int): Is the number of objects created from this clase
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """The constructor to initialize instances of this class"""

        self.id = 0

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list of dictionaries
        Args:
            list_dictionaries (list of dicts): The list of dictionaries
            to return it's own JSON string representation
        """

        if not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        Args:
            list_objs (list): A list of instances who inherits of Base
            for example: list of Rectangle or list of Square instances
        """

        file_name = f"{cls.__name__}.json"
        with open(file_name, "w", encoding="utf-8") as file:

            if list_objs:
                list_objs = [obj.to_dictionary() for obj in list_objs]

            list_objs_to_json = cls.to_json_string(list_objs)
            file.write(list_objs_to_json)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string
        Args:
            json_string (str): s a string representing a list of dictionaries
        """

        if not json_string:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        Args:
            dictionary (dict): A dictionary that conttains all values of
            the attributes of the new instance to create
        """

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a file
        The filename must be: <Class name>.json - example: Rectangle.json
        """

        try:
            file_name = f"{cls.__name__}.json"

            with open(file_name, "r") as file:
                file_content = file.read()

            list_attr_values = cls.from_json_string(file_content)
            list_instance = []

            for attributes in list_attr_values:
                list_instance.append(cls.create(**attributes))

            return list_instance
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Writes a list_objs to a CSV file
        Format of the CSV:
            Rectangle: <id>,<width>,<height>,<x>,<y>
            Square: <id>,<size>,<x>,<y>
        Args:
            list_objs (list): A list of instances who inherits of Base
            for example: list of Rectangle or list of Square instances
        """

        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            csv_writer = csv.writer(file)
            if not list_objs:
                csv_writer.writerow([])
                return

            if cls.__name__ == "Rectangle":
                list_objs = [[obj.id, obj.width, obj.height, obj.x, obj.y]
                             for obj in list_objs]
            elif cls.__name__ == "Square":
                list_objs = [[obj.id, obj.size, obj.x, obj.y]
                             for obj in list_objs]
            csv_writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """
        Returns a list of instances from a csv file
        The filename must be: <Class name>.csv - example: Rectangle.csv
        """

        try:
            instance_list = []
            file_name = f"{cls.__name__}.csv"
            obj_dict = {}
            with open(file_name, "r") as file:
                csv_reader = csv.reader(file)
                for line in csv_reader:
                    line = [int(item) for item in line]
                    if cls.__name__ == "Rectangle":
                        obj_dict = {"id": line[0], "width": line[1],
                                    "height":  line[2], "x": line[3],
                                    "y": line[4]}
                    elif cls.__name__ == "Square":
                        obj_dict = {"id": line[0], "size": line[1],
                                    "x":  line[2], "y": line[3]}
                    instance_list.append(cls.create(**obj_dict))
        except FileNotFoundError:
            return []
        return instance_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles and Squares
        Args:
            list_rectangles (list): Is the list of rectangles to be drawn
            list_squares (list): Is the list of squares to be drawn
        """

        my_turtle = turtle.Turtle()
        my_turtle.screen.bgcolor("#a0db8e")
        my_turtle.pensize(3)
        my_turtle.color("#555656")
        for rectangle in list_rectangles:
            my_turtle.showturtle()
            my_turtle.penup()
            my_turtle.goto(rectangle.x, rectangle.y)
            my_turtle.pendown()
            my_turtle.forward(rectangle.width)
            my_turtle.left(90)
            my_turtle.forward(rectangle.height)
            my_turtle.left(90)
            my_turtle.forward(rectangle.width)
            my_turtle.left(90)
            my_turtle.forward(rectangle.height)
            my_turtle.left(90)
            my_turtle.hideturtle()

        my_turtle.color("#0a75ad")
        for square in list_squares:
            my_turtle.showturtle()
            my_turtle.penup()
            my_turtle.goto(square.x, square.y)
            my_turtle.pendown()
            my_turtle.forward(square.size)
            my_turtle.left(90)
            my_turtle.forward(square.size)
            my_turtle.left(90)
            my_turtle.forward(square.size)
            my_turtle.left(90)
            my_turtle.forward(square.size)
            my_turtle.left(90)
            my_turtle.hideturtle()

        turtle.done()
