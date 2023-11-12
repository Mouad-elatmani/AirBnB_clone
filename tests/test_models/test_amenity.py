#!/usr/bin/python3
"""testing theamenity class"""

import unittest
from models.amenity import Amenity
from datetime import datetime


class TestingAmenity(unittest.TestCase):
    """
    testing and checking the existing of attributes
    """

    def testamenity(self):
        theamenity = Amenity()
        self.assertTrue(hasattr(theamenity, "name"))
        self.assertTrue(hasattr(theamenity, "id"))
        self.assertTrue(hasattr(theamenity, "created_at"))
        self.assertTrue(hasattr(theamenity, "updated_at"))


if __name__ == "__main__":
    unittest.main()
