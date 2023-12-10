#!/usr/bin/python3
"""Defines unittests for models/state.py"""


import unittest
from models.state import State
"""Defines the imported modules"""


class TestState(unittest.TestCase):
    """Defines unittests for the State class"""

    def test_attributes(self):
        """Tests the attributes of the State class"""
        state = State()
        self.assertEqual(state.name, "")
