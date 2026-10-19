import unittest

from package.maths import addition, division, multiplication, subtraction


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


if __name__ == "__main__":
    unittest.main()
