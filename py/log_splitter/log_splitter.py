#!/usr/bin/python3

import sys
import os
from itertools import chain
from pprint import pprint


def get_translation_table():
    '''
    non_printable = [
        chr(i) for i in range(ord('\t'))] + [
        chr(i) for i in range(ord('\r') + 1, 0x20)] + [
        chr(i) for i in range(0x80, 0x100)]
        '''
    non_printable = [
        chr(i) for i in chain(
            range(ord('\t')), range(ord('\r') +
                                    1, ord(' ')), range(0x80, 0x100))
    ]
    return str.maketrans('', '', ''.join(non_printable))


'''
def write_output_file(contents, base_fname, no):
    out_fname = base_fname + '.' + str(no)
    print('write_output_file: start to writing: ', out_fname)
    with open(out_fname, 'w') as out_f:
        out_f.write(contents)
'''


def get_output_file_holder(old_holder=None, idx=1, base_fname=None):
    if old_holder:
        old_holder['fp'].close()
        idx = old_holder['idx'] + 1
        base_fname = old_holder['base_fname']
    elif base_fname:
        pass
    else:
        # if you reach here, exceptional case
        return None

    out_fname = base_fname + '.' + str(idx)
    print('get_output_file_holder: opening for writing: ', out_fname)
    fp = open(out_fname, 'w')
    return {'idx': idx, 'fp': fp, 'base_fname': base_fname}


if len(sys.argv) < 2:
    print('not enough arguments')
    sys.exit(-1)

in_fname = sys.argv[1]
only_pp = False
try:
    only_pp = True if sys.argv[2] == 'only_pp' else False
except:
    pass
pp_fname = in_fname + '.pp'

remap = get_translation_table()

if os.path.exists(pp_fname):
    try:
        os.remove(pp_fname)
    except:
        print('L53. exception occurred')
        sys.exit(-1)

print('## start to writing pp file: ', pp_fname)
in_fsize = os.stat(in_fname).st_size
in_pos = 0
progress, old_progress = 0, 0
with open(in_fname, 'rb') as in_f, open(pp_fname, 'a') as pp_f:
    while True:
        in_data_b = in_f.read(128 * 1024)
        if len(in_data_b) == 0: break
        in_pos += len(in_data_b)
        progress = 10 * in_pos // in_fsize
        if progress > old_progress:
            print('progress: {}'.format(progress))
        old_progress = progress
        # convert bytes to string
        in_data = ''.join(map(chr, in_data_b))
        # print('type of in_data:', type(in_data))
        out_data = in_data.translate(remap)
        pp_f.write(out_data)

if only_pp:
    print('only_pp is ture.')
    sys.exit(0)

pp_fsize = os.stat(pp_fname).st_size
pp_pos = 0
progress, old_progress = 0, 0
#out_file_holder = {'no': 1, 'fp': None}
ofh = get_output_file_holder(base_fname=pp_fname)
with open(pp_fname) as pp_f:
    first_line = pp_f.readline()
    ofh['fp'].write(first_line)
    for l in pp_f:
        if 'Booting Linux on' in l:
            ofh = get_output_file_holder(ofh)
        ofh['fp'].write(l)
        pp_pos += len(l)
        progress = 10 * pp_pos // pp_fsize
        if progress > old_progress:
            print('progress: {}'.format(progress))
        old_progress = progress

ofh['fp'].close()
