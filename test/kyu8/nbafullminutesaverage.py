import unittest

from src.kyu8.nbafullminutesaverage import NbaFullMinutesAverage

class NbaMinutesAverageTest(unittest.TestCase):

    def test_result(self):
        self.assertEqual(
            28.8,
            NbaFullMinutesAverage(12, 20).result()
        )
        self.assertEqual(
            48.0,
            NbaFullMinutesAverage(10, 10).result()
        )
        self.assertEqual(
            14.1,
            NbaFullMinutesAverage(5, 17).result()
        )
        self.assertEqual(
            0,
            NbaFullMinutesAverage(0, 0).result()
        )
        self.assertEqual(
            42.6,
            NbaFullMinutesAverage(30.8, 34.7).result()
        )
        self.assertEqual(
            32.5,
            NbaFullMinutesAverage(22.9, 33.8).result()
        )
