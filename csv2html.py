#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os
import pandas as pd


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
    if len(sys.argv)<2:
        print 'please specify input csv filename.'
        sys.exit(0)
    csv_fname = sys.argv[1]
    df = pd.read_csv(csv_fname)

    f = open('out.html','w')
    head_str = make_head_str(False)
    f.write(head_str)
    f.write( df.to_html() )
    f.write(tail_str)
    f.close()

