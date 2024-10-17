#!/usr/bin/env python3
"""Generate random strings"""

from argparse import ArgumentParser
from random import choice
from string import printable


def get_length() -> int:
    """Get length of string from command line using argparse"""
    parser = ArgumentParser(description="Generate random strings")
    parser.add_argument(
        "length",
        type=int,
        help="Length of the random string",
    )
    return parser.parse_args().length


def generate_random_string(length: int) -> str:
    """Generate a random string of length `length`"""
    string = ""
    for _ in range(length):
        string += choice(printable[:-5])
    return string


if __name__ == "__main__":
    print(generate_random_string(get_length()))
