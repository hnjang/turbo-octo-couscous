from itertools import groupby
from pprint import pprint

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
    result =[
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

if __name__ == '__main__':
    print("Example:")
    print(house('''
0000000
##00##0
######0
##00##0
#0000#0
'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert house('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24

    assert house('''0000000000
#000##000#
##########
##000000##
0000000000
''') == 30

    assert house('''0000
0000
#000
''') == 1

    assert house('''0000
0000
''') == 0

    assert house('''
0##0
0000
#00#
''') == 12

    print("Coding complete? Click 'Check' to earn cool rewards!")

