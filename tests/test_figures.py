import pytest
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
from math import sqrt


@pytest.mark.parametrize("test_input",
                         [
                             'Circle(-1)',
                             'Rectangle(-1, -1)',
                             'Square(-1)',
                             'Triangle(-1, -1, -1)'
                         ])
def test_figures_creation(test_input):
    with pytest.raises(ValueError):
        eval(test_input)


def test_triangle_creation():
    with pytest.raises(ValueError):
        Triangle(1, 2, 3)


@pytest.mark.parametrize("test_input,expected",
                         [
                             ('Circle', 'Круг'),
                             ('Rectangle', 'Прямоугольник'),
                             ('Square', 'Квадрат'),
                             ('Triangle', 'Треугольник')
                         ])
def test_get_figures_name(test_input, expected):
    assert eval(test_input + '.name') == expected


@pytest.mark.parametrize("test_input", [1, 3, 7])
def test_get_area_circle(test_input):
    assert Circle(test_input).area == 3.14 * test_input * test_input


@pytest.mark.parametrize("test_input",
                         [(1, 1),
                          (120, 8),
                          (4, 13)
                          ])
def test_get_area_rectangle(test_input):
    assert Rectangle(test_input[0], test_input[1]).area == test_input[0] * test_input[1]


@pytest.mark.parametrize("test_input", [17, 1, 720])
def test_get_area_square(test_input):
    assert Square(test_input).area == test_input * test_input


@pytest.mark.parametrize("test_input",
                         [(6, 7, 8),
                          (12, 8, 14),
                          (120, 130, 50)
                          ])
def test_get_area_triangle(test_input):
    semi_perimeter = (test_input[0] + test_input[1] + test_input[2]) / 2
    assert Triangle(test_input[0], test_input[1], test_input[2]).area == sqrt(
        semi_perimeter * (semi_perimeter - test_input[0]) * (semi_perimeter - test_input[1]) * (
                semi_perimeter - test_input[2]))


@pytest.mark.parametrize("test_input", [1, 3, 7])
def test_get_perimeter_circle(test_input):
    assert Circle(test_input).perimeter == 2 * 3.14 * test_input


@pytest.mark.parametrize("test_input",
                         [(1, 1),
                          (120, 8),
                          (4, 13)
                          ])
def test_get_perimeter_rectangle(test_input):
    assert Rectangle(test_input[0], test_input[1]).perimeter == 2 * (test_input[0] + test_input[1])


@pytest.mark.parametrize("test_input", [17, 1, 720])
def test_get_perimeter_square(test_input):
    assert Square(test_input).perimeter == 4 * test_input


@pytest.mark.parametrize("test_input",
                         [(6, 7, 8),
                          (12, 8, 14),
                          (120, 130, 50)
                          ])
def test_get_perimeter_triangle(test_input):
    assert Triangle(test_input[0], test_input[1], test_input[2]).perimeter == test_input[0] + test_input[1] + \
           test_input[2]


@pytest.mark.parametrize("test_input",
                         [
                             'Circle(1)',
                             'Rectangle(1, 1)',
                             'Square(1)',
                             'Triangle(2, 3, 4)'
                         ])
def test_add_area_bad(test_input):
    with pytest.raises(ValueError):
        eval(test_input).add_area(123)


@pytest.mark.parametrize("test_input", [1, 3, 7])
def test_add_area_circle(test_input):
    circle = Circle(test_input)
    triangle = Triangle(12, 16, 22)
    assert circle.add_area(triangle) == circle.area + triangle.area


@pytest.mark.parametrize("test_input",
                         [(1, 1),
                          (120, 8),
                          (4, 13)
                          ])
def test_add_area_rectangle(test_input):
    rectangle = Rectangle(test_input[0], test_input[1])
    square = Square(781)
    assert rectangle.add_area(square) == rectangle.area + square.area


@pytest.mark.parametrize("test_input", [17, 1, 720])
def test_add_area_square(test_input):
    square = Square(test_input)
    triangle = Triangle(12, 16, 22)
    assert square.add_area(triangle) == square.area + triangle.area


@pytest.mark.parametrize("test_input",
                         [(6, 7, 8),
                          (12, 8, 14),
                          (120, 130, 50)
                          ])
def test_add_area_triangle(test_input):
    triangle = Triangle(test_input[0], test_input[1], test_input[2])
    square = Square(622)
    assert triangle.add_area(square) == triangle.area + square.area
