#!/usr/bin/env python

import sys, json

items = []
for line in open(sys.argv[1]).read().split('\n'):
    if line.startswith('#') or len(line) == 0:
        continue
    a = json.loads(line)
    items.append(a)
for it in items:
    if it[0] == 'RECORD':
        print('-'*50)
        for a in it:
            if type(a) == list and type(a[0]) == list:
                for _ in a:
                    print(' ', _)
            else:
                print(a)
#     for v in it:
#         if type(v) == list:
#             print('list', len(v))
#         else:
#             print(v)
