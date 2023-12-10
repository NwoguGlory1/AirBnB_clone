#!/usr/bin/python3
"""Defines the unittest for amenity"""


import unittest
from models.amenity import Amenity
"""Defines the imported modules"""


class TestAmenity(unittest.TestCase):
    """Defines the test for the class Amenity"""
    amenity = Amenity()
    self.assertEqual(amenity.name, "")
