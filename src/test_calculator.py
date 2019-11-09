import unittest
from unittest.mock import patch
from src.calculator import Stock, calculate

class CalculatorTest(unittest.TestCase):
    def test_calculate_calendar_from_stock(self):
        stock = [
            Stock('chocolate', 7),
            Stock('sweets', 8),
            Stock('coal', 9)
        ]
        names = ['Jane']

        calendars = calculate(stock, names)

        self.assertEqual(len(calendars), 1)
        self.assertEqual(len(calendars['Jane']), 24)

        calendar = calendars['Jane']
        self.assertEqual(list(calendar.values()).count('chocolate'), 7)
        self.assertEqual(list(calendar.values()).count('sweets'), 8)
        self.assertEqual(list(calendar.values()).count('coal'), 9)

    @patch('random.shuffle')
    def test_randomizes_order_of_presents(self, shuffle):
        stock = [
            Stock('wine', 24),
            Stock('beer', 24),
        ]

        randomized_stock = ['wine', 'beer'] * 24
        expected_stock = ['wine'] * 24 + ['beer'] * 24
        def shuffle_effect(input):
            self.assertEqual(input, expected_stock)
            for n, _ in enumerate(input):
                input[n] = randomized_stock[n]
        shuffle.side_effect = shuffle_effect

        names = ['Jane', 'John']
        calendars = calculate(stock, names)

        janesCalendar = calendars['Jane']
        johnsCalendar = calendars['John']
        self.assertEqual(list(janesCalendar.values()), ['wine'] * 24)
        self.assertEqual(list(johnsCalendar.values()), ['beer'] * 24)

        shuffle.assert_called()

    def test_raise_value_error_if_not_enough_stock_is_present(self):
        stock = [
            Stock('chocolate', 47)
        ]
        names = ['John', 'Jane']

        with self.assertRaises(ValueError) as context:
            calculate(stock, names)

        self.assertEqual(str(context.exception), 'Not enough presents for everyone :(')
