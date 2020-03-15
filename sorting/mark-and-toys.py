#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    #sort prices from low to high
    prices.sort()

    total_cost = 0
    number_toys = 0
    #loop through prices adding them to a total, once it reaches k, break the loop
    for price in prices:
        total_cost += price
        if total_cost >= k:
            break
        number_toys += 1

    return number_toys




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
