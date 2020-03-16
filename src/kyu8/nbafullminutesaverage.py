# https://www.codewars.com/kata/587c2d08bb65b5e8040004fd
class NbaFullMinutesAverage:
    
    def __init__(self, ppg, mpg):
        self.ppg = ppg
        self.mpg = mpg
    
    def result(self):
        if self.ppg == 0 or self.mpg == 0:
            return 0
        else:
            return round(48 *(self.ppg / self.mpg), 1)
