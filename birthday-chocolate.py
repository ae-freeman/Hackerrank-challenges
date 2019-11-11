#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    segments = 0

    for i in range(len(s)):
        sum = 0
        n = 0
        while(n < m):
            sum += s[i + n]
            n += 1
        if sum == d:
            segments += 1
        if (i + n) == len(s):
            break


    return segments

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])
