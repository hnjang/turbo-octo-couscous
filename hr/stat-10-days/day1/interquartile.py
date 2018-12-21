#!/usr/bin/python3
import sys
from pprint import pprint
import collections
from functools import cmp_to_key
from scipy import stats
import numpy as np
import statistics


def median(v):
    if len(v)==0: return None
    m = len(v) // 2
    v.sort()
    # pprint(v)
    if len(v)%2==1:
        return v[m]
    else:
        return (v[m] + v[m -1])/2.0


def median_freq(v):
    if len(v)==1: return v[0][0]
    total_cnt = sum([v[i][1] for i in range(len(v))])
    v.sort(key=lambda x: x[0])
    # pprint(v)
    # print('start total_cnt: %d'%(total_cnt))
    if total_cnt % 2 == 1:
        # pick one
        idx = (total_cnt // 2)
        for vv in v:
            if (idx) < vv[1]:
                return vv[0]
            idx -= vv[1]
        return None
    else:
        # pick two items
        idx = (total_cnt // 2) - 1
        for i, vv in enumerate(v):
            if (idx + 1) < vv[1]:
                return vv[0]
            elif idx < vv[1]:
                return (vv[0] + v[i+1][0]) / 2
            idx -= vv[1]
        return None


def interquartile(n, x, f):
    v = [[x[i], f[i]] for i in range(len(x))]
    q2 = median_freq(v)
    lower = [vv for vv in v if vv[0] < q2]
    upper = [vv for vv in v if vv[0] > q2]
    q1 = median_freq(lower)
    q3 = median_freq(upper)
    print(q3-q1)


def interquartile_v2(n, x, f):
    s = []
    for i in range(n):
        s += [x[i]]* f[i]
    pprint(s)
    N = sum(f)
    s.sort()
    if n%2 != 0:
        q1 = median(s[:N//2])
        q3 = median(s[N//2+1:])
    else:
        q1 = median(s[:N//2])
        q3 = median(s[N//2:])
    print('%.1f'%(q3-q1))


if __name__ == '__main__':
    n = int(input())
    x = [int(__) for __ in input().split()]
    f = [int(__) for __ in input().split()]
    interquartile_v2(n, x, f)

