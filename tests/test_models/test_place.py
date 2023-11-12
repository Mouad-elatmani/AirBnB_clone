#!/usr/bin/python3
"""testing the place class"""

import unittest
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """
    testing and cheking the type and existing of attributes
    """

    def test_existing(self):
        test_Place = Place()
        self.assertTrue(hasattr(test_Place, "city_id"))
        self.assertTrue(hasattr(test_Place, "user_id"))
        self.assertTrue(hasattr(test_Place, "name"))
        self.assertTrue(hasattr(test_Place, "id"))
        self.assertTrue(hasattr(test_Place, "description"))
        self.assertTrue(hasattr(test_Place, "number_rooms"))
        self.assertTrue(hasattr(test_Place, "number_bathrooms"))
        self.assertTrue(hasattr(test_Place, "max_guest"))
        self.assertTrue(hasattr(test_Place, "price_by_night"))
        self.assertTrue(hasattr(test_Place, "latitude"))
        self.assertTrue(hasattr(test_Place, "longitude"))
        self.assertTrue(hasattr(test_Place, "amenity_ids"))
        self.assertTrue(hasattr(test_Place, "created_at"))
        self.assertTrue(hasattr(test_Place, "updated_at"))
