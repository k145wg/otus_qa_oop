from src.Figure import Figure
from math import sqrt


class Triangle(Figure):
    name = 'Треугольник'

    def __init__(self, a, b, c):
        if (a <= 0) or (b <= 0) or (c <= 0):
            raise ValueError('Значение одной или нескольких сторон неположительное')
        elif not ((a + b > c) and (c + b > a) and (c + a > b)):
            raise ValueError('Несуществующий треугольник')
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        semi_perimeter = self.calculate_perimeter() / 2
        return sqrt(semi_perimeter * (semi_perimeter - self.a) * (semi_perimeter - self.b) * (semi_perimeter - self.c))

    def calculate_perimeter(self):
        return self.a + self.b + self.c
