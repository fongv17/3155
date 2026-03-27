import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.add(0, 2, 3),5)
        self.assertEqual(Calculator.add(0, 5, 3), 8)

    def test_sub(self):
        self.assertEqual(Calculator.subtract(0, 2, 1), 1)
        self.assertEqual(Calculator.subtract(0, 6, 1), 5)

    def test_multiply(self):
        self.assertEqual(Calculator.multiplication(0, 4, 5), 20)
        self.assertEqual(Calculator.multiplication(0, 6, 5), 30)

    def test_divide(self):
        self.assertEqual(Calculator.division(0, 6, 2), 3)
        self.assertEqual(Calculator.division(0, 8, 2), 4)

    if __name__ == "__main__":
        unittest.main()