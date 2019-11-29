#!/usr/bin/python3
import sys
import os
import glob
from pprint import pprint

rl = lambda: sys.stdin.readline().strip()
I = lambda: int(rl())

n = rl()
if n==None or n=='':
    n = 987654321
l = []
for i in range(n):
    t = rl()
    if 'https://youtu' in t:
        l.append(t)
    else:
        break

pprint(l)

TMP_DIR = './tmp'

try:
    os.mkdir(TMP_DIR)
except:
    pass
os.chdir(TMP_DIR)
for ll in l:
    print('youtube-dl -f 140 %s'%(ll))
    os.system('youtube-dl -f 140 %s'%(ll))
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
