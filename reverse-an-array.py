#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):

    #METHOD 1

    # a.reverse()
    # return a

    #METHOD 2
    #This method says go over the whole list (no start/stop), iterator is 1, so get all         of them, and start from the end because it is -1
    return a[::-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
