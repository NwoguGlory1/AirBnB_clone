#!/usr/bin/python3
"""Defines the module base_model"""

import uuid
import datetime
"""Defines the imported modules"""


class BaseModel:
    def __init__(self): 
        """Defines the class BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        Defines a magic method prints:[<class name>](<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
        self.__dict__)

    def save(self):
        """Updates the public instance attribute, with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ obj"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
