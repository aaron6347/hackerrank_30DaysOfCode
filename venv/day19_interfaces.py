"""day19_interfaces.py
    Created by Aaron at 06-Apr-20"""
class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        # count=0
        # for x in range(1,n+1):
        #     if n%x==0:
        #         count+=x
        # return count
        return sum([x for x in range(1, n+1) if n%x==0])


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
# 6