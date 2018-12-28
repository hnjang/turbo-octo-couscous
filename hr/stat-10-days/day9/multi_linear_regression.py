#!/usr/bin/python3
import sys
import math
from pprint import pprint
import collections
from functools import cmp_to_key
from scipy import stats
import numpy as np
import statistics as st
from sklearn import linear_model


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
    return (l**k) / (math.e**l) / math.factorial(k)


def get_expected_cost(coeff, l):
    if len(coeff) != 3:
        return None
    return coeff[0] + coeff[1] * l + coeff[2] * (l + l**2)


def phi(x):
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0


def pnormal(m, s, v):
    v_norm = (v - m) / s
    return phi(v_norm)


def clt1():
    max_weight = int(input())
    nr_box = int(input())
    m_weight_box = int(input())
    s_weight_box = int(input())
    s_weight_sample = s_weight_box * (nr_box**0.5)
    # print('%d %f'%(m_weight_box * nr_box, s_weight_sample))
    print('{0:0.4f}'.format(
        pnormal(m_weight_box * nr_box, s_weight_sample, max_weight)))


def clt2():
    nr_ticket = int(input())
    nr_student = int(input())
    m_purchased = float(input())
    s_purchased = float(input())
    s_purchased_sample = s_purchased * (nr_student**0.5)
    print('{0:0.4f}'.format(
        pnormal(m_purchased * nr_student, s_purchased_sample, nr_ticket)))


def clt3():
    sample_size = int(input())
    m = int(input())
    s = int(input())
    range_percent = float(input())
    z = float(input())
    sd_sample = s / (sample_size**0.5)
    b = z * sd_sample + m
    a = (-z * sd_sample) + m
    print('{:0.2f}\n{:0.2f}'.format(a, b))


def clt3_spouy001():
    samples = float(input())
    mean = float(input())
    sd = float(input())
    interval = float(input())
    z = float(input())

    sd_sample = sd / (samples**0.5)
    print(round(mean - sd_sample * z, 2))
    print(round(mean + sd_sample * z, 2))


def pearson_ccoeff(x, y):
    m_x, m_y = st.mean(x), st.mean(y)
    s_x, s_y = st.pstdev(x), st.pstdev(y)
    acc = 0.0
    for i in range(len(x)):
        acc += (x[i] - m_x) * (y[i] - m_y)
    return acc / (len(x) * s_x * s_y)


def get_rank(X):
    x_rank = dict((x, i + 1) for i, x in enumerate(sorted(X)))
    return [x_rank[x] for x in X]


def spearman_rank_ccoeff(x, y):
    r_x, r_y = get_rank(x), get_rank(y)
    pprint(r_x)
    pprint(x)
    pprint(r_y)
    pprint(y)
    d2 = [(r_x[i] - r_y[i])**2 for i in range(len(x))]
    pprint(d2)
    pprint(sum(d2))
    return 1 - 6 * sum(d2) / (len(x) * (len(x)**2 - 1))


def predict_linear_model():
    xl, y = [], []
    for i in range(5):
        t = [int(__) for __ in input().split()]
        xl.append(t[0])
        y.append(t[1])
    x = np.asarray(xl).reshape(-1, 1)
    # print(x)
    lm = linear_model.LinearRegression()
    lm.fit(x, y)
    ret = lm.predict([[80]])
    print('{:0.3f}'.format(ret[0]))


def predict_linear_model_v2():
    size = 5
    x, y = [], []
    for i in range(size):
        t = [int(__) for __ in input().split()]
        x.append(t[0])
        y.append(t[1])
    mean_x, mean_y = st.mean(x), st.mean(y)
    x_squared = sum([xx**2 for xx in x])
    xy = sum([x[i]*y[i] for i in range(size)])
    b = (size*xy - sum(x)*sum(y)) / (size*x_squared - sum(x)**2)
    a = mean_y - b * mean_x
    print('{:0.3f}'.format(a+b*80))


def multi_regression():
    [m, n] = [int(__) for __ in input().split()]
    x = []
    y = []
    for i in range(n):
        tmp = [float(__) for __ in input().split()]
        x.append(tmp[:m])
        y.append(tmp[-1])
    lm = linear_model.LinearRegression()
    lm.fit(x, y)
    a = lm.intercept_
    b = lm.coef_
    # print (a, b[0], b[1])
    q = int(input())
    for i in range(q):
        new_x = [float(__) for __ in input().split()]
        ret = lm.predict([new_x])
        print('{:0.2f}'.format(ret[0]))


if __name__ == '__main__':
    multi_regression()
