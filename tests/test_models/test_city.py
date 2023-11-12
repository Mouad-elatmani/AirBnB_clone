#!/usr/bin/python3
"""testing the city class"""

import unittest
from models.city import City
from datetime import datetime

class TestCity(unittest.TestCase):
    """
    testing and cheking the type and existing of attributes
    """

    def test_existing(self):
        testCity = City()
        self.assertTrue(hasattr(testCity, "name"))
        self.assertTrue(hasattr(testCity, "id"))
        self.assertTrue(hasattr(testCity, "state_id"))
        self.assertTrue(hasattr(testCity, "created_at"))
        self.assertTrue(hasattr(testCity, "updated_at"))

if __name__ == "__main__":
    unittest.main()
