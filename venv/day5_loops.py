"""day5_loops.py
    Created by Aaron at 23-Mar-20"""
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    for x in range(1,11):
        print("{0} x {1} = {2}".format(n,x,n*x))
# 2