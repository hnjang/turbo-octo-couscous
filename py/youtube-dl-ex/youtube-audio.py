#!/usr/bin/python3
import sys
import os
import glob


def read_int(string=None):
    return int(input(string))

output_type = input()
if output_type not in ['def', 'mp3']:
    print('output_type is %s. something worng' % output_type)
    sys.exit(-1)
l = []
while True:
    inp = input()
    if inp=='end': break
    l.append(inp)

TMP_DIR = './tmp'

try:
    os.mkdir(TMP_DIR)
except:
    pass
os.chdir(TMP_DIR)
for ll in l:
    if len(ll)==0: break
    os.system('youtube-dl -f 140 %s'%(ll))
    g = glob.glob('*.m4a')
    if len(g)<=0: continue
    if output_type != 'mp3':
        src = g[0]
    else:
        os.system('ffmpeg -i \"%s\" \"%s.mp3\"'%(g[0],g[0]))
        dest = os.path.join('..','%s.mp3'%g[0])
        os.remove(g[0])
        src = '%s.mp3'%g[0]
    dest = os.path.join('..', src)
    os.rename(src, dest)

os.chdir('..')
os.rmdir(TMP_DIR)
