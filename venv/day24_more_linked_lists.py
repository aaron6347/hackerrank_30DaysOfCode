"""day24_more_linked_lists.py
    Created by Aaron at 04-Oct-20"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
            p = Node(data)
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        cval = -1000000
        cur = prev = head
        while cur.next != None:
            if cval != cur.data:
                cval = cur.data
                prev = cur
                cur = cur.next
            else:
                prev.next = cur.next
                del cur
                cur = prev.next
        if cval == cur.data:
            prev.next = None
            del cur
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head);

# 6
# 1
# 2
# 2
# 3
# 3
# 4