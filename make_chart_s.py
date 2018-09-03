#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os
import pandas as pd
import svgwrite

g_origin = [90, 405]
g_max = [790, 5]
g_dname = ''

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
    print 'KEY: %s'%df.keys()
    ll = df[0].values.tolist()
    print ll

    # prepare writing coordinates
    g_dname = ll[0]
    limit_y = int(ll[-1] / 5 + 1) *5
    print 'limit_y: %d'%limit_y
    step_y = (g_origin[1] - g_max[1]) / limit_y
    print 'step_y: %f'%step_y
    ll = ll[1:-4]
    item_cnt = len(ll)
    step_x = (g_max[0] - g_origin[0]) / item_cnt
    print 'step_x: %d'%step_x
    coords = []
    cur_x = g_origin[0]
    for i in xrange(item_cnt):
        cur_y = int(g_origin[1] - (step_y*ll[i]) +0.5)
        coords.append((cur_x, cur_y))
        cur_x += step_x

    # start writing svg
    out_fname = 'out.svg'
    dwg = svgwrite.Drawing(filename=out_fname, debug=True)
    glines = dwg.g(id='grid', stroke='gray')
    glines.add(dwg.line(start=(g_origin[0], g_max[1]), end=tuple(g_origin))) # xGrid
    glines.add(dwg.line(start=(g_max[0], g_origin[1]), end=tuple(g_origin))) # yGrid
    dwg.add(glines)
    data = dwg.g(id='data')
    pline = dwg.polyline(coords, stroke="blue", stroke_width="2", fill="none")
    data.add(pline)
    dwg.add(data)
    dwg.save()
    print('#### check output file: %s'%out_fname)

