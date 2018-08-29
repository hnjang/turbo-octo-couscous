#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os
import pandas as pd
from svg.charts import line

if __name__ == "__main__":
    print 'Let\'s make a line chart (using svg.charts)'
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
    data_name = ll[0]
    ll = ll[1:-4]
    item_cnt = len(ll)

    fields = ['%d'%(x+1) for x in xrange(item_cnt)]
    lc = line.Line(dict(
        height = 800,
        width = 800,
        fields = fields,
	step_x_labels = 2,
	#min_scale_value = 20
	))
    lc.add_data({'data': ll, 'title': data_name})

    out_fname = 'out2.svg'
    f = open(out_fname,'w')
    f.write(lc.burn())
    f.close()
    print('#### check output file: %s'%out_fname)

