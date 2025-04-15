# https://github.com/moritaporretti/lab10-MP-AN.git
# Partner 1: Morita Porretti
# Partner 2: Alula Nahu


import unittest
from calculator import (
    add, subtract, mul, div,
    logarithm, exp, square_root, hypotenuse
)

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 5), 4)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-3, -1), -2)

    def test_multiply(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-1, 5), -5)

    def test_divide(self):
        self.assertEqual(div(2, 6), 3)
        with self.assertRaises(ZeroDivisionError):
            div(0, 6)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3.0)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)
        with self.assertRaises(ValueError):
            logarithm(-2, 10)
        with self.assertRaises(ValueError):
            logarithm(2, -10)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 100)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3.0)
        with self.assertRaises(ValueError):
            square_root(-1)

    def test_exponent(self):
        self.assertEqual(exp(2, 3), 8)
        self.assertEqual(exp(5, 0), 1)

