#!/usr/bin/python3
"""FileStorage Module"""


import json
from models.base_model import BaseModel


class FileStorage:
    """ FileStorage cls for creating and manipulating FileStorage objects"""
    __file_path = './file.json'
    __objects = {}

    def __init__(self):
        """ Initializes a new instance of the FileStorage class """
        pass

    def all(self):
        """ Retrives the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets a new instance using the format <obj class name>.id = obj"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        with open(self.__file_path, "w", encoding='utf-8') as file:
            temp = {}
            for key, value in self.__objects.items():
                temp[key] = value.to_dict()
            json.dump(temp, file)

    def reload(self):
        """deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, "r", encoding='utf-8') as file:
                for key, value in json.load(file).items():
                    if "BaseModel" in key:
                        self.__objects[key] = BaseModel(**value)

        except FileNotFoundError:
            pass
