"""day29_bitwise_and.py
    Created by Aaron at 04-Oct-20"""

# !/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        print(k - 1 if ((k - 1) | k) <= n else k - 2)

# 3
# 5 2
# 8 5
# 2 2