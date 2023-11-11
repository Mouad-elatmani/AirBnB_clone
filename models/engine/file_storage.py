#!/usr/bin/python3
"""FileStorage Module"""


import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """ FileStorage cls for creating and manipulating FileStorage objects"""
    __file_path = './file.json'
    __objects = {}

    def __init__(self):
        """ Initializes a new instance of the FileStorage class """
        pass

    def all(self):
        """ Retrives the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets a new instance using the format <obj class name>.id = obj"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        with open(self.__file_path, "w", encoding='utf-8') as file:
            temp = {}
            for key, value in FileStorage.__objects.items():
                temp[key] = value.to_dict()
            json.dump(temp, file)

    def reload(self):
        """deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, "r", encoding='utf-8') as file:
                new_dict = json.load(file)
                for key, value in new_dict.items():
                    """if "BaseModel" in key:
                        self.__objects[key] = BaseModel(**value)
                    elif "User" in key:
                        self.__objects[key] = User(**value)"""
                    cl_nm = value.get('__class__')
                    if cl_nm:
                        obj = eval(cl_nm + '(**value)')
                        FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass
