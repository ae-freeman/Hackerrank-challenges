import sys

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

    def levelOrder(self,root):
        #Write your code here
        #if there is a root node:
        if root:
            queue = [root] #add that root to the queue to traverse
            while queue: #while there is at least one piece of data in queue
                node = queue.pop() #take off the first piece of data and traverse it
                print(node.data, end=" ") #print that node out
                if node.left: #if it has a left child, add that to the queue
                    queue.insert(0, node.left)
                if node.right: #if it has a right child, add that to the queue
                    queue.insert(0, node.right)


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
