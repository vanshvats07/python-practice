import unittest

from package.maths import addition, multiplication, subtraction


class MathsTests(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(3, 5), 8)

    def test_subtraction(self):
        self.assertEqual(subtraction(2, 1), 1)

    def test_multiplication(self):
        self.assertEqual(multiplication(3, 5), 15)


if __name__ == "__main__":
    unittest.main()
