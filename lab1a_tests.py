# CPE 202 Lab 1 Test Cases

import unittest
from lab1a import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_01(self) -> None:
        tlist = [1, 2, 3]
        self.assertEqual(max_list_iter(tlist), 3)   # basic test

    def test_max_list_02(self) -> None:
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_03(self) -> None:
        tlist: List[int] = []
        self.assertEqual(max_list_iter(tlist), None)    # used to check for empty list

    def test_reverse_01(self) -> None:
        intlist = [1, 2, 3]
        revlist = reverse_list(intlist)
        self.assertEqual(revlist, [3, 2, 1])
        self.assertEqual(intlist, [1, 2, 3])    # basic test

    def test_reverse_02(self) -> None:
        intlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(intlist)

    def test_reverse_mutate_01(self) -> None:
        intlist = [1, 2, 3]
        reverse_list_mutate(intlist)
        self.assertEqual(intlist, [3, 2, 1])    # used to check odd list length

    def test_reverse_mutate_02(self) -> None:
        intlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(intlist)

    def test_reverse_mutate_03(self) -> None:
        intlist = [1, 2, 3, 4]
        reverse_list_mutate(intlist)
        self.assertEqual(intlist, [4, 3, 2, 1])   # used to check even list length

if __name__ == "__main__":
        unittest.main()
