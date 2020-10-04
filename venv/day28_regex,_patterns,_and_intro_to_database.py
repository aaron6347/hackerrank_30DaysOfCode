"""day28_regex,_patterns,_and_intro_to_database.py
    Created by Aaron at 04-Oct-20"""

# !/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    ar = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if bool(re.search(".@gmail.com$", emailID)):
            ar.append((firstName, emailID))

    for name, _ in sorted(ar):
        print(name)

# 6
# riya riya@gmail.com
# julia julia@julia.me
# julia sjulia@gmail.com
# julia julia@gmail.com
# samantha samantha@gmail.com
# tanya tanya@gmail.com