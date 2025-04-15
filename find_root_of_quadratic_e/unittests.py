import math
import unittest

from find_root_of_quadratic_e.equation_functions import solve_quadratic, parse_expression


class TestQuadraticSolver(unittest.TestCase):

    def test_two_real_roots(self):
        a, b, c, rhs = 1, -5, 6, 0
        roots, _ = solve_quadratic(a, b, c, rhs, '-', '+')
        self.assertEqual(sorted(roots), [2.0, 3.0])

    def test_one_real_root(self):
        a, b, c, rhs = 1, -2, 1, 0
        roots, _ = solve_quadratic(a, b, c, rhs, '-', '+')
        self.assertEqual(roots, [1.0])

    def test_no_real_roots(self):
        a, b, c, rhs = 1, 2, 5, 0
        roots, _ = solve_quadratic(a, b, c, rhs, '+', '+')
        self.assertEqual(roots, [])

    def test_linear_equation(self):
        a, b, c, rhs = 0, 2, -6, 0
        roots, _ = solve_quadratic(a, b, c, rhs, '+', '-')
        self.assertEqual(roots, [3.0])

    def test_not_even_linear(self):
        a, b, c, rhs = 0, 0, 5, 0
        roots, _ = solve_quadratic(a, b, c, rhs, '+', '+')
        self.assertEqual(roots, [])

    def test_equation_1(self):
        a, b, c, rhs = 1, -5, 4, 0
        roots, _ = solve_quadratic(a, b, c, rhs, '-', '+')
        self.assertEqual(roots, [1, 4])

    def test_equation_2(self):
        a, b, c, rhs = 1, -7, 12, 0
        roots, _ = solve_quadratic(a, b, c, rhs, '-', '+')
        self.assertEqual(roots, [3, 4])

    def test_equation_3(self):
        a, b, c, rhs = 1, 14, 45, 0
        roots, _ = solve_quadratic(a, b, c, rhs, '-', '+')
        self.assertEqual(roots, [-9, -5])

    def test_equation_4(self):
        a, b, c, rhs = 1, -12, 35, 0
        roots, _ = solve_quadratic(a, b, c, rhs, '-', '+')
        self.assertEqual(roots, [5, 7])

class TestParseExpression(unittest.TestCase):

    def test_full_quadratic(self):
        self.assertEqual(parse_expression("x^2 - 6x + 9"), (1, -6, 9))

    def test_negative_leading_coefficient(self):
        self.assertEqual(parse_expression("-2x^2 + 3x - 1"), (-2, 3, -1))

    def test_no_constant_term(self):
        self.assertEqual(parse_expression("x^2 + 4x"), (1, 4, 0))

    def test_no_x_term(self):
        self.assertEqual(parse_expression("2x^2 - 5"), (2, 0, -5))

    def test_linear_expression(self):
        self.assertEqual(parse_expression("3x - 9"), (0, 3, -9))

    def test_constant_only(self):
        self.assertEqual(parse_expression("7"), (0, 0, 7))

    def test_negative_x_and_constant(self):
        self.assertEqual(parse_expression("-x - 2"), (0, -1, -2))

    def test_single_x_squared(self):
        self.assertEqual(parse_expression("-x^2"), (-1, 0, 0))

    def test_messy_spacing(self):
        self.assertEqual(parse_expression(" - x^2 +   4x  -    5 "), (-1, 4, -5))


if __name__ == '__main__':
    unittest.main()