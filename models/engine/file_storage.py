#!/usr/bin/python3
"""Module defines a class ``FileStorage`` used to serialize/deserialize
python data to/from a JSON file"""
import json
from models.base_model import BaseModel


class FileStorage():
    """object used to store data using a dictionary representation"""
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """constructor for class object ``FileStorage``"""
        pass

    def all(self):
        """method returns dictionary (string representation of instances)"""
        return self.__objects

    def new(self, obj):
        """method assigns key/pair values to private attribute ``objects``"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """method serializes innstances to a JSON file"""
        easyDict = {}
        for key, val in self.__objects.items():
            easyDict[key] = val.to_dict()
        with open(self.__file_path, 'w') as JsFile:
            json.dump(easyDict, JsFile)

    def reload(self):
        """method deserializes JSON file to pythonic instances.
        If JSON file is missing exception is silenced"""
        try:
            with open(self.__file_path, 'r') as JsFile:
                json_obj = json.load(JsFile)
            for key, val in json_obj.items():
                my_dict = '{}(**{})'.format(val['__class__'], val)
                self.__objects[key] = eval(my_dict)
        except:
            pass
