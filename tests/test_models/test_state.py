#!/usr/bin/python3
"""Defines unittests for models/state.py"""


import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Defines unittests for the State class"""

    def test_attributes(self):
        """Tests the attributes of the State class"""
        state = State()
        self.assertEqual(state.name, "")
