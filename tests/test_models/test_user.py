#!/usr/bin/python3
"""testing the user class"""

import unittest
from models.user import User
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestUser(unittest.TestCase):
    """
    testing the class User and check the attribue and type of the cass
    """

    def test_user(self):
        test_user = User()
        self.assertTrue(hasattr(theuser, "email"))
        self.assertTrue(hasattr(theuser, "password"))
        self.assertTrue(hasattr(theuser, "first_name"))
        self.assertTrue(hasattr(theuser, "last_name"))
        self.assertTrue(hasattr(theuser, "id"))
        self.assertTrue(hasattr(theuser, "created_at"))
        self.assertTrue(hasattr(theuser, "updated_at"))


if __name__ == "__main__":
    unittest.main()
