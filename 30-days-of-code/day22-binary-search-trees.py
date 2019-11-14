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


#Write your code here
    def getHeight(self,root):
        if root: #(if a root exists, set left and right to 0)
            left = 0
            right = 0
            if root.left: #(if a left child exists, find height using recursive function)
                left = 1 + self.getHeight(root.left)
            if root.right:
                right = 1+ self.getHeight(root.right)
            return max(left, right) #(find the max from figuring out left and right heights)
        else:
            return 0


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)
