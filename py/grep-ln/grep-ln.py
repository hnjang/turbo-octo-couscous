#!/usr/bin/python3

from collections import deque
import argparse


def search(lines, pattern, history=5):
    prev_lines = deque(maxlen=history)
    cnt = 0
    for no, line in enumerate(lines):
        if pattern in line:
            cnt += 1
            yield line, prev_lines, no, cnt
        prev_lines.append(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern")
    parser.add_argument("filename")
    parser.add_argument("-n", "--num", type=int, help="specify N", default=2)
    args = parser.parse_args()
    print('pattern: {}, filename: {}'.format(args.pattern, args.filename))
    with open(args.filename) as f:
        for line, prevlines, line_no, cnt in search(f, args.pattern, args.num):
            print('Line_no/idx: {}/{}'.format(line_no, cnt) + '-' * 20)
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
