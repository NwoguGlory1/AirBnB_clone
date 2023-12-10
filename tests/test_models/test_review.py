#!/usr/bin/python3
"""Defines unittests for models/review.py"""


import unittest
from models.review import Review
"""Defines the imported modules"""


class TestReview(unittest.TestCase):
    """Defines unittests for the Review class"""

    def test_attributes(self):
        """Tests the attributes of the Review class"""
        review = Review()
        self.assertEqual(review.name, "")
