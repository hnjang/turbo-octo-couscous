#!/usr/bin/python3
import sys
import os
import glob
from pprint import pprint

rl = lambda: sys.stdin.readline().strip()
I = lambda: int(rl())

n = I()
l = []
for i in range(n):
    l.append(rl())

pprint(l)

TMP_DIR = './tmp'

try:
    os.mkdir(TMP_DIR)
except:
    pass
os.chdir(TMP_DIR)
for ll in l:
    print('youtube-dl \'bestvideo[height<=480]+bestaudio/best[height<=480]\' %s'%(ll))
    os.system('youtube-dl \'bestvideo[height<=480]+bestaudio/best[height<=480]\' %s'%(ll))
    g = glob.glob('*.m4a')
    if len(g)<=0: continue

os.chdir('..')
os.rmdir(TMP_DIR)
'''
https://askubuntu.com/questions/486297/how-to-select-video-quality-from-youtube-dl
https://github.com/ytdl-org/youtube-dl#user-content-format-selection-examples
'''
