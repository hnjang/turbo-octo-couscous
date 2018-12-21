#!/usr/bin/python3
import sys
from pprint import pprint
import collections
from functools import cmp_to_key
from scipy import stats
import numpy as np

def median(v):
    if len(v)==0: return None
    m = len(v) // 2
    v.sort()
    pprint(v)
    if len(v)%2==1:
        return v[m]
    else:
        return (v[m] + v[m -1])/2.0

if __name__ == '__main__':
    n = int(input())
    v = [int(__) for __ in input().split()]
    q2 = median(v)
    lower = [__ for __ in v if __ < q2]
    upper = [__ for __ in v if __ > q2]
    q1 = median(lower)
    q3 = median(upper)
    for qq in [q1,q2,q3]:
        print(qq)

    '''
    res = [np.percentile(v, r) for r in [25, 50, 75]]
    res_int = [int(r) for r in res]
    for r in res:
        print(r)
    '''
