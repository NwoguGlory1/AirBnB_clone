#!/usr/bin/python3
from datetime import datetime
import uuid

class BaseModel:                                                                  """A BaseModel class that defines all common attributes/methods for other classes"""                                                                        def __init__(self):
        self.id = str(uuid.uuid4())                                                   """Assign with an uuid when an instance is created """                        self.created_at = datetime.now()                                              """Assign with the current datetime when an instance is created"""
        self.updated_at = datetime.now()                                              """Assign with the current datetime when an instance is created, updates anytime object changes"""

    def __str__(self):                                                                """Provides a string representation of an object & displays it"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
                                                                                  def save(self):
        """Updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
                                                                                  def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
