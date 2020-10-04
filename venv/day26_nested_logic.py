"""day_26_nested_logic.py
    Created by Aaron at 04-Oct-20"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
d1, m1, y1 = input().split(" ")
d2, m2, y2 = input().split(" ")
d1 = int(d1)
d2 = int(d2)
m1 = int(m1)
m2 = int(m2)
y1 = int(y1)
y2 = int(y2)
fine = 0
if y2 < y1 :
    fine += 10000
elif y2 == y1:
    if m2 < m1:
        fine += (500*(m1-m2))
    elif m2 == m1:
        if d2 < d1:
            fine += (15*(d1-d2))
print(fine)

# 9 6 2015
# 6 6 2015