#!/usr/bin/python3

import sys
import csv
import math
from pprint import pprint


def row_iter_csv(source) -> csv.reader:
    return csv.reader(source)


def float_none(data):
    try:
        return float(data)
    except ValueError:
        return math.nan


float_row = lambda row: list(map(float_none, row))

# validtors
all_numeric = lambda row: not any(map(math.isnan, row)) and len(row) == 8
check_length = lambda row: len(row) == 8


def head_filter_map(validator, converter, row_iter):
    return filter(validator, map(converter, row_iter))


with open('some.csv', 'r', newline='') as f:
    reader = row_iter_csv(f)
    result = head_filter_map(all_numeric, float_row, reader)
    pprint(list(result))
