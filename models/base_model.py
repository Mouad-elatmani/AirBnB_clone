#!/usr/bin/python3
"""
Module that defines the BaseModel class
"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """
    BaseModel for creating and manipulating BaseModel objects
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class
        """
        if kwargs:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        self.__dict__[key] = datetime.fromisoformat(val)
                    else:
                        self.__dict__[key] = val
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        String representation
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update public instance attribute updated_at with current datetime
        """
        self.updated_at = datetime.now()

        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        """
        dicti = self.__dict__.copy()
        dicti['__class__'] = self.__class__.__name__
        dicti['created_at'] = self.created_at.isoformat()
        dicti.update({"updated_at": self.updated_at.isoformat()})
        return dicti
