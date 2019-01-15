import sys
from itertools import groupby
from pprint import pprint
from itertools import combinations
import math


def count_words(text: str, words: set) -> int:
    t_text = text.lower()
    cnt = 0
    for w in words:
        idx = t_text.find(w)
        if idx == -1: continue
        cnt += 1
        t_text.replace(w, '')
    return cnt


def long_repeat_old(line):
    if len(line) == 0: return 0
    t_line = line
    tokens = []
    while len(t_line) > 0:
        need_to_sep = False
        for i in range(len(t_line)):
            if t_line[i] != t_line[0]:
                need_to_sep = True
                break
        if not need_to_sep:
            tokens.append(t_line)
            break
        tokens.append(t_line[:i])
        t_line = t_line[i:]
    result = max([len(tt) for tt in tokens])
    return result


def long_repeat(line):
    if len(line) == 0: return 0
    ch = line[0]
    max_cnt = 1
    current = 1
    for l in line[1:]:
        if l == ch:
            current += 1
        else:
            max_cnt = max(max_cnt, current)
            current = 1
            ch = l
    max_cnt = max(max_cnt, current)

    return max_cnt


def two_teams(sailors):
    #replace this for solution
    print('entry')
    result = [
        sorted([k for k in sailors if sailors[k] < 20 or sailors[k] > 40]),
        sorted([k for k in sailors if sailors[k] >= 20 and sailors[k] <= 40])
    ]
    pprint(result)
    return result


def house(plan):
    p = [list(__) for __ in plan.split()]
    max_r, max_c = 0, 0
    min_r, min_c = 11, 11
    no_hash = True
    # pprint(p)
    for row in range(len(p)):
        if '#' in p[row]:
            max_r, min_r = max(max_r, row), min(min_r, row)
            no_hash = False
    if no_hash: return 0

    for col in range(len(p[0])):
        for row in range(len(p)):
            if '#' == p[row][col]:
                max_c, min_c = max(max_c, col), min(min_c, col)
                break
    area = (max_r - min_r + 1) * (max_c - min_c + 1)
    return area


def cms_search(ss, t, row, col):
    if row < 0 or col >= len(ss[row]):
        return (False, None)

    # print('t row col : ', t, row, col)
    for i, x in enumerate(ss[row][col:]):
        if x == t:
            return (True, i)
    for j, y in enumerate(range(row - 1, -1, -1)):
        if ss[y][col] == t:
            return (True, j + 1)
    (found, dist) = cms_search(ss, t, row - 1, col + 1)
    if not found: return (False, None)
    return (found, dist + 1)


def navigation(seaside):
    updown = list(reversed(seaside))
    leftright = [list(reversed(__)) for __ in seaside]
    lrud = list(reversed(leftright))
    sum_dist = 0
    for t in 'CMS':
        for idx, ss in enumerate([seaside, updown, leftright, lrud]):
            for r, row_ss in enumerate(ss):
                if 'Y' not in row_ss: continue
                for c, col_ss in enumerate(row_ss):
                    if 'Y' == col_ss:
                        start = (r, c)
            (found, dist) = cms_search(ss, t, start[0], start[1])
            if found:
                break
        sum_dist += dist
    return sum_dist


def stone_wall(wall):
    w = [__ for __ in wall.split()]
    lengths = []
    for i in range(len(w[0])):
        t = 0
        for j in range(len(w)):
            if w[j][i] == '#':
                t += 1
        lengths.append(t)
    # return lengths.index(min(lengths))
    return min(range(len(lengths)), key=lengths.__getitem__)


def find_shooting_line(c1, c2):
    if c1[0] == c2[0]:
        return (None, None)
    a = -(c2[1] - c1[1]) / (c2[0] - c1[0])
    b = a * c1[0] + c1[1]
    return (a, b)


def find_dogs_number(a, b, coords):
    cnt = 0
    for c in coords:
        if (a * c[0] + c[1]) == b:
            cnt += 1
    return cnt


def find_distance(a, b):
    # find the distance
    # eq: ax + y = b
    #     y = -ax -b
    # distance = abs(b) / math.hypot(1, a)
    # this can be derived easily
    return abs(b) / math.hypot(1, a)


def wild_dogs(coords):
    max_cnt = 0
    for dog_pair in combinations(coords, 2):
        (a, b) = find_shooting_line(*dog_pair)
        if a == None: continue
        cnt = find_dogs_number(a, b, coords)
        if max_cnt < cnt:
            max_cnt = cnt
            candidates = [(a, b)]
        elif max_cnt == cnt:
            candidates.append((a, b))

    result = float('inf')
    for ab in candidates:
        result = min(result, find_distance(ab[0], ab[1]))

    result = round(result, 2)
    print('result: ', result)
    return result


if __name__ == '__main__':
    print("Example:")
    print(
        wild_dogs([(7, 122), (8, 139), (9, 156), (10, 173), (11, 190), (-100,
                                                                        1)]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert wild_dogs([(7, 122), (8, 139), (9, 156), (10, 173), (11, 190),
                      (-100, 1)]) == 0.18

    assert wild_dogs([(6, -0.5), (3, -5), (1, -20)]) == 3.63

    assert wild_dogs([(10, 10), (13, 13), (21, 18)]) == 0
    print(wild_dogs([[10, 23], [4, 5], [7, 14], [10, 110]]))
    print("Coding complete? Click 'Check' to earn cool rewards!")
