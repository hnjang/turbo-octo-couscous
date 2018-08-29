#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os
import pandas as pd

g_origin = [90, 405]
g_max = [790, 5]
g_dname = ''

g_pline_sstr = \
'''<g class="data">
  <polyline
     fill="none"
     stroke="blue"
     stroke-width="2"
     points="
'''

g_pline_estr = '" /> </g>'

g_head_str = '''<svg version="1.2" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="graph" aria-labelledby="title" role="img">
  <style>
      <![CDATA[
.x-labels {  text-anchor: middle;}
.y-labels {  text-anchor: end;}
.graph {  height: 500px;  width: 800px;}
.grid {  stroke: #ccc;  stroke-dasharray: 0;  stroke-width: 1;}
.labels {  font-size: 13px;}
.label-title {  font-weight: bold;  text-transform: uppercase;  font-size: 12px;  fill: black;}
.data {  fill: blue;  stroke-width: 1;  }
      ]]>
  </style>
  <title id="title">A line chart showing some information</title>'''

g_tail_str = '\n</svg>'

def make_grid_str():
    grid_str = '''<g class="grid" id="xGrid">
  <line x1="%d" x2="%d" y1="%d" y2="%d"></line>
</g>
<g class="grid" id="yGrid">
  <line x1="%d" x2="%d" y1="%d" y2="%d"></line>
</g>'''%(g_origin[0], g_origin[0], g_max[1], g_origin[1],
        g_origin[0], g_max[0], g_origin[1], g_origin[1])
    return grid_str

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
    cur_x = g_origin[0]

    # start writing coordinates
    out_fname = 'out.svg'
    f = open(out_fname,'w')
    string = g_head_str
    string += make_grid_str()
    string += g_pline_sstr
    f.write( string )
    for i in xrange(item_cnt):
        cur_y = int(g_origin[1] - (step_y*ll[i]) +0.5)
        f.write( '%d, %d\n'%(cur_x, cur_y) )
        cur_x += step_x
    string = g_pline_estr
    string += g_tail_str
    f.write(string)
    f.close()
    print('#### check output file: %s'%out_fname)

