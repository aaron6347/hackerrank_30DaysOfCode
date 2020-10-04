"""day25_running_time_and_complexity.py
    Created by Aaron at 04-Oct-20"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

runs = int(input())
for _ in range(runs):
    n = int(input())
    if n < 2:
        print("Not prime")
    elif n == 2:
        print("Prime")
    else:
        end = int(math.sqrt(n)+1)
        for x in range(2, end):
            if n%x == 0:
                print("Not prime")
                break
            elif n%x != 0 and  x == end-1:
                print("Prime")

# 3
# 12
# 5
# 7