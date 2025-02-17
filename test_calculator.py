import calculator
import unittest


class TestAddition(unittest.TestCase):
    def test_add(self):
        self.assertEqual(4, calculator.add(2, 2))


class TestSubtraction(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(2, calculator.subtract(4, 2))
