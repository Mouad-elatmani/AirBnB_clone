#!/usr/bin/python3
"""FileStorage Module"""
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path='./file.json'
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"]=obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w",encoding='utf-8') as file:
            temp={}
            for key,value in self.__objects.items():
                temp[key]=value.to_dict()
            json.dump(temp, file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing."""

        try:
            with open(self.__file_path,"r",encoding = 'utf-8') as file:
                for key, value in json.load(file).items():
                    if "BaseModel" in key:
                        self.__objects[key] = BaseModel(**value)



        except FileNotFoundError:
            pass


        
    



