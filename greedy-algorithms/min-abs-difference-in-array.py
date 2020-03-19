#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):

    minimum = 1000000

    #Sort array - two numbers next to each other will have a smaller difference than         elsewhere in array.
    arr.sort()

    #Therefore, only need to look at current item at index and the one next to it
    for i in range(len(arr) - 1):
        difference = abs(arr[i] - arr[i + 1])

        minimum = min(minimum, difference)

    return minimum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
