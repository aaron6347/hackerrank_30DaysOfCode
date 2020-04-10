"""day17_more_exceptions.py
    Created by Aaron at 04-Apr-20"""
#Write your code here
class Calculator:
    def power(self, n, p):
        if n<0 or p<0:
            raise ValueError("n and p should be non-negative")
        return n**p

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)
# 4
# 3 5
# 2 4
# -1 -2
# -1 3