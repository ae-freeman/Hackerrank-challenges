#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):

    #find original number of chocolates to buy
    chocolates = math.floor(n/c)

    #get total -> recursive function
    total = chocolates + getExtras(chocolates)

    return total

def getExtras(chocolates):

    #how many he can buy with current wrappers
    extra_chocs = math.floor(chocolates/m)
    #how many wrappers he has left after 2nd purchase
    leftover_wrappers = chocolates % m

    #if second purchase wrappers and leftover wrappers can buy him at least one more chocolate, increase value
    #of extra_chocs by the result of the function being called again
    if extra_chocs + leftover_wrappers >= m:
        extra_chocs += getExtras(extra_chocs + leftover_wrappers)

    return extra_chocs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
