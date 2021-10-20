#!/usr/bin/python3

""" this module contains one class """
import json


class Base:
    """this is the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init method"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert a list of dictionaries to json"""
        if list_dictionaries == None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save a list of objects to a file"""
        fname = "{}.json".format(cls.__name__)
        with open(fname, encoding="utf-8", mode="w") as f:
            if list_objs == None:
                f.write("[]")
            else:
                list_dict = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """convert json string to a list of dictionaries"""
        if json_string == None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create class instance from dictionary"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """return list of instances from a file"""
        fname = "{}.json".format(cls.__name__)
        try:
            with open(fname, mode="r", encoding="utf-8") as f:
                list_dicts = Base.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
