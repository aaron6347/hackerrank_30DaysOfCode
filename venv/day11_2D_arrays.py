"""day11_2D_arrays.py
    Created by Aaron at 29-Mar-20"""
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(max([sum(arr[r][c:c+3])+arr[r+1][c+1]+sum(arr[r+2][c:c+3]) for r in range(4) for c in range(4)]))
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0