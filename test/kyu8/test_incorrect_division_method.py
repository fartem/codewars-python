import unittest

from src.kyu8.incorrect_division_method import IncorrectDivisionMethod

class DivisionMethodTest(unittest.TestCase):

    def test_divide_numbers(self):
        self.assertEqual(
            2,
            IncorrectDivisionMethod(4, 2).solution()
        )
        self.assertEqual(
            5,
            IncorrectDivisionMethod(10, 2).solution()
        )
        self.assertEqual(
            2.25,
            IncorrectDivisionMethod(9, 4).solution()
        )
        self.assertEqual(
            4.2,
            IncorrectDivisionMethod(21, 5).solution()
        )
        self.assertEqual(
            3,
            IncorrectDivisionMethod(9, 3).solution()
        )
        self.assertEqual(
            0.01,
            IncorrectDivisionMethod(1, 100).solution()
        )
