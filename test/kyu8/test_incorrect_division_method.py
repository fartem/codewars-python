import unittest

from src.kyu8.incorrect_division_method import DivisionMethod

class DivisionMethodTest(unittest.TestCase):

    def test_divide_numbers(self):
        self.assertEqual(
            2,
            DivisionMethod(4, 2).divide_numbers()
        )
        self.assertEqual(
            5,
            DivisionMethod(10, 2).divide_numbers()
        )
        self.assertEqual(
            2.25,
            DivisionMethod(9, 4).divide_numbers()
        )
        self.assertEqual(
            4.2,
            DivisionMethod(21, 5).divide_numbers()
        )
        self.assertEqual(
            3,
            DivisionMethod(9, 3).divide_numbers()
        )
        self.assertEqual(
            0.01,
            DivisionMethod(1, 100).divide_numbers()
        )
