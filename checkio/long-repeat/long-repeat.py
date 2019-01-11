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


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('aa') == 2, "TC: aa"
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
