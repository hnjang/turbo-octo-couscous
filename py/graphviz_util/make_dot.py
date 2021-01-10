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
# set default value for 'group'
for cc in contents:
    #print(cc)
    #print(cc.get('group',''))
    cc['group'] = cc.get('group','')

links = [__ for __ in contents if __['group'] != 'comment']
comments = [__ for __ in contents if __['group']=='comment']

#pprint(contents)

out_fname = in_fname +'.dot'
with open(out_fname, 'w') as out_f:
    # Put head contents
    out_f.write('digraph {\n')
    
    # Put links
    for ll in links:
        if ll['type']=='link':
            out_f.write('  %s -> %s\n'%(ll['nodes'][0], ll['nodes'][1]))
        elif ll['type']=='switch':
            for i, ch in enumerate(ll['nodes'][1:]):
                out_f.write('  %s -> %s[label="%s"]\n'%(ll['nodes'][0], ch, ll['labels'][i]))
        elif ll['type']=='end-switch':
            for i, parent in enumerate(ll['nodes'][:-1]):
                out_f.write('  %s -> %s\n'%(parent, ll['nodes'][-1]))
        else:
            print('unrecognized type: %s.'%ll['type'])
            print('dump the element...')
            pprint(ll)
                
    out_f.write('\n#now, here are comments\n\n')
    for cc in comments:
        #cmt_node_name = unicode.join(u'', [cc['node'],'_cmt'])
        try:
            cmt_node_name = cc['node'] + '_cmt'
            out_f.write('  %s -> %s[arrowhead="none"]\n'%(cc['node'], cmt_node_name))
            out_f.write('  %s[label="%s"]\n'%(cmt_node_name, cc['comment']))
        except:
            print('exception! check if the element has values for "node", "comment".')
            print('dump the element...')
            pprint(cc)

    # Put tail contents
    out_f.write('}\n')

    
print('output file is created: %s'%out_fname)
