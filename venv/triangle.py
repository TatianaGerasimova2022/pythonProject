import math


class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.perim = side1 + side2 + side3
        self.square = math.sqrt(self.perim * (self.perim - self.side1) * (self.perim - self.side2) * (self.perim - self.side3))
    def __str__(self):
        return 'сторона1='+str(self.side1)
    def type(self):
        if self.side1==self.side2==self.side3:
            return'равносторонний'
        else:
            return 'другой'