"""day8_dictionaries_and_maps.py
    Created by Aaron at 26-Mar-20"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
dic={}
for _ in range(n):
    a,*b=map(str, input().split())
    dic[a]=b
while True:
    try:
        c=input()
        try:
            print("{0}={1}".format(c,*dic[c]))
        except KeyError:
            print("Not found")
    except EOFError:
        break
# 3
# sam 99912222
# tom 11122222
# harry 12299933
# sam
# edward
# harry