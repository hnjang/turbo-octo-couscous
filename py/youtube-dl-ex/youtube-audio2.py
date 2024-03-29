#!/usr/bin/python3
import sys
import os
import glob
from pprint import pprint

rl = lambda: sys.stdin.readline().strip()
I = lambda: int(rl())

n = rl()
if n==None or n=='' or n=='0':
    n = 987654321

print(n)
l = []
for i in range(n):
    t = rl()
    print('%d: %s'%(i,t))
    if t.startswith('https://youtu') or t.startswith('https://www.youtube'):
        l.append(t)
    else:
        break

print('Start download...')
pprint(l)

TMP_DIR = './tmp'

try:
    os.mkdir(TMP_DIR)
except:
    pass
os.chdir(TMP_DIR)
for ll in l:
    print('youtube-dl -f 140 %s'%(ll))
    os.system('youtube-dl  -f 140 %s'%(ll))
    g = glob.glob('*.m4a')
    if len(g)<=0: continue
    continue
    os.system('ffmpeg -i \"%s\" \"%s.mp3\"'%(g[0],g[0]))
    print('renaming...')
    dest = os.path.join('..','%s.mp3'%g[0])
    os.rename('%s.mp3'%g[0], dest)
    os.remove(g[0])

os.chdir('..')
os.rmdir(TMP_DIR)
