#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os
import pandas as pd

g_origin = [90, 400]
g_max = [700, 5]
g_dname = ''

tail_str = \
'''
</body>
</html>
'''

def make_head_str(want_hl):
    hl_even_child_code = '''
tr:nth-child(even) {
    background-color: #dddddd;
}'''

    head_str_start = '''<!DOCTYPE html>
<html>
<head>
<style>
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
}

td, th {
    border: 1px solid #dddddd;
    text-align: right;
    padding: 8px;
}'''
    head_str_end = '''
</style>
</head>

<body>'''
    if want_hl:
        return head_str_start + hl_even_child_code + head_str_end
    else:
        return head_str_start + head_str_end

if __name__ == "__main__":
    print 'Let\'s make a line chart'
    if len(sys.argv)<2:
        print 'please specify input csv filename.'
        sys.exit(0)
    csv_fname = sys.argv[1]
    # read csv
    df = pd.read_csv(csv_fname)

    # convert it to a list
    df = df.transpose()
    print df
    print 'KEY: %s'%df.keys()
    ll = df[0].values.tolist()
    print ll

    # prepare writing coordinates
    g_dname = ll[0]
    step_y = (g_origin[1] - g_max[1]) / (ll[-1] - ll[-2])
    print 'step_y: %f'%step_y
    ll = ll[1:-4]
    item_cnt = len(ll)
    step_x = (g_max[0] - g_origin[0]) / item_cnt
    print 'step_x: %d'%step_x
    cur_x = g_origin[0]

    # start writing coordinates
    out_fname = 'out.svg'
    f = open(out_fname,'w')
    #head_str = make_head_str(False)
    for i in xrange(item_cnt):
        cur_y = int(g_origin[1] - (step_y*ll[i]) +0.5)
        f.write( '%d, %d\n'%(cur_x, cur_y) )
        cur_x += step_x

    #f.write(tail_str)
    f.close()
    print('#### check output file: %s'%out_fname)

