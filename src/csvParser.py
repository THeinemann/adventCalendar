import csv
from src.calculator import Stock

def parseCsv(filename):
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        return [ Stock(r['name'], int(r['amount'])) for r in reader ]
