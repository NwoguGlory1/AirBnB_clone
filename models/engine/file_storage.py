#!/usr/bin/python3
"""Defines the file_storage module"""

import json
"""Defines the imported Modules"""


class FileStorage:
    """
    Defines the class FileStorage that serializes instances to a JSON file
    and deserializes a JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Defines the public instance method all() that returns the dict"""
        return FileStorage.__objects

    def new(self, obj):
        """
        Defines the public instance method that sets in __objects the obj
        with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Defines the public instance method that serializes __objects to the
        JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, 'w') as file:
            obj_dict = {}
            for key, value in FileStorage.__objects.items():
                obj_dict[key] = value.to_dict()
            json.dump(obj_dict, file)

    def reload(self):
        """
        Defines the public instance method that deserializes the JSON file
        to __objects (only if the JSON file (__file_path) exists ; otherwise,
        nothing occurs. If the file doesn’t exist, no exception is raised)
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        """Defines the imported model method Basemodel"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    obj = eval(class_name)(**value)
                    FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass
