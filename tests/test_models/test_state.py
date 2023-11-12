#!/usr/bin/python3
"""testing the state class"""

import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """
    testing and checking existing of attributes
    """

    def test_state(self):
        thestate = State()
        self.assertTrue(hasattr(thestate, "name"))
        self.assertTrue(hasattr(thestate, "id"))
        self.assertTrue(hasattr(thestate, "created_at"))
        self.assertTrue(hasattr(thestate, "updated_at"))


if __name__ == "__main__":
    unittest.main()
