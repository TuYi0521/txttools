#coding=utf-8

import re
import sys


filepath = sys.argv[1]
outpath = filepath
# print(filepath)
f = open(filepath,'r')
result = list()
for line in f.readlines():
    line = line.strip()
    l = re.findall('.*title =        "(.*)"',line)
    if len(l):
        # print(l)
        l = "".join(l)
        msg ='title =        "{%s}",' %l
        result.append(msg)
    else:
        result.append(line)
# print(result)
f.close()                
open(outpath, 'w+').write('%s' % '\n'.join(result))

