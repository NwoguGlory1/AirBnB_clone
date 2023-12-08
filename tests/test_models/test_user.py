#!/usr/bin/python3
"""Defines the unittest for user."""


class TestUser(unittest.Testcase):
    """Defines the test for the class User"""

    def test_attributes(self):
        """Tests the attributes of the State class"""
        user = User()
        self.assertEqual(user.name, "")
