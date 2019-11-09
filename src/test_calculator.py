import unittest
from src.calculator import Stock, calculate

class CalculatorTest(unittest.TestCase):
    def test_calculate_calendar_from_stock(self):
        stock = [
            Stock('chocolate', 7),
            Stock('sweets', 8),
            Stock('coal', 9)
        ]
        names = ['Jane']

        calendar = calculate(stock, names)

        self.assertEquals(len(calendar), 1)
        self.assertEquals(len(calendar['Jane']), 24)

        self.assertEquals(list(calendar['Jane'].values()).count('chocolate'), 7)
        self.assertEquals(list(calendar['Jane'].values()).count('sweets'), 8)
        self.assertEquals(list(calendar['Jane'].values()).count('coal'), 9)

    def test_raise_value_error_if_not_enough_stock_is_present(self):
        stock = [
            Stock('chocolate', 47)
        ]
        names = ['John', 'Jane']

        with self.assertRaises(ValueError) as context:
            calculate(stock, names)

        self.assertEquals(str(context.exception), 'Not enough presents for everyone :(')
