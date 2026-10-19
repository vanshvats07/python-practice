import unittest

from package.maths import (
    addition,
    division,
    exponentiation,
    floor_division,
    multiplication,
    remainder,
    subtraction,
)


class MathsTests(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(3, 5), 8)

    def test_subtraction(self):
        self.assertEqual(subtraction(2, 1), 1)

    def test_multiplication(self):
        self.assertEqual(multiplication(3, 5), 15)

    def test_division(self):
        self.assertEqual(division(8, 2), 4)

    def test_division_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            division(8, 0)

    def test_exponentiation(self):
        self.assertEqual(exponentiation(2, 3), 8)
        self.assertEqual(exponentiation(2, -2), 0.25)

    def test_floor_division(self):
        self.assertEqual(floor_division(7, 3), 2)
        self.assertEqual(floor_division(-7, 3), -3)

    def test_remainder(self):
        self.assertEqual(remainder(7, 3), 1)
        self.assertEqual(remainder(-7, 3), 2)


if __name__ == "__main__":
    unittest.main()
