import argparse


def parse_arguments(args):
    parser = argparse.ArgumentParser(description = 'Create the presents of advent calendars based on stock')
    parser.add_argument('stock', metavar='STOCk', help='A file which contains the stock of presents in CSV format')
    parser.add_argument('calendar_names', metavar='NAME', nargs='+', help='The names of the calendars, e.g. names of the children')

    parser.parse_args(args)
