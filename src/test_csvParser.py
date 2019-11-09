import unittest
from os import path
from src.csvParser import parseCsv
from src.calculator import Stock

EXAMPLE_STOCK_FILE=path.dirname(path.abspath(__file__)) + '/test_resources/exampleStock.csv'

class TestCsvParser(unittest.TestCase):
    def test_parses_csv(self):
        stock = parseCsv(EXAMPLE_STOCK_FILE)

        expectedStock = [
            Stock('chocolate', 10),
            Stock('licorice', 7),
            Stock('chewing gum', 6),
            Stock('coal', 1)
        ]

        self.assertEqual(stock, expectedStock)
