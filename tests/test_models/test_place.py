#!/usr/bin/python3
"""Defines unittests for models/place.py"""


import unittest
from models.place import Place
"""Defines the imported modules"""


class TestPlace(unittest.TestCase):
    """Defines unittests for the Place class"""

    def test_attributes(self):
        """Tests the attributes of the Place class"""
        place = Place()
        self.assertEqual(place.name, "")
