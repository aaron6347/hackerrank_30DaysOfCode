"""day15_linked_list.py
    Created by Aaron at 02-Apr-20"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
    #Complete this method
        if head==None:
            head=Node(data)
        elif head.next==None:
            head.next=Node(data)
        else:
            self.insert(head.next, data)
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head);
# 4
# 2
# 3
# 4
# 1