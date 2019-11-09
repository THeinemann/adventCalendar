from .cli import parse_arguments, print_calendars
from .calculator import calculate
from .csvParser import parseCsv
import sys

def main(args = sys.argv[1:]):
    config = parse_arguments(args)
    stock = parseCsv(config.stock)

    results = calculate(stock, config.calendar_names)

    print_calendars(results)
