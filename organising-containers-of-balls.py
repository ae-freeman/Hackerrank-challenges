#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    box_totals = []
    type_totals = []

    n = len(container)

    for i in range(n):
        box_total = 0
        for j in range(n):

            box_total += container[j][i]

        type_total = 0
        for k in range(n):

            type_total += container[i][k]

        box_totals.append(box_total)
        type_totals.append(type_total)

    box_totals.sort()
    type_totals.sort()

    if box_totals == type_totals:
        return "Possible"
    else:
        return "Impossible"




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
