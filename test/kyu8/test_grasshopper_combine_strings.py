import unittest

from src.kyu8.grasshopper_combine_strings import CombineStrings

class CombineStringsTest(unittest.TestCase):

    def test_combine_names(self):
        self.assertEqual(
            "James Stevens",
            CombineStrings("James", "Stevens").combine_names()
        )
        self.assertEqual(
            "Davy Back",
            CombineStrings("Davy", "Back").combine_names()
        )
        self.assertEqual(
            "Arthur Dent",
            CombineStrings("Arthur", "Dent").combine_names()
        )
