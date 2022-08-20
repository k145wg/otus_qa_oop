from src.Figure import Figure


class Rectangle(Figure):
    name = 'Прямоугольник'

    def __init__(self, a, b):
        if (a <= 0) or (b <= 0):
            raise ValueError('Несуществующий прямоугольник')
        self.a = a
        self.b = b

    def calculate_area(self):
        return self.a * self.b

    def calculate_perimeter(self):
        return 2 * (self.a + self.b)
