#!/usr/bin/python3
import sys
import os
import glob

rl = lambda: sys.stdin.readline().strip()
I = lambda: int(rl())

n = I()
l = []
for i in range(n):
    l.append(rl())

TMP_DIR = './tmp'

try:
    os.mkdir(TMP_DIR)
except:
    pass
os.chdir(TMP_DIR)
for ll in l:
    os.system('youtube-dl -f 140 %s'%(ll))
    g = glob.glob('*.m4a')
    if len(g)<=0: continue
    os.system('ffmpeg -i \"%s\" \"%s.mp3\"'%(g[0],g[0]))
    print('renaming...')
    dest = os.path.join('..','%s.mp3'%g[0])
    os.rename('%s.mp3'%g[0], dest)
    os.remove(g[0])

os.chdir('..')
os.rmdir(TMP_DIR)
