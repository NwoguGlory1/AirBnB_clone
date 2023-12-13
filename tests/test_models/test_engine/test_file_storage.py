#!/usr/bin/python3
"""Defines the unittest for file_storage"""

from os.path import exists
from os import remove
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review
from datetime import datetime
import io
import json

"""Defines the imported modules"""


class TestFileStorage(unittest.TestCase):
    """Defines the unittest for the class FileStorage"""

    def TestFileStorage_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def TestFileStorage_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def TestFileStorage_filepath_is_private(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def TestFileStorage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)

class TestFileStorage7Methods(unittest.TestCase):
    """Defines tests for all methods"""
    file_storage = FileStorage()

    def setUp(self):
        """ ensures that file does not exist before each test method"""
        try:
            remove("file.json")
        except:
            pass
        self.file_storage._FileStorage__objects = {}


    def tearDown(self):
        """ removes each test file after each test method """
        try:
            remove("file.json")
        except:
            pass

    def test_all(self):
        """Defines the test for all()"""
        self.assertEqual(dict, type(self.file_storage.all()))
        self.assertIsInstance(self.file_storage.all(), dict)

    def test_all_with_arg(self):
        """Defines the test for all() with an argument"""
        with self.assertRaises(TypeError):
            self.file_storage.all(None)

    def test_new(self):
        """Defines the test for new()"""
        B = BaseModel()
        U = User()
        S = State()
        P = Place()
        C = City()
        A = Amenity()
        R = Review()
        self.file_storage.new(BaseModel())
        self.file_storage.new(User())
        self.file_storage.new(State())
        self.file_storage.new(Place())
        self.file_storage.new(City())
        self.file_storage.new(Amenity())
        self.file_storage.new(Review())

        self.assertIn("BaseModel." + B.id, self.file_storage.all().keys())
        self.assertIn(B, self.file_storage.all().values())
        # ... similar assertions for other objects ...

    def test_new_with_args(self):
        """Defines the test for new() with arguments"""
        with self.assertRaises(TypeError):
            self.file_storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        """Defines the test for new() with None"""
        with self.assertRaises(AttributeError):
            self.file_storage.new(None)

    def test_save(self):
        """Defines the test for save()"""
        B = BaseModel()
        U = User()
        S = State()
        P = Place()
        C = City()
        A = Amenity()
        R = Review()
        self.file_storage.new(BaseModel())
        self.file_storage.new(User())
        self.file_storage.new(State())
        self.file_storage.new(Place())
        self.file_storage.new(City())
        self.file_storage.new(Amenity())
        self.file_storage.new(Review())
        self.file_storage.save()

        # Add assertions for save() based on your implementation

    def test_save_with_arg(self):
        """Defines the test for save() with an argument"""
        with self.assertRaises(TypeError):
            self.file_storage.save(None)

    def test_reload(self):
        """Defines the test for reload()"""
        B = BaseModel()
        U = User()
        S = State()
        P = Place()
        C = City()
        A = Amenity()
        R = Review()
        self.file_storage.new(BaseModel())
        self.file_storage.new(User())
        self.file_storage.new(State())
        self.file_storage.new(Place())
        self.file_storage.new(City())
        self.file_storage.new(Amenity())
        self.file_storage.new(Review())
        self.file_storage.save()
        F_obj = self.file_storage._FileStorage__objects

        # Add assertions for reload() based on your implementation

        def test_reload_with_arg(self):
        """Defines the test for reload() with an argument"""
        with self.assertRaises(TypeError):
            self.file_storage.reload(None)

if __name__ == "__main__":
    unittest.main()
