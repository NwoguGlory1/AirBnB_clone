#!/usr/bin/python3
"""Defines the unittest for user."""


import unittest
from models.user import User
"""Defines the imported modules"""


class TestUser(unittest.TestCase):
    """Defines the test for the class User"""

    def test_attributes(self):
        """Tests the attributes of the State class"""
        user = User()
        self.assertEqual(user.name, "")
