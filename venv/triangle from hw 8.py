import math


class Triangle:
    def __init__(self, sides, angles):
        self.sides = sides
        self.angles = angles

    def perim(self):
        return sum(self.sides)

    def square(self):
        return math.sqrt(self.perim() *
                         (self.perim() - self.sides[0]) *
                         (self.perim() - self.sides[1]) *
                         (self.perim() - self.sides[2]))

    def __str__(self):
        return 'сторона1=' + str(self.sides[0]) + '\n' + \
               'сторона2=' + str(self.sides[1]) + '\n' + \
               'сторона3=' + str(self.sides[2])

    def type(self):
        if self.sides[0] == self.sides[1] == self.sides[2]:
            return 'равносторонний'
        elif self.angles[0] == 90 or self.angles[1] == 90 or self.angles[2] == 90:
            return 'прямоугольный'
        elif self.sides[0] == self.sides[1] or self.sides[1] == self.sides[2] or self.sides[2] == self.sides[0]:
            return 'равнобедренный'
        else:
            return 'произвольный'


class IsoscelesTriangle(Triangle):
    def square(self):
        if self.sides[0] == self.sides[1]:
            return (self.sides[2] * math.sqrt(self.sides[0] ** 2 - (self.sides[2] ** 2) / 4)) / 2
    def square(self):
        if self.sides[1] == self.sides[2]:
            return (self.sides[0] * math.sqrt(self.sides[1] ** 2 - (self.sides[0] ** 2) / 4)) / 2
    def square(self):
        if self.sides[2] == self.sides[0]:
            return (self.sides[1] * math.sqrt(self.sides[2] ** 2 - (self.sides[1] ** 2) / 4)) / 2


class RightTriangle(Triangle):
    def square(self):
        if self.angles[0] == 90 and self.sides[0] ** 2 == self.sides[1] ** 2 + self.sides[2] ** 2:
            return (self.sides[1] * self.sides[2]) / 2
    def square(self):
        if self.angles[1] == 90 and self.sides[2] ** 2 == self.sides[1] ** 2 + self.sides[0] ** 2:
            return (self.sides[1] * self.sides[0]) / 2
    def square(self):
        if self.angles[2] == 90 and self.sides[1] ** 2 == self.sides[0] ** 2 + self.sides[2] ** 2:
            return (self.sides[0] * self.sides[2]) / 2


tr = Triangle([5, 4, 3], [30, 30, 120])
print(tr.sides)
print(tr.perim())
print(tr.square())
print(tr)
