from src.Figure import Figure


class Circle(Figure):
    name = 'Круг'

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError('Несуществующий круг')
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius
