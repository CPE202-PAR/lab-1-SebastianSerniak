# CPE 202 Location Class Test Cases, Lab 1

import unittest
from location import *

class TestLocation(unittest.TestCase):

    def test_init(self) -> None:
        loc = Location('SLO', 35.3, -120.7)
        self.assertEqual(repr(loc), "Location('SLO', 35.3, -120.7)")

    def test_eq(self) -> None:
        loc = Location('SLO', 35.3, -120.7)
        loc1 = Location('SLO', 35.3, -120.7)
        self.assertEqual(loc == loc1, True)

    def test_repr0(self) -> None:
        loc = Location('SLO', 35.3, -120.7)
        self.assertEqual(repr(loc), "Location('SLO', 35.3, -120.7)")

    def test_repr1(self) -> None:
        loc = Location('Paris', 48.9, 2.4)
        self.assertEqual(repr(loc), "Location('Paris', 48.9, 2.4)")
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
