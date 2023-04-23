class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

import unittest

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        result = self.calculator.add(2, 3)
        self.assertEqual(result, 5, msg="Addition test failed: expected 5, but got {}".format(result))

    def test_subtraction(self):
        result = self.calculator.subtract(5, 2)
        self.assertEqual(result, 3, msg="Subtraction test failed: expected 3, but got {}".format(result))

if __name__ == '__main__':
    unittest.main()
