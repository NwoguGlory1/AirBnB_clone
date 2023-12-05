#!/usr/bin/python3
"""Defines the file_storage module"""


from models.base_model import BaseModel
"""Defines the imported Modules"""


class FileStorage:
    """
    Defines the class FileStorage that serializes instances to a JSON file
    and deserializes a JSON file to instances
    """
    def __init__(self):
        """Defines the constructor for the class FileStorage"""
        self.__file_path =
        self.__objects =

    def all(self):
        """Defines the public instance method all() that returns the dict"""
    def new(seld, obj):
        """
        Defines the public instance method that sets in __objects the obj
        with key <obj class name>.id
        """
    def save(self):
        """
        Defines the public instance method that serializes __objects to the
        JSON file (path: __file_path)
        """
    def reload(self):
        """
        Defines the public instance method that deserializes the JSON file
        to __objects (only if the JSON file (__file_path) exists ; otherwise,
        nothing occurs. If the file doesn’t exist, no exception is raised)
        """
