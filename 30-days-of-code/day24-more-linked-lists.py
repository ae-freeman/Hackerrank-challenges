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

        #Check if there are any nodes in list
        if not head:
            return None

        #Define current to be the the first pointer to keep track of where we are in list
        current = head

        #Whilst there is a pointer to another node, do this
        while current.next:

            #Check if the current node data is equal to the next node data
            if current.next.data == current.data:

                #If it is, define new to be the node two pointers away
                new = current.next.next

                #Delete the next data point
                current.next = None

                #Make pointer two away now the next pointer
                current.next = new
            #If the next data is different, then just go on to the next pointer, no changes
            else:
                current = current.next

         #return the head pointer of the now updated list
        return head







mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head); 
