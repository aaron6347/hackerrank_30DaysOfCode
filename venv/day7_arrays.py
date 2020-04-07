"""day7_arrays.py
    Created by Aaron at 25-Mar-20"""
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    print(*arr[::-1])
# 4
# 1 4 3 2