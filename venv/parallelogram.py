import math


class Parallelogram:
    def __init__(self, side1, side2, angle):
        self.side1 = side1
        self.side2 = side2
        self.angle = angle
        self.perim = 2 * (side1 + side2)

    def square(self):
        return self.side1 * self.side2 * math.sin(self.angle)
