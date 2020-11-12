import unittest

from src.kyu8.grasshopper_combine_strings import GrasshopperCombineStrings

class CombineStringsTest(unittest.TestCase):

    def test_combine_names(self):
        self.assertEqual(
            "James Stevens",
            GrasshopperCombineStrings("James", "Stevens").solution()
        )
        self.assertEqual(
            "Davy Back",
            GrasshopperCombineStrings("Davy", "Back").solution()
        )
        self.assertEqual(
            "Arthur Dent",
            GrasshopperCombineStrings("Arthur", "Dent").solution()
        )
