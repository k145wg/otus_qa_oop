from src.Figure import Figure


class Square(Figure):
    name = 'Квадрат'

    def __init__(self, a):
        if a <= 0:
            raise ValueError('Несуществующий квадрат')
        self.a = a

    def calculate_area(self):
        return self.a * self.a

    def calculate_perimeter(self):
        return 4 * self.a
