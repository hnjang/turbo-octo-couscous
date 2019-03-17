#!/usr/bin/python3

from fractions import gcd
import math


def get_loss_block(big, small):
    print('get_loss_block: entry: big:{} small:{}'.format(big, small))
    loss = 0
    old = 1
    curr_big = big
    for i in range(small):
        curr = math.ceil(curr_big / small)
        loss += (curr - old + 1)
        # print('loss block: from {} to {}, {}'.format(old, curr, curr - old + 1))
        old = curr
        curr_big += big
    print('get_loss_block: curr_big:{}'.format(curr_big))
    print('get_loss_block: loss:{}'.format(loss))
    return loss


def get_loss_block_v2(big, small):
    loss = 0
    old = 1
    diff = big / small
    curr_f = 0
    for i in range(small):
        curr_f += diff
        curr = math.ceil(curr_f)
        loss += (curr - old + 1)
        old = curr
    return loss


def solution(w, h):
    print('start: {} {}'.format(w, h))
    div = gcd(w, h)
    print('div: {}'.format(div))
    ww = w // div
    hh = h // div

    if ww == 1 and hh == 1:
        loss = div
    else:
        loss = get_loss_block(max([ww, hh]), min([ww, hh])) * div

    answer = w * h - loss
    return answer


data = [[11, 100], [10, 21], [10, 19], [37, 63], [10, 90], [30, 70], [40, 60],
        [50, 50], [1, 15], [3, 15], [4, 15], [8, 12]]

data2 = [
    [85, 124],
    [854, 1245],
    [8545, 12452],
    [85456, 124525],
    [854565, 1245258],
    # [85456505, 94525854],
    [85456505, 100000000],
    [9999, 100000000],
    [10001, 100000000],
    # [9999999, 100000000],
    [10000001, 100000000],
    # [49999999, 100000000],
    [50000001, 100000000],
    # [99999999, 100000000],
    [100000000, 100000000]
]
data.extend(data2)
for d in data:
    print(solution(*d))
