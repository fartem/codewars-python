import unittest

from src.kyu8.grasshopper_combine_strings import CombineStrings

class CombineStringsTest(unittest.TestCase):

    def test_combine_names(self):
        self.assertEqual(
            "James Stevens",
            CombineStrings("James", "Stevens").solution()
        )
        self.assertEqual(
            "Davy Back",
            CombineStrings("Davy", "Back").solution()
        )
        self.assertEqual(
            "Arthur Dent",
            CombineStrings("Arthur", "Dent").solution()
        )
