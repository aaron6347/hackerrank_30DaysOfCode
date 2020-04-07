"""day10_binary_numbers.py
    Created by Aaron at 28-Mar-20"""
# !/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    print(max(map(len, str(format(n, 'b')).split('0'))))
# 5