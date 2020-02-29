#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the serviceLane function below.
def serviceLane(width, cases):

    max_widths = []

    for case in cases:
        max_width = 3
        for i in range(case[0], case[1] + 1):

            if width[i] < max_width:
                max_width = width[i]

        max_widths.append(max_width)

    return(max_widths)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(width, cases)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
