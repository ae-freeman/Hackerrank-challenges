#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    frequency = dict()

    for i in range(n):
        if ar[i] in frequency.keys():
            frequency[ar[i]] += 1
        else:
            frequency[ar[i]] = 1
    
    pairs = 0

    for i in frequency:
        number_pairs = frequency[i] // 2
        pairs = pairs + number_pairs

    return pairs



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
