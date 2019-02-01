#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os
import datetime
import string
import copy
import numpy as np
from pprint import pprint

# every get_rank_xxx() returns the ordinal ranks,
# except get_rank_dict()

def get_rank_np(l: list):
    arr = np.array(l)
    t = arr.argsort()
    rank_arr = np.empty_like(arr)
    rank_arr[t] = np.arange(len(arr))
    return rank_arr.tolist()


def get_rank_simple(l: list):
    #return sorted(range(len(l)), key=lambda x: l[x])
    output = [0] * len(l)
    for i, v in enumerate(sorted(range(len(l)), key=lambda x: l[x])):
        output[v] = i
        print('output[{}] = {}'.format(v, i))
        print('l[{}] = {}'.format(v, l[v]))
    return output

def get_rank_simple_v2(l: list):
    if len(l)==0: return []
    l.sort()
    return [l.index(x) for x in sorted(range(len(l)), key=l.__getitem__)]

def get_rank_dict(l: list):
    t_rank = dict((x, i) for i, x in enumerate(sorted(l)))
    pprint(t_rank)
    return [t_rank[x] for x in l]

data = [
        [],
        [1],
        [9, 7, 5, 3, 1],
        [9, 7, 7, 5, 3, 1]
        ]

for d in data:
    print('='*20)
    print('value: ', d)
    print('get_rank_np: ', get_rank_np(d))
    print('get_rank_simple: ', get_rank_simple(d))
    print('get_rank_dict: ', get_rank_dict(d))
    #print('get_rank_simple_v2: ', get_rank_simple_v2(d))

