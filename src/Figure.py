class Figure:
    name = None

    def __init__(self):
        pass

    def calculate_area(self):
        return None

    def calculate_perimeter(self):
        return None

    @property
    def area(self):
        return self.calculate_area()

    @property
    def perimeter(self):
        return self.calculate_perimeter()

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError
        return figure.calculate_area() + self.calculate_area()
