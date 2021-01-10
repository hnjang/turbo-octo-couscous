#!/usr/bin/python

import sys
from pprint import pprint
import json

if 1>len(sys.argv):
    print('not enough args...')
    sys.exit(-1)

in_fname = sys.argv[1]
print('input file:%s'%in_fname)
with open(in_fname, 'r') as in_f:
    data = in_f.read()
    
decoded = json.loads(data)
contents = decoded['contents']
links = [__ for __ in contents if __['type']=='link']
comments = [__ for __ in contents if __['type']=='comment']

#pprint(contents)

out_fname = in_fname +'.dot'
with open(out_fname, 'w') as out_f:
    # Put links
    for ll in links:
        out_f.write('  %s -> %s\n'%(ll['nodes'][0], ll['nodes'][1]))
    out_f.write('\n#now, here is comments\n\n')
    for cc in comments:
        #cmt_node_name = unicode.join(u'', [cc['node'],'_cmt'])
        cmt_node_name = cc['node'] + '_cmt'
        out_f.write('  %s -> %s[arrowhead="none"]\n'%(cc['node'], cmt_node_name))
        out_f.write('  %s[label="%s"]\n'%(cmt_node_name, cc['comment']))
    
print('output file is created: %s'%out_fname)
