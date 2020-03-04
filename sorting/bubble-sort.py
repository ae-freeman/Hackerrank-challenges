#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    num_swaps = 0

    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
                num_swaps += 1

    print("Array is sorted in", num_swaps, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[len(a) - 1])

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
