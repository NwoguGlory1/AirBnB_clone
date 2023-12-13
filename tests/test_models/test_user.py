#!/usr/bin/python3
"""Defines the unittest for user."""
import unittest
from models.base_model import BaseModel
from models.user import User

class TestUser(unittest.TestCase):
    """Defines the test for the class User"""

    def setUp(self):
      """sets up all method, runs before all methods """
      self.user = User()
      self.value = User
      self.new_user = self.value()

    def test_email(self):
        """Tests the email method of User class """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """Tests the password method of User class """
        new = self.value
        self.assertEqual(type(new.password), str)

    def test_first_name(self):
        """Tests the first_name method of User class """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Tests the last name method of User class """
        new = self.value()
        self.assertEqual(type(new.last_name), str)
        if __name__ ==  "__main__":
            unittest.main()

    """def test_email_str(self):
        """ """
        with self.assertRaises(TypeError):
            if not isinstance(self.new_user.email, str):
                if __name__ == "__main__":
                    unittest.main() """
