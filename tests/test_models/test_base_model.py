#!/usr/bin/python3
"""Defines a unittest for base_model module"""

import unittest
from models.base_model import BaseModel
"""Defines the imported modules"""


class TestBaseModel(unittest.TestCase):
    """Defines the test for the class BaseModel"""
    def test_base_model(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertEqual(str(my_model), "[{}] ({}) {}".format(
            my_model.__class__.__name__, my_model.id, my_model.__dict__))

    def test_save(self):
       """Defines a test for the save method"""
       my_model = BaseModel()
       old_updated_at = my_model.updated_at
       my_model.save()
       self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict(self):
        """Defines the test for the to_dict method"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        expected_dict = {
                'id': my_model.id,
                'created_at': my_model.created_at.isoformat(),
                'updated_at': my_model.updated_at.isoformat(),
                'name': 'My First Model',
                'my_number': 89,
                '__class__': 'BaseModel'
                }
        self.assertDictEqual(my_model_json, expected_dict)
    
    def setup(self):
        """Defines the setup method for the test"""
        pass

    def teardown(self):
        """Defines the teardown meathod of the test"""
        pass
