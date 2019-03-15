#!/usr/bin/python3

import sys
import csv
import random
from pprint import pprint


def get_sub_dataset(cnt):
    return [['x', 'y'] * (cnt // 2), [random.random() for i in range(cnt)]]


data = []
for i in range(4):
    data.extend(get_sub_dataset(8))
data.extend([list(range(8))])
data.extend([[1, 2, 3, 4, 5, 6, 7, 'x']])
pprint(data)

with open('some.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
