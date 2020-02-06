#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):

    minimum = -1
    min_list = []

    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] == a [j] and abs(j - i) > 0:
                min_list.append(abs(j - i))
    if(min_list):
        minimum = min(min_list)

    return minimum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
