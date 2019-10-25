#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):

    new_max = 0
    new_min = 0

    current_max = scores[0]
    current_min = scores[0]

    for i in range(len(scores)):
        if scores[i] > current_max:
            current_max = scores[i]
            new_max += 1
        elif scores[i] < current_min:
            current_min = scores[i]
            new_min += 1

    return new_max, new_min


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
