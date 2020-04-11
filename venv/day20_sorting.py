"""day20_sorting.py
    Created by Aaron at 07-Apr-20"""
#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
count=0
for x in range(len(a)):
    for y in range(len(a)-1):
        if a[y]> a[y+1]:
            a[y], a[y+1]=a[y+1],a[y]
            count+=1
    if count==0:
        break
print('Array is sorted in {} swaps.'.format(count))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[len(a)-1]))
# 3
# 3 2 1