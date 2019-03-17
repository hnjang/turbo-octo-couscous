#!/usr/bin/python3

import collections

def solution(v):
    print(v)
    xs = [vv[0] for vv in v]
    ys = [vv[1] for vv in v]
    cnt_x = collections.Counter(xs)
    cnt_y = collections.Counter(ys)
    answer = [min(cnt_x.items(), key=lambda x: x[1])[0],
            min(cnt_y.items(), key=lambda x: x[1])[0]]

    print('Hello Python')

    return answer

print(solution([[1, 4], [3, 4], [3, 10]]))
