# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     RE
   Description :
   Author :       #TUYI#
   date：          7/29/2019
-------------------------------------------------
"""
__author__ = '#TUYI#'

# import re
# filepath = '/Users/niklaus/Documents/OneDrive - Nanyang Technological University/dev/python/MILP/DDT_Inequ.txt'
# print(filepath)
# f = open(filepath,'r')
# result = list()
# for line in f.readlines():
#     print(line)
#     line = line.strip()
#     l = re.findall(r'An inequality \((.*)\) x \+ (.*) >= 0',line)
#     print(len(l))
#     if len(l):
#         print(l)
#         l = str(l).replace('(','')
#         l = str(l).replace(')','')
#         print(l)
#         l = ",".join(l)
#         msg ='(%s)' %l
#         result.append(msg)
#     else:
#         result.append(line)
# # print(result)
# f.close()                
# open('/Users/niklaus/Documents/OneDrive - Nanyang Technological University/dev/python/MILP/result.txt', 'w').write('%s' % '\n'.join(result))


import re
filepath = '/Users/niklaus/Documents/OneDrive - Nanyang Technological University/dev/python/MILP/DDT_Inequ.txt'
print(filepath)
f = open(filepath,'r')
result = []
for line in f.readlines():
    print(line)
    line = line.strip()
    l = re.findall(r'An inequality \((.*)\) x \+ (.*) >= 0',line)
    print(len(l))
    if len(l):
        print(l)
        l = str(l).strip()
        l = l.replace('(','')
        l = str(l).replace('\'','')
        l = str(l).replace(')','')
        l = l.replace('[','')
        l = l.replace(']','')

        print(l)
        # l = ",".join(l)
        msg ='(%s)' %l
        result.append(msg)
    else:
        result.append(line)
# print(result)
f.close()                
out = open('/Users/niklaus/Documents/OneDrive - Nanyang Technological University/dev/python/MILP/result.txt', 'w')
out.write('template = [\\\n')
out.write('%s' % ',\\\n'.join(result))
out.write(']')