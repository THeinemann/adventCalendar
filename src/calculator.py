from typing import List, Dict
import random

class Stock:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

Name = str
AdventCalendar = Dict[int, str]
AdventCalendars = Dict[Name, AdventCalendar]

def flatten(nestedList):
    return [ item for sublist in nestedList for item in sublist ]

def calculate(stock: List[Stock], names: List[Name], days=24) -> AdventCalendars:
    dayRange = range(1, days + 1)

    fullStock = flatten([ [s.name] * s.amount for s in stock ])

    if len(fullStock) < len(names) * days:
        raise ValueError('Not enough presents for everyone :(')

    random.shuffle(fullStock)

    calendars = { name: {} for name in names }

    nextItem = 0
    for day in dayRange:
        for name in names:
            item = fullStock[nextItem]
            calendars[name][day] = fullStock[nextItem]
            nextItem = nextItem + 1

    return calendars
