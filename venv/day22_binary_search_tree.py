"""day22_binary_search_tree.py
    Created by Aaron at 04-Oct-20"""

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        #Write your code here
        lval = rval = 0
        if root.left != None:
            lval = self.getHeight(root.left) + 1
        if root.right != None:
            rval = self.getHeight(root.right) + 1
        return max(lval, rval)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)

# 7
# 3
# 5
# 2
# 1
# 4
# 6
# 7