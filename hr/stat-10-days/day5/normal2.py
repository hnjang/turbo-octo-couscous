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


def geometry_pmf(n, p):
    return (1 - p)**(n - 1) * p


def ppoisson(k, l):
    return (l ** k) / (math.e ** l) / math.factorial(k)


def get_expected_cost(coeff, l):
    if len(coeff) != 3:
        return None
    return coeff[0] + coeff[1] * l + coeff[2] * (l + l**2)


def phi(x):
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0


def pnormal(m, s, v):
    v_norm = (v - m) / s
    return phi(v_norm)

if __name__ == '__main__':
    info = [float(__) for __ in input().split()]
    m, s = info[0], info[1]
    first = float(input())
    print('{0:0.2f}'.format(100 - 100*pnormal(m, s, first)))

    second = float(input())
    ans_3 = pnormal(m, s, second)
    ans_2 = 1 - ans_3
    print('{0:0.2f}'.format(ans_2 * 100))
    print('{0:0.2f}'.format(ans_3 * 100))

