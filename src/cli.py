import argparse
import sys
import csv

def parse_arguments(args):
    parser = argparse.ArgumentParser(description = 'Create the presents of advent calendars based on stock')
    parser.add_argument('stock', metavar='STOCk', help='A file which contains the stock of presents in CSV format')
    parser.add_argument('calendar_names', metavar='NAME', nargs='+', help='The names of the calendars, e.g. names of the children')

    return parser.parse_args(args)

def print_calendars(calendars, output=sys.stdout):
    names = list(calendars.keys())
    days = list(calendars[names[0]].keys())
    days.sort()

    writer = csv.writer(output)
    writer.writerow(['Day', *names])

    for day in days:
        row = [day, *[calendars[name][day] for name in names]]
        writer.writerow(row)
