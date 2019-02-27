#!/usr/bin/python3

import sys
from pprint import pprint


def get_translation_table():
    non_printable = \
        [chr(i) for i in range(ord('\t'))] + \
        [chr(i) for i in range(ord('\r') + 1, 0x20)] +\
        [chr(i) for i in range(0x80, 0x100)]
    return str.maketrans('', '', ''.join(non_printable))


def write_output_file(contents, base_fname, no):
    out_fname = base_fname + '.' + str(no)
    print('write_output_file: start to writing: ', out_fname)
    with open(out_fname, 'w') as out_f:
        out_f.write(contents)


if len(sys.argv) < 2:
    print('not enough arguments')
    sys.exit(-1)

in_fname = sys.argv[1]
pp_fname = in_fname + '.pp'

no = 1

remap = get_translation_table()

with open(in_fname, 'rb') as in_f:
    in_data_b = in_f.read()
    # convert bytes to string
    in_data = ''.join(map(chr, in_data_b))
    print('type of in_data:', type(in_data))
    out_data = in_data.translate(remap)
    print('## start to writing pp file: ', pp_fname)
    with open(pp_fname, 'w') as pp_f:
        pp_f.write(out_data)

with open(pp_fname) as pp_f:
    first_line = pp_f.readline()
    contents = first_line
    for l in pp_f:
        if 'Booting Linux on' in l:
            write_output_file(contents, pp_fname, no)
            no += 1
            contents = l
            continue
        contents = contents + l

write_output_file(contents, pp_fname, no)
