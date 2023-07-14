#!/usr/bin/python3

"""Defines a Base class"""
import json


class Base:
    """Represents a Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialises the a new base object"""

        if id is None:
            Base.__nb_objects += 1
            self.id = self._Base__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""

        with open("%s.json" % cls.__name__, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                dict_list = [x.to_dictionary() for x in list_objs]
                jsonfile.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string
        """

        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""

        if dictionary and dictionary is not {}:
            if cls.__name__ == "Rectangle":
                instance = cls(5, 3)
            else:
                instance = cls(5)
            instance.update(**dictionary)
            return instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""

        try:
            with open("{}.json".format(cls.__name__), "r") as jsonfile:
                dict_list = Base.from_json_string(jsonfile.read())
                return [cls.create(**i) for i in dict_list]
        except IOError:
            return []
