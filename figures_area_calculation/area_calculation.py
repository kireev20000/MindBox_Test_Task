from math import sqrt, pi


class Figure:
    """ Базовый класс фигур."""
    def calculate_area(self):
        raise NotImplementedError(
            "В дочернем классе должен быть "
            "переопределен метод calculate_area()"
        )


class Circle(Figure):
    """ Класс работы с кругом."""
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius**2


class Triangle(Figure):
    """ Класс работы с треугольником."""
    def __init__(self, side1, side2, side3):
        self.a = side1
        self.b = side2
        self.c = side3

        if not (self.a + self.b > self.c and
                self.a + self.c > self.b and
                self.b + self.c > self.a):
            raise ValueError('Это не треугольник! У треугольника '
                             'сумма любых двух сторон должна быть '
                             'больше третьей!')

    def calculate_area(self):
        """ Расчет площади по формуле Герона."""
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def is_right_triangle(self):
        """ Является ли треугольник прямоугольным."""
        t = sorted(list([self.a, self.b, self.c]))
        return bool(t[0] > 0 and t[0] * t[0] + t[1] * t[1] == t[2] * t[2])


class Rectangle(Figure):
    """ Класс работы с прямоугольником (для примера добавления)."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


def calculate_area(*args, **kwargs):
    if len(args) == 1:
        return Circle(*args).calculate_area()
    if len(args) == 2:
        return Rectangle(*args).calculate_area()
    if len(args) == 3:
        return Triangle(*args).calculate_area()
    if len(args) > 3:
        raise NotImplementedError(
            "Метод расчета площади этой фигуры не реализован!"
        )


if __name__ == '__main__':
    pass
