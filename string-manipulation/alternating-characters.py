#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):

    deletions = 0
    n = len(s)

    for l in range(n - 1):
        if s[l] == s[l + 1]:
            deletions += 1
            l += 1
    return deletions


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
