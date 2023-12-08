#!/usr/bin/python3
"""Defines unittests for models/city.py"""

import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Defines unittests for the State class"""

    def test_attributes(self):
        """Tests the attributes of the State class"""
        city = City()
        self.assertEqual(state.name, "")
