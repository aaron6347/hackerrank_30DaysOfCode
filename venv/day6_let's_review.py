"""day6_let's_review.py
    Created by Aaron at 24-Mar-20"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for _ in range(n):
    s=input()
    a=b=""
    for x in range(0,len(s),+2):
       a+=s[x:x+1]
       b+=s[x+1:x+2]
    print("{0} {1}".format(a,b))
# 2
# Hacker
# Rank