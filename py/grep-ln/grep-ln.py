#!/usr/bin/python3

from collections import deque
import argparse

def search(lines, pattern, history=5):
    prev_lines = deque(maxlen=history)
    for no, line in enumerate(lines):
        if pattern in line:
            yield line, prev_lines, no
        prev_lines.append(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern")
    parser.add_argument("filename")
    args = parser.parse_args()
    '''if len(sys.argv) < 3:
        print('not enough argument')
        sys.exit(-1)
    pattern = sys.argv[1]
    fname = sys.argv[2]'''
    print('pattern: {}, filename: {}'.format(args.pattern, args.filename))
    with open(args.filename) as f:
        for line, prevlines, no in search(f, args.pattern, 2):
            print('Ln: {}'.format(no) + '-' * 20)
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
