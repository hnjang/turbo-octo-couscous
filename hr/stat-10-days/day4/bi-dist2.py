#!/usr/bin/python3
import sys
import math
from pprint import pprint
import collections
from functools import cmp_to_key
from scipy import stats
import numpy as np
import statistics as st


def median(v):
    if len(v) == 0:
        return None
    m = len(v) // 2
    v.sort()
    # pprint(v)
    if len(v) % 2 == 1:
        return v[m]
    else:
        return (v[m] + v[m - 1]) / 2.0


def median_freq(v):
    if len(v) == 1:
        return v[0][0]
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
                return (vv[0] + v[i + 1][0]) / 2
            idx -= vv[1]
        return None


def interquartile(n, x, f):
    v = [[x[i], f[i]] for i in range(len(x))]
    q2 = median_freq(v)
    lower = [vv for vv in v if vv[0] < q2]
    upper = [vv for vv in v if vv[0] > q2]
    q1 = median_freq(lower)
    q3 = median_freq(upper)
    print(q3 - q1)


def interquartile_v2(n, x, f):
    s = []
    for i in range(n):
        s += [x[i]] * f[i]
    pprint(s)
    N = sum(f)
    s.sort()
    if n % 2 != 0:
        q1 = median(s[:N // 2])
        q3 = median(s[N // 2 + 1:])
    else:
        q1 = median(s[:N // 2])
        q3 = median(s[N // 2:])
    print('%.1f' % (q3 - q1))


def binomial_coeff(n, k):
    if n == k:
        return 1
    elif k == 1:
        return n
    elif k > n:
        return 0
    else:
        num = math.factorial(n)
        denom = math.factorial(k) * math.factorial(n - k)
        return num // denom


def binomial_pmf(k, n, p):
    coeff = binomial_coeff(n, k)
    return coeff * (p**k) * ((1 - p)**(n - k))


if __name__ == '__main__':
    def_percent, batch = [int(__) for __ in input().split()]
    def_prob = def_percent / 100
    res = 0  # no more than 1
    for k in range(2):
        r = binomial_pmf(k, batch, def_prob)
        # print('%.3f' % r)
        res += r
    prob_2 = binomial_pmf(2, batch, def_prob)
    print('{0:0.3f}'.format(res + prob_2))
    print('{0:0.3f}'.format(1 - res))
