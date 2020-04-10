"""day16_exceptions_string_to_integer.py
    Created by Aaron at 03-Apr-20"""
#!/bin/python3

import sys


S = input().strip()
try:
    print(int(S))
except ValueError:
    print('Bad String')
# za