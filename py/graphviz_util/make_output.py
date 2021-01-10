#!/usr/bin/python

import sys
import os
import glob

conf = dict()
conf['dot_bin'] = r'D:\download\graphviz-2.44.1-win32\Graphviz\bin\dot.exe'

g = glob.glob('.\\*.dot')
gout_fname = ['.\\%s.svg' % (gg) for gg in g]
magick_out_fname = ['.\\%s.png' % (gg) for gg in g]

for i, gg in enumerate(g):
    os.system('%s -Tsvg %s > %s' % (conf['dot_bin'], gg, gout_fname[i]))
print('SVG files are created')

for i , infile in enumerate(gout_fname):
    if not os.path.exists(magick_out_fname[i]):
        os.system('magick convert -density 600 %s %s'%(infile, magick_out_fname[i]))
    else:
        print('Skip converting(outfile exists: %s)'%magick_out_fname[i])
