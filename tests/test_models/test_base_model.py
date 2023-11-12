#!/usr/bin/python3
"""testing the class BasseModel"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    testing and cheking the type and existing of attributes
    """

    def test_existing(self):
        testBase = BaseModel()
        self.assertTrue(hasattr(testBase, "id"))
        self.assertTrue(hasattr(testBase, "created_at"))
        self.assertTrue(hasattr(testBase, "updated_at"))


if __name__ == "__main__":
    unittest.main()
