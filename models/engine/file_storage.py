#!/usr/bin/python3
import json

class FileStorage:
    """A class that serializes instances to a JSON file, deserializes JSON file to instances"""

    def __init__(self, file_path="file.json"):
        """ Constructor """
        self.__file_path = "file_path"
        self.__objects = {}

    def all(self, cls=None):
        """Returns the dictionary __objects"""
        if cls:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id """
        obj_id = obj.__class__.__name__ + '.' + obj.id
        self.__objects[obj_id] = obj

    def save(self):
        jdic[key] = {key: value.to_dict()for key, value in self.__objects.items()}
        with open(self.__filepath, 'w', encoding="utf-8") as file:
            json.dump(jdic, file)

    def  reload(self):
        """Deserializes the JSON file to __objects """
        try:
            from models.base_model import BaseModel
            with open(self.__file_path, 'r', encoding = "utf-8") as file:
                data = json.load(file)
                for key, value in data.items():
                    clas = value["__class__"]
                    obj = eval(clas + "(**value)")

                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
