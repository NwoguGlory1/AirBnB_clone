#!/usr/bin/python3
"""Defines the module base_model"""


import uuid
import datetime
from models import storage
"""Defines the imported modules"""


class BaseModel:
    """Defines the  class BaseModel that creates an object"""
    def __init__(self, *args, **kwargs):
        """Defines the constructor for the class BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'id' and value is None:
                    value = str(uuid.uuid4())
                if key in ['created_at', 'updated_at']:
                    value = datetime.datetime.strptime(value,
                            '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Defines a magic method prints:[<class name>](<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute, with the current datetime"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ obj"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict.pop('_sa_instance_state', None)
        return obj_dict
