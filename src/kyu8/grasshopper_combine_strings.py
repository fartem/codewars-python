# https://www.codewars.com/kata/55f73f66d160f1f1db000059
class GrasshopperCombineStrings:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def solution(self):
        return "{} {}".format(self.first, self.last)
