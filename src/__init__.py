from .cli import parse_arguments
import sys

def main(args = sys.argv[1:]):
    parse_arguments(args)
