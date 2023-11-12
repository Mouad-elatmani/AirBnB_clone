#!/usr/bin/python3
"""testing the review class"""

import unittest
from models.review import Review
from datetime import datetime


class Testingreview(unittest.TestCase):
    """
    testing and checking the exitsence of attributes
    """

    def test_review(self):
        thereview = Review()
        self.assertTrue(hasattr(thereview, "id"))
        self.assertTrue(hasattr(thereview, "place_id"))
        self.assertTrue(hasattr(thereview, "user_id"))
        self.assertTrue(hasattr(thereview, "text"))
        self.assertTrue(hasattr(thereview, "created_at"))
        self.assertTrue(hasattr(thereview, "updated_at"))


if __name__ == "__main__":
    unittest.main()
