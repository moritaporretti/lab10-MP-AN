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
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 100), 0)


     def test_divide(self):
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(7, 2), 3.5)
        self.assertEqual(div(-6, 2), -3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(10, 1000), 3)
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(math.e, math.e**2), 2)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, 0)
        with self.assertRaises(ValueError):
            logarithm(10, -5)


    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 100)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(1, 1), math.sqrt(2))


    def test_sqrt(self):
        self.assertEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(2), math.sqrt(2))
        with self.assertRaises(ValueError):
            square_root(-1)
            
     def test_exponent(self):
        self.assertEqual(exp(2, 3), 8)
        self.assertEqual(exp(5, 0), 1)
        self.assertEqual(exp(1, 10), 1)

    # Do not touch this
    if __name__ == "__main__":
        unittest.main()

