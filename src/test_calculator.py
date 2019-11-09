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
