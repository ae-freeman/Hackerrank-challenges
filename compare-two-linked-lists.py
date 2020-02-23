#!/bin/python3

import os
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):
    current_1 = llist1
    current_2 = llist2

    if current_1 == None and current_2 == None:
        return 0

    while current_1 != None and current_2 != None:
        if current_1.data != current_2.data:
            return 0

        if current_1.next == None and current_2.next == None:
            return 1

        current_1 = current_1.next
        current_2 = current_2.next

    return 0

if __name__ == '__main__':
