import unittest
import figures_area_calculation.area_calculation as figures


class TestFigures(unittest.TestCase):
    """ Тестируем вычисления площади фигур."""
    def test_area_calculation(self):
        test_data = {
            (4, ): 50.26548245743669,
            (4, 2, ): 8,
            (4, 5, 6, ): 9.921567416492215,
         }
        for numbers, result in test_data.items():
            self.assertEqual(figures.calculate_area(*numbers), result)

    def test_not_implemented(self):
        """ Тестируем неизвестные фигуры."""
        with self.assertRaises(NotImplementedError):
            figures.calculate_area(1, 2, 3, 4, )

    def test_is_triangle(self):
        """ Тестируем треугольник ли это. """
        with self.assertRaises(ValueError):
            figures.calculate_area(1, 2, 3, )

    def test_is_right_triangle(self):
        """ Тестируем является ли треугольник прямоугольным. """
        test_data = {
            (3, 4, 5, ): True,
            (145, 105, 100, ): True,
            (70, 130, 110, ): False,
        }
        for numbers, result in test_data.items():
            self.assertEqual(
                figures.Triangle(*numbers).is_right_triangle(), result
            )


if __name__ == '__main__':
    unittest.main()
