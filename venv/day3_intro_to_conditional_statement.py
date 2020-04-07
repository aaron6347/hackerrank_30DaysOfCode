"""day3_intro_to_conditional_statement.py
    Created by Aaron at 21-Mar-20"""
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    if N%2==1:
        print("Weird")
    elif N>1 and N<6:
        print("Not Weird")
    elif N>5 and N<21:
        print ("Weird")
    else:
        print("Not Weird")
# 3