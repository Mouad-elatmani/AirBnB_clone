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

    def test_type(self):
        testBase = BaseModel()
        self.assertIsInstance(testBase.id, str)
        self.assertIsInstance(testBase.created_at, datetime)
        self.assertIsInstance(testBase.updated_at, datetime)

    def test_datetime_model(self):
        """testing datetime base model"""
        model_3 = BaseModel()
        model_4 = BaseModel()
        self.assertNotEqual(model_3.created_at, model_3.updated_at)
        self.assertNotEqual(model_3.created_at, model_4.created_at)


if __name__ == "__main__":
    unittest.main()
