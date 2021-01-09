#!/usr/bin/python

import sys
import glob

target_path = '.\\'
g = glob.glob('.\\*.dot')
gout_fname = ['%s\\%s.svg' % (target_path, gg) for gg in g]
magick_out_fname = ['%s\\%s.png' % (target_path, gg) for gg in g]

for i, gg in enumerate(g):
    os.system('%s -Tsvg %s > %s' % (dot_bin, gg, gout_fname[i]))
print('SVG files are created')

for i , infile in enumerate(gout_fname):
    if not os.path.exists(magick_out_fname[i]):
        os.system('magick convert -density 600 %s %s'%infile, magick_out_fname[i])
    else:
        print('SKip converting(outfile exists: %s)'%magick_out_fname[i])
