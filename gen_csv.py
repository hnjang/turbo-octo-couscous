#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os
import math, random
import numpy

def uniform(a,b,size):
    return [random.uniform(a,b) for x in xrange(size)]

def gaussian(m,sigma,size):
    return [random.gauss(m,sigma) for x in xrange(size)]

def gamma(a,b,size):
    return [random.gammavariate(a,b) for x in xrange(size)]

def write_data(fname, ds, raw_data=False):
    f = open(fname,'w')
    size = len(ds[0])
    if size==0:
        print 'there is nothing to do. size==0!'
        return
    temp_array = [ str(__+1) for __ in xrange(size) ]
    f_line = '-,'
    if raw_data: f_line += ','.join(temp_array) +','
    f_line +='average,stdev,min,max\n'
    f.write(f_line)
    for i,s in enumerate(data_name):
        string = s
        if raw_data:
            for j in xrange(size):
                string += ',' +str(ds[i][j])
        string += ',' +'%.1f'%(numpy.mean(ds[i]))
        string += ',' +'%.1f'%(numpy.std(ds[i]))
        string += ',' +'%.1f'%(min(ds[i]))
        string += ',' +'%.1f'%(max(ds[i]))
        string += '\n'
        f.write(string)
    f.close()
    return

low = 0
high = 100
mid = (low+high)/2
size = 50
random.seed()

if __name__ == "__main__":
    # uniform distribution
    a = uniform(low, high, size)

    # gaussian dist
    b = gaussian(mid, 5, size)

    # gaussian dist (big sigma)
    c = gaussian(mid, 20, size)

    # gamma dist
    d = gamma(10, mid/10, size)

    ds = [a,b,c,d]
    data_name = ['uniform', 'gauss 1', 'gauss 2', 'gamma']

    out_fname = 'out.csv'
    write_data(out_fname, ds)
    print('#### check output file: %s'%out_fname)

    out_fname = 'out_all.csv'
    write_data(out_fname, ds, True)
    print('#### check output file: %s'%out_fname)

