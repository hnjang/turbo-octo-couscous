#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os
import math, random
import numpy

g_low = 0
g_high = 100
g_mid = (g_low+g_high)/2
g_size = 50

def uniform(a,b,size):
    return [random.uniform(a,b) for x in xrange(size)]

def gaussian(m,sigma,size):
    return [random.gauss(m,sigma) for x in xrange(size)]

def gamma(a,b,size):
    return [random.gammavariate(a,b) for x in xrange(size)]

def write_table(fname, ds, data_name, raw_data=False):
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
                string += ',' +'%.4f'%(ds[i][j])
        string += ',' +'%.1f'%(numpy.mean(ds[i]))
        string += ',' +'%.1f'%(numpy.std(ds[i]))
        string += ',' +'%.1f'%(min(ds[i]))
        string += ',' +'%.1f'%(max(ds[i]))
        string += '\n'
        f.write(string)
    f.close()
    return

def make_table():
    print 'making a table...'
    # uniform distribution
    a = uniform(g_low, g_high, g_size)

    # gaussian dist
    b = gaussian(g_mid, 5, g_size)

    # gaussian dist (big sigma)
    c = gaussian(g_mid, 20, g_size)

    # gamma dist
    d = gamma(10, g_mid/10, g_size)

    ds = [a,b,c,d]
    data_name = ['uniform', 'gauss 1', 'gauss 2', 'gamma']

    out_fname = 'out.csv'
    write_table(out_fname, ds, data_name)
    print('#### check output file: %s'%out_fname)

    out_fname = 'out_all.csv'
    write_table(out_fname, ds, data_name, True)
    print('#### check output file: %s'%out_fname)

def make_series(mean=10, sigma=3):
    print 'making a series...'
    x = gaussian(mean, sigma, g_size)
    ds = [x]
    data_name = ['price']
    out_fname = 'out_all.csv'
    write_table(out_fname, ds, data_name, True)
    print('#### check output file: %s'%out_fname)

rl = lambda: sys.stdin.readline()
I = lambda: int(rl())

if __name__ == "__main__":
    random.seed()

    l_func = [
            make_series,
            make_table
            ]
    print 'Let\'s make some csv files with random-based values'
    print '1. Make a serise (gaussian)'
    print '2. Make a table'
    inp = I()
    if (inp<1 or inp>len(l_func)):
        print 'your input is out-of-bound. input:%d range:%d~%d'%(inp, 1, len(l_func))
        sys.exit(0)
    l_func[inp-1]()


